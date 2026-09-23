#!/usr/bin/env python3
"""Validate the published tables and regenerate the data dictionary
(data/schema.json), the Frictionless descriptor (data/datapackage.json) and the
resource list in kaggle/dataset-metadata.json.

    python3 tools/package.py          # validate and rebuild the descriptors
    python3 tools/package.py --check  # validate only

tools/build.py builds the tables themselves; this only describes and checks them.
"""
import csv, json, os, sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
VERSION = "2026.09.23"
TITLE = "Florida Save Our Homes Benefit by County (2026)"
PAGE = "https://stepuplaw.com/data/florida-save-our-homes-by-county/"
STATEWIDE_2026 = 815135591712  # DOR 2026 preliminary DR-489V, line 12
DASHES = (chr(0x2012), chr(0x2013), chr(0x2014), chr(0x2015))

TABLES = {
    "counties": ("counties.csv", "67 counties x roll years 2022 to 2026 (335 rows)", ["county", "year"], [
        ("county", "string", "County name as DOR spells it (Miami-Dade, Saint Johns, Saint Lucie, DeSoto)"),
        ("year", "integer", "Tax roll year (assessment date January 1 of that year). 2026 is the preliminary roll"),
        ("homestead_parcels", "integer", "Parcels with NAL field JV_HMSTD (Just Value, Homestead Property) greater than 0. 2026 only"),
        ("homestead_just_value_total", "integer", "Sum of JV_HMSTD over those parcels, in dollars. 2026 only"),
        ("homestead_assessed_value_total", "integer", "Sum of AV_HMSTD (Assessed Value, Homestead Property) before exemptions, in dollars. 2026 only"),
        ("soh_differential_total", "integer", "County Save Our Homes differential (homestead just value minus capped assessed value) as DOR reports it in the Data Book, county_overview.xlsx, sheet Save Our Homes Value History"),
        ("avg_soh_differential_per_homestead", "integer", "(homestead_just_value_total minus homestead_assessed_value_total) divided by homestead_parcels, all from the NAL. 2026 only"),
        ("avg_total_millage", "number", "DOR Total Millage Rate for the county (county-wide plus less-than-county-wide levies averaged over the county), from millage_taxes_levied.xlsx. 2022 to 2025"),
        ("est_avg_annual_tax_saved", "integer", "ESTIMATE. avg_soh_differential_per_homestead x the county's 2025 Total Millage Rate / 1000, in dollars a year. 2026 only"),
        ("source", "string", "Table, sheet and column for every figure in the row"),
        ("source_url", "string", "DOR file URLs, separated by ' | '"),
        ("note", "string", "Roll status, what is blank and why, and the NAL versus Data Book gap for 2026"),
    ]),
    "distribution_2026": ("distribution_2026.csv", "2026 parcel-level distribution of the differential per county, from the DOR NAL roll", ["county"], [
        ("county", "string", "County name as DOR spells it"),
        ("nal_file", "string", "The DOR NAL roll file read"),
        ("roll", "string", "Preliminary or Final (Final for Citrus only)"),
        ("homestead_parcels", "integer", "Parcels with JV_HMSTD greater than 0"),
        ("median_soh_differential", "number", "Median of JV_HMSTD minus AV_HMSTD over homestead parcels"),
        ("p25_soh_differential", "number", "25th percentile of the differential"),
        ("p75_soh_differential", "number", "75th percentile of the differential"),
        ("p90_soh_differential", "number", "90th percentile of the differential"),
        ("p99_soh_differential", "number", "99th percentile of the differential"),
        ("max_soh_differential", "number", "Largest single-parcel differential, as recorded on the roll"),
        ("share_with_zero_differential", "number", "Share of homestead parcels whose differential is zero or less"),
        ("parcels_differential_over_500k", "integer", "Homestead parcels whose differential exceeds the $500,000 portability limit"),
        ("share_over_500k", "number", "parcels_differential_over_500k divided by homestead_parcels"),
        ("differential_above_500k_total", "integer", "Sum over those parcels of the differential above $500,000, the part portability cannot carry"),
        ("median_homestead_just_value", "number", "Median JV_HMSTD"),
        ("median_homestead_assessed_value", "number", "Median AV_HMSTD"),
    ]),
    "portability_by_county": ("portability_by_county.csv", "DOR-reported portability transfers and value ported, by county, 2022 to 2026", ["county", "year"], [
        ("county", "string", "County name as DOR spells it"),
        ("year", "integer", "Tax roll year"),
        ("portability_transfers", "integer", "Number of portability transfers DOR reports"),
        ("portability_value_total", "integer", "Total differential ported, in dollars"),
        ("avg_value_ported_per_transfer", "integer", "portability_value_total divided by portability_transfers (computed)"),
        ("source", "string", "Table and sheets"),
        ("source_url", "string", "DOR file URL"),
        ("note", "string", "Method notes"),
    ]),
}


def read(fn):
    return list(csv.DictReader(open(os.path.join(ROOT, "data", fn), newline="")))


def validate():
    errors = []
    for name, (fn, _, _, fields) in TABLES.items():
        rows = read(fn)
        cols = [f[0] for f in fields]
        if rows and list(rows[0].keys()) != cols:
            errors.append(f"{fn}: columns {list(rows[0].keys())} do not match the schema")
        blob = open(os.path.join(ROOT, "data", fn), encoding="utf-8").read()
        if any(d in blob for d in DASHES):
            errors.append(f"{fn}: contains an em or en dash")
    c = read("counties.csv")
    if len(c) != 335:
        errors.append(f"counties.csv: expected 335 rows, found {len(c)}")
    y26 = [r for r in c if r["year"] == "2026"]
    total = sum(int(r["soh_differential_total"]) for r in y26)
    if total != STATEWIDE_2026:
        errors.append(f"2026 county SOH sum {total} != DR-489V line 12 {STATEWIDE_2026}")
    if any(not r["homestead_parcels"] for r in y26):
        errors.append("a 2026 row lacks a NAL homestead count")
    if len(read("distribution_2026.csv")) != 67:
        errors.append("distribution_2026.csv: expected 67 rows")
    return errors


def schema(fields, pk):
    return {"fields": [{"name": n, "type": t, "description": d} for n, t, d in fields], "primaryKey": pk}


def main():
    errors = validate()
    print(f"{len(errors)} errors")
    for e in errors:
        print("  " + e)
    if errors:
        sys.exit(1)
    if "--check" in sys.argv:
        return
    d = os.path.join(ROOT, "data")
    sch = {name: schema(f, pk) for name, (_, _, pk, f) in TABLES.items()}
    with open(os.path.join(d, "schema.json"), "w") as f:
        json.dump(sch, f, indent=2)
        f.write("\n")
    pkg = {
        "name": "florida-save-our-homes-by-county-2026",
        "title": TITLE,
        "version": VERSION,
        "licenses": [{"name": "CC-BY-4.0", "path": "https://creativecommons.org/licenses/by/4.0/"}],
        "homepage": PAGE,
        "contributors": [{"title": "Kevin D. Klagge", "role": "author", "organization": "Klagge Law, PLLC (StepUpLaw)"}],
        "sources": [{"title": "Florida Department of Revenue, Property Tax Oversight, Data Book and NAL roll files",
                     "path": "https://floridarevenue.com/property/Pages/DataPortal.aspx"}],
        "resources": [{"name": name, "path": fn, "description": desc, "format": "csv", "mediatype": "text/csv",
                       "schema": sch[name]} for name, (fn, desc, _, _) in TABLES.items()],
    }
    with open(os.path.join(d, "datapackage.json"), "w") as f:
        json.dump(pkg, f, indent=2)
        f.write("\n")
    kpath = os.path.join(ROOT, "kaggle", "dataset-metadata.json")
    k = json.load(open(kpath))
    k["resources"] = [
        {"path": fn, "description": desc,
         "schema": {"fields": [{"name": n, "description": dd, "type": t} for n, t, dd in fields]}}
        for fn, desc, _, fields in TABLES.values()
    ] + [{"path": "counties.json", "description": "The same 335 rows as counties.csv, as a JSON array"},
         {"path": "schema.json", "description": "Data dictionary for the three CSV files"}]
    with open(kpath, "w") as f:
        json.dump(k, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("wrote schema.json, datapackage.json and the Kaggle resource list")


if __name__ == "__main__":
    main()
