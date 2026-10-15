# 380. Extinction at the critical Dirichlet eigenvalue for strong-KPP reactions

**Area:** Reaction–diffusion; critical habitat thresholds

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`\Omega\subset\mathbb R^d`$, $`d\ge2`$, be a connected unbounded uniformly $`C^{2,\gamma}`$ domain, and define

```math
\lambda_1(\Omega)=\inf_{0\ne\phi\in C_c^\infty(\Omega)}\frac{\int_\Omega|\nabla\phi|^2}{\int_\Omega\phi^2}.
```

Let $`f\in C^{1,\gamma}([0,\infty))`$ satisfy $`f(0)=f(1)=0`$, $`f'(0)>0`$, $`f>0`$ on $`(0,1)`$, $`f<0`$ on $`(1,\infty)`$, and strict decrease of $`f(s)/s`$ on $`(0,1]`$. If $`\lambda_1(\Omega)=f'(0)`$, must the Dirichlet problem

```math
-\Delta u=f(u)\quad\hbox{in }\Omega,\qquad u=0\quad\hbox{on }\partial\Omega
```

have no bounded positive classical solution? Uniform boundary regularity means common-radius boundary graph charts with uniformly bounded $`C^{2,\gamma}`$ norms. The domain need not be periodic or geometrically convergent at infinity.

## Application

The equality balances low-density reproduction with diffusive loss exactly. Its resolution would determine whether an irregular infinite habitat can sustain a population precisely at this threshold.

## References

1. H. Berestycki and C. Graham, [*The steady states of strong-KPP reactions in general domains*](https://arxiv.org/abs/2212.06611), Journal of the European Mathematical Society, published online (2025), §1, Conjecture 1.7, Theorem 1.5 and Proposition 1.6; DOI [10.4171/JEMS/1578](https://doi.org/10.4171/JEMS/1578).
2. H. Berestycki and C. Graham, [*A Stable-Compact Method for Qualitative Properties of Semilinear Elliptic Equations*](https://doi.org/10.1007/s00205-026-02168-6), Archive for Rational Mechanics and Analysis 250 (2026), article 21, §7, comparison and uniqueness theory, and §8.1.

## Status review

Reviewed 15 October 2026 against the original target in [PR #151](https://github.com/MColbrook/AIM/pull/151). Critical Dirichlet spectral equality can coexist with a bounded positive strong-KPP equilibrium on a uniformly smooth unbounded domain.

[Proof or source](../research/solutions/380-critical-kpp-counterexample/paper/main.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/380-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** Critical Dirichlet spectral equality can coexist with a bounded positive strong-KPP equilibrium on a uniformly smooth unbounded domain.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

Checked on 22 September 2026 using the critical-eigenvalue nonexistence conjecture and strong-KPP steady states. The JEMS paper proves the threshold statement for bounded and periodic domains, and explicitly leaves the general critical case open. Its weak-KPP critical examples use reactions linear near zero and do not satisfy the strict quotient condition here. The 2026 uniqueness theorems do not establish critical nonexistence on arbitrary unbounded domains. This is an existence threshold, distinct from uniqueness when a positive equilibrium exists. No general proof or strong-KPP counterexample was located.
