# 650. Central limit theorem for the first path Betti number

**Area:** Applied topology / probability
**Status:** ✅ SOLVED
**Last checked:** 2026-10-15

## Problem statement

Let $`G_n`$ be a random digraph on $`[n]`$, with every ordered edge $`(i,j)`$, $`i\ne j`$, present independently with probability $`p_n`$. Reciprocal edges are allowed. Assume

```math
np_n\longrightarrow\infty,\qquad n^{2/3}p_n\longrightarrow0.
```

Define the non-regular first path Betti number as follows. Over $`\mathbb Q`$, let $`\Lambda_k`$ be spanned by all vertex sequences $`[v_0,\ldots,v_k]`$, with the alternating deletion boundary $`\partial`$. Let $`A_k`$ be the span of sequences whose successive edges belong to $`G_n`$, and, for $`k\ge1`$, put

```math
\Omega_k=A_k\cap\partial^{-1}(A_{k-1}),\qquad
B_n=\dim_{\mathbb Q}\frac{\ker(\partial:\Omega_1\to\Omega_0)}{\partial\Omega_2}.
```

Repeated vertices are permitted, and no terms with consecutive repetitions are discarded by the boundary. Here $`\Omega_0=A_0`$. This is the rank of the source's integer non-regular path homology.

Does every sequence $`(p_n)`$ satisfying the two conditions obey

```math
\frac{B_n-\mathbb E B_n}{\sqrt{\mathop{\mathrm{Var}}\nolimits(B_n)}}
\xrightarrow{\ d\ }\mathcal N(0,1)?
```

## Application

A central limit theorem would support calibrated significance tests for path-homology features in directed networks without repeatedly computing homology for large collections of simulated graphs.

## References

1. T. Chaplin, [First Betti number of the path homology of random directed graphs](https://doi.org/10.1007/s41468-022-00108-3), Journal of Applied and Computational Topology **8** (2024), 1503–1549, Conjecture B.2, Section 3.1 and Propositions 4.2–4.4. [Preprint](https://arxiv.org/abs/2111.13493).

## Status review

Reviewed 15 October 2026 against the original target in [PR #117](https://github.com/MColbrook/AIM/pull/117). Rational nonregular first path Betti number CLT with true mean and variance for every requested density sequence, with variance asymptotic to the edge-count variance.

[Proof or source](../research/solutions/650-random-digraph-path-betti-central-limit/manuscript.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/650-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** Rational nonregular first path Betti number CLT with true mean and variance for every requested density sequence, with variance asymptotic to the edge-count variance.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

Conjecture B.2 explicitly proposes this limit in the stated density range. The source proves $`\mathbb E B_n\sim n(n-1)p_n`$ and concentration relative to this mean, but those results do not give a limit for fluctuations at the standard-deviation scale. Its numerical normality tests are evidence, not a proof. Current searches found no matching solution or announced proof.
