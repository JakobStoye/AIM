# 048 — Calderón uniqueness from an arbitrary local boundary patch

**Area:** Inverse problems / partial boundary data

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`\Omega\subset\mathbb R^n`$, $`n\geq3`$, be a bounded connected smooth domain, and let $`\Gamma`$ be any nonempty relatively open subset of $`\partial\Omega`$. For a positive $`\gamma\in C^\infty(\overline\Omega)`$, impose smooth boundary voltages supported in $`\Gamma`$ and measure the flux on $`\Gamma`$:

```math
\Lambda^\Gamma_\gamma f
=\gamma\partial_\nu u_f|_\Gamma,\quad
\nabla\cdot(\gamma\nabla u_f)=0,\quad
u_f|_{\partial\Omega}=f\in C_c^\infty(\Gamma).
```

Is $`\Lambda^\Gamma_{\gamma_1}=\Lambda^\Gamma_{\gamma_2}`$ sufficient to conclude $`\gamma_1=\gamma_2`$ throughout $`\Omega`$? No condition is imposed on the shape of the inaccessible boundary, and the conductivities need not be known near it.

## Application

In electrical imaging, electrodes may cover only one accessible part of an object. This isolates whether complete local experiments nevertheless determine its entire conductivity.

## References

1. C. Kenig and M. Salo, *Recent progress in the Calderón problem with partial data* (2014), §8, open problems. [Author manuscript](https://users.jyu.fi/~salomi/pub/calderon_partial_survey3.pdf).
2. C. Kenig and M. Salo, *The Calderón problem with partial data on manifolds and applications*, Analysis & PDE **6** (2013), 2003–2048. [Paper](https://msp.org/apde/2013/6-8/apde-v6-n8-p07-p.pdf).
3. Giovanni Covi, Antti Kujanpää and Jesse Railo, *Partial data stability for the inverse fractional conductivity problem* (2025), introduction comparing the classical problem. [Preprint](https://arxiv.org/abs/2505.18567).

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Smooth-Anisotropic-Uniqueness-in-the-Calderon-Problem-from-One-Boundary-Patch-September-24-2026/paper.pdf), result family 365 (2026). Statement locator: `build/sections/01-introduction.tex, main:scalar corollary`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** The explicit scalar corollary proves equality throughout the closed domain for strictly positive smooth scalar conductivities from identical arbitrary same-patch voltage/flux measurements, all n>=3, with no inaccessible-boundary agreement assumption.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-048) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/365.md). docs/365 links only the rough scalar nonuniqueness comparator, not the smooth same-patch uniqueness result. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/048-arbitrary-local-calderon-data.md).
