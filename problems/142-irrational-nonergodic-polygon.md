# 142 — An irrational polygon with nonergodic billiard flow

**Area:** Billiard dynamics / transport and ergodicity

**Status:** 🟡 PARTIAL

**Last checked:** 2026-10-13

## Problem statement

Does there exist a bounded simple polygon $`P\subset\mathbb R^2`$, with at least one interior angle an irrational multiple of $`\pi`$, whose unit-speed specular billiard flow is not ergodic?

More precisely, equip $`P\times S^1`$ with normalized Liouville measure

```math
d\mu=\frac{dx\,dy\,d\theta}{2\pi\,\mathop{\mathrm{Area}}\nolimits(P)}.
```

Straight motion inside $`P`$ is reflected at each side by equal incidence and reflection angles. Ignore the null set of trajectories hitting vertices. The requested example must have a measurable set $`A`$ invariant under this flow with $`0<\mu(A)<1`$.

The whole unit tangent bundle is used, rather than a single directional component of a rational-polygon unfolding.

## Application

Polygonal billiards model collision transport without curved focusing or dispersing walls. A counterexample would identify a mechanism preventing global mixing even when the reflection angles generate infinitely many directions.

## References

1. E. Gutkin, *Billiard dynamics: An updated survey with the emphasis on open problems* (2012), [Chaos 22, 026116](https://doi.org/10.1063/1.4729307), Problem 8. Explicit source of the existence question.
2. J. Chaika and G. Forni, *Weakly mixing polygonal billiards* (2026), [Annals of Mathematics 203, 695–735](https://doi.org/10.4007/annals.2026.203.3.1), main theorem. Establishes weak mixing for a dense $`G_\delta`$ set of nonrational polygons.
3. F. Arana-Herrera, J. Chaika and G. Forni, *Weak mixing in rational billiards* (2024), [arXiv:2410.11117](https://arxiv.org/abs/2410.11117), §6.2. Lists remaining ergodicity questions for nonrational polygons.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Weak-mixing-of-triangular-billiards-with-an-irrational-angle-October-5-2026/weak-mixing-triangular-billiards.pdf), result family 150 (2026). Statement locator: `Theorem 1.1, PDF page 1; Introduction theorem label thm:main, normalized measure immediately preceding.`.

## Status review

**Known cases:** Every irrational-angle Euclidean triangle is weakly mixing, hence ergodic, for the specified Liouville billiard measure. This rules out a nonergodic example with three sides.

**Remaining target:** Decide whether an irrational polygon with four or more sides can be nonergodic, or rule out all such examples.

**Statement comparison:** The weak-mixing theorem applies to every nondegenerate irrational-angle Euclidean triangle under precisely normalized position-times-uniform-direction Liouville measure, excluding the same null vertex-hit trajectories. Weak mixing implies ergodicity, so every three-side instance of the requested irrational polygon example is impossible; the existential question for larger polygons remains open.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-142) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/150.md). Family150 selected Lean docs formalize ergodicity of irrational triangles, which suffices for this partial exclusion; weak mixing is not the selected comparator claim. Comparator presence is not local verification. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/142-irrational-nonergodic-polygon.md).
