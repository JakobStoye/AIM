# Comparison with AIM 431

Target: [431. Analytic boundary diffusion on continuous functions for Lipschitz domains](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/431-dtn-analyticity-continuous-boundary.md), revision `c9929805cece044705abaaebe1cebddac1ba11a6`.

The locations below refer to the manuscript in this package. This is a full solution claim, subject to independent mathematical review.

| Original requirement | Result and manuscript location | Coverage |
| --- | --- | --- |
| Every bounded connected Lipschitz domain in R^d, d >= 2 | Section 1 hypotheses and Theorem 1.1 | Same full geometry and dimension range; boundary components may be disconnected |
| Real symmetric uniformly positive definite C with Lipschitz entries on the closure | Equation (1), Section 1; coefficient freezing in Proposition 3.3 | Same coefficient class; no smooth boundary assumption |
| Weak Dirichlet-to-Neumann operator for -div(C grad), harmonic extension and outward conormal derivative | Equation (2), definition of N_c in Section 1 | Same canonical operator and sign, with Hausdorff surface measure |
| C(boundary Omega) with the supremum norm, and the given real-time C0 semigroup | Section 1 and Lemma 3.2 | Same Banach space and semigroup; no replacement of the boundary measure |
| Some nonzero holomorphic sector | Theorem 1.1; complete contour proof in Section 4 | Stronger angle pi/2 |
| Uniform norm bounds for 0 < abs(z) <= 1 in each strictly smaller sector | Equation (3), proved in Section 4 | Stronger bound for all nonzero z in each smaller sector |
| Quantifiers over every admissible domain/coefficient pair; finite constants for each pair | Theorem 1.1 and Proposition 3.3 | Constants may depend on the fixed pair and sector; no universal class-wide bound claimed |

## Public dependencies and their roles

- **Arendt--ter Elst (2020), arXiv:1707.05556:** Corollary 3.5 supplies the continuous kernel; Proposition 5.1(b) supplies contractivity; Theorem 5.3(a) supplies the C0 realization. Potential V=0 and the real symmetric Lipschitz hypotheses match the manuscript. Lemma 3.2 uses these facts, but does not infer supremum norm holomorphy from L2 holomorphy.
- **Auscher--Axelsson--McIntosh (2010), doi:10.1007/s11512-009-0108-2:** Theorem 2.2(i) and Corollary 2.4 give vertical L2 Dirichlet control for real symmetric uniformly elliptic matrices independent of the normal variable. Theorem 5.3 identifies their solution with the variational energy solution for smooth data; the manuscript's Lemma 2.1 proves the H1/2 approximation and maximum-principle bridges. The path (1-s)I+sA remains in the well-posed class.
- **Trudinger (1973), Theorem 5.1 and Corollaries 5.4--5.5:** Interior L2-to-supremum and forced Hölder estimates in the real uniformly elliptic specialization. Lemmas 2.2, 2.3 and 3.1 apply these estimates to reflected equations.
- **Nittka, arXiv:0906.5285v1 (2009), Section 3.1 and Lemma 3.3 (journal publication 2011):** Sobolev reflection and chain rule for Lipschitz graphs, used in Lemma 3.1 and Proposition 3.3.
- **Evans--Gariepy (2015), Section 3.3.4:** Lipschitz graph area formula. Proposition 3.3 retains the separate weak-star density limit, and does not identify it with the area density of the limiting graph.
- **Rudin, Real and Complex Analysis (1987), Chapter 9; Functional Analysis (1991), Theorems 3.27, 3.29 and 3.31:** Fourier energy calculation and norm-valued contour integration. The resolvent estimates, residue sign, identification with the real-time semigroup, and strong continuity are proved in the manuscript.

The background sources ter Elst--Ouhabaz (2019) and their 2025 open-problem note identify the smooth-boundary result and the stated Lipschitz-boundary question. They are not used as a proof of the new conclusion. The manuscript makes no pointwise Poisson-kernel claim and does not address the separate complex-coefficient question.
