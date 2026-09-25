module.exports = {
  content: ["_site/**/*.html", "_site/**/*.js"],
  css: ["_site/assets/css/*.css"],
  output: "_site/assets/css/",
  skippedContentGlobs: ["_site/assets/**/*.html"],
  // Keep attribute-selector rules (e.g. the PDF tag on a[href$=".pdf"]) in grouped lists.
  safelist: { greedy: [/doc-groups/] },
};
