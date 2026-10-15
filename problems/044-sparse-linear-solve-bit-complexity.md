# 044. Quadratic-scale bit complexity for well-conditioned sparse systems

**Area:** Sparse numerical linear algebra

**Status:** 🟠 SOLUTION CLAIMED

**Last checked:** 2026-10-15

## Problem statement

For each fixed positive integer $`c`$, let $`A\in\mathbb Q^{n\times n}`$ be nonsingular with $`m=\mathop{\mathrm{nnz}}\nolimits(A)`$ and $`\kappa_2(A)=\|A\|_2\|A^{-1}\|_2\le n^c`$, and let $`b\in\mathbb Q^n\setminus\{0\}`$. Assume all numerators and denominators in the input have at most $`c\lceil\log_2(2n)\rceil`$ bits.

Is there a randomized algorithm using $`\widetilde O(nm)`$ bit operations which, with probability at least $`0.99`$, outputs a rational $`\widehat x`$ satisfying

```math
\|\widehat x-A^{-1}b\|_2\le n^{-c}\|A^{-1}b\|_2?
```

Here $`\widetilde O`$ hides powers of $`\log n`$, with constants allowed to depend on fixed $`c`$. The input is given by its sparse nonzero list. The target is a finite-precision complexity bound, including all arithmetic costs.

## Application

For matrices with O(n) nonzeros, this asks for approximately quadratic bit work even when no graph or positive-definite structure is available. It targets the cost of reliable sparse solves in general scientific models.

## References

1. R. Peng and S. Vempala, [Solving Sparse Linear Systems Faster than Matrix Multiplication](https://arxiv.org/abs/2007.10254), SODA 2021, 504–521. Bit-complexity algorithm and polynomial-condition-number regime.
2. N. Amsel et al., [Linear Systems and Eigenvalue Problems: Open Questions from a Simons Workshop](https://arxiv.org/abs/2602.05394), 2026; Problem 2.10.

## Status review

Reviewed 15 October 2026 against the original target in [PR #170](https://github.com/MColbrook/AIM/pull/170). Claim: affirmative bit-complexity bound

[Proof or source](https://arxiv.org/pdf/2609.38101v1) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/170-scope-review_141_169.md#aim-044). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Review boundary:** The public source claims the full target. Its complete argument has not received an independent audit here, and a peer-reviewed published resolution was not established by this review; the source-to-target comparison alone is not full proof verification.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Resolution-source report (2026-10-15):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-15-prior-resolutions.md#aim-044). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-08)

**Literature check:** Open in cited literature; no later resolution located

Checked on **2026-09-08**. Problem 2.10 asks whether the O(n nnz(A)) arithmetic scale extends to finite precision. This entry fixes polynomial conditioning and input precision explicitly. No later bound meeting the target was located.

Searches included: `sparse linear systems n nnz bit complexity 2026`; `Peng Vempala sparse linear systems quadratic 2026`; `sparse linear solve word RAM nearly quadratic`. This is a documented literature check, not a certification that no solution exists.
