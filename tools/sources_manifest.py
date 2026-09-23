#!/usr/bin/env python3
"""Write data/sources/manifest.csv and refresh data/sources/manifest.json.

Every source file is listed with the DOR (or Legislature) URL it was downloaded
from, its size, its SHA-256 and when it was retrieved. Files kept in this
repository are hashed from disk, so the manifest cannot drift from them.

The 67 county NAL roll files (about 825 MB, nal_2026/raw/) are NOT in the
repository. Their rows come from the manifest written when they were downloaded
(tools/nal_summarize.py), so anyone can fetch the same files from DOR and check
the hash before rerunning the build.

    python3 tools/sources_manifest.py
"""
import csv, hashlib, json, os

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
SRC = os.path.join(ROOT, "data", "sources")
MANIFEST = os.path.join(SRC, "manifest.json")

# Saved law texts were renamed for the repository (the originals had no extension
# or a '#' in the name). Old manifest key -> repository path.
RENAME = {
    "law/193.155": "law/193.155-2025.html",
    "law/Constitution": "law/fl_constitution.html",
}
DROP = {"law/Constitution#A7S04"}  # second copy of the same Constitution page
EXTRA = {  # derived files kept beside the sources, no download URL
    "law/0193.155.txt": "text extracted from law/0193.155.html by tools/html2txt.py",
    "extracted/databook_extract.csv": "built by tools/extract_databook.py from the Data Book workbooks",
    "nal_2026/nal_2026_homestead_summary.csv": "built by tools/nal_summarize.py from the NAL roll files",
}

old = json.load(open(MANIFEST))
out = {}
for k, v in old.items():
    if k in DROP:
        continue
    k = RENAME.get(k, k)
    out[k] = dict(v)
for k, v in out.items():
    p = os.path.join(SRC, k)
    if os.path.exists(p):
        data = open(p, "rb").read()
        v["bytes"], v["sha256"] = len(data), hashlib.sha256(data).hexdigest()
        v["in_repository"] = True
    else:
        if not k.startswith("nal_2026/raw/"):
            raise SystemExit(f"{k} is in the manifest but missing from disk")
        v["in_repository"] = False
for k, note in EXTRA.items():
    data = open(os.path.join(SRC, k), "rb").read()
    out[k] = {"url": "", "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
              "retrieved": "", "in_repository": True, "note": note}

json.dump(out, open(MANIFEST, "w"), indent=1, sort_keys=True)
with open(os.path.join(SRC, "manifest.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["path", "in_repository", "bytes", "sha256", "retrieved", "url", "note"])
    for k in sorted(out):
        v = out[k]
        w.writerow([k, "yes" if v["in_repository"] else "no", v["bytes"], v["sha256"],
                    v.get("retrieved", ""), v.get("url", ""), v.get("note", "")])
n_out = sum(1 for v in out.values() if not v["in_repository"])
print(f"{len(out)} files, {n_out} not in the repository "
      f"({sum(v['bytes'] for v in out.values() if not v['in_repository']):,} bytes)")
