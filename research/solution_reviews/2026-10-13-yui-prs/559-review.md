# AIM559: independent review of PR#77

Date:2026-10-13. [PR#77](https://github.com/MColbrook/AIM/pull/77), Kaiwen Jin. Reviewed head:`8112a718b350324672c81c059624d5a561e20907`. Original target:`c9929805cece044705abaaebe1cebddac1ba11a6`, compared with the unchanged current statement.

**Decision: Solved.** Undecidability: universal positivity of univariate unnormalized trace polynomials admits no algorithmic decider.

[PDF](../../solutions/559-univariate-trace-decidability/paper/trace_decidability.pdf) · [Source](../../solutions/559-univariate-trace-decidability/paper/trace_decidability.tex)

## Complete independent argument audit

Stationary Hermite interpolants at0,...,k and the nonnegative separator h=product(x-j)^2 give a uniform nearest-node estimate: their error divided by h is bounded near every double zero and at infinity by the degree gap. Summing over arbitrary spectra gives |s-m|<=Ct with integer multiplicities and constants independent of matrix size. Zero padding introduces no trace of I. The finite polynomial variation estimate and the explicit polynomial penalty absorb that error. Integer positivity leaves2P(m)+(eta+1)^2 nonnegative; a negative integer value is realized by an exact diagonal node matrix with zero separator. Both directions of the computable reduction hold for every matrix size, including all-node spectra. This resolves the exact unnormalized decision problem, not just a normalized variant. A second fresh audit confirmed the reduction.

All three references were checked: Acevedo-Blekherman-Debus-Riener, The wonderful geometry of the Vandermonde map, FoCM26(2026),2005-2051, DOI10.1007/s10208-025-09718-6; Klep-Pascoe-Volcic2009.10081v2, JAlgebra579(2021),303-317; Hatami-Norine1005.2382v3, Section5, supplies the discrete sign-undecidability input. No normalized theorem is silently used for arbitrary unnormalized multiplicities.

## Package and PDF evidence

The complete manuscript, target comparison, README, disclosures and ancillary content were inspected. All bibliography keys resolve; cited primary theorem hypotheses were compared with their actual uses. Original supplied file hashes were verified at the pinned revision. The source rebuilt successfully with shell execution disabled; text and every rendered page agree with the supplied PDF, without missing content, unresolved references or material clipping. Numerical diagnostics and structural checks do not by themselves certify a theorem.

The earlier advisory triage is superseded by this completed independent AI argument audit, including the primary-source, uniform-quantifier and reproduction checks above. No concrete unresolved proof step or omitted original target clause was identified. Solved follows CONTRIBUTING.md's documented-independent-audit criterion. No human peer review or Lean verification is asserted. Original problem pages and statements are retained.
