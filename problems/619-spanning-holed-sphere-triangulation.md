# 619. Spanning triangulated spheres with holes in surface triangulations

**Area:** Topological graph theory and rigidity

**Status:** 🟡 PARTIAL

**Last checked:** 2026-10-16

## Problem statement

Let $`\mathbb S_g`$ be the sphere with $`g`$ pairwise disjoint open disks removed, with disjoint closures. A triangulation of a compact surface is an embedding of a finite simple graph, containing the surface boundary, such that every complementary face is an open disk bounded by a triangle.

The Euler genus of a closed orientable surface with $`h`$ handles is $`2h`$; that of a closed nonorientable surface with $`h`$ crosscaps is $`h`$.

Is it true that every triangulation $`G`$ of every closed connected surface of Euler genus $`g`$ contains a spanning subgraph that is a triangulation of $`\mathbb S_g`$? Spanning means retaining all vertices; no new vertices may be added.

## Application

Such spanning planar structures connect surface topology with rigidity in the plane. The conjecture strengthens the existence of spanning planar Laman subgraphs in surface triangulations.

## References

1. K. Clinch, S. Dewar, N. Fuladi, M. Gorsky, T. Huynh, E. Kastis, A. Nakamoto, A. Nixon and B. Servatius, [Triangulated Spheres with Holes in Triangulated Surfaces](https://doi.org/10.1007/s00454-026-00836-8), *Discrete & Computational Geometry* (2026), Conjecture 1.3. [arXiv:2410.04450](https://arxiv.org/abs/2410.04450).

## Status review

**Resolution-source report (2026-10-16):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-16-prior-resolutions.md#aim-619). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-24)

**Known cases:** The sphere, projective plane and torus cases are established. The source also proves the result for orientable surfaces when facewidth is sufficiently large, with a genus-dependent threshold.

**Remaining target:** Removing that hypothesis and treating arbitrary nonorientable surfaces remains open. The number of holes cannot be uniformly reduced below the Euler genus.
