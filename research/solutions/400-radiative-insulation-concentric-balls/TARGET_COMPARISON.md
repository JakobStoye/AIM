# Comparison with AIM problem 400

Target: [Concentric-ball optimality for thermal insulation with radiative heat transfer](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/400-radiative-insulation-concentric-balls.md), revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

The submitted manuscript presents an affirmative analytic proof of the complete displayed inequality. The claim is submitted for independent mathematical review.

| Original requirement | Manuscript location and coverage |
| --- | --- |
| Every integer n >= 2, beta > 0, gamma >= 0 and R > 1 | Theorem 1.1 and the parameter declaration before (1.1); no further parameter restriction. |
| The exact radiative polynomial | Equation (1.1), with all four terms and both parameters. Lemma 2.2 treats gamma = 0 and gamma > 0. |
| Every bounded Lipschitz open outer set | Energy (1.2) and Theorem 1.1. Connectedness is not required; the boundary-trace discussion in Section 2 addresses local charts. |
| A merely measurable heated set K contained in the outer set | Energy (1.2), Theorem 1.1 and its interpretation. No boundary regularity of K is imposed. |
| H1 temperatures, 0 <= v <= 1 and v = 1 almost everywhere on K | Energy (1.2). Section 2 justifies attainment of this minimum. |
| Interior boundary trace and Hausdorff boundary integral | Energy (1.2), the trace convention immediately following it, and Section 2. |
| Heated volume equal to the unit-ball volume | Theorem 1.1. This gives the unit-temperature core in Proposition 3.1. |
| Total volume at most the radius-R ball volume | Theorem 1.1. Proposition 3.1 gives radial support within radius R. |
| Minimum over every radius from 1 to R | Equation (1.3). Lemma 2.1 proves the exact ball formula, continuity at radius 1 and existence of the minimum. |
| Bare heated ball and unused insulation | Theorem 1.1 and its following paragraph; Proposition 4.2 permits tail truncation and outer radius 1. |
| Full comparison for every admissible pair | Propositions 3.1, 4.1 and 4.2, assembled in the final proof of Theorem 1.1. |

The proof is analytic. It does not use numerical evidence or a computer-generated certificate. The related quadratic, penalized-volume and inactive-constraint results of Bucur, Nahon, Nitsch and Trombetti are credited in the Introduction; the manuscript proves the remaining radiative constrained comparison by an additional argument. No claim is made for an arbitrary increasing boundary potential or about uniqueness of optimal shapes.

OpenAI Codex assisted with the argument, algebra, source checking and writing. One AI reader and one AI referee reviewed an anonymized earlier draft in fresh contexts on a shared host. These were internal reviews; no separate detailed review report is submitted. Independent mathematical review is requested. A successful build or internal AI review is not community acceptance or formal verification.
