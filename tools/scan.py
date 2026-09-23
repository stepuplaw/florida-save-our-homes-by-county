"""Scan all saved xlsx for cells matching a regex; print file, sheet, row, cell."""
import sys, os, re, glob
sys.path.insert(0, os.path.dirname(__file__))
from xlsx import sheets

pat = re.compile(sys.argv[1], re.I)
root = os.path.join(os.path.dirname(__file__), "..", "data", "sources")
for p in sorted(glob.glob(os.path.join(root, "*", "*.xlsx"))):
    if "amendment_1" in p and "--all" not in sys.argv:
        continue
    for name, rows in sheets(p).items():
        for i, r in enumerate(rows[:12]):
            for c in r:
                if isinstance(c, str) and pat.search(c):
                    print(os.path.relpath(p, root), "|", name, "| r", i, "|", c.replace("\n", " ")[:120])
