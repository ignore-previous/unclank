"""Apply unclank's pass bars to a `claude plugin eval --json` result.

Run the evals with `--threshold 0 --ablation none --json <file>`, then:

    python scripts/eval_summary.py <file> [<file> ...]

Bars, by grader name:
- tell-*: planted Avoid tells. Mean share found across runs must be at least 80%.
- clean-*: no Avoid hits on a clean fixture. Must pass in at least 2 of 3 runs.
- fired: the skill under test was invoked. Must pass in every run.
- not-fired: no unclank skill fired on an unrelated prompt. Must pass in every run.
- block: the UNCLANK-AUDIT block is present. Must pass in every run.
Any other grader is reported but not barred.
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict

TELL_BAR = 0.8
CLEAN_BAR = 2 / 3


def summarise(path: str) -> bool:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    model = data.get("suite", {}).get("modelOverride") or "default model"
    print(f"== {path} ({model})")
    ok_all = True
    for case in data["cases"]:
        runs = case["arms"]["with"]
        lines: list[str] = []
        ok = True
        errors = [r["error"] for r in runs if r.get("error")]
        if errors:
            ok = False
            lines.append(f"run errors: {errors}")
        tell_shares: list[float] = []
        missed: dict[str, int] = defaultdict(int)
        other: dict[str, list[bool]] = defaultdict(list)
        for r in runs:
            tells = [g for g in r["graders"] if g["name"].startswith("tell-")]
            if tells:
                tell_shares.append(sum(g["passed"] for g in tells) / len(tells))
                for g in tells:
                    if not g["passed"]:
                        missed[g["name"]] += 1
            for g in r["graders"]:
                if not g["name"].startswith("tell-"):
                    other[g["name"]].append(bool(g["passed"]))
        if tell_shares:
            mean = sum(tell_shares) / len(tell_shares)
            good = mean >= TELL_BAR
            ok &= good
            per_run = ", ".join(f"{s:.0%}" for s in tell_shares)
            lines.append(f"{'PASS' if good else 'FAIL'} planted tells found: mean {mean:.0%} (runs: {per_run})")
            if missed:
                lines.append("     missed: " + ", ".join(f"{k} x{v}" for k, v in sorted(missed.items())))
        for name, passes in sorted(other.items()):
            n, k = len(passes), sum(passes)
            if name.startswith("clean-"):
                good = k / n >= CLEAN_BAR
            elif name in ("fired", "not-fired", "block"):
                good = k == n
            else:
                lines.append(f"info {name}: {k}/{n}")
                continue
            ok &= good
            lines.append(f"{'PASS' if good else 'FAIL'} {name}: {k}/{n}")
        ok_all &= ok
        print(f"{'PASS' if ok else 'FAIL'} {case['name']}")
        for line in lines:
            print(f"  {line}")
    return ok_all


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 2
    results = [summarise(p) for p in argv]
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main(argv=sys.argv[1:]))
