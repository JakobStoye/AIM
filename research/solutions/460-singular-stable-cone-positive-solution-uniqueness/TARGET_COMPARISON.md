# Comparison with AIM problem 460

Target: [the problem statement](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/460-singular-stable-cone-positive-solution-uniqueness.md) at revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

The proposed conclusion is the full positive proportionality assertion. The following locations refer to the included manuscript.

| Original requirement | Manuscript location | Scope |
|---|---|---|
| Every integer n >= 2 and every 0 < s < 1 | Introduction, Theorem 1.1 | Identical |
| Finite even nonnegative spectral measure, bounded total mass and positive directional 2s-moment | Equation (1.1), Theorem 1.1; class bounds (2.4)--(2.5) | Identical; singular and atomic measures are included |
| The stated positive stable operator, with factor 1/2 and the original radial normalization | Equation (1.2); measure and compensated form in Section 2 | Identical; the process generator is its negative |
| Every proper closed convex cone with nonempty interior | Theorem 1.1 | Identical |
| Globally continuous profiles, zero on the cone and positive on its complement | Theorem 1.1 | Identical |
| Harmonicity in the viscosity sense | Theorem 1.1 and Lemma 2.2 | Identical; Lemma 2.2 proves the local equivalence needed for the distributional arguments |
| Separate polynomial exponents beta_i < 2s | Theorem 1.1, Proposition 3.4 and the final proof | Identical; the temporary exponents q and p are selected inside the proof |
| A positive constant c with w_1 = c w_2 on all of R^n | Theorem 1.1 and its proof in Section 4 | Full proposed conclusion |
| No profile homogeneity or directional monotonicity assumption | Theorem 1.1; growth normalization in Proposition 3.4 | Neither is imposed |

The supporting results are stated explicitly in Lemma 2.1 and traced to Fernández-Real and Ros-Oton, *Integro-Differential Elliptic Equations*, arXiv:2411.12455v1: Lemma 2.2.30, Theorems 2.4.3, 2.4.15(b), 2.6.12, and Lemma B.1.4. Section 2 checks their general-measure applicability. The stopping argument uses the Lévy-process results identified in Schilling, arXiv:1603.00251v2, with the sign and integrability limits proved in the manuscript.

Ros-Oton and Weidner, arXiv:2308.01695v1, supply the closest comparison-method background; their angular density and monotonicity hypotheses are not imported as assumptions of Theorem 1.1. Ros-Oton and Serra, arXiv:1412.3892v1, supply regularity and the half-space benchmark. The manuscript distinguishes the precise integrable-growth target above from the broader wording of the book's Open Question 4.4.

This package presents an analytic solution claim for independent review. It does not report a published resolution, a human acceptance decision, or proof-assistant verification.
