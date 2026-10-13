# 065 — Positive metric entropy for a standard map

**Area:** Hamiltonian chaos and transport

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

On $`\mathbb T^2=(\mathbb R/2\pi\mathbb Z)^2`$, equipped with normalized Lebesgue measure $`m`$, consider the area-preserving standard map

```math
T_K(x,y)=(x+y+K\sin x,\ y+K\sin x)\pmod {2\pi}.
```

Prove that there exists a real $`K\ne0`$ with positive Kolmogorov–Sinai entropy $`h_m(T_K)>0`$. Here

```math
h_m(T)=\sup_{\mathcal P}\lim_{n\to\infty}\frac1n
 H_m\!\left(\bigvee_{j=0}^{n-1}T^{-j}\mathcal P\right),
\quad H_m(\mathcal P)=-\sum_{P\in\mathcal P}m(P)\log m(P),
```

and the supremum runs over finite measurable partitions.

## Application

The standard map models a periodically kicked rotor. Positive entropy for physical area measure would rigorously establish sustained chaos on a set of positive phase-space area.

## References

1. Alex Blumenthal, *Statistical Properties for Compositions of Standard Maps with Increasing Coefficient* Ergodic Theory and Dynamical Systems **41** (2021), 981–1024; online 2020, introduction. [DOI](https://doi.org/10.1017/etds.2019.115), [preprint](https://arxiv.org/abs/1710.09058).
2. Pierre Berger, *Wild Dynamics on Manifolds* (2025 preprint, ICM 2026 survey), §§1.4 and 2.3. [Author's survey](https://arxiv.org/abs/2510.12929).

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Positive-Metric-Entropy-for-the-Standard-Map-at-Large-Parameters-September-23-2026/paper.pdf), result family 146 (2026). Statement locator: `Theorem 1.1, PDF page 2; Introduction, theorem label main:entropy (first theorem).`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** For the unit torus source map f_k(x,y)=(x+y+k sin(2 pi x), y+k sin(2 pi x)), every k above a positive threshold has positive entropy for normalized area. Coordinate scaling X=2 pi x,Y=2 pi y gives the exact AIM map with K=2 pi k, preserving normalized probability and entropy. Hence an admissible nonzero K exists.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-065) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/146.md). StandardMapEntropy comparator defines the actual sine map and finite-partition entropy and the full parameter-tail statement. The comparator theorem ends in sorry; upstream proof-module and reproduction/axiom evidence must be evaluated separately. No local verification claimed. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/065-standard-map-metric-entropy.md).
