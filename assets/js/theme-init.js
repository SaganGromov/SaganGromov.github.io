(() => {
  document.documentElement.classList.add("js");
  try {
    const saved = localStorage.getItem("geometry-notebook-theme");
    if (saved === "light" || saved === "dark") document.documentElement.dataset.theme = saved;
  } catch {
    // System preference remains the fallback.
  }
})();
