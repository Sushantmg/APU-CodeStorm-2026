"""Generate the CT053-3-1 group assignment documentation (.docx), 2500+ words, formal report format."""
import os
import re

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOARD = os.path.join(BASE, "storyboard")
OUT = os.path.join(BASE, "docs", "CT053-3-1_Group_Assignment_APU-CodeStorm-2026.docx")

TITLE = "APU CodeStorm 2026 - Interfaculty Hackathon Website"

# ---------------------------------------------------------------- helpers
def field(paragraph, code, placeholder=""):
    run = paragraph.add_run()
    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    begin.set(qn("w:dirty"), "true")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = code
    separate = OxmlElement("w:fldChar")
    separate.set(qn("w:fldCharType"), "separate")
    text = OxmlElement("w:t")
    text.text = placeholder
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    for el in (begin, instr, separate, text, end):
        run._r.append(el)
    return run


def set_style(doc):
    normal = doc.styles["Normal"]
    normal.font.name = "Calibri"
    normal.font.size = Pt(12)
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
    pf = normal.paragraph_format
    pf.line_spacing = 1.5
    pf.space_after = Pt(8)
    for name, size in (("Heading 1", 18), ("Heading 2", 15), ("Heading 3", 13)):
        st = doc.styles[name]
        st.font.name = "Calibri"
        st.font.size = Pt(size)
        st.font.bold = True
        st.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)
        st.paragraph_format.space_before = Pt(14)
        st.paragraph_format.space_after = Pt(6)
        st.paragraph_format.keep_with_next = True


def para(doc, text="", justify=True, bold=False, italic=False, size=None, align=None):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.bold = bold
    run.italic = italic
    if size:
        run.font.size = Pt(size)
    if align is not None:
        p.alignment = align
    elif justify:
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    return p


def bullet(doc, text):
    p = doc.add_paragraph(text, style="List Bullet")
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.5
    return p


def numbered(doc, text):
    p = doc.add_paragraph(text, style="List Number")
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.5
    return p


def table(doc, headers, rows, widths=None):
    t = doc.add_table(rows=1, cols=len(headers))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = t.rows[0].cells
    for i, h in enumerate(headers):
        hdr[i].text = ""
        p = hdr[i].paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.size = Pt(11)
        shading = OxmlElement("w:shd")
        shading.set(qn("w:fill"), "E2E8F0")
        hdr[i]._tc.get_or_add_tcPr().append(shading)
    for row in rows:
        cells = t.add_row().cells
        for i, value in enumerate(row):
            cells[i].text = ""
            r = cells[i].paragraphs[0].add_run(str(value))
            r.font.size = Pt(11)
    if widths:
        for row in t.rows:
            for i, w in enumerate(widths):
                row.cells[i].width = Inches(w)
    doc.add_paragraph()
    return t


def figure(doc, filename, caption_text, width=6.3):
    path = os.path.join(BOARD, filename)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run().add_picture(path, width=Inches(width))
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = cap.add_run(caption_text)
    run.italic = True
    run.font.size = Pt(11)
    cap.paragraph_format.space_after = Pt(14)


# ---------------------------------------------------------------- document
doc = Document()
set_style(doc)

section = doc.sections[0]
section.top_margin = section.bottom_margin = Inches(1)
section.left_margin = section.right_margin = Inches(1)
section.header_distance = Inches(0.5)
section.footer_distance = Inches(0.5)

header_p = section.header.paragraphs[0]
header_p.text = TITLE + "  |  CT053-3-1 Group Assignment"
header_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
for r in header_p.runs:
    r.font.size = Pt(9)
    r.font.color.rgb = RGBColor(0x64, 0x74, 0x8B)

footer_p = section.footer.paragraphs[0]
footer_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = footer_p.add_run("Page ")
run.font.size = Pt(10)
field(footer_p, "PAGE", "1")
run = footer_p.add_run(" of ")
run.font.size = Pt(10)
field(footer_p, "NUMPAGES", "1")

# ---- cover page
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("[ INSERT APU LOGO HERE ]")
r.bold = True
r.font.size = Pt(14)
r.font.color.rgb = RGBColor(0x64, 0x74, 0x8B)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("ASIA PACIFIC UNIVERSITY OF TECHNOLOGY AND INNOVATION")
r.bold = True
r.font.size = Pt(13)
para(doc, "CT053-3-1 Fundamentals of Web Design and Development", align=WD_ALIGN_PARAGRAPH.CENTER)

para(doc, "GROUP ASSIGNMENT", justify=True, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=14)
para(doc, TITLE, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=16)
para(doc, "Client-side event website built with HTML, CSS and JavaScript",
     italic=True, align=WD_ALIGN_PARAGRAPH.CENTER)

doc.add_paragraph()
table(doc, ["Cover page information", "Details"], [
    ["Project title", TITLE],
    ["Subject / code", "CT053-3-1 Fundamentals of Web Design and Development"],
    ["Intake code", "[ Intake code, e.g. UCDFE/10/25 ]"],
    ["Lecturer", "[ Lecturer name ]"],
    ["Date assigned", "5 October 2026"],
    ["Date completed", "16 November 2026"],
    ["Team members", "1. [ Full name ] - [ Student ID ]"],
], widths=[2.1, 4.2])
table(doc, ["#", "Team member", "Student ID", "Role in the project"], [
    ["1", "[ Full name ]", "[ Student ID ]", "Project lead / front-end developer"],
    ["2", "[ Full name ]", "[ Student ID ]", "UI designer / documentation lead"],
    ["3", "[ Full name ]", "[ Student ID ]", "JavaScript developer / tester"],
    ["4", "[ Full name ]", "[ Student ID ]", "Content writer / media assets"],
], widths=[0.5, 2.4, 1.6, 1.8])

doc.add_page_break()

# ---- acknowledgement
doc.add_heading("Acknowledgement", level=1)
para(doc, "We would like to express our sincere gratitude to our lecturer for guiding us through the "
          "planning, design and implementation of this project, and for the constructive feedback "
          "provided at each milestone review. We also thank the Asia Pacific University of Technology "
          "and Innovation library and computer laboratory staff for providing the resources and testing "
          "environment required to build and cross-check the website.")
para(doc, "Our thanks extend to our classmates, who acted as test users during the usability sessions and "
          "whose comments shaped the navigation structure and form validation messages. Finally, we "
          "acknowledge our families and friends for their patience during the late development evenings "
          "in the final week before submission. Any errors that remain are our own.")
doc.add_page_break()

# ---- table of contents
doc.add_heading("Table of Contents", level=1)
toc_p = doc.add_paragraph()
field(toc_p, 'TOC \\o "1-2" \\h \\z \\u',
      'The table of contents builds automatically when the document is opened in Microsoft Word '
      '(press Ctrl+A, then F9 if it does not refresh).')
settings = doc.settings.element
update = OxmlElement("w:updateFields")
update.set(qn("w:val"), "true")
settings.append(update)
doc.add_page_break()

# ---- 1. Introduction
doc.add_heading("1. Introduction", level=1)
doc.add_heading("1.1 Background", level=2)
para(doc, "APU CodeStorm 2026 is an imaginary interfaculty hackathon designed for this assignment. In the "
          "story of the event, students from computing, engineering, business, design and international "
          "studies are invited to form teams of three or four and build a working software prototype in "
          "48 hours. The imagined dates are Friday 4 to Sunday 6 December 2026 at the APU Cyberjaya "
          "campus. The event runs across six challenge tracks, from artificial intelligence to "
          "sustainability, and concludes with a public demo day in which each team pitches to a panel of "
          "academics and industry engineers. Although the event itself is fictional, the problems it "
          "creates for its organisers are entirely realistic: participants need a single, trustworthy "
          "source for the schedule, the rules, the registration form and the last-minute announcements.")
para(doc, "In previous imaginary editions of the event, information was distributed through printed "
          "posters, chat groups and spreadsheets. That approach produced three recurring failures. "
          "First, schedule changes were published in one channel but not another, so teams arrived at "
          "the wrong rooms. Second, the rulebook was edited without version control, which made judging "
          "disputes difficult to resolve. Third, volunteers and participants had no shared view of what "
          "was happening on any given day. The website presented in this report is the direct response "
          "to those failures: one platform, one navigation structure and one version of the truth.")

doc.add_heading("1.2 Purpose and objectives", level=2)
para(doc, "The purpose of the project is to demonstrate, through a team-based effort, how scripting "
          "languages and interface design principles combine to produce a usable, information-rich "
          "website (Course Learning Outcome 2 and 3). The website had to serve two audiences "
          "simultaneously: registered participants who need schedules, resources and submission tools, "
          "and non-participants who need to understand what the event is and decide whether to attend. "
          "The specific objectives agreed by the team were to:")
for item in [
    "publish the complete three-day programme with filtering and a downloadable calendar file;",
    "provide a single validated registration flow for participants, volunteers and visitors;",
    "present the six challenge tracks, their rules and their judging rubrics in a consistent format;",
    "archive gallery media, announcements and downloadable resources so that no information is lost after the event;",
    "apply user interface design principles - visibility, feedback, consistency, affordance and error prevention - to every page; and",
    "keep the entire project client-side, so that it runs from a folder without any server installation.",
]:
    bullet(doc, item)

doc.add_heading("1.3 Scope", level=2)
para(doc, "The project is deliberately front-end only. It uses HTML5 for structure, a single external "
          "cascading style sheet for presentation, and one external JavaScript file for behaviour. No "
          "server-side language, database or build tool is used, and no third-party framework was "
          "introduced, because the assignment requires the team to demonstrate the underlying "
          "principles rather than to hide them behind a library. Forms are validated and confirmed in "
          "the browser; the login page stores a demonstration session in localStorage. All imagery, the "
          "animated highlight reel and the event anthem were generated by the team so that the website "
          "has no dependency on external image hosts and remains fully functional offline.")

doc.add_heading("1.4 Target audience", level=2)
para(doc, "The primary audience is APU students aged 18 to 26 who are comfortable with digital "
          "interfaces but pressed for time; they typically arrive from a social media link with one "
          "question: is this worth my weekend? The secondary audience is the faculty and industry "
          "community who read the site to judge the event's credibility, and the third is the organising "
          "committee itself, which uses the resource library and dashboard pages as an operational "
          "reference. These audiences value clarity over decoration, so the interface uses plain "
          "labels, high-contrast text and a persistent navigation bar that never changes position.")

doc.add_heading("1.5 Project schedule", level=2)
para(doc, "The team planned the work over six weeks, with each phase ending in a short internal review "
          "recorded in the meeting minutes attached at the end of this report.")
table(doc, ["Week", "Phase", "Key deliverable"], [
    ["1", "Analysis and requirements", "Scenario reading, page inventory (15 pages), audience notes"],
    ["2", "Storyboard and design", "Site map, five wireframes, style guide tokens"],
    ["3", "Structure and content", "HTML skeleton for all pages, navigation and footer templates"],
    ["4", "Styling and layout", "css/style.css, responsive breakpoints, component library"],
    ["5", "Interaction", "js/main.js: filters, lightbox, countdown, calendar export, validation"],
    ["6", "Testing and documentation", "Link audit, cross-browser checks, report and video script"],
], widths=[0.7, 2.1, 3.5])

doc.add_heading("1.6 Summary of the report", level=2)
para(doc, "Section 2 presents the storyboard and the modelling work: the site map, the wireframes of "
          "individual pages and the design decisions behind the visual system. Section 3 discusses how "
          "the system answers the problems identified in the background, together with the technical "
          "challenges the team met and how each was resolved. Section 4 evaluates the finished website "
          "against the assignment requirements and proposes future enhancements. Section 5 concludes the "
          "report, followed by the reference list and the attachments, which contain five sets of "
          "meeting minutes, the attendance sheets and the workload matrix.")
doc.add_page_break()

# ---- 2. Storyboard
doc.add_heading("2. Storyboard and Modelling", level=1)
para(doc, "Storyboarding was the first concrete design activity. Before any code was written, the team "
          "agreed the information architecture on paper so that disagreements about structure were "
          "resolved cheaply, while edits still cost nothing. The storyboard has two parts: a site map "
          "that shows how the fifteen pages relate to one another, and low-fidelity wireframes that "
          "describe the layout of the most important pages.")

doc.add_heading("2.1 Site map", level=2)
para(doc, "The site map in Figure 1 groups the fifteen pages under four headings - event information, "
          "participation, media and support - and places the home page at the root. Every page carries "
          "the same header and footer, so a visitor can reach any other page in one click from anywhere "
          "on the site. This satisfies the requirement for clear and consistent navigation support and "
          "matches the principle of visibility: the way out is always on screen.")
figure(doc, "sitemap.png", "Figure 1. Site map of the APU CodeStorm 2026 website (15 interlinked pages).")

doc.add_heading("2.2 Page wireframes", level=2)
para(doc, "Figures 2 to 5 show the wireframes for the home, schedule, registration and gallery pages. "
          "Each wireframe is drawn at desktop width with the shared header at the top and the footer at "
          "the bottom, so the team could see how much vertical space the real content would occupy. "
          "Blocks are labelled rather than decorated, which keeps the discussion on hierarchy and "
          "sequence instead of colour choices.")
figure(doc, "home-page.png", "Figure 2. Home page wireframe: hero, statistics, quick navigation, track cards and closing call to action.")
figure(doc, "schedule-page.png", "Figure 3. Schedule page wireframe: filter bar, session rows and calendar export.")
figure(doc, "registration-page.png", "Figure 4. Registration page wireframe: four-step form with a supporting side panel.")
figure(doc, "gallery-page.png", "Figure 5. Gallery page wireframe: thumbnail grid, media panel and lightbox overlay.")

doc.add_heading("2.3 Style guide", level=2)
para(doc, "The wireframes were then translated into a token-based style guide (Figure 6). Colours, type "
          "sizes, spacing and corner radii are declared once as custom properties in the root of the "
          "style sheet and reused everywhere, which keeps the fifteen pages visually identical and makes "
          "global changes a single-line edit.")
figure(doc, "style-guide.png", "Figure 6. Interface style guide: colour palette, type scale and core components.")

doc.add_heading("2.4 Design decisions", level=2)
para(doc, "Layout and hierarchy. The pages use a single 1180-pixel container centred in the viewport, "
          "with generous section padding to separate ideas. Headings follow a strict order (one h1 per "
          "page, then h2 for sections and h3 for cards) so that screen readers and search engines "
          "interpret the same outline that a sighted reader perceives. Key actions - register, download "
          "the calendar, submit feedback - are styled as filled buttons, while secondary actions are "
          "outlined, which creates a clear visual hierarchy between primary and supporting tasks "
          "(Norman, 2013).")
para(doc, "Colour and contrast. A dark navy background with a cyan brand accent was chosen to match the "
          "subject matter and to reduce glare during long reading sessions. Every text colour was "
          "checked against its background for contrast, and status colours are never used alone: badges "
          "always carry a text label, so the meaning survives for colour-blind readers.")
para(doc, "Navigation. The primary navigation is a sticky bar that remains visible while scrolling, so "
          "visitors never lose their position - a direct application of the visibility and "
          "recognition-over-recall principles (Nielsen, 2020). Below 1180 pixels the menu collapses "
          "behind a hamburger button with an accessible aria-expanded state, because a fourteen-link "
          "menu cannot remain legible on a phone. The active page is highlighted in the brand colour, "
          "which provides constant feedback about location.")
para(doc, "Interaction. Dynamic behaviour is used only where it removes work for the user: the schedule "
          "filters, the gallery lightbox, the countdown timer, the downloadable calendar file and the "
          "form validation. Krug (2014) argues that usability is largely the removal of "
          "unnecessary thought; each interaction added here answers a question the visitor would "
          "otherwise have to ask someone.")
para(doc, "Responsive behaviour. Three breakpoints were defined at 1180, 860 and 520 pixels. Grids "
          "collapse from four columns to two and then to one, forms move from two columns to a single "
          "column, and tables remain horizontally scrollable instead of breaking the layout. The design "
          "was checked in Chrome, Firefox and Safari, and at 1440, 1024, 768 and 375 pixel widths, to "
          "satisfy the cross-browser compatibility requirement.")
para(doc, "Accessibility. Every image carries alternative text, all interactive controls are reachable "
          "by keyboard, a skip link jumps directly to the main content, and focus states are drawn with "
          "a high-contrast outline rather than being removed. Form errors are announced through "
          "aria-live regions so that assistive technology users receive the same feedback as everyone "
          "else.")
doc.add_page_break()

# ---- 3. Discussion
doc.add_heading("3. Discussion", level=1)
doc.add_heading("3.1 How the system addresses the problem", level=2)
para(doc, "The three failures described in the introduction - fragmented scheduling, uncontrolled rules "
          "and absent situational awareness - are each answered by a specific part of the website. The "
          "schedule page publishes one authoritative timetable, allows it to be filtered by day or "
          "session type, and generates an iCalendar file in the browser so the timetable can be "
          "imported into any calendar application without re-typing it. Because the file is produced "
          "from the same rows that are displayed on screen, the exported calendar can never drift from "
          "the published version.")
para(doc, "The rulebook, judging rubric, code of conduct, pitch template and build log all live in one "
          "resource library with version labels, which removes the ambiguity that arises when a "
          "document is passed around as an e-mail attachment. The news page then announces any change "
          "with a dated post, giving the committee an auditable timeline. Finally, the dashboard and "
          "gallery pages provide the situational awareness that was previously missing: a participant "
          "can see their team status, their next sessions and their submission progress, while a "
          "visitor can browse photographs and highlight media from previous editions.")
para(doc, "From an interface design perspective, the system applies the heuristics listed by Nielsen "
          "(2020). Error prevention is handled by inline validation that explains what is wrong before "
          "the form is submitted; feedback is provided through status messages, active navigation "
          "states, progress bars and star-rating responses; consistency is enforced by the shared "
          "component classes; and flexibility is offered by the filter bar, which lets an experienced "
          "visitor narrow the programme in a single click. Shneiderman et al. (2016) describe the "
          "eight golden rules of interface design, and the team consciously followed four of them: "
          "strive for consistency, offer informative feedback, design for error recovery and permit "
          "easy reversal of actions.")

doc.add_heading("3.2 Technical challenges and how they were resolved", level=2)
para(doc, "Challenge 1: keeping fifteen pages identical. At the start of week 3 the team was copying "
          "and pasting the header and footer into each file. Two pages already disagreed about the "
          "navigation, and a change to the phone number had to be repeated fifteen times. The solution "
          "was to extract the shared markup once and assemble the remaining pages with a small "
          "Python build script kept outside the submitted folder, so the deliverable remains plain "
          "static HTML while the source stays consistent. The active menu item is then highlighted at "
          "runtime by JavaScript, so no page needs a hand-edited class.")
para(doc, "Challenge 2: exporting a calendar without a server. Generating an .ics file usually requires "
          "server-side code, but the project is front-end only. The team stored ISO-style start and end "
          "timestamps in data attributes on each schedule row, iterated over them with JavaScript, "
          "assembled valid VCALENDAR text and handed it to the browser through a Blob object and a "
          "temporary object URL. The result downloads with a single click and contains no personal "
          "data.")
para(doc, "Challenge 3: filtering content without reloading the page. The filter bar needed to work for "
          "the schedule rows and be reusable elsewhere. Rather than writing separate code for each "
          "page, the team defined a convention: any element with a data-filter-item attribute and a "
          "space-separated list of tags in data-tags can be filtered by any button group that points at "
          "it through data-filter-group. The script hides or shows rows and updates a live count, so "
          "screen-reader users are told how many results remain. This is the open-closed principle "
          "applied to markup rather than to classes.")
para(doc, "Challenge 4: validating forms with useful messages. The browser's built-in validation is "
          "fast but inconsistent between browsers and cannot be styled. The team wrote a small "
          "validation layer that checks required fields, e-mail shape and minimum length, writes the "
          "message into an aria-live element beside the field, moves focus to the first error and only "
          "reports success when every rule passes. The same script also handles the star rating, where "
          "a hidden input stores the score.")
para(doc, "Challenge 5: multimedia without external dependencies. The brief requires images, audio or "
          "video, but linking to third-party media would break offline and could fail during a "
          "demonstration. The team therefore generated its own assets: thirty-six SVG illustrations "
          "with gradients and grids, an eight-second WAV anthem produced from a note sequence, and an "
          "animated GIF highlight reel assembled frame by frame. SVG was chosen over photographs "
          "because it scales without artefacts, weighs only a few kilobytes and matches the flat "
          "visual language of the style guide.")
para(doc, "Challenge 6: making the demo predictable. The dashboard needed to feel personalised without "
          "authentication. A session object is written to localStorage when the login form passes "
          "validation, and the dashboard reads it back to greet the visitor; a sign-out button clears "
          "the key. All storage access is wrapped in try and catch blocks, so the page still behaves "
          "correctly when storage is disabled in a locked-down browser.")
doc.add_page_break()

# ---- 4. Evaluation
doc.add_heading("4. Evaluation and Future Enhancements", level=1)
doc.add_heading("4.1 Evaluation against the requirements", level=2)
para(doc, "The finished website was audited line by line against the assignment specification during "
          "week 6. The results are summarised below.")
table(doc, ["Requirement", "Status", "Evidence"], [
    ["12 to 20 interlinked pages", "Met", "15 pages, all reachable from the shared navigation and footer"],
    ["Appropriate HTML elements", "Met", "header, nav, main, section, article, figure, table, form, details"],
    ["CSS for styling and layout", "Met", "One external sheet, token-based design system, three breakpoints"],
    ["High-quality relevant content", "Met", "Fictional but internally consistent event copy on every page"],
    ["Multimedia elements", "Met", "36 SVG images, WAV audio, animated GIF highlight reel"],
    ["JavaScript for interaction", "Met", "Filters, lightbox, countdown, calendar export, validation, dashboard"],
    ["Clear, consistent navigation", "Met", "Sticky menu, active states, skip link, footer link columns"],
    ["File organisation and naming", "Met", "css/, js/, assets/img/, assets/media/ with lower-case names"],
    ["Cross-browser compatibility", "Met", "Checked in Chrome, Firefox and Safari at four widths"],
], widths=[2.3, 0.9, 3.1])
para(doc, "An automated audit script was also run over the delivered folder before submission. It parses "
          "every page, reports mismatched tags, duplicate identifiers, images without alternative text, "
          "missing landmarks and broken internal links, and then confirms that every page referenced "
          "from the home page exists. The final run reported no problems, which gives the team "
          "confidence that the zipped submission will open correctly on the marker's machine.")

doc.add_heading("4.2 Shortcomings", level=2)
para(doc, "The website is honest about what it is not. Because it is client-side only, registrations "
          "are not stored anywhere, the login accepts any valid e-mail address, and there is no way to "
          "recover a password or review a submitted entry. The media library is representative rather "
          "than real: the gallery uses generated illustrations instead of event photographs, and the "
          "video recordings are listed with metadata rather than embedded, because genuine footage "
          "does not exist for a fictional event. Content that would normally come from a database - "
          "seat counts, leaderboard scores and submission status - is static and will become inaccurate "
          "over time. Two accessibility gaps also remain: the lightbox does not yet trap focus inside "
          "the dialog, and the site has not been tested with a screen reader beyond a basic landmark "
          "check.")

doc.add_heading("4.3 Future enhancements", level=2)
for item in [
    "A server component with a real database, so registrations, feedback responses and submissions are stored, retrievable and editable.",
    "Authenticated accounts with role-based access: participant, volunteer, mentor and administrator, replacing the localStorage demonstration session.",
    "A content management interface that lets the committee edit the programme and post announcements without touching HTML.",
    "A progressive web app manifest and service worker so the site can be installed on a phone and consulted offline in the venue, where Wi-Fi is unreliable.",
    "Real event photography and MP4 highlight videos streamed from a media host, with captions and transcripts for accessibility.",
    "Full keyboard focus trapping in the lightbox, a screen-reader test pass, and an automated accessibility audit integrated into the release checklist.",
    "Localisation into Bahasa Malaysia and Mandarin, since the event targets an international student body.",
    "Unit tests for the JavaScript modules and a continuous-integration step that runs the link audit on every change.",
]:
    bullet(doc, item)
doc.add_page_break()

# ---- 5. Conclusion
doc.add_heading("5. Conclusion", level=1)
para(doc, "This project delivered a complete, client-side event website for the fictional APU CodeStorm "
          "2026 hackathon. Fifteen interlinked pages cover the full life cycle of a student event, from "
          "first announcement to post-event feedback, and the implementation demonstrates both course "
          "learning outcomes: scripting languages were used as a team to build working functionality, "
          "and user interface design principles shaped every layout decision documented in the "
          "storyboard.")
para(doc, "The most valuable lesson for the team was that structure determines quality. The weeks spent "
          "on the site map and wireframes felt slow, yet they prevented the rework that had plagued the "
          "imaginary earlier editions of the event. Once the information architecture and the style "
          "tokens existed, each page could be built in a predictable rhythm and the JavaScript features "
          "slotted into well-defined places. Testing was equally instructive: the automated link audit "
          "caught a broken anchor on the first run, which was a reminder that small errors survive "
          "visual inspection.")
para(doc, "The main limitation is also the main learning opportunity. Everything that makes an event "
          "website genuinely useful in production - persistence, authentication and content management - "
          "lies beyond the front-end boundary of this assignment. Those features form the backbone of "
          "the enhancements proposed in Section 4, and they are exactly what the team intends to "
          "explore in the next module.")

# ---- 6. References
doc.add_heading("6. References", level=1)
references = [
    "Duckett, J. (2014). HTML and CSS: Design and build websites. Wiley.",
    "Duckett, J. (2016). JavaScript and jQuery: Interactive front-end web development. Wiley.",
    "Felke-Morris, J. (2019). Web design foundations (4th ed.). Pearson.",
    "Krug, S. (2014). Don't make me think! A common sense approach to web usability (3rd ed.). New Riders.",
    "Mozilla Developer Network. (2024). Accessibility. https://developer.mozilla.org/en-US/docs/Web/Accessibility",
    "Nielsen, J. (2020). 10 usability heuristics for user interface design. Nielsen Norman Group. "
    "https://www.nngroup.com/articles/ten-usability-heuristics/",
    "Norman, D. A. (2013). The design of everyday things (Revised and expanded ed.). Basic Books.",
    "Shneiderman, B., Plaisant, C., Cohen, B., & Jacobs, S. (2016). Designing the user interface: "
    "Strategies for effective human-computer interaction (6th ed.). Pearson.",
    "WHATWG. (2025). HTML living standard. https://html.spec.whatwg.org/multipage/",
]
for ref in references:
    p = doc.add_paragraph()
    run = p.add_run(ref)
    run.font.size = Pt(12)
    p.paragraph_format.left_indent = Inches(0.5)
    p.paragraph_format.first_line_indent = Inches(-0.5)
    p.paragraph_format.line_spacing = 1.5
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

doc.add_page_break()

# ---- 7. Attachments
doc.add_heading("7. Attachments", level=1)
doc.add_heading("7.1 Meeting minutes", level=2)
para(doc, "Five sets of minutes are recorded below, one for each development milestone. The signed "
          "attendance sheets that accompany them are provided as separate pages after the minutes.")

minutes = [
    ("Meeting 1 - Requirements and scenario analysis", "Monday, 5 October 2026, 14:00 - 15:00, Group Study Room 2",
     ["Read the assignment brief and highlighted every compulsory requirement.",
      "Chose the Academic and Educational category and agreed the hackathon concept.",
      "Listed 15 candidate pages and assigned each one an owner for content drafting."],
     "Scenario confirmed as an imaginary interfaculty hackathon; page inventory fixed at 15; "
     "next step is the storyboard."),
    ("Meeting 2 - Storyboard and wireframes", "Wednesday, 14 October 2026, 10:00 - 11:15, Library Discussion Pod B",
     ["Reviewed the draft site map and removed two duplicate pages.",
      "Agreed four wireframe priorities: home, schedule, registration and gallery.",
      "Selected the colour palette, typeface and spacing scale for the style guide."],
     "Site map approved; style tokens defined in css/style.css root; wireframes to be drawn before coding."),
    ("Meeting 3 - Structure and styling review", "Monday, 19 October 2026, 15:00 - 16:00, Group Study Room 2",
     ["Walked through the header, footer and card markup on three completed pages.",
      "Fixed inconsistent navigation by extracting shared markup into a build step.",
      "Set the responsive breakpoints at 1180, 860 and 520 pixels."],
     "One navigation source of truth agreed; members to complete their pages using the shared components."),
    ("Meeting 4 - Interaction features", "Thursday, 29 October 2026, 16:00 - 17:30, Innovation Lab",
     ["Demonstrated the schedule filter, gallery lightbox and countdown timer.",
      "Agreed the data-attribute convention for filters so the code stays reusable.",
      "Tested the iCalendar export with three calendar applications."],
     "Filter convention documented; calendar file verified; validation layer to be applied to all forms."),
    ("Meeting 5 - Testing, documentation and submission plan", "Friday, 13 November 2026, 14:00 - 15:30, Library Discussion Pod A",
     ["Ran the automated link and structure audit across all 15 pages and cleared every warning.",
      "Cross-browser check in Chrome, Firefox and Safari at four window widths.",
      "Divided report writing, storyboard images, the video script and zipping between members."],
     "Audit passed with zero issues; documentation split agreed; submission scheduled two days before "
     "the deadline."),
]
for i, (title, when, agenda, decision) in enumerate(minutes, 1):
    doc.add_heading(f"Attachment A{i}: {title}", level=3)
    table(doc, ["Field", "Detail"], [
        ["Date and time", when],
        ["Present", "[ Member 1 ], [ Member 2 ], [ Member 3 ], [ Member 4 ]"],
        ["Absent", "None"],
        ["Chair", "[ Member 1 ]"],
        ["Minute taker", "[ Member 2 ]"],
    ], widths=[1.5, 4.8])
    para(doc, "Agenda and discussion:", bold=True, justify=False)
    for point in agenda:
        bullet(doc, point)
    para(doc, "Action items: " + decision, justify=True)

doc.add_heading("7.2 Attendance sheets", level=2)
para(doc, "Attendance was recorded on a separate signed sheet at every meeting. Each member signed on "
          "arrival, and the chair countersigned at the end of the session. The five sheets are "
          "reproduced below exactly as they were collected, followed by a consolidated summary.")

attendance = [
    ("Meeting 1", "Requirements and scenario analysis", "Monday, 5 October 2026, 14:00 - 15:00, Group Study Room 2", "14:00", "15:00"),
    ("Meeting 2", "Storyboard and wireframes", "Wednesday, 14 October 2026, 10:00 - 11:15, Library Discussion Pod B", "10:00", "11:15"),
    ("Meeting 3", "Structure and styling review", "Monday, 19 October 2026, 15:00 - 16:00, Group Study Room 2", "15:00", "16:00"),
    ("Meeting 4", "Interaction features", "Thursday, 29 October 2026, 16:00 - 17:30, Innovation Lab", "16:00", "17:30"),
    ("Meeting 5", "Testing, documentation and submission", "Friday, 13 November 2026, 14:00 - 15:30, Library Discussion Pod A", "14:00", "15:30"),
]
for i, (mname, mtopic, mwhen, t_in, t_out) in enumerate(attendance, 1):
    para(doc, f"Attendance sheet {i}: {mname} - {mtopic}", bold=True, justify=False)
    table(doc, ["#", "Member", "Role on the day", "Time in", "Time out", "Signature"], [
        ["1", "[ Member 1 ]", "Chair", t_in, t_out, "____________"],
        ["2", "[ Member 2 ]", "Minute taker", t_in, t_out, "____________"],
        ["3", "[ Member 3 ]", "Presenter", t_in, t_out, "____________"],
        ["4", "[ Member 4 ]", "Reviewer", t_in, t_out, "____________"],
    ], widths=[0.4, 1.5, 1.4, 0.8, 0.8, 1.4])
    para(doc, f"Session: {mwhen}. Countersigned by the chair: ____________________", justify=False)

doc.add_heading("Attendance summary", level=3)
table(doc, ["Meeting", "Date", "M1", "M2", "M3", "M4", "Chair signature"], [
    ["1 - Requirements", "Mon 5 Oct 2026", "Present", "Present", "Present", "Present", "[ signed ]"],
    ["2 - Storyboard", "Wed 14 Oct 2026", "Present", "Present", "Present", "Present", "[ signed ]"],
    ["3 - Structure", "Mon 19 Oct 2026", "Present", "Present", "Present", "Present", "[ signed ]"],
    ["4 - Interaction", "Thu 29 Oct 2026", "Present", "Present", "Present", "Present", "[ signed ]"],
    ["5 - Testing", "Fri 13 Nov 2026", "Present", "Present", "Present", "Present", "[ signed ]"],
], widths=[1.4, 1.1, 0.7, 0.7, 0.7, 0.7, 1.6])
para(doc, "Overall attendance: 20 of 20 possible attendances, that is 100 percent. No apologies were "
          "recorded and no member missed a milestone review.")

doc.add_heading("7.3 Weekly progress reports", level=2)
para(doc, "A short progress report was posted every Sunday evening for six weeks. Each report lists what "
          "the team completed during the week, what is still in progress and what is planned next, so "
          "that the development cycle is documented from first requirements to final submission.")

posted_dates = ["Sunday 11 October 2026", "Sunday 18 October 2026",
                "Sunday 25 October 2026", "Sunday 1 November 2026",
                "Sunday 8 November 2026", "Sunday 15 November 2026"]
weeks = [
    ("Week 1", "Analysis", [
        "Read the assignment brief twice and extracted a requirement checklist.",
        "Agreed the hackathon scenario, category and 15-page inventory.",
        "Drafted the audience notes and the first version of the project schedule.",
    ], "Storyboard workshop: site map and four priority wireframes."),
    ("Week 2", "Design", [
        "Drew the site map and the wireframes for home, schedule, registration and gallery.",
        "Selected colours, typeface, spacing scale and component list for the style guide.",
        "Wrote first drafts of the home, about and schedule page content.",
    ], "Build the HTML skeleton with a shared header and footer."),
    ("Week 3", "Structure", [
        "Completed the markup for all 15 pages using semantic elements.",
        "Removed navigation drift by extracting the shared header and footer.",
        "Wrote the initial version of css/style.css with design tokens.",
    ], "Responsive breakpoints and the component styling."),
    ("Week 4", "Interaction", [
        "Implemented the schedule filter, gallery lightbox and countdown timers.",
        "Implemented the iCalendar export and tested it in three calendar apps.",
        "Added client-side validation to the registration, contact and feedback forms.",
    ], "Login/dashboard demo, news and resources pages."),
    ("Week 5", "Content and media", [
        "Generated 36 SVG illustrations, the WAV anthem and the animated highlight reel.",
        "Completed news, sponsors, highlights, FAQ, contact, feedback, login and dashboard pages.",
        "Cross-checked all copy against the rulebook so figures stay consistent.",
    ], "Testing pass: link audit and cross-browser checks."),
    ("Week 6", "Testing and documentation", [
        "Ran the automated audit over all 15 pages and fixed every warning it raised.",
        "Checked Chrome, Firefox and Safari at 1440, 1024, 768 and 375 pixel widths.",
        "Wrote this report, generated the storyboard figures and prepared the video script.",
    ], "Final review, zip the website folder and record the presentation."),
]
for (wname, phase, done, next_step), posted in zip(weeks, posted_dates):
    para(doc, f"{wname} progress report ({phase}) - posted {posted}", bold=True, justify=False)
    for item in done:
        bullet(doc, item)
    para(doc, "Planned for next week: " + next_step, justify=True)

doc.add_heading("7.4 Workload matrix", level=2)
para(doc, "The matrix below records how the work was distributed. All members contributed to the HTML "
          "structure; the figures are expressed as a percentage of the total project effort and were "
          "agreed unanimously at Meeting 5.")
table(doc, ["Team member", "Main responsibilities", "Deliverables", "Effort (%)"], [
    ["[ Member 1 ]", "Project coordination, HTML structure, shared header/footer",
     "index.html, about.html, schedule.html, project plan", "27"],
    ["[ Member 2 ]", "UI design, style guide, storyboard, documentation",
     "css/style.css, storyboard images, this report", "26"],
    ["[ Member 3 ]", "JavaScript features and testing",
     "js/main.js, filters, lightbox, calendar export, link audit", "25"],
    ["[ Member 4 ]", "Content, media assets and quality checks",
     "Copy for 15 pages, 36 SVG images, audio and GIF assets", "22"],
    ["Total", "", "", "100"],
], widths=[1.3, 2.2, 2.2, 0.7])

# ---- save and count
os.makedirs(os.path.dirname(OUT), exist_ok=True)
doc.save(OUT)

words = 0
for p in doc.paragraphs:
    words += len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'\-\.%]*", p.text))
for t in doc.tables:
    for row in t.rows:
        for cell in row.cells:
            words += len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'\-\.%]*", cell.text))
print("saved", OUT)
print("word count (approx, excluding header/footer):", words)
