# 037. Kadison’s similarity problem

**Area:** Operator representations and stability

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

For every unital complex $`C^*`$-algebra $`\mathcal A`$, complex Hilbert space $`H`$, and bounded unital algebra homomorphism $`\pi:\mathcal A\to\mathcal B(H)`$, must there exist a bounded invertible $`S\in\mathcal B(H)`$ for which

```math
a\longmapsto S^{-1}\pi(a)S
```

is a $`*`$-homomorphism? Thus the transformed map must satisfy $`S^{-1}\pi(a^*)S=(S^{-1}\pi(a)S)^*`$ for every $`a\in\mathcal A`$. No complete-boundedness assumption is permitted.

## Application

The problem asks when a bounded operator representation can be put in adjoint-preserving coordinates. This concerns the mathematical stability of operator models and observable representations; it is not a claim of an immediate numerical procedure.

## References

1. E. Papapetros, [A new approach to the similarity problem](https://doi.org/10.1007/s43036-024-00363-4), Advances in Operator Theory (2024). Exact statement and reformulations.
2. G. K. Eleftherakis and V. I. Paulsen, [Hyperreflexivity of Von Neumann Algebras and Similarity of Finitely Generated $`C^*`$-Algebras](https://doi.org/10.1007/s00020-026-02832-2), Integral Equations and Operator Theory (2026), preliminaries. Further equivalences.
3. J. Peterson, [Open problems in operator algebras](https://www.math.uwaterloo.ca/~j37peter/problems.html), updated May 2026; Problem O.5.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Kadisons-similarity-theorem-through-uniform-derivation-estimates-September-23-2026/paper.pdf), result family 288 (2026). Statement locator: `build/sections/introduction.tex, thm:similarity`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** Exactly arbitrary unital complex C*-algebras, arbitrary complex Hilbert spaces and bounded unital algebra homomorphisms, without complete-boundedness assumption. The manuscript uses S*pi*S^-1 rather than S^-1*pi*S; replacing S by its inverse reconciles the conventions.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-037) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/288.md). docs/288 describes the full unrestricted similarity theorem via KadisonSimilarity. No local kernel log inspected. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/037-kadison-similarity.md).
