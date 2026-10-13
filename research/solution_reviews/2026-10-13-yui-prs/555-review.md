# AIM555: independent review of PR#46

Date:2026-10-13. [PR#46](https://github.com/MColbrook/AIM/pull/46), Kaiwen Jin. Reviewed head:`4f2a858c30c12c9e096ebaa7688c20e44d125721`. Original target:`c9929805cece044705abaaebe1cebddac1ba11a6`, compared with the unchanged current statement.

**Decision: Solved.** Affirmative: maximal finite-rate gain from nonadaptive randomization is one.

[PDF](../../solutions/555-nonadaptive-randomization-gain/paper/main.pdf) · [Source](../../solutions/555-nonadaptive-randomization-gain/paper/main.tex)

## Complete independent argument audit

For the finite lp block, the central-fiber error is controlled from below by the maximum dual distance of a coordinate to the measurement row space, even for nonlinear reconstruction. Approximating rows give a low-rank matrix with trace>=m(1-rho); Frobenius and rank Cauchy-Schwarz yield rho>=(1-sqrt(n/m))/(1+sqrt(n)m^(-1/q)), hence>=1/4 on the selected large blocks.

The fixed infinite operator is an l1 sum of lp blocks of sizes2^k into an l-infinity sum with weights2^(-sk), p=q/(q-1), s=1/q^2 and even q>=4. Exact prefix and block restriction give s<=a<=sq/2. The CountSketch allocation has cost<=n for every random seed; expected maximum is bounded by summing block errors against the l1 input norm. Finite continuous seed maps establish measurability. Hence b>=s+1/p and gain>=1-3/(2q)+1/q^2. KNU's symmetric-ball comparison gives b<=a+1 and finiteness, since an infinite b would contradict the deterministic upper exponent. Taking q to infinity proves the exact supremum. The operator does not change with budget.

All four references were checked: KNU2406.07108v2 Theorem1/Corollary14/Section6.3 (actual symmetric and continuous-information hypotheses); Kunsch-Wnuk2410.23067v2 Proposition4.1 (constants, repetition and budget); Krieg-Ullrich2602.02066v2 (normalization); and the pinned AIM555 target. The adaptive randomized error in the comparison only strengthens its use for the nonadaptive class.

## Package and PDF evidence

The complete manuscript, target comparison, README, disclosures and ancillary content were inspected. All bibliography keys resolve; cited primary theorem hypotheses were compared with their actual uses. Original supplied file hashes were verified at the pinned revision. The source rebuilt successfully with shell execution disabled; text and every rendered page agree with the supplied PDF, without missing content, unresolved references or material clipping. Numerical diagnostics and structural checks do not by themselves certify a theorem.

The earlier advisory triage is superseded by this completed independent AI argument audit, including the primary-source, uniform-quantifier and reproduction checks above. No concrete unresolved proof step or omitted original target clause was identified. Solved follows CONTRIBUTING.md's documented-independent-audit criterion. No human peer review or Lean verification is asserted. Original problem pages and statements are retained.
