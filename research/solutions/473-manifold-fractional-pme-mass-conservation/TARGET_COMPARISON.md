# Target comparison for AIM 473

Target: [473. Mass conservation for fractional porous-medium flow on noncompact manifolds](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/473-manifold-fractional-pme-mass-conservation.md), revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

Submitted argument: [manuscript](paper/mass_conservation.pdf), Theorem 2.2. The table is based on the manuscript and the public target.

| Original requirement | Manuscript location | Scope |
|---|---|---|
| Every complete connected noncompact Riemannian manifold of dimension at least two | Section 2, geometric assumptions (2), and Theorem 2.2 | Same class; no model-space or symmetry restriction |
| Ricci curvature bounded below for any nonnegative comparison constant | Assumptions (2); cutoff specialization in Lemma 2.3 | Includes zero comparison constant |
| Uniform Faber–Krahn inequality on relatively compact smooth domains | Opening of Section 2 | The variational argument proves the all-open version needed by the cited linear estimates, with the original constant and dimension |
| Every porous-medium exponent greater than one and fractional order strictly between zero and one | Definition 2.1 and Theorem 2.2; interpolation in Proposition 4.1 | Entire stated ranges |
| Spectral fractional Laplace–Beltrami operator and the normalized Green kernel | Section 2, (4), normalization paragraph and Lemma 2.3 | Exact spectral realization and Gamma normalization |
| Every nonnegative integrable initial datum | Theorem 2.2; finite regularized energy in Proposition 4.1 | No boundedness or finite initial energy premise |
| Weighted continuity at every basepoint and every finite horizon | Definition 2.1; potential estimate (6) and Proposition 3.2 | Same continuity topology |
| Local time-space integrability of the nonlinear power, compact smooth dual tests and the prescribed initial trace | Definition 2.1 and (5); endpoint integration in Proposition 3.2 | No constant or nonlinear weak test is inserted |
| Every such WDS with spatial L1 membership at each finite time | Theorem 2.2 and Proposition 3.2 | A uniform mass upper bound and power integrability are derived for the given solution |
| Conservation at every finite positive time | Final proof of Theorem 2.2; all-endpoint identity (13) | Equality at every finite time, with the initial mass recovered by strong L1 continuity |

No minimality, nonlinear semigroup construction, energy-solution property or uniqueness identification is imposed on the given solution. The paper does not prove uniqueness in the larger weighted class.

The additional argument establishes the needed global nonlinear integrability for the arbitrary WDS. It is not a restatement of the constructed-solution smoothing theorem.

| Public source | Exact input used | Manuscript treatment |
|---|---|---|
| Berchio–Bonforte–Grillo–Muratori, arXiv:2109.10732v2; final Math. Ann. 389 (2024), 3603–3651 | Gaussian bound (2.3), Remark 2.1 and Lemma 5.2; linear subordination discussion in the proof of Proposition 5.1 | Section 2 states the bounds, reconciles the printed Green normalization, and proves the exact spectral potential representation |
| von Criegern–Grillo–Monticelli, arXiv:2609.12954v1 (2026), Corollary 8.6 | Conservation for WDSs constructed by monotone approximation on nonnegative-Ricci manifolds with a finite fractional Green kernel | Credited in the Introduction as a related prior result; no construction assumption is transferred to the present arbitrary WDS |
| Bianchi–Setti, arXiv:1607.06008v1, Corollary 2.3 | Ordinary Laplacian cutoffs under the Ricci lower bound | Lemma 2.3 uses their curvature exponent zero to prove heat conservativeness |
| Sard, Bull. Amer. Math. Soc. 48 (1942), Theorem 7.2 | Smooth scalar maps admit regular values | Section 2 constructs intermediate smooth domains for the variational FK argument |
| Teschl, Mathematical Methods in Quantum Mechanics, 2009 edition, Section 3.1 | Spectral functional calculus | Lemma 2.3 checks the normalized Green/semigroup representation |

The contribution is analytic. No numerical, computer-assisted or formal-proof certificate is asserted. The package is submitted for independent review; catalogue classification is left to the maintainers.
