"""Download each 2026 county NAL zip from the DOR data portal and summarize homestead fields.

Output: data/sources/nal_2026/nal_2026_homestead_summary.csv (one row per county file), appended
as each county finishes so the run can resume.

Homestead parcel = a real property parcel with JV_HMSTD > 0 (the NAL field "Just Value, Homestead
Property", i.e. value subject to the s. 193.155 Save Our Homes cap).
"""
import csv, io, os, sys, zipfile, json, urllib.request, urllib.parse
sys.path.insert(0, os.path.dirname(__file__))

BASE = os.path.join(os.path.dirname(__file__), "..", "data", "sources", "nal_2026")
OUT = os.path.join(BASE, "nal_2026_homestead_summary.csv")
FOLDERS = ["/property/dataportal/Documents/PTO Data Portal/Tax Roll Data Files/NAL/2026P",
           "/property/dataportal/Documents/PTO Data Portal/Tax Roll Data Files/NAL/2026F"]
COLS = ["file", "roll", "co_no", "asmnt_yr", "parcels_all", "homestead_parcels",
        "homestead_just_value_total", "homestead_assessed_value_total", "soh_differential_total",
        "parcels_with_exmpt_01", "jv_all", "av_nsd_all", "source_url"]


def list_files(folder):
    url = ("https://floridarevenue.com/property/dataportal/_api/web/GetFolderByServerRelativeUrl('%s')/Files"
           % urllib.parse.quote(folder))
    req = urllib.request.Request(url, headers={"Accept": "application/json;odata=verbose", "User-Agent": "Mozilla/5.0"})
    return [f["ServerRelativeUrl"] for f in json.load(urllib.request.urlopen(req, timeout=120))["d"]["results"]]


def num(s):
    s = (s or "").strip()
    return int(float(s)) if s else 0


def summarize(path):
    z = zipfile.ZipFile(path)
    name = [n for n in z.namelist() if n.lower().endswith((".csv", ".txt"))][0]
    s = dict(parcels_all=0, homestead_parcels=0, homestead_just_value_total=0,
             homestead_assessed_value_total=0, parcels_with_exmpt_01=0, jv_all=0, av_nsd_all=0)
    co, yr = set(), set()
    with z.open(name) as fh:
        rd = csv.DictReader(io.TextIOWrapper(fh, encoding="latin-1", newline=""))
        rd.fieldnames = [f.strip() for f in rd.fieldnames]
        for r in rd:
            s["parcels_all"] += 1
            co.add(r["CO_NO"].strip()); yr.add(r["ASMNT_YR"].strip())
            jvh = num(r["JV_HMSTD"])
            s["jv_all"] += num(r["JV"]); s["av_nsd_all"] += num(r["AV_NSD"])
            if num(r.get("EXMPT_01")) > 0:
                s["parcels_with_exmpt_01"] += 1
            if jvh > 0:
                s["homestead_parcels"] += 1
                s["homestead_just_value_total"] += jvh
                s["homestead_assessed_value_total"] += num(r["AV_HMSTD"])
    s["soh_differential_total"] = s["homestead_just_value_total"] - s["homestead_assessed_value_total"]
    s["co_no"] = "/".join(sorted(co)); s["asmnt_yr"] = "/".join(sorted(yr))
    return s


done = set()
if os.path.exists(OUT):
    done = {r["file"] for r in csv.DictReader(open(OUT))}
else:
    with open(OUT, "w", newline="") as f:
        csv.writer(f).writerow(COLS)

import threading, shutil, hashlib, datetime
from concurrent.futures import ThreadPoolExecutor

LOCK = threading.Lock()
RAW = os.path.join(BASE, "raw")
MANIFEST = os.path.join(BASE, "..", "manifest.json")
os.makedirs(RAW, exist_ok=True)


def download(url, fn):
    """Stream to a .part file and rename when complete, so partial files are never used."""
    path = os.path.join(RAW, fn)
    if not os.path.exists(path):
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (research dataset build)"})
        with urllib.request.urlopen(req, timeout=600) as r, open(path + ".part", "wb") as f:
            shutil.copyfileobj(r, f, 1 << 20)
        os.replace(path + ".part", path)
    h = hashlib.sha256(open(path, "rb").read()).hexdigest()
    with LOCK:
        m = json.load(open(MANIFEST)) if os.path.exists(MANIFEST) else {}
        m["nal_2026/raw/" + fn] = {"url": url, "bytes": os.path.getsize(path), "sha256": h,
                                   "retrieved": datetime.datetime.now().isoformat(timespec="seconds")}
        json.dump(m, open(MANIFEST, "w"), indent=1, sort_keys=True)
    return path


def job(task):
    fn, roll, url = task
    try:
        s = summarize(download(url, fn))
    except Exception as e:
        print("FAIL", fn, e, flush=True)
        return
    s.update(file=fn, roll=roll, source_url=url)
    with LOCK:
        with open(OUT, "a", newline="") as f:
            csv.writer(f).writerow([s[c] for c in COLS])
    print("done", fn, s["homestead_parcels"], s["soh_differential_total"], flush=True)


tasks = []
for folder in FOLDERS:
    roll = "Final" if folder.endswith("F") else "Preliminary"
    for sru in list_files(folder):
        fn = sru.split("/")[-1]
        if fn not in done:
            tasks.append((fn, roll, "https://floridarevenue.com" + urllib.parse.quote(sru)))
print(len(tasks), "files to process", flush=True)
with ThreadPoolExecutor(int(os.environ.get("WORKERS", "16"))) as ex:
    list(ex.map(job, tasks))
