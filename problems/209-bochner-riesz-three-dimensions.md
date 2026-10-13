# 209. Sharp Bochner–Riesz summability in three dimensions

**Area:** Harmonic analysis; frequency filtering

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

For $`\delta>0`$ and a Schwartz function $`f`$ on $`\mathbb R^3`$, define $`B^\delta f`$ through its Fourier transform by

```math
\widehat{B^\delta f}(\xi)=(1-|\xi|^2)_+^\delta\widehat f(\xi),\qquad r_+=\max\{r,0\}.
```

For every $`1<p<\infty`$ and

```math
\delta>\max\left\{3\left|\frac1p-\frac12\right|-\frac12,\,0\right\},
```

does there exist $`C_{p,\delta}<\infty`$ such that $`\|B^\delta f\|_{L^p}\le C_{p,\delta}\|f\|_{L^p}`$ for all such $`f`$?

## Application

Bochner–Riesz means smooth a spherical frequency cutoff. The sharp threshold determines how little smoothing suffices to reconstruct a signal without unbounded amplification in the chosen integrability norm.

## References

1. Shukun Wu, [On the Bochner–Riesz operator in three dimensions](https://arxiv.org/abs/2008.13043), *J. Anal. Math.* 149 (2023), 677–718. Introduction, Conjecture 1.1 and equation (1.3), states the threshold; the main theorem covers a restricted exponent range.
2. Shaoming Guo, Changkeun Oh, Hong Wang, Shukun Wu, and Ruixiang Zhang, [The Bochner–Riesz problem: an old approach revisited](https://arxiv.org/abs/2104.11188), *Peking Math. J.* 8 (2025), 201–270. Conjecture 1.1, Theorem 1.3, and Remark 1.4 separate the conjecture from known bounds.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Bochner-Riesz-Multipliers-in-Three-Dimensions-September-24-2026/Bochner-Riesz-Multipliers-in-Three-Dimensions-September-24-2026.pdf), result family 078 (2026). Statement locator: `Theorem thm:bochner-riesz; Corollary cor:full-bochner-riesz`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** The primary L3 estimate holds for every positive order; the explicitly read analytic-interpolation and duality corollary gives all 1<=p<=infinity under delta>max(3|1/p-1/2|-1/2,0). Restricting to AIM 1<p<infinity gives exactly its multiplier and full strict range. No equality endpoint is needed.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-209) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** No corresponding complete Lean development was identified in the linked family record; no Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/209-bochner-riesz-three-dimensions.md).
