"""Block up to N seconds (default 540) or until the NAL run log shows the pool finished; print status."""
import os, sys, time
log = os.path.join(os.path.dirname(__file__), "..", "run.log")
summ = os.path.join(os.path.dirname(__file__), "..", "data", "sources", "nal_2026", "nal_2026_homestead_summary.csv")
end = time.time() + int(sys.argv[1] if len(sys.argv) > 1 else 540)
start = sum(1 for _ in open(summ)) - 1
while time.time() < end:
    lines = open(log).read().splitlines()
    done = sum(1 for l in lines if l.startswith(("done", "FAIL")))
    if done >= 67:
        break
    time.sleep(20)
lines = open(log).read().splitlines()
print("summarized:", sum(1 for _ in open(summ)) - 1, "(was", start, ") finished lines:",
      sum(1 for l in lines if l.startswith(("done", "FAIL"))), "fails:", [l for l in lines if l.startswith("FAIL")])
raw = os.path.join(os.path.dirname(summ), "raw")
print("in progress:", [(f, os.path.getsize(os.path.join(raw, f)) // 1_000_000) for f in os.listdir(raw) if f.endswith(".part")])
