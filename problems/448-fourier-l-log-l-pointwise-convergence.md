# 448. Almost-everywhere Fourier reconstruction of L log L signals

**Area:** Fourier analysis and endpoint signal reconstruction

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13
## Problem statement

Let $`\mathbb T=\mathbb R/\mathbb Z`$ with normalized Lebesgue measure. Suppose $`f:\mathbb T\to\mathbb C`$ is measurable and

```math
\int_{\mathbb T}|f(x)|\log(e+|f(x)|)\,dx<\infty.
```

Define $`\widehat f(k)=\int_{\mathbb T}f(x)e^{-2\pi ikx}\,dx`$ and the symmetric partial sums $`S_Nf(x)=\sum_{k=-N}^{N}\widehat f(k)e^{2\pi ikx}`$. Must $`S_Nf(x)\to f(x)`$ for almost every $`x`$ as $`N\to\infty`$? The assertion concerns the full sequence of partial sums, without averaging or restriction to a sparse subsequence.

## Application

The question identifies a near-integrable signal class for which direct spectral reconstruction recovers pointwise values despite large localized amplitudes. It is an endpoint stability issue for Fourier approximations.

## References

1. F. Di Plinio, [Weak-Lp bounds for the Carleson and Walsh–Carleson operators](https://doi.org/10.1016/j.crma.2014.02.005), *Comptes Rendus Mathématique* **352** (2014), 327–331, introduction and discussion of the L log L conjecture; [preprint](https://arxiv.org/abs/1312.0398).
2. F. Di Plinio and A. Fragkos, [The weak-type Carleson theorem via wave packet estimates](https://arxiv.org/abs/2204.08051), *Transactions of the American Mathematical Society* (2025), §1, Theorem A and Remark 1.2.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Almost-everywhere-Fourier-convergence-in-L-log-L-September-23-2026/paper.pdf), result family 075 (2026). Statement locator: `Theorem thm:main`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** Source torus R/(2*pi*Z) with normalized measure and e^(ikx) is AIM unit torus after x=2*pi*y. Integrability with log(2+|f|) is equivalent to log(e+|f|), with bounded ratio and finite measure. Both state complex measurable data and a single null set outside which the entire sequence of ordinary symmetric partial sums converges to f.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-448) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/075.md). Actual paperMain establishes full symmetric sums for measurable complex LlogL data on the normalized 2*pi torus; coordinate rescaling identifies AIM. No local reproduction/axiom log. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/448-fourier-l-log-l-pointwise-convergence.md).
