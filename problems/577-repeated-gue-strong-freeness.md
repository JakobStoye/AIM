# 577. Strong freeness for one random interaction on overlapping tensor legs

**Area:** Random matrices and quantum many-body systems

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`X_N`$ be a normalized Gaussian unitary ensemble matrix of size $`N^2`$, viewed as an operator on $`\mathbb C^N\otimes\mathbb C^N`$. Thus its independent diagonal entries have variance $`N^{-2}`$, and its upper-triangular entries are centered complex Gaussians with $`\mathbb E|(X_N)_{ab}|^2=N^{-2}`$. On $`(\mathbb C^N)^{\otimes3}`$ define

```math
A_N=X_N\otimes I_N,\qquad B_N=I_N\otimes X_N.
```

Both embeddings use exactly the same realization of $`X_N`$, in the indicated tensor-factor order.

Let $`s_1,s_2`$ be freely independent centered semicircular elements of variance one in their reduced free-product $`C^*`$-algebra. Is it true that, for every noncommutative polynomial $`P\in\mathbb C\langle x,y\rangle`$,

```math
\|P(A_N,B_N)\|_{\mathrm{op}}\xrightarrow[N\to\infty]{\mathbb P}\|P(s_1,s_2)\|?
```

Prove this operator-norm convergence or exhibit a polynomial for which it fails. This is the three-site, two-interaction case of the repeated-matrix question in [1, Section 5(2)], whose authors conjecturally expect freeness when the same local interaction is placed on different tensor legs.

## Application

Nearest-neighbor quantum Hamiltonians can use one local interaction repeatedly along a chain. Norm convergence would identify limiting spectral edges for polynomial observables in the overlapping interactions, giving information beyond an averaged eigenvalue distribution. For example, taking $`P(x,y)=x+y`$ would predict the norm $`2\sqrt2`$ for this three-site Hamiltonian.

## References

1. B. Collins and W. Yuan, [Strong convergence for tensor GUE random matrices](https://doi.org/10.3150/25-BEJ1933), *Bernoulli* **32**(3) (2026), 1812–1826. [Author manuscript](https://arxiv.org/abs/2407.09065), Sections 1.1 and 5, question (2).
2. C.-F. Chen, J. Garza-Vargas and R. van Handel, [A new approach to strong convergence II: The classical ensembles](https://arxiv.org/html/2412.00593v3), revised 6 June 2026. Section 9.4, Theorem 9.8.

## Status review

Reviewed 15 October 2026 against the original target in [PR #90](https://github.com/MColbrook/AIM/pull/90). Affirmative norm convergence for the full repeated-GUE three-leg model.

[Proof or source](../research/solutions/kaiwen-jin-577/paper/repeated_gue_three_legs.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/577-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** Every fixed complex noncommutative polynomial has the prescribed free-pair operator-norm limit in probability.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Known comparison:** The corresponding model with independent local GUE matrices has strong convergence results. The general tensor theorem in [2] allows arbitrary overlap patterns and resolves the independent-matrix tensor questions from [1]. Its construction expressly requires independent local matrices.

**Remaining target:** Establish the displayed limit when the two interactions reuse the same matrix, or show that their dependence changes the limiting norm. Independence cannot be inferred merely because the embeddings act on different pairs of sites.

The source's arXiv record remains version 1 of 12 July 2024; its Section 5 separately lists this repeated-matrix question. The June 2026 theorem was checked against that distinction. Searches through 24 September 2026 found no matching solution announcement or repository duplicate. Native Palomar, GitHub repository/issue, and Zenodo searches returned no matching records for the topic or source identifier.
