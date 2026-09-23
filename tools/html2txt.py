"""Strip tags from an html file and print text lines matching an optional regex (with context)."""
import sys, re, html

t = open(sys.argv[1], encoding="utf-8", errors="replace").read()
t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</li>", "\n", t)
t = html.unescape(re.sub(r"<[^>]+>", " ", t))
t = "\n".join(re.sub(r"[ \t\xa0]+", " ", l).strip() for l in t.splitlines())
t = re.sub(r"\n{2,}", "\n", t)
if len(sys.argv) > 2:
    pat = re.compile(sys.argv[2], re.I)
    for m in pat.finditer(t):
        print("...", t[max(0, m.start() - int(sys.argv[3] if len(sys.argv) > 3 else 300)):m.end() + 1500], "\n----")
else:
    print(t)
