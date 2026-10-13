#!/usr/bin/env python3
"""Generate PDF figures from the recorded case manifest."""

import argparse
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results",type=Path,default=ROOT/"numerical_case/results/paper-v1")
    args=parser.parse_args()
    manifest=json.loads((args.results/"manifest.json").read_text())
    if manifest["status"] != "PASS":
        raise RuntimeError("results have not passed validation")
    destination=ROOT/"numerical_case/figures"
    destination.mkdir(exist_ok=True)
    plt.rcParams.update({"font.size":10,"pdf.fonttype":42})
    figure,axes=plt.subplots(1,2,figsize=(9.8,3.9))
    names=["isotropic","polar anisotropy","alternating layers","random layers"]
    for axis,d in zip(axes,(2,3)):
        for case,label in enumerate(names):
            data=np.load(args.results/f"d{d}_case{case:02d}.npz")
            logs=data["expanded_logs"]
            n=np.arange(1,len(logs)+1)
            axis.plot(n**(1/(d-1)),logs,label=label,linewidth=1.4)
        axis.set(title=f"d = {d}",xlabel="mode index" if d==2 else "square root of mode index",ylabel="log singular value")
        axis.grid(alpha=0.25)
    handles, labels = axes[0].get_legend_handles_labels()
    figure.legend(handles, labels, loc="lower center", ncol=4, fontsize=10,
                  bbox_to_anchor=(0.5, -0.02), frameon=False)
    figure.tight_layout(rect=(0, 0.07, 1, 1))
    figure.savefig(destination/"radial_spectra.pdf",bbox_inches="tight")
    plt.close(figure)
    figure,axes=plt.subplots(1,2,figsize=(9.8,3.9))
    for axis,d in zip(axes,(2,3)):
        for case,label in ((0,"isotropic"),(1,"polar anisotropy"),(2,"alternating layers"),(3,"random layers")):
            data=np.load(args.results/f"d{d}_case{case:02d}.npz")
            n=np.arange(1,len(data["expanded_logs"])+1)
            # The theorem requires the plotted normalized quantity to be >= 1.
            ratio=2*np.cumsum(data["expanded_logs"])/data["product_bound"]
            axis.plot(n**(1/(d-1)),ratio,label=label,linewidth=1.3)
        axis.axhline(1,color="black",linestyle="--",linewidth=1)
        axis.set(title=f"d = {d}",xlabel="mode index" if d==2 else "square root of mode index",ylabel="log determinant / upper bound",yscale="log")
        axis.grid(alpha=0.25)
    handles, labels = axes[0].get_legend_handles_labels()
    figure.legend(handles, labels, loc="lower center", ncol=4, fontsize=10,
                  bbox_to_anchor=(0.5, -0.02), frameon=False)
    figure.tight_layout(rect=(0, 0.07, 1, 1))
    figure.savefig(destination/"determinant_comparison.pdf",bbox_inches="tight")
    plt.close(figure)
    print("Generated radial_spectra.pdf and determinant_comparison.pdf")


if __name__ == "__main__":
    main()
