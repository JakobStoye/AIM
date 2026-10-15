# 384. Uniqueness of positive reaction–diffusion equilibria outside two obstacles

**Area:** Reaction–diffusion; populations in perforated habitats

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

For any $`d\ge2`$, radii $`r_a,r_b>0`$ and centers $`a,b\in\mathbb R^d`$ with $`|a-b|>r_a+r_b`$, put

```math
\Omega=\mathbb R^d\setminus\bigl(\overline{B_{r_a}(a)}\cup\overline{B_{r_b}(b)}\bigr).
```

Let $`f\in C^{1,\gamma}([0,\infty))`$, $`0<\gamma<1`$, satisfy $`f(0)=f(1)=0`$, $`f'(0)>0`$, $`f'(1)<0`$, $`f>0`$ on $`(0,1)`$ and $`f<0`$ on $`(1,\infty)`$. Must

```math
-\Delta u=f(u)\quad\hbox{in }\Omega,\qquad u=0\quad\hbox{on }\partial\Omega
```

have exactly one bounded positive solution $`u\in C^2(\Omega)\cap C(\overline\Omega)`$? The per-capita growth rate $`f(s)/s`$ is allowed to increase, so the problem includes positive reactions outside the strong-KPP class. The obstacle separation is arbitrary subject to disjointness.

## Application

Two absorbing obstacles form a simple habitat in which their diffusion boundary layers can interact. The question asks whether this interaction alone can produce multiple positive equilibrium populations for a monostable growth law.

## References

1. H. Berestycki and C. Graham, [*A Stable-Compact Method for Qualitative Properties of Semilinear Elliptic Equations*](https://doi.org/10.1007/s00205-026-02168-6), Archive for Rational Mechanics and Analysis 250 (2026), article 21, §8.5, Open Question 7(ii), and Theorem 1.1.
2. H. Berestycki and C. Graham, [*The steady states of strong-KPP reactions in general domains*](https://arxiv.org/abs/2212.06611), Journal of the European Mathematical Society, published online (2025), §1, comparison with uniqueness under the stronger reaction hypothesis; DOI [10.4171/JEMS/1578](https://doi.org/10.4171/JEMS/1578).

## Status review

Reviewed 15 October 2026 against the original target in [PR #152](https://github.com/MColbrook/AIM/pull/152). Two disjoint disks admit two distinct bounded positive monostable Dirichlet equilibria for one admissible reaction.

[Proof or source](../research/solutions/384-two-disk-monostable-counterexample/paper/main.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/384-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** Two disjoint disks admit two distinct bounded positive monostable Dirichlet equilibria for one admissible reaction.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

Checked on 22 September 2026 using the two-obstacle semilinear elliptic problem and later reaction–diffusion uniqueness results. The March 2026 primary paper asks this exact question. It proves uniqueness outside a single ball and explains why sufficiently separated balls are also covered. Its argument does not cover nearby disjoint obstacles. The general strong-KPP question imposes a decreasing growth quotient; the present problem instead fixes a simple geometry and permits a broader reaction class. No later result resolving arbitrary separation or giving a counterexample was located.
