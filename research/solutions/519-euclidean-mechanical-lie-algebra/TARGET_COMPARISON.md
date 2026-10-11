# Correspondence with AIM problem 519

Target: [Universal identities for Euclidean mechanical Lie brackets](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/519-euclidean-mechanical-lie-algebra.md).
Statement revision: `c9929805cece044705abaaebe1cebddac1ba11a6`.

| Original requirement | Manuscript location and result | Coverage |
|---|---|---|
| Real scalar field and nonnegative direct-sum grading | Section 1, equation (1) | Identical category and bracket rule, including [L_0,L_0]=0 |
| Free object on A of degree 2 and B of degree 0 | Section 1 before Theorem 1.1; Section 2, equation (5) | Same degree-preserving assignment property; cited structural theorem applies to this object |
| Fixed kinetic energy T=|p|^2/2 | Section 1 definition of Phi and equation (2) | No variable metric, extra kinetic generators or additional potentials |
| Poisson sign f_q g_p-f_p g_q | Equation (2), and Section 3 following equation (12) | Explicit positive gradient-product identification |
| Every positive dimension and every smooth real potential | Theorem 1.1 and its final proof in Section 3 | Joint kernel already zero for the polynomial subclass, hence for all smooth potentials |
| No additional universal identities | Theorem 1.1, equation (3) | Full target: the joint kernel equals zero |
| No individual-potential injectivity required | Paragraph after Theorem 1.1 | Exactly the original universal quantifiers |
| All finite Lie orders and momentum degrees | Lemmas 2.1--2.3 and Proposition 2.4 | Large potential probes lower every nonzero positive homogeneous element; no order cutoff in the proof |
| Potential-part faithfulness | Lemmas 3.1--3.2 and equation (13) | Injective rooted-tree symmetrization, explicit incidence-jet separation and finite Taylor polynomial realization |

Public mathematical dependencies are McLachlan--Murua, Theorem 1 and section
2.3; Chapoton--Livernet, Theorem 1.9 and Corollary 1.10; and Bergeron--Loday,
Theorem 3.1. Section 3 proves the one-generator specialization and actual
potential realization explicitly. Appendix A supplies the associative
realization used for the marker argument. No private supplementary proof is
needed to read the manuscript.

Appendix B and the code provide supporting exact computations through order
18. The analytical proof is independent of these finite computations. No
formal proof-assistant verification or independent human peer review is
claimed. Please assess this as a complete solution claim.
