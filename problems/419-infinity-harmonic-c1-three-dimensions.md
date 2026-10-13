# 419. Continuous gradients for three-dimensional infinity-harmonic functions

**Area:** Degenerate elliptic PDEs and supremal variational problems

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13
## Problem statement

Let $`\Omega\subset\mathbb R^3`$ be open and let $`u\in C(\Omega)`$ be a viscosity solution of

```math
-\Delta_\infty u=-\sum_{i,j=1}^3(\partial_i u)(\partial_j u)\partial_{ij}u=0.
```

Must $`u\in C^1_{\mathrm{loc}}(\Omega)`$? Here the viscosity convention tests the displayed operator against smooth functions touching $`u`$ from above or below. This asks for continuity of the gradient, beyond its known existence at every point; it imposes no nonvanishing-gradient hypothesis.

## Application

Infinity-harmonic functions describe absolutely minimizing extensions for maximum-gradient costs. Gradient regularity matters for optimal Lipschitz interpolation and continuum limits of tug-of-war models.

## References

1. L. C. Evans and C. K. Smart, [Everywhere differentiability of infinity harmonic functions](https://doi.org/10.1007/s00526-010-0388-1), *Calculus of Variations and PDE* **42** (2011), 289–299, introduction and main theorem.
2. O. Savin, [C1 regularity for infinity harmonic functions in two dimensions](https://www.math.columbia.edu/~savin/c12d.pdf), *Archive for Rational Mechanics and Analysis* **176** (2005), 351–361, Theorem 1 and introduction.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Uniform-Interior-C1alpha-Estimates-for-Infinity-Harmonic-Functions-October-4-2026/interior-c1-infinity-harmonic.pdf), result family 377 (2026). Statement locator: `build/manuscript/sections/01-introduction.tex, thm:main and cor:interior-c1`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** The theorem gives interior C1,alpha in every dimension d>=3 for continuous viscosity infinity-harmonic functions, including zero-gradient tests. The corollary explicitly localizes by bounded compact balls, so the target arbitrary continuous 3D solution has continuous gradient locally. Connectedness is handled componentwise.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-419) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** No corresponding complete Lean development was identified in the linked family record; no Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/419-infinity-harmonic-c1-three-dimensions.md).
