# Compact numerical publication inputs

These files retain measured scalar quantities rather than Fourier trajectories:

- `global_summary.csv`: 48 rows with case identifiers, maximum reference
  error and its tau^gamma normalization, reference-quality fraction,
  error-energy fractions, defect coherence and reconstruction discrepancy.
- `local_summary.csv`: 48 rows with full/resonant normalized remainder
  norms and the absolute Fourier-envelope ratio.
- `defect_accumulation.csv`: 17 selected times and the norms of error,
  transported defect sum and transported feedback sum.
- `run_manifest.json`: original numerical settings, seed, runtime versions,
  numerical source hashes and resource observations.
- `validation.json`: selected spatial, dtype and independent smooth-ODE checks.
- `rough_ode_validation.json`: two DOP853 reference comparisons at two tolerances.
- `frequency_checks.json`: finite signed-integer and covariance diagnostics.
- `export_receipt.json`: hashes binding these inputs to the numerical export.

The original summaries describe the measurements used in the manuscript.
The [reproduction report](../../REPRODUCTION_REPORT.md) describes the additional
submission-package replay. The original runtime manifest is retained rather
than replaced with a later timing.

Run `python numerical_case/make_figures.py` from the package root to redraw
the figures. The full raw data can be regenerated locally using the commands
in the [parent README](../README.md). They are ignored and are not delivered.

The reference-quality fraction is an empirical two-resolution comparison,
not a rigorous reference-error bound. These files contain numerical evidence
and do not certify any infinite-dimensional estimate.
