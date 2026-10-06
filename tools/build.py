"""Assemble the remaining static pages from a shared header/footer (extracted from index.html)."""
import os
import re

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "website")
FRAG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fragments")

index = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
HEADER = re.search(r'<header class="site-header">.*?</header>', index, re.S).group(0)
FOOTER = re.search(r'<footer class="site-footer">.*?</footer>', index, re.S).group(0)
BUTTON = re.search(r'<button class="to-top".*?</button>', index, re.S).group(0)

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{desc}">
  <meta name="author" content="APU CodeStorm 2026 Organising Committee">
  <title>{title}</title>
  <link rel="icon" type="image/svg+xml" href="assets/img/favicon.svg">
  <link rel="stylesheet" href="css/style.css">
  <script src="js/main.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to main content</a>

{header}

{main}

{footer}

  {button}
</body>
</html>
"""

for name in sorted(os.listdir(FRAG)):
    if not name.endswith(".frag"):
        continue
    raw = open(os.path.join(FRAG, name), encoding="utf-8").read()
    title = re.search(r"<!--TITLE:\s*(.*?)\s*-->", raw, re.S).group(1)
    desc = re.search(r"<!--DESC:\s*(.*?)\s*-->", raw, re.S).group(1).replace("\n", " ")
    main = re.sub(r"<!--(?:TITLE|DESC):.*?-->", "", raw, flags=re.S).strip()
    main = '<main id="main">\n' + main + '\n  </main>'
    out = TEMPLATE.format(title=title, desc=desc, header=HEADER, main=main,
                          footer=FOOTER, button=BUTTON)
    path = os.path.join(ROOT, name.replace(".frag", ".html"))
    open(path, "w", encoding="utf-8").write(out)
    print("built", os.path.basename(path))
