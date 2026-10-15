# 446. The sharp Beurling–Ahlfors bound for planar elliptic systems

**Area:** Planar elliptic PDEs and singular integral operators

**Status:** 🟠 SOLUTION CLAIMED

**Last checked:** 2026-10-15
## Problem statement

For $`f\in C_c^\infty(\mathbb C;\mathbb C)`$, with planar Lebesgue measure $`dA`$, define

```math
\mathcal B f(z)=-\frac1\pi\lim_{\varepsilon\downarrow0}\int_{|z-w|>\varepsilon}\frac{f(w)}{(z-w)^2}\,dA(w).
```

For every $`1<p<\infty`$, is

```math
\|\mathcal B f\|_{L^p(\mathbb C)}\le(p^*-1)\|f\|_{L^p(\mathbb C)},\qquad p^*=\max\{p,p/(p-1)\}?
```

The proposed constant is the known lower bound for the operator norm; the question is the matching upper bound. The case $`p=2`$ is known.

## Application

The operator converts the antiholomorphic derivative of a planar potential into its holomorphic derivative. Its sharp norm controls distortion and integrability in Beltrami equations, a standard model for planar anisotropic elliptic systems.

## References

1. T. Iwaniec, [Extremal inequalities in Sobolev spaces and quasiconformal mappings](https://doi.org/10.4171/ZAA/37), *Zeitschrift für Analysis und ihre Anwendungen* **1** (1982), no. 6, 1–16, conjectured sharp derivative inequality.
2. R. Bañuelos, [Cotlar martingale transforms and related singular integrals](https://arxiv.org/abs/2604.09365), preprint (2026), §6.1, equation (6.1), and §6.4.

## Status review

Reviewed 15 October 2026 against the original target in [PR #170](https://github.com/MColbrook/AIM/pull/170). Claim: affirmative sharp bound, claimed

[Proof or source](https://arxiv.org/pdf/2609.28311v2) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/170-source-scope-review_115_140.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Review boundary:** Independent review of the complete external proof remains outstanding.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Resolution-source report (2026-10-15):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-15-prior-resolutions.md#aim-446). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-22)

**Literature check:** Open in cited literature; no later resolution located.

The 2026 paper explicitly retains the sharp norm as open and reviews nonsharp upper bounds. Searches for the Iwaniec conjecture and Beurling–Ahlfors sharp norm through the review date found no resolution of the complex-valued estimate for all p. Sharp inequalities for special input classes or martingale transforms do not give the full operator norm.
