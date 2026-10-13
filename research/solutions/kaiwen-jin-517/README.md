# Local elliptic approximation widths — AIM 517

Author: Kaiwen Jin (yui.ui.siki@gmail.com).

The manuscript proves

    d_n(T) <= C exp(-c n^(1/(d-1))), d=2,3, n>=1,

for the normalized cutoff operator for scalar, real symmetric uniformly
elliptic equations on nested cubes, with measurable bounded coefficients.
Constants may depend on the fixed coefficient, geometry and cutoff.
The exact target is [AIM Problem 517 at its frozen revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/517-sharp-local-elliptic-widths.md).
The paper gives the complete analytic proof; numerical checks are separate
finite-case evidence.

## Contents

- paper/main.pdf: manuscript; main.tex and references.bib: editable source.
- paper/REFERENCE_GUIDE.md: primary source links and passage locations.
- src/elliptic_widths: sphere counting, matrix comparisons and logarithmically
  rescaled exact radial propagation.
- test: independent reference, invariance and invalid-input tests.
- numerical_case: fixed configuration, reproducible cases, vector figures
  and a compact recorded summary.

The [target comparison](TARGET_COMPARISON.md) maps the original requirements
to the manuscript. The [recorded reproduction](REPRODUCTION_RECORD.md) gives
the actual validation outcomes.

## Reproduce

The recorded environment is Python 3.13.3, NumPy 2.4.4, matplotlib 3.10.9
and mpmath 1.3.0. Prepare a clean environment with:

~~~bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 -m pip install --no-deps -e .
~~~

Run the validation suite:

~~~bash
PYTHONPATH=src OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
  VECLIB_MAXIMUM_THREADS=1 python3 -m unittest discover -s test -v
~~~

Generate all 40 radial cases and 80 matrix comparisons, then the figures:

~~~bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
  python3 numerical_case/run_cases.py
python3 numerical_case/plot_cases.py
~~~

The runner refuses to overwrite existing results. For a separate run use
--output numerical_case/results/repeat-v1, then pass that directory as
--results to the plotter. Raw arrays and the detailed input, environment
and hash manifest remain in numerical_case/results/, ignored by Git.
Scripts, configuration, figures and the compact summary are versioned.
See [case documentation](numerical_case/README.md).

Build with TeX Live:

~~~bash
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
~~~

Supplied figures make a paper build independent of rerunning experiments.
The numerical method uses exact layer exponentials, with binary64 roundoff
and finite angular truncation. Its checks are not formal verification or
independent human review of the analytic proof.
