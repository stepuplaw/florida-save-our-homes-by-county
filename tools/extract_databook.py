"""Extract per-county, per-year Data Book figures used in the dataset.

Writes data/sources/extracted/databook_extract.csv with, for each county and roll year 2021 to 2026:
  soh_latest        SOH differential from the newest county_overview.xlsx "Save Our Homes Value History"
                    (databook_current, which carries the latest revision of every year)
  soh_own_book      SOH differential as first published in that year's own Data Book
  status            roll status label in that year's county_overview "Statewide Property Value" sheet
  total_millage     "Total Millage Rate" in that year's millage_taxes_levied.xlsx "Millage Rates"
  countywide_millage, school_millage (operating + debt), aggregate_millage (less than county-wide)
"""
import csv, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from xlsx import sheets

ROOT = os.path.join(os.path.dirname(__file__), "..", "data", "sources")
OUT = os.path.join(ROOT, "extracted")
os.makedirs(OUT, exist_ok=True)
BOOK = {2021: "databook_2021", 2022: "databook_2022", 2023: "databook_2023",
        2024: "databook_2024", 2025: "databook_2025", 2026: "databook_current"}


def county_rows(rows, start=4):
    for r in rows[start:]:
        if r and isinstance(r[0], str) and r[0].strip() and not r[0].strip().lower().startswith(("total", "state", "*", "note", "source", "contact")):
            if len(r) > 2 and any(isinstance(v, (int, float)) for v in r[1:]):
                yield norm(r[0]), r + [None] * 40


def norm(name):
    """DOR tables label Miami-Dade as 'Dade' in millage tables and add footnote digits ('Orange1')."""
    n = re.sub(r"[\d*]+$", "", name.strip()).strip()
    return {"Dade": "Miami-Dade", "St. Johns": "Saint Johns", "St. Lucie": "Saint Lucie",
            "St Johns": "Saint Johns", "St Lucie": "Saint Lucie", "Desoto": "DeSoto"}.get(n, n)


def by_header(rows, hdr_row=3):
    return {str(h).strip(): i for i, h in enumerate(rows[hdr_row]) if h is not None}


latest = sheets(os.path.join(ROOT, "databook_current", "county_overview.xlsx"))["Save Our Homes Value History"]
lh = by_header(latest)
soh_latest = {(c, y): r[lh[str(y)]] for c, r in county_rows(latest) for y in BOOK if str(y) in lh}

out = []
for y, d in BOOK.items():
    co = sheets(os.path.join(ROOT, d, "county_overview.xlsx"))
    own = co["Save Our Homes Value History"]
    oh = by_header(own)
    own_v = {c: r[oh[str(y)]] for c, r in county_rows(own)}
    status = {c: r[1] for c, r in county_rows(co["Statewide Property Value"])}
    mill = {}
    if d != "databook_current":  # current book's millage table is still the 2025 levy
        m = sheets(os.path.join(ROOT, d, "millage_taxes_levied.xlsx"))["Millage Rates"]
        assert m[1][0] == y, (d, m[1][0])
        hdr = [str(h).strip() if h else "" for h in m[3]]
        for c, r in county_rows(m):
            r = r + [None] * (len(hdr) - len(r))
            g = lambda i: r[i] or 0
            mill[c] = dict(total_millage=r[hdr.index("Total Millage Rate")],
                           countywide_millage=r[hdr.index("Sub Total (County Wide Millage)")],
                           school_millage=g(hdr.index("School Board Operating")) + g(hdr.index("School Board Debt Service")),
                           aggregate_millage=r[hdr.index("Sub Total (Aggregate Millage)")])
    for c in own_v:
        row = dict(county=c, year=y, status=status.get(c), soh_latest=soh_latest.get((c, y)),
                   soh_own_book=own_v[c], millage_book=d if mill else "")
        row.update(mill.get(c, {}))
        out.append(row)

cols = ["county", "year", "status", "soh_latest", "soh_own_book", "total_millage", "countywide_millage",
        "school_millage", "aggregate_millage", "millage_book"]
with open(os.path.join(OUT, "databook_extract.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, cols); w.writeheader(); w.writerows(out)
from collections import Counter
print(Counter(r["year"] for r in out))
print(sorted({r["county"] for r in out}))
