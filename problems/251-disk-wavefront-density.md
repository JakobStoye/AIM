# 251 — Asymptotic density of reflected wavefronts in a disk

**Area:** Geometric optics / long-time propagation

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`D=\{x\in\mathbb R^2:|x|\leq1\}`$ and $`P\in\mathop{\mathrm{int}}\nolimits D\setminus\{0\}`$. Launch a unit-speed ray from $`P`$ in every direction, reflecting specularly at $`\partial D`$, and let $`W_t(P)`$ be their positions at time $`t`$. Is it true that

```math
\lim_{t\to\infty}\ \sup_{x\in D}\ \inf_{y\in W_t(P)}|x-y|=0
```

for every such $`P`$? The limit concerns each sufficiently late individual wavefront, not the union of wavefronts over time.

## Application

The statement would quantify eventual spatial coverage by an impulsive point source in an ideal circular reflecting cavity. Individual rays can remain confined by caustics, making simultaneous coverage a different issue from ray recurrence.

## References

1. E. Kang and O. Knill, *Density of Wave Fronts* (2026), [The Mathematical Intelligencer](https://doi.org/10.1007/s00283-026-10528-z); [author manuscript](https://arxiv.org/abs/2501.14611), §5.2. Explicitly asks about all noncentral sources in a circular billiard; proves density for flat tori and associated square billiards.
2. B. Albach et al., *Open problems in billiards and quantitative symplectic geometry* (2026), [arXiv:2602.12896](https://arxiv.org/abs/2602.12896), S. Tabachnikov's section, “Density of reflected wave fronts”. Identifies the circular-table case as unresolved.

## Status review

Reviewed 15 October 2026 against the original target in [PR #170](https://github.com/MColbrook/AIM/pull/170). Affirmative

[Proof or source](https://ahl.centre-mersenne.org/item/10.5802/ahl.42.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/170-source-scope-review_90_114.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** This requires an actual reduction: Theorem3.9 is not itself a disk-wavefront theorem. Fix source radius r>0 and use signed angular momentum/impact parameter b in J=[0,r/2], with a probability marginal having positive density there. A chord has length L(b)=2sqrt(1-b²), and the angular advance between collisions is2acos(b). In a suspension-torus trivialization the unit-speed frequencies are therefore (1/L(b),acos(b)/(pi L(b))). These are the frequencies in the report, and they must not be copied from the differently normalized displayed vector in Proposition3.7. Every nonzero integer combination is a nonconstant analytic function on a neighborhood of J: otherwise acos(b) would be an affine combination of sqrt(1-b²) and a constant, which differentiation excludes. Its derivative's zeros are isolated, so Theorem3.3 gives Keplerian shear with invariant sigma-algebra exactly the b-marginal.

For clarity, with torus coordinates u mod1 and theta mod2pi, the physical position is rotation(theta−2acos(b)u) times [(1−u)+u exp(2i acos(b))]. The seam at u=0,1 matches, so this is continuous on J×T². At fixed b its spatial image is the entire annulus b<=|x|<=1. Initial rays from P with the chosen b form a measurable Dirac-fibre measure with that fixed marginal; one orientation branch suffices, since |b|<=r/2 is physically available. The forward proof of Theorem3.9 convolves these Dirac fibres by small torus kernels. Torus translations preserve their Wasserstein distance, and shear applies to the smoothed densities; the already verified invariant sigma-algebra supplies the correct limit. Consequently the initial singular measure converges at every late real time to marginal×Haar. Since J contains arbitrarily small positive b, that limit pushes forward to a measure with full support on the closed disk. Every nonnegative continuous spatial bump around any point has positive limiting integral. A finite epsilon-cover then shows that every sufficiently late individual wavefront meets each covering ball, giving the required uniform spatial distance limit. Omitting b=0 as a null endpoint makes no difference. This proves the full target, with no central-source assertion or convergence rate.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Resolution-source report (2026-10-15):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-15-prior-resolutions.md#aim-251). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-13)

**Literature check:** Open in cited literature; no later resolution located.

The center must be excluded because its fronts periodically refocus. The cited density theorem for flat tori and square billiards does not establish the disk case. Searches included “density of wave fronts circle 2026 proof”, “reflected wavefronts billiard disk dense”, and the Kang–Knill title. A circular-table theorem on numbers of caustic cusps is a different assertion. No proof of the displayed limit was located.
