# AIM633: independent review of PR#38

Date:2026-10-13. [PR#38](https://github.com/MColbrook/AIM/pull/38), Kaiwen Jin. Reviewed head:`f69a9853cae1afc0f82ee4f466c5a53b30709f9a`. Original target:`c9929805cece044705abaaebe1cebddac1ba11a6`, compared with the unchanged current statement.

**Decision: Solved.** Affirmative: vertex-star decomposition on every uniform Freudenthal mesh for every polynomial degree k>=5.

[PDF](../../solutions/633-kaiwen-jin-freudenthal-potentials/paper/main.pdf) · [Source](../../solutions/633-kaiwen-jin-freudenthal-potentials/paper/main.tex)

## Complete independent argument audit

Shared Bernstein coefficients encode global continuity and integer barycentric gradients encode curl. Vertex support is tested on every incident tetrahedron, not just a chosen owner. The pivot-identity normal form has exactly the constraint row space; its canonical vectors span the entire kernel. The potential/curl correspondence gives the original divergence-free target.

Critical degree6 uses the N=6 exact reference with151959 variables, rank72519 and dimension79440. Clipping and template coverage handle every physical boundary/interior state within the declared radii, with both row-space inclusions and zero-extension faces checked. The725 nonlocal vectors have1450 exact local repair parts. N=1,...,4 use exact residuals and complementary nonzero modular minors; N=5,7 replay diagnoses transport, without replacing its uniform analytic proof.

For degrees>=7 capped gap types and symbolic sources encode unbounded parameters. The affine region inequalities are proved uniformly, including boundary splitting, pivot owners and all reverse face profiles. The dimension count is exact symbolic algebra, including transition degrees and the eventual identity. I inspected all proof-critical source and independently replayed verify_all.py under Python3.12.3/NumPy2.2.6/SymPy1.14 and g++13.3 with undefined-behavior sanitizer. It passed in216.27seconds, including105320 sources,631920 inequalities,210640 plane identities,59943 rules,17331 pivots and888 reverse profiles, critical identities/repairs and independent integer assembly. See633-certificate-replay.json. This is an exact certificate plus analytic uniform coverage, not Lean.

Both references were checked: Farrell-Mitchell-Scott, SIAMJScientificComputing46(2)(2024),A629-A644,2211.05494v2, DOI10.1137/22M1533943; and Ding-Ming-Yu-Zhu2609.25690v1,22Sept2026. The original no-boundary-condition scope and contextual inf-sup theorem are distinguished. No quantitative norm-stable decomposition beyond the original algebraic target is claimed.

## Package and PDF evidence

The complete manuscript, target comparison, README, disclosures and ancillary content were inspected. All bibliography keys resolve; cited primary theorem hypotheses were compared with their actual uses. Original supplied file hashes were verified at the pinned revision. The source rebuilt successfully with shell execution disabled; text and every rendered page agree with the supplied PDF, without missing content, unresolved references or material clipping. The633 font-extraction differences were normalized and checked individually; they do not change the mathematics. Numerical diagnostics and structural checks do not by themselves certify a theorem.

The earlier advisory triage is superseded by this completed independent AI argument audit, including the primary-source, uniform-quantifier and reproduction checks above. No concrete unresolved proof step or omitted original target clause was identified. Solved follows CONTRIBUTING.md's documented-independent-audit criterion. No human peer review or Lean verification is asserted. Original problem pages and statements are retained.

A further [fresh independent stress test](633-second-check.md) reconstructs the full argument and its source hypotheses separately and supports the same complete-target decision.
