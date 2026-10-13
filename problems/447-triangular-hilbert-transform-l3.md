# 447. A uniform L3 estimate for the triangular Hilbert transform

**Area:** Multilinear harmonic analysis and coupled signal interactions

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13
## Problem statement

For Schwartz functions $`f,g:\mathbb R^2\to\mathbb C`$ and $`0<\varepsilon<R<\infty`$, set

```math
H_{\varepsilon,R}(f,g)(x,y)=\int_{\varepsilon<|t|<R}f(x+t,y)g(x,y+t)\,\frac{dt}{t}.
```

Does there exist an absolute constant $`C`$ such that

```math
\|H_{\varepsilon,R}(f,g)\|_{L^{3/2}(\mathbb R^2)}\le C\|f\|_{L^3(\mathbb R^2)}\|g\|_{L^3(\mathbb R^2)}
```

for every $`f,g,\varepsilon,R`$? The constant must be independent of both truncation scales.

## Application

This operator couples two signals sampled along crossing coordinate directions with a singular interaction kernel. Uniform control would supply a basic bound for modulation-sensitive multilinear interactions and encompass important Fourier reconstruction estimates.

## References

1. F. Yu-Hsiang Lin and L. Slavíková, [Rough averages of triangular Hilbert transforms](https://arxiv.org/abs/2607.20206), preprint (2026), §1, definition of H and discussion before (1.1).
2. P. Durcik, V. Kovač and C. Thiele, [Power-type cancellation for the simplex Hilbert transform](https://arxiv.org/abs/1608.00156), *Journal d’Analyse Mathématique* **139** (2019), 67–82, introduction and main theorem; [published article](https://doi.org/10.1007/s11854-019-0052-4).

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-maximal-triangular-Hilbert-transform-at-the-symmetric-point-September-24-2026/paper.pdf), result family 082 (2026). Statement locator: `Theorem thm:main`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** The operator is literally AIM integral F(x+t,y)G(x,y+t)dt/t with both finite hard truncation endpoints. An absolute bound for the pointwise supremum over epsilon,R in L^(3/2), for arbitrary complex L3 inputs, dominates every individual truncation. This is a full resolution, stronger than AIM; it is not merely the dyadic companion.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-447) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/082.md). Actual main_estimate formalizes the maximal estimate and full-measure/measurability conditions with genuine hard integrals. No local replay/axiom log. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/447-triangular-hilbert-transform-l3.md).
