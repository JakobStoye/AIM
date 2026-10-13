# 016. Localization at every disorder strength in two dimensions

**Area:** Disordered quantum transport

**Status:** 🟡 PARTIAL

**Last checked:** 2026-10-13

## Problem statement

On $`\ell^2(\mathbb Z^2)`$ let

```math
(H_\eta\psi)(n)=\sum_{|m-n|_1=1}\psi(m)+\eta V_n\psi(n),
```

where the $`V_n`$ are independent uniform variables on $`[-1,1]`$. Prove or disprove that for every fixed $`\eta>0`$, almost surely $`H_\eta`$ has a complete orthonormal basis of exponentially decaying eigenfunctions. Explicitly, each basis vector $`\phi`$ must satisfy $`|\phi(n)|\le C_\phi e^{-c_\phi|n-n_\phi|}`$ for some $`C_\phi,c_\phi>0`$ and $`n_\phi\in\mathbb Z^2`$. No uniform decay rate across all eigenvalues is demanded.

## Application

This would establish whether arbitrarily weak disorder ultimately localizes all single-particle states in a two-dimensional material, despite apparently extended behavior at accessible finite scales.

## References

1. B. Simon, [Schrödinger operators in the twenty-first century](https://web.ma.utexas.edu/mp_arc-bin/mpa?yn=00-78), in Mathematical Physics 2000 (2000), Problem 2.
2. F. Hernández, [Lecture notes on Quantum Diffusion and Random Matrix Theory](https://arxiv.org/abs/2511.04380), preprint (2025), §1, two-dimensional localization discussion.
3. J. Šuntajs, T. Prosen and L. Vidmar, [Localization challenges quantum chaos in the finite two-dimensional Anderson model](https://arxiv.org/abs/2212.10625), Physical Review B 107 (2023), 064205, numerical investigation.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/paper.pdf), result family 261 (2026). Statement locator: `build/sections/introduction.tex, main:theorem and scope paragraph at line 95`.

## Status review

**Known cases:** The OpenAI manuscript proves pure-point spectrum and a complete orthonormal eigenbasis at every fixed positive disorder. Exponential localization was already known at strong disorder.

**Remaining target:** Establish exponential decay for an entire orthonormal eigenbasis at every positive disorder, including weak disorder. Pure-point spectral type alone does not provide that decay.

**Statement comparison:** Same uniform law and every fixed positive disorder. The theorem supplies pure-point type and a complete orthonormal eigenbasis but explicitly does not assert exponential eigenfunction decay.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-016) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/261.md). docs/261 establishes only spectrum [-4-h,4+h], not pure-point type or exponential decay. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/016-anderson-planar-localization.md).
