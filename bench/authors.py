#!/usr/bin/env python3
"""authors.py <patched_verdicts.json> [id ...]: the GVS5H authors' own verdicts
(runs/patched_verdicts.json in their repo) for the given problem ids — the 27B
harness and the 27B single call, five passes each — so a run here is compared
with the same ids there. No ids: the five-pass averages over their hundred."""
import json, sys

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    v = json.load(open(sys.argv[1]))["q38-fn-5pass"]
    ids = sys.argv[2:]
    for run, res in v.items():
        vd = res["verdicts"]
        if ids:
            marks = "".join("✓" if vd.get(i) else "✗" for i in ids)
            print(f"{run:24} {sum(vd.get(i, False) for i in ids)}/{len(ids)}  {marks}")
        else:
            print(f"{run:24} raw {res['old_pass@1']:.0f}  patched {res['new_pass@1']:.0f}  (n={len(vd)})")

if __name__ == "__main__":
    main()
