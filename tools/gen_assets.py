"""Generate SVG imagery, animated GIF and WAV audio for the APU CodeStorm 2026 site."""
import math
import os
import struct
import wave
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "website")
IMG = os.path.join(ROOT, "assets", "img")
MEDIA = os.path.join(ROOT, "assets", "media")
os.makedirs(IMG, exist_ok=True)
os.makedirs(MEDIA, exist_ok=True)

FONT = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_B = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"


def write(name, svg):
    with open(os.path.join(IMG, name), "w", encoding="utf-8") as f:
        f.write(svg.strip() + "\n")
    print("svg", name)


def gradient_svg(title, subtitle, c1, c2, w=800, h=600, icon="</>"):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{title}">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{c1}"/><stop offset="100%" stop-color="{c2}"/>
    </linearGradient>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M40 0H0V40" fill="none" stroke="rgba(255,255,255,.14)" stroke-width="1"/>
    </pattern>
  </defs>
  <rect width="{w}" height="{h}" fill="url(#g)"/>
  <rect width="{w}" height="{h}" fill="url(#grid)"/>
  <circle cx="{w*0.85}" cy="{h*0.2}" r="140" fill="rgba(255,255,255,.10)"/>
  <circle cx="{w*0.12}" cy="{h*0.85}" r="110" fill="rgba(0,0,0,.16)"/>
  <text x="60" y="{h*0.52}" font-family="Helvetica,Arial" font-size="86" font-weight="bold" fill="#ffffff" opacity=".92">{icon}</text>
  <text x="60" y="{h*0.70}" font-family="Helvetica,Arial" font-size="44" font-weight="bold" fill="#ffffff">{title}</text>
  <text x="60" y="{h*0.80}" font-family="Helvetica,Arial" font-size="24" fill="rgba(255,255,255,.85)">{subtitle}</text>
</svg>"""


# ---------------- Logo / brand ----------------
write("logo.svg", """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64" role="img" aria-label="APU CodeStorm logo">
  <defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#22d3ee"/><stop offset="100%" stop-color="#f59e0b"/></linearGradient></defs>
  <path d="M32 3 58 18v28L32 61 6 46V18z" fill="url(#lg)"/>
  <path d="M32 9 53 21v22L32 55 11 43V21z" fill="#0b1220"/>
  <text x="32" y="41" font-family="Helvetica,Arial" font-size="24" font-weight="bold" fill="#22d3ee" text-anchor="middle">&lt;/&gt;</text>
</svg>""")

write("favicon.svg", """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <path d="M16 2 29 9.5v13L16 30 3 22.5v-13z" fill="#22d3ee"/>
  <text x="16" y="21" font-family="Helvetica,Arial" font-size="14" font-weight="bold" fill="#0b1220" text-anchor="middle">&lt;/&gt;</text>
</svg>""")

write("hero.svg", """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 700" width="1600" height="700" role="img" aria-label="CodeStorm hero banner">
  <defs>
    <linearGradient id="h" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0b1220"/><stop offset="55%" stop-color="#10233d"/><stop offset="100%" stop-color="#0e7490"/>
    </linearGradient>
    <pattern id="hg" width="48" height="48" patternUnits="userSpaceOnUse">
      <path d="M48 0H0V48" fill="none" stroke="rgba(34,211,238,.13)"/>
    </pattern>
  </defs>
  <rect width="1600" height="700" fill="url(#h)"/>
  <rect width="1600" height="700" fill="url(#hg)"/>
  <circle cx="1320" cy="150" r="230" fill="rgba(34,211,238,.16)"/>
  <circle cx="1480" cy="520" r="170" fill="rgba(245,158,11,.14)"/>
  <g opacity=".55" fill="none" stroke="#22d3ee" stroke-width="3">
    <path d="M120 560h300M120 590h180M120 620h240"/>
  </g>
  <g font-family="Helvetica,Arial" fill="#e2e8f0" font-size="30">
    <text x="1130" y="300" fill="#22d3ee">&lt;hack&gt;</text>
    <text x="1130" y="350" fill="#f59e0b">48 hours</text>
    <text x="1130" y="400" fill="#94a3b8">&lt;/hack&gt;</text>
  </g>
</svg>""")

# ---------------- Gallery images ----------------
gallery = [
    ("Opening Ceremony", "Keynote &amp; brief reveal", "#0ea5e9", "#1e3a8a"),
    ("Team Formation", "Find your crew", "#8b5cf6", "#312e81"),
    ("Sprint Coding", "Hour 06 of 48", "#06b6d4", "#0f766e"),
    ("Mentor Session", "Industry guidance", "#f59e0b", "#7c2d12"),
    ("Debug Marathon", "Late night grind", "#22c55e", "#064e3b"),
    ("UI/UX Clinic", "Design critique", "#ec4899", "#581c87"),
    ("Lightning Demos", "60 second pitches", "#ef4444", "#450a0a"),
    ("Judging Round", "Panel evaluation", "#6366f1", "#1e1b4b"),
    ("Award Ceremony", "Winners revealed", "#eab308", "#422006"),
    ("Networking Night", "Sponsors &amp; students", "#14b8a6", "#042f2e"),
    ("Prototype Showcase", "Working demos", "#a855f7", "#3b0764"),
    ("Closing Remarks", "See you next year", "#0284c7", "#082f49"),
]
for i, (t, s, c1, c2) in enumerate(gallery, 1):
    write(f"gallery-{i:02d}.svg", gradient_svg(t, s, c1, c2, icon="{ }" if i % 2 else "//"))

# ---------------- Committee avatars ----------------
committee = [("NA", "#0ea5e9"), ("RK", "#8b5cf6"), ("TS", "#f59e0b"), ("AM", "#22c55e"),
             ("JD", "#ec4899"), ("LP", "#6366f1"), ("MF", "#14b8a6"), ("SR", "#ef4444")]
for initials, colour in committee:
    write(f"avatar-{initials.lower()}.svg", f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200" role="img" aria-label="{initials}">
  <defs><linearGradient id="a" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="{colour}"/><stop offset="100%" stop-color="#0b1220"/></linearGradient></defs>
  <rect width="200" height="200" rx="24" fill="url(#a)"/>
  <circle cx="100" cy="78" r="38" fill="rgba(255,255,255,.85)"/>
  <path d="M40 175c8-38 32-56 60-56s52 18 60 56z" fill="rgba(255,255,255,.85)"/>
  <text x="100" y="186" font-family="Helvetica,Arial" font-size="26" font-weight="bold" fill="#ffffff" text-anchor="middle">{initials}</text>
</svg>""")

# ---------------- Sponsor logos ----------------
sponsors = [("Nexlify", "#22d3ee"), ("ByteForge", "#f59e0b"), ("CloudNine", "#a78bfa"),
            ("DataPulse", "#34d399"), ("Quantum Labs", "#f472b6"), ("PixelWorks", "#60a5fa")]
for name, colour in sponsors:
    slug = name.lower().replace(" ", "-")
    write(f"sponsor-{slug}.svg", f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 120" width="320" height="120" role="img" aria-label="{name} sponsor logo">
  <rect x="2" y="2" width="316" height="116" rx="16" fill="#0f172a" stroke="{colour}" stroke-width="2"/>
  <circle cx="52" cy="60" r="22" fill="{colour}"/>
  <path d="M44 60l8-12 8 12-8 12z" fill="#0f172a"/>
  <text x="90" y="70" font-family="Helvetica,Arial" font-size="30" font-weight="bold" fill="#e2e8f0">{name}</text>
</svg>""")

# ---------------- Past event / highlight images ----------------
past = [("CodeStorm 2025", "42 teams, 300 participants", "#0f766e", "#0b1220"),
        ("CodeStorm 2024", "First all-female winning team", "#7c3aed", "#0b1220"),
        ("CodeStorm 2023", "Launch edition on campus", "#b45309", "#0b1220")]
for i, (t, s, c1, c2) in enumerate(past, 1):
    write(f"past-{i}.svg", gradient_svg(t, s, c1, c2, w=700, h=500, icon="*"))

# ---------------- Wide banner images for content pages ----------------
banners = [("schedule-banner", "48 Hour Timeline", "#1d4ed8", "#0b1220"),
           ("register-banner", "Register Your Team", "#047857", "#0b1220"),
           ("faq-banner", "Questions Answered", "#b91c1c", "#0b1220"),
           ("contact-banner", "Get In Touch", "#6d28d9", "#0b1220")]
for name, t, c1, c2 in banners:
    write(f"{name}.svg", gradient_svg(t, "APU CodeStorm 2026", c1, c2, w=1600, h=420, icon="#"))


# ---------------- Animated GIF highlight reel ----------------
def make_gif():
    frames = []
    W, H = 640, 360
    labels = ["48 HOURS", "6 TRACKS", "128 TEAMS", "RM 20,000 PRIZES", "BUILD. BREAK. BREAKTHROUGH."]
    try:
        fb = ImageFont.truetype(FONT_B, 34)
        fs = ImageFont.truetype(FONT, 20)
    except OSError:
        fb = fs = ImageFont.load_default()
    for idx in range(20):
        img = Image.new("RGB", (W, H))
        d = ImageDraw.Draw(img)
        for y in range(H):
            t = y / H
            d.line([(0, y), (W, y)], fill=(int(11 + 14 * t), int(18 + 40 * t), int(32 + 110 * t)))
        for gx in range(0, W, 40):
            d.line([(gx, 0), (gx, H)], fill=(30, 60, 90))
        for gy in range(0, H, 40):
            d.line([(0, gy), (W, gy)], fill=(30, 60, 90))
        band = int((idx / 20) * (W + 240)) - 240
        d.rectangle([band, 130, band + 240, 230], fill=(34, 211, 238))
        label = labels[idx % len(labels)]
        tw = d.textlength(label, font=fb)
        d.text(((W - tw) / 2, 152), label, font=fb, fill=(11, 18, 32))
        sub = "APU CodeStorm 2026 Highlights"
        sw = d.textlength(sub, font=fs)
        d.text(((W - sw) / 2, 250), sub, font=fs, fill=(226, 232, 240))
        frames.append(img.convert("P", palette=Image.ADAPTIVE, colors=64))
    frames[0].save(os.path.join(MEDIA, "highlights.gif"), save_all=True, append_images=frames[1:],
                   duration=90, loop=0, optimize=True)
    print("gif highlights.gif")


make_gif()


# ---------------- WAV audio: event anthem loop ----------------
def make_wav():
    rate = 44100
    seconds = 8.0
    notes = [261.63, 329.63, 392.00, 523.25, 392.00, 329.63]  # C major arpeggio
    frames = bytearray()
    total = int(rate * seconds)
    step = rate // 4
    for i in range(total):
        seg = (i // step) % len(notes)
        f = notes[seg]
        t = (i % step) / rate
        env = min(1.0, t * 12) * math.exp(-2.2 * t)
        v = 0.42 * env * (math.sin(2 * math.pi * f * i / rate) +
                          0.35 * math.sin(4 * math.pi * f * i / rate))
        sample = int(max(-1.0, min(1.0, v)) * 32767)
        frames += struct.pack("<hh", sample, sample)
    with wave.open(os.path.join(MEDIA, "codestorm-anthem.wav"), "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(rate)
        w.writeframes(bytes(frames))
    print("wav codestorm-anthem.wav")


make_wav()
print("done")
