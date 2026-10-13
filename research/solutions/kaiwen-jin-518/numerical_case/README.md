# Numerical cases

The case definitions are in [config.json](config.json). All code imports
the supplied `kdvlogloss` library from `src/`. Install and test the package
using the commands in the [root README](../README.md).

The 48 global rows use eight real mean-zero input families normalized to
H^gamma norm 2, final time 0.25, initial bandwidth N = 8 or 16 and fixed
evolution cutoff K = 4*N. Each input uses six step counts, 16 through 512.
References use 8192 and 16384 steps. The predeclared empirical quality
criterion is reference difference / observed maximum error <= 0.01.

The 48 local cases have H^gamma norm 1, gamma in {0.1, 0.5, 1},
N in {4, 8, 16, 32}, tau = N^-3 and four phase families. All remainder
output modes through 3*N are retained. Input formulas are explicit in
`run_study.py` and Section 5 of the paper; seeds are fixed in `config.json`.

| Script | Output and purpose |
| --- | --- |
| `run_study.py` | Global/local cases, full Fourier checkpoints, step defects and feedback, timestep references, selected spatial/dtype/smooth-ODE checks and runtime metadata. |
| `validate_rough_ode.py` | DOP853 Galerkin checks for two generated reference trajectories, at two tolerance pairs. Requires `run_study.py` first. |
| `check_frequency_bounds.py` | Exact signed-integer comparisons for 2,085,056 finite quadruples and 989 seeded covariance samples; finite diagnostic only. |
| `export_publication_summary.py` | Copies the small scalar summaries/reports and extracts 17 scalar plot samples from locally generated data. Requires the preceding three scripts. |
| `make_figures.py` | Reads compact summaries and redraws three vector PDFs, the table and a numerical summary. No raw data required. |

Run the commands in this order to regenerate everything:

```bash
python numerical_case/run_study.py
python numerical_case/validate_rough_ode.py
python numerical_case/check_frequency_bounds.py
python numerical_case/export_publication_summary.py
python numerical_case/make_figures.py
```

Raw outputs are written to the ignored `results/` directory. The main runner
also accepts `--output` and `--config`; the rough-ODE checker uses the default
`results/` path. To preserve the supplied summaries during a rerun, export
with `--output numerical_case/reproduction_summary`, and plot with
`--summary numerical_case/reproduction_summary` after the checks.

Arrays in generated NPZ archives are plain numeric data; load them with
`np.load(path, allow_pickle=False)`. States are complex coefficient rows
on the explicitly stored modes; `time` records the sampling times. Reference
archives store every finest coarse-grid time rather than every internal
reference step. Checkpoints also retain the individual defect and feedback
and their Airy-transported sums.

The [summary directory](summary/README.md) explains the delivered measurements.
This is ordinary finite numerical evidence: smooth polynomial inputs,
nonrigorous reference trajectories and platform-dependent floating-point
arithmetic. It neither certifies the continuum theorem nor establishes a
uniform fully discrete rate or a lower bound. Apple Silicon longdouble has
the same recorded mantissa width as binary64; actual extra-precision checks
use mpmath in the test suite.
