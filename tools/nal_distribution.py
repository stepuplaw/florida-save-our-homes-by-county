"""Per-county distribution of the parcel-level SOH differential (JV_HMSTD minus AV_HMSTD) among homestead
parcels (JV_HMSTD > 0) in the saved 2026 NAL zips. Writes data/distribution_2026.csv.

These are descriptive statistics of the DOR NAL roll, not estimates.
"""
import csv, io, os, sys, zipfile, glob, re

ROOT = os.path.join(os.path.dirname(__file__), "..")
RAW = os.path.join(ROOT, "data", "sources", "nal_2026", "raw")
OUT = os.path.join(ROOT, "data", "distribution_2026.csv")
CAP = 500_000


def num(s):
    s = (s or "").strip()
    return int(float(s)) if s else 0


def pct(sorted_vals, q):
    if not sorted_vals:
        return ""
    k = (len(sorted_vals) - 1) * q
    lo, hi = int(k), min(int(k) + 1, len(sorted_vals) - 1)
    return round(sorted_vals[lo] + (sorted_vals[hi] - sorted_vals[lo]) * (k - lo))


COLS = ["county", "nal_file", "roll", "homestead_parcels", "median_soh_differential", "p25_soh_differential",
        "p75_soh_differential", "p90_soh_differential", "p99_soh_differential", "max_soh_differential",
        "share_with_zero_differential", "parcels_differential_over_500k", "share_over_500k",
        "differential_above_500k_total", "median_homestead_just_value", "median_homestead_assessed_value"]
names = {r["file"]: r for r in csv.DictReader(open(os.path.join(ROOT, "data", "sources", "nal_2026", "nal_2026_homestead_summary.csv")))}
rows = []
for p in sorted(glob.glob(os.path.join(RAW, "*.zip"))):
    fn = os.path.basename(p)
    z = zipfile.ZipFile(p)
    name = [n for n in z.namelist() if n.lower().endswith((".csv", ".txt"))][0]
    d, jv, av = [], [], []
    with z.open(name) as fh:
        rd = csv.DictReader(io.TextIOWrapper(fh, encoding="latin-1", newline=""))
        rd.fieldnames = [f.strip() for f in rd.fieldnames]
        for r in rd:
            j = num(r["JV_HMSTD"])
            if j > 0:
                a = num(r["AV_HMSTD"])
                d.append(j - a); jv.append(j); av.append(a)
    d.sort(); jv.sort(); av.sort()
    n = len(d)
    over = [x for x in d if x > CAP]
    county = re.sub(r"\s+\d+$", "", re.sub(r"\s+(Preliminary|Final) NAL 2026\.zip$", "", fn)).strip()
    county = {"Dade": "Miami-Dade"}.get(county, county)
    rows.append(dict(county=county, nal_file=fn, roll=names.get(fn, {}).get("roll", ""), homestead_parcels=n,
                     median_soh_differential=pct(d, .5), p25_soh_differential=pct(d, .25),
                     p75_soh_differential=pct(d, .75), p90_soh_differential=pct(d, .9),
                     p99_soh_differential=pct(d, .99), max_soh_differential=d[-1] if d else "",
                     share_with_zero_differential=round(sum(1 for x in d if x <= 0) / n, 4) if n else "",
                     parcels_differential_over_500k=len(over), share_over_500k=round(len(over) / n, 4) if n else "",
                     differential_above_500k_total=sum(x - CAP for x in over),
                     median_homestead_just_value=pct(jv, .5), median_homestead_assessed_value=pct(av, .5)))
    print(county, n, rows[-1]["median_soh_differential"], flush=True)
rows.sort(key=lambda r: r["county"])
with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, COLS); w.writeheader(); w.writerows(rows)
