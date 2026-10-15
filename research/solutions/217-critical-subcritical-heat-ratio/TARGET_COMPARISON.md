# Comparison with AIM Problem 217

Target: [the complete problem statement at revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/217-critical-subcritical-heat-ratio.md).

Proposed resolution: the [manuscript](paper/main.pdf), Theorem 1.1, gives a counterexample to the full universal question. Section 1 restates the original hypotheses and explains why a diagonal test of the conclusion is admissible even though the integral-test points must be distinct.

| Original requirement | Constructed object or verification | Manuscript location |
| --- | --- | --- |
| Connected, complete, noncompact smooth manifold without boundary | The Euclidean line with its usual metric | Theorem 1.1 and the following paragraph, pp. 1–2 |
| Two smooth real potentials bounded below | One fixed nonnegative compact bump `q`; one fixed `V_0 = w'' + (w')²`. Both are smooth and bounded | Lemma 2.3, p. 3; Section 3, pp. 4–5 |
| Friedrichs realizations on the same square-integrable space | Both operators act on `L²(R,dx)`, with the standard bounded-potential form/domain | Theorem 1.1, p. 1; start of Section 2, p. 2 |
| Both operators nonnegative | Positivity of `q`; factorization of the reference quadratic form | Lemma 2.3, p. 3; equation (16), p. 4 |
| Both spectral bottoms zero | Translated free test functions for the numerator; explicit resistance-tent tests for the final reference | Lemma 2.3, p. 3; Section 3, p. 6 |
| One fixed pair of distinct points with finite numerator integral | The pair `(0,1)`; explicit positive zero-energy solution and finite Green limit | Lemmas 2.2–2.3, p. 3; Appendix A, pp. 6–8 |
| The same pair with infinite reference integral | Preserved unit zero intervals make both resistance integrals infinite; the exact Green exhaustion gives divergence at `(0,1)` | Equations (20)–(21), p. 5; Section 3, p. 6; Appendix A |
| Reference has no nonzero square-integrable zero mode | A form-zero vector must be a multiple of `exp(w)`; this function is at least one everywhere | Factorization discussion, p. 4, applied to the final reference on p. 5 |
| No potential ordering is assumed | No ordering is imposed; the constructed potential difference takes both signs | End of Section 3, p. 6 |
| Claimed limit for every compact subset of the product manifold | At times tending to infinity, the quotient at `(0,0)` is at least the sequence index; choose the compact singleton `{(0,0)}` | Theorem 1.1, equations (3)–(4), pp. 1–2; concluding estimate, p. 6 |

The construction yields one fixed pair, rather than a sequence of counterexamples depending on the observation time. Each finite approximation has its own strictly positive gap. Its time is selected first, followed by a radius that protects the estimate under all later exterior changes. Only local stabilization is used to define the final smooth potential. The final reference has spectral bottom zero.

The conclusion is an infinite limsup along a sequence, which already negates the proposed zero limit. The manuscript makes no claim about all-time quotient asymptotics or about the ordered nonnegative-perturbation comparison. Its citations distinguish the original question from the conditional results. This is a complete analytic counterexample claim submitted for independent review; no numerical or formal evidence is substituted for its proof.
