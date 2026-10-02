(() => {
  "use strict";

  function wireDropdown(btnId, panelId) {
    const btn = document.getElementById(btnId);
    const panel = document.getElementById(panelId);
    if (!btn || !panel) return;
    btn.addEventListener("click", (e) => {
      e.stopPropagation();
      const willOpen = panel.hidden;
      document.querySelectorAll(".dropdown-panel").forEach((p) => { p.hidden = true; });
      panel.hidden = !willOpen;
    });
  }

  wireDropdown("lang-pill-btn", "lang-dropdown");
  wireDropdown("notif-btn", "notif-dropdown");
  wireDropdown("user-pill-btn", "user-dropdown");

  document.addEventListener("click", () => {
    document.querySelectorAll(".dropdown-panel").forEach((p) => { p.hidden = true; });
  });

  document.querySelectorAll("#lang-dropdown .dropdown-item").forEach((item) => {
    item.addEventListener("click", (e) => {
      e.stopPropagation();
      document.getElementById("lang-pill-btn").textContent = item.dataset.lang;
      document.getElementById("lang-dropdown").hidden = true;
    });
  });
})();
