# Reproducible numerical cases

The runner imports src/elliptic_widths rather than duplicating its method.
Configuration is in config.json; seed 5172026 fixes the NumPy random
stream, and the script fixes draw order.
The paper runner requires the stated geometry and degree/layer budget;
altered geometry is rejected before creating a result directory. General
radial geometries can be passed directly to the library.

## Campaign

For d=2 and d=3, use R=1, r=1/2, a core ending at 2^-8, 64 logarithmic
annuli and degrees 1 through 80:

| Case | Coefficients |
|---|---|
| 00 | a_r=a_t=1 |
| 01 | a_r=4, a_t=1/4 |
| 02 | alternating a_r=1/5 and 5, a_t=1/a_r |
| 03–19 | independent exp(Uniform[-3,3]) values per coefficient and layer |

Included mode counts are 160 and 6560. Every included mode is retained;
these are finite-degree spectra. Each case splits every annulus into two
equal logarithmic subintervals with unchanged coefficients to check
representation invariance. This is not mesh convergence. Constant cases
have exact analytic references.

There are 40 finite-form trials per dimension using random subspaces
of an ambient 40-mode space. The script constructs G<=beta B and
Eprime>=alpha Q, then checks the bound for trace(G^-1 Eprime).
This is a matrix experiment under prescribed premises, not a general
rough-coefficient PDE discretization. Counting is checked through 10,000
indices.

## Commands and retained results

~~~bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
  python3 numerical_case/run_cases.py
python3 numerical_case/plot_cases.py
~~~

Default results are in results/paper-v1. For another run:

~~~bash
python3 numerical_case/run_cases.py --output numerical_case/results/repeat-v1
python3 numerical_case/plot_cases.py --results numerical_case/results/repeat-v1
~~~

Existing result directories are never overwritten. Each new directory has:

- d2_case00.npz through d3_case19.npz: radii, coefficients, degreewise
  log ratios, multiplicity-expanded logs and both prefix bounds;
- manifest.json: complete configuration, case and finite-form check records,
  reference checks, margins, subdivision differences, elapsed time,
  runtime versions and SHA256 values for each array file. Full coefficient
  arrays are in the corresponding NPZ files.

Detailed arrays and manifests stay local and are ignored by Git.
summaries/paper_results.json retains the compact actual campaign result;
figures/ retains the vector PDFs used in the manuscript.

## Interpretation

Set L_m=2*sum(log s_j) and
B_m=(alpha/beta)*log(r/R)*sum(ell_j+d-2) for included prefixes.
The theorem requires L_m<=B_m<0. The second figure plots L_m/B_m:
at least 1 passes, and larger means stronger contraction. The vertical
axis is logarithmic. The first figure plots natural logarithms against
m or sqrt(m). No floor or clipping is used.

The recorded run passed 40 radial cases and 80 form trials. Its largest
constant-case log error is 1.71e-13; its largest subdivision difference
is 1.02e-12. Bound tolerance is 1e-8 and subdivision tolerance 2e-11.
These are binary64 numerical checks, not certified enclosures.
