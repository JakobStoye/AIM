# Correspondence with AIM 554

Target: [554 — Sharp asymptotic constant for rational approximation of fractional inverse powers](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/554-stieltjes-rational-asymptotic-constant.md), repository revision `c9929805cece044705abaaebe1cebddac1ba11a6`. All locations below refer to the submitted final manuscript, *The leading constant for rational approximation of fractional inverse powers*.

| Original requirement | Manuscript result and location | Coverage |
| --- | --- | --- |
| Every fixed `0<a<b<infinity` and every fixed `0<gamma<1`, followed by `n -> infinity` | Theorem 1; Section 3.2 fixes the interval, exponent and tolerance before the degree limit, then sends tolerance to zero | Full fixed-parameter scope |
| Real numerator degree at most `n-1`, denominator degree at most `n`, denominator nonzero on `[a,b]` | Equation (1); Section 3.1 constructs an admissible interpolant of exactly the allowed type by the Mobius degree cancellation and positive Jacobi orthogonality | Full approximation class |
| No restriction on poles outside the interval | Section 3.2 compares the constructed interpolant against every admissible real rational function by a difference numerator of degree at most `2n-1` | Full; the lower bound does not restrict competing poles |
| Absolute maximum error, without a relative-error substitution | Equation (1), interpolation error (18), and the weighted bounds in Section 3.2 | Full absolute uniform norm |
| Elliptic modulus `k=(sqrt(b)-sqrt(a))/(sqrt(b)+sqrt(a))`, with the stated complete-integral convention | Equation (2) and Lemma 3 identify the slit-disk radius as `exp(-mu(k))` using the relative square-root benchmark | Same normalization |
| Leading constant `4(ab)^(-gamma/2) sin(pi gamma)` | Theorem 1, equation (3); equation (15) supplies the geometric mean and Section 3.2 supplies both matching minimax bounds | Full proposed limit |

## Public theorem dependencies

- Baratchart and Yattselev, *Convergent interpolation to Cauchy integrals over analytic arcs with Jacobi-type weights*, IMRN 2010, [doi:10.1093/imrn/rnq026](https://doi.org/10.1093/imrn/rnq026), [arXiv:0911.3850v1](https://arxiv.org/abs/0911.3850v1), Theorem 2 on preprint p. 7; Definitions 1–2 on pp. 5–6; equations (2.5), (2.9), (2.11). Section 3.1 verifies the Jacobi exponents, source smoothness, fixed separation and local product decay. The normalized counting measures of the particular constructed node scheme converge. Its geometric mean and normalized Szego function are evaluated in (19)–(20).
- Braess and Hackbusch, *On the approximation of Stieltjes functions by exponential sums and rational functions with applications to partial differential equations*, Numerische Mathematik 158 (2026), [doi:10.1007/s00211-025-01523-1](https://doi.org/10.1007/s00211-025-01523-1), Theorem 4.2. Lemma 3 uses its exact relative type `(n,n-1)` square-root asymptotic to identify the radius. The manuscript proves the necessary alternating comparison itself. Equation (3.5) supplies the elementary beta integral used in (17).
- Baratchart, Prokhorov and Saff, *Asymptotics for minimal Blaschke products and best $`L_1`$ meromorphic approximants of Markov functions*, CMFT 1 (2001), 501–520, [author PDF](https://math.vanderbilt.edu/saffeb/texts/193.pdf), Section 3 on pp. 6–7. Section 2 uses its annulus/Green geometry and proves the needed weighted interval supremum construction. Its L1 approximation conclusions are not substituted for an absolute uniform result.
- Bak and Newman, *Complex Analysis*, third edition, [doi:10.1007/978-1-4419-7288-0](https://doi.org/10.1007/978-1-4419-7288-0), Section 7.2, for analytic-arc reflection. Section 2 supplies the endpoint square-root argument and holomorphic descent needed here.

The manuscript contains the supplementary weighted construction, its alternating values, the precise subdiagonal rational transfer and the full-class lower bound. Its published argument and cited sources support the complete fixed target; the submission requests independent assessment.
