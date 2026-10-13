# 046 — Calderón uniqueness for bounded measurable conductivities

**Area:** Inverse problems / electrical impedance tomography

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`\Omega\subset\mathbb R^3`$ be a bounded connected domain with smooth boundary. For a real scalar conductivity $`\gamma\in L^\infty(\Omega)`$ satisfying $`0<c\leq\gamma\leq C<\infty`$ almost everywhere, let $`u_f\in H^1(\Omega)`$ solve

```math
\nabla\cdot(\gamma\nabla u_f)=0,\qquad u_f|_{\partial\Omega}=f.
```

For $`f,h\in H^{1/2}(\partial\Omega)`$, define the weak Dirichlet-to-Neumann map by
$`\langle\Lambda_\gamma f,h\rangle=\int_\Omega\gamma\nabla u_f\cdot\nabla v_h\,dx`$, where $`v_h`$ is any $`H^1`$ extension of the boundary trace $`h`$. Prove or disprove that

```math
\Lambda_{\gamma_1}=\Lambda_{\gamma_2}\quad\Longrightarrow\quad
\gamma_1=\gamma_2\ \text{almost everywhere in }\Omega
```

for every pair of such conductivities. No continuity, derivative, or known partition assumption is imposed.

## Application

This asks whether ideal boundary voltage/current measurements can distinguish arbitrary bounded heterogeneous conductors, including discontinuous tissue or material coefficients.

## References

1. G. Uhlmann, *30 Years of Calderón's Problem* (2013), discussion of low regularity after the uniqueness theorems. [Authoritative lecture proceedings](https://www.numdam.org/article/SLSEDP_2012-2013____A13_0.pdf).
2. P. Caro, M. Á. García-Ferrero and K. M. Rogers, *Reconstruction for the Calderón problem with Lipschitz conductivities*, Analysis & PDE **18** (2025), 2033–2060, introduction and main theorem. [Paper](https://doi.org/10.2140/apde.2025.18.2033); [preprint](https://arxiv.org/abs/2401.06120).

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Nonuniqueness-for-Bounded-Measurable-Scalar-Conductivities-in-Three-Dimensions-September-23-2026/paper.pdf), result family 365 (2026). Statement locator: `build/paper.tex, thm:main`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete counterexample to the original target.

**Statement comparison:** Uniformly positive bounded real scalar conductivities on the smooth ball B(0,3) differ on positive volume and have exactly the same full weak H1/2-to-H-1/2 DN operator. This directly refutes the all-pairs target and even keeps both conductivities equal to one near the boundary.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-046) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/365.md). docs/365 covers this full rough scalar-conductivity counterexample via Conductivity. It does not cover the separate smooth anisotropic papers. No local kernel log inspected. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/046-rough-conductivity-calderon.md).
