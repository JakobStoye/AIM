# 207. Can entangled codewords improve amplitude-damping classical capacity?

**Area:** Quantum communication; dissipative qubits

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

For $`0<\gamma<1`$, define a qubit channel

```math
\mathcal A_\gamma(\rho)=K_0\rho K_0^\dagger+K_1\rho K_1^\dagger,\quad K_0=\begin{pmatrix}1&0\\0&\sqrt{1-\gamma}\end{pmatrix},\quad K_1=\begin{pmatrix}0&\sqrt\gamma\\0&0\end{pmatrix}.
```

For any finite-dimensional quantum channel $`\Phi`$, let

```math
\chi(\Phi)=\sup_{\{p_j,\rho_j\}}\left[S\!\left(\sum_jp_j\Phi(\rho_j)\right)-\sum_jp_jS(\Phi(\rho_j))\right],
```

where the supremum is over finite ensembles of input density operators and $`S(\rho)=-\mathop{\mathrm{Tr}}\nolimits(\rho\log_2\rho)`$.

Is $`\chi(\mathcal A_\gamma^{\otimes n})=n\chi(\mathcal A_\gamma)`$ for every $`n\ge1`$ and every $`0<\gamma<1`$? Equivalently, does its unassisted classical capacity $`\sup_{n\ge1}\chi(\mathcal A_\gamma^{\otimes n})/n`$ equal the one-use Holevo information?

## Application

Amplitude damping models energy relaxation, including spontaneous emission. This asks whether entangling classical-message codewords across repeated uses increases the achievable communication rate.

## References

1. Felix Leditzky, Eneet Kaur, Nilanjana Datta, and Mark M. Wilde, [Approaches for approximate additivity of the Holevo information of quantum channels](https://arxiv.org/abs/1709.01111), *Phys. Rev. A* 97 (2018), 012332. Introduction and Section IV.A, equation (28), explicitly leave the channel’s classical capacity undetermined.
2. Fernando G. S. L. Brandão, Jens Eisert, Michał Horodecki, and Dong Yang, [Entangled inputs cannot make imperfect quantum channels perfect](https://arxiv.org/abs/1010.5074), *Phys. Rev. Lett.* 106 (2011), 230502; corrected preprint 2013. The amplitude-damping application supplies rigorous capacity bounds.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Classical-capacity-and-entropy-inequalities-for-generalized-amplitude-damping-September-24-2026/paper.pdf), result family 276 (2026). Statement locator: `build/paper.tex, thm:main and generalized-channel definition`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** The theorem establishes unrestricted tensor-power Holevo additivity for all generalized amplitude-damping parameters. At stationary excited population nu=0 the Kraus channel is the target ordinary amplitude-damping channel. Entropy and capacity are in bits, and arbitrary entangled block inputs are included.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-207) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/276.md). docs/276 covers tensor-power additivity for all parameters via AmplitudeDamping. No local kernel log inspected. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/207-amplitude-damping-additivity.md).
