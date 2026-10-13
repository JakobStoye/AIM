# 210. Sharp local smoothing for the three-dimensional wave equation

**Area:** Wave propagation; dispersive estimates

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

For a Schwartz function $`f`$ on $`\mathbb R^3`$, let

```math
u(t,x)=e^{it\sqrt{-\Delta}}f(x),\qquad \widehat u(t,\xi)=e^{it|\xi|}\widehat f(\xi).
```

For every $`3\le p<\infty`$ and $`\varepsilon>0`$, is there a constant $`C_{p,\varepsilon}`$ such that, for every $`\lambda\ge1`$ and every $`f`$ with Fourier support in $`\{\lambda\le|\xi|\le2\lambda\}`$,

```math
\left(\int_1^2\int_{\mathbb R^3}|u(t,x)|^p\,dx\,dt\right)^{1/p}\le C_{p,\varepsilon}\lambda^{1-3/p+\varepsilon}\|f\|_{L^p(\mathbb R^3)}?
```

## Application

This measures the additional regularity gained by averaging a propagating wave over time. It constrains persistent wave focusing and supports estimates for nonlinear wave equations with rough initial data.

## References

1. David Beltran, Jonathan Hickman, and Christopher D. Sogge, [Sharp local smoothing estimates for Fourier integral operators](https://arxiv.org/abs/1812.11616), survey (2019). Section 2.3, Conjecture 2.4, gives the Euclidean half-wave conjecture and distinguishes it from manifold and general Fourier-integral-operator versions.
2. Tainara Borges, Benjamin Foster, Yumeng Ou, and Eyvindur Palsson, [Nonempty interior of pinned distance and tree sets](https://doi.org/10.1016/j.aim.2026.110917), *Adv. Math.* (2026). Section 2.3, Conjecture 12, and the discussion following Theorem 3 retain the open three-dimensional threshold.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Critical-local-smoothing-for-the-three-dimensional-wave-equation-September-24-2026/paper.pdf), result family 079 (2026). Statement locator: `Theorem thm:main; Corollary cor:full-range, eq:phys-full-range and its annular interpolation proof`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** The half-wave and time interval [1,2] agree. The critical p=3 estimate permits every positive Sobolev loss; the read corollary/interpolation proof covers all p>2. For AIM p>=3 choose alpha=1-3/p+epsilon and localize to lambda<=|xi|<=2lambda; the annular multiplier bound gives lambda^alpha times the Lp input norm, uniformly in lambda>=1.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-210) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** No corresponding complete Lean development was identified in the linked family record; no Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/210-euclidean-wave-local-smoothing.md).
