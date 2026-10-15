# AIM 499: independent review of PR #93

Date: 2026-10-15. Reviewer: OpenAI Codex, independent AI review in the receiving repository; no human review or Lean verification is asserted.

PR: [#93](https://github.com/MColbrook/AIM/pull/93). Reviewed head: `9cd0516e31464c112e8d66a9c0bfd7e172e68f14`.

Outcome: **Solved** — Six-point counterexample to injectivity of the Rips shadow map.

Proof: [rips_shadow_counterexample.pdf](../../../research/resolved/499-rips-shadow-fundamental-group/paper/rips_shadow_counterexample.pdf). The original problem page, complete manuscript, target comparison, package README and other supplied explanatory material were compared.

## Mathematical audit

Recomputed the five rational squared-distance types, including the narrow threshold gap 499941/500000<1<500481/500000. The maximal triangles are exactly012,013,245,345. Sending1 to0 and5 to4 is a retraction carried by each simplex; linear interpolation therefore gives an actual strong deformation retraction to the cycle2,0,3,4. This is stronger than a homology calculation and proves pi1=Z. The first pair of affine triangles forms the stated convex quadrilateral by its two linear slice bounds; reflection/interchange of coordinates gives the second. Both contain the origin, so radial scaling contracts their union and the projected generator dies. The disconnected intersection in the abstract complex is not confused with the common axis segment in the shadow. Positive scaling and zero-coordinate padding preserve all strict inequalities and the actual maps.

## References and scope

Adamaszek–Frick–Vakili1602.04131v1 Conjecture7.2 explicitly asks pi1 injectivity in all dimensions, with no generic-position or full-affine-dimension premise. Chambers–de Silva–Erickson–Ghrist0712.0395v1 is correctly used only for the known planar theorem. Hatcher's circle fundamental group, deformation-retraction invariance and change-of-basepoint facts apply. The complete manuscript is self-contained for the finite geometry and both homotopies; no missing substantive external input was identified.

## Delivery checks

Read both explanatory Markdown documents and the complete checker/test source. The standard-library code uses exact Fraction arithmetic and enumerates every face; its cocycle is supplementary evidence, not a substitute for the homotopies. Root independently ran the checker and all3 tests successfully. Visually inspected all three PDF pages; equations, table, author/contact and references are present and unclipped.

Integrity clarification: exact canonical Git-blob checks confirm all six submitted payload hashes and byte counts. Initial worktree mismatches were Windows CRLF checkout conversion, addressed by an LF attribute for research/resolved. The manifest needs no content repair; the submitted PDF matches the rebuilt source.
