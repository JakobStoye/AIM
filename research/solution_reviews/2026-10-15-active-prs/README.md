# Individual solution PR reviews, 15 October 2026

Reviewed 82 open pull requests individually: 81 manuscript packages and one literature report covering 38 further targets. The review was by OpenAI Codex in separate review contexts and the coordinating maintainer session. It is an independent AI review, not human peer review or Lean verification. Closed requests were not reopened. The [pinned heads, replies and merge receipts](reviewed-pull-requests.json) identify exactly what was processed. PR 171, which arrived during the review, is included; this record does not claim to review later submissions.

The decisions cover 119 targets: **87 Solved, three Partial and 29 Solution claimed**. Of 81 manuscript submissions, 78 passed the documented complete argument audit, two provide partial progress, and one complete computational claim awaits full replay. Of 38 source comparisons, nine have published-resolution or complete independent argument evidence, one is partial, and 28 remain complete claims pending verification. A successful PDF build, plausible calculation or claim of formalization alone is insufficient for acceptance as a complete solution.

All original problem pages, IDs, statements, applications and bibliographies are retained. The [preservation receipt](preservation-check.json) compares those three sections with the admission snapshot. The README, CATALOG and RESOLVED are regenerated from the revised metadata; claims are listed separately from solved entries.

## Partial results and outstanding checks

- **AIM 040 / PR 170:** the disclosed randomized high-probability AMG construction does not establish an unconditional guarantee under the original unstated probability convention.
- **AIM 423 / PR 136:** the nonclosed ordinary-Sobolev restriction has a domain defect; the intended closed magnetic realization remains unresolved throughout the intermediate-field range.
- **AIM 458 / PR 171:** Section 3.3 omits the compatible fractional right-inverse hypotheses added by the Kunstmann–Weis erratum. Uniqueness among existing solutions and zero/small-noise cases are retained; full non-small-noise existence/dependence remains unproved by this submission. The package and manuscript carry a maintainer note.
- **AIM 571 / PR 122:** the geometry, all 618 inputs, deduplication, exact aggregation and controls were audited, but not all 608 complete Normaliz series were independently regenerated. This is a complete claim awaiting an essential replay, with no demonstrated mathematical gap.
- **AIM 241 / PR 170:** all 19 public custom Lean modules were inspected, with no explicit unproved assumption found. A frozen project, local kernel replay and transitive axiom receipt remain outstanding; see the [dependency inspection](241-dependency-inspection.md).
- Other claims in the table have a matching complete source claim, but the whole external proof was not independently recertified. A lack of completed verification is not recorded as an invented partial theorem.

## Scope-sensitive resolutions

AIM 366 refutes the literal broad smooth rapid-decay formulation and leaves the physically conservative formulation open. AIM 521 refutes the literal displayed persistence region; it is not a replacement full classification. AIM 042 has the explicit fixed floating-format cost model and disclosed precision dependence. AIM 142 has a [complete independent zero-frequency proof audit](142-independent-zero-frequency-review.md), including nonconvex polygon geometry; no stronger weak-mixing claim is certified. Follow the individual reports for other qualifications.

## Checks and editorial changes

Every submitted manuscript was read against the exact target, all ancillary content and proof-critical references were checked, and all PDF pages were visually inspected. All 81 submitted PDFs rebuilt safely with shell escape and automatic package installation disabled, with resolved reference keys. One rebuild differed only in “section A” versus “appendix A”; no mathematical content differed. Exact computational checks and corruption controls are recorded in the individual reports and the [verification receipt](verification-summary.json) and [850 package-integrity checks](package-integrity.json).

Canonical Git payload checks confirmed the original hashes for the 577, 499 and 458 packages; initial worktree mismatches were Windows CRLF conversion. LF attributes preserve those bytes. Math delimiters in the 540 package README and the 403 review were corrected to the repository format; the 540 integrity files were refreshed without changing its TeX or PDF. The 572 code docstring now links to the included manuscript instead of a missing file, and its embedded verification archive and manifests were refreshed. The submitted HHK bibliography title and PDF were correct and retained; an earlier erroneous title suggestion was explicitly corrected on the PR. The 458 maintainer note and missing 2013 erratum were added without claiming to repair the proof. The literature report uses the actual 15 October review date and corrected 394 source labels. External source PDFs and downloaded datasets are linked, not copied into AIM.

Validation passed: [59 full catalogue tests and 12 focused Windows tests](catalogue-tests.json), 850 package-integrity checks, and preservation of all 357 original statement/application/reference sections. The final staged tree is also checked for links, math formatting and generated-file freshness.

## Decisions

| AIM | PR | Decision | Outcome | Review |
| --- | --- | --- | --- | --- |
| 030 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solution claimed | Claim: affirmative existence in every dimension | [Review](170-scope-review_141_169.md#aim-030) |
| 040 | [#170](https://github.com/MColbrook/AIM/pull/170) | Partially resolved | Qualified randomized AMG construction; deterministic/unqualified target remains. | [Review](170-source-scope-root.md) |
| 042 | [#161](https://github.com/MColbrook/AIM/pull/161) | Solved | Selected bidiagonal triplets with fixed-format O(nk) work and gap-independent accuracy. | [Review](042-review.md) |
| 044 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solution claimed | Claim: affirmative bit-complexity bound | [Review](170-scope-review_141_169.md#aim-044) |
| 092 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solution claimed | Claim: affirmative dimension-free Poincare inequality | [Review](170-scope-review_141_169.md#aim-092) |
| 098 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solution claimed | Claim: full molecular charge-bound claim; threshold bridge checked, complete screening proof awaiting independent review. | [Review](170-source-scope-root.md) |
| 108 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solution claimed | Claim: affirmative uniqueness of the critical catenoid | [Review](170-scope-review_141_169.md#aim-108) |
| 110 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solution claimed | Claim: steklov counterexample claim; product reduction checked, underlying nodal-growth theorem awaiting independent review. | [Review](170-source-scope-root.md) |
| 111 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solution claimed | Claim: affirmative unbounded first Steklov multiplicity | [Review](170-scope-review_141_169.md#aim-111) |
| 112 | [#135](https://github.com/MColbrook/AIM/pull/135) | Solved | The affirmative result covers every admissible prescribed embedded boundary, including curves and filling codimension one. | [Review](112-review.md) |
| 123 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solution claimed | Claim: negative: smooth bracket-generating counterexample | [Review](170-scope-review_141_169.md#aim-123) |
| 125 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solution claimed | Claim: negative: branching analytic equiregular minimizers | [Review](170-scope-review_141_169.md#aim-125) |
| 126 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solution claimed | Claim: affirmative sharp Heisenberg isoperimetry | [Review](170-scope-review_141_169.md#aim-126) |
| 141 | [#141](https://github.com/MColbrook/AIM/pull/141) | Solved | A fixed five-dimensional polynomial STLC system has no finite jet guaranteeing STLC with the same bounded controls. | [Review](141-review.md) |
| 142 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solved | No irrational simple polygon with nonergodic full billiard flow, by the zero-frequency proof extension. | [Review](142-independent-zero-frequency-review.md) |
| 162 | [#126](https://github.com/MColbrook/AIM/pull/126) | Solved | An extreme solitary wave exists for the exact bidirectional Whitham model. | [Review](162-review.md) |
| 175 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solution claimed | Claim: affirmative | [Review](170-source-scope-review_90_114.md) |
| 185 | [#144](https://github.com/MColbrook/AIM/pull/144) | Solved | The stirred catalytic model poisons to CO almost surely at every site for every admitted iid law with positive CO density. | [Review](185-review.md) |
| 191 | [#146](https://github.com/MColbrook/AIM/pull/146) | Solved | For the specified Gaussian pinning model, strong disorder implies a strictly positive quenched–annealed critical-point shift. | [Review](191-review.md) |
| 193 | [#143](https://github.com/MColbrook/AIM/pull/143) | Solved | The Gaussian three-dimensional polymer moment threshold is a continuous strictly decreasing bijection onto [5/3,infinity). | [Review](193-review.md) |
| 195 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solution claimed | Claim: complete bosonic Laughlin gap claim awaiting independent argument and certificate review. | [Review](170-source-scope-root.md) |
| 214 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solution claimed | Claim: negative | [Review](170-source-scope-review_90_114.md) |
| 216 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solved | A measurable-conductor counterexample to smooth multiplier invariance of the flux domain. | [Review](170-source-scope-root.md) |
| 217 | [#147](https://github.com/MColbrook/AIM/pull/147) | Solved | One fixed pair of smooth bounded potentials violates the proposed unordered critical/subcritical heat-kernel comparison. | [Review](217-review.md) |
| 241 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solution claimed | Claim: two-profile counterexample claim; public dependency closure inspected, local Lean replay pending. | [Review](170-source-scope-root.md) |
| 250 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solution claimed | Claim: affirmative | [Review](170-source-scope-review_90_114.md) |
| 251 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solved | Affirmative | [Review](170-source-scope-review_90_114.md) |
| 252 | [#164](https://github.com/MColbrook/AIM/pull/164) | Solved | Total integrability of the Minkowski billiard in its own norm ball forces an inner-product norm, without an extra symmetry assumption. | [Review](252-review.md) |
| 298 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solution claimed | Claim: negative | [Review](170-source-scope-review_90_114.md) |
| 325 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solved | Negative | [Review](170-source-scope-review_90_114.md) |
| 328 | [#145](https://github.com/MColbrook/AIM/pull/145) | Solved | An exact positive-edge ultrametric three-leaf example for the symmetric twenty-state model violates the proposed Fitch accuracy inequality. | [Review](328-review.md) |
| 330 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solution claimed | Claim: affirmative | [Review](170-source-scope-review_90_114.md) |
| 338 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solution claimed | Claim: negative | [Review](170-source-scope-review_90_114.md) |
| 340 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solution claimed | Claim: negative | [Review](170-source-scope-review_90_114.md) |
| 342 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solution claimed | Claim: nonadditivity claim with exact finite artifact replay; complete analytic reduction awaiting independent review. | [Review](170-source-scope-root.md) |
| 348 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solution claimed | Claim: negative: finite-time Brownian branching explosion | [Review](170-scope-review_141_169.md#aim-348) |
| 361 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solution claimed | Claim: affirmative existence, claimed | [Review](170-source-scope-review_115_140.md) |
| 366 | [#140](https://github.com/MColbrook/AIM/pull/140) | Solved | Counterexample to rapid-decay continuation in the explicitly stated broad class of jointly smooth solutions, using a positive inverse-sixth-power tail from Gaussian data. | [Review](366-review.md) |
| 367 | [#133](https://github.com/MColbrook/AIM/pull/133) | Solved | Counterexample to the proposed universal square-root logarithmic error bound, with one fixed compactly supported small-BV initial datum. | [Review](367-review.md) |
| 376 | [#138](https://github.com/MColbrook/AIM/pull/138) | Solved | The conditional-density argument establishes a subsequential vanishing-center-of-mass-diffusion limit for the complete stated periodic three-dimensional FENE target. | [Review](376-review.md) |
| 379 | [#149](https://github.com/MColbrook/AIM/pull/149) | Solved | Universal strong-KPP uniqueness fails on a uniformly smooth connected unbounded domain in dimension 21. | [Review](379-review.md) |
| 380 | [#151](https://github.com/MColbrook/AIM/pull/151) | Solved | Critical Dirichlet spectral equality can coexist with a bounded positive strong-KPP equilibrium on a uniformly smooth unbounded domain. | [Review](380-review.md) |
| 383 | [#148](https://github.com/MColbrook/AIM/pull/148) | Solved | Finite-cluster mass is continuous and equals one at every finite positive onset of Flory gelation in the stated kernel class. | [Review](383-review.md) |
| 384 | [#152](https://github.com/MColbrook/AIM/pull/152) | Solved | Two disjoint disks admit two distinct bounded positive monostable Dirichlet equilibria for one admissible reaction. | [Review](384-review.md) |
| 390 | [#134](https://github.com/MColbrook/AIM/pull/134) | Solved | Local strong Hessian integrability at the requested exponent for the full planar Alexandrov class, implying the weak endpoint estimate. | [Review](390-review.md) |
| 392 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solution claimed | Claim: affirmative codimension-two transport-interface regularity | [Review](170-scope-review_141_169.md#aim-392) |
| 393 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solution claimed | Claim: affirmative codimension-two partial-transport regularity | [Review](170-scope-review_141_169.md#aim-393) |
| 394 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solution claimed | Claim: affirmative convex injectivity domains under weak MTW | [Review](170-scope-review_141_169.md#aim-394) |
| 396 | [#130](https://github.com/MColbrook/AIM/pull/130) | Solved | Uniform small-data L2 decay with exponent one half at the exact critical length fourteen pi, for every real energy-class datum in one common small ball. | [Review](396-review.md) |
| 400 | [#128](https://github.com/MColbrook/AIM/pull/128) | Solved | Concentric-ball optimality for the full radiative insulation law. | [Review](400-review.md) |
| 402 | [#159](https://github.com/MColbrook/AIM/pull/159) | Solved | The exact product-L2 logarithmic interpolation inequality holds for the two distinct Caputo orders and every initial pair. | [Review](402-review.md) |
| 403 | [#160](https://github.com/MColbrook/AIM/pull/160) | Solved | The norm control cost has liminf T log C_S(T,L) at least L^2/pi, strictly excluding the proposed L^2/4 coefficient. | [Review](403-review.md) |
| 404 | [#131](https://github.com/MColbrook/AIM/pull/131) | Solved | Whole-family local uniform vanishing-viscosity convergence for the exact quadratic local MFG in dimensions one through three, with initial vacuum allowed. | [Review](404-review.md) |
| 405 | [#127](https://github.com/MColbrook/AIM/pull/127) | Solved | A dimension-independent half-power vanishing-noise density rate. | [Review](405-review.md) |
| 411 | [#162](https://github.com/MColbrook/AIM/pull/162) | Solved | Admissibility for all strongly measurable bounded inputs implies zero-class admissibility and norm-continuous convolution states on every closed finite interval. | [Review](411-review.md) |
| 412 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solution claimed | Claim: negative, claimed | [Review](170-source-scope-review_115_140.md) |
| 413 | [#132](https://github.com/MColbrook/AIM/pull/132) | Solved | Schwartz Gaussian data give the exact requested homogeneous quarter-Sobolev norm inflation at nonzero arbitrarily short negative times. | [Review](413-review.md) |
| 416 | [#129](https://github.com/MColbrook/AIM/pull/129) | Solved | Uniform attraction to the positive equilibrium for every dimension, positive diffusivity triple and strictly positive compatible datum in the full stated mass range. | [Review](416-review.md) |
| 423 | [#136](https://github.com/MColbrook/AIM/pull/136) | Partially resolved | Verified domain clarification: the printed ordinary Sobolev restriction is nonclosed; the intended closed magnetic spectral problem is not settled. | [Review](423-review.md) |
| 424 | [#139](https://github.com/MColbrook/AIM/pull/139) | Solved | Purely real spectrum for every requested spherical strip width, real Robin parameter and integer mode. | [Review](424-review.md) |
| 425 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solved | Affirmative example | [Review](170-source-scope-review_115_140.md) |
| 429 | [#142](https://github.com/MColbrook/AIM/pull/142) | Solved | The constant-index transmission count has the sharp O(r^(d-1)) Weyl remainder at every sufficiently large exact radius. | [Review](429-review.md) |
| 433 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solved | Negative example for every p>2 and d>=3 | [Review](170-source-scope-review_115_140.md) |
| 441 | [#137](https://github.com/MColbrook/AIM/pull/137) | Solved | Counterexample to universal global regularity: finite-time gradient blowup for the actual coupled three-dimensional ionization system from smooth compactly supported optical data and zero nonnegative density, with one admissible positive photoionization coefficient. | [Review](441-review.md) |
| 446 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solution claimed | Claim: affirmative sharp bound, claimed | [Review](170-source-scope-review_115_140.md) |
| 455 | [#166](https://github.com/MColbrook/AIM/pull/166) | Solved | The entire smooth-transport variational SPDE class has a deterministic positive parabolic Hölder exponent on each positive-time strip. | [Review](455-review.md) |
| 457 | [#167](https://github.com/MColbrook/AIM/pull/167) | Solved | Local well-posedness holds at the exact inhomogeneous B^(-1/2)_(6,4) endpoint for all prescribed transport families in AIM 457. | [Review](457-review.md) |
| 458 | [#171](https://github.com/MColbrook/AIM/pull/171) | Partially resolved | Partial progress: conditional pathwise uniqueness and perturbative cases; full non-small-noise local theory has an unverified channel-calculus input. | [Review](458-review.md) |
| 460 | [#156](https://github.com/MColbrook/AIM/pull/156) | Solved | Positive integrable-growth harmonic profiles outside every admitted convex cone are proportional, including singular spectral measures. | [Review](460-review.md) |
| 461 | [#154](https://github.com/MColbrook/AIM/pull/154) | Solved | The specified relaxed infinity-fractional subsolution–supersolution comparison fails, even with identical smooth initial data. | [Review](461-review.md) |
| 462 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solution claimed | Claim: negative for every strict ellipticity pair, claimed | [Review](170-source-scope-review_115_140.md) |
| 463 | [#150](https://github.com/MColbrook/AIM/pull/150) | Solved | The proposed kernel-uniform full-order Sobolev estimate fails at every finite sufficiently large p for strict ellipticity pairs. | [Review](463-review.md) |
| 467 | [#153](https://github.com/MColbrook/AIM/pull/153) | Solved | For 1/2<s<1 and m>2 an existing bounded energy weak solution cannot have the requested global jointly continuous representative. | [Review](467-review.md) |
| 469 | [#155](https://github.com/MColbrook/AIM/pull/155) | Solved | The regional superlinear SKT strong solutions converge along one global subsequence to a genuine no-flux local weak solution for every fixed s>1. | [Review](469-review.md) |
| 473 | [#158](https://github.com/MColbrook/AIM/pull/158) | Solved | Every weak dual solution in the stated spatial-L1 class conserves its initial mass at every finite time. | [Review](473-review.md) |
| 474 | [#157](https://github.com/MColbrook/AIM/pull/157) | Solved | Every admitted complete manifold and positive point mass has a nonnegative distributional fractional porous-medium solution with the required positive-time continuity and initial trace. | [Review](474-review.md) |
| 478 | [#168](https://github.com/MColbrook/AIM/pull/168) | Solved | The critical stochastic SQG equation has the required pathwise unique global adapted H3 solution for the full specified nonlinear finite-noise class. | [Review](478-review.md) |
| 481 | [#169](https://github.com/MColbrook/AIM/pull/169) | Solved | Every stated compactly supported H1 probability datum admits one global fourth-order weak curve with bounded support on each finite horizon. | [Review](481-review.md) |
| 482 | [#163](https://github.com/MColbrook/AIM/pull/163) | Solved | The unrestricted finite-entropy renormalized reaction–diffusion uniqueness assertion is false. | [Review](482-review.md) |
| 485 | [#165](https://github.com/MColbrook/AIM/pull/165) | Solved | The full support-independent global C^(1,s) obstacle estimate holds for the stated integrable angular-density class. | [Review](485-review.md) |
| 499 | [#93](https://github.com/MColbrook/AIM/pull/93) | Solved | Six-point counterexample to injectivity of the Rips shadow map. | [Review](499-review.md) |
| 500 | [#94](https://github.com/MColbrook/AIM/pull/94) | Solved | A dimension-four counterexample refutes all-state irreducibility of the higher-dimensional clump dynamics. | [Review](500-review.md) |
| 501 | [#91](https://github.com/MColbrook/AIM/pull/91) | Solved | An integral optimum exists for every compactly supported integral codimension-one current, including noncycles. | [Review](501-review.md) |
| 504 | [#92](https://github.com/MColbrook/AIM/pull/92) | Solved | The exact exponential excursion-height rate is kappa*beta throughout the specified strict subcritical interval. | [Review](504-review.md) |
| 512 | [#95](https://github.com/MColbrook/AIM/pull/95) | Solved | The proposed join is the homotopy type of the ordinary strict spherical Rips complex throughout a nonempty interval after the first transition. | [Review](512-review.md) |
| 513 | [#96](https://github.com/MColbrook/AIM/pull/96) | Solved | An oriented flat five-manifold contradicts the universal centre-rank TC formula. | [Review](513-review.md) |
| 514 | [#97](https://github.com/MColbrook/AIM/pull/97) | Solved | Every connected sum of two closed oriented aspherical n-manifolds has maximal unreduced TC=2n+1 for n>=3. | [Review](514-review.md) |
| 520 | [#103](https://github.com/MColbrook/AIM/pull/103) | Solved | The unrestricted persistence-diagram space has no coarse embedding into Hilbert space for every p in the remaining interval[1,2]. | [Review](520-review.md) |
| 521 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solved | Negative for the displayed region | [Review](170-source-scope-review_90_114.md) |
| 525 | [#98](https://github.com/MColbrook/AIM/pull/98) | Solved | A positive-norm surface product has no degree-four class of the proposed TC weight. | [Review](525-review.md) |
| 529 | [#100](https://github.com/MColbrook/AIM/pull/100) | Solved | The normalized high-dimensional Betti numbers converge to an explicitly described nondegenerate law with all positive moments, excluding the proposed power-law tail. | [Review](529-review.md) |
| 531 | [#99](https://github.com/MColbrook/AIM/pull/99) | Solved | An exact integral chain certificate disproves the proposed all-k homology formula at k=5. | [Review](531-review.md) |
| 532 | [#102](https://github.com/MColbrook/AIM/pull/102) | Solved | The closed Rips complex of the2k-by-2k torus grid at half its diameter has the full conjectured wedge homotopy type for every k>=3. | [Review](532-review.md) |
| 537 | [#101](https://github.com/MColbrook/AIM/pull/101) | Solved | The prescribed no-finite-bar persistence fibre has the same F2 homology as the underlying simplicial complex. | [Review](537-review.md) |
| 540 | [#119](https://github.com/MColbrook/AIM/pull/119) | Solved | The infimum of full-tensor barrier parameters has quadratic growth in the hyperbolic radius, without any symmetry assumption. | [Review](540-review.md) |
| 547 | [#104](https://github.com/MColbrook/AIM/pull/104) | Solved | The proposed Morse quantity bounds the largest coordinate size of the canonical minimal persistence grid. | [Review](547-review.md) |
| 565 | [#105](https://github.com/MColbrook/AIM/pull/105) | Solved | A square pyramid is a counterexample to the proposed Macbeath-center asymmetry inclusion. | [Review](565-review.md) |
| 571 | [#122](https://github.com/MColbrook/AIM/pull/122) | Solution claimed | Claim: all-parameter half-integral collinear polygon formula via exact finite boundary-chain generating functions and Burnside, with an explicit Normaliz software dependency. | [Review](571-review.md) |
| 572 | [#125](https://github.com/MColbrook/AIM/pull/125) | Solved | Exact cubic count of entire Ehrhart functions for every requested half-integral polygon interior count, including integral polygons and period collapse. | [Review](572-review.md) |
| 577 | [#90](https://github.com/MColbrook/AIM/pull/90) | Solved | Affirmative norm convergence for the full repeated-GUE three-leg model. | [Review](577-review.md) |
| 578 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solved | Negative | [Review](170-source-scope-review_90_114.md) |
| 593 | [#106](https://github.com/MColbrook/AIM/pull/106) | Solved | Every arrangement in the question contains the required embedded rectangular grid; the proof also gives the stronger2k−1 sufficient threshold. | [Review](593-review.md) |
| 596 | [#108](https://github.com/MColbrook/AIM/pull/108) | Solved | The fractional flat-transversal theorem can be rounded to boundedly many actual flats for arbitrary concentric-fat convex bodies. | [Review](596-review.md) |
| 602 | [#123](https://github.com/MColbrook/AIM/pull/123) | Solved | A facial-cycle bound 100000 times genus times girth holds uniformly for both closed-surface types, including the stated noncellular embeddings. | [Review](602-review.md) |
| 610 | [#107](https://github.com/MColbrook/AIM/pull/107) | Solved | An explicit45-dimensional reflexive polytope violates the conjectured facet bound. | [Review](610-review.md) |
| 619 | [#170](https://github.com/MColbrook/AIM/pull/170) | Solved | Negative | [Review](170-source-scope-review_90_114.md) |
| 627 | [#124](https://github.com/MColbrook/AIM/pull/124) | Solved | A six-point periodic four-dimensional Costas array disproves the universal order restriction. | [Review](627-review.md) |
| 628 | [#110](https://github.com/MColbrook/AIM/pull/110) | Solved | There exists a closed connected PL four-manifold with odd Euler characteristic and a finite flag-no-square triangulation. | [Review](628-review.md) |
| 629 | [#111](https://github.com/MColbrook/AIM/pull/111) | Solved | Discreteness of the finite extrapolation set is equivalent to the full strong-PV conjugate condition. | [Review](629-review.md) |
| 630 | [#109](https://github.com/MColbrook/AIM/pull/109) | Solved | Every fixed extrapolation parameter outside[0,1] produces a relatively dense set in its full real or complex ambient space. | [Review](630-review.md) |
| 635 | [#114](https://github.com/MColbrook/AIM/pull/114) | Solved | Bounded pairwise intersections force a mod-two area four-cycle with area tending uniformly to zero. | [Review](635-review.md) |
| 640 | [#112](https://github.com/MColbrook/AIM/pull/112) | Solved | Elementary abelian2-groups deterministically refute the proposed uniform random coboundary-expansion assertion. | [Review](640-review.md) |
| 643 | [#115](https://github.com/MColbrook/AIM/pull/115) | Solved | Counterexample on a countable pure three-complex: maximum triangle degree three, coercive normalized upper Laplacian on the full weighted space, and trivial kernel. | [Review](643-review.md) |
| 644 | [#113](https://github.com/MColbrook/AIM/pull/113) | Solved | The reduced topological complexity is2 with probability tending to one along all sample sizes in the homogeneous lower model. | [Review](644-review.md) |
| 645 | [#116](https://github.com/MColbrook/AIM/pull/116) | Solved | Finite 32768-vertex three-ample simplicial complex with a simplicial retract onto a four-cycle. | [Review](645-review.md) |
| 647 | [#121](https://github.com/MColbrook/AIM/pull/121) | Solved | For every fixed full-dimensional convex polytope in every fixed dimension at least three, connectivity occurs exactly when the last isolated vertex disappears with high probability. | [Review](647-review.md) |
| 648 | [#118](https://github.com/MColbrook/AIM/pull/118) | Solved | Both noncritical spatial limits for the actual most-isolated point, with the stated tie rule. | [Review](648-review.md) |
| 649 | [#120](https://github.com/MColbrook/AIM/pull/120) | Solved | Rational nonregular first path homology vanishes with high probability throughout the requested exponent range above minus two-thirds. | [Review](649-review.md) |
| 650 | [#117](https://github.com/MColbrook/AIM/pull/117) | Solved | Rational nonregular first path Betti number CLT with true mean and variance for every requested density sequence, with variance asymptotic to the edge-count variance. | [Review](650-review.md) |

The [full decision ledger](decisions-integrated.json) records the verified progress, remaining targets and evidence boundaries. The [literature report](../../literature_reports/2026-10-15-prior-resolutions.md) retains the original source comparisons and snapshot badges.
