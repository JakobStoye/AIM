# Target comparison for AIM 650

Original target: [Central limit theorem for the first path Betti number](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/650-random-digraph-path-betti-central-limit.md), repository revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

| Original requirement | Manuscript location | Coverage |
|---|---|---|
| Random digraph on `[n]`, no loops, independent ordered edges of probability `p_n` | Section 1 model, Theorem 1 | Same model; reverse orientations are independent and both may occur. |
| Rational non-regular sequence chains; repeated vertices and diagonal boundary terms retained | Section 1 definitions, Lemma 1 | Same convention; an individual reciprocal path is excluded from Omega_2 and common-base differences are retained. |
| Omega_0=A_0 and Omega_k=A_k intersect boundary inverse of A_(k-1) | Section 1 definitions, Lemma 1 | Exact stated complex and quotient; no replacement by regular homology. |
| Every sequence with n p_n tending to infinity and n^(2/3) p_n tending to zero | Theorem 1, equations (1), (11)–(16) | Full original sequence range, without a power law, monotonicity, or connectivity assumption. |
| Actual expectation in the centering | Equation (17), proof of Theorem 1 | Exact identity and true centered correction; no approximate mean substitution. |
| Actual variance in the denominator | Equations (18)–(19), closing proof | Variance equivalence and eventual positivity are proved before transfer to the true denominator. |
| Convergence in distribution to N(0,1) | Theorem 1 and final characteristic-function argument | Full asserted limit. |
| Source's integer non-regular rank represented over Q | Section 1 rational definition | The proof treats the rational dimension specified by the original statement. |

The additional conclusion is `Var B_n ~ n(n-1)p_n(1-p_n)`. Section 2 proves negligible boundary-rank variance; Section 3 proves negligible weak-component variance even for disconnected graphs.

The only imported probability facts are the standard normal characteristic function (Chatterjee, Proposition 5.11.1) and Levy's continuity theorem (Doebler, Theorem 1.1). Their stated conventions and hypotheses are given at the end of Section 4 and checked through the explicit characteristic-function convergence. Chaplin is credited for the source conjecture and generator background. See [references](REFERENCES.md).

The submitted manuscript contains the complete analytic argument and its public dependencies. Independent mathematical review is requested.
