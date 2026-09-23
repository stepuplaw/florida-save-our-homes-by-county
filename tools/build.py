"""Build data/counties.csv and data/counties.json (67 counties x roll years 2022 to 2026), plus
data/portability_by_county.csv (DOR Amendment 1 Impact report, portability sheets).

Inputs (all saved under data/sources/):
  extracted/databook_extract.csv          from tools/extract_databook.py
  nal_2026/nal_2026_homestead_summary.csv from tools/nal_summarize.py
  databook_current/amendment_1_impact.xlsx
"""
import csv, json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from xlsx import sheets

ROOT = os.path.join(os.path.dirname(__file__), "..")
SRC = os.path.join(ROOT, "data", "sources")
YEARS = [2022, 2023, 2024, 2025, 2026]
DB_URL = "https://floridarevenue.com/property/dataportal/Documents/PTO%20Data%20Portal/Databook%20Historical%20Data/{y}DataBookFiles/{f}"
CUR_URL = "https://floridarevenue.com/property/Documents/{f}"


def book_url(y, f):
    return CUR_URL.format(f=f) if y == 2026 else DB_URL.format(y=y, f=f)


def county_from_file(fn):
    c = re.sub(r"\s+\d+$", "", re.sub(r"\s+(Preliminary|Final) NAL 2026\.zip$", "", fn)).strip()
    return {"Dade": "Miami-Dade"}.get(c, c)


db = {(r["county"], int(r["year"])): r for r in csv.DictReader(open(os.path.join(SRC, "extracted", "databook_extract.csv")))}
nal = {}
for r in csv.DictReader(open(os.path.join(SRC, "nal_2026", "nal_2026_homestead_summary.csv"))):
    c = county_from_file(r["file"])
    # prefer a Final roll file over a Preliminary one if both exist
    if c not in nal or r["roll"] == "Final":
        nal[c] = r
counties = sorted({c for c, _ in db})
assert len(counties) == 67, len(counties)

rows = []
for c in counties:
    for y in YEARS:
        d = db[(c, y)]
        soh = int(float(d["soh_latest"])) if d["soh_latest"] else None
        src = [f"FDOR Property Tax Oversight, Data Book: county_overview.xlsx, sheet 'Save Our Homes Value History', column {y}"
               + (" (latest revision, as carried in the 2026 Data Book)" if y < 2026 else " (2026 preliminary roll)")]
        urls = [CUR_URL.format(f="county_overview.xlsx")]
        notes = []
        row = dict(county=c, year=y, homestead_parcels=None, homestead_just_value_total=None,
                   homestead_assessed_value_total=None, soh_differential_total=soh,
                   avg_soh_differential_per_homestead=None, avg_total_millage=None,
                   est_avg_annual_tax_saved=None)
        if y < 2026:
            row["avg_total_millage"] = float(d["total_millage"])
            src.append(f"FDOR Data Book {y}: millage_taxes_levied.xlsx, sheet 'Millage Rates', column 'Total Millage Rate'")
            urls.append(book_url(y, "millage_taxes_levied.xlsx"))
            notes.append(f"{y} final roll figures. Homestead parcel count and homestead just and assessed value totals are "
                         "not published by DOR for this year at county level (the Data Book has no homestead breakout and "
                         "DOR no longer hosts pre-2026 NAL roll files), so they, the per-homestead average and the tax "
                         "estimate are left blank.")
        else:
            n = nal.get(c)
            if n:
                hp = int(n["homestead_parcels"]); jv = int(n["homestead_just_value_total"]); av = int(n["homestead_assessed_value_total"])
                row.update(homestead_parcels=hp, homestead_just_value_total=jv, homestead_assessed_value_total=av)
                avg = (jv - av) / hp
                row["avg_soh_differential_per_homestead"] = round(avg)
                m25 = float(db[(c, 2025)]["total_millage"])
                row["est_avg_annual_tax_saved"] = round(avg * m25 / 1000)
                src.append(f"FDOR NAL roll file '{n['file']}' ({n['roll']} 2026 roll): parcels with JV_HMSTD > 0; "
                           "sums of JV_HMSTD and AV_HMSTD")
                urls.append(n["source_url"])
                src.append("FDOR Data Book 2025: millage_taxes_levied.xlsx 'Total Millage Rate' (used for the 2026 estimate)")
                urls.append(book_url(2025, "millage_taxes_levied.xlsx"))
                gap = (jv - av) / soh - 1 if soh else None
                notes.append(
                    f"2026 {n['roll'].lower()} roll. Homestead parcels = NAL parcels with JV_HMSTD > 0. "
                    f"avg_soh_differential_per_homestead = (homestead_just_value_total minus homestead_assessed_value_total) / "
                    f"homestead_parcels, all from the NAL; the NAL differential ({jv - av:,}) is {gap:+.1%} versus the Data Book "
                    f"soh_differential_total. avg_total_millage left blank: 2026 levies are not yet published by DOR. "
                    f"ESTIMATE: est_avg_annual_tax_saved = avg_soh_differential_per_homestead x 2025 DOR Total Millage Rate "
                    f"({m25}) / 1000.")
                if n["roll"] == "Final":
                    notes.append("Citrus 2026 preliminary NAL is not on the DOR portal; the 2026 final NAL was used.")
            else:
                notes.append("2026 NAL file for this county could not be retrieved; homestead fields blank.")
        row["source"] = " | ".join(src)
        row["source_url"] = " | ".join(urls)
        row["note"] = " ".join(notes)
        rows.append(row)

COLS = ["county", "year", "homestead_parcels", "homestead_just_value_total", "homestead_assessed_value_total",
        "soh_differential_total", "avg_soh_differential_per_homestead", "avg_total_millage",
        "est_avg_annual_tax_saved", "source", "source_url", "note"]
os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)
with open(os.path.join(ROOT, "data", "counties.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, COLS); w.writeheader()
    for r in rows:
        w.writerow({k: ("" if r[k] is None else r[k]) for k in COLS})
json.dump([{k: r[k] for k in COLS} for r in rows], open(os.path.join(ROOT, "data", "counties.json"), "w"), indent=1)

# ---- supplementary: portability (DOR Amendment 1 Impact report) ----
wb = sheets(os.path.join(SRC, "databook_current", "amendment_1_impact.xlsx"))
def series(sheet):
    rs = wb[sheet]
    hdr = [str(h).strip() if h is not None else "" for h in rs[3]]
    out = {}
    for r in rs[4:]:
        if r and isinstance(r[0], str) and len(r) > 3 and isinstance(r[2], (int, float)):
            r = r + [None] * 50
            name = {"Dade": "Miami-Dade"}.get(r[0].strip(), r[0].strip())
            out[name] = {y: r[hdr.index(f"{y} Value")] for y in YEARS if f"{y} Value" in hdr}
    return out
val, cnt = series("Portability Impact"), series("Portablity Counts")
with open(os.path.join(ROOT, "data", "portability_by_county.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["county", "year", "portability_transfers", "portability_value_total", "avg_value_ported_per_transfer",
                "source", "source_url", "note"])
    for c in counties:
        for y in YEARS:
            v, n = val.get(c, {}).get(y), cnt.get(c, {}).get(y)
            w.writerow([c, y, n if n is not None else "", v if v is not None else "",
                        round(v / n) if v and n else "",
                        "FDOR Data Book 2026: amendment_1_impact.xlsx, sheets 'Portability Impact' and 'Portablity Counts'",
                        CUR_URL.format(f="amendment_1_impact.xlsx"),
                        ("2026 preliminary roll. " if y == 2026 else "") +
                        "avg_value_ported_per_transfer = portability_value_total / portability_transfers (computed)."])
print("rows", len(rows), "with 2026 homestead data:", sum(1 for r in rows if r["homestead_parcels"]))
missing = [c for c in counties if c not in nal]
print("counties missing NAL:", missing)
print("portability counties:", len(val), len(cnt))
