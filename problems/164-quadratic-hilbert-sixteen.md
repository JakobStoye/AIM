# 164. A uniform limit-cycle bound for quadratic planar dynamics

**Area:** Nonlinear oscillations and dynamical systems

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Does there exist an integer $`H_2<\infty`$ such that every system

```math
\dot x=P(x,y),\qquad\dot y=Q(x,y),\qquad P,Q\in\mathbb R[x,y],\quad\max(\deg P,\deg Q)\le2,
```

has at most $`H_2`$ distinct limit cycles in $`\mathbb R^2`$? A limit cycle is an isolated periodic orbit, counted once as a geometric curve, without multiplicity. The bound must be independent of all polynomial coefficients.

## Application

Quadratic rate equations model interacting populations, chemical kinetics, and nonlinear oscillators. A uniform bound would limit the number of isolated oscillatory regimes such models can support.

## References

1. Armengol Gasull and Paulo Santana, *A note on Hilbert 16th Problem* (2024), §1. [Paper](https://arxiv.org/html/2407.13465v2). Explicitly states that finiteness of the quadratic Hilbert number is unknown.

2. Yulij Ilyashenko, *Centennial history of Hilbert’s 16th problem*, Bulletin of the American Mathematical Society 39 (2002), 301–354. [Article](https://doi.org/10.1090/S0273-0979-02-00946-1). Distinguishes individual finiteness from the uniform-bound problem.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026.pdf), result family 143 (2026). Statement locator: `Theorem 1.1, PDF page 3; Uniform boundedness theorem, label thm:uniform, 01-introduction.tex lines 12-16.`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** Uniform boundedness states that every real planar polynomial vector field of degree at most d has at most the finite integer B(d) isolated geometric periodic-orbit images in the whole plane, independent of coefficients. Specializing d=2 supplies H_2. Definitions match AIM without multiplicity.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-164) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/143.md). Family143 Lean docs link only QuinticLienard: degree<=5 classical Lienard systems, not arbitrary quadratic planar vector fields. Thus complete AIM164 is not covered by the selected formal statement; no Lean verified status. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/164-quadratic-hilbert-sixteen.md).
