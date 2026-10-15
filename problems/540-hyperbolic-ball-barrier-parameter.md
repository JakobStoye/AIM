# 540. Sharp barrier-parameter growth for hyperbolic balls

**Area:** Numerical optimization on manifolds

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`\mathbb H^2`$ have constant curvature $`-1`$, fix $`o\in\mathbb H^2`$, and put $`D_R=\{x:d(o,x)<R\}`$. Use the Levi-Civita connection to define covariant derivatives. A $`\theta`$-barrier on $`D_R`$ is a function $`F\in C^3(D_R)`$ whose Hessian $`H_x=(\nabla^2F)_x`$ is positive definite, whose epigraph is closed in $`\mathbb H^2\times\mathbb R`$, and which satisfies, for every $`x\in D_R`$ and $`u,v,w\in T_x\mathbb H^2`$,

```math
| (\nabla^3F)_x(u,v,w)|\le 2\sqrt{H_x(u,u)H_x(v,v)H_x(w,w)},\qquad |dF_x(v)|^2\le\theta H_x(v,v).
```

The first inequality is required for arbitrary triples, not just three equal vectors. Closedness imposes divergence of $`F`$ at the boundary of the ball.

Define

```math
\theta_*(R)=\inf\{\theta\ge0:\text{a $\theta$-barrier on $D_R$ exists}\}.
```

Determine the asymptotic order of $`\theta_*(R)`$ as $`R\to\infty`$, up to multiplicative constants independent of $`R`$. In particular, is $`\theta_*(R)=O(\sqrt R)`$? The barrier may depend on $`R`$, and no rotational symmetry or evaluation algorithm is assumed.

## Application

The barrier parameter controls iteration bounds for interior-point methods on curved spaces. Its optimal dependence on the domain radius quantifies a geometric limitation of these methods, including their use in geometric estimation and optimization on manifolds.

## References

1. C. Criscitiello, H. Nieuwboer and M. Walter, [Negative curvature obstructs the existence of good barriers for interior-point methods](https://arxiv.org/abs/2604.07319v1), preprint (2026), Corollary 1.4 and the following open question; §2.3 fixes the barrier definition.
2. H. Hirai, H. Nieuwboer and M. Walter, [Interior-Point Methods on Manifolds: Theory and Applications](https://doi.org/10.1007/s10208-026-09756-8), Foundations of Computational Mathematics (2026), Definition 4.1 and Theorem 1.6; §1.6 describes geometric estimation applications.

## Status review

Reviewed 15 October 2026 against the original target in [PR #119](https://github.com/MColbrook/AIM/pull/119). The infimum of full-tensor barrier parameters has quadratic growth in the hyperbolic radius, without any symmetry assumption.

[Proof or source](../research/solutions/540-hyperbolic-ball-barrier-parameter/paper/hyperbolic_ball_barriers.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/540-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** The infimum of full-tensor barrier parameters has quadratic growth in the hyperbolic radius, without any symmetry assumption.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

The known bounds leave the gap

```math
\frac{\sqrt R}{128}-\frac14\le\theta_*(R)\le C(1+R^2)
```

for a universal constant $`C`$. The lower bound in [1] even holds for the weaker notion of self-concordance along geodesics; the construction in [2] gives the upper bound for the full definition used here. Neither bound determines the sharp order.

The current version of [1] explicitly retains this gap. No matching solution announcement was found in the literature, author-page, GitHub, Zenodo-indexed and Palomar checks on the date above. Native Zenodo access returned HTTP 403.
