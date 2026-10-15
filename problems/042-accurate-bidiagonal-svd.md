# 042. Accurate selected bidiagonal singular vectors in O(kn) work

**Area:** Numerical linear algebra and low-rank approximation

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`B\in\mathbb R^{n\times n}`$ be upper bidiagonal, with singular values $`\sigma_1(B)\ge\cdots\ge\sigma_n(B)\ge0`$. Given $`k`$ distinct requested indices $`j_1,\ldots,j_k\in\{1,\ldots,n\}`$, construct a floating-point algorithm that computes corresponding singular triplets $`(\widehat\sigma_i,\widehat u_i,\widehat v_i)`$ in $`O(kn)`$ arithmetic operations, with unit vectors, nonnegative estimates, and

```math
|\widehat\sigma_i-\sigma_{j_i}(B)|\le C\epsilon n\|B\|_2,
```



```math
\|B\widehat v_i-\widehat\sigma_i\widehat u_i\|_2\le C\epsilon n\|B\|_2,
```



```math
\|B^T\widehat u_i-\widehat\sigma_i\widehat v_i\|_2\le C\epsilon n\|B\|_2,
```



```math
|\widehat u_i^T\widehat u_j|\le C\epsilon n,\qquad
|\widehat v_i^T\widehat v_j|\le C\epsilon n\quad(i\ne j).
```

Here $`\epsilon`$ is unit roundoff and $`C`$ is a universal constant, independent of singular-value gaps or clusters; assume $`\epsilon n`$ is small and exclude overflow and underflow. A repeated value permits any orthonormal basis of its singular subspace.

## Application

Dense SVD algorithms reduce their input to bidiagonal form. A reliably accurate linear-work-per-vector final stage would improve selected SVD computations used for compression and scientific data analysis.

## References

1. B. Großer and B. Lang, [An O(n²) algorithm for the bidiagonal SVD](https://doi.org/10.1016/S0024-3795(01)00398-6), Linear Algebra and its Applications 358 (2003), 45–70. Relatively robust representation approach.
2. O. A. Marques, J. W. Demmel and P. B. Vasconcelos, [Bidiagonal SVD Computation via an Associated Tridiagonal Eigenproblem](https://doi.org/10.1145/3361746), ACM Transactions on Mathematical Software 46 (2020); Appendix B.
3. N. Amsel et al., [Linear Systems and Eigenvalue Problems: Open Questions from a Simons Workshop](https://arxiv.org/abs/2602.05394), 2026; Problem 3.8.

## Status review

Reviewed 15 October 2026 against the original target in [PR #161](https://github.com/MColbrook/AIM/pull/161). Selected bidiagonal triplets with fixed-format O(nk) work and gap-independent accuracy.

[Proof or source](../research/solutions/042-selected-bidiagonal-directions/paper/main.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/042-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** Ordered values, both residual equations and both orthogonality estimates hold in the explicitly stated fixed-format floating-arithmetic model; precision costs are disclosed.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located

Checked on **2026-09-08**. Problem 3.8 still asks for the combined work, residual and orthogonality guarantees. This entry makes the intended selected-SVD task explicit by requiring both singular-vector equations and accuracy at the requested ordered indices; the source displays only the first residual equation. Earlier O(n²) titles alone do not establish reliable implementations for clustered spectra. No later solution was located.

Searches included: `bidiagonal O(kn) 2026 SVD`; `bidiagonal SVD MR 2026`; `bidiagonal SVD residual orthogonality open problem`. This is a documented literature check, not a certification that no solution exists.
