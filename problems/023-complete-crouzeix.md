# 023. The complete Crouzeix conjecture

**Area:** Operator theory and numerical linear algebra

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

For every $`n,m\ge1`$, $`A\in\mathbb C^{n\times n}`$, and polynomial $`F(z)=\sum_{j=0}^d C_jz^j`$ with coefficients $`C_j\in\mathbb C^{m\times m}`$, is

```math
\left\|\sum_{j=0}^d C_j\otimes A^j\right\|_2
\le 2\max_{z\in W(A)}\|F(z)\|_2?
```

Here $`W(A)=\{x^*Ax:x\in\mathbb C^n,\ \|x\|_2=1\}`$, $`\otimes`$ is the Kronecker product, and $`\|\cdot\|_2`$ is the Euclidean operator norm. The unresolved range is arbitrary $`n\ge4`$ and arbitrary matrix level $`m`$.

## Application

Matrix-valued approximation bounds control coupled matrix functions and block computations. Complete spectral-set bounds also govern dilation and similarity methods used to analyze nonnormal operators.

## References

1. M. Crouzeix and C. Palencia, [The numerical range is a $`(1+\sqrt2)`$-spectral set](https://doi.org/10.1137/17M1116672), SIAM J. Matrix Anal. Appl. 38 (2017), 649–655. Universal complete bound.
2. P. Åhag, R. Czyż and J. Virtanen, [Square Functions and the Complete Crouzeix Conjecture in Dimension Three](https://arxiv.org/abs/2608.27346), 2026, v2; introduction and Theorem 1.1. Complete bound through order three.
3. A. Townsend and A. Greenbaum, [The Neurosurgery Resident Who Proved Crouzeix’s Conjecture](https://alextownsend.net/essays/SIAMNews_CrouzeixConjecture.pdf), 15 August 2026. Expert verification of the distinct scalar result.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026/paper.pdf), result family 325 (2026). Statement locator: `build/main.tex, thm:main`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** All n,m, all degrees, arbitrary complex coefficient matrices and constant two match. The manuscript orders tensors A^j tensor C_j and AIM orders C_j tensor A^j; the tensor-factor flip is unitary and preserves the operator norm.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-023) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/325.md). docs/325 covers the full finite-matrix target via DirectCrouzeix/CompleteCrouzeix, plus arbitrary-Hilbert and structural extensions. No local kernel log inspected. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/023-complete-crouzeix.md).
