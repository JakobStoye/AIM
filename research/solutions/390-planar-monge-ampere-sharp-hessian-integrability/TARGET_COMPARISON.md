# Comparison with AIM Problem 390

Target: [Sharp weak integrability of planar Monge–Ampère Hessians](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/390-planar-monge-ampere-sharp-hessian-integrability.md), revision a153f469ee0ea64e876b2ad97c79d252c19a3e22.

The manuscript's Theorem 1.1 uses the same Alexandrov measure inequalities and proves local strong integrability at the target power. This implies the requested weak estimate for every positive threshold.

| Original requirement | Manuscript location | Relation |
|---|---|---|
| Every $`0<\lambda<1`$ | Theorem 1.1; Proposition 3.1; final proof | Same full range; a finite integer $`m>K+1`$ is available for each $`K=\lambda^{-1}>1`$ |
| Bounded convex planar domain | Theorem 1.1; Section 2 | Same PDE domain class; no boundary value or periodicity imposed |
| Convex Alexandrov solution with the bounds on every Borel set | Equation (1.1); Proposition 2.1 | Identical measure hypotheses; the density and coordinate identities are obtained in this class |
| Full distributional Hessian represented by a matrix field | Section 2, localized higher integrability; Proposition 2.1 | The whole weak Hessian is a field; no singular part is discarded |
| Every $`\Omega'\Subset\Omega`$ | Theorem 1.1; final proof | Finite cover of the compact image $`Y(\overline{\Omega'})`$ |
| Exact $`p_\lambda=(1+\lambda^2)/(1-\lambda^2)`$ | Theorem 1.1; Proposition 3.1; final proof | $`p_\lambda=1+2/(K^2-1)`$, exactly |
| Finite supremum over all positive thresholds | Equation (1.3); final proof | Follows from the strong integral by the pointwise power bound |
| Public imported results | Section 2; Lemma 3.1; bibliography | Baseline Sobolev regularity, planar strict convexity, Lipschitz area formula and normalized quasiconformal estimates are identified where used; the local projection and area transformation arguments are included |
| Allowed local constant dependence | Introduction; fixed disks in Section 3; final proof | Constants may depend on $`\lambda,u,\Omega'`$; rotation and scale uniformity are established only where used |

The supplementary local argument uses a weighted scalar Lipschitz projection and its residual-set energy estimate. It credits Agazzi et al.'s calibration/projection ideas and does not apply their periodic theorem to a local domain. The exact original-class area transformation is proved in Section 2.

The submitted material is a proposed complete analytic solution claim for mathematical review. Its existence and compilation do not establish AIM acceptance or independent human certification.
