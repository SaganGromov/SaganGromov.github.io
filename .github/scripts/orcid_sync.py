#!/usr/bin/env python3
"""Compare the works listed on /pesquisa/ with the public ORCID record.

ORCID only lets member organizations write to records (Member API), so this
script cannot push works itself. It does the rest: it reads the site, reads
the public ORCID record, finds works missing from ORCID, fetches their
metadata from DataCite (arXiv DOIs) or Crossref (journal DOIs), and writes a
BibTeX file ready for ORCID's "Add works > Import BibTeX".

ORCID's BibTeX importer has no entry type that maps to "Preprint"
(bibToWorkTypeMap in ORCID/orcid-angular sends @misc and @unpublished to
"Other"), and DataCite's claim service maps arXiv's resourceTypeGeneral
"Preprint" to "Other" as well. After importing, set each preprint's
Work type to "Preprint" by hand.

Exit status: 0 if ORCID lists every work on the site, 1 if some are missing,
2 on a fetch or parse error. Standard library only.
"""

import argparse
import html
import json
import re
import sys
import unicodedata
import urllib.parse
import urllib.request
from pathlib import Path

ORCID_ID = "0009-0001-5658-7467"
SITE_PAGE = Path(__file__).resolve().parents[2] / "_pages" / "pesquisa.md"
UA = "orcid-sync/1.0 (https://sagangromov.github.io; mailto:matheus.andrade5488@gmail.com)"


def get_json(url):
    req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def norm_title(t):
    t = unicodedata.normalize("NFKD", html.unescape(t)).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", t.lower())


def norm_arxiv(v):
    v = v.lower().strip()
    v = re.sub(r"^(https?://arxiv\.org/(abs|pdf)/|arxiv:|10\.48550/arxiv\.)", "", v)
    return re.sub(r"v\d+$", "", v)


def site_works(page_html):
    """One entry per <li>: title, section, DOIs and arXiv ids found in its links."""
    works, section = [], None
    for chunk in re.split(r"(<h2[^>]*>.*?</h2>|<li>)", page_html, flags=re.S):
        m = re.match(r"<h2[^>]*>(.*?)</h2>", chunk, flags=re.S)
        if m:
            section = m.group(1).strip()
            continue
        t = re.search(r'<div class="title">(?:<a[^>]*>)?(.*?)(?:</a>)?</div>', chunk, flags=re.S)
        if not t:
            continue
        hrefs = re.findall(r'href="([^"]+)"', chunk)
        dois = {
            urllib.parse.unquote(h.split("doi.org/", 1)[1]).lower()
            for h in hrefs
            if "doi.org/10." in h
        }
        arxiv = {norm_arxiv(h) for h in hrefs if re.search(r"arxiv\.org/abs/", h)}
        works.append(
            {"title": html.unescape(re.sub(r"<[^>]+>", "", t.group(1))).strip(),
             "section": section, "dois": dois, "arxiv": arxiv}
        )
    return works


def orcid_works(orcid_id):
    data = get_json(f"https://pub.orcid.org/v3.0/{orcid_id}/works")
    dois, arxiv, titles = set(), set(), set()
    for group in data.get("group", []):
        for s in group.get("work-summary", []):
            titles.add(norm_title(s["title"]["title"]["value"]))
            for e in (s.get("external-ids") or {}).get("external-id", []):
                typ, val = e["external-id-type"], e["external-id-value"]
                if typ == "doi":
                    dois.add(val.lower())
                    if val.lower().startswith("10.48550/arxiv."):
                        arxiv.add(norm_arxiv(val))
                elif typ == "arxiv":
                    arxiv.add(norm_arxiv(val))
    return dois, arxiv, titles


def in_orcid(w, orcid):
    dois, arxiv, titles = orcid
    return bool(w["dois"] & dois or w["arxiv"] & arxiv or norm_title(w["title"]) in titles)


def bib_escape(s):
    return s.replace("{", "").replace("}", "").strip()


def bib_entry(w):
    """BibTeX from registry metadata, not from the page, so names and dates are authoritative."""
    if w["dois"]:
        doi = sorted(w["dois"])[0]
        m = get_json(f"https://api.crossref.org/works/{urllib.parse.quote(doi)}")["message"]
        authors = [f'{a.get("family", "")}, {a.get("given", "")}'.strip(", ") for a in m.get("author", [])]
        year = m.get("issued", {}).get("date-parts", [[None]])[0][0]
        fields = {
            "title": m["title"][0],
            "author": " and ".join(authors),
            "journal": (m.get("container-title") or [""])[0],
            "volume": m.get("volume", ""),
            "number": m.get("issue", ""),
            "pages": m.get("page") or m.get("article-number", ""),
            "year": str(year or ""),
            "doi": doi,
            "url": f"https://doi.org/{doi}",
        }
        if w["arxiv"]:
            fields["eprint"] = sorted(w["arxiv"])[0]
            fields["archiveprefix"] = "arXiv"
        kind, key = "article", doi
    else:
        aid = sorted(w["arxiv"])[0]
        doi = f"10.48550/arXiv.{aid}"
        a = get_json(f"https://api.datacite.org/dois/{doi}")["data"]["attributes"]
        fields = {
            "title": a["titles"][0]["title"],
            "author": " and ".join(c["name"] for c in a["creators"]),
            "year": str(a.get("publicationYear", "")),
            "eprint": aid,
            "archiveprefix": "arXiv",
            "howpublished": f"arXiv preprint arXiv:{aid}",
            "doi": doi,
            "url": f"https://arxiv.org/abs/{aid}",
        }
        kind, key = "misc", f"arXiv:{aid}"
    body = ",\n".join(f"  {k} = {{{bib_escape(v)}}}" for k, v in fields.items() if v)
    return f"@{kind}{{{re.sub(r'[^A-Za-z0-9:.]', '_', key)},\n{body}\n}}\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--page", type=Path, default=SITE_PAGE, help="site page to read (default: _pages/pesquisa.md)")
    ap.add_argument("--orcid", default=ORCID_ID)
    ap.add_argument("--bib", type=Path, help="write BibTeX for the missing works here")
    ap.add_argument("--summary", type=Path, help="append a Markdown report here (e.g. $GITHUB_STEP_SUMMARY)")
    args = ap.parse_args()

    try:
        works = site_works(args.page.read_text(encoding="utf-8"))
        if not works:
            raise ValueError(f"no works parsed from {args.page}; did the page markup change?")
        orcid = orcid_works(args.orcid)
        missing = [w for w in works if not in_orcid(w, orcid)]
        entries = [bib_entry(w) for w in missing]
    except Exception as e:  # network, JSON, or markup change: fail loudly, never report "in sync"
        print(f"error: {e}", file=sys.stderr)
        return 2

    lines = [f"ORCID {args.orcid}: {len(works) - len(missing)}/{len(works)} site works present."]
    for w in missing:
        lines.append(f"- MISSING [{w['section']}] {w['title']}")
    report = "\n".join(lines)
    print(report)

    if args.bib and entries:
        args.bib.write_text("\n".join(entries), encoding="utf-8")
        print(f"\nBibTeX for {len(entries)} work(s) written to {args.bib}.")
        print("Import: https://orcid.org/my-orcid > Works > + Add > Import BibTeX,")
        print('then edit each imported @misc work and set Work type to "Preprint".')
    if args.summary:
        with args.summary.open("a", encoding="utf-8") as f:
            f.write("## ORCID sync\n\n```\n" + report + "\n```\n")
            if entries:
                f.write("\nDownload the `orcid-missing-bib` artifact and import it at "
                        "https://orcid.org/my-orcid (Works > + Add > Import BibTeX), then set "
                        "each preprint's Work type to Preprint (BibTeX import makes them Other).\n")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
