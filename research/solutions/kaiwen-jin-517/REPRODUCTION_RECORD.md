# Recorded reproduction

Date: 11 October 2026. The supplied paper and numerical package were checked
from a separate directory containing only the selected public inputs.
The recorded software versions are in [ENVIRONMENT.json](ENVIRONMENT.json);
dependency pins are in [requirements.txt](requirements.txt).

The following commands use the package root and a fresh result directory:

~~~bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src OPENBLAS_NUM_THREADS=1 \
  OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
  python3 -m unittest discover -s test -v
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
  python3 numerical_case/run_cases.py --output numerical_case/results/reproduction
python3 numerical_case/plot_cases.py --results numerical_case/results/reproduction
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
~~~

Actual outcomes:

- All 23 unit tests passed, including independent 70-digit matrix-exponential
  references, analytic constant-coefficient formulas, basis and layer
  invariance, multiplicity counting and invalid-input checks.
- All 40 radial cases and 80 finite-form comparisons passed. Counting was
  checked through 10,000 indices. Every reproduced numerical array agreed
  entry by entry with the original recorded array, and the compact summary
  matched [paper_results.json](numerical_case/summaries/paper_results.json).
- The maximum constant-case log error was 1.71e-13 and the maximum layer
  subdivision difference was 1.02e-12. Bound tolerance was 1e-8 and subdivision
  tolerance was 2e-11. These are binary64 checks, not certified enclosures.
- Both regenerated vector figures had exactly matching rendered pixels and
  text. The supplied figure bytes are retained as the publication inputs.
- The manuscript compiled to 11 pages without warnings. The rebuilt PDF's
  extracted text and word positions matched the supplied PDF. All 34 labeled
  targets and 37 typed reference uses passed the reference-type preflight.

Detailed result arrays are generated locally and ignored by Git. The inputs,
scripts, vector figures and compact summaries are included. These experiments
are ordinary finite-case evidence. They do not certify the analytic theorem
for every coefficient, constitute formal verification, or supply independent
human mathematical review. The full analytic proof appears in the manuscript.
