# Target comparison for Problem 512

Target: [The first Rips homotopy transition for higher-dimensional spheres](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/512-spherical-rips-first-transition.md), revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

The submitted [manuscript](paper/main.pdf), *The first Vietoris--Rips homotopy transition of round spheres*, claims the affirmative alternative in Theorem 1.1.

| Original requirement | Manuscript location and conclusion |
| --- | --- |
| Every integer n >= 3 | Theorem 1.1 and the opening of Section 2 fix an arbitrary such dimension. |
| Unit sphere with round geodesic metric | Section 1 defines S^n in R^(n+1) and d(x,y) = arccos <x,y>. |
| Ordinary CW realization; finite simplices have diameter strictly less than r | Section 1 defines K_n(r) with exactly this convention. Proposition 2.1 and the final proof in Section 4 compare the strict labelled realization to this ordinary CW space. |
| r_n = arccos(-1/(n+1)) | Section 1 defines this threshold; Section 2 writes r_0 = r_n and d = n+1. |
| Q_n = SO(n+1)/A_(n+2), with the alternating group acting by orientation-preserving regular-simplex symmetries | Section 1 defines Q_n. Section 3.2 verifies the rotational orbit and its exact stabilizer. |
| Some epsilon_n in (0, pi-r_n) | Lemma 2.2 supplies a common s with r_n < s < arccos(-1/n). The final proof takes epsilon_n = s-r_n. |
| All r_n < r < r_n+epsilon_n | Section 4 fixes any such r. The individual finite-label collar may depend on its degree; the scale interval does not. Canonical inclusions in every degree and realization homotopy invariance complete the transfer. |
| Homotopy equivalence K_n(r) ≃ S^n * Q_n | Lemma 3.5 and Proposition 3.6 compute the closed labelled model up to weak equivalence as the join. Section 4 transfers it to the strict model, uses Proposition 2.1, and upgrades the zigzag to homotopy equivalence by CW approximation and Whitehead's theorem. |

The closed labelled realization computed in Section 3 is an intermediate object. Lemma 4.1 and the remainder of Section 4 establish the required right interval of strict ordinary complexes.

External credit: Mémoli--Wang (arXiv:2609.33009v1, Theorems 4.5 and 5.1 and Propositions 2.5, 2.6 and 2.9) provide the spherical stationary spectrum, its local finiteness and strict-realization comparisons. The manuscript adds the explicit endpoint attachment and combines the definable collar result of Ji--Meng with the all-label noncritical interval. Ebert--Randal-Williams and Corvellec provide the realization and deformation tools. Earlier formulations and known low-dimensional cases are credited in Section 1.

This comparison records a full analytic solution claim for review. Catalogue classification and acceptance belong to the receiving repository's maintainers.
