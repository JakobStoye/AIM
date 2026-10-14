# Target comparison for AIM 416

Source: [original problem statement](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/416-catalytic-reaction-diffusion-positive-attractor.md), revision a153f469ee0ea64e876b2ad97c79d252c19a3e22. This table compares that public statement with the finished manuscript.

| Original requirement | Manuscript result and location | Scope |
| --- | --- | --- |
| Every spatial dimension; bounded connected smooth domain with volume one | Theorem 1.1; Section 2 constructs the heat estimates using fixed positive times | Identical; no dimension cutoff |
| Arbitrary d1,d2,d3 > 0 | System (1), Theorem 1.1, both heat lemmas and Section 3 | Identical; unequal diffusivities allowed |
| Strictly positive a0,b0,c0 in C2 of the closed domain, with homogeneous Neumann compatibility | Theorem 1.1; Section 3 proves preservation of nonnegativity and finite-time positivity of the total catalyst mass | Identical data class |
| Unique global bounded classical solution of the given three equations | System (1) and Theorem 1.1 | Identical solution concept; already assumed by the target |
| Conserved masses M1 = integral(a0+c0), M2 = integral(b0+c0) | Equation (2), then mean identities (8) | Identical normalization |
| M2 <= M1 < 2 M2, including M1=M2 | Theorem 1.1; Section 3 uses delta=2 M2-M1>0 | Entire stated mass range |
| Sum of the three uniform norms tends to zero at (M1/2,M2-M1/2,M1/2) | Theorem 1.1; (10)-(12), logistic comparison, and the final application of Lemma 2.2 | Full conclusion; no added smallness or rate hypothesis |
| Source inputs and applicability | Nguyen--Tang Theorem 2.1 supplies the existing boundedness context, and the proof of their Theorem 2.7 supplies the credited energy. Baudoin, author version 13 February 2019, Chapter 4, Proposition 4.49 and Section 8 (Proposition 4.56 and Theorem 4.58), supplies Green, Neumann kernel and spectral facts | Exact sources and locators are cited in the manuscript; the compactness, time-continuity and forced-decay consequences are proved in Section 2 |

The AIM statement already imposes the strict positive C2 compatible-data formulation used in Theorem 1.1. No smoothing reduction or change of data class is needed. The broader nonnegative-data wording of the conjecture printed in Nguyen--Tang includes a stationary catalyst-free state; the manuscript does not claim that broader assertion.

The proposed result covers the entire target at the pinned revision. No part of that target is left as a numerical or conditional case. This correspondence is a submission claim for mathematical assessment.
