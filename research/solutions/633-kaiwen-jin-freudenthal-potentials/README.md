# AIM 633: Local potential bases on Freudenthal meshes

Submission package, version 0.1.0, by **Kaiwen Jin**
(`yui.ui.siki@gmail.com`). It addresses [problem 633](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/633-freudenthal-local-potential-basis.md)
at AIM revision `c9929805cece044705abaaebe1cebddac1ba11a6`.

The manuscript claims a complete affirmative resolution of the local-support
target: for every integer `N >= 1` and `k >= 5`, the actual continuous vector
piecewise degree-`k+1` potential space with continuous curl on the stated
Freudenthal mesh has a basis supported on single closed vertex stars. No
boundary condition or gradient quotient is added. This is a natural-language
computer-assisted proof, submitted for independent mathematical review.
It does not claim a uniform decomposition norm, multigrid convergence or
proof-assistant verification.

## Materials

| Path | Purpose |
|---|---|
| `paper/main.pdf`, `paper/main.tex` | Complete paper and standalone editable source |
| `TARGET_COMPARISON.md` | Original-target correspondence and scope |
| `src/freudenthal/` | Numerical library, independent integer assembly and finite checking programs |
| `src/freudenthal/certificates/` | Essential fixed integer witnesses and file/member manifests |
| `test/` | Geometry, rank, locality, evaluation and persistence regressions |
| `numerical_case/` | Ten-case driver, full row-length histograms and compact results |
| `paper/figures/` | Vector figure exports |
| `VERIFICATION.md` | Actual isolated-package execution outcomes and limitations |
| `PUBLIC_MANIFEST.json`, `SHA256SUMS` | Exact package-file inventory and hashes |

The source embeds the bibliography and plot, so it can be compiled as a
standalone LaTeX document. A C++17 compiler is required for the complete
certificate replay. The frozen Python environment uses Python 3.13; other
supported Python versions can resolve compatible validation dependencies.

## Reproduction

Run these commands from this package directory, not from the AIM repository
root:

```bash
python3.13 -m venv .venv
.venv/bin/python -m pip install -r requirements-lock.txt
.venv/bin/python -m pip install . --no-deps
.venv/bin/python -m pytest -p no:cacheprovider test
.venv/bin/python -m ruff check src/freudenthal test numerical_case/*.py verify_all.py

OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
  .venv/bin/python verify_all.py --output numerical_case/results/certificates
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
  .venv/bin/python numerical_case/run_cases.py --output numerical_case/results/paper_cases
.venv/bin/python numerical_case/plot_results.py
```

The drivers refuse existing output directories. Select a new `--output` path
for a repeat run. Plotting with `--update-paper` also regenerates the marked
inline plot in the editable manuscript. See [the API guide](src/README.md),
[case instructions](numerical_case/README.md) and
[certificate description](src/freudenthal/CERTIFICATES.md).

Full generated bases and logs are reproducible local outputs, rather than
distributed ordinary numerical data. The fixed 8.5 MB certificate inputs
are included because the theorem's finite identities require them.

## AI use and review

ChatGPT assisted with the candidate construction and certificate-producing
code. Codex assisted with the expanded proof, implementation, tests,
reference checks and manuscript preparation. The paper includes this
disclosure at its end. No separate detailed AI referee report is submitted;
independent review of the complete mathematical argument is requested.
Successful execution of the finite checks does not replace the analytical
arguments covering every grid and degree.
