# AIM517: independent review of PR#39

Date:2026-10-13. [PR#39](https://github.com/MColbrook/AIM/pull/39), Kaiwen Jin. Reviewed head:`c5902207726a88e2f2922c7ffb1189272e755cdb`. Original target:`c9929805cece044705abaaebe1cebddac1ba11a6`, compared with the unchanged current statement.

**Decision: Solved.** Affirmative: sharp local elliptic widths with exponent1/(d-1) for arbitrary measurable symmetric elliptic coefficients in d=2,3.

[PDF](../../solutions/kaiwen-jin-517/paper/main.pdf) · [Source](../../solutions/kaiwen-jin-517/paper/main.tex)

## Complete independent argument audit

Sobolev slicing supplies good radii. A-harmonic energy minimization gives the Gram comparison with ordinary harmonic extension; ellipticity controls radial growth by the tangential form. Spherical-harmonic count sums give the required d=2,3 lower bounds. Inversion and log-determinant integration yield the complete product estimate. Singular inner Gram matrices make the determinant bound immediate; unique continuation is not an implicit assumption.

Caccioppoli/Rellich make restriction compact in the energy quotient. Applying the Gram bound to right singular vectors and using monotonicity gives the individual bound with the correct squared singular-value normalization. Harmonicity cancels the cutoff mixed terms. A finite ball cover and partition of unity produce approximation spaces including local constants with the required dimension budget. No smooth coefficient or radial/separable assumption enters the analytic theorem.

All23 tests passed, including independent high-precision exponentials, scaling/interface invariances and invalid inputs. All40 radial and80 matrix cases passed; shell-splitting error<=1.26e-12 and both comparison excesses strictly negative. These are supplemental floating-point checks. The runner refreshes its scalar summary even when --output is elsewhere; that change was confined to scratch and is not an original-manifest discrepancy. All eight references were checked: AIM, Ma2311.08761v3, Ma-Scheichl-Dodwell2103.09545v3, Li-WangAnnMath152(2000),645-658, Bandtlow-ChuBLMS41(2009),903-915, Axler-Bourdon-Ramey2nded, GuermondMATH6612025 and MelroseLecture14(2017). The new determinant improvement is internally derived; no stronger rough-coefficient result is assumed.

## Package and PDF evidence

The complete manuscript, target comparison, README, disclosures and ancillary content were inspected. All bibliography keys resolve; cited primary theorem hypotheses were compared with their actual uses. Original supplied file hashes were verified at the pinned revision. The source rebuilt successfully with shell execution disabled; text and every rendered page agree with the supplied PDF, without missing content, unresolved references or material clipping. Numerical diagnostics and structural checks do not by themselves certify a theorem.

The earlier advisory triage is superseded by this completed independent AI argument audit, including the primary-source, uniform-quantifier and reproduction checks above. No concrete unresolved proof step or omitted original target clause was identified. Solved follows CONTRIBUTING.md's documented-independent-audit criterion. No human peer review or Lean verification is asserted. Original problem pages and statements are retained.

A further [fresh independent stress test](517-second-check.md) reconstructs the full argument and its source hypotheses separately and supports the same complete-target decision.
