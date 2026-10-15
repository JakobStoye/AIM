# Correspondence with AIM 529

This comparison uses the submitted manuscript and the [public problem](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/529-preferential-attachment-betti-limit.md),
frozen at AIM revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.
The result is an analytic solution claim pending independent mathematical review.

| Original requirement | Manuscript result and location | Scope |
| --- | --- | --- |
| Every fixed integer `q >= 2`, `m >= 2q`, real `delta > -m`, and `x < 1/(2q)` | Equation (1), Theorem 2.2 | Entire strict parameter regime; no additional hypothesis |
| Two initial vertices with `m` parallel edges; `m` sequential attachments with degree-plus-`delta` weights and no loops | Section 2, equation (2), Lemma 2.1 | Exact ordered process law, including partial births and multiplicity |
| Finite clique complex of the underlying simple graph, rational `beta_q(T)` | Section 2 and Section 4 | Same finite observable and coefficient field |
| Normalization by the ensemble expectation | Theorem 2.2, equation (7), Proposition 4.4 | Exact asymptotic mean; deterministic mean eventually positive |
| Convergence to a nondegenerate random variable | Theorem 2.2, equation (8), Proposition 5.1 and Lemma 4.3 | `W = A/E[A]`, positive almost surely and not almost surely constant |
| Determine the limiting law | Equations (3)–(6), (8) | Explicit independent-Beta and endpoint-uniform random-series construction |
| Establish or refute positive-exponent regular variation | Proposition 3.3 and Section 5, concluding proof of Theorem 2.2 | Every positive moment finite; the stated ratio fails for every finite positive exponent |
| Label-uniform control needed to pass from finitely many bases to the full law | Lemmas 3.1–3.2, Proposition 3.5 | Constants depend on fixed parameters and moment order, not labels or time; time limit precedes label-cutoff limit |
| Compare link births with actual finite homology | Lemmas 4.1–4.3, Proposition 4.4 | Exceptional links contribute lower order; earlier cones control inclusion ranks |

The main law is not a finite simulation or an infinite-complex homology result.
The manuscript does not claim moment convergence of the normalized Betti
numbers at every order, a density, an exact stretched-exponential tail, or
uniform estimates at the critical boundary.

The closest public references supply expectation/order estimates and the
Pólya and finite-link framework: Siu (2025), author preprint v2,
Definitions 3.1/3.3 and Theorem 4.1; Siu–Samorodnitsky–Yu–He (2025), author
preprint v3, Theorem 3 and Proposition 14. Dey–Terlov (2026), arXiv v1,
concerns triangles counted with edge multiplicity in the same graph family, a different observable.
The manuscript gives its own joint moment, label-summability and finite-chain
arguments. The probability interfaces cited from Durrett's fifth-edition
January 11, 2019 author draft are the independent-series theorem (2.5.6),
Kronecker's lemma (2.5.9), and the second Borel–Cantelli lemma (2.3.7),
used conditionally on the independent environment.
