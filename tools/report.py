"""Print markdown tables and facts used in FINDINGS.md, computed only from data/*.csv."""
import csv, os
ROOT = os.path.join(os.path.dirname(__file__), "..", "data")
rows = list(csv.DictReader(open(os.path.join(ROOT, "counties.csv"))))
dist = {r["county"]: r for r in csv.DictReader(open(os.path.join(ROOT, "distribution_2026.csv")))} if os.path.exists(os.path.join(ROOT, "distribution_2026.csv")) else {}
port = list(csv.DictReader(open(os.path.join(ROOT, "portability_by_county.csv"))))
f = lambda v: float(v) if v not in ("", None) else None
by = {(r["county"], int(r["year"])): r for r in rows}
counties = sorted({r["county"] for r in rows})
money = lambda v: "" if v is None else f"${v:,.0f}"

print("## A. 2026 ranking by estimated annual tax saved per average homestead\n")
print("| Rank | County | Homestead parcels | SOH differential total (DOR) | Avg differential per homestead | Median differential | 2025 total mills | Est. avg annual tax saved | Est. tax saved at median | Homesteads over $500k |")
print("|---|---|---|---|---|---|---|---|---|---|")
lat = sorted([by[(c, 2026)] for c in counties if f(by[(c, 2026)]["est_avg_annual_tax_saved"]) is not None],
             key=lambda r: -f(r["est_avg_annual_tax_saved"]))
for i, r in enumerate(lat, 1):
    d = dist.get(r["county"], {})
    print(f"| {i} | {r['county']} | {int(r['homestead_parcels']):,} | {money(f(r['soh_differential_total']))} | "
          f"{money(f(r['avg_soh_differential_per_homestead']))} | {money(f(d.get('median_soh_differential')))} | "
          f"{f(by[(r['county'], 2025)]['avg_total_millage']):.4f} | {money(f(r['est_avg_annual_tax_saved']))} | "
          f"{money(f(d['median_soh_differential']) * f(by[(r['county'], 2025)]['avg_total_millage']) / 1000)} | "
          f"{int(d['parcels_differential_over_500k']):,} ({float(d['share_over_500k']):.1%}) |" if d else "| |")

print("\n## B. SOH differential total, change over five years\n")
print("| County | 2022 | 2023 | 2024 | 2025 | 2026 prelim | Change 2022 to 2026 | Change 2025 to 2026 |")
print("|---|---|---|---|---|---|---|---|")
ch = []
for c in counties:
    v = {y: f(by[(c, y)]["soh_differential_total"]) for y in range(2022, 2027)}
    ch.append((c, v, v[2026] / v[2022] - 1, v[2026] / v[2025] - 1))
for c, v, a, b in sorted(ch, key=lambda t: -t[2]):
    print(f"| {c} | " + " | ".join(money(v[y]) for y in range(2022, 2027)) + f" | {a:+.1%} | {b:+.1%} |")
st = {y: sum(f(by[(c, y)]["soh_differential_total"]) for c in counties) for y in range(2022, 2027)}
print("\nStatewide sum of county SOH:", {y: money(v) for y, v in st.items()})
print("Counties where 2026 SOH < 2025 SOH:", sum(1 for t in ch if t[3] < 0), "of 67")
print("Counties where 2026 SOH < 2022 SOH:", sum(1 for t in ch if t[2] < 0))
print("Peak year per county:", __import__("collections").Counter(max(v, key=v.get) for _, v, _, _ in ch))

print("\n## C. Millage 2022 to 2025\n")
for c in counties:
    m = [f(by[(c, y)]["avg_total_millage"]) for y in range(2022, 2026)]
    if max(m) - min(m) > 1.5:
        print(c, m)
ml = sorted(((f(by[(c, 2025)]["avg_total_millage"]), c) for c in counties))
print("lowest 2025:", ml[:5], "\nhighest 2025:", ml[-5:])

print("\n## D. Statewide 2026 (NAL)\n")
hp = sum(int(by[(c, 2026)]["homestead_parcels"] or 0) for c in counties)
jv = sum(int(by[(c, 2026)]["homestead_just_value_total"] or 0) for c in counties)
av = sum(int(by[(c, 2026)]["homestead_assessed_value_total"] or 0) for c in counties)
print(f"homestead parcels {hp:,}; JV {money(jv)}; AV {money(av)}; diff {money(jv-av)}; avg {money((jv-av)/hp if hp else None)}; AV/JV {av/jv:.3f}" if hp else "no NAL")
tax = sum(f(by[(c, 2026)]["est_avg_annual_tax_saved"]) * int(by[(c, 2026)]["homestead_parcels"]) for c in counties if by[(c, 2026)]["homestead_parcels"])
print(f"implied statewide tax on NAL differential at 2025 millage: {money(tax)}")
if dist:
    over = sum(int(d["parcels_differential_over_500k"]) for d in dist.values())
    above = sum(int(d["differential_above_500k_total"]) for d in dist.values())
    zero = sum(float(d["share_with_zero_differential"]) * int(d["homestead_parcels"]) for d in dist.values())
    print(f"homesteads with differential > $500k: {over:,}; differential above cap total {money(above)}; zero-differential homesteads {zero:,.0f}")
    print("\nmean/median ratio by county:")
    rat = sorted(((f(by[(c, 2026)]["avg_soh_differential_per_homestead"]) / f(dist[c]["median_soh_differential"]), c) for c in counties if c in dist and f(dist[c]["median_soh_differential"])), reverse=True)
    print(rat[:8], rat[-5:])
    print("share zero differential top:", sorted(((float(d["share_with_zero_differential"]), c) for c, d in dist.items()), reverse=True)[:8])
    print("p90 top:", sorted(((int(d["p90_soh_differential"]), c) for c, d in dist.items()), reverse=True)[:8])
    print("max:", sorted(((int(d["max_soh_differential"]), c) for c, d in dist.items()), reverse=True)[:5])
    print("median JV/AV top:", sorted(((int(d["median_homestead_just_value"]), c) for c, d in dist.items()), reverse=True)[:5])
    print("AV/JV lowest:", sorted((int(by[(c,2026)]["homestead_assessed_value_total"]) / int(by[(c,2026)]["homestead_just_value_total"]), c) for c in counties if by[(c,2026)]["homestead_parcels"])[:8])
    print("AV/JV highest:", sorted((int(by[(c,2026)]["homestead_assessed_value_total"]) / int(by[(c,2026)]["homestead_just_value_total"]), c) for c in counties if by[(c,2026)]["homestead_parcels"])[-5:])

print("\n## E. Portability\n")
pb = {(r["county"], int(r["year"])): r for r in port}
for y in range(2022, 2027):
    n = sum(int(pb[(c, y)]["portability_transfers"] or 0) for c in counties)
    v = sum(float(pb[(c, y)]["portability_value_total"] or 0) for c in counties)
    print(y, f"transfers {n:,} value {money(v)} avg {money(v/n)}")
pr = sorted(((f(pb[(c, 2026)]["avg_value_ported_per_transfer"]) or 0, c, pb[(c, 2026)]["portability_transfers"]) for c in counties), reverse=True)
print("avg ported 2026 top:", pr[:8], "\nbottom:", pr[-5:])
print("ported avg vs county avg differential (2026):")
for v, c, n in pr[:67]:
    a = f(by[(c, 2026)]["avg_soh_differential_per_homestead"])
    if a and v:
        pass
print("counties where avg ported > avg differential:", sum(1 for v, c, n in pr if f(by[(c, 2026)]["avg_soh_differential_per_homestead"]) and v > f(by[(c, 2026)]["avg_soh_differential_per_homestead"])))
