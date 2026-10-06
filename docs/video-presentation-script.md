# Video Presentation Script - APU CodeStorm 2026 (MP4, target 4-5 minutes)

Record with any screen recorder (OBS, Zoom, PowerPoint/Keynote export). Export to **MP4 (H.264)**,
1920x1080, and upload to Moodle.

## Before recording
- Close chat apps, open `website/index.html` in full-screen browser window.
- Prepare tabs: Home, Schedule (with the .ics download clicked), Register, Gallery (lightbox open), Contact (map).
- Mic check: speak 10 cm from the mic, record 10 seconds of silence-free audio as a test.

---

### 0:00 - 0:25 | Title and team
**Screen:** cover slide (team names, IDs, intake, subject, project title).
**Say:** "Hello, we are team [team name] with [member names]. This is our CT053-3-1 group assignment:
APU CodeStorm 2026 - a fully client-side event website for an imaginary interfaculty hackathon,
built with HTML, CSS and JavaScript only, with no backend."

### 0:25 - 1:10 | Home page + concept
**Screen:** `index.html`, scroll slowly from hero to footer.
**Say:**
- The concept: a 48-hour interfaculty hackathon, 6 tracks, RM 20,000 in prizes.
- Point out the hero, live countdown (data-driven), quick navigation cards, track cards.
- Mention multimedia: the WAV anthem player and the animated GIF highlight reel.
- Close with the shared footer: contact details, quick links, participant links.

### 1:10 - 1:55 | Schedule - filters and calendar export
**Screen:** `schedule.html`.
**Do:** click Day 1, then Clinics, then All sessions; click **Download calendar (.ics)** and open the file.
**Say:** "The programme is filterable by day and session type using data attributes, so no page reload
is needed. The same rows generate a valid iCalendar file entirely in the browser - no server involved."

### 1:55 - 2:35 | Registration - form validation
**Screen:** `register.html`.
**Do:** submit an empty form (show inline errors), then fill it correctly and submit (show success alert).
**Say:** "One form covers participants, volunteers and audience. Validation runs client-side: required
fields, e-mail format, minimum length and the rules checkbox. Errors appear beside the field and focus
moves to the first problem; success is announced in a live region."

### 2:35 - 3:10 | Gallery, activities and interaction
**Screen:** `gallery.html` then `activities.html`.
**Do:** open a lightbox image, close with Escape; on Activities switch the track tabs.
**Say:** "The lightbox is keyboard accessible - Escape closes it. Track briefs use tabbed panels with
ARIA roles, so six long documents occupy one screen."

### 3:10 - 3:50 | Login, dashboard and design system
**Screen:** `login.html` -> sign in -> `dashboard.html`; then open `css/style.css` briefly.
**Do:** sign in with any valid e-mail and 4-character password; show the dashboard greeting and logout.
**Say:** "Login stores a demonstration session in localStorage - no server is used. The dashboard greets
the user, shows submission progress and a second countdown to the code freeze. All pages share one
token-based style guide: three breakpoints at 1180, 860 and 520 pixels, sticky navigation with active
states, skip link, and consistent components."

### 3:50 - 4:30 | Documentation, storyboard and testing
**Screen:** report PDF/Word - cover, table of contents, site map figure, wireframes, workload matrix.
**Say:**
- 4,000+ word report: introduction, storyboard with site map and wireframes, discussion of six technical
  challenges and their solutions, evaluation against every requirement, future enhancements, APA
  references, five sets of meeting minutes, attendance sheet and workload matrix.
- Testing: automated audit for broken links, mismatched tags, duplicate IDs, missing alt text - final run
  reported zero issues; cross-browser checks in Chrome, Firefox and Safari at four widths.

### 4:30 - 5:00 | Close
**Screen:** back to home page hero.
**Say:** "The submission includes the zipped website folder, this report and this video. Thank you -
we are happy to take questions."

---

## Recording checklist
- [ ] Audio level consistent, no clipping
- [ ] Mouse pointer highlighted / zoomed for small text
- [ ] No personal data or unrelated tabs visible
- [ ] Length 4-5 minutes
- [ ] Export MP4 (H.264) and verify it plays before uploading
