# 206. Composing two PPT channels destroys all entanglement

**Area:** Quantum information; repeater channels

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`d\ge2`$ and let $`\Phi,\Psi:M_d(\mathbb C)\to M_d(\mathbb C)`$ be completely positive trace-preserving maps. Assume that $`T\circ\Phi`$ and $`T\circ\Psi`$ are also completely positive, where $`T`$ is matrix transposition in a fixed basis. Complete positivity means that $`\mathop{\mathrm{id}}\nolimits_r\otimes\Phi`$ preserves positive semidefiniteness for every $`r\ge1`$, and similarly for the other maps.

Must $`\Psi\circ\Phi`$ be entanglement breaking? Explicitly, for every density operator $`\rho`$ on $`\mathbb C^d\otimes\mathbb C^d`$, must

```math
(\mathop{\mathrm{id}}\nolimits_d\otimes(\Psi\circ\Phi))(\rho)=\sum_{j=1}^k p_j\alpha_j\otimes\beta_j
```

for some finite $`k`$, probabilities $`p_j`$, and density operators $`\alpha_j,\beta_j`$?

## Application

This determines whether a pair of noisy quantum links with positive partial transpose can retain terminal entanglement, a basic limitation for quantum repeater designs.

## References

1. Matthias Christandl, Alexander Müller-Hermes, and Michael M. Wolf, [When Do Composed Maps Become Entanglement Breaking?](https://arxiv.org/abs/1807.01266), *Ann. Henri Poincaré* 20 (2019). Introduction and the discussion of the PPT-squared conjecture establish the formulation and dimension-three result.
2. Junhyeong An and Soojoon Lee, [Beyond the Positive Partial Transpose Squared Conjecture: The Qutrit Case](https://arxiv.org/abs/2607.15947), preprint, 17 July 2026. Introduction and Section II, Conjecture 2, explicitly leave higher dimensions open.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Entanglement-with-zero-distillable-secret-key-in-local-dimension-ten-September-27-2026/paper.pdf), result family 272 (2026). Statement locator: `build/source/sections/introduction.tex, thm:main-channel`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete counterexample to the original target.

**Statement comparison:** The manuscript constructs a trace-preserving PPT channel Theta on M21 whose square is not entanglement breaking. Taking Phi=Psi=Theta directly disproves the all-dimension all-channel target. The separate two non-trace-preserving maps would not by themselves be enough.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-206) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/272.md). docs/272 covers the dimension-21 trace-preserving PPT channel counterexample via DimensionTenChannel; the zero-secret-key statement is outside the comparators. No local kernel log inspected. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/206-ppt-squared.md).
