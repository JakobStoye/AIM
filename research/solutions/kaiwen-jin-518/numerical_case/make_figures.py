"""Generate vector paper figures and the table from compact publication CSVs."""
from pathlib import Path
import argparse
import csv
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--summary", type=Path, default=ROOT / "numerical_case/summary")
RESULT = parser.parse_args().summary
OUT = ROOT / "paper/figures"
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"font.family": "serif", "font.size": 10,
                    "axes.grid": True, "grid.alpha": .25,
                    "savefig.bbox": "tight", "pdf.fonttype": 42})
colors = {0.1: "#2166ac", 0.5: "#1b7837", 1.0: "#b2182b"}
with (RESULT / "global_summary.csv").open() as f:
    rows = list(csv.DictReader(f))
with (RESULT / "local_summary.csv").open() as f:
    local = list(csv.DictReader(f))

fig, axes = plt.subplots(1, 3, figsize=(11.2, 3.1), constrained_layout=True)
for ax, gamma in zip(axes, (0.1, 0.5, 1.0)):
    for family, marker in [("mixed", "o"), ("power", "s")]:
        r = [x for x in rows if float(x["gamma"]) == gamma and
             x["family"] == family and int(x["N"]) == 8]
        r.sort(key=lambda x: float(x["tau"]))
        x = np.array([float(t["tau"]) for t in r])
        y = np.array([float(t["max_error_l2"]) for t in r])
        ax.loglog(x, y, marker=marker, label=family, color=colors[gamma],
                  linestyle="-" if family == "mixed" else "--", markersize=4)
    ax.set_title(r"$\gamma={:g}$, $N=8$, $K=32$".format(gamma))
    ax.set_xlabel(r"$\tau$")
    ax.set_ylabel(r"$\max_n\|u_{\rm ref}(t_n)-u_K^n\|_2$")
    ax.legend(fontsize=9)
fig.savefig(OUT / "global_convergence.pdf")
plt.close(fig)

fig, axes = plt.subplots(1, 3, figsize=(11.2, 3.1), constrained_layout=True)
styles = {"even": ("o", "-"), "odd": ("s", "--"),
          "half_airy": ("^", "-."), "random": ("x", ":")}
for ax, gamma in zip(axes, (0.1, 0.5, 1.0)):
    for phase, (marker, ls) in styles.items():
        r = [x for x in local if float(x["gamma"]) == gamma and x["phase"] == phase]
        r.sort(key=lambda x: int(x["N"]))
        ax.loglog([int(t["N"]) for t in r],
                  [float(t["normalized_remainder"]) for t in r],
                  marker=marker, linestyle=ls, label=phase.replace("_", " "),
                  markersize=4)
    ax.set_title(r"$\gamma={:g}$, $\tau=N^{{-3}}$".format(gamma))
    ax.set_xlabel(r"Initial bandwidth $N$")
    ax.set_ylabel(r"$\|R_{2,\tau}(f,f,f)\|_2/\tau^{1+\gamma}$")
    ax.set_xticks([4, 8, 16, 32], labels=["4", "8", "16", "32"])
    ax.legend(fontsize=8)
fig.savefig(OUT / "local_remainder.pdf")
plt.close(fig)

case = "mixed_g0.1_N16_L16"
with (RESULT / "defect_accumulation.csv").open() as stream:
    defect_rows = list(csv.DictReader(stream))
# The compact CSV retains measured norms at every selected coarse grid time.
time = [float(row["time"]) for row in defect_rows]
error = [float(row["error_l2"]) for row in defect_rows]
defect = [float(row["transported_defect_l2"]) for row in defect_rows]
feedback = [float(row["transported_feedback_l2"]) for row in defect_rows]
fig, ax = plt.subplots(figsize=(6.1, 3.2), constrained_layout=True)
ax.plot(time, error, "o-", label="observed error", markersize=3)
ax.plot(time, defect, "s--", label="transported defect sum", markersize=3)
ax.plot(time, feedback, "^:", label="transported feedback sum", markersize=3)
ax.set(xlabel="Time", ylabel=r"$L^2$ norm",
       title=r"Mixed data: $\gamma=0.1$, $N=16$, $K=64$, $L=16$")
ax.legend(fontsize=9)
fig.savefig(OUT / "defect_accumulation.pdf")
plt.close(fig)

finest = [x for x in rows if int(x["steps"]) == 512]
table = [r"\begin{tabular}{llrrrr}", r"\toprule",
         r"Family & $\gamma$ & $N$ & $E_{512}$ & $E_{512}/\tau^\gamma$ & $d_{\rm ref}/E_{512}$\\",
         r"\midrule"]
for r in finest:
    table.append("{} & {} & {} & {:.3e} & {:.3e} & {:.3e} \\\\".format(
        r["family"], "{:g}".format(float(r["gamma"])), r["N"],
        float(r["max_error_l2"]), float(r["normalized_max_error"]),
        float(r["reference_quality_fraction"])))
table += [r"\bottomrule", r"\end{tabular}"]
(ROOT / "paper/numerical_table.tex").write_text("\n".join(table) + "\n")
report = {
    "global_rows": len(rows), "local_rows": len(local),
    "max_reference_fraction": max(float(r["reference_quality_fraction"]) for r in rows),
    "max_reconstruction_error": max(float(r["reconstruction_error"]) for r in rows),
    "peak_phase_fraction_range": [min(float(r["peak_phase_fraction"]) for r in rows),
                                  max(float(r["peak_phase_fraction"]) for r in rows)],
    "peak_lowest_mode_fraction_range": [min(float(r["peak_lowest_mode_fraction"]) for r in rows),
                                        max(float(r["peak_lowest_mode_fraction"]) for r in rows)],
    "local_half_airy_envelope_ratio_range":
        [min(float(r["absolute_envelope_ratio"]) for r in local if r["phase"] == "half_airy"),
         max(float(r["absolute_envelope_ratio"]) for r in local if r["phase"] == "half_airy")],
    "selected_defect_case": case,
    "classification": "NUMERICAL EVIDENCE, finite smooth Fourier data",
    "figure_inputs": ["global_summary.csv", "local_summary.csv", "defect_accumulation.csv"],
}
(ROOT / "paper/numerical_summary.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
