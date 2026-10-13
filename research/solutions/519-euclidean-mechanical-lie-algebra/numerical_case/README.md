# Exact paper cases

`run_cases.py` calls the library in `src/aim519`, without third-party numerical
dependencies. The tested environment is CPython 3.13.3 on macOS arm64.
Integer coefficients have arbitrary precision; polynomial coefficients use
`fractions.Fraction`. The modular arithmetic is in the prime field F_1000003.
No floating-point tolerance or singular-value rank cutoff is used.

| Case | Configuration | Saved local detail | Small published output |
|---|---|---|---|
| `audit` | Orders 1--18; marker with 10 leaves; prime 1000003 | Every integer mechanical-tree column, source label, elimination pivot and block hash | Full order table and audit summary |
| `replay` | All blocks of the generated certificate | Verified order/degree block list and input/output manifest | Column/block totals |
| `crosscheck` | d=2; potential degree 5; seeds 519 and 2026; order 8; q=0, p=(1,2) | Exact pointwise value comparisons and iterated-lowering traces | Counts for 80 pointwise value comparisons; 8 lowering cases and 17 steps through order 5 |

Commands are in the root README. Run one numerical process at a time. Use a
new output directory for every run; an existing directory is rejected. An
order-10 pilot is obtained by changing `--max-order 18` to `--max-order 10`.
The drivers deliberately cap the audit at order 18. Higher cutoffs and
higher-order iterated lowering need a separate resource assessment: recursive
expressions grow quickly, even though the arithmetic is exact.

Tree arithmetic uses canonical unrooted encodings and counts isomorphic
outputs with multiplicity. A momentum-bearing tree has a thick core and a
nonnegative number of momentum leaves at each vertex. The free Lie input is
expanded as an integer polynomial in associative words before evaluation.
The normal ordering uses `x*A=A*x+y_x` and `x*y_s=y_s*x+x*s`, preserving the
paper's Poisson sign.

The replay module is separate from the tree construction: it checks the
supplied integer matrices and pivots without reconstructing brackets. The
audit driver reconstructs all columns, which is necessary to validate their
relation to the algebra. The sparse-polynomial implementation independently
calibrates the contractions by direct rational Poisson differentiation.

The prime-field full-rank result implies rational and real full column rank
for each finite integer matrix. A failure at a different prime would not
by itself prove rational dependence. The finite cutoffs do not establish
the all-order theorem, which has an analytical proof in the manuscript.

Use `plot_dimensions.py --table summaries/rank_summary.csv --output figures/dimensions.svg`
to regenerate the small vector plot. It displays integer source dimensions
and modular ranks by original-letter order, not errors or convergence rates.
