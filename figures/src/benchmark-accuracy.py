"""Accuracy of each harness by task group, all 300 tasks of the v4.7 benchmark, with Wilson 95% intervals.

Reads figures/src/data/benchmark-v47.csv (correct trials per group; evidence E45) and writes
figures/src/data/benchmark-v47-ci.dat for figures/src/benchmark-accuracy.tex. Standard library only.
  python figures/src/benchmark-accuracy.py
"""
import csv
import math
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ARMS = ("opentrading", "opencode", "dsh")


def wilson(k, n, z=1.959964):
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return 100 * p, 100 * (p - max(0.0, c - h)), 100 * (min(1.0, c + h) - p)


rows = list(csv.DictReader(open(HERE / "data" / "benchmark-v47.csv", encoding="utf-8")))
out = ["group " + " ".join(f"{a} {a}_lo {a}_hi" for a in ARMS)]
for r in rows:
    n = int(r["tasks"])
    vals = []
    for a in ARMS:
        vals += [f"{abs(v):.2f}" for v in wilson(int(r[a]), n)]
    out.append(r["group"] + " " + " ".join(vals))
(HERE / "data" / "benchmark-v47-ci.dat").write_text("\n".join(out) + "\n", encoding="utf-8")
