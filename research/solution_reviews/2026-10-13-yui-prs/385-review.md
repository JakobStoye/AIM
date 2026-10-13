# AIM 385: independent review of PR #53

**Date:** 2026-10-13. **Reviewer:** OpenAI Codex, an independent AI argument audit during maintainer review; no human or Lean verification is asserted.

**PR:** [#53](https://github.com/MColbrook/AIM/pull/53). **Audited head:** `1b29cbe43828ce9b9fa1eeff602756fba40ff879`. **Target revision:** `c9929805cece044705abaaebe1cebddac1ba11a6`.

**Direct proof:** [Source manuscript](https://github.com/MColbrook/AIM/blob/1b29cbe43828ce9b9fa1eeff602756fba40ff879/research/solutions/385-equal-speed-wentzell-wave-observability/paper/equal_speed_observability.tex).

All source sections, ancillary mathematical claims and bibliography entries were read and audited independently of the submission's own AI checks.

## Exact target

The proof retains the exact annulus, unit equal bulk/surface speeds, outer Dirichlet condition, outward annular normal and full bulk-plus-surface energy. Smooth compatible real solutions have energy one and observation tending to zero at every fixed finite time; this refutes the entire threshold-time assertion.

## Complete independent argument audit

1. The Bessel determinant solves the separated radial equation and vanishes at the outer circle. Its Wronskian gives $`F_r(2)=-1/\pi`$ exactly. The inner boundary equation is $`F_r(1)+(\lambda^2-m^2)F(1)=0`$, with the correct inner outward-normal sign (source lines 101-135).
2. The actual NIST turning-point formulas give inner values of order $`m^{-1/3}`$ and argument derivatives of order $`m^{-2/3}`$, with the stated Airy constants/signs. The fixed-angle Debye formulas give the outer values and phase at $`2m`$. Integrating the Bessel ODE over shifts $`|\lambda-m|\le Mm^{-1/3}`$ gives uniform absolute errors smaller than each leading scale. No uncontrolled asymptotic remainder is differentiated (138-231).
3. The determinant and radial derivative have scales $`m^{-5/6}`$ and $`m^{-1/6}`$. A sine addition identity selects in each consecutive pair of angular orders a phase factor bounded away from zero. A fixed sufficiently large frequency-shift interval makes the normalized boundary equation have opposite signs at its endpoints. The intermediate value theorem supplies exact roots and a uniform inner-value lower bound at those roots. No equidistribution assumption is needed (233-301).
4. The exact separated modes satisfy the bulk equation, both boundary equations and every compatibility condition. Initial surface kinetic energy alone is at least a fixed multiple of $`m^{1/3}`$, while the fixed outer derivative gives observation at most $`2T/\pi`$. Energy normalization therefore gives unit energy and $`O(Tm^{-1/3})`$ observation, contradicting any finite constant at each finite time (305-348). The circle measures and normalization constants check exactly.

## References and ancillary claims

All four bibliography entries were checked. The actual Baudouin-Darde-Ervedoza-Mercado paper has the stated authors/title/journal metadata and Theorems 2.2 and 2.4 cover the strict faster/slower cases. The actual Chorfi-Maniar-Morales survey leaves equality open. NIST provides the quoted Wronskian, Airy values/derivatives, Debye values and uniform turning-point expansions with the correct signs/prefactors; the related standard sections also exist. The pinned AIM reference is correct. The new subsequence, noncancellation and exact-root arguments are proved internally.

Primary evidence: [annular-wave paper](https://imar.ro/journals/Mathematical_Reports/Pdfs/2022/1-2/5.pdf), [survey](https://arxiv.org/html/2505.14795v1), [NIST 10.20](https://dlmf.nist.gov/10.20), [NIST 10.19](https://dlmf.nist.gov/10.19), [NIST 10.5](https://dlmf.nist.gov/10.5).

## Decision

**Solved - negative answer by a complete independently audited exact mode family.** No substantive gap or missing target clause remains. PDF/source consistency and repository checks are separate integration work.

## PDF consistency and layout

All rendered manuscript pages were inspected in the all-page contact sheet; title, author, theorem/proof structure, final conclusions and bibliography agree with the audited source. No clipped equations, blank pages or unresolved references were observed. The maintainer integration also checks the complete package hashes.

## Ancillary package content

The package README, exact-target comparison, AI-use disclosures, manifests and reproduction guidance were inspected. Their mathematical scope agrees with the manuscript, and none claims human or Lean verification. Maintainer integrity checks cover the listed files. There is no executable proof certificate or numerical experiment used as a proof premise.
