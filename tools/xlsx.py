"""Minimal stdlib xlsx reader: sheets(path) -> {sheet_name: [[cell values]]}."""
import zipfile, re, sys
import xml.etree.ElementTree as ET

NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
      "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
      "pr": "http://schemas.openxmlformats.org/package/2006/relationships"}


def _col(ref):
    letters = re.match(r"[A-Z]+", ref).group(0)
    n = 0
    for ch in letters:
        n = n * 26 + ord(ch) - 64
    return n - 1


def sheets(path):
    z = zipfile.ZipFile(path)
    shared = []
    if "xl/sharedStrings.xml" in z.namelist():
        root = ET.fromstring(z.read("xl/sharedStrings.xml"))
        for si in root.findall("m:si", NS):
            shared.append("".join(t.text or "" for t in si.iter("{%s}t" % NS["m"])))
    wb = ET.fromstring(z.read("xl/workbook.xml"))
    rels = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
    target = {r.get("Id"): r.get("Target") for r in rels.findall("pr:Relationship", NS)}
    out = {}
    for s in wb.find("m:sheets", NS).findall("m:sheet", NS):
        rid = s.get("{%s}id" % NS["r"])
        t = target[rid].lstrip("/")
        t = t if t.startswith("xl/") else "xl/" + t
        root = ET.fromstring(z.read(t))
        rows = []
        for row in root.iter("{%s}row" % NS["m"]):
            vals = {}
            for c in row.findall("m:c", NS):
                typ = c.get("t")
                v = c.find("m:v", NS)
                if typ == "s" and v is not None:
                    val = shared[int(v.text)]
                elif typ == "inlineStr":
                    val = "".join(x.text or "" for x in c.iter("{%s}t" % NS["m"]))
                elif v is not None:
                    val = v.text
                    try:
                        f = float(val)
                        val = int(f) if f.is_integer() else f
                    except ValueError:
                        pass
                else:
                    val = None
                vals[_col(c.get("r"))] = val
            if vals:
                r = [None] * (max(vals) + 1)
                for k, v in vals.items():
                    r[k] = v
                rows.append(r)
            else:
                rows.append([])
        out[s.get("name")] = rows
    return out


if __name__ == "__main__":
    # usage: xlsx.py file [sheet_substring] [maxrows]
    p = sys.argv[1]
    sub = sys.argv[2] if len(sys.argv) > 2 else None
    mx = int(sys.argv[3]) if len(sys.argv) > 3 else 15
    for name, rows in sheets(p).items():
        if sub and sub.lower() not in name.lower():
            continue
        print(f"=== {name}  ({len(rows)} rows)")
        for r in rows[:mx]:
            print("  ", r)
