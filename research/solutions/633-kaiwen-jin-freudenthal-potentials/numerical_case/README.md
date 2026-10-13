# Paper cases and figures

From the package directory, after installation:

```bash
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
  .venv/bin/python verify_all.py --output numerical_case/results/certificates
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
  .venv/bin/python numerical_case/run_cases.py --output numerical_case/results/paper_cases
.venv/bin/python numerical_case/plot_results.py
```

Use fresh output directories. The complete campaign runs one process at a
time and one numerical-library thread. `CXX` can select the C++17 compiler.

The driver constructs exactly the ten Table 1 cases: `(N,d) = (1,6), (2,6),
(3,6), (4,6), (5,6), (7,6), (2,7), (4,7), (3,13), (2,20)`. Each basis
has integer coefficients, zero all-component curl residual, a checked owner
star for every row and checked independence. These are finite regression
cases, not convergence or conditioning experiments.

Local case directories contain sparse basis/normal-form arrays, parameter
and owner metadata, check summaries and invocation/source/environment hashes.
The small `summaries/` files retain dimensions, scalar-entry counts, complete
row-length histograms and figure metrics. No randomness is used. Local run
times are observations rather than comparative performance claims.

The plot uses every histogram bin for `N=4,d=6` and `N=4,d=7`, normalized by
the respective dimension. Its unit is nonzero scalar component entries
`(q,j)` in vector Bernstein coefficients. Output is PDF/SVG/PGF. The optional
`--update-paper` argument regenerates only the marked inline plot in
`paper/main.tex`. Full generated matrices and logs are ignored; the fixed
proof-critical witness files under `src/` are distributed.
