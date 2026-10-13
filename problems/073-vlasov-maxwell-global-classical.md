# 073. Large-data global classical solutions of relativistic Vlasov–Maxwell

**Area:** Kinetic theory and plasma physics

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Set $`\widehat v=v/\sqrt{1+|v|^2}`$. For nonnegative $`f_0\in C_c^\infty(\mathbb R_x^3\times\mathbb R_v^3)`$ and smooth finite-energy electromagnetic data with bounded derivatives satisfying
$`\nabla\cdot E_0=\int f_0\,dv`$ and $`\nabla\cdot B_0=0`$, does the system

```math
\partial_tf+\widehat v\cdot\nabla_x f+
(E+\widehat v\times B)\cdot\nabla_v f=0,
```



```math
\partial_tE=\nabla\times B-j,\quad
\partial_tB=-\nabla\times E,\quad
j=\int\widehat v f\,dv
```

have a classical solution for all $`t\ge0`$? Require the propagated Gauss constraints, finite field energy, and bounded particle-momentum support on every finite time interval. There is no smallness or symmetry assumption; units normalize the particle mass, charge and speed of light.

## Application

This is the self-consistent collisionless model for relativistic plasmas; momentum growth controls whether classical particle-field evolution remains predictive.

## References

- [Daniel Han-Kwan, Toan T. Nguyen and Frédéric Rousset, *Linear Landau Damping for the Vlasov-Maxwell System in R³* (Annals of PDE, 2025), introduction and references to the classical continuation theory](https://doi.org/10.1007/s40818-025-00217-z).
- [Luis Silvestre, *Regularity estimates and open problems in kinetic equations* (2022), kinetic regularity background](https://arxiv.org/abs/2204.06401).

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/paper.pdf), result family 362 (2026). Statement locator: `build/sections/introduction.tex, thm:global and eq:data`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** Exact one-species R3 relativistic Vlasov-Maxwell normalization, compact nonnegative smooth particle data, Cb-infinity finite-L2-energy fields and Gauss constraints. The global solution has compact phase-space support on each finite interval, so in particular bounded momentum support, preserves Gauss constraints and finite field energy; no size/symmetry restriction.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-073) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/362.md). docs/362 describes the full target. Its linked [comparator statement](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/ComparatorChallenges/VlasovMaxwell.lean) ends the theorem with `sorry`; that file is not a checked proof of the result. No local kernel replay or transitive axiom audit has been completed, so no AIM Lean-verified status is asserted. The [PR35 processing record](../research/solution_reviews/2026-10-13-yui-prs/073-pr35-review.md) records this source check.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/073-vlasov-maxwell-global-classical.md).
