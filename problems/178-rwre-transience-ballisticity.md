# 178. Does directional transience imply ballistic transport in an iid medium?

**Area:** Diffusion and transport in random environments

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

At each $`x\in\mathbb Z^3`$, sample independently an identically distributed probability vector $`(\omega_x(e))_{|e|_1=1}`$. Assume a deterministic $`\kappa>0`$ satisfies $`\omega_x(e)\ge\kappa`$ almost surely for every direction $`e`$. Given the environment, start $`X_0=0`$ and use transition probabilities $`P_\omega(X_{n+1}=x+e\mid X_n=x)=\omega_x(e)`$. Write $`P`$ for the joint law of environment and walk. For any unit vector $`\ell`$, does

```math
P(X_n\cdot\ell\longrightarrow+\infty)=1
```

imply the existence of a deterministic $`v`$ with $`v\cdot\ell>0`$ and $`P(X_n/n\to v)=1`$?

## Application

The statement asks whether persistent transport through an independently disordered medium must have positive macroscopic velocity, or can be slowed to zero by traps.

## References

- [David Campos and Alejandro F. Ramírez, *Ellipticity criteria for ballistic behavior of random walks in random environment* (2014)](https://doi.org/10.1007/s00440-013-0527-7), Conjecture 1.1.
- [Enrique Guerra and Alejandro F. Ramírez, *A proof of Sznitman's conjecture about ballistic RWRE* (2020)](https://arxiv.org/abs/1809.02011), abstract and main theorem.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Directional-transience-implies-ballisticity-September-23-2026/paper.pdf), result family 220 (2026). Statement locator: `Theorem 1.1, PDF page 3; Directional transience implies ballisticity theorem, label thm:main, 01-introduction.tex lines 50-61.`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** Directional transience implies ballisticity is stated for every d>=2, iid nearest-neighbor transition rows with a common positive lower bound, every fixed unit direction, and annealed almost-sure escape. It gives a deterministic vector limit X_n/n and strictly positive projection in the same direction, exactly including AIM d=3.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-178) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/220.md). DirectionalBallisticity comparator constructs an environment sampled once and retained along the walk, annealed path law, uniform ellipticity, and the exact vector limit. The declaration uses sorry; no local verification claimed. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/178-rwre-transience-ballisticity.md).
