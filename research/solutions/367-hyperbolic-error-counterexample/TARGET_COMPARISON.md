# Target comparison: Problem 367

Target: [the complete public statement](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/367-universal-hyperbolic-error-rate.md), revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

Submitted result: Theorem 1.1 of [the manuscript](paper/paper.pdf), with its proof in Sections 2–3. This is a negative answer to the displayed universal rate. One admissible fixed system and fixed positive class parameters suffice to refute that universal assertion.

| Original requirement | Result and location in the manuscript | Scope |
| --- | --- | --- |
| A C4 flux, strictly hyperbolic near zero, with every field genuinely nonlinear | Equation (4), Section 1, p. 2: a polynomial diagonal two-component flux on U=(-1,1)^2; eigenvalues z1 and 2+z2, and field derivatives equal to one | All system hypotheses hold; the example is one fixed system |
| A uniformly strictly convex entropy pair with Dq=Deta Df | Equation (4) and its following calculation, p. 2: quadratic entropy with Hessian I and the displayed entropy flux | The prescribed single-entropy premise is met |
| Fixed T,R,M>0 and sufficiently small fixed delta | Theorem 1.1, p. 2, and the start of Section 3, p. 4: T=R=M=1; kappa chosen once below delta and the semigroup-domain threshold | Works for every sufficiently small fixed delta; no parameter varies with n |
| Flows into spatial L1 with values in U and support in [-R,R] | Equations (14)–(18), pp. 4–5: disjoint cells in [0,kappa], bounded amplitudes, summable masses and a uniform time modulus | Every approximation has the required range, support and continuity |
| Uniform total variation at most delta | Section 3 after (17), p. 5: TV at most 2kappa/3, justified on finite partitions | Uniform in time and approximation index |
| Initial discrepancy at most epsilon from the prescribed datum | Equations (15)–(16), p. 4, and the initial-trace argument, pp. 4–5: u^(n)(0)=u0 | The same datum is fixed for every n; discrepancy is zero |
| Time modulus M|t-s|+epsilon | Lemma 2.1, equation (9), and equation (18), pp. 3–5: the global modulus is at most (kappa^2/63)|t-s| | Stronger than the required bound with M=1 |
| Conservation residual for every signed scalar Cc1 test and every strip | Equations (1)–(2), Lemma 2.1 and the residual limit (19), pp. 1–5: the vector residual is exactly zero | Includes strips beginning at zero |
| Entropy residual for every nonnegative scalar Cc1 test and every strip | Equations (10)–(12), p. 3, and the bound following (20), p. 5: residual at least -epsilon_n(t-s)||phi_x||infinity | Stronger than the stated epsilon_n(t-s+epsilon_n) test-norm bound |
| Validity of countable sums and residuals at the accumulation point | Equations (17) and (19), p. 5: uniform L1 tails and an explicit bound for both endpoint and spacetime residual differences | No omitted limiting defect or initial-time strip |
| Comparison with the standard small-BV entropy semigroup | Equation (20), p. 5, using Bressan–Guerra Theorem 1.1 | The exact entropy profile is identified with S_t u0 |
| 0<epsilon<e^-1 and a constant depending only on the stated fixed data | Equations (5)–(6), p. 2, and (21), p. 6: epsilon_n=(kappa^4/12)2^(-14n), error=(kappa^2 t/4)2^(-6n), normalized ratio diverges | No finite permitted constant exists; even the initial datum remains fixed |

The only imported PDE theorem used to identify the comparison solution is [Bressan–Guerra, arXiv:2305.10737v1](https://arxiv.org/abs/2305.10737v1), Theorem 1.1 on PDF p. 3, with the small-BV domain inclusion described on PDF p. 1. The manuscript verifies strict hyperbolicity, field conditions, strict entropy convexity, exact conservation and entropy inequalities, L1 continuity and domain membership before invoking it. The cited survey supplies background and the rate question; the exact target is the fixed public statement above.

This is an analytic construction. It makes no claim of an optimal modulus, a counterexample for every flux separately, or failure of qualitative convergence. Independent review of the complete argument is requested.
