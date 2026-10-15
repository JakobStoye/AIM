# Comparison with Problem 252

Target: [Rigidity of a totally integrable Minkowski billiard in its own unit ball](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/252-self-ball-minkowski-integrability.md), repository revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

Submitted claim: Theorem 1.1 in [the manuscript](paper/minkowski_integrability.pdf). It proves the entire stated implication for the original smooth strongly convex class.

| Original requirement | Manuscript location and agreement |
|---|---|
| Every norm on the real plane, smooth off zero with positive-definite Hessian of its square | Section 1 defines exactly this class; Theorem 1.1 quantifies over every such norm. Section 2 uses its strong convexity for positive curvature, twist and a nondegenerate support maximum. |
| Table is the norm's own unit ball | Section 1 sets K={N<=1}; Section 2 sets P=-J K*, so the propagation norm and table are linked exactly as in the problem. |
| Boundary parametrized by N-arclength and chord generating function N(gamma(t)-gamma(s)) | Both definitions and the Euler--Lagrange equation appear in Section 1. Section 2.1 explains why smooth boundary reparametrization preserves the finite stationary Hessian. |
| Entire phase annulus | Total integrability is defined for the entire ordered-distinct-point annulus. Section 2.2 covers every original orbit and both alternating phase components; Section 2.3 averages the whole union. |
| Continuous invariant simple curves winding once | Section 1 uses precisely this C0 hypothesis. Section 2.1 imports the continuous-invariant-curve local maximum property; no differentiability of leaves is assumed. |
| Positive-definite symmetric Q with N(v)=sqrt(v^T Qv) for all v | Theorem 1.1 states this conclusion. Its final proof forces equality in the polar area-product bound, obtains a centered ellipse, and identifies its gauge, including at zero. |
| No extra symmetry or self-polarity assumption | Only central symmetry supplied by the norm is used. Section 2.3 uses antipodes; Section 2.2 permits the position and momentum curves to be different. |

The main supporting steps are Lemma 2.1 (support maximum), Sections 2.1--2.3 (negative finite variations, complete half maps, invariant measure and averaging), Lemma 3.1 (boundary parameter and polar area product), and Lemma 3.2 (energy determinant bound). These steps are proved in the public manuscript.

External inputs are identified where used: Bialy's general positive-mixed-derivative twist statement for continuous essential invariant curves, Bianchi--Kelly's symmetric Blaschke--Santalo inequality and equality case, and ordinary planar isoperimetry as presented by Osserman. The prior finite-linear-symmetry theorem and neighboring single symplectic-table rigidity theorem are credited as context; neither is asserted to cover the full target directly.

The paper makes a complete analytic solution claim. It asserts neither upstream acceptance nor a formal verification result. Integrability only near the boundary of phase space is outside the theorem.
