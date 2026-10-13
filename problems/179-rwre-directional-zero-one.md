# 179. The directional zero–one law in three-dimensional random media

**Area:** Random transport and ergodicity

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`(\omega_x)_{x\in\mathbb Z^3}`$ be iid nearest-neighbor transition probability vectors, with $`\omega_x(e)\ge\kappa>0`$ almost surely for each of the six unit lattice directions. Conditional on $`\omega`$, let the walk start at $`0`$ and take step $`e`$ from $`x`$ with probability $`\omega_x(e)`$. Under the joint law $`P`$ of the environment and the walk, must

```math
P(X_n\cdot\ell\longrightarrow+\infty)\in\{0,1\}
```

hold for every deterministic unit vector $`\ell\in\mathbb R^3`$?

## Application

This tests whether transport in a fixed macroscopic direction is an all-or-nothing property of an independently disordered medium. It is a basic obstruction to an unconditional deterministic law of large numbers.

## References

- [Ofer Zeitouni, *Random Walks in Random Environments*, author survey (19 July 2006)](https://www.wisdom.weizmann.ac.il/~zeitouni/pdf/rwrereview.pdf), Conjecture 4.2 and Theorem 4.3.
- [Martin P. W. Zerner and Franz Merkl, *A zero-one law for planar random walks in random environment* (2001)](https://doi.org/10.1214/aop/1015345769), the planar result.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-directional-zero-one-law-under-strict-ellipticity-September-23-2026/paper.pdf), result family 220 (2026). Statement locator: `Theorem 1.1, PDF page 2; Introduction theorem label thm:main, 01-introduction.tex lines 61-69, strict-ellipticity equation and path-law definitions preceding.`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** The zero-one theorem covers every d>=3, iid nearest-neighbor transition rows, every fixed nonzero real direction, and merely strict positivity. Uniform ellipticity of the AIM Z^3 model is stronger and hence sufficient. Its escape event and annealed law from the origin agree exactly.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-179) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/220.md). DirectionalWalk comparator gives the iid product environment and annealed origin escape event; main declaration uses sorry. No local verification claimed. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/179-rwre-directional-zero-one.md).
