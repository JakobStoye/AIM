# AIM 398: independent review of PR #56

**Date:** 2026-10-13. **Reviewer:** OpenAI Codex, an independent AI argument audit during maintainer review; no human or Lean verification is asserted.

**PR:** [#56](https://github.com/MColbrook/AIM/pull/56). **Audited head:** `a44c2c3ff89538a75e814dda1b958bd8c688485f`. **Target revision:** `c9929805cece044705abaaebe1cebddac1ba11a6`.

**Direct proof:** [Source manuscript](https://github.com/MColbrook/AIM/blob/a44c2c3ff89538a75e814dda1b958bd8c688485f/research/solutions/398-parabolic-obstacle-counterexample/paper/obstacle_control_counterexample.tex).

All source sections, ancillary mathematical claims and bibliography entries were read and audited independently of the submission's own AI checks.

## Exact target

The target is universal over admissible smooth obstacles and initial states, allows any finite terminal time, and permits arbitrary admissible endpoint controls in $`H^1`$. One valid obstacle and initial state for which all such controls fail at every finite time therefore resolves the full target negatively.

## Complete independent argument audit

1. The polynomial obstacle has endpoints $`-3`$ and two maxima of height $`1`$. The smooth initial datum $`9x(1-x)`$ has zero boundary values and, with $`r=x(1-x)`$, exceeds the obstacle by $`81(r-1/6)^2+3/4`$ (source lines 118-125).
2. Truncating the stationary minimizer at height $`1`$ is admissible and cannot increase derivative energy. Uniqueness forces its values to be at most $`1`$. Continuity and the obstacle peaks then give value $`1`$ at both internal endpoints. Replacing the central segment by the constant $`1`$ is an admissible competitor that removes precisely the segment's derivative energy. Minimality therefore proves the stationary plateau (92-115).
3. Upward variations preserve the obstacle and boundary constraints and yield the weak heat supersolution inequality. The affine boundary lift is valid for $`H^1`$ controls; the proof uses time distributions and requires no classical free-boundary regularity (127-145).
4. The nonnegative sine on $`(1/3,2/3)`$, extended by zero, is in $`H^1_0`$. The state constraint gives both internal point traces at least $`1`$ almost everywhere. Integration by parts gives $`m'+k^2m\ge2k`$ for $`k=3\pi`$, and hence $`F'+k^2F\ge0`$ for the deviation moment $`F=m-2/k`$ (147-176).
5. Continuity into $`L^2`$ makes $`F`$ continuous. Mollification proves monotonicity of $`e^{k^2t}F(t)`$ including both temporal endpoints. The initial state is at least $`2`$ on the plateau, so $`F(T)\ge(2/k)e^{-k^2T}>0`$. Since the sine's squared norm is $`1/6`$, Cauchy-Schwarz gives the announced error bound $`2\sqrt6e^{-9\pi^2T}/(3\pi)`$ independently of endpoint controls (178-194).

## References and ancillary claims

All five references were checked for identity and use. Geshkovski's institutional dissertation record confirms author, title, Universidad Autonoma de Madrid and 2021; it is contextual rather than a proof premise. Pighin-Zuazua's publisher DOI record agrees with the 2018 citation, and its actual Section 7.3 distinguishes penalized control from exact obstacle control. Gerard's actual 2019 notes contain the cited Propositions 1.8.2, 1.8.5 and 1.8.7 at the stated pages, supplying continuous representatives and the endpoint characterization of $`H^1_0`$. Hunter's Proposition 3.22 supplies the truncation derivative. The AIM reference pins the correct statement. No additional external theorem is required by the novel argument.

Primary evidence: [dissertation record](https://repositorio.uam.es/bitstream/10486/696540/1/geshkovski_borjan.pdf), [Pighin-Zuazua](https://arxiv.org/html/1711.07678v4), [Gerard notes](https://www.imo.universite-paris-saclay.fr/~patrick.gerard/Distributions2019_Chap1,2,3.pdf), [Hunter Chapter 3](https://www.math.ucdavis.edu/~hunter/pdes/ch3.pdf).

## Decision

**Solved - negative answer by a complete independently audited counterexample.** No substantive gap or missing target clause remains. Approximate/asymptotic steering and other restricted obstacle geometries are not ruled out. Packaging checks are separate integration work.

## PDF consistency and layout

All rendered manuscript pages were inspected in the all-page contact sheet; title, author, theorem/proof structure, final conclusions and bibliography agree with the audited source. No clipped equations, blank pages or unresolved references were observed. The maintainer integration also checks the complete package hashes.

## Ancillary package content

The package README, exact-target comparison, AI-use disclosures, manifests and reproduction guidance were inspected. Their mathematical scope agrees with the manuscript, and none claims human or Lean verification. Maintainer integrity checks cover the listed files. There is no executable proof certificate or numerical experiment used as a proof premise.
