"""Generate storyboard images (site map, wireframes, style guide) for the report."""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "storyboard")
os.makedirs(OUT, exist_ok=True)

REG = "/System/Library/Fonts/Supplemental/Arial.ttf"
BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"


def font(size, bold=False):
    try:
        return ImageFont.truetype(BOLD if bold else REG, size)
    except OSError:
        return ImageFont.load_default()


F10, F12, F14, F16, F20, F26 = font(13), font(16), font(17, True), font(19, True), font(24, True), font(32, True)

INK = (30, 41, 59)
LINE = (100, 116, 139)
FILL = (241, 245, 249)
FILL2 = (226, 232, 240)
BRAND = (8, 145, 178)
PAPER = (255, 255, 255)


def new(w, h):
    img = Image.new("RGB", (w, h), PAPER)
    return img, ImageDraw.Draw(img)


def box(d, x, y, w, h, label="", fill=FILL, outline=LINE, f=F14, bold_label=True):
    d.rounded_rectangle([x, y, x + w, y + h], radius=8, fill=fill, outline=outline, width=2)
    if label:
        lines = label.split("\n")
        total = len(lines) * (f.size + 6)
        ty = y + (h - total) / 2
        for line in lines:
            tw = d.textlength(line, font=f)
            d.text((x + (w - tw) / 2, ty), line, font=f, fill=INK)
            ty += f.size + 6
    return (x, y, w, h)


def caption(d, x, y, text, f=F12):
    d.text((x, y), text, font=f, fill=(71, 85, 105))


def title(img, d, text, sub=""):
    d.rectangle([0, 0, img.width, 76], fill=(15, 23, 42))
    d.text((40, 22), text, font=F26, fill=(255, 255, 255))
    if sub:
        d.text((40, 56), sub, font=F10, fill=(148, 163, 184))


# ---------------------------------------------------------------- site map
def sitemap():
    img, d = new(1500, 1080)
    title(img, d, "APU CodeStorm 2026 - Site Map", "15 interlinked pages, one shared header, navigation and footer")

    root = box(d, 620, 110, 260, 60, "index.html  (Home)", fill=(8, 145, 178), outline=(8, 145, 178), f=F16)
    d.rectangle([748, 170, 752, 210], fill=LINE)

    groups = [
        ("Event information", ["about.html  About", "schedule.html  Schedule",
                               "activities.html  Activities", "highlights.html  Past events"]),
        ("Participate", ["register.html  Register", "login.html  Login",
                         "dashboard.html  Dashboard", "feedback.html  Feedback"]),
        ("Media & content", ["gallery.html  Gallery", "news.html  News",
                                 "resources.html  Resources", "sponsors.html  Sponsors"]),
        ("Support", ["faq.html  FAQ", "contact.html  Contact"]),
    ]

    xs = [70, 430, 790, 1150]
    d.line([xs[0] + 150, 210, xs[-1] + 150, 210], fill=LINE, width=3)
    d.line([750, 210, 750, 210], fill=LINE, width=3)

    y = 250
    for i, (gname, children) in enumerate(groups):
        gx = xs[i]
        d.line([gx + 150, 210, gx + 150, y], fill=LINE, width=3)
        box(d, gx, y, 300, 54, gname, fill=FILL2, f=F14)
        cy = y + 90
        for child in children:
            d.line([gx + 150, y + 54, gx + 150, cy], fill=(148, 163, 184), width=2)
            d.line([gx + 150, cy + 26, gx + 30, cy + 26], fill=(148, 163, 184), width=2)
            box(d, gx + 30, cy, 270, 52, child, f=F12, outline=(148, 163, 184))
            cy += 66

    y2 = 760
    box(d, 70, y2, 640, 120, "Shared components: header + responsive navigation\n"
                             "shared css/style.css + js/main.js\n"
                             "shared footer + back-to-top button", f=F14)
    box(d, 760, y2, 640, 120, "Assets: 36 SVG images, 1 animated GIF, 1 WAV audio\n"
                              "assets/img/  -  assets/media/\n"
                              "No backend: forms validate in the browser", f=F14)

    caption(d, 70, 900, "Every page links to every other page through the persistent navigation bar (desktop: inline menu, mobile: hamburger panel) "
                        "and the footer link columns.")
    caption(d, 70, 926, "Deep links (for example contact.html#map and schedule.html filters) are reachable from at least two different pages.")
    img.save(os.path.join(OUT, "sitemap.png"))
    print("sitemap.png")


# ---------------------------------------------------------------- wireframes
def chrome(d, active="Home"):
    box(d, 50, 30, 800, 60, "", fill=FILL2)
    box(d, 66, 42, 36, 36, "logo", f=F10, outline=(148, 163, 184))
    labels = ["Home", "About", "Schedule", "Register", "Gallery", "FAQ"]
    x = 150
    for lb in labels:
        if lb == active:
            box(d, x, 44, 74, 32, lb, fill=(186, 230, 253), f=F10, outline=BRAND)
        else:
            box(d, x, 44, 74, 32, lb, fill=FILL, f=F10, outline=(203, 213, 225))
        x += 48
    d.text((640, 52), "menu continues / hamburger below 1180 px", font=F10, fill=(100, 116, 139))


def footer(d, h):
    box(d, 50, h - 150, 800, 100, "", fill=FILL2)
    for i in range(4):
        box(d, 70 + i * 195, h - 136, 175, 72, ["Brand + socials", "Quick links", "Participants", "Contact"][i],
            f=F10, fill=FILL)
    caption(d, 50, h - 42, "Footer: sitemap-style link columns, copyright line with JS-injected year.")


def wireframe(name, active, blocks, note):
    h = 1240
    img, d = new(900, h)
    d.rectangle([0, 0, 900, h], fill=(248, 250, 252))
    title(img, d, f"Wireframe - {name}", "Low-fidelity blueprint (desktop, 1180 px content container)")
    d.rectangle([0, 76, 900, h], fill=(248, 250, 252))
    chrome(d, active)
    y = 110
    for kind, label, height in blocks:
        if kind == "hero":
            box(d, 50, y, 800, height, label, fill=(224, 242, 254), outline=BRAND, f=F14)
        elif kind == "row":
            cols = int(label.split("|")[1])
            text = label.split("|")[0]
            n = cols
            gap = 14
            w = (800 - gap * (n - 1)) / n
            box(d, 50, y, 800, 26, text, fill=FILL2, f=F10, outline=(203, 213, 225))
            yy = y + 34
            rows = height // 100
            for r in range(rows):
                for c in range(n):
                    box(d, 50 + c * (w + gap), yy, w, 84, "", fill=FILL, f=F10,
                        outline=(203, 213, 225))
                yy += 98
            y += height
            continue
        elif kind == "form":
            box(d, 50, y, 490, height, label, fill=FILL, f=F12, outline=(203, 213, 225))
            box(d, 560, y, 290, height, "SIDE PANEL\nstatus\nlinks\nimages", fill=FILL2, f=F12,
                outline=(203, 213, 225))
        elif kind == "list":
            rows = height // 58
            yy = y
            for r in range(rows):
                box(d, 50, yy, 800, 48, label, fill=FILL, f=F10, outline=(203, 213, 225))
                yy += 58
            y += height
            continue
        elif kind == "text":
            d.text((50, y), label, font=F12, fill=(71, 85, 105))
            y += height
            continue
        y += height
    footer(d, h)
    caption(d, 50, min(y + 8, h - 172), note)
    img.save(os.path.join(OUT, name.replace(" ", "-").lower() + ".png"))
    print(name.replace(" ", "-").lower() + ".png")


wireframe("Home page", "Home", [
    ("hero", "HERO: event name, tagline, countdown, CTA buttons, banner image", 210),
    ("row", "Statistics row|4", 60),
    ("text", "Quick navigation - 4 cards", 30),
    ("row", "Challenge tracks|3", 240),
    ("text", "Highlights: audio player + animated GIF | Why take part cards", 30),
    ("row", "Final CTA|2", 60),
], "Sections stack vertically; each card links to a full page. Countdown driven by data-countdown attribute.")

wireframe("Schedule page", "Schedule", [
    ("hero", "PAGE HEADER: title, date range, Download .ics button", 130),
    ("text", "Filter bar: All | Day 1 | Day 2 | Day 3 | Keynotes | Clinics | Social", 40),
    ("list", "session row: time | title + venue | badge", 348),
    ("text", "Venue notes + calendar export panel", 40),
    ("row", "Venue map|2", 200),
], "Rows are filtered by JS using data-tags; the same rows generate the downloadable .ics calendar file.")

wireframe("Registration page", "Register", [
    ("hero", "PAGE HEADER: closing date, one-form promise", 110),
    ("form", "FORM:\n1 participation type\n2 team + captain details\n3 team members\n4 requirements + declaration\n[Submit registration]", 420),
    ("text", "Form validation runs client-side: required, e-mail format, minLength, checkbox consent", 40),
    ("row", "Related|2", 90),
], "Two-column layout: primary form on the left, key dates and seat availability panel on the right.")

wireframe("Gallery page", "Gallery", [
    ("hero", "PAGE HEADER: how to use the lightbox", 110),
    ("text", "Photo gallery - 12 thumbnails", 30),
    ("row", "thumb|4", 210),
    ("text", "Video highlights: animated recap + media library panel", 40),
    ("row", "Media|2", 110),
    ("text", "Audio player + photo usage policy", 40),
    ("row", "End|2", 70),
], "Clicking a thumbnail opens the full-screen lightbox (Esc or close button to exit).")

# ---------------------------------------------------------------- style guide
def styleguide():
    img, d = new(900, 720)
    title(img, d, "Interface style guide", "Tokens used across all 15 pages (css/style.css :root)")
    y = 110
    d.text((50, y), "Colour palette", font=F20, fill=INK)
    y += 40
    swatches = [("Background", "#0b1220", (11, 18, 32)), ("Surface", "#0f172a", (15, 23, 42)),
                ("Border", "#22304d", (34, 48, 77)), ("Text", "#e2e8f0", (226, 232, 240)),
                ("Brand", "#22d3ee", (34, 211, 238)), ("Accent", "#f59e0b", (245, 158, 11)),
                ("Success", "#22c55e", (34, 197, 94)), ("Danger", "#ef4444", (239, 68, 68))]
    x = 50
    for name, hexs, rgb in swatches:
        d.rounded_rectangle([x, y, x + 92, y + 74], radius=8, fill=rgb, outline=LINE)
        d.text((x + 6, y + 80), name, font=F10, fill=INK)
        d.text((x + 6, y + 98), hexs, font=F10, fill=(100, 116, 139))
        x += 104
    y += 150
    d.text((50, y), "Typography - Segoe UI / Calibri stack", font=F20, fill=INK)
    y += 42
    for label, f, sample in [("H1", F26, "Build. Break. Breakthrough."), ("H2", F20, "Challenge tracks"),
                             ("Body", F14, "Paragraph text at 16 px with 1.65 line height for long-form readability."),
                             ("Small", F12, "Captions, metadata and helper text (13 px).")]:
        d.text((50, y), label, font=F10, fill=(100, 116, 139))
        d.text((130, y - 6), sample, font=f, fill=INK)
        y += f.size + 26
    y += 10
    d.text((50, y), "Components", font=F20, fill=INK)
    y += 42
    box(d, 50, y, 160, 44, "Primary button", fill=(34, 211, 238), outline=(34, 211, 238), f=F12)
    box(d, 230, y, 160, 44, "Ghost button", fill=FILL, f=F12)
    box(d, 410, y, 110, 44, "Badge", fill=(207, 250, 254), outline=BRAND, f=F10)
    box(d, 540, y, 150, 44, "Filter pill", fill=(254, 243, 199), outline=(245, 158, 11), f=F10)
    box(d, 710, y, 140, 44, "Card (hover lift)", fill=FILL2, f=F10)
    y += 70
    box(d, 50, y, 800, 60, "Form field: label + input + hint + inline error message", fill=FILL, f=F12)
    y += 84
    caption(d, 50, y, "Spacing scale: 8 / 12 / 16 / 24 / 32 px. Radii: 8 px small, 14 px card, 999 px pill.")
    caption(d, 50, y + 26, "Breakpoints: 1180 px (navigation collapses to a hamburger), 860 px (single-column grids), 520 px (stacked footer).")
    img.save(os.path.join(OUT, "style-guide.png"))
    print("style-guide.png")


sitemap()
styleguide()
