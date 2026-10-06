"""Verify the website: internal links, assets, required elements, basic HTML well-formedness."""
import os
import re
from html.parser import HTMLParser

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "website")
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}


class Check(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []
        self.refs = []
        self.ids = set()
        self.dup_ids = set()
        self.imgs = 0
        self.imgs_no_alt = 0

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if "id" in d:
            if d["id"] in self.ids:
                self.dup_ids.add(d["id"])
            self.ids.add(d["id"])
        if tag == "img":
            self.imgs += 1
            if "alt" not in d:
                self.imgs_no_alt += 1
        for key in ("href", "src", "data-full", "poster"):
            v = d.get(key)
            if v:
                self.refs.append(v)
        if tag not in VOID:
            self.stack.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.errors.append(f"stray </{tag}> at {self.getpos()}")
            return
        open_tag, pos = self.stack.pop()
        if open_tag != tag:
            self.errors.append(f"mismatched </{tag}> at {self.getpos()} (opened <{open_tag}> at {pos})")


pages = sorted(f for f in os.listdir(ROOT) if f.endswith(".html"))
problems = []
print(f"{len(pages)} pages found\n")

for page in pages:
    html = open(os.path.join(ROOT, page), encoding="utf-8").read()
    c = Check()
    c.feed(html)
    if c.stack:
        c.errors.append("unclosed: " + ", ".join(f"<{t}>@{p}" for t, p in c.stack))
    for e in c.errors:
        problems.append(f"{page}: {e}")
    if c.dup_ids:
        problems.append(f"{page}: duplicate ids {c.dup_ids}")
    if c.imgs_no_alt:
        problems.append(f"{page}: {c.imgs_no_alt} img without alt")
    for needle, label in [
        ('<header class="site-header">', "header"),
        ('<footer class="site-footer">', "footer"),
        ('css/style.css', "stylesheet"),
        ('js/main.js', "script"),
        ('id="primary-nav"', "nav"),
        ('class="skip-link"', "skip link"),
        ('<title>', "title"),
        ('name="description"', "meta description"),
    ]:
        if needle not in html:
            problems.append(f"{page}: missing {label}")
    # local reference check
    for ref in c.refs:
        if ref.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:", "javascript:")):
            if ref.startswith("#") and len(ref) > 1 and ref[1:] not in c.ids:
                problems.append(f"{page}: anchor {ref} not found on page")
            continue
        target = ref.split("#")[0].split("?")[0]
        if not target:
            continue
        path = os.path.normpath(os.path.join(ROOT, target))
        if not os.path.exists(path):
            problems.append(f"{page}: broken reference -> {ref}")

# pages linked from nav/footer
index = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
linked = set(re.findall(r'href="([^"#]+\.html)"', index))
missing_links = linked - set(pages)
if missing_links:
    problems.append(f"index links to non-existent pages: {missing_links}")

# pages not linked from index at all
orphans = set(pages) - linked - {"index.html"}
if orphans:
    problems.append(f"orphan pages (not linked from home): {sorted(orphans)}")

if problems:
    print("PROBLEMS:")
    for p in problems:
        print(" -", p)
else:
    print("All checks passed: links, assets, structure, alt text, nav/footer, anchors.")
