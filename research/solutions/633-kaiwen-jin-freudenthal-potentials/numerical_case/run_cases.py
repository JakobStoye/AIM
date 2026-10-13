"""Reproduce all finite construction cases reported in the paper."""

import argparse
import hashlib
import importlib.metadata
import json
import os
import platform
import subprocess
import sys
import time
from pathlib import Path

import numpy as np

from freudenthal import construct_basis
from freudenthal.provenance import implementation_manifest

ROOT = Path(__file__).resolve().parents[1]
CASES = [(1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (7, 6), (2, 7), (4, 7), (3, 13), (2, 20)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "numerical_case/results/paper_cases")
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError("Use a fresh output directory to preserve previous run results")
    args.output.mkdir(parents=True)
    implementation = implementation_manifest()
    cases = []
    histograms = {}
    for N, degree in CASES:
        start = time.perf_counter()
        basis = construct_basis(N, degree)
        case = args.output / f"N{N}_d{degree}"
        basis.save(case)
        summary = {**basis.summary(), "seconds": time.perf_counter() - start}
        summary["basis_sha256"] = hashlib.sha256((case / "basis.npz").read_bytes()).hexdigest()
        (case / "run.json").write_text(json.dumps(summary, indent=2) + "\n")
        cases.append(summary)
        lengths = np.diff(basis.coefficients.indptr)
        histograms[case.name] = {
            "dimension": len(basis),
            "counts": np.bincount(lengths).tolist(),
            "basis_sha256": summary["basis_sha256"],
        }
        print(json.dumps(summary), flush=True)
    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True, stderr=subprocess.DEVNULL
        ).strip()
    except subprocess.CalledProcessError:
        commit = "uncommitted initial implementation"
    manifest = {
        "cases": cases,
        "argv": sys.argv,
        "commit": commit,
        "python": sys.version,
        "platform": platform.platform(),
        "parameters": CASES,
        "arithmetic": "integer coefficients, bounded int64 products, exact modular independence",
        "thread_limits": {
            name: os.environ.get(name)
            for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS")
        },
        "randomness": "none",
        "implementation": implementation,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "versions": {p: importlib.metadata.version(p) for p in ("numpy", "scipy")},
    }
    (args.output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    summaries = ROOT / "numerical_case/summaries"
    summaries.mkdir(parents=True, exist_ok=True)
    (summaries / "paper_cases.json").write_text(
        json.dumps({"cases": cases, "versions": manifest["versions"]}, indent=2) + "\n"
    )
    (summaries / "sparsity_histograms.json").write_text(json.dumps(histograms, indent=2) + "\n")
    (summaries / "implementation.json").write_text(json.dumps(implementation, indent=2) + "\n")


if __name__ == "__main__":
    main()
