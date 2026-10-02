(() => {
  "use strict";

  const trigger = document.getElementById("cmdbar-trigger");
  const overlay = document.getElementById("cmdbar-overlay");

  function openCmdbar() {
    if (!overlay) return;
    overlay.classList.add("is-open");
    const input = overlay.querySelector(".cmdbar-input");
    if (input) input.focus();
  }
  function closeCmdbar() {
    if (!overlay) return;
    overlay.classList.remove("is-open");
  }

  if (trigger) trigger.addEventListener("click", openCmdbar);
  if (overlay) {
    overlay.addEventListener("click", (e) => {
      if (e.target === overlay) closeCmdbar();
    });
  }
  document.addEventListener("keydown", (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
      e.preventDefault();
      openCmdbar();
    }
    if (e.key === "Escape") closeCmdbar();
  });
})();
