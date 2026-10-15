# 141 — Finite-jet determination of small-time local controllability

**Area:** Nonlinear control / local system identification

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`n\ge3`$ and let $`X_0,\ldots,X_m`$ be real-analytic vector fields near $`0\in\mathbb R^n`$, with $`X_0(0)=0`$. Controls are measurable maps into $`[-1,1]^m`$, and trajectories satisfy

```math
\dot x=X_0(x)+\sum_{j=1}^m u_j(t)X_j(x).
```

Call the system small-time locally controllable at $`0`$ if, for every sufficiently small $`t>0`$, its points reachable from $`0`$ in time at most $`t`$ contain a neighborhood of $`0`$.

If this property holds, must there exist an integer $`N`$ such that every real-analytic tuple $`Y_0,\ldots,Y_m`$ with

```math
D^\alpha Y_j(0)=D^\alpha X_j(0)\quad
(0\le j\le m,\ |\alpha|\le N)
```

has the same controllability property with the same control set? Here $`\alpha`$ is a multi-index; $`N`$ may depend on the original system.

## Application

The conjecture asks whether finitely many locally measured Taylor coefficients can certify a nonlinear system's ability to move in every nearby direction in arbitrarily short time.

## References

1. S. Jafarpour, *On small-time local controllability* (2020), [SIAM Journal on Control and Optimization 58, 425–446; arXiv:1604.02432](https://arxiv.org/abs/1604.02432), Conjecture 1.1 and the polynomial-growth implication (Theorem 7.1 and Corollary 7.2 in the linked preprint). Exact conjecture and a sufficient condition.
2. K. Beauchard and F. Marbach, *A Unified Approach of Obstructions to Small-Time Local Controllability for Scalar-Input Systems* (2026), [Journal of Dynamical and Control Systems 32, Article 4](https://doi.org/10.1007/s10883-025-09752-1), introduction and §§6–9. Develops necessary conditions and resolves a different conjecture concerning particular Lie-bracket obstructions.

## Status review

Reviewed 15 October 2026 against the original target in [PR #141](https://github.com/MColbrook/AIM/pull/141). A fixed five-dimensional polynomial STLC system has no finite jet guaranteeing STLC with the same bounded controls.

[Proof or source](../research/solutions/141-finite-jet-control-counterexample/paper/main.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/141-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** Full negative answer; every finite N is covered by a positive drift monomial of degree 2k>N.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Known cases:** Finite-jet determination is established under a polynomial lower-growth condition on reachable neighborhoods.

**Remaining target:** Finite-jet determination for all the stated real-analytic controllable systems in dimensions at least three.

**Literature check:** Open in cited literature; no later resolution located.

Jafarpour records the conjecture as open for $`n\ge3`$, and proves it under a polynomial lower-growth condition on reachable neighborhoods. The planar case is established. Searches included “finite jet small-time local controllability conjecture solved 2026” and “Jafarpour finite differentiations controllability Beauchard Marbach”. The 2026 obstruction theorems do not establish finite-jet determination for all analytic systems.
