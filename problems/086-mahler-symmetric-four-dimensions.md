# 086. The symmetric Mahler inequality in four dimensions

**Area:** Convex geometry and optimization

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

For every compact convex body $`K\subset\mathbb R^4`$ with nonempty interior and $`K=-K`$, define its polar

```math
K^\circ=\{y\in\mathbb R^4:\langle x,y\rangle\le1
\text{ for all }x\in K\}.
```

Is

```math
\mathop{\mathrm{vol}}\nolimits_4(K)\mathop{\mathrm{vol}}\nolimits_4(K^\circ)
\ge\frac{4^4}{4!}?
```

The conjectured bound is attained by the cube and its polar cross-polytope. No polytope, unconditional-symmetry, or smoothness restriction may be placed on $`K`$. Only the inequality, not a complete equality classification, is requested.

## Application

Polarity exchanges primal and dual norm constraints. A sharp volume-product inequality quantifies how small their uncertainty or feasible regions can simultaneously be.

## References

- [Hiroshi Iriyeh and Masataka Shibata, *Symmetric Mahler's conjecture for the volume product in the 3-dimensional case* (Duke Mathematical Journal, 2020)](https://arxiv.org/abs/1706.01749).
- [Shibing Chen, Yuanyuan Li, Dongmeng Xi and Zhe-Feng Xu, *The Mahler Conjecture in Three Dimensions* (2026), introduction and three-dimensional results](https://arxiv.org/abs/2605.09334).

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-symmetric-Mahler-conjecture-and-its-equality-cases-September-22-2026/paper.pdf), result family 087 (2026). Statement locator: `Theorem thm:main; equation eq:main-inequality`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** Set n=4 in the unrestricted origin-symmetric convex-body inequality |K||Kpolar|>=4^n/n!. Compactness, nonempty interior, ordinary Euclidean polar and volume are exactly AIM hypotheses. Equality classification is extra, not needed.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-086) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/087.md). Actual endpoint symmetric_mahler has no external hypothesis beyond compactness/convexity/symmetry/nonempty interior. Set n=4. No successful local replay/axiom audit. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/086-mahler-symmetric-four-dimensions.md).
