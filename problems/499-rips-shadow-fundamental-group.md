# 499. Injectivity of the Rips shadow map on fundamental groups

**Area:** Applied topology and geometric reconstruction

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`X\subset\mathbb R^n`$ be a nonempty finite set, $`n\ge1`$, and $`r>0`$. Using Euclidean distances, form

```math
K=\mathop{\mathrm{VR}}\nolimits_{<}(X;r)=\{\sigma\subseteq X:\mathop{\mathrm{diam}}\nolimits(\sigma)<r\}.
```

Its shadow is the geometric union

```math
S(X;r)=\bigcup_{\sigma\in K}\mathop{\mathrm{conv}}\nolimits(\sigma)\subset\mathbb R^n.
```

The vertex inclusion extends affinely on each simplex to a continuous map $`p:|K|\to S(X;r)`$. For every base vertex $`x_0\in X`$, is

```math
p_*:\pi_1(|K|,x_0)\longrightarrow\pi_1(S(X;r),x_0)
```

injective? Thus, can a nontrivial loop in the abstract Rips complex become null-homotopic after projection onto its shadow?

This is Conjecture 7.2 of [1]. It concerns each finite sample at each fixed scale; no dense-sampling or vanishing-scale limit is assumed.

## Application

A Rips complex is built from pairwise distance information, while its shadow lies in the physical space containing the sample. Injectivity would ensure that projecting to this geometric representation does not erase a nontrivial fundamental-group class. This matters when relating combinatorial topology to geometric reconstructions of sampled spaces.

## References

1. M. Adamaszek, F. Frick and A. Vakili, [On Homotopy Types of Euclidean Rips Complexes](https://doi.org/10.1007/s00454-017-9916-5), Discrete & Computational Geometry **58** (2017), 526–542; [author preprint](https://arxiv.org/abs/1602.04131), Definitions 1.1–1.2, Theorem I and Conjecture 7.2.
2. E. W. Chambers, V. de Silva, J. Erickson and R. Ghrist, [Vietoris–Rips Complexes of Planar Point Sets](https://arxiv.org/abs/0712.0395), Discrete & Computational Geometry **44** (2010), 75–90. Planar shadow theorem and Proposition 5.4.
3. K. Kawamura, S. Majhi and A. Mitra, [The Shadow of Vietoris–Rips Complexes in Limits](https://arxiv.org/abs/2601.01359), preprint (2026), §4.3, Assumption (H) and Theorem 4.11.

## Status review

Reviewed 15 October 2026 against the original target in [PR #93](https://github.com/MColbrook/AIM/pull/93). Six-point counterexample to injectivity of the Rips shadow map.

[Proof or source](../research/resolved/499-rips-shadow-fundamental-group/paper/rips_shadow_counterexample.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/499-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** An admissible rational six-point Euclidean sample has abstract fundamental group Z and contractible affine shadow, in every ambient dimension at least three and every positive scale.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Known cases:** In the plane the shadow map induces an isomorphism on fundamental groups [2], also covering subsets of a line. In three-dimensional ambient space, [1] proves surjectivity; injectivity is the missing assertion.

**Remaining target:** Injectivity in all ambient dimensions at least three. The known failure of surjectivity in dimension four does not answer this question.

The 2026 limit theorem [3] concerns an inverse limit over scales after a direct limit over finite samples, under additional geometric hypotheses. It does not establish this fixed-sample assertion. No matching general resolution or announcement was found in the 23 September 2026 review.
