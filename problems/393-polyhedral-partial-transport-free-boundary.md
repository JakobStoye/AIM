# 393. Singular-set dimension of polyhedral partial-transport free boundaries

**Area:** Free-boundary PDEs / optimal transport

**Status:** 🟠 SOLUTION CLAIMED

**Last checked:** 2026-10-15

## Problem statement

Let $`n\ge3`$, and let bounded domains $`\Omega,\Omega^*\subset\mathbb R^n`$ be strictly separated by a hyperplane; assume $`\Omega^*`$ has boundary made of finitely many flat polygonal facets and may be nonconvex. Fix $`0<m<\min(|\Omega|,|\Omega^*|)`$. Minimize $`\int|x-y|^2\,d\gamma`$ over nonnegative measures of mass $`m`$ whose marginals are bounded by $`\mathbf1_\Omega dx`$ and $`\mathbf1_{\Omega^*}dy`$. Let $`U\subset\Omega`$ be the open active source region of the optimal plan and $`\mathcal F=\partial U\cap\Omega`$ its interior free boundary.
Must $`\mathcal F`$ be locally a smooth embedded hypersurface outside a relatively closed set of Hausdorff dimension at most $`n-2`$?

## Application

Partial transport selects which material to move when supply and demand need not be exhausted. Its free boundary separates moved from unmoved material and determines the stability of partial matching and resource allocation.

## References

1. S. Chen, Y. Li and J. Liu, *Optimal (partial) transport to non-convex polygonal domains*, preprint, version 4 (17 May 2026), Conjecture 5.2 and §1 definition of the active regions. [Full text](https://arxiv.org/html/2311.15655v4).
2. L. A. Caffarelli and R. J. McCann, *Free boundaries in optimal transport and Monge–Ampère obstacle problems*, Annals of Mathematics 171 (2010), 673–730, formulation and free-boundary regularity theory. [DOI](https://doi.org/10.4007/annals.2010.171.673).

## Status review

Reviewed 15 October 2026 against the original target in [PR #170](https://github.com/MColbrook/AIM/pull/170). Claim: affirmative codimension-two partial-transport regularity

[Proof or source](https://arxiv.org/pdf/2610.18756v1) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/170-scope-review_141_169.md#aim-393). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Review boundary:** The public source claims the full target. Its complete argument has not received an independent audit here, and a peer-reviewed published resolution was not established by this review; the source-to-target comparison alone is not full proof verification.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Resolution-source report (2026-10-15):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-15-prior-resolutions.md#aim-393). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-22)

**Literature check:** Open in cited literature; no later resolution located.

The 2026 source proves the two-dimensional polygonal result and explicitly leaves this higher-dimensional free-boundary conjecture. Searches through 22 September 2026 for partial transport nonconvex polytopes, Chen–Li–Liu Conjecture 5.2, and subsequent free-boundary regularity papers located no matching resolution. Smooth-target and convex-target results do not cover the stated nonconvex polyhedral geometry.
