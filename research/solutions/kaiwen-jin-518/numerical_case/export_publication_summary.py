"""Export compact, measured figure inputs from the local numerical campaign.

Full Fourier arrays and per-step CSV files stay in the gitignored results
directory. This export contains only the 48 global/local scalar summaries,
17 selected figure samples, runtime metadata and validation reports.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
SELECTED_CASE = "mixed_g0.1_N16_L16"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def export(results: Path, output: Path) -> dict:
    output.mkdir(parents=True, exist_ok=True)
    copies = {
        "global_summary.csv": "global_summary.csv",
        "local_summary.csv": "local_summary.csv",
        "manifest.json": "run_manifest.json",
        "validation.json": "validation.json",
        "rough_ode_validation.json": "rough_ode_validation.json",
        "frequency_checks.json": "frequency_checks.json",
    }
    source_hashes = {}
    for source, target in copies.items():
        path = results / source
        shutil.copyfile(path, output / target)
        source_hashes[source] = sha256(path)

    checkpoint = results / "checkpoints" / f"{SELECTED_CASE}.npz"
    with np.load(checkpoint, allow_pickle=False) as data:
        time = data["time"]
        norms = [np.linalg.norm(data[key], axis=1) for key in
                 ("error", "transported_defect_sum", "transported_feedback_sum")]
    with (output / "defect_accumulation.csv").open("w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["time", "error_l2", "transported_defect_l2", "transported_feedback_l2"])
        writer.writerows(zip(time, *norms))
    source_hashes[f"checkpoints/{SELECTED_CASE}.npz"] = sha256(checkpoint)
    exported = list(copies.values()) + ["defect_accumulation.csv"]
    receipt = {
        "classification": "NUMERICAL EVIDENCE; compact publication inputs",
        "local_raw_directory": "numerical_case/results",
        "raw_directory_version_controlled": False,
        "selected_defect_case": SELECTED_CASE,
        "selected_defect_samples": len(time),
        "source_archive_sha256": source_hashes,
        "exported_files": {name: sha256(output / name) for name in exported},
        "scope": "Measured scalar summaries and plot inputs; no Fourier trajectories or checkpoints",
    }
    (output / "export_receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    return receipt


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results", type=Path, default=HERE / "results")
    parser.add_argument("--output", type=Path, default=HERE / "summary")
    args = parser.parse_args()
    print(json.dumps(export(args.results, args.output), indent=2))


if __name__ == "__main__":
    main()
