# 034. Uniform spatial stability of von Neumann algebras

**Area:** Operator perturbation theory

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

For von Neumann algebras $`M,N\subseteq\mathcal B(H)`$, let $`M_1,N_1`$ denote their closed operator-norm unit balls and define

```math
d(M,N)=\max\left\{\sup_{x\in M_1}\inf_{y\in N_1}\|x-y\|,\sup_{y\in N_1}\inf_{x\in M_1}\|y-x\|\right\}.
```

Is it true that for every $`\varepsilon>0`$ there exists $`\delta>0`$, independent of $`H,M,N`$, such that $`d(M,N)<\delta`$ implies the existence of a unitary $`u\in\mathcal B(H)`$ satisfying

```math
uMu^*=N,\qquad\|u-I\|<\varepsilon?
```

## Application

This asks whether uniformly small errors in an entire operator algebra can be corrected by a small change of coordinates. Its application is foundational stability of observable algebras, rather than a finite-dimensional numerical algorithm.

## References

1. J. Peterson, [Open problems in operator algebras](https://www.math.uwaterloo.ca/~j37peter/problems.html), updated 15 May 2026; Problem O.4. Exact spatial formulation.
2. R. V. Kadison and D. Kastler, Perturbations of von Neumann algebras. I. Stability of type, American Journal of Mathematics 94 (1972), 38–54. Foundational paper, cited in Peterson’s problem list.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Universal-strong-Kadison-Kastler-stability-September-23-2026/paper.pdf), result family 289 (2026). Statement locator: `build/sections/01-introduction.tex, thm:main`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** The two-sided norm-unit-ball distance and the epsilon/delta quantifiers agree exactly for von Neumann algebras sharing identity I_H, the standard convention for the target. The separate one-sided near-inclusion and C*-algebra counterexamples do not refute this target.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-034) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/289.md). docs/289 covers the universal near-identity unitary conjugacy statement via StrongKadisonKastler. No local kernel log inspected. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/034-kadison-kastler.md).
