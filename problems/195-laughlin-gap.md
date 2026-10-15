# 195. The bosonic Laughlin contact-interaction gap

**Area:** Fractional quantum Hall physics

**Status:** 🟠 SOLUTION CLAIMED

**Last checked:** 2026-10-15

## Problem statement

Let $`\mathcal P_N`$ be the symmetric complex polynomials in $`z_1,\ldots,z_N`$ of total degree at most $`N(N-1)`$, with inner product

```math
\langle F,G\rangle=\pi^{-N}\int_{\mathbb C^N}\overline{F(z)}G(z)e^{-\sum_j|z_j|^2}\,dz.
```

On the full polynomial space define the orthogonal projection

```math
(P_{ij}F)(z)=F\left(z_1,\ldots,\frac{z_i+z_j}{2},\ldots,\frac{z_i+z_j}{2},\ldots,z_N\right).
```

The sum $`H_N=\sum_{i<j}P_{ij}`$ preserves $`\mathcal P_N`$. Its kernel contains the Laughlin polynomial $`\prod_{i<j}(z_i-z_j)^2`$. Does there exist $`c>0`$ such that, for every $`N\ge2`$,

```math
\inf\big(\sigma(H_N|_{\mathcal P_N})\setminus\{0\}\big)\ge c?
```

This fixes the contact-interaction normalization and the angular-momentum cutoff while letting particle number grow.

## Application

The gap protects a correlated quantum Hall fluid against low-energy perturbations. The same model describes rapidly rotating ultracold bosons restricted to the lowest Landau level.

## References

1. N. Rougerie, [On the Laughlin function and its perturbations](https://arxiv.org/abs/1906.11656), Séminaire Laurent Schwartz (2018–2019), Appendix A, Conjecture A.1 and the contact-interaction formula following (A.6): exact gap question at filling one half.
2. N. Rougerie and J. Yngvason, [Quantum Hall phases of cold Bose gases](https://arxiv.org/abs/2209.14215), Encyclopedia of Condensed Matter Physics, second edition (2024), discussion of the yrast curve and spectral-gap conjecture: physical interpretation and later assessment.

## Status review

Reviewed 15 October 2026 against the original target in [PR #170](https://github.com/MColbrook/AIM/pull/170). Claim: complete bosonic Laughlin gap claim awaiting independent argument and certificate review.

[Proof or source](https://github.com/Shencongli/bosonic-laughlin-spectral-gap/blob/fda5da170a1a87c2a7a8e970254c7073c228a99a/paper.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/170-source-scope-root.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Review boundary:** Independent review of the analytic reduction and every required exact/interval certificate remains outstanding.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Resolution-source report (2026-10-15):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-15-prior-resolutions.md#aim-195). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-13)

**Literature check:** Open in cited literature; no later resolution located.

The selected case is the full lowest-Landau-level contact interaction, with the degree cutoff used in Rougerie’s conjecture. Results for truncated pseudopotentials or thin-cylinder limits change the Hamiltonian or geometry. The 2024 paper “The charge gap is greater than the neutral gap in fractional quantum Hall systems” (arXiv:2410.11645) explicitly still treats the full pseudopotential gap as open; comparing two gaps does not prove a positive lower bound.

**Search audit:** “Laughlin spectral gap conjecture full contact pseudopotential proof 2025 2026”; “2410.11645 Haldane conjecture neutral gap”. Searches included later proofs, counterexamples, and 2025–2026 updates. No resolution matching the stated hypotheses was located.
