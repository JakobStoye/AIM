# 401. Continuity of manifold transport under MTW and convex injectivity domains

**Area:** Monge–Ampère PDEs / transport on manifolds

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`(M,g)`$ be a compact connected smooth Riemannian manifold without boundary, of dimension $`n\ge3`$, and $`c(x,y)=d_g(x,y)^2/2`$. For each $`x`$ let $`I_x\subset T_xM`$ be the open set of vectors along which $`\exp_x`$ is minimizing beyond time one. Assume $`I_x`$ is convex, and assume the weak MTW condition

```math
-\frac32\left.\partial_s^2\partial_t^2 c(\exp_x(t\xi),\exp_x(v+s\eta))\right|_{s=t=0}\ge0\quad(v\in I_x,\ \xi\perp\eta).
```

For every pair of probability densities $`f,g_1`$ with respect to Riemannian volume satisfying $`0<a\le f,g_1\le b<\infty`$ almost everywhere, must the unique almost-everywhere optimal map transporting $`f`$ to $`g_1`$ for cost $`c`$ have a continuous representative on $`M`$?

## Application

Continuity prevents arbitrarily close source locations from being assigned distant destinations. The problem identifies whether known geometric necessities suffice for stable mass redistribution on curved spaces.

## References

1. G. De Philippis and A. Figalli, *The Monge–Ampère equation and its link to optimal transportation*, Bulletin of the American Mathematical Society 51 (2014), 527–580, §5.2, open problem (7). [Author manuscript](https://arxiv.org/abs/1310.6167).
2. A. Figalli, L. Rifford and C. Villani, *Necessary and sufficient conditions for continuity of optimal transport maps on Riemannian manifolds*, Tohoku Mathematical Journal 63 (2011), 855–876, introduction and continuity criteria. [Journal full text](https://www.jstage.jst.go.jp/article/tmj/63/4/63_855/_pdf/-char/ja).

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Uniform-Bi-Holder-Transport-from-Weak-MTW-September-25-2026/paper.pdf), result family 360 (2026). Statement locator: `build/sections/introduction.tex, thm:main`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** Same squared-distance cost and weak MTW formula. The theorem gives an almost-everywhere unique optimal map with a global bi-Holder homeomorphic representative for measurable probability densities between fixed positive finite bounds on compact connected smooth manifolds. It does not require convex injectivity domains in advance, so covers the target assumptions.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-401) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/360.md). docs/360 covers full bi-Holder transport via BiholderTransport. Supporting finite-family geometric statements have narrower scope. No local kernel log inspected. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/401-mtw-convex-domains-transport-continuity.md).
