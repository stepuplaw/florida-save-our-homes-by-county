"""Append a timestamped line to progress.log: python3 tools/log.py "message"."""
import sys, os, datetime

p = os.path.join(os.path.dirname(__file__), "..", "progress.log")
with open(p, "a") as f:
    f.write(f"{datetime.datetime.now().isoformat(timespec='seconds')} {' '.join(sys.argv[1:])}\n")
