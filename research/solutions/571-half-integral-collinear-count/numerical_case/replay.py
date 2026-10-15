"""Recompute a selected cell or the entire finite calculation with ordinary BigInt."""
import argparse
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from exact_algebra import rational_equal


def main():
    if not __debug__:
        raise RuntimeError("Replay checks require ordinary Python; do not use -O.")
    parser = argparse.ArgumentParser(description=__doc__)
    choice = parser.add_mutually_exclusive_group(required=True)
    choice.add_argument("--all", action="store_true", help="Recompute all 608 distinct systems.")
    choice.add_argument("--cell", type=int, help="Recompute one cell in the chosen action.")
    parser.add_argument("--action", choices=["identity", "H", "V", "HV"], default="identity")
    parser.add_argument("--output", type=Path, default=ROOT / "numerical_case/raw/replay.json")
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError("Choose a fresh output path; existing data are never overwritten.")
    import PyNormaliz as nmz
    nmz.NmzSetNumberOfNormalizThreads(1)
    document = json.loads((ROOT / "numerical_case/exact_series.json").read_text())
    groups = document["groups"]
    if not args.all:
        groups = [g for g in groups if {"action": args.action, "index": args.cell} in g["members"]]
        if len(groups) != 1:
            raise ValueError("The selected cell does not exist.")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    results = []
    for group in groups:
        started = time.monotonic()
        payload = group["input"]
        cone = nmz.Cone(**{k: v for k, v in payload.items() if v})
        assert cone.Compute("HilbertSeries", "BigInt", "NoGradingDenom")
        series, grade = cone.HilbertSeries(), cone.Grading()
        assert grade == group["grading_readback"]
        assert rational_equal(series, group["series"])
        results.append({"input_sha256": group["input_sha256"], "members": group["members"],
                        "series": series, "grading_readback": grade,
                        "seconds": time.monotonic() - started})
        report = {"status": "COMPLETE" if len(results) == len(groups) else "IN_PROGRESS",
                  "at": datetime.now(timezone.utc).isoformat(), "groups_requested": len(groups),
                  "groups_completed": len(results), "compute_options":
                  ["HilbertSeries", "BigInt", "NoGradingDenom"], "normaliz_threads": 1,
                  "data_sha256": hashlib.sha256(
                      (ROOT / "numerical_case/exact_series.json").read_bytes()).hexdigest(),
                  "results": results}
        temporary = args.output.with_name(args.output.name + ".tmp")
        temporary.write_text(json.dumps(report, indent=2) + "\n")
        temporary.replace(args.output)
        print(json.dumps({"completed": len(results), "requested": len(groups),
                          "members": group["members"], "exact_rational_agreement": True}), flush=True)


if __name__ == "__main__":
    main()
