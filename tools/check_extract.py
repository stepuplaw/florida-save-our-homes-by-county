import csv, os
p = os.path.join(os.path.dirname(__file__), "..", "data", "sources", "extracted", "databook_extract.csv")
rows = list(csv.DictReader(open(p)))
for r in rows:
    if r["year"] != "2026" and not r["total_millage"]:
        print("no millage", r["county"], r["year"])
    if not r["soh_latest"]:
        print("no soh", r["county"], r["year"])
    elif r["soh_own_book"] and r["soh_latest"] != r["soh_own_book"]:
        a, b = float(r["soh_latest"]), float(r["soh_own_book"])
        if b and abs(a / b - 1) > 0.01:
            print(f"revision >1%: {r['county']} {r['year']} latest={a:,.0f} own={b:,.0f} ({a/b-1:+.2%})")
print({r["year"]: r["status"] for r in rows if r["county"] == "Alachua"})
