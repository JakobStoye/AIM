"""Create vector sparsity figures from the complete saved row-length histograms."""

import argparse
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
BEGIN = "% BEGIN GENERATED SPARSITY"
END = "% END GENERATED SPARSITY"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--update-paper", action="store_true")
    args = parser.parse_args()
    hist = json.loads((ROOT / "numerical_case/summaries/sparsity_histograms.json").read_text())
    output = ROOT / "paper/figures"
    output.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({"font.size": 10, "pdf.fonttype": 42, "svg.fonttype": "none"})
    fig, ax = plt.subplots(figsize=(5.8, 3.4))
    pgf = [
        r"\begin{tikzpicture}",
        r"\begin{axis}[width=.85\textwidth,height=5.6cm,xmin=0,xmax=70,ymin=0,ymax=1.02,",
        r"xlabel={Nonzero scalar coefficient entries per basis row $s$},",
        r"ylabel={Fraction of rows with at most $s$ entries},",
        r"ytick={0,.25,.5,.75,1},grid=major,",
        r"legend style={at={(.5,-.28)},anchor=north,legend columns=2,draw=none},",
        r"tick label style={font=\small},label style={font=\small}]",
    ]
    metrics = {}
    for degree, color, pgf_color in [
        (6, "#255f95", "blue!70!black"),
        (7, "#bb592d", "orange!80!black"),
    ]:
        record = hist[f"N4_d{degree}"]
        counts = np.asarray(record["counts"], dtype=np.int64)
        if counts.sum() != record["dimension"] or counts[0] != 0:
            raise ValueError("Invalid complete sparsity histogram")
        budget = np.arange(len(counts))
        fraction = np.cumsum(counts) / record["dimension"]
        ax.step(budget, fraction, where="post", color=color, label=f"N=4, d={degree}", lw=1.7)
        coordinates = " ".join(f"({s},{y:.12f})" for s, y in zip(budget, fraction))
        pgf += [
            rf"\addplot+[const plot,no marks,thick,color={pgf_color}] coordinates {{{coordinates}}};",
            rf"\addlegendentry{{$N=4$, $d={degree}$}}",
        ]
        metrics[str(degree)] = {
            "mean_nnz": float(np.dot(counts, budget) / record["dimension"]),
            "max_nnz": int(budget[-1]),
            "dimension": record["dimension"],
            "basis_sha256": record["basis_sha256"],
        }
    ax.set(
        xlim=(0, 70),
        ylim=(0, 1.02),
        xlabel="Nonzero scalar coefficient entries per basis row, s",
        ylabel="Fraction of rows with at most s entries",
    )
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
    ax.grid(alpha=0.2)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.22), ncols=2, frameon=False)
    fig.subplots_adjust(left=0.14, bottom=0.32, right=0.98, top=0.97)
    fig.savefig(
        output / "sparsity.pdf", metadata={"Title": "Sparsity of local Freudenthal potential bases"}
    )
    fig.savefig(output / "sparsity.svg")
    plt.close(fig)
    pgf += [r"\end{axis}", r"\end{tikzpicture}"]
    text = "\n".join(pgf)
    (output / "sparsity.pgf").write_text(text + "\n")
    (ROOT / "numerical_case/summaries/figure_metrics.json").write_text(
        json.dumps(metrics, indent=2) + "\n"
    )
    if args.update_paper:
        paper = ROOT / "paper/main.tex"
        content = paper.read_text()
        head, rest = content.split(BEGIN, 1)
        _, tail = rest.split(END, 1)
        paper.write_text(head + BEGIN + "\n" + text + "\n" + END + tail)
    print(json.dumps(metrics))


if __name__ == "__main__":
    main()
