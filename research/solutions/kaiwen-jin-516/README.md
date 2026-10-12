# AIM 516: tails of uniform-DAG Markov equivalence classes

Proposed complete resolution by Kaiwen Jin. Contact: yui.ui.siki@gmail.com.

The [manuscript](paper/main.pdf) proves universal constants c,C>0 with

```math
\Pr(|M(G_n)|>t)\le C\exp[-c(\log t/\log\log t)^2]
```

for all sufficiently large real t, uniformly in every integer n>=1. Here G_n
is uniform over simple labeled DAGs, and M(G_n) consists of DAGs with the same
skeleton and unshielded colliders. Corollary 1.2 gives every requested exponent
2-epsilon. The stronger intermediate theorem is a Gaussian tail for vertices
in nontrivial essential-graph components. Complete skeletons give the matching
exponential scale and rule out a uniform endpoint exp[-c(log t)^2].

The [target comparison](TARGET_COMPARISON.md) records the full quantifiers and
manuscript locations. [Editable source](paper/main.tex) and a
[primary-reference guide](paper/REFERENCE_GUIDE.md) are included. The proof is
analytic; no computation is a premise of the theorem. Catalogue classification
and independent mathematical assessment remain with the receiving maintainers.

## Finite verification

The standalone script independently enumerates the 543 labeled DAGs on four
vertices, groups them into 185 Markov equivalence classes, integrates the
auxiliary within-layer rankings with exact fractions, and checks the source
weights, prefix identity and necessary component conditions. It is a finite
consistency check, with no implication of asymptotic or formal verification.
It requires only the Python standard library.

From this package directory, run:

```sh
python3 verification/verify_small_graphs.py > verification/reproduced.json
python3 - <<'PYCODE'
import json
from pathlib import Path
expected = json.loads(Path("verification/summary.json").read_text())
actual = json.loads(Path("verification/reproduced.json").read_text())
assert actual == expected
print("Exact finite reproduction matches the recorded summary.")
PYCODE
```

To build the manuscript from its public source:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=paper/build paper/main.tex
```

The [reproduction record](REPRODUCTION_RECORD.md) and
[environment description](ENVIRONMENT.json) state the tested scope.
[MANIFEST.json](MANIFEST.json) and [SHA256SUMS](SHA256SUMS) identify the supplied
files. A rebuilt PDF can differ bytewise because of timestamps; the supplied
PDF is the fixed manuscript artifact.

## AI use and review

OpenAI Codex (GPT-6.1 Sol) assisted with the argument, source checks, finite
verification, writing and typesetting. The manuscript contains a complete
proof and an AI-use declaration. These AI checks are not independent human
review or formal verification. No separate detailed AI review is submitted;
independent mathematical review is requested.
