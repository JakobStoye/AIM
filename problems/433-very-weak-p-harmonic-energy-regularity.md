# 433. A nonlinear Weyl lemma at the minimal p-harmonic integrability threshold

**Area:** Degenerate elliptic PDEs and nonlinear potential theory

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15
## Problem statement

Let $`d\ge3`$, $`p>2`$, and $`\Omega\subset\mathbb R^d`$ be open. If $`u\in W^{1,p-1}_{\mathrm{loc}}(\Omega)`$ satisfies

```math
\int_\Omega |\nabla u|^{p-2}\nabla u\cdot\nabla\varphi\,dx=0\qquad(\varphi\in C_c^\infty(\Omega)),
```

must $`u\in W^{1,p}_{\mathrm{loc}}(\Omega)`$? Equivalently, must this distributional solution have a representative that is an ordinary weak p-harmonic function? The endpoint assumption ensures integrability of the flux but does not assume finite p-energy.

## Application

Nonlinear conduction laws naturally provide flux information before energy bounds. This question determines whether distributional stationary states automatically enter the usual finite-energy theory.

## References

1. P. Lindqvist, [Notes on the p-Laplace Equation](https://jyx.jyu.fi/bitstreams/2a8cbc94-58e9-4e75-94d6-0f1f5bc22ac1/download), second edition, University of Jyväskylä Report 161 (2017), §11, p. 93, “Very Weak Solutions.”
2. J. L. Lewis, [On very weak solutions of certain elliptic systems](https://doi.org/10.1080/03605309308820984), *Communications in PDE* **18** (1993), 1515–1537, higher-integrability results.

## Status review

Reviewed 15 October 2026 against the original target in [PR #170](https://github.com/MColbrook/AIM/pull/170). Negative example for every p>2 and d>=3

[Proof or source](https://ems.press/content/serial-article-files/51447) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/170-source-scope-review_115_140.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** The actual theorem supplies, for every p>1 other than2, a continuous planar distributional p-harmonic u in W^(1,p-1+epsilon), with infinite p-energy on every nonempty open subdomain. In particular for p>2 its local gradient and u belong to L^(p-1), and the nonlinear flux is L1. Theorem9.4 repeats the same claim; its strong-gradient limit and constitutive-inclusion passage have the stated interface. To match d>=3 choose Omega=B×(0,1)^(d-2) and U(x,z)=u(x), where B is the source ball. The weak gradient is (grad u,0); finite local product measure gives W^(1,p-1)_loc. For any smooth compactly supported test, integration over z produces a smooth compactly supported planar test; Fubini is valid for the L1 flux and reduces the equation exactly to the planar distributional equation. A product of compactly contained nonempty open sets has p-energy equal to its positive transverse volume times the infinite planar energy by Tonelli. Thus U is not locally W^(1,p), and changing representatives cannot change its weak gradient. There is no dimension or endpoint-integrability mismatch. This is an actual published counterexample plus an elementary extension, not an unreviewed new endpoint conjecture.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Resolution-source report (2026-10-15):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-15-prior-resolutions.md#aim-433). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-22)

**Literature check:** Open in cited literature; no later resolution located.

Lindqvist distinguishes the endpoint p−1 from the known p−epsilon theory. Searches for endpoint very weak p-harmonic regularity and 2025–2026 higher-integrability results found no theorem reaching this endpoint for all p and dimensions. Results for general elliptic systems with additional integrability do not settle the scalar endpoint.
