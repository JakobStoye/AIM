# 030. SIC measurements in every finite dimension

**Area:** Quantum measurement and frame theory

**Status:** 🟠 SOLUTION CLAIMED

**Last checked:** 2026-10-15

## Problem statement

For every integer $`d\ge2`$, do there exist $`d^2`$ unit vectors $`\psi_1,\ldots,\psi_{d^2}\in\mathbb C^d`$ such that

```math
|\langle\psi_j,\psi_k\rangle|^2=\frac1{d+1}\quad(j\ne k)?
```

Such a family is a symmetric informationally complete set. The measurement effects $`E_j=d^{-1}\psi_j\psi_j^*`$ then satisfy $`\sum_jE_j=I_d`$. No group-covariance assumption is imposed.

## Application

A SIC gives a minimal, highly symmetric informationally complete measurement for reconstructing a quantum state. It is also a maximal equiangular line configuration and an optimal finite frame for several estimation criteria.

## References

1. M. Appleby, S. T. Flammia and G. S. Kopp, [A Constructive Approach to Zauner’s Conjecture via the Stark Conjectures](https://arxiv.org/abs/2501.03970), 2025. Conditional general construction.
2. C. Butucea, J. Johannes and H. Stein, [Locally Gentle State Certification for High Dimensional Quantum Systems](https://arxiv.org/abs/2602.04550), 2026, v3. Recent measurement application and discussion of SIC existence.

## Status review

Reviewed 15 October 2026 against the original target in [PR #170](https://github.com/MColbrook/AIM/pull/170). Claim: affirmative existence in every dimension

[Proof or source](https://hexagonmath.org/pdf/2610.00186v1) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/170-scope-review_141_169.md#aim-030). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Review boundary:** The public source claims the full target. Its complete argument has not received an independent audit here, and a peer-reviewed published resolution was not established by this review; the source-to-target comparison alone is not full proof verification.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Resolution-source report (2026-10-15):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-15-prior-resolutions.md#aim-030). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-08)

**Literature check:** Open in cited literature; no later resolution located

Checked on **2026-09-08**. Appleby–Flammia–Kopp explicitly require two number-theoretic/special-value conjectures for their all-dimension construction. The 2026 certification work continues to treat general SIC existence as conjectural. Neither numerical examples in many dimensions nor a conditional formula prove the universal assertion.

Searches included: `SIC POVM all dimensions 2026 conjecture`; `Zauner conjecture solved 2026`; `Constructive Approach Zauner Stark conjectures`. This is a documented literature check, not a certification that no solution exists.
