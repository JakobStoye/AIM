# Target comparison for Problem 478

The target is [Problem 478: Global regularity for critical SQG with state-dependent noise](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/478-critical-stochastic-sqg-global-regularity.md), at revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.
The result claimed in the accompanying manuscript is Theorem 1.1.

| Original requirement | Manuscript result and location | Coverage |
|---|---|---|
| Critical Ito SQG on the two-dimensional torus, Lambda=(-Delta)^(1/2), Riesz multipliers zero on constants | Equation (1.1), conventions at the end of Section 1, and the full-space realization (2.1) | Same equation and normalization. The constant mode is retained. |
| Every deterministic smooth periodic datum | Assumptions before Theorem 1.1 and Proposition 2.1 | Entire stated datum class; no smallness or zero-mean condition. |
| Every finite smooth coefficient family, globally scalar-Lipschitz uniformly in space, bounded positive-order derivatives and bounded g_k(x,0) | Equation (1.2), Theorem 1.1, local composition estimate (2.3), noise increment estimate (4.2), and tame estimate (4.12) | Full stated spatial/state-dependent nonlinear class. No affine or additive restriction. |
| Prescribed independent Brownian motions and adapted pathwise solution | Theorem 1.1, Proposition 2.1, and final proof in Section 4.4 | Same stochastic basis and Brownian motions; no replacement noise. |
| Almost-sure global existence for every finite horizon | Proposition 3.1, Proposition 4.2, estimate (4.13), and Section 4.4 | Finite maximal lifetime is excluded by countable deterministic localization. |
| Pathwise uniqueness and paths continuous in H3 | Theorem 1.1 and the last paragraph of its proof | Both are global on every finite time interval. |
| Integral identity in H1 | Theorem 1.1 and the final paragraph in Section 4.4 | The proof obtains the identity in H2, which implies the requested H1 identity. |

The amplitude estimate is proved before amplitude localization. At each fixed integer amplitude level, a spatial exponent is chosen independently of the finite power used in the increment integral; a sufficiently large finite power gives a positive Holder exponent. The final countable exhaustion removes these auxiliary stopping levels without adding a hypothesis.

The manuscript uses the local theorem of Roeckner--Zhu--Zhu through an explicit realization on full L2, the periodic spatial kernel estimates of Constantin--Tarfulea--Vicol, and the continuous martingale estimate and iteration method of Hsu--Wang--Wang. Their roles and applicable formulas are stated and the remaining argument is given in the paper. It does not invoke a previously proved global nonlinear critical endpoint theorem.

This is a complete solution claim for the displayed original target, submitted for independent mathematical review. Catalogue classification and acceptance remain with the maintainers.
