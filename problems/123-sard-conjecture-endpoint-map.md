# 123 — Sard conjecture for smooth bracket-generating distributions

**Area:** Nonholonomic control / sub-Riemannian geometry

**Status:** 🟠 SOLUTION CLAIMED

**Last checked:** 2026-10-15

## Problem statement

Let $`M`$ be a smooth $`n`$-manifold and let smooth vector fields $`X_1,\ldots,X_r`$ span a constant-rank distribution $`\Delta\subset TM`$. Suppose their iterated Lie brackets span $`T_xM`$ at every $`x`$. For fixed $`x_0`$, define the endpoint map

```math
E_{x_0}:u\longmapsto x_u(1),\qquad
\dot x_u(t)=\sum_{j=1}^r u_j(t)X_j(x_u(t)),\quad x_u(0)=x_0,
```

on the open subset of $`L^2([0,1];\mathbb R^r)`$ for which the trajectory exists. Call a control singular when the differential $`DE_{x_0}(u)`$ is not onto $`T_{E_{x_0}(u)}M`$.

Is the set of endpoints of all singular controls null for every smooth positive volume density on $`M`$, for every such distribution and every $`x_0`$?

## Application

Singular trajectories are the exceptional motions that evade ordinary first-order controllability tests in systems with nonholonomic constraints. The conjecture says their destinations occupy no volume.

## References

1. A. Belotto da Silva, A. Parusiński and L. Rifford, *Abnormal singular foliations and the Sard conjecture for generic co-rank one distributions* (2025), [Revista Matemática Iberoamericana 41, 1599–1628](https://doi.org/10.4171/RMI/1567), §1. States the general conjecture and proves specified rank and generic cases.
2. A. Belotto da Silva, A. Figalli, A. Parusiński and L. Rifford, *Strong Sard conjecture and regularity of singular minimizing geodesics for analytic sub-Riemannian structures in dimension 3* (2022), [Inventiones Mathematicae](https://doi.org/10.1007/s00222-022-01111-2), main theorems. Resolves an analytic three-dimensional setting.

## Status review

Reviewed 15 October 2026 against the original target in [PR #170](https://github.com/MColbrook/AIM/pull/170). Claim: negative: smooth bracket-generating counterexample

[Proof or source](https://arxiv.org/pdf/2609.05991v1) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/170-scope-review_141_169.md#aim-123). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Review boundary:** The public source claims the full target. Its complete argument has not received an independent audit here, and a peer-reviewed published resolution was not established by this review; the source-to-target comparison alone is not full proof verification.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Resolution-source report (2026-10-15):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-15-prior-resolutions.md#aim-123). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-08)

**Known cases:** The null-endpoint conclusion is established for rank-three distributions in dimension four and for the cited generic corank-one class.

**Remaining target:** The null-endpoint conclusion for every smooth bracket-generating distribution in the displayed class.

**Literature check:** Open in cited literature; no later resolution located.

The 2025 paper proves the result for rank-three distributions in dimension four and for generic corank-one distributions, while retaining the general smooth conjecture. Searches included “Sard conjecture smooth distributions solution 2025 2026” and “analytic minimal rank Sard conjecture 2026”. Analytic, minimal-rank and generic-distribution theorems have narrower quantifiers than the statement above.
