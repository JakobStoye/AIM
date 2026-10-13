# AIM 615: independent review of PR #81

**Date:** 2026-10-13. **Reviewer:** OpenAI Codex, independent AI argument audit during maintainer review; no human or Lean verification is asserted.

**PR:** [#81](https://github.com/MColbrook/AIM/pull/81). **Audited head:** `312df9569f5265fd7a85dfe7f7c1b5300cb5765b`. **Target revision:** `c9929805cece044705abaaebe1cebddac1ba11a6`.

**Direct proof:** [Source manuscript](https://github.com/MColbrook/AIM/blob/312df9569f5265fd7a85dfe7f7c1b5300cb5765b/research/solutions/615-gambler-scaling/paper/gambler_scaling.tex).

All source sections, mathematical ancillary claims and bibliography entries were checked independently of the submission's own AI checks.

## Exact target

The target is the fourth-order Brownian approximation for each fixed positive capital proportion and each elimination order. The theorem proves it for order 321 and transfers it to all orders by relabeling. It does not confuse this scaling with the regime of two fixed small capitals and one growing capital.

## Complete independent argument audit

1. The equilateral lattice coordinates give six unit-length transfer steps with isotropic second and fourth moments. For order 321 the boundary payoff is $`1-b/M`$ on $`c=0`$ and zero on the other open sides. This follows from the two-player winner fraction. Interior lattice points cannot reach a vertex in one transfer; corner payoff ambiguity is harmless. The finite averaging problem has the stated maximum-principle uniqueness (source lines 64-114).
2. Reflection interchanges the two losing players and preserves the stencil. Adding the reflected discrete or Brownian payoff gives the same affine function $`1-(b+c)/M`$. The error is therefore odd across the bisector and exactly zero there. Brownian similarity scaling matches the precise fixed-proportion limit (116-130).
3. At the two compatible corners, subtracting a matching affine function permits six odd reflections, giving a bounded harmonic function on a punctured disk. Its isolated singularity is removable. Away from the incompatible corner zero, local reflection and a finite normalized cover give harmonic continuation and derivative bounds $`C_k|z|^{-k}`$ with constants independent of the total capital (137-164).
4. The stencil's second and fourth moments give $`Ph-h=\Delta h/4+\Delta^2h/64+\mathcal R_h`$. For the harmonic payoff the remainder is $`O(r^{-6})`$ with derivative $`O(r^{-7})`$. The defect vanishes on both half-wedge rays; projection to the nearer ray gives the additional factor $`\sin(6\theta)`$. The feet stay inside the closed triangle with radius bounded below by a fixed fraction of $`r`$ (166-232).
5. The positive half-wedge barrier $`r^{-4}\sin(6\theta)`$ has Laplacian $`-20r^{-6}\sin(6\theta)`$ and vanishing bi-Laplacian. Homogeneous derivative estimates and the same oddness/projection argument bound the discrete remainder by $`Cr^{-10}\sin(6\theta)`$. For a fixed sufficiently large cutoff radius the barrier's discrete Laplacian dominates the defect (234-264).
6. A jump across the bisector occurs only when $`b-c=1`$, and its endpoint is the reflected original lattice point. Incorporating its negative value changes the diagonal to $`7/6`$ and leaves at most five positive-side neighbors. The resulting finite comparison principle is proved explicitly, including the strict contradiction at crossing points and propagation to the physical boundary otherwise (268-283).
7. A fixed multiple of the barrier dominates the bounded error at the finitely many inner neighbors. Comparison gives $`|e_M(z)|\le K|z|^{-4}`$ uniformly in $`M`$. Substituting $`M=nN`$, $`z=n(B+C\omega)`$ gives the exact $`O((nN)^{-4})`$ target. Reflection and relabeling cover the bisector and every elimination order. Equal losing capitals give the asserted exact agreement (285-325).

## Probability-scope clarification

The preceding sentence in lines 76-83 concerns the remaining two-player game, for which the sufficient directed-transfer path has probability at least $`2^{-M}`$ as written. This is not a demonstrated false probability statement. For a specified pair and direction while three players survive, the step probability is $`1/6`$ instead. A useful clarification is to state both finite-block arguments: a prescribed sequence of at most M same-pair directed transfers has probability at least $`6^{-M}`$ and forces the first elimination, and subsequent two-player directed transfers have probability at least $`2^{-M}`$ and force absorption. Repeating blocks gives the almost-sure claims. This clarification does not assert that the overall three-player elimination probability in M steps is below $`2^{-M}`$, and does not change the theorem or its error estimate.

## References and ancillary claims

All three entries were verified. Diaconis-Ethier's publisher/author versions have the stated 2022 metadata and Theorem 4.1/Conjecture 4.2(b), identifying the same diffusion limit. Denisov-Wachtel's DOI record confirms volume 34(5), 2024, 4387-4407, and its actual Proposition 5 distinguishes cubic-order scaling from the separate fixed-small-capital asymptotic. Axler-Bourdon-Ramey's author-hosted second edition confirms the 2001 book and the stated reflection, removable-singularity and derivative-estimate theorems. Their hypotheses are established in the local continuation construction. The additional maximum-principle/analyticity references are applicable. No external fourth-order error estimate is assumed.

Primary evidence: [Diaconis-Ethier](https://projecteuclid.org/journals/statistical-science/volume-37/issue-3/Gamblers-Ruin-and-the-ICM/10.1214/21-STS826.pdf), [Denisov-Wachtel](https://arxiv.org/html/2212.11526v1), [Harmonic Function Theory](https://www.axler.net/HFT.pdf).

## Decision

**Solved - affirmative.** The complete main argument resolves every target clause; no substantive gap remains. The probability-scope clarification above is editorial and does not change the decision.

## PDF consistency and layout

Every rendered manuscript page was inspected in the all-page contact sheets. The title, author, theorem/proof structure, conclusions and bibliography agree with the audited source; no clipped equations, blank pages or unresolved references were observed. If the probability-scope clarification is applied to AIM 615, it must also be reflected in the regenerated PDF and package hashes.

## Ancillary package content

The package README, exact-target comparison, AI-use disclosures, manifests and reproduction guidance were inspected. Their mathematical scope agrees with the manuscript, and none claims human or Lean verification. Maintainer integrity checks cover the listed files. There is no executable proof certificate or numerical experiment used as a proof premise.
