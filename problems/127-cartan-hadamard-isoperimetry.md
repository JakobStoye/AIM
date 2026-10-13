# 127 — Euclidean isoperimetry in higher-dimensional Cartan–Hadamard manifolds

**Area:** Geometric analysis / volume and boundary optimization

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`(M^n,g)`$ be a complete simply connected smooth Riemannian manifold, with $`n\ge5`$ and sectional curvature everywhere nonpositive. Let $`\Omega\Subset M`$ be a domain with smooth boundary. Write $`V=\mathop{\mathrm{Vol}}\nolimits_g(\Omega)`$, $`A=\mathop{\mathrm{Area}}\nolimits_g(\partial\Omega)`$, and let $`\omega_n`$ be the volume of the Euclidean unit ball.

Must

```math
A\ge n\omega_n^{1/n}V^{(n-1)/n}
```

hold for every such domain? No pinching, symmetry, small-volume or curvature-nullity hypothesis is imposed.

## Application

The inequality would compare the boundary cost of enclosing material in negatively curved spaces with the Euclidean optimum. It also supplies sharp constants for diffusion and Sobolev estimates.

## References

1. M. Ghomi and J. I. Stavroulakis, *A Local Isoperimetric Inequality for Balls with Nonpositive Curvature* (2026), [IMRN, rnag043](https://doi.org/10.1093/imrn/rnag043), §1 and Theorem 1.1. States the conjecture and proves a local metric-perturbation result.
2. M. Ghomi, *Isoperimetric and total curvature inequalities in Cartan-Hadamard manifolds with nullity* (2026), [arXiv:2605.24638](https://arxiv.org/abs/2605.24638), Theorem 1.1 and Corollary 1.2. Covers manifolds with nullity index at least $`n-3`$.
3. M. Ghomi, *Total curvature and isoperimetric inequalities in pinched Cartan-Hadamard manifolds* (2026), [arXiv:2608.12020](https://arxiv.org/abs/2608.12020), abstract and introduction. Establishes a five-dimensional result with sufficiently tight curvature pinching.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Generalized-Cartan-Hadamard-isoperimetry-and-Euclidean-equality-rigidity-September-23-2026/paper.pdf), result family 337 (2026). Statement locator: `build/sections/01-introduction.tex, thm:main with kappa=0`. [Additional PDF 2](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Sharp-integral-fillings-in-CAT%280%29-spaces-September-23-2026/paper.pdf).

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** The theorem includes all smooth complete simply connected n>=2 manifolds with Sec<=0 and every finite-volume finite-perimeter set. For the target smooth relatively compact domain, perimeter is boundary area; the coefficient is exactly n*omega_n^(1/n). This includes n>=5 with no additional geometric restriction. The CAT(0) companion separately states cor:cartan-hadamard with exactly the same smooth-domain inequality in every d>=3.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-127) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/337.md). docs/337 covers sharp integral-current filling in proper CAT(0) spaces via SharpCAT0Filling. The companion explicitly derives the smooth Cartan-Hadamard domain inequality by uniqueness of compactly supported top-dimensional fillings. This is mathematical target coverage with a geometric-current reduction, not a successful local kernel verification. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/127-cartan-hadamard-isoperimetry.md).
