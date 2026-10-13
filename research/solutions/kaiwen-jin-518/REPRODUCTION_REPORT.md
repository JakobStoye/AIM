# Numerical reproduction and document build

**Date:** 10 October 2026.  
**Scope:** execution of the delivered numerical code and checks of the delivered document files.  
**Executor:** Codex using the supplied Python package and recorded runtime.

## Environment and installation

The submission package was installed in a separate verification environment
with `pip install -r requirements-lock.txt -e .`. Its imported `kdvlogloss`
module was checked to come from the exported package's own `src/` directory.
All 17 locked dependency versions matched. The runtime was Python 3.13.3
on macOS/arm64, with NumPy 2.4.4, SciPy 1.18.1, Matplotlib 3.10.9,
pytest 9.1.1 and mpmath 1.3.0. Numerical-library threads were capped at one.

## Actual checks

| Command or check | Recorded result |
| --- | --- |
| `python -m pytest -q` | 21 passed; zero failures, errors or skips. |
| `python numerical_case/run_study.py` | 48 global rows and 48 local cases; all 48 global reference-quality checks passed. Replay took 83.87 seconds with 384.3 MB recorded peak resident memory. |
| `python numerical_case/validate_rough_ode.py` | Both DOP853 case comparisons reproduced the supplied numerical values. |
| `python numerical_case/check_frequency_bounds.py` | 2,085,056 finite integer quadruples and 989 seeded covariance samples passed. |
| `python numerical_case/export_publication_summary.py --output numerical_case/reproduction_summary` | Global/local CSVs, the 17-sample defect CSV, spatial/dtype/smooth-ODE report and finite frequency report reproduced byte for byte. The rough-ODE case values also matched; elapsed-time metadata can differ. |
| `python numerical_case/make_figures.py` | All three vector figures regenerated and rendered identically to the supplied original figures. |
| Numerical source hashes | All five source hashes in the original campaign manifest matched the delivered files. |
| Manuscript plot data | All 135 coordinate pairs in 21 inline plot curves matched the supplied CSVs, allowing the source's displayed decimal rounding. |
| Standalone LaTeX source | Successful compilation with the Codex desktop editor's compiler; the canonical PDF was exported with two successful pdfLaTeX runs, without warnings or bad-box messages. |
| PDF/source availability | Complete 15-page PDF, matching standalone source, embedded bibliography/table/plot coordinates and final AI use declaration; no additional files are needed to compile the article. |

The original runtime metadata used in the article is retained in
`numerical_case/summary/run_manifest.json`. The original and replay timing
observations are distinct measurements. Generated arrays and replay outputs
are reproducible local files and are excluded from this material package.

## Interpretation

The tests check the implemented update against independent literal and
high-precision expansions, invariants and an independently time-integrated
Galerkin ODE. The campaign's 0.01 reference-quality threshold compares two
reference timesteps; it supplies no rigorous error enclosure. The finite
frequency checks do not prove an infinite-frequency inequality. The dtype
comparison on this Apple Silicon runtime supplies no extra mantissa bits;
the high-precision tests use mpmath instead.

This record supports numerical reproducibility and file concordance.
Independent mathematical review of the complete analytic argument remains
requested. No formal verification or human peer review is claimed here.
