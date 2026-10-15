# 251 — Asymptotic density of reflected wavefronts in a disk

**Area:** Geometric optics / long-time propagation

**Status:** 🔵 OPEN

**Last checked:** 2026-10-16

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

**Resolution-source report (2026-10-16):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-16-prior-resolutions.md#aim-251). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-13)

**Literature check:** Open in cited literature; no later resolution located.

The center must be excluded because its fronts periodically refocus. The cited density theorem for flat tori and square billiards does not establish the disk case. Searches included “density of wave fronts circle 2026 proof”, “reflected wavefronts billiard disk dense”, and the Kang–Knill title. A circular-table theorem on numbers of caustic cusps is a different assertion. No proof of the displayed limit was located.
