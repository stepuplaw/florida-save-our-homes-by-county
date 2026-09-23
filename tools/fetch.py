"""Download a list of URLs into data/sources/, keeping a manifest of url, file, size, time."""
import sys, os, json, urllib.request, datetime, hashlib

BASE = os.path.join(os.path.dirname(__file__), "..", "data", "sources")
MANIFEST = os.path.join(BASE, "manifest.json")


def fetch(url, name=None, subdir=""):
    d = os.path.join(BASE, subdir)
    os.makedirs(d, exist_ok=True)
    name = name or urllib.parse.unquote(url.rstrip("/").split("/")[-1])
    path = os.path.join(d, name)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (research dataset build)"})
    with urllib.request.urlopen(req, timeout=300) as r:
        data = r.read()
    with open(path, "wb") as f:
        f.write(data)
    m = json.load(open(MANIFEST)) if os.path.exists(MANIFEST) else {}
    m[os.path.join(subdir, name)] = {
        "url": url,
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "retrieved": datetime.datetime.now().isoformat(timespec="seconds"),
    }
    json.dump(m, open(MANIFEST, "w"), indent=1, sort_keys=True)
    print(f"{len(data):>10}  {os.path.join(subdir, name)}")
    return path


if __name__ == "__main__":
    import urllib.parse
    args = sys.argv[1:]
    sub = ""
    if args and args[0].startswith("--dir="):
        sub = args.pop(0)[6:]
    for u in args:
        try:
            fetch(u, subdir=sub)
        except Exception as e:
            print("FAIL", u, e)
