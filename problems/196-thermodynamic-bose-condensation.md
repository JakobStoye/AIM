# 196. Bose condensation at fixed dilute density

**Area:** Ultracold quantum gases

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Fix a nonzero, nonnegative, radial potential $`V\in C_c^\infty(\mathbb R^3)`$. Let $`\Lambda_L=(\mathbb R/L\mathbb Z)^3`$ and $`V_L(x)=\sum_{k\in\mathbb Z^3}V(x+Lk)`$. On symmetric $`L^2(\Lambda_L^N)`$ define

```math
H_{N,L}=\sum_{j=1}^N-\Delta_{x_j}+\sum_{i<j}V_L(x_i-x_j).
```

Let $`\Psi_{N,L}`$ be its normalized nonnegative ground state, let $`\gamma_{N,L}^{(1)}`$ be its one-particle reduced density operator normalized to trace $`N`$, and put $`\phi_L=L^{-3/2}`$. Prove or disprove: there is $`\rho_0(V)>0`$ such that every fixed $`0<\rho<\rho_0(V)`$ satisfies

```math
\liminf_{\substack{L\to\infty,\ N\to\infty\\N/L^3\to\rho}}\frac{\langle\phi_L,\gamma_{N,L}^{(1)}\phi_L\rangle}{N}>0.
```

The potential and the density remain fixed during the thermodynamic limit.

## Application

This would derive macroscopic occupation of one orbital directly from a repulsive many-atom Hamiltonian, a basic microscopic explanation of condensation in a homogeneous dilute gas.

## References

1. J. J. Chong, H. Liang and P. T. Nam, [Kinetic localization via Poincaré-type inequalities and applications to the condensation of Bose gases](https://arxiv.org/abs/2510.20493), preprint (2025; revised May 2026), §1 and §2.2: explicitly identifies thermodynamic condensation as open and distinguishes its scaling regime.
2. E. H. Lieb and R. Seiringer, [Bose-Einstein Condensation of Dilute Gases in Traps](https://arxiv.org/abs/math-ph/0210028), preprint (2002), §1, Introduction and Main Results: rigorous condensation in the different Gross–Pitaevskii limit.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-density-uniform-condensate-bound-for-dilute-Bose-gases-September-27-2026/paper.pdf), result family 267 (2026). Statement locator: `build/sections/introduction.tex, thm:main`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** The density-uniform theorem covers every fixed bounded measurable nonzero nonnegative radial finite-range potential, so includes every target Cc-infinity potential. At T=0 its exact canonical ground state has occupation at least c*(V)>0 at every sufficiently dilute fixed density along all thermodynamic sequences, with trace-N density matrix and constant orbital.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-196) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/267.md). docs/267 covers only the hard-sphere ground-state model. The target requires smooth finite-range potentials; that formalization does not cover it. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/196-thermodynamic-bose-condensation.md).
