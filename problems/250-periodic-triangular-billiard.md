# 250 — A periodic nonsingular billiard trajectory in every triangle

**Area:** Hamiltonian dynamics / ray transport

**Status:** 🟡 PARTIAL

**Last checked:** 2026-10-16

## Problem statement

Does every nondegenerate Euclidean triangle $`D\subset\mathbb R^2`$ admit a periodic specular billiard trajectory?

Precisely, find an integer $`m\geq2`$ and boundary points $`q_0,\ldots,q_{m-1}`$ in the relative interiors of sides, with consecutive points distinct, such that the segments $`[q_i,q_{i+1}]`$ lie in $`D`$ and the incoming and outgoing unit velocities at each $`q_i`$ are related by reflection across that side's tangent line. Indices are cyclic. Vertices and grazing collisions are excluded; the final position and direction must both repeat.

## Application

The question asks whether every triangular optical or mechanical cavity supports at least one exactly repeating ray path, including triangles with irrational angle ratios.

## References

1. R. E. Schwartz, *Obtuse Triangular Billiards I: Near the (2,3,6) Triangle* (2006), [Experimental Mathematics 15, 161–182](https://doi.org/10.1080/10586458.2006.10128961), introduction and main theorems. Formulates the general existence problem and treats a specified region of triangle space.
2. R. E. Schwartz and collaborators, [McBilliards research project](https://mcbilliards.sourceforge.net/), “About” and “Papers”. Explicit current expert problem statement and links to computer-assisted partial results.
3. A. Katok et al., *Problems on invariant measures and related topics*, [AIM workshop problem collection](https://aimath.org/WWN/measrigid/measrigid.pdf), §7, Question 46. States the unresolved obtuse-triangle case and contrasts rational polygons.

## Status review

**Resolution-source report (2026-10-16):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-16-prior-resolutions.md#aim-250). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-13)

**Known cases:** Periodic nonsingular trajectories are known for rational-angle triangles; acute triangles also have the classical orthic orbit.

**Remaining target:** Existence for every nondegenerate triangle, including arbitrary obtuse triangles with irrational angle ratios.

**Literature check:** Open in cited literature; no later resolution located.

Acute triangles have the classical orthic orbit, and rational-angle polygons have periodic trajectories. These results do not cover arbitrary obtuse triangles. Searches included “periodic every triangle billiards 2026 proof”, “obtuse triangular billiards existence solved”, and “McBilliards periodic triangles latest”. Papers realizing a given triangle as an orbit inside an ellipse reverse the roles of trajectory and table. No all-triangle theorem or aperiodic triangle was located.
