#!/usr/bin/env python3
"""Generate save-our-homes-overview.ipynb.

The notebook is generated rather than hand-edited, so the prose and the code
live in one reviewable file. Rebuild and run it with

    python3 notebooks/build_overview_notebook.py
    python3 -m nbconvert --execute --inplace notebooks/save-our-homes-overview.ipynb
"""
import pathlib
import nbformat as nbf

HERE = pathlib.Path(__file__).resolve().parent
md, code = nbf.v4.new_markdown_cell, nbf.v4.new_code_cell

cells = [
    md("# Florida Save Our Homes benefit by county\n\n"
       "This notebook loads `data/counties.csv` and `data/distribution_2026.csv` and reproduces the headline "
       "figures in the README. Each row of `counties.csv` is one county in one roll year."),
    code("import pandas as pd\n\n"
         "df = pd.read_csv('../data/counties.csv')\n"
         "dist = pd.read_csv('../data/distribution_2026.csv')\n"
         "df.shape"),
    md("## The statewide differential by year\n\n"
       "The 2026 county figures sum exactly to line 12 of DOR's 2026 preliminary DR-489V recapitulation, $815,135,591,712."),
    code("by_year = df.groupby('year')['soh_differential_total'].sum()\n"
         "assert by_year[2026] == 815_135_591_712\n"
         "(by_year / 1e9).round(1)"),
    md("## Estimated tax the cap saves the average homestead, 2026\n\n"
       "An estimate: the average differential times the county's 2025 Total Millage Rate, divided by 1,000. "
       "The average is recomputed from the NAL totals rather than the rounded column, which is how the dataset computes it."),
    code("m25 = df[df.year == 2025].set_index('county')['avg_total_millage']\n"
         "y26 = df[df.year == 2026].set_index('county')\n"
         "avg = (y26['homestead_just_value_total'] - y26['homestead_assessed_value_total']) / y26['homestead_parcels']\n"
         "check = (avg * m25 / 1000).round()\n"
         "assert (check == y26['est_avg_annual_tax_saved']).all()\n"
         "y26[['homestead_parcels', 'avg_soh_differential_per_homestead', 'est_avg_annual_tax_saved']]"
         ".sort_values('est_avg_annual_tax_saved', ascending=False).head(10)"),
    md("## Homesteads above the $500,000 portability limit\n\n"
       "Portability carries at most $500,000 of differential to a new Florida homestead. The part above it is lost on a move."),
    code("d = dist.set_index('county')\n"
         "above = d['differential_above_500k_total'] * m25 / 1000\n"
         "print(f\"{d['parcels_differential_over_500k'].sum():,} homesteads, \"\n"
         "      f\"${d['differential_above_500k_total'].sum() / 1e9:.1f} billion above the limit, \"\n"
         "      f\"about ${above.sum() / 1e9:.2f} billion a year in tax at 2025 rates\")"),
]

nb = nbf.v4.new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nbf.write(nb, HERE / "save-our-homes-overview.ipynb")
print("wrote", HERE / "save-our-homes-overview.ipynb")
