"""Compare NAL-derived 2026 homestead differential with the Data Book 2026 SOH value by county."""
import csv, os, re

ROOT = os.path.join(os.path.dirname(__file__), "..", "data", "sources")
db = {r["county"]: float(r["soh_latest"]) for r in csv.DictReader(open(os.path.join(ROOT, "extracted", "databook_extract.csv"))) if r["year"] == "2026"}
for r in csv.DictReader(open(os.path.join(ROOT, "nal_2026", "nal_2026_homestead_summary.csv"))):
    c = re.sub(r"\s+\d+$", "", re.sub(r"\s+(Preliminary|Final) NAL 2026\.zip$", "", r["file"])).strip()
    c = {"Dade": "Miami-Dade"}.get(c, c)
    n = float(r["soh_differential_total"])
    b = db.get(c)
    print(f"{c:14s} {r['co_no']:>4} {r['roll']:12s} NAL={n:>18,.0f} DB={b:>18,.0f} diff={n/b-1:+.3%}  hs={r['homestead_parcels']} ex01={r['parcels_with_exmpt_01']}" if b else f"{c} not in databook")
