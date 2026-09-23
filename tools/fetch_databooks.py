"""Download archived DOR Data Book workbooks for the given years into data/sources/databook_<year>/."""
import sys, urllib.parse
sys.path.insert(0, __import__("os").path.dirname(__file__))
from fetch import fetch

FILES = ["county_overview.xlsx", "millage_taxes_levied.xlsx", "exemption_values.xlsx",
         "statewide_recap.xlsx", "parcel_count.xlsx", "amendment_1_impact.xlsx", "jat.pdf",
         "assessed_value.xlsx", "just_value.xlsx"]
for y in sys.argv[1:]:
    for f in FILES:
        url = ("https://floridarevenue.com/property/dataportal/Documents/PTO%20Data%20Portal/"
               "Databook%20Historical%20Data/" + urllib.parse.quote(f"{y}DataBookFiles/{f}"))
        try:
            fetch(url, subdir=f"databook_{y}")
        except Exception as e:
            print("FAIL", y, f, e)
