# 391. Affine Bernstein rigidity in dimensions three through nine

**Area:** Fourth-order elliptic PDEs / geometric variational problems

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

For each integer $`3\le n\le9`$, let $`u\in C^4(\mathbb R^n)`$ have positive-definite Hessian everywhere. Define

```math
U^{ij}=\mathop{\mathrm{cof}}\nolimits(D^2u)_{ij},\qquad w=(\det D^2u)^{-(n+1)/(n+2)}.
```

If $`u`$ satisfies the affine maximal surface equation

```math
\sum_{i,j=1}^n U^{ij}\partial_{ij}w=0\quad\text{on }\mathbb R^n,
```

must $`u`$ be a quadratic polynomial with positive-definite quadratic part? This asks the entire-graph case of the affine Bernstein conjecture, without additional growth, bounded-Hessian or affine-metric completeness assumptions.

## Application

The equation is the Euler–Lagrange equation for affine surface area. Rigidity of entire profiles is a basic obstruction to singularity formation and loss of compactness in geometric optimization governed by this fourth-order PDE.

## References

1. N. S. Trudinger and X.-J. Wang, *The Monge–Ampère equation and its geometric applications*, Handbook of Geometric Analysis, vol. I (2008), 467–524, §6.3, conjecture following Theorem 6.4. [Author chapter](https://maths-people.anu.edu.au/~wang/publications/MA.pdf).
2. Y. Sun, C. Xing and R. Xu, *New non-quadratic Euclidean complete affine maximal type hypersurfaces via Calabi affine geometry*, preprint (26 August 2026), §1, equations (1.1)–(1.3) and Theorem 1.3. [arXiv:2608.25330](https://arxiv.org/abs/2608.25330).

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-affine-Bernstein-theorem-in-dimensions-three-through-nine-September-24-2026/main.pdf), result family 353 (2026). Statement locator: `build/main.tex, thm:main`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** For n=3,...,9 the theorem classifies smooth positive-Hessian affine maximal graphs complete in induced Euclidean metric. An entire graph is Euclidean-complete because its metric dominates Euclidean distance and the graph is closed. The C4 target bootstraps locally to smoothness: the positive cofactor matrix makes the w equation elliptic on compact subsets, and det(D2u)=w^(-(n+2)/(n+1)) plus local Monge-Ampere regularity iterates Schauder regularity. No growth or affine completeness is needed.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-391) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/353.md). docs/353 covers the smooth Euclidean-complete graph theorem via AffineBernstein. The C4 bootstrap and target comparison are mathematical implications, not a locally checked Lean theorem. No local kernel log inspected. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/391-affine-bernstein-entire-low-dimensions.md).
