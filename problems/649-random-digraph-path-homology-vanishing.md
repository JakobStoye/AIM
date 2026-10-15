# 649. Vanishing threshold for first path homology of a random digraph

**Area:** Applied topology / random graphs
**Status:** ✅ SOLVED
**Last checked:** 2026-10-15

## Problem statement

Let $`G_n`$ be a random digraph on $`[n]`$, with each ordered edge $`(i,j)`$, $`i\ne j`$, present independently with probability $`p_n=n^\alpha`$; reciprocal edges are allowed.

Use non-regular path homology over $`\mathbb Q`$. More explicitly, let $`\Lambda_k`$ be the vector space on all vertex sequences $`[v_0,\ldots,v_k]`$, allowing repetitions, with the alternating deletion boundary $`\partial`$. Let $`A_k\subseteq\Lambda_k`$ be spanned by the sequences whose successive ordered edges belong to $`G_n`$, and, for $`k\ge1`$, set

```math
\Omega_k=A_k\cap\partial^{-1}(A_{k-1}),\qquad
\beta_1^{\mathrm{nr}}(G_n)=\dim_{\mathbb Q}
\frac{\ker(\partial:\Omega_1\to\Omega_0)}{\partial\Omega_2}.
```

No terms with repeated consecutive vertices are discarded when applying $`\partial`$; this specifies the non-regular convention. Here $`\Omega_0=A_0`$. This rational dimension is the rank of the integer path-homology group used in the source.

Is it true that, for every fixed $`-2/3<\alpha\le0`$,

```math
\Pr\{\beta_1^{\mathrm{nr}}(G_n)=0\}\longrightarrow1?
```

## Application

The threshold would identify when first path homology ceases to detect statistically unusual structure in directed-network data under an independent-edge null model.

## References

1. T. Chaplin, [First Betti number of the path homology of random directed graphs](https://doi.org/10.1007/s41468-022-00108-3), Journal of Applied and Computational Topology **8** (2024), 1503–1549, Conjecture B.1, Theorem 1.4 and Section 3.1. [Preprint](https://arxiv.org/abs/2111.13493).

## Status review

Reviewed 15 October 2026 against the original target in [PR #120](https://github.com/MColbrook/AIM/pull/120). Rational nonregular first path homology vanishes with high probability throughout the requested exponent range above minus two-thirds.

[Proof or source](../research/solutions/649-random-digraph-path-homology-vanishing/paper/path_homology_vanishing.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/649-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** Rational nonregular first path homology vanishes with high probability throughout the requested exponent range above minus two-thirds.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Known cases:** Vanishing is proved for $`\alpha>-1/3`$, whereas nonzero first Betti number occurs with high probability for $`-1<\alpha<-2/3`$. The source also proves vanishing when $`p_n\gg(\log n/n)^{1/3}`$.

**Remaining target:** Establish vanishing throughout $`-2/3<\alpha\le-1/3`$, or disprove the proposed exponent. The critical value $`\alpha=-2/3`$ is not included.

The regular first path Betti number is at most the non-regular one, so this assertion also implies the regular version posed in the same conjecture. These are kept as one problem. Current searches found no matching solution or announced proof.
