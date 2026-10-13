# Universal identities for Euclidean mechanical Lie brackets

Manuscript and exact computational material for AIM problem 519.

The paper proves that the joint kernel of all Euclidean mechanical Poisson
realizations is zero, already for polynomial potentials. The argument uses
degree lowering and a separate tree/jet separation proof. The computations
are supporting finite checks, not the proof of the all-order theorem.

Author: Kaiwen Jin. Contact: yui.ui.siki@gmail.com.

- `paper/main.pdf`: complete manuscript, including its AI-assistance statement.
- `paper/main.tex`: editable, standalone LaTeX source.
- `TARGET_COMPARISON.md`: correspondence with the original quantified target.
- `src/aim519/`: exact ComMag, associative, mechanical-tree, polynomial and
  finite-field routines.
- `test/`: mathematical reference cases, independent identities and corrupted
  certificate checks.
- `numerical_case/`: case drivers, reproduction instructions and small summaries.

## Reproduction

The computational library uses only the Python standard library. Python
3.13.3 is the tested interpreter; Python 3.11 or later is required. No package
installation is needed for these commands, run from the repository root:

```sh
PYTHONPATH=src python3 -m unittest discover -s test -v
python3 numerical_case/run_cases.py audit --max-order 18 --output numerical_case/results/order18
python3 numerical_case/run_cases.py replay --certificate numerical_case/results/order18/data/rank_certificates.json.gz --output numerical_case/results/replay
python3 numerical_case/run_cases.py crosscheck --output numerical_case/results/crosscheck
```

Every output directory must be fresh. Full integer matrices, elimination
pivots, lowering traces, timings and source/output hashes are stored locally
and can be regenerated. Large raw outputs are excluded from Git; selected
small publication summaries remain available in `numerical_case/summaries/`.
Computation is sequential and exact. Cached sparse mappings have a fixed LRU
cap of 4096 entries per function. Finite-field rank uses the prime 1000003;
the direct polynomial checks use rational coefficients.

Build the manuscript with a LaTeX distribution providing the listed standard
packages:

```sh
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The original target is
[AIM 519 at revision c9929805cece044705abaaebe1cebddac1ba11a6](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/519-euclidean-mechanical-lie-algebra.md).
This package presents a complete solution claim for mathematical review.
Repository validation and AI-assisted checking do not constitute independent
human peer review or acceptance by the problem catalogue.
