# 450. Stein’s Hilbert-transform bound along Lipschitz directions

**Area:** Directional singular integrals and variable-direction propagation

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13
## Problem statement

Do absolute constants $`K\ge1`$ and $`C<\infty`$ exist such that the following holds? For every $`v:\mathbb R^2\to S^1`$ satisfying $`|v(x)-v(y)|\le|x-y|`$, every Schwartz function $`f`$, and every $`\lambda>0`$, define

```math
H_vf(x)=\lim_{\varepsilon\downarrow0}\int_{\varepsilon<|t|<1/K}f(x-tv(x))\,\frac{dt}{t}.
```

Then require

```math
\lambda^2\big|\{x\in\mathbb R^2:|H_vf(x)|>\lambda\}\big|\le C\|f\|_{L^2(\mathbb R^2)}^2.
```

The constants must be uniform over all such direction fields, including fields depending on both spatial coordinates.

## Application

Directional singular integrals model filtering along a spatially varying preferred orientation. The estimate would give uniform control when the local direction changes at a bounded rate, a basic issue for anisotropic transport and directional image processing.

## References

1. M. Lacey and X. Li, [On a conjecture of E. M. Stein on the Hilbert transform on vector fields](https://doi.org/10.1090/S0065-9266-10-00572-7), *Memoirs of the American Mathematical Society* **205** (2010), no. 965, Conjecture 1.5 and equation (1.6); [preprint](https://arxiv.org/abs/0704.0808).
2. F. Di Plinio, S. Guo, C. Thiele and P. Zorin-Kranich, [Square functions for bi-Lipschitz maps and directional operators](https://doi.org/10.1016/j.jfa.2018.07.005), *Journal of Functional Analysis* **275** (2018), 2015–2058, introduction and Corollary 1.4; [preprint](https://arxiv.org/abs/1706.07111).

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-uniform-Hilbert-transform-estimate-for-Lipschitz-directions-September-25-2026/main.pdf), result family 083 (2026). Statement locator: `Theorem thm:main`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** The theorem assumes all 1-Lipschitz unit fields on R2, allows both coordinates, holds at absolute outer scale a*>0, and proves a strong L2 principal-value bound and the exact weak-(2,2) inequality for Schwartz data. Choose AIM K=1/a* (>=1) and C=C*^2. Symmetric principal values exist pointwise on Schwartz inputs.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-450) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/083.md). Actual main provides principal-value and weak-(2,2) at an existential short scale; uniform_truncation additionally gives the reciprocal-Lipschitz bound. It discharges laceyLiInput through a proved import, not an external assumption in the endpoint. No local replay/axiom audit. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/450-stein-lipschitz-direction-hilbert-bound.md).
