# AIM 417: independent review of PR #57

**Date:** 2026-10-13. **Reviewer:** OpenAI Codex, independent AI argument audit during maintainer review. This is not independent human review or Lean verification.

**PR:** [#57](https://github.com/MColbrook/AIM/pull/57). **Audited head:** `fff30eeb072395341d9944e4c75d5267b770f3b8`. **Target revision:** `c9929805cece044705abaaebe1cebddac1ba11a6`.

**Direct proof:** [Small-time controllability without polynomial reachable neighborhoods](https://github.com/MColbrook/AIM/blob/fff30eeb072395341d9944e4c75d5267b770f3b8/research/solutions/417-polynomial-reachable-growth-counterexample/paper/main.tex).

## Exact target

The proposed five-dimensional system is polynomial, has zero drift at the origin, and uses two measurable controls in the prescribed cube. Its triangular equations give global absolutely continuous solutions. A single system in dimension five refutes the universal assertion for dimensions at least three. Both interior reachability and failure of every polynomial inner ball must be established; the manuscript supplies separate arguments for them.

## Complete argument audit

1. For a closed triple-integrator trajectory put $`f=x_3`$, $`A=\int f'^4`$, $`q=ff''+f'^2/3`$ and $`E=\int q^2`$. The six zero endpoint jets and bounded third derivative follow directly from the dynamics. Integration by parts gives $`\int ff''f'^2=-A/3`$, hence $`E=\int f^2f''^2-A/9`$ (source lines 120–147).
2. The bounds $`|f''|\le t`$, $`|f'|\le t^2/2`$, $`|f|\le t^3/6`$ follow by successive integration. Clipping $`f`$ at $`\varepsilon=2A/(3t^6)`$ shows that the low-amplitude region contributes at most $`A/2`$. For the logarithmic weight above that level, a second integration by parts gives $`\int qf'^2w(f)=A_{\mathrm{hi}}/3`$. Cauchy–Schwarz gives $`E\ge A/[36\log^2(t^9/(4A))]`$. The threshold level sets contribute nothing because $`f'=0`$ almost everywhere on each fixed level set. All compositions are absolutely continuous (148–206).
3. A negative fourth-axis endpoint has displacement $`E-\int x_5^2f'^4`$. Since $`|x_5|\le t`$, negativity implies $`E<t^2A`$ and therefore $`0<-x_4<t^{11}e^{-1/(6t)}/4`$. This bound increases with duration, so it covers endpoints reached in any time at most $`t`$ and every measurable control (209–227).
4. The quintic corrections in the concentrating profile match its first three jets exactly. On the central interval the profile $`s^{3/4}`$ has $`q=0`$ and $`f'^4=81/(256s)`$. Changes of variables in the endpoint pieces cancel the scale factors in both quartic integrals. Thus $`E_\eta=E_0>0`$, whereas $`A_\eta=A_0+(81/256)\log(c/\eta)`$ tends to infinity. Each fixed profile has a finite third-derivative norm and the required endpoint regularity (237–291).
5. Raising $`x_5`$ to a small fixed positive value, applying a sufficiently concentrated loop, and returning $`x_5`$ to zero produces an exact negative fourth-coordinate interval. A loop with $`x_5=0`$ produces a positive interval. Scaling the amplitude by $`\sigma^3/(1+\|f'''_\eta\|_\infty)`$ makes both controls admissible. These intervals are attained exactly, with all other coordinates zero (293–335).
6. The Gram matrix of the three endpoint moment polynomials is positive definite and supplies linear steering to every sufficiently small target in the other four coordinates. The resulting fourth displacement is a continuous polynomial $`F(z)`$ with $`F(0)=0`$. Prepending the scalar loop with displacement $`y_4-F(z)`$ therefore attains every sufficiently small full target. The total duration is less than $`t`$, proving interior reachability, not merely accessibility (336–372).
7. The negative-axis bound is smaller than every fixed positive multiple of $`t^N`$ at sufficiently small time. A negative-axis point inside any proposed polynomial ball is consequently unreachable. This defeats all $`C,T,N`$ and finishes the exact counterexample (374–380).

## References and ancillary claims

All four bibliography entries were checked. Jafarpour's authorship, title, journal, 58 (2020), 425–446 and DOI match publisher metadata; the pinned preprint poses the same quantitative conjecture. Beauchard–Marbach's actual Section 6 gives the stated $`1/9`$ lower bound and unknown optimal constant. Hunter's cited Appendix 3.A, Theorems 3.60 and 3.62, printed page 79, gives the absolutely continuous calculus used. The AIM link pins the correct target. No additional external theorem is needed for the profile construction, Gram matrix or integral estimates. The critical-constant consequence follows from the same profiles and is not an extra premise.

Primary evidence: [Jafarpour](https://arxiv.org/html/1604.02432v7), [Beauchard–Marbach](https://arxiv.org/html/2608.28582v1), [Hunter Appendix 3.A](https://www.math.ucdavis.edu/~hunter/pdes/ch3A.pdf).

## Decision

**Solved — negative answer by a complete independently audited counterexample.** No missing target clause or substantive gap remains. Package hashes, PDF consistency and repository validation are separate integration checks.

## PDF consistency and layout

All rendered manuscript pages were inspected in the all-page contact sheet; title, author, theorem/proof structure, final conclusions and bibliography agree with the audited source. No clipped equations, blank pages or unresolved references were observed. The maintainer integration also checks the complete package hashes.

## Ancillary package content

The package README, exact-target comparison, AI-use disclosures, manifests and reproduction guidance were inspected. Their mathematical scope agrees with the manuscript, and none claims human or Lean verification. Maintainer integrity checks cover the listed files. The optional Python script was inspected in full before execution; it imports only fractions/json and performs exact polynomial arithmetic. Its replay passed, with A0=39711684231/4460904448, E0=27933688011/1312030720 and central coefficient 81/256, matching the reproduction document. This verifies the stated finite arithmetic only; the general controllability argument was audited analytically above. The replay record is [417-independent-profile-check.json](417-independent-profile-check.json).
