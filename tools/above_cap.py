"""Estimated annual tax on differential above the $500,000 portability cap, per county (2026 NAL, 2025 millage)."""
import csv, os
D = os.path.join(os.path.dirname(__file__), "..", "data")
dist = {r["county"]: r for r in csv.DictReader(open(os.path.join(D, "distribution_2026.csv")))}
mill = {r["county"]: float(r["avg_total_millage"]) for r in csv.DictReader(open(os.path.join(D, "counties.csv"))) if r["year"] == "2025"}
out = []
for c, d in dist.items():
    n = int(d["parcels_differential_over_500k"])
    tot = int(d["differential_above_500k_total"])
    tax = tot * mill[c] / 1000
    out.append((tax, c, n, tot, tax / n if n else 0))
print("| County | Homesteads over $500k | Differential above cap | Est. annual tax on it (2025 mills) | Per affected homestead |")
print("|---|---|---|---|---|")
for tax, c, n, tot, per in sorted(out, reverse=True)[:12]:
    print(f"| {c} | {n:,} | ${tot:,.0f} | ${tax:,.0f} | ${per:,.0f} |")
print("statewide tax above cap:", f"${sum(o[0] for o in out):,.0f}")
