(() => {
  const root = document.documentElement;
  const themeButton = document.querySelector("[data-theme-button]");
  const menuButton = document.querySelector("[data-menu-button]");
  const nav = document.querySelector("[data-primary-nav]");
  const systemTheme = () =>
    window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  const currentTheme = () => (root.dataset.theme === "auto" ? systemTheme() : root.dataset.theme);

  const syncThemeButton = () => {
    if (!themeButton) return;
    const dark = currentTheme() === "dark";
    themeButton.dataset.current = dark ? "dark" : "light";
    themeButton.setAttribute(
      "aria-label",
      dark ? themeButton.dataset.lightLabel : themeButton.dataset.darkLabel,
    );
  };

  themeButton?.addEventListener("click", () => {
    const next = currentTheme() === "dark" ? "light" : "dark";
    root.dataset.theme = next;
    try {
      localStorage.setItem("geometry-notebook-theme", next);
    } catch {
      // The selected theme still applies to the current page.
    }
    syncThemeButton();
  });

  window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", () => {
    if (root.dataset.theme === "auto") syncThemeButton();
  });

  menuButton?.addEventListener("click", () => {
    const open = menuButton.getAttribute("aria-expanded") === "true";
    menuButton.setAttribute("aria-expanded", String(!open));
    nav?.classList.toggle("is-open", !open);
  });

  nav?.querySelectorAll("a").forEach((link) =>
    link.addEventListener("click", () => {
      menuButton?.setAttribute("aria-expanded", "false");
      nav.classList.remove("is-open");
    }),
  );

  const normalize = (text) =>
    text.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLocaleLowerCase();
  const search = document.querySelector("[data-library-search]");
  const items = [...document.querySelectorAll("[data-library-item]")];
  const count = document.querySelector("[data-filter-count]");
  const empty = document.querySelector("[data-library-empty]");

  search?.addEventListener("input", () => {
    const query = normalize(search.value.trim());
    let visible = 0;
    for (const item of items) {
      const matches = normalize(item.dataset.search).includes(query);
      item.hidden = !matches;
      if (matches) visible += 1;
    }
    if (count) count.textContent = query ? visible + " / " + items.length : "";
    if (empty) empty.hidden = visible !== 0;
  });

  document.querySelectorAll("[data-year]").forEach((node) => {
    node.textContent = String(new Date().getFullYear());
  });
  syncThemeButton();
})();
