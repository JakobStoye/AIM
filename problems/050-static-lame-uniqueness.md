# 050 — Recover both Lamé moduli from static boundary measurements

**Area:** Inverse elasticity / nondestructive testing

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`\Omega\subset\mathbb R^3`$ be a bounded connected smooth domain. For smooth coefficients $`\lambda,\mu`$ satisfying $`\mu>0`$ and $`3\lambda+2\mu>0`$ on $`\overline\Omega`$, set

```math
\varepsilon(u)=\tfrac12(\nabla u+\nabla u^T),\qquad
\sigma_{\lambda,\mu}(u)=\lambda(\nabla\cdot u)I+2\mu\varepsilon(u).
```

For each boundary displacement $`f\in H^{1/2}(\partial\Omega;\mathbb R^3)`$, let $`u`$ solve $`\nabla\cdot\sigma_{\lambda,\mu}(u)=0`$ with trace $`f`$, and define the traction map $`\Lambda_{\lambda,\mu}f=\sigma_{\lambda,\mu}(u)\nu`$.

Does equality of the full traction maps for two admissible coefficient pairs imply equality of both $`\lambda`$ and $`\mu`$ in $`\Omega`$? Both coefficients are arbitrary smooth spatial functions.

## Application

Boundary loading and displacement measurements are used to infer elastic defects and tissue stiffness. This asks whether they contain enough information to separate the two isotropic elastic moduli.

## References

1. V. Markaki, D. Kourounis and A. Charalambopoulos, *On the identification of Lamé parameters in linear isotropic elasticity via a weighted self-guided TV-regularization method*, Journal of Inverse and Ill-posed Problems **32** (2024), 213–231, introduction. [Paper](https://doi.org/10.1515/jiip-2021-0050).
2. R.-Y. Lai, *Uniqueness and stability of Lamé parameters in elastography*, Journal of Spectral Theory **4** (2014), 841–877. [Paper](https://doi.org/10.4171/JST/88).

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Global-Uniqueness-for-the-Smooth-Isotropic-Elasticity-Inverse-Problem-September-24-2026/article.pdf), result family 372 (2026). Statement locator: `build/sections/introduction.tex, thm:main`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** Exactly bounded connected smooth 3D domains, arbitrary smooth real lambda/mu, mu>0 and 3lambda+2mu>0, static zero-frequency displacement-to-traction map and recovery of both coefficients. No near-boundary or near-constant condition is added.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-050) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/372.md). docs/372 covers the full uniqueness target via ElasticityUniqueness. No local kernel log inspected. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/050-static-lame-uniqueness.md).
