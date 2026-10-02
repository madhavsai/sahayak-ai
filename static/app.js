(() => {
  "use strict";

  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // ---- Today's date in hero ledger ----
  const todayEl = document.getElementById("ledger-today");
  if (todayEl) {
    todayEl.textContent = new Date().toLocaleDateString("en-IN", {
      day: "numeric", month: "short",
    });
  }

  // ---- Vertical toggle (construction / distribution) ----
  const toggleBtns = document.querySelectorAll(".toggle-btn");
  const demoMessages = {
    construction: {
      te: "Sir material vachindi, kaani fitting team inka site ki raledu",
      en: "(Sir, the material has arrived, but the fitting team hasn't reached the site yet)",
      entries: [
        ["Type", "Material delivery — flagged, team not on site"],
        ["Project", "Block C, Hyderabad site"],
        ["Action", "Task created for site supervisor, status: pending"],
        ["Logged", "Automatically, from WhatsApp — zero typing"],
      ],
    },
    distribution: {
      te: "Bhaiya 50 bags cement kal tak chahiye, stock hai kya",
      en: "(Need 50 bags of cement by tomorrow — do you have stock?)",
      entries: [
        ["Type", "New order request — 50 bags cement"],
        ["Customer", "Ramesh Traders"],
        ["Action", "Stock checked, order drafted, awaiting your confirm"],
        ["Logged", "Automatically, from WhatsApp — zero typing"],
      ],
    },
  };

  function setVertical(vertical) {
    toggleBtns.forEach((btn) => {
      const active = btn.dataset.vertical === vertical;
      btn.classList.toggle("is-active", active);
      btn.setAttribute("aria-selected", String(active));
    });

    document.querySelectorAll("[data-vertical-text]").forEach((el) => {
      el.hidden = el.dataset.verticalText !== vertical;
    });

    const bubble = document.getElementById("demo-bubble");
    const msg = demoMessages[vertical];
    if (bubble && msg) {
      bubble.querySelector(".chat-msg-te").textContent = msg.te;
      bubble.querySelector(".chat-msg-en").textContent = msg.en;
      bubble.dataset.verticalMsg = vertical;
    }
    resetDemo();
  }

  toggleBtns.forEach((btn) => {
    btn.addEventListener("click", () => setVertical(btn.dataset.vertical));
  });

  // ---- Chip fill for business type ----
  document.querySelectorAll(".chip[data-fill]").forEach((chip) => {
    chip.addEventListener("click", () => {
      const target = document.getElementById(chip.dataset.fill);
      if (target) target.value = chip.dataset.value;
    });
  });

  // ---- Select all three services ----
  const selectAllBtn = document.getElementById("select-all-services");
  if (selectAllBtn) {
    selectAllBtn.addEventListener("click", () => {
      document.querySelectorAll('input[name="services"]').forEach((cb) => (cb.checked = true));
    });
  }

  // ---- The one bold moment: message -> ledger ----
  const playBtn = document.getElementById("demo-play");
  const ledgerBody = document.getElementById("demo-ledger-body");
  const bubble = document.getElementById("demo-bubble");

  function resetDemo() {
    if (ledgerBody) {
      ledgerBody.innerHTML = '<p class="demo-ledger-empty">Waiting for the message to come through…</p>';
    }
    if (bubble) bubble.style.opacity = "1";
    if (playBtn) {
      playBtn.disabled = false;
      playBtn.textContent = "Watch it get logged →";
    }
  }

  function playDemo() {
    const vertical = document.querySelector(".toggle-btn.is-active")?.dataset.vertical || "construction";
    const entries = demoMessages[vertical].entries;
    if (!ledgerBody || !playBtn) return;

    playBtn.disabled = true;
    playBtn.textContent = "Logging…";
    ledgerBody.innerHTML = "";

    const delayUnit = prefersReducedMotion ? 0 : 420;

    entries.forEach((entry, i) => {
      setTimeout(() => {
        const row = document.createElement("div");
        row.className = "demo-ledger-entry";
        row.innerHTML = `<span class="dle-label">${entry[0]}</span><span class="dle-value">${entry[1]}</span>`;
        if (!prefersReducedMotion) {
          row.style.opacity = "0";
          row.style.transition = "opacity 260ms ease";
        }
        ledgerBody.appendChild(row);
        if (!prefersReducedMotion) {
          requestAnimationFrame(() => { row.style.opacity = "1"; });
        }
        if (i === entries.length - 1) {
          playBtn.textContent = "Logged — try again ↺";
          playBtn.disabled = false;
        }
      }, i * delayUnit);
    });
  }

  if (playBtn) {
    playBtn.addEventListener("click", () => {
      if (playBtn.textContent.includes("try again")) {
        resetDemo();
        return;
      }
      playDemo();
    });
  }

  // ---- Signup form ----
  const form = document.getElementById("signup-form");
  const statusEl = document.getElementById("form-status");

  if (form) {
    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      const submitBtn = document.getElementById("signup-submit");
      const services = Array.from(form.querySelectorAll('input[name="services"]:checked')).map((cb) => cb.value);

      if (services.length === 0) {
        statusEl.textContent = "Pick at least one service you'd use.";
        statusEl.className = "form-status is-error";
        return;
      }

      const payload = {
        name: form.name.value.trim(),
        contact: form.contact.value.trim(),
        business_type: form.business_type.value.trim(),
        services,
        wants_call: form.wants_call.checked,
      };

      submitBtn.disabled = true;
      submitBtn.textContent = "Sending…";
      statusEl.textContent = "";
      statusEl.className = "form-status";

      try {
        const res = await fetch("/api/signup", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload),
        });
        if (!res.ok) throw new Error("Request failed");
        statusEl.textContent = "Done — thank you. We'll be in touch.";
        statusEl.className = "form-status is-success";
        form.reset();
        submitBtn.textContent = "Get early access";
      } catch (err) {
        statusEl.textContent = "Something went wrong — please try again in a moment.";
        statusEl.className = "form-status is-error";
        submitBtn.textContent = "Get early access";
      } finally {
        submitBtn.disabled = false;
      }
    });
  }
})();
