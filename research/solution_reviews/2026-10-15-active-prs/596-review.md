# AIM 596: independent review of PR #108

Date: 2026-10-15. Reviewer: OpenAI Codex, independent AI review in the receiving repository; no human review or Lean verification is asserted.

PR: [#108](https://github.com/MColbrook/AIM/pull/108). Reviewed head: `b0f3f707f434785784adc3792bfd93a4c2a5597a`.

Outcome: **Solved** — The fractional flat-transversal theorem can be rounded to boundedly many actual flats for arbitrary concentric-fat convex bodies.

Proof: [main.pdf](../../../research/solutions/aim-596-fat-convex-transversals/paper/main.pdf). The original problem page, complete manuscript, target comparison, package README and other supplied explanatory material were compared.

## Mathematical audit

The measure-grouping lemma repeatedly selects a body of minimum outer radius. Groups share overlap mass at least $`\varepsilon^2/2`$ with their distinguished body; a second-moment bound on their incidence indicators gives at most $`2/\varepsilon^2`$ groups. Every member of a group has radius at least the distinguished radius, which is exactly the one-sided size control used subsequently.

For a group at scale $`s`$, an approximate flat whose distance to every body is at most a fixed multiple of $`s`$ can be replaced by a bounded set of parallel exact transversals. In the orthogonal quotient, interpolate from a nearby point in the body toward the center by $`s/(2R)`$. Its inner ball contains a uniformly sized ball in a uniformly bounded region, regardless of how large $`R/s`$ is. A fixed grid hits all such balls. This explicitly removes any need for a global maximum/minimum radius ratio.

The spherical induction is checked at the level of actual sets. Gnomonic projection on the prescribed cap preserves convexity and has the stated Lipschitz bounds; the spherical convex hull of an $`s`$-neighborhood stays inside the $`2s`$-neighborhood. Radial projection away from a pole remains compact, properly hemispherical and fat with a uniform multiplicative loss. The submitted sine estimates handle both an outer cap smaller than its pole distance and the complementary case. No projection is applied through a body containing a pole.

For great-$`j`$-sphere weak nets, large-radius bodies are pierced by a fixed finite cap net. For small-radius groups, probes that hit the distinguished body can be rotated by at most its scale to contain its center. Projection lowers the great-sphere dimension by one on the remaining bodies, preserving a fixed fatness constant; bodies containing a pole are hit separately. The induction terminates at the antipodal-pair case. Its approximate lifted probes are rounded to exact great-sphere probes with the local gnomonic estimate. The affine version translates conditioned flats through the distinguished center, fattens, projects radially, invokes the spherical result in one lower dimension, lifts and applies the Euclidean exact rounding. Every resulting bound depends only on the displayed parameters.

Finally the published fractional-Helly theorem and the abstract fractional-transversal theorem provide a finite-support fractional cover of bounded total mass. Normalization gives the incidence probability required by the new weak-net theorem, yielding a bounded actual transversal family. Families smaller than the local-condition threshold are handled directly. The proof therefore closes the rounding problem for arbitrary sizes, not just translates, equal-radius families or a fractional relaxation.

## References and scope

The exact concentric-fat definition, admissible dimensions and fractional-Helly input were checked in [Jung–Pálvölgyi's published primary article](https://link.springer.com/article/10.1007/s00454-026-00852-8), Theorem5 and Theorem22. [Alon–Kalai–Matoušek–Meshulam's author manuscript](https://web.math.princeton.edu/~nalon/PDFS/akmm6.pdf), Theorem8(i), gives the cited bounded fractional transversal with the required (p,q) and fractional-Helly assumptions; finite support is part of that convention and can also be obtained from finitely many incidence patterns. The new exact rounding and weak-net induction are proved in the submitted text.

## Delivery checks

All seven PDF pages, all projection and recurrence formulas, complete ancillary prose and target comparison were read and visually inspected. The output is an existence proof with explicit finite recurrences, not a numerical estimate or Lean certificate.
