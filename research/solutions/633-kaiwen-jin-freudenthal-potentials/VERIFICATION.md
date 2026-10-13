# Execution evidence for the submitted package

The files in this package were installed and executed in a fresh Python
environment on macOS arm64 on 11 October 2026. Only this package's source,
fixed certificate inputs, tests and drivers were needed. The complete
certificate replay and the ten paper cases used one process at a time,
with `OMP_NUM_THREADS`, `OPENBLAS_NUM_THREADS` and
`VECLIB_MAXIMUM_THREADS` all set to `1`. No random seed is needed.

## Environment and commands

Python 3.13.3; NumPy 2.5.3; SciPy 1.18.1; SymPy 1.14.0;
pytest 9.1.1; Matplotlib 3.11.2; Ruff 0.17.0. The full dependency pins are
in `requirements-lock.txt`. The C++ compiler was Apple clang 17.0.0
(`clang-1700.6.4.2`). The exact parameter checker was compiled as C++17
with `-O2 -Wall -Wextra -Werror -fsanitize=undefined
-fno-sanitize-recover=all`.

From the package directory, the following commands reproduce the checks
after the environment setup in `README.md`:

```bash
.venv/bin/python -m pytest -p no:cacheprovider test
.venv/bin/python -m ruff check --no-cache src/freudenthal test numerical_case/*.py verify_all.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
  .venv/bin/python verify_all.py --output numerical_case/results/certificates
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
  .venv/bin/python numerical_case/run_cases.py --output numerical_case/results/paper_cases
.venv/bin/python numerical_case/plot_results.py
```

Use fresh output directories; the drivers refuse to overwrite earlier runs.
The library used by the certificate and case drivers was the installed
package. Unit tests read the same submitted source through the package's
pytest configuration.

## Outcomes

All 34 tests passed; Ruff passed. The complete certificate replay exited
successfully, including independent assembly of the integer curl constraints,
small-grid rank and residual certificates, degree-six normal-form transfer
and local repairs, all-degree symbolic sources, pivot/support checks,
reverse row identities and exact dimension counts. The C++ checker completed
with the enabled undefined-behavior sanitizer. Its reported finite traversal
counts include 249,177 unbounded parameter chambers for pivot/support and
144,744 for the reverse identities. See
`numerical_case/summaries/certificates.json` for the complete compact results.

Every paper case passed the exact all-component curl constraints, the
row-by-row owner-star support check and independence check. The dimensions
and scalar nonzero-entry counts reproduce Table 1:

| N | Potential degree d | Dimension | Scalar nonzero entries |
|---:|---:|---:|---:|
| 1 | 6 | 795 | 3,072 |
| 2 | 6 | 4,164 | 27,565 |
| 3 | 6 | 11,913 | 97,975 |
| 4 | 6 | 25,842 | 238,875 |
| 5 | 6 | 47,751 | 478,780 |
| 7 | 6 | 122,709 | 1,342,470 |
| 2 | 7 | 6,792 | 35,712 |
| 4 | 7 | 43,962 | 307,104 |
| 3 | 13 | 148,749 | 421,569 |
| 2 | 20 | 178,548 | 335,622 |

The driver retains complete row-length histograms and deterministic basis
hashes in `numerical_case/summaries/`. Figure regeneration uses every bin
for the two `N=4` cases and agrees with the manuscript's inline plot.
The mean scalar counts are approximately 9.24367309 for `d=6` and
6.98566944 for `d=7`; both maximum row counts are 69. Runtime observations
in the JSON files are not comparative performance results.

The submitted standalone TeX compiled successfully, and the 12-page PDF
was checked for the edited availability text, figure layout, references
and final AI-use disclosure. The source and PDF hashes, along with all
other distributed files, are recorded in `PUBLIC_MANIFEST.json` and
`SHA256SUMS`.

## Mathematical interpretation

These executions validate the distributed finite witnesses and the
implementation regressions. The all-parameter conclusion additionally
depends on the analytical coverage and transfer arguments in Section 3
of the paper. The numerical cases alone do not imply it. This package
contains a complete natural-language computer-assisted solution claim;
it does not assert proof-assistant verification or independent human
certification. Independent mathematical review is requested.
