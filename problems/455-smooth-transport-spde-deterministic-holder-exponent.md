# 455. A deterministic Hölder exponent for smooth-transport parabolic SPDEs

**Area:** Stochastic parabolic PDEs; quantitative regularity

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

On $`\mathbb T^d`$, $`d\ge2`$, consider the scalar Itô equation

```math
du=\nabla\cdot(a\nabla u)\,dt+\sum_{k\ge1}(b_k\cdot\nabla u)\,dW^k_t,\qquad u(0)=u_0,
```

where the Brownian motions are independent, $`u_0\in C^\infty(\mathbb T^d)`$ is deterministic, and the coefficients are progressively measurable in $`(t,\omega)`$ and measurable in $`x`$. Assume fixed deterministic bounds

```math
|a|+\Big(\sum_k|b_k|^2\Big)^{1/2}\le M,\qquad
\eta^\top\Big(a-\tfrac12\sum_kb_k\otimes b_k\Big)\eta\ge\nu|\eta|^2\quad(\eta\in\mathbb R^d),
```

with $`M<\infty`$ and $`\nu>0`$. Use the variational solution in $`C([0,T];L^2)\cap L^2(0,T;H^1)`$, defined by testing against smooth spatial functions and integrating the stochastic terms in the Itô sense.

Now assume that $`b=(b_k)_k`$ is smooth in $`x`$ and, for every integer $`j\ge1`$, obeys a deterministic uniform bound $`\sup_{t,\omega}\|b(t,\omega,\cdot)\|_{C^j(\mathbb T^d;\ell^2(\mathbb R^d))}\le M_j`$. The diffusion matrix $`a`$ remains merely bounded and measurable. For every $`0<\tau<T`$, is there a deterministic $`\gamma>0`$, depending only on $`d,\nu,M,(M_j),\tau,T`$, such that

```math
\mathbb P\bigl(u\in C^{\gamma/2,\gamma}([\tau,T]\times\mathbb T^d)\bigr)=1?
```

The Hölder norm itself may be random and unbounded. The question is whether the exponent can be chosen independently of the sample; no commuting-flow or spatially constant-noise assumption is allowed.

## Application

For diffusion subject to random transport, a deterministic Hölder exponent would give a common regularity scale across realizations: spatial exponent $`\gamma`$ and temporal exponent $`\gamma/2`$. The corresponding Hölder norm may still depend on the realization and be unbounded.

## References

1. A. Agresti, M. Sauerbrey and M. Veraar, *A stochastic flow approach to De Giorgi–Nash–Moser estimates for SPDEs with smooth transport noise* (2025 preprint, manuscript dated August 2026), Theorem 1.1, §1.2 and §4. [Full manuscript](https://arxiv.org/html/2511.12692v1).

## Status review

Reviewed 15 October 2026 against the original target in [PR #166](https://github.com/MColbrook/AIM/pull/166). The entire smooth-transport variational SPDE class has a deterministic positive parabolic Hölder exponent on each positive-time strip.

[Proof or source](../research/solutions/455-smooth-transport-spde-deterministic-holder-exponent/manuscript.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/455-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** The entire smooth-transport variational SPDE class has a deterministic positive parabolic Hölder exponent on each positive-time strip.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

This is the second open question of §1.2. Theorem 1.1 gives positive sample-dependent exponents; Proposition 4.3 obtains deterministic ones only with extra structure. The example of an unbounded ellipticity ratio after the stochastic-flow transformation is an obstruction to that method, not a counterexample to the assertion. Searches on 2026-09-22 for uniform stochastic Hölder exponents and later De Giorgi–Nash–Moser results found no theorem for the full stated class. This keeps the smooth-noise hypothesis, unlike the separate rough-noise regularity problem.
