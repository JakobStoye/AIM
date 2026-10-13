# AIM494: independent review of PR#85

Date:2026-10-13. [PR#85](https://github.com/MColbrook/AIM/pull/85), Kaiwen Jin. Reviewed head:`22d05af29e9febd77cceb59298889c1c8ad64d96`. Original target:`c9929805cece044705abaaebe1cebddac1ba11a6`, compared with the unchanged current statement.

**Decision: Solved.** Negative: degree-zero universality fails for the unrestricted multi-parameter interleaving target.

[PDF](../../solutions/494-degree-zero-interleaving-counterexample/paper/interleaving_counterexample.pdf) · [Source](../../solutions/494-degree-zero-interleaving-counterexample/paper/interleaving_counterexample.tex)

## Complete independent argument audit

Intersections of colimit images K_U and sums over proper supersets L_U intrinsically recover the finite coordinate-support multiset, independent of basis. Shift matching capped at three, together with the exceptional class, is a pseudometric on all modules. A uniform perturbation of arbitrary functions on arbitrary spaces induces inverse bijections of the actual H0 set colimits and shifted support containments, proving stability, including infinite/exceptional cases. No unwarranted identification with ambient connected components is used.

The four-parameter three-generator free-module pair has the stated inverse integer matrices, so its one-interleaving works over every field. The Hall obstruction forces support-matching cost three and the zero-shift obstruction excludes an interleaving below one. Thus a stable pseudometric exceeds interleaving distance. Lesnick1106.5305v4 Conjecture5.7 explicitly permits i=0; this admissible counterexample resolves the original universal target. Positive-degree variants remain separate questions, not a missing clause for this negative answer. Bjerkevik1609.02086v3 Example5.3 was compared directly with all birth vectors and matrices. Both bibliography entries and their journal/preprint metadata were checked.

## Package and PDF evidence

The complete manuscript, target comparison, README, disclosures and ancillary content were inspected. All bibliography keys resolve; cited primary theorem hypotheses were compared with their actual uses. Original supplied file hashes were verified at the pinned revision. The source rebuilt successfully with shell execution disabled; text and every rendered page agree with the supplied PDF, without missing content, unresolved references or material clipping. Numerical diagnostics and structural checks do not by themselves certify a theorem.

The earlier advisory triage is superseded by this completed independent AI argument audit, including the primary-source, uniform-quantifier and reproduction checks above. No concrete unresolved proof step or omitted original target clause was identified. Solved follows CONTRIBUTING.md's documented-independent-audit criterion. No human peer review or Lean verification is asserted. Original problem pages and statements are retained.
