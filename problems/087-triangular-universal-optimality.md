# 087. Gaussian-energy optimality of the triangular lattice among periodic configurations

**Area:** Crystallization and energy minimization

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`\Lambda_\triangle\subset\mathbb R^2`$ be the triangular lattice scaled to covolume one. For any integer $`N\ge1`$, a lattice $`L`$ of covolume $`N`$, and points $`a_1,\ldots,a_N`$ distinct modulo $`L`$, set $`P=\bigcup_i(a_i+L)`$. Prove or disprove, for every $`\alpha>0`$,

```math
\frac1N\sum_{i,j=1}^{N}\ \sum_{\substack{v\in L\\(i,j,v)\ne(i,i,0)}}
e^{-\pi\alpha|a_i-a_j-v|^2}
\ \ge\
\sum_{v\in\Lambda_\triangle\setminus\{0\}}e^{-\pi\alpha|v|^2}.
```

In the left sum, omit only the self-interaction $`j=i,v=0`$ for each $`i`$. All configurations have point density one. This is the periodic Gaussian formulation of triangular-lattice universal optimality.

## Application

This is a crystallization question for particles with repulsive Gaussian interactions: at fixed density, can any periodic arrangement have lower energy than the triangular crystal? Because positive mixtures of Gaussian kernels generate a broad family of completely monotone pair energies, a proof would identify the same preferred crystal for many such interaction models.

## References

- [Henry Cohn and Abhinav Kumar, *Universally optimal distribution of points on spheres* (Journal of the AMS, 2007), Euclidean universal-optimality conjecture](https://arxiv.org/abs/math/0607446).
- [Mircea Petrache and Sylvia Serfaty, *Crystallization for Coulomb and Riesz Interactions as a Consequence of the Cohn-Kumar Conjecture* (2019), opening discussion](https://arxiv.org/abs/1908.09714).

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/An-atomic-certificate-for-triangular-lattice-universal-optimality-September-26-2026/paper.pdf), result family 090 (2026). Statement locator: `Theorems thm:universal and thm:gaussian; transfer eq:gaussian-energy`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** Use g(t)=exp(-pi*alpha*t) for every alpha>0. Any AIM periodic union of N translates of a lattice of covolume N is locally finite and has centered-disk density one. Its ordered-pair finite-disk energy per particle converges to the displayed per-cell average: each offset occurs with frequency 1/N, Gaussian tails are summable, and boundary pairs have vanishing normalized contribution. Both sides omit only equal-point self-interactions. The theorem therefore yields the full arbitrary-N periodic bound.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-087) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/090.md). Actual universal_energy_minimum proves the all-configuration completely-monotone energy statement, and sharp_gaussian_minorants_atomic supplies every Gaussian parameter. Periodic per-cell identification is a mathematical transfer, not a separately replayed AIM adapter. No local verification log. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/087-triangular-universal-optimality.md).
