# 619. Spanning triangulated spheres with holes in surface triangulations

**Area:** Topological graph theory and rigidity

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`\mathbb S_g`$ be the sphere with $`g`$ pairwise disjoint open disks removed, with disjoint closures. A triangulation of a compact surface is an embedding of a finite simple graph, containing the surface boundary, such that every complementary face is an open disk bounded by a triangle.

The Euler genus of a closed orientable surface with $`h`$ handles is $`2h`$; that of a closed nonorientable surface with $`h`$ crosscaps is $`h`$.

Is it true that every triangulation $`G`$ of every closed connected surface of Euler genus $`g`$ contains a spanning subgraph that is a triangulation of $`\mathbb S_g`$? Spanning means retaining all vertices; no new vertices may be added.

## Application

Such spanning planar structures connect surface topology with rigidity in the plane. The conjecture strengthens the existence of spanning planar Laman subgraphs in surface triangulations.

## References

1. K. Clinch, S. Dewar, N. Fuladi, M. Gorsky, T. Huynh, E. Kastis, A. Nakamoto, A. Nixon and B. Servatius, [Triangulated Spheres with Holes in Triangulated Surfaces](https://doi.org/10.1007/s00454-026-00836-8), *Discrete & Computational Geometry* (2026), Conjecture 1.3. [arXiv:2410.04450](https://arxiv.org/abs/2410.04450).

## Status review

Reviewed 15 October 2026 against the original target in [PR #170](https://github.com/MColbrook/AIM/pull/170). Negative

[Proof or source](https://arxiv.org/pdf/math/0507592v1) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/170-source-scope-review_90_114.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** The author source explicitly supplies closed orientable genus-two triangulations on ten vertices. The first24-face dataset record was independently parsed. Every edge occurs in exactly two triangles, every vertex link is one connected cycle, the dual adjacency is connected, and consistent triangle orientations exist. It has10 vertices,36 edges and24 faces, hence Euler characteristic−2 and orientable genus2/Euler genus4. The finite-check receipt is619-source-example-check.json.

A sphere with four holes whose removed-disk closures are disjoint has four disjoint boundary circles. In an embedding of a finite simple graph that contains this boundary, each such circle is a vertex cycle of length at least three, and the cycles have disjoint vertex sets. Thus any such triangulation needs at least12 vertices. No spanning subgraph of the ten-vertex graph can qualify, regardless of how that subgraph is embedded. The original Clinch etal source was checked directly: it really uses pairwise-disjoint closures, finite simple graphs and the same Euler-genus4/four-hole Conjecture1.3; the counterexample is not obtained by strengthening the catalogue's definition beyond that source. This disproves the stated unrestricted conjecture, without changing the positive sufficiently-large-facewidth theorem.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Resolution-source report (2026-10-15):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-15-prior-resolutions.md#aim-619). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-24)

**Known cases:** The sphere, projective plane and torus cases are established. The source also proves the result for orientable surfaces when facewidth is sufficiently large, with a genus-dependent threshold.

**Remaining target:** Removing that hypothesis and treating arbitrary nonorientable surfaces remains open. The number of holes cannot be uniformly reduced below the Euler genus.
