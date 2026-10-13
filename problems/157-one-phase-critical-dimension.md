# 157. The first dimension with a singular one-phase minimizing cone

**Area:** Free boundaries and fluid interfaces

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

For $`d\ge2`$ and a ball $`B\subset\mathbb R^d`$, define

```math
J_B(u)=\int_B\left(|\nabla u|^2+\mathbf1_{\{u>0\}}\right)\,dx.
```

Let $`d_*`$ be the least $`d`$ for which there is a nonnegative, nonzero $`u\in H^1_{\mathrm{loc}}(\mathbb R^d)\cap C(\mathbb R^d)`$, homogeneous of degree one, with $`0\in\partial\{u>0\}`$, minimizing $`J_B`$ in every ball among nonnegative competitors $`v`$ with $`v-u\in H^1_0(B)`$, and not of the form $`(x\cdot e)_+`$ for a unit vector $`e`$. Determine $`d_*`$. The unresolved alternatives are $`5,6,7`$.

## Application

No direct application is identified in this entry. The question identifies the first dimension admitting a singular minimizing cone in the one-phase Bernoulli problem, refining its mathematical regularity theory. The unresolved dimensions are higher than those of ordinary physical space.

## References

1. David Jerison and Ovidiu Savin, *Some remarks on stability of cones for the one-phase free boundary problem*, Geometric and Functional Analysis 25 (2015), 1240–1257. [Article](https://doi.org/10.1007/s00039-015-0335-6). Low-dimensional flatness theorem.

2. Daniela De Silva and David Jerison, *A singular energy minimizing free boundary*, Journal für die reine und angewandte Mathematik 635 (2009), 1–21. [Article](https://doi.org/10.1515/CRELLE.2009.074). Seven-dimensional minimizing cone.

3. Benjy Firester, Raphael Tsiamis and Yipeng Wang, *Stability inequalities for one-phase cones* (2026), introduction and Theorem 1.1. [Paper](https://arxiv.org/abs/2601.16966). Explicitly records $`5\le d_*\le7`$ and proves new results under bi-orthogonal symmetry.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-critical-dimension-for-one-phase-Bernoulli-minimizers-September-24-2026/The-critical-dimension-for-one-phase-Bernoulli-minimizers-September-24-2026.pdf), result family 367 (2026). Statement locator: `build/paper.tex, thm:main`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** Exactly J=integral(|grad u|^2+indicator(u>0)), one-homogeneous nonnegative global minimizers with arbitrary nonnegative Sobolev same-trace competitors. Every cone through dimension six is flat and a nonflat cone exists in dimension seven, so the target critical dimension is seven. Standard minimizer regularity supplies continuity for the existence example.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-157) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/367.md). docs/367 covers only existence of a nonflat cone in dimension seven via BernoulliNonflatInSeven; flatness in dimensions at most six is outside it, so it does not determine the full critical dimension. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/157-one-phase-critical-dimension.md).
