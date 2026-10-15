# Exact profile-constant calculation

The files `data/Re_Pstar.dat` and `data/Im_Pstar.dat` contain the real and imaginary rational coefficients of the degree-50 Chebyshev polynomial P_* in Appendix A of:

Roland Donninger and Birgit Schörkhuber, *Self-Similar Blowup for the Cubic Schrödinger Equation*, [arXiv:2406.16597v3](https://arxiv.org/abs/2406.16597v3), 9 December 2025. Each file lists coefficients in increasing degree from 0 through 50. The mathematical coefficients are reproduced unchanged as inputs to the finite calculation in the accompanying note.

The exact input SHA-256 values are:

```text
a020445a9830aebbceebdda17f6771e33d0a3a714ab11d89aa00959e09b4970b  data/Re_Pstar.dat
de553121fc460e50f7a7246fd262f0bcb0c77ebbbdc5057521eaf56e31a3879c  data/Im_Pstar.dat
```

From the package root, run:

```sh
python3 code/check_constants.py
```

The script uses `fractions.Fraction` for every comparison. It checks all 51 complex input coefficients by file identity, computes the endpoint sums and derivative sum, and independently recomputes those values by generating the Chebyshev polynomials in the monomial basis. It then checks the three inequalities in Appendix A, the self-map and contraction bounds, the obstruction margins, and the sufficient positive-ionization envelope for the profile perturbation. All exact rational bounds appear in the JSON output. The recorded replay is `verification/exact_constants.json`; its Python-version field is execution metadata.

Python 3.13.3 was used; the program has no third-party dependencies. Run without `-O`: the program deliberately refuses optimized execution because its inequalities use assertions. Changed input hashes, a wrong coefficient count, or a failed exact inequality cause a nonzero exit.

This is a finite rational calculation. It does not reverify the published scalar inverse/residual bounds, simulate the coupled PDE, establish asymptotic parameter uniformity, or provide a numerical blowup datum. The value 10^(-23) belongs only to the profile forcing envelope; the full Cauchy construction makes a further qualitative smallness choice.
