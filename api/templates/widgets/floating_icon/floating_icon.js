function togglePanel() {
  for (const _ of [
    ["main_nav_panel", "hide"],
    ["left", "show"],
  ]) {
    document.getElementById(_[0]).classList.toggle(_[1]);
  }
}
