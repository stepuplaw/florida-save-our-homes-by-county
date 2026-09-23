"""List a folder on the DOR SharePoint data portal via the REST API.
usage: splist.py "/property/dataportal/Documents/PTO Data Portal/..." """
import sys, json, urllib.request, urllib.parse

folder = sys.argv[1]
base = "https://floridarevenue.com/property/dataportal/_api/web/GetFolderByServerRelativeUrl('%s')/%s"
for kind in ("Folders", "Files"):
    url = base % (urllib.parse.quote(folder), kind)
    req = urllib.request.Request(url, headers={"Accept": "application/json;odata=verbose", "User-Agent": "Mozilla/5.0"})
    try:
        d = json.load(urllib.request.urlopen(req, timeout=120))
    except Exception as e:
        print(kind, "FAIL", e)
        continue
    for it in d["d"]["results"]:
        if kind == "Folders":
            print("DIR ", it["ServerRelativeUrl"], it.get("ItemCount"))
        else:
            print("FILE", it["ServerRelativeUrl"], it.get("Length"), it.get("TimeLastModified"))
