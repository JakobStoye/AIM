# 537. Betti numbers of a persistence fiber with no finite bars

**Area:** Applied topology and inverse persistent homology

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`K`$ be a finite connected simplicial complex, and use homology with coefficients in $`\mathbb F_2`$. Write $`\beta_q(K)=\dim_{\mathbb F_2}H_q(K;\mathbb F_2)`$. Define a graded barcode $`D_K`$ containing one infinite bar born at $`1`$ in degree zero, and $`\beta_q(K)`$ infinite bars born at $`2`$ in each degree $`q\ge1`$. There are no finite bars in any degree.

Let $`m`$ be the number of distinct finite endpoints in $`D_K`$, so $`m=1`$ if all positive-degree Betti numbers vanish, and $`m=2`$ otherwise. Set $`I=[1,m+1]`$. A filter is an assignment $`f:K\to I`$ to all nonempty simplices such that $`f(\tau)\le f(\sigma)`$ whenever $`\tau`$ is a face of $`\sigma`$. Its sublevel complexes are

```math
K_t(f)=\{\sigma\in K:f(\sigma)\le t\}.
```

Let $`\mathop{\mathrm{PH}}\nolimits(f)`$ be the graded barcode of ordinary, unreduced persistent homology of these sublevel complexes, and give

```math
F_K=\{f:\mathop{\mathrm{PH}}\nolimits(f)=D_K\}
```

the subspace topology inherited from $`I^{|K|}`$.

Is it true that, for every such $`K`$ and every $`q\ge0`$,

```math
\dim_{\mathbb F_2}H_q(F_K;\mathbb F_2)=\beta_q(K)?
```

This is an equality of Betti numbers. The filters range over assignments to all simplices; restricting to filters determined solely by vertex values changes the question.

## Application

The fiber describes the collection of filtrations that produce the same persistence summary. Its topology measures ambiguity in reconstructing data from persistent homology and informs the study of optimization constrained by a target barcode.

## References

1. J. Leygonie and G. Henselman-Petrusek, [Algorithmic reconstruction of the fiber of persistent homology on cell complexes](https://doi.org/10.1007/s41468-024-00165-w), Journal of Applied and Computational Topology **8** (2024), 2015–2049, §§1–1.2 and Conjecture 1, p.2044; [preprint](https://arxiv.org/abs/2110.14676).
2. H. A. Harrington, U. Tillmann and M. Torras-Pérez, [The fiber of multiparameter persistent homology for simplicial complexes](https://arxiv.org/abs/2608.04640v1), version 1 (2026), Theorem 5.3 and Proposition 5.9.

## Status review

Reviewed 15 October 2026 against the original target in [PR #101](https://github.com/MColbrook/AIM/pull/101). The prescribed no-finite-bar persistence fibre has the same F2 homology as the underlying simplicial complex.

[Proof or source](../research/solutions/537-persistence-fiber-betti-numbers/paper/persistence_fiber.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/537-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** Every finite simplicial complex and every degree, including ordinary H0 and the empty-complex convention in the target, is covered.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

Reference [1] proposes the equality from computed examples. The formulation uses the connected-complex setting preceding the conjecture and its stated $`\mathbb F_2`$ computations, with the compact filter interval normalized as in §1.2.

Reference [2] proves polyhedral structure and a bound on the dimension of a fiber. Its multigraded Betti numbers describe the persistence module; those results do not compute the homology Betti numbers of $`F_K`$ required here. Results for continuous functions on geometric trees also have a different domain. No matching solution announcement was found as of the check date.
