# 361. Can one-dimensional entropy-dissipating systems have two bounded solutions?

**Area:** Continuum mechanics; admissibility of shock dynamics

**Status:** 🔵 OPEN

**Last checked:** 2026-10-16

## Problem statement

Do there exist an integer $`N\ge2`$, an open convex state set $`U\subset\mathbb R^N`$, a smooth flux $`f:U\to\mathbb R^N`$ with $`Df(u)`$ having $`N`$ distinct real eigenvalues for every $`u\in U`$, and a smooth entropy pair $`(\eta,q)`$ satisfying

```math
D^2\eta(u)>0,\qquad Dq(u)=D\eta(u)Df(u),
```

together with $`T>0`$ and bounded measurable initial data $`u_0`$, for which two distinct bounded distributional solutions $`u,v:(0,T)\times\mathbb R\to K\Subset U`$ satisfy

```math
w_t+f(w)_x=0,\qquad \partial_t\eta(w)+\partial_xq(w)\le0\quad(w=u,v),
```

and both attain $`u_0`$ strongly in $`L^1_{\rm loc}`$ at $`t=0`$? Distinct means that they differ on a set of positive spacetime measure. The displayed entropy inequality must hold throughout spacetime, rather than only at jump discontinuities; no bounded-variation hypothesis is imposed.

## Application

An entropy inequality encodes the second law or energy dissipation in continuum models. This problem tests whether that physical criterion by itself can fail to select a unique one-dimensional evolution when arbitrarily fine oscillations are allowed.

## References

1. A. Bressan, [*One Dimensional Hyperbolic Conservation Laws: Past and Future*](https://arxiv.org/abs/2310.16707), Journal of Hyperbolic Differential Equations 21 (2024), 523–561, §8, Open Problem 6.
2. S. G. Krupa, [*Non-uniqueness and BV blowup for vacuously Liu-admissible solutions to $`p`$-system via computer-assisted proof*](https://doi.org/10.1007/s00021-026-01018-5), Journal of Mathematical Fluid Mechanics 28 (2026), article 37; [preprint](https://arxiv.org/abs/2403.07784), introduction and discussion of the convex-entropy obstruction.
3. A. Bressan and G. Guerra, [*Unique solutions to hyperbolic conservation laws with a strictly convex entropy*](https://arxiv.org/abs/2305.10737), Journal of Differential Equations (2024), Theorem 1.1, uniqueness in the small-BV semigroup domain.

## Status review

**Resolution-source report (2026-10-16):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-16-prior-resolutions.md#aim-361). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-22)

**Literature check:** Open in cited literature; no later resolution located.

Checked on 22 September 2026 using one-dimensional nonuniqueness with strictly convex entropy, $`p`$-system convex integration, and Bressan's Open Problem 6. Krupa's 2026 paper obtains nonuniqueness satisfying jump-based Liu admissibility, but explicitly states that its construction does not satisfy the required convex entropy condition. Multidimensional compressible Euler counterexamples use additional spatial dimensions. The small-BV uniqueness theorem does not apply to arbitrary bounded solutions. No matching one-dimensional entropy-admissible example was located.
