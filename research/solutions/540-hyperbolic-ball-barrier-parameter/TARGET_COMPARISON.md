# Correspondence with AIM 540

Original problem: [Sharp barrier-parameter growth for hyperbolic balls](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/540-hyperbolic-ball-barrier-parameter.md), revision a153f469ee0ea64e876b2ad97c79d252c19a3e22.

Submitted manuscript: *Quadratic barrier parameters for hyperbolic balls*, by Kaiwen Jin.

| Original requirement | Manuscript result and location | Scope |
| --- | --- | --- |
| Hyperbolic plane with curvature -1, arbitrary fixed center, entire open ball D_R | Section 1, p.1; polar geometry in Section 2 | Same domain and normalization. |
| C3 functions with positive definite Levi-Civita Hessian | Definition in Section 1, p.1; Lemma 2.1 and Proposition 2.2 | Every barrier in the original regularity class. |
| Epigraph closed in the ambient hyperbolic plane times the real line | Section 1 definition; Proposition 3.1 proof, p.4 | The upper construction has positive Hessian and ambient closed epigraph. The lower proof holds even without the closedness condition. |
| Third covariant derivative inequality for all points and arbitrary u,v,w, with coefficient 2 | Equation (1), p.1; Lemma 2.1, p.2; full-definition source specialization and polarization in Proposition 3.1, p.4 | No diagonal-only or symmetrized third-derivative substitution. |
| Squared differential bounded by theta times the Hessian for every vector | Equation (2), p.1; all-ray comparison in Proposition 2.2, pp.3-4; upper construction in Proposition 3.1 | Exact theta normalization and full vector scope. |
| Infimum over all admissible barriers, without rotational symmetry | Section 1 definition and Theorem 1.1; Proposition 2.2, pp.3-4, and final proof, p.5 | Lower bound applies to all F; no radial reduction, averaging, or minimizer attainment is required. |
| F may depend on R; no evaluation algorithm is assumed | Uniform lower argument in Proposition 2.2; explicit F_R in Proposition 3.1 | Same quantifiers; analytic result. |
| Determine the asymptotic order up to constants independent of R | Theorem 1.1, p.2, and its proof, p.5 | For R>=2, R^2/1024 <= theta_*(R) <= (9/4)R^2. |
| Decide whether theta_*(R)=O(sqrt R) | Theorem 1.1, p.2 | No, for the full definition in the original problem. |
| Applicable public imported theorem | Hirai, Nieuwboer, Walter, Theorem 5.16(i) and Theorem 1.6, cited in Proposition 3.1 | Known full-definition upper construction, specialized to a totally geodesic slice. |

The claim covers the complete original asymptotic target. The estimates do not settle the distinct optimization problem obtained by imposing self-concordance only on three equal tangent vectors. No whole-target formalization or human review is asserted by this package.
