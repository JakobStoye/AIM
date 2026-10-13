# AIM519: independent review of PR#40

Date:2026-10-13. [PR#40](https://github.com/MColbrook/AIM/pull/40), Kaiwen Jin. Reviewed head:`8dc12e3f97d7c2230981ad0d46ab00aa06188bfd`. Original target:`c9929805cece044705abaaebe1cebddac1ba11a6`, compared with the unchanged current statement.

**Decision: Solved.** Affirmative: no additional universal Euclidean mechanical Lie identities, in every order.

[PDF](../../solutions/519-euclidean-mechanical-lie-algebra/paper/main.pdf) · [Source](../../solutions/519-euclidean-mechanical-lie-algebra/paper/main.tex)

## Complete independent argument audit

The exact free decomposition separates the ComMag part X from free Lie generators A and y_s. A sufficiently large marker decodes every ordered word branch, proving faithful degree-one action. For higher degree, the derivation A->y_x agrees with ad_x up to the explicit larger-label ideal. Projecting and retracting the new marker yields(m-1)u, so every nonzero graded ideal intersects X. The common realization kernel is graded.

Rooting the all-vertex tree joining operation gives the symmetric pre-Lie product. Bergeron-Loday injection passes to coinvariants by finite-group averaging in characteristic zero. Distinct edge-color jet indices reconstruct each unrooted tree and cannot cancel with another tree; arbitrary finitely prescribed jets are realized by polynomial potentials in sufficiently large dimension. Hence the kernel meets X trivially and is zero in every order. Finite rank tables are not the premise of this argument.

I inspected all associative/Lyndon, marker, canonical-tree, Poisson-sign, prime elimination and rational-polynomial routines, including replay controls. All30 standard-library tests passed. Full order18 audit/replay and80 direct polynomial crosschecks are separately recorded. All four references were checked: McLachlan-Murua1905.07554 Theorem1 gives the actual generators and product; Bergeron-Loday1004.1204v3 Theorem3.1 gives the injection; Chapoton-LivernetIMRN2001(8),395-408 gives the rooted-tree operad; Blanes-Casas-MuruaActa33(2024),1-161 is context. Published low-order computations are not represented as an all-order proof.

## Package and PDF evidence

The complete manuscript, target comparison, README, disclosures and ancillary content were inspected. All bibliography keys resolve; cited primary theorem hypotheses were compared with their actual uses. Original supplied file hashes were verified at the pinned revision. The source rebuilt successfully with shell execution disabled; text and every rendered page agree with the supplied PDF, without missing content, unresolved references or material clipping. Numerical diagnostics and structural checks do not by themselves certify a theorem.

The earlier advisory triage is superseded by this completed independent AI argument audit, including the primary-source, uniform-quantifier and reproduction checks above. No concrete unresolved proof step or omitted original target clause was identified. Solved follows CONTRIBUTING.md's documented-independent-audit criterion. No human peer review or Lean verification is asserted. Original problem pages and statements are retained.

The completed exact campaign reproduced all6705 columns through order18; independent saved-matrix replay passed all91 blocks. Direct rational Poisson differentiation passed80 calibrations and8 iterated-lowering cases. These checks supplement the all-order argument. See [reproduction record](reproduction-checks.json).
