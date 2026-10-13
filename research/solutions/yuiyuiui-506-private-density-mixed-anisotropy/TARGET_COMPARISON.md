# Correspondence with AIM Problem 506

Original statement:
[506-private-density-mixed-anisotropy.md](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/506-private-density-mixed-anisotropy.md).
Statement revision: `c9929805cece044705abaaebe1cebddac1ba11a6`.
Submitted result: *Minimax private density estimation with mixed anisotropy*,
Theorem 1, Eq.(3), with its proofs in Sections 2--4.
Evidence status: complete analytic solution claim, awaiting independent
mathematical assessment.

| Original requirement | Result and location in the manuscript | Scope |
|---|---|---|
| Domain [0,1]^d, stipulated real Fourier basis and tensor products | Section 1 defines the identical basis and indexing; Section 2 retains the sum Fourier weights | Exact |
| d>=2, R^2>d, A>0, positive integer beta/delta with common ratio | Section 1 assumptions before Theorem 1; all constant dependence in Theorem 1 | Exact |
| At least one delta_m<d and one delta_k>d | Section 1 keeps both strict inequalities and allows other delta=d coordinates | Full strict mixed class |
| Every probability density in W^beta(R) | Section 1 density class; Proposition 3 uniform upper bound; Section 4 lower family has deterministic positivity and exact Fourier-ball membership | Exact |
| Original adversarial discriminator ball and expected unsquared distance | Section 1 risk Eq.(2); exact weighted dual identity Eq.(4); pointwise norm-to-sign inequality Eq.(19) gives a lower bound for the expected norm itself | Exact |
| Every sequentially interactive alpha-LDP channel conditioned on all prior releases | Eq.(1) reproduces the privacy condition; Lemma 4 uses the full history and joint RN densities; the imported Theorem 10 has the same full-history class | Full mechanism infimum |
| Measurable L2-valued estimators | Eq.(2) specifies this value space; Eq.(8) gives a finite Fourier polynomial; Section 4 lower bound decodes any such estimator through continuous Fourier coordinates | Exact |
| 0<alpha<=A, n alpha^2>=1, constants independent of n and alpha | Theorem 1 and Proposition 3; Lemma 4 has n(e^alpha-1)^2 information bound; Section 4 extends the critical lower bound to every bounded T interval | Uniform original ranges |
| Matching lower and upper rates including necessary logarithms | Eq.(3): power for q>1, one log(eT) for q=1, parametric rate for q<1; q=sum_m 1/delta_m | All parameter tuples |
| Public imported lower theorem | Albert, Chevallier, Laurent and Sacko, JMLR 27(69), 2026, Theorem 10 p.14; complete applicable formula and interface in final proof on p.7 | Credited noncritical lower and bounded-T control |

The paper's three cases are determined by the harmonic mean
`bar_delta = d/q`, rather than by assigning all coordinates to one regime.
Its proof does not substitute a noninteractive minimax problem for the original
interactive problem. The upper construction is noninteractive and belongs to
the full allowed class; both lower arguments quantify over the full class.

The main contributions supplied in this manuscript are the weighted Fourier
coefficient sampling analysis for mixed anisotropy and the critical
orthogonal-information hypercube lower argument. A bounded prior-art check
does not establish an exhaustive novelty or priority claim.
