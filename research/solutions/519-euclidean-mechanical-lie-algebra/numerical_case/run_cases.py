#!/usr/bin/env python3
"""Run a paper case in a fresh directory, preserving source and output hashes."""

from __future__ import annotations

import argparse
import datetime as dt
import gzip
import hashlib
import json
import platform
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from aim519.audit import run_audit
from aim519.certificates import verify_block
from aim519.polynomial import iterated_lowering, polynomial_calibration


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case", choices=("audit", "crosscheck", "replay"))
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--max-order", type=int, default=18)
    parser.add_argument("--prime", type=int, default=1000003)
    parser.add_argument("--certificate", type=Path)
    args = parser.parse_args()
    if args.case == "replay" and args.certificate is None:
        parser.error("--certificate is required for replay")
    args.output.mkdir(parents=True, exist_ok=False)
    started = dt.datetime.now(dt.timezone.utc).isoformat()
    sources = list((ROOT / "src").rglob("*.py")) + [Path(__file__)]
    manifest = {
        "case": args.case,
        "started_utc": started,
        "status": "RUNNING",
        "python": sys.version,
        "platform": platform.platform(),
        "parameters": {"max_order": args.max_order, "prime": args.prime},
        "command": sys.argv,
        "arithmetic": "unbounded Python integers and fractions.Fraction",
        "workers": 1,
        "placement": "LOCAL_EXECUTION",
        "source_sha256": {
            str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(sources)
        },
    }
    if args.certificate:
        manifest["input_sha256"] = hashlib.sha256(args.certificate.read_bytes()).hexdigest()
    commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True)
    manifest["git_commit_at_start"] = commit.stdout.strip() if commit.returncode == 0 else None
    path = args.output / "manifest.json"
    path.write_text(json.dumps(manifest, indent=2) + "\n")
    clock = time.monotonic()
    try:
        if args.case == "audit":
            summary = run_audit(args.max_order, args.output / "data", args.prime)
        elif args.case == "crosscheck":
            calibrations = []
            for seed in (519, 2026):
                details = {}
                calibration = polynomial_calibration(8, 2, seed, details=details)
                details.update(calibration)
                (args.output / f"polynomial_seed_{seed}.json").write_text(
                    json.dumps(details, indent=2) + "\n"
                )
                calibrations.append(calibration)
            traces = iterated_lowering(5)
            (args.output / "lowering_traces.json").write_text(json.dumps(traces, indent=2) + "\n")
            summary = {
                "polynomial_calibrations": calibrations,
                "lowering_max_order": 5,
                "iterated_lowering_cases": len(traces),
                "iterated_lowering_steps": sum(len(t["steps"]) for t in traces),
                "max_initial_degree": max(t["initial_degree"] for t in traces),
                "max_final_potential_terms": max(
                    t["nonzero_final_potential_terms"] for t in traces
                ),
                "all_passed": True,
                "exact_arithmetic": True,
            }
        else:
            with gzip.open(args.certificate, "rt") as file:
                blocks = json.load(file)
            verified = []
            for block in blocks:
                if block["order"] <= args.max_order:
                    rank = verify_block(block)
                    row = {"order": block["order"], "degree": block["degree"], "rank": rank}
                    verified.append(row)
                    print(json.dumps(row), flush=True)
            if not verified:
                raise ValueError("No certificate blocks selected")
            (args.output / "verified_blocks.json").write_text(json.dumps(verified, indent=2) + "\n")
            summary = {
                "verified_columns": sum(r["rank"] for r in verified),
                "verified_blocks": len(verified),
                "all_passed": True,
            }
        summary["elapsed_seconds"] = round(time.monotonic() - clock, 3)
        (args.output / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
        manifest["status"] = "PASSED"
    except BaseException as error:
        status = "INTERRUPTED" if isinstance(error, KeyboardInterrupt) else "FAILED"
        manifest.update(status=status, error=f"{type(error).__name__}: {error}")
        raise
    finally:
        manifest["finished_utc"] = dt.datetime.now(dt.timezone.utc).isoformat()
        manifest["output_sha256"] = {
            str(p.relative_to(args.output)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(args.output.rglob("*"))
            if p.is_file() and p != path
        }
        path.write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps(summary, indent=2), flush=True)


if __name__ == "__main__":
    main()
