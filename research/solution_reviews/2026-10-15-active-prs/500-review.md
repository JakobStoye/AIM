# AIM 500: independent review of PR #94

Date: 2026-10-15. Reviewer: OpenAI Codex, independent AI review in the receiving repository; no human review or Lean verification is asserted.

PR: [#94](https://github.com/MColbrook/AIM/pull/94). Reviewed head: `a82eec0914141bb1e5bc5eb75f9abbf30e44bfec`.

Outcome: **Solved** — A dimension-four counterexample refutes all-state irreducibility of the higher-dimensional clump dynamics.

Proof: [cube_dynamics.pdf](../../../research/solutions/500-higher-dimensional-ising-clumps/paper/cube_dynamics.pdf). The original problem page, complete manuscript, target comparison, package README and other supplied explanatory material were compared.

## Mathematical audit

Proper normal links inherit acyclicity from the exact punctured-ball condition via suspension. Induction over normal codimension identifies the links as PL balls: embedded acyclic surfaces/three-manifolds have sphere boundary and are balls by low-dimensional PL Schoenflies. Thus every four-dimensional state is a PL manifold, not merely the specially constructed witness. Restricting a permitted cube-supported strong retraction proves its attachment set contractible. A maximal lower-dimensional attachment face would make the union link acquire nonzero reduced homology by Mayer–Vietoris, excluding such faces. The attachment is therefore a contractible union of cube facets, a three-ball in S3. Its complementary facet closure is another ball; replacing this boundary patch preserves the boundary homeomorphism type. Lickorish supplies an embedded compact contractible four-manifold with nontrivial boundary group. The hypersurface cubulation theorem carries its boundary by ambient isotopy to grid three-faces; connected open grid four-cells are then entirely inside/outside, and closedness/density recovers the whole manifold as finitely many whole cubes. Nested conical punctured balls factor through a contractible manifold half-ball and give the exact Euclidean regularity condition. Rescaling and translating pins a cube. The boundary-group obstruction is independent of rates, and finite jump histories cannot cross components.

## References and scope

Checked Lickorish's original Pacific J.Math208(2003)283–290, Theorem1 and p286: the boundary group is explicitly nontrivial. Checked Boege–Hinojosa–Verjovsky0905.4053v2 Theorem2.8, which concerns arbitrary smooth compact closed hypersurfaces, not just spherical knots, and gives the required ambient isotopy. Baryshnikov–Onaran provides the original all-state conjecture, not a theorem assumed in the refutation. Hatcher, Hatcher's 3-manifold notes and Rourke–Sanderson supply the stated duality, local PL and low-dimensional Schoenflies facts. No four-dimensional Schoenflies or classification theorem is assumed.

## Delivery checks

Read complete source, README and target comparison; all seven PDF pages visually inspected, including the full bibliography on the final page. The construction is an analytic existence proof and honestly supplies no explicit cube-coordinate list. One four-dimensional witness resolves the original universal assertion while leaving related dimension-three research open.
