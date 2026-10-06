# APU CodeStorm 2026 — CT053-3-1 Group Assignment

A client-side event website for an imaginary interfaculty hackathon, plus the written
documentation and storyboard required by the CT053-3-1 *Fundamentals of Web Design and
Development* group assignment (Asia Pacific University of Technology and Innovation, 2026).

**Event:** APU CodeStorm 2026 — a 48-hour interfaculty hackathon, Fri 4 – Sun 6 December 2026,
APU Cyberjaya campus.

## Repository contents

| Folder | What it is |
| --- | --- |
| `website/` | The deliverable website — 15 interlinked pages, HTML + CSS + JS only |
| `docs/` | The report (`.docx`, 4,900+ words) and the video presentation script |
| `storyboard/` | Site map, four page wireframes and the style guide (PNG) |
| `tools/` | Scripts used to generate assets, build pages and run the link audit |
| `APU-CodeStorm-2026-website.zip` | Zipped website folder, ready for Moodle submission |

## Website

```
website/
├── index.html        home — hero, countdown, tracks, highlights
├── about.html        purpose, objectives, committee, rules
├── schedule.html     filterable 3-day programme + .ics calendar export
├── activities.html   six track briefs (tabs), side competitions, rules table
├── register.html     participant / volunteer / audience form with validation
├── gallery.html      12-image lightbox, media library, audio
├── news.html         announcements, deadlines, subscription form
├── resources.html    rulebook, rubric, templates, design kit downloads
├── sponsors.html     sponsor tiers and partner table
├── highlights.html   past editions archive and records
├── faq.html          accordion FAQ
├── contact.html      enquiry form, contact channels, venue floor plan
├── feedback.html     post-event survey with star rating
├── login.html        front-end demo login (localStorage session)
├── dashboard.html    participant hub: team status, submissions, countdown
├── css/style.css     token-based design system, 3 responsive breakpoints
├── js/main.js        nav, filters, lightbox, countdown, calendar, validation
└── assets/           36 SVG images, WAV anthem, animated GIF reel
```

### Run it locally

```bash
cd website
python3 -m http.server 8088
# open http://localhost:8088
```

Or simply open `website/index.html` in a browser — no build step, no dependencies.

### Checks

```bash
python3 tools/verify.py     # links, assets, tags, alt text, landmarks
python3 tools/build.py      # rebuild generated pages from tools/fragments/
python3 tools/gen_assets.py # regenerate SVG / GIF / WAV assets
python3 tools/gen_storyboard.py
python3 tools/gen_report.py # regenerate the .docx report
```

## Requirements coverage

- 15 interlinked pages (brief: 12–20), shared header/nav/footer
- Semantic HTML5, one external stylesheet, one external script
- Multimedia: SVG imagery, WAV audio, animated GIF
- JavaScript interaction: filters, lightbox, countdowns, calendar export, form validation, tabs
- Responsive at 1180 / 860 / 520 px, keyboard accessible, skip link, alt text throughout
- Report: 4,900+ words, formal formatting, TOC, storyboard figures, APA references,
  five meeting minutes, attendance sheets, weekly reports, workload matrix

## Team

| # | Member | Student ID | Role |
| --- | --- | --- | --- |
| 1 | [ Full name ] | [ Student ID ] | Project lead / front-end developer |
| 2 | [ Full name ] | [ Student ID ] | UI designer / documentation lead |
| 3 | [ Full name ] | [ Student ID ] | JavaScript developer / tester |
| 4 | [ Full name ] | [ Student ID ] | Content writer / media assets |
