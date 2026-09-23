"""Assemble FINDINGS.md from tools/REPORT_template.md and generated tables (no figures retyped)."""
import csv, os, re, subprocess, sys
S = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(S, "..")
tables = open(os.path.join(ROOT, "data", "report_tables.md")).read()


def section_table(letter):
    sec = tables.split(f"## {letter}.")[1].split("\n## ")[0]
    return "\n".join(l for l in sec.splitlines() if l.startswith("|"))


rows = {(r["county"], r["year"]): r for r in csv.DictReader(open(os.path.join(ROOT, "data", "counties.csv")))}
dist = {r["county"]: r for r in csv.DictReader(open(os.path.join(ROOT, "data", "distribution_2026.csv")))}
mv = []
for (c, y), r in rows.items():
    if y == "2026" and r["est_avg_annual_tax_saved"]:
        m = float(rows[(c, "2025")]["avg_total_millage"])
        mv.append((float(r["est_avg_annual_tax_saved"]), c, float(dist[c]["median_soh_differential"]) * m / 1000))
move = "\n".join(f"| {c} | ${a:,.0f} | ${b:,.0f} |" for a, c, b in sorted(mv, reverse=True)[:10])
cap = subprocess.run([sys.executable, os.path.join(S, "above_cap.py")], capture_output=True, text=True).stdout
cap = "\n".join(l for l in cap.splitlines() if l.startswith("|"))

t = open(os.path.join(S, "REPORT_template.md")).read()
t = t.replace("{{TABLE_A}}", section_table("A")).replace("{{TABLE_B}}", section_table("B"))
t = t.replace("{{TABLE_MOVE}}", move).replace("{{TABLE_CAP}}", cap)
assert "{{" not in t
assert not re.search("[\u2013\u2014]", t), "en/em dash found"
open(os.path.join(ROOT, "FINDINGS.md"), "w").write(t)
print("FINDINGS.md written", len(t), "chars")
