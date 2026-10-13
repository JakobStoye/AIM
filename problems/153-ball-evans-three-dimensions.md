# 153. Smooth approximation of three-dimensional Sobolev homeomorphisms

**Area:** Nonlinear elasticity and approximation

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

For every pair of bounded domains $`\Omega,\Delta\subset\mathbb R^3`$, every $`1\le p<\infty`$, and every orientation-preserving homeomorphism $`f:\Omega\to\Delta`$ belonging to $`W^{1,p}(\Omega;\mathbb R^3)`$, do there exist smooth diffeomorphisms $`f_j:\Omega\to\Delta`$ such that

```math
\|f_j-f\|_{W^{1,p}(\Omega)}\longrightarrow0?
```

Decide this statement in dimension three; a negative answer may specify an exponent and a homeomorphism for which approximation fails. Boundary equality is not an additional requirement in this formulation.

## Application

In nonlinear elasticity, injectivity prevents distinct material points from occupying the same position. The conjecture tests whether smooth deformation models can approximate every admissible three-dimensional Sobolev deformation while preserving that constraint and controlling the deformation gradient, a foundation for variational approximation of elastic bodies.

## References

1. Stanislav Hencl, *Ball–Evans approximation problem: recent progress and open problems* (2025). [Paper](https://arxiv.org/abs/2502.01336). §2, Open problem 1, provides the higher-dimensional question and physical motivation.

2. Tadeusz Iwaniec, Leonid Kovalev and Jani Onninen, *Diffeomorphic Approximation of Sobolev Homeomorphisms*, Archive for Rational Mechanics and Analysis 201 (2011), 1047–1067. [Paper](https://arxiv.org/abs/1009.0286). Main theorem establishes planar approximation for $`1<p<\infty`$.

3. Daniel Campbell, Luigi D’Onofrio and Tomáš Vítek, *Diffeomorphic Approximation of Piecewise Affine Homeomorphisms*, Journal of Geometric Analysis 36 (2026), article 157. [Article](https://doi.org/10.1007/s12220-026-02398-w). Main theorem smooths already piecewise affine maps in dimensions three and four.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-1-le-p-le-2-September-24-2026/main.pdf), result family 368 (2026). Statement locator: `both manuscripts build/sections/01-introduction.tex, main:theorem`. [Additional PDF 2](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-p-gt-2-September-24-2026/main.pdf).

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** The first manuscript covers $`1\le p\le2`$ and the second covers $`2<p<\infty`$. Together they prove strong $`W^{1,p}`$ approximation by smooth diffeomorphisms onto the same target for any bounded 3D domains and any Sobolev homeomorphism. No boundary smoothness or boundary equality is required; orientation-preserving maps are included.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-153) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** No corresponding complete Lean development was identified in the linked family record; no Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/153-ball-evans-three-dimensions.md).
