# 110. Linear growth of interior Steklov nodal volume

**Area:** Boundary-driven wave patterns

**Status:** 🟡 PARTIAL

**Last checked:** 2026-10-16

## Problem statement

Let $`(M,g)`$ be any smooth compact connected $`d`$-dimensional Riemannian manifold with smooth nonempty boundary, $`d\ge2`$. For a real nonzero Steklov eigenfunction

```math
\Delta_g u=0\text{ in }M,\qquad\partial_\nu u=\sigma u\text{ on }\partial M,\qquad\sigma>0,
```

write $`Z_u=\{x\in\mathop{\mathrm{int}}\nolimits M:u(x)=0\}`$. Prove or disprove that there are constants $`0<c_M\le C_M<\infty`$, independent of $`u`$ and $`\sigma`$, such that

```math
c_M\sigma\le\mathcal H^{d-1}_g(Z_u)\le C_M\sigma.
```

Only the nodal set inside the medium is counted; the boundary trace has a different-dimensional zero set.

## Application

Nodal interfaces partition the interior of a boundary-loaded vibrating medium. The proposed law predicts their total size directly from the boundary spectral frequency.

## References

1. B. Colbois, A. Girouard, C. Gordon and D. Sher, [Some recent developments on the Steklov eigenvalue problem](https://doi.org/10.1007/s13163-023-00480-3), Revista Matemática Complutense 37 (2024), Open Question 10.7: proposed interior and boundary nodal estimates; this entry takes the interior question.
2. C. D. Sogge, X. Wang and J. Zhu, [Lower bounds for interior nodal sets of Steklov eigenfunctions](https://arxiv.org/abs/1503.01091), preprint (2015), main theorem: nonsharp interior lower bound.
3. I. Polterovich, D. A. Sher and J. A. Toth, [Nodal length of Steklov eigenfunctions on real-analytic Riemannian surfaces](https://arxiv.org/abs/1506.07600), preprint (2015), main theorem: the analytic surface case.
4. X. Huang, Y. Sire, X. Wang and C. Zhang, [Sharp $`L^p`$ estimates for generalized Steklov eigenfunctions with an application to nodal sets](https://doi.org/10.4171/JST/598), Journal of Spectral Theory 16 (2026), §4 and Theorem 2: later boundary-nodal estimates.

## Status review

**Resolution-source report (2026-10-16):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-16-prior-resolutions.md#aim-110). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-08)

**Known cases:** The two-sided linear interior nodal-length estimate is established for real-analytic Riemannian surfaces.

**Remaining target:** The corresponding two-sided interior nodal-volume estimate for every smooth manifold in every dimension at least two.

**Literature check:** Open in cited literature; no later resolution located.

The analytic two-dimensional case is established. The 2024 survey asks for the general smooth estimates. The April 2026 paper improves estimates for boundary nodal sets and does not establish the displayed two-sided interior estimate.

**Search audit:** “Steklov interior nodal volume linear bound conjecture”; “Steklov eigenfunctions nodal 2026”; “smooth Steklov Yau nodal bounds”. Searches included proof, counterexample, and 2025–2026 updates. No later resolution of the stated problem was located; this is a literature review, not a proof of openness.
