"""For each databook folder, show roll year/status labels of key tables."""
import sys, os, glob
sys.path.insert(0, os.path.dirname(__file__))
from xlsx import sheets

root = os.path.join(os.path.dirname(__file__), "..", "data", "sources")
for d in sorted(glob.glob(os.path.join(root, "databook_*"))):
    m = sheets(os.path.join(d, "millage_taxes_levied.xlsx"))["Millage Rates"]
    co = sheets(os.path.join(d, "county_overview.xlsx"))
    sv = co["Statewide Property Value"]
    soh = co["Save Our Homes Value History"]
    print(os.path.basename(d), "| millage year:", m[1][:1], "| overview year:", sv[1][:1],
          "status:", sv[4][1], "| SOH hdr last:", soh[3][-3:], "| SOH Alachua last:", soh[4][-3:])
