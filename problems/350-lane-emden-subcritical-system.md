# 350. Nonexistence of subcritical Lane–Emden equilibria in higher dimensions

**Area:** Nonlinear elliptic systems; reaction–diffusion

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

For every integer $`n\ge5`$ and exponents $`p,q>0`$ satisfying

```math
\frac1{p+1}+\frac1{q+1}>1-\frac2n,
```

is it impossible to find strictly positive functions $`u,v\in C^2(\mathbb R^n)`$ satisfying

```math
-\Delta u=v^p,\qquad-\Delta v=u^q\quad\hbox{on }\mathbb R^n?
```

No radial symmetry, stability, decay, integrability or finite-energy assumption is imposed. This is the remaining higher-dimensional part of the Lane–Emden conjecture.

## Application

Such coupled elliptic equations describe steady states in cooperative reaction–diffusion systems. Nonexistence on the whole space is also a tool for obtaining bounds and excluding concentration in bounded-domain models.

## References

1. K. Li, M. Li and J. Wei, [*On a new region for the Lane–Emden conjecture in higher dimensions*](https://arxiv.org/abs/2510.06613), preprint (2025), §1, displayed Conjecture and Theorem 1.1.
2. P. Souplet, [*The proof of the Lane–Emden conjecture in four space dimensions*](https://doi.org/10.1016/j.aim.2009.02.014), Advances in Mathematics 221 (2009), 1409–1427, main theorem.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Subcritical-Henon-Lane-Emden-Conjecture-September-24-2026/paper.pdf), result family 370 (2026). Statement locator: `build/sections/01-introduction.tex, cor:lane-emden`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** The unweighted corollary covers n>=3 and all p,q>0 under exactly 1/(p+1)+1/(q+1)>(n-2)/n, excluding strictly positive entire C2 solutions without symmetry, decay, integrability, stability or energy assumptions. This includes every n>=5 target case.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-350) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/370.md). docs/370 covers the complete unweighted target as a specialization of HenonEmden. No local kernel log inspected. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/350-lane-emden-subcritical-system.md).
