# 205. The entropy photon-number inequality

**Area:** Quantum optics; communication limits

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`\rho_A,\rho_B`$ be arbitrary states of $`n\ge1`$ bosonic modes, each with finite expected total photon number. The joint input is $`\rho_A\otimes\rho_B`$. For $`0\le\eta\le1`$, mix corresponding modes by a beam-splitter unitary, so that the output annihilation operators are

```math
c_j=\sqrt\eta\,a_j+\sqrt{1-\eta}\,b_j,\qquad d_j=-\sqrt{1-\eta}\,a_j+\sqrt\eta\,b_j.
```

Let $`\rho_C`$ be the reduced state of the $`c`$ modes after discarding the $`d`$ modes. With $`S(\rho)=-\mathop{\mathrm{Tr}}\nolimits(\rho\log\rho)`$ and $`g(t)=(t+1)\log(t+1)-t\log t`$ for $`t\ge0`$, is

```math
g^{-1}\!\left(\frac{S(\rho_C)}n\right)\ge\eta g^{-1}\!\left(\frac{S(\rho_A)}n\right)+(1-\eta)g^{-1}\!\left(\frac{S(\rho_B)}n\right)
```

always true? The inverse is on $`[0,\infty)`$; correlations among the $`n`$ modes within either input are allowed.

## Application

This gives a sharp lower bound on optical output noise at fixed input entropies, with consequences for information rates in bosonic broadcast and wiretap communication.

## References

1. Saikat Guha, Baris I. Erkmen, and Jeffrey H. Shapiro, [The Entropy Photon-Number Inequality and its Consequences](https://arxiv.org/abs/0710.5666), preprint (2007). Equation (13) states the original beam-splitter conjecture.
2. Giacomo De Palma, Dario Trevisan, Vittorio Giovannetti, and Luigi Ambrosio, [Gaussian optimizers for entropic inequalities in quantum information](https://arxiv.org/abs/1803.02360), *J. Math. Phys.* 59 (2018), 081101. Section V.B, Conjecture V.15, equation (70), gives the multimode form; Section VII.A distinguishes the proved quantum entropy-power inequality.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-entropy-photon-number-inequality-September-24-2026/paper.pdf), result family 273 (2026). Statement locator: `build/sections/00-introduction.tex, thm:epni`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** The exact displayed g-inverse entropy photon-number inequality is proved for any finite number of modes, any transmissivity in [0,1], finite photon energy, product inputs, and arbitrary correlations within either port. Entropy uses natural logarithms as in the target.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-205) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/273.md). docs/273 describes the full EPnI target via EntropyPhotonNumber; only channel-capacity consequences are outside it. No local kernel log inspected. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/205-entropy-photon-number.md).
