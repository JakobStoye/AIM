# 047 — Smooth anisotropic Calderón uniqueness

**Area:** Inverse problems / anisotropic imaging

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`M`$ be a compact connected smooth manifold of dimension $`n\geq3`$ with nonempty smooth boundary. For a smooth Riemannian metric $`g`$, define $`\Lambda_g f=\partial_{\nu_g}u|_{\partial M}`$, where $`\Delta_g u=0`$ and $`u|_{\partial M}=f`$. Consider two metrics inducing the same boundary metric, so their boundary operators have the same interpretation.

Does $`\Lambda_{g_1}=\Lambda_{g_2}`$ imply the existence of a smooth diffeomorphism $`F:M\to M`$, with $`F|_{\partial M}=\mathrm{Id}`$, such that $`g_1=F^*g_2`$? The data consist of this single zero-frequency boundary operator for each metric.

## Application

Anisotropic electrical conductivity depends on direction as well as position. This question specifies the unavoidable coordinate ambiguity in recovering it from boundary electrical measurements.

## References

1. J. M. Lee and G. Uhlmann, *Determining anisotropic real-analytic conductivities by boundary measurements*, Communications on Pure and Applied Mathematics **42** (1989), 1097–1112. [Paper](https://doi.org/10.1002/cpa.3160420804).
2. Y. Yi, *Riemannian and Lorentzian Calderón Problem Under Magnetic Perturbation*, IMRN **2025**, rnaf366, §1.1. [Paper](https://doi.org/10.1093/imrn/rnaf366).

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Smooth-Anisotropic-Uniqueness-in-the-Calderon-Problem-from-One-Boundary-Patch-September-24-2026/paper.pdf), result family 365 (2026). Statement locator: `build/sections/01-introduction.tex, main:full corollary`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** The explicit full-boundary corollary recovers arbitrary smooth metrics on any compact connected smooth n>=3 manifold by a diffeomorphism fixing every boundary point. Equal target pointwise normal-DN operators with the same boundary metric yield equal density-valued energy maps, so the corollary applies.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-047) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/365.md). docs/365 links only the bounded-measurable scalar counterexample. No Lean formalization of this smooth anisotropic target is provided in the family document. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/047-smooth-anisotropic-calderon.md).
