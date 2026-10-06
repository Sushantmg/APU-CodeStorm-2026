/* APU CodeStorm 2026 - shared scripts (navigation, filters, forms, gallery, dashboard) */
(function () {
  "use strict";

  var $ = function (sel, ctx) { return (ctx || document).querySelector(sel); };
  var $$ = function (sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); };

  /* ---------- Mobile navigation ---------- */
  var toggle = $(".nav-toggle");
  var nav = $("#primary-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(open));
      toggle.textContent = open ? "\u2715" : "\u2630";
    });
  }

  /* ---------- Active link highlight ---------- */
  var page = (location.pathname.split("/").pop() || "index.html").toLowerCase();
  $$("#primary-nav a, .footer-nav a").forEach(function (a) {
    if (a.getAttribute("href") && a.getAttribute("href").toLowerCase() === page) {
      a.classList.add("active");
      a.setAttribute("aria-current", "page");
    }
  });

  /* ---------- Footer year ---------- */
  $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------- Countdown ---------- */
  var cd = $("[data-countdown]");
  if (cd) {
    var target = new Date(cd.getAttribute("data-countdown")).getTime();
    var tick = function () {
      var diff = Math.max(0, target - Date.now());
      var d = Math.floor(diff / 86400000);
      var h = Math.floor(diff / 3600000) % 24;
      var m = Math.floor(diff / 60000) % 60;
      var s = Math.floor(diff / 1000) % 60;
      var parts = { days: d, hours: h, minutes: m, seconds: s };
      Object.keys(parts).forEach(function (k) {
        var node = cd.querySelector('[data-unit="' + k + '"]');
        if (node) { node.textContent = String(parts[k]).padStart(2, "0"); }
      });
    };
    tick();
    setInterval(tick, 1000);
  }

  /* ---------- Generic tabs ---------- */
  $$("[data-tabs]").forEach(function (group) {
    var buttons = $$(".tab-btn", group);
    var panels = $$(".tab-panel", group);
    buttons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        buttons.forEach(function (b) { b.setAttribute("aria-selected", "false"); });
        panels.forEach(function (p) { p.hidden = true; });
        btn.setAttribute("aria-selected", "true");
        var panel = $("#" + btn.getAttribute("aria-controls"));
        if (panel) { panel.hidden = false; }
      });
    });
  });

  /* ---------- Schedule / activity filters ---------- */
  $$("[data-filter-group]").forEach(function (bar) {
    var targetSel = bar.getAttribute("data-filter-group");
    var items = $$("[data-filter-item]");
    $$(".filter-btn", bar).forEach(function (btn) {
      btn.addEventListener("click", function () {
        $$(".filter-btn", bar).forEach(function (b) { b.classList.remove("is-active"); });
        btn.classList.add("is-active");
        var key = btn.getAttribute("data-filter");
        var shown = 0;
        items.forEach(function (item) {
          var match = key === "all" ||
            (item.getAttribute("data-tags") || "").split(" ").indexOf(key) !== -1;
          item.hidden = !match;
          if (match) { shown++; }
        });
        var counter = $("#filter-count");
        if (counter) { counter.textContent = shown + " item(s) shown"; }
      });
    });
  });

  /* ---------- Downloadable calendar (.ics) ---------- */
  var icsBtn = $("#download-calendar");
  if (icsBtn) {
    icsBtn.addEventListener("click", function (e) {
      e.preventDefault();
      var lines = [
        "BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//APU CodeStorm 2026//EN",
        "CALSCALE:GREGORIAN", "X-WR-CALNAME:APU CodeStorm 2026"
      ];
      $$("[data-event]").forEach(function (row, i) {
        var start = row.getAttribute("data-start");
        var end = row.getAttribute("data-end");
        var title = (row.querySelector("h4") || {}).textContent || "CodeStorm Session";
        var loc = row.getAttribute("data-venue") || "APU Cyberjaya Campus";
        var desc = (row.querySelector("p") || {}).textContent || "APU CodeStorm 2026";
        lines = lines.concat([
          "BEGIN:VEVENT",
          "UID:codestorm2026-" + i + "@apu.edu.my",
          "DTSTAMP:" + stamp(new Date()),
          "DTSTART:" + start,
          "DTEND:" + end,
          "SUMMARY:" + title.trim(),
          "LOCATION:" + loc,
          "DESCRIPTION:" + desc.trim().replace(/\s+/g, " "),
          "END:VEVENT"
        ]);
      });
      lines.push("END:VCALENDAR");
      download("codestorm-2026-schedule.ics", lines.join("\r\n"), "text/calendar");
    });
  }

  function stamp(d) {
    return d.toISOString().replace(/[-:]/g, "").replace(/\.\d{3}/, "");
  }

  function download(name, content, type) {
    var blob = new Blob([content], { type: type + ";charset=utf-8" });
    var url = URL.createObjectURL(blob);
    var a = document.createElement("a");
    a.href = url;
    a.download = name;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    setTimeout(function () { URL.revokeObjectURL(url); }, 1500);
  }
  $$("[data-download-text]").forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      e.preventDefault();
      download(btn.getAttribute("data-download-name") || "codestorm-file.txt",
        btn.getAttribute("data-download-text"), "text/plain");
    });
  });

  /* ---------- Gallery lightbox ---------- */
  var lightbox = $("#lightbox");
  if (lightbox) {
    var caption = $(".lightbox__caption", lightbox);
    var img = $(".lightbox__img", lightbox);
    var closeBtn = $(".lightbox__close", lightbox);
    var open = function (src, alt) {
      img.src = src;
      img.alt = alt;
      caption.textContent = alt;
      lightbox.classList.add("is-open");
      lightbox.setAttribute("aria-hidden", "false");
      closeBtn.focus();
    };
    var close = function () {
      lightbox.classList.remove("is-open");
      lightbox.setAttribute("aria-hidden", "true");
    };
    $$(".gallery-item").forEach(function (item) {
      item.addEventListener("click", function () {
        var thumb = item.querySelector("img");
        open(thumb.getAttribute("data-full") || thumb.src, thumb.alt);
      });
      item.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); item.click(); }
      });
    });
    closeBtn.addEventListener("click", close);
    lightbox.addEventListener("click", function (e) {
      if (e.target === lightbox) { close(); }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { close(); }
    });
  }

  /* ---------- Client-side form validation ---------- */
  function setError(field, message) {
    var wrap = field.closest(".field") || field.closest("fieldset");
    if (!wrap) { return; }
    var box = wrap.querySelector(".error");
    wrap.classList.toggle("is-invalid", Boolean(message));
    if (box) { box.textContent = message || ""; }
  }

  $$("form[data-validate]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var ok = true;
      $$("input, select, textarea", form).forEach(function (field) {
        if (field.type === "radio") { return; }
        var value = (field.value || "").trim();
        if (field.required && !value) {
          setError(field, "This field is required.");
          ok = false;
        } else if (field.type === "email" && value && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(value)) {
          setError(field, "Enter a valid e-mail address.");
          ok = false;
        } else if (field.minLength && value && value.length < field.minLength) {
          setError(field, "Must be at least " + field.minLength + " characters.");
          ok = false;
        } else {
          setError(field, "");
        }
      });
      var checks = $$('input[type="checkbox"][required]', form);
      checks.forEach(function (c) {
        if (!c.checked) {
          ok = false;
          var hint = c.closest(".field, .check");
          if (hint) {
            var box = hint.querySelector(".error");
            if (box) { box.textContent = "Please accept this to continue."; }
          }
        }
      });

      var result = $(".form-result", form);
      if (!ok) {
        if (result) {
          result.hidden = false;
          result.className = "alert alert--error form-result";
          result.textContent = "Please correct the highlighted fields and try again.";
        }
        var firstBad = $(".is-invalid input, .is-invalid select, .is-invalid textarea", form);
        if (firstBad) { firstBad.focus(); }
        return;
      }

      if (result) {
        result.hidden = false;
        result.className = "alert alert--ok form-result";
        result.innerHTML = "<strong>Submitted successfully.</strong> " +
          (form.getAttribute("data-success") ||
            "A confirmation e-mail will be sent to you within 2 working days.");
      }
      form.reset();
      var rating = form.querySelector("[data-stars]");
      if (rating) { setStars(0); }
    });

    $$("input, select, textarea", form).forEach(function (field) {
      field.addEventListener("input", function () { setError(field, ""); });
    });
  });

  /* ---------- Star rating ---------- */
  var starWrap = $("[data-stars]");
  if (starWrap) {
    var starButtons = $$("button", starWrap);
    var current = 0;
    var setStars = function (n) {
      current = n;
      starButtons.forEach(function (b, i) { b.classList.toggle("is-on", i < n); });
      var input = $("#rating-value");
      if (input) { input.value = String(n); }
      var label = $("#rating-label");
      if (label) {
        label.textContent = n === 0 ? "No rating selected" :
          n + " out of 5 - " + ["", "Poor", "Fair", "Good", "Very good", "Excellent"][n];
      }
    };
    starButtons.forEach(function (b, i) {
      b.addEventListener("click", function () { setStars(i + 1); });
      b.addEventListener("mouseenter", function () {
        starButtons.forEach(function (x, j) { x.classList.toggle("is-on", j <= i); });
      });
      b.addEventListener("mouseleave", function () { setStars(current); });
    });
    setStars(0);
  }

  /* ---------- Login / dashboard (front-end demo with localStorage) ---------- */
  var loginForm = $("#login-form");
  if (loginForm) {
    loginForm.addEventListener("submit", function (e) {
      e.preventDefault();
      var email = $("#login-email");
      var pass = $("#login-password");
      var result = $(".form-result", loginForm);
      var valid = email.value.trim() && /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email.value) &&
        pass.value.length >= 4;
      if (!valid) {
        result.hidden = false;
        result.className = "alert alert--error form-result";
        result.textContent = "Enter a valid e-mail and a password of at least 4 characters.";
        return;
      }
      var user = { email: email.value.trim(), since: new Date().toISOString() };
      try { localStorage.setItem("codestorm-user", JSON.stringify(user)); } catch (err) { /* storage blocked */ }
      result.hidden = false;
      result.className = "alert alert--ok form-result";
      result.textContent = "Login successful. Redirecting to your dashboard...";
      setTimeout(function () { location.href = "dashboard.html"; }, 700);
    });
  }

  var dashUser = $("#dash-user");
  if (dashUser) {
    var stored = null;
    try { stored = JSON.parse(localStorage.getItem("codestorm-user") || "null"); } catch (err) { stored = null; }
    var name = stored && stored.email ? stored.email.split("@")[0] : "Guest Hacker";
    dashUser.textContent = name;
    var logout = $("#logout-btn");
    if (logout) {
      logout.addEventListener("click", function () {
        try { localStorage.removeItem("codestorm-user"); } catch (err) { /* ignore */ }
        location.href = "login.html";
      });
    }
  }

  /* ---------- Back to top ---------- */
  var toTop = $(".to-top");
  if (toTop) {
    window.addEventListener("scroll", function () {
      toTop.classList.toggle("is-visible", window.scrollY > 420);
    }, { passive: true });
    toTop.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  /* ---------- Sponsor / stats reveal on scroll ---------- */
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.style.opacity = "1";
          entry.target.style.transform = "none";
          io.unobserve(entry.target);
        }
      });
    }, { threshold: .15 });
    $$(".card, .stat, .person").forEach(function (el) {
      el.style.opacity = "0";
      el.style.transform = "translateY(14px)";
      el.style.transition = "opacity .5s ease, transform .5s ease";
      io.observe(el);
    });
  }
})();
