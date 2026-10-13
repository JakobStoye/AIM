# 089. One-dimensionality of monotone Allen–Cahn fronts in dimension five

**Area:** Phase transitions

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`u\in C^2(\mathbb R^5;(-1,1))`$ solve

```math
-\Delta u=u-u^3\quad\text{in }\mathbb R^5,\qquad
\partial_{x_5}u>0\quad\text{everywhere}.
```

Must there exist $`a\in\mathbb R^5`$ with $`|a|=1`$, $`a_5>0`$, and $`b\in\mathbb R`$ such that

```math
u(x)=\tanh\!\left(\frac{a\cdot x-b}{\sqrt2}\right)?
```

Do not assume prescribed limits as $`x_5\to\pm\infty`$, minimizing energy, or an additional energy-growth bound. This is the original monotone De Giorgi question specialized to five dimensions.

## Application

The Allen–Cahn equation models diffuse phase interfaces. The assertion would force every globally monotone stationary interface in this dimension to be planar.

## References

- [Nassif Ghoussoub and Changfeng Gui, *On De Giorgi's conjecture in dimensions 4 and 5* (Annals of Mathematics, 2003), hypotheses of the partial results](https://doi.org/10.4007/annals.2003.157.313).
- [Enric Florit-Simon and Joaquim Serra, *On stable solutions to the Allen-Cahn equation with bounded energy density in R⁴* (2025), introduction and main theorem](https://arxiv.org/abs/2509.02739).

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/De-Giorgis-conjecture-in-dimension-eight-September-26-2026/article.pdf), result family 375 (2026). Statement locator: `build/sections/00-introduction.tex, thm:monotone`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** The unrestricted monotone Allen-Cahn rigidity theorem is stated in dimension eight with no directional limits, energy growth or minimization hypothesis. Embed the target by U(x1,...,x8)=u(x1,...,x4,x8). The extra-coordinate independence forces their components of the resulting unit direction to vanish, giving exactly the dimension-five tanh profile with positive fifth component.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-089) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** No corresponding complete Lean development was identified in the linked family record; no Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/089-de-giorgi-dimension-five.md).
