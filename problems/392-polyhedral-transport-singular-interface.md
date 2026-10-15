# 392. Regularity of transport interfaces for nonconvex polyhedral targets

**Area:** Monge–Ampère PDEs / optimal transport

**Status:** 🔵 OPEN

**Last checked:** 2026-10-16

## Problem statement

Let $`n\ge3`$, let $`\Omega\subset\mathbb R^n`$ be a bounded domain, and let $`\Omega^*`$ be a bounded nonconvex polyhedral domain of the same volume. Here polyhedral means that its boundary is a finite union of flat polygonal facets. Let $`u`$ be a convex Brenier potential satisfying $`(\nabla u)_\#\mathbf1_\Omega=\mathbf1_{\Omega^*}`$, and set

```math
A=\{x\in\Omega:u\text{ is not differentiable at }x\},\qquad \Sigma=\overline A\cap\Omega.
```

Is there a relatively closed $`S\subset\Sigma`$ with $`\dim_H S\le n-2`$ such that $`\Sigma\setminus S`$ is locally a smooth embedded hypersurface? The empty singular set is allowed.

## Application

Optimal transport to complex polyhedral geometries underlies mesh generation and mass allocation. The conjecture predicts that discontinuities concentrate along smooth interfaces with only lower-dimensional junctions.

## References

1. S. Chen, Y. Li and J. Liu, *Optimal (partial) transport to non-convex polygonal domains*, preprint, version 4 (17 May 2026), Conjecture 5.1. [Full text](https://arxiv.org/html/2311.15655v4).
2. S. Chen and J. Liu, *Regularity of singular set in optimal transportation*, Inventiones Mathematicae 242 (2025), 1–44, introduction and principal regularity theorems. [DOI](https://doi.org/10.1007/s00222-025-01353-w); [preprint](https://arxiv.org/abs/2210.13841).

## Status review

**Resolution-source report (2026-10-16):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-16-prior-resolutions.md#aim-392). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-22)

**Literature check:** Open in cited literature; no later resolution located.

Conjecture 5.1 is posed after the authors prove the planar polygonal case. The 2025 Inventiones theorem treats a target made of two disjoint convex domains, not a general nonconvex polyhedral target. Searches through 22 September 2026 for higher-dimensional polyhedral transport interfaces and later versions of both papers located no proof or counterexample. This concerns the structure of the full-transport singular set, rather than the free boundary in partial transport.
