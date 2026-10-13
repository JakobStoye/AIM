# Comparison with AIM 063

Target: [063 — Characterizing realizable geodesic scattering data](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/063-range-of-geodesic-scattering.md), revision `c9929805cece044705abaaebe1cebddac1ba11a6`.

Submitted result: Theorem 2.1 of [A variational characterization of geodesic scattering on simple disks](paper/geodesic_scattering.pdf), with conditions C1–C5 stated in Section 2 and the complete proof in Sections 3–4. The comparison below uses this manuscript and the public problem statement.

| Original requirement | Manuscript result and location | Coverage |
| --- | --- | --- |
| Fixed smooth disk M and prescribed boundary metric h | Section 2 fixes the boundary arclength cylinder from h. Theorem 2.1 quantifies over every smooth compact disk and smooth positive boundary metric. The closing proof, page 11, pulls the selected disk metric back to this M. | Same smooth Riemannian setting. |
| Proposed map on the whole open boundary unit cotangent bundle | Theorem 2.1 allows every map A on this bundle. C1 tests smoothness and the endpoint diffeomorphism rather than assumes data already arise from a metric. | Entire open cylinder, not a finite sample or local perturbation. |
| Exit point and tangential exit covector, without reversal | Section 2 fixes the convention and constructs D with D_s=-P and D_t=Q. Lemma 3.1 derives these identities for actual metrics. The closing proof of Theorem 2.1 recovers both components for every input state. | Same scattering convention. |
| Smooth simple Riemannian realization inducing h | C3 checks the selected class's smooth positive representative and prescribed trace. C4 gives explicit all-state geodesic/Jacobi tests; Lemma 4.2 proves their equivalence to simplicity. The final pullback preserves h. | No Finsler substitute, added smallness or genericity hypothesis. |
| Conditions expressed solely through A and h | C1 constructs the action and full lift; C2 extracts the uniquely normalized boundary coordinate; C3 uses all-curve inequalities on a fixed Euclidean disk and strong real L2 closure to select one least-norm class. Lemma 4.1 proves this construction is nonempty and unique before any realization test. | No unknown realizing metric is an input to the criterion. |
| Necessary conditions | Proposition 4.3 identifies an actual metric's conformal density with the universally selected minimizer using the integrated length pairing. Lemmas 3.1–3.3 supply the boundary and conformal tests. | Every realizing smooth simple metric satisfies C1–C5. |
| Sufficient conditions | Lemma 4.4 passes smooth-approximant length inequalities through strong L2 closure by a geodesic-family L1 estimate. Lemma 4.5 forces equality of all boundary distances from positive twist and area saturation. The proof of Theorem 2.1 then recovers A and the fixed-disk metric. | Full global realization, with no individual-curve L2 trace assumption. |
| Intrinsic characterization | Lemma 4.1 gives a total canonical selection after the boundary prerequisites; later tests inspect that uniquely selected object. The closing proof establishes independence of orientation, arclength origin and boundary triple. | Does not restate existence of some interior metric; qualitative rather than an effective finite procedure. |

## Public dependencies and scope

The manuscript states the operational hypotheses and Fourier normalization of the imported surface results. Its main source is Paternain–Salo–Uhlmann, *Geometric Inverse Problems: With Emphasis on Two Dimensions* (2023), [DOI](https://doi.org/10.1017/9781009039901). In particular, Theorems 5.1.1, 8.2.1–8.2.2 and 10.2.3 are used on actual simple surfaces to recover smooth holomorphic traces; Theorem 3.4.15 supplies smooth uniformization; Theorem 3.8.2 supplies the simplicity equivalence. The factor 2π between the source's fiber integral and the manuscript's zeroth Fourier average is explicit in Section 3.2.

Pestov–Uhlmann's boundary-distance rigidity and actual-metric boundary reconstruction, Bohr–Paternain's fixed-metric non-Abelian range theorem, and Burago–Ivanov's Finsler lens-map results are credited as context, not substituted for this target. Milnor's explicitly cited September 1991 revision supplies the half-plane automorphism classification. All five references have direct public links in the manuscript.

The submission claims both directions of the full stated target. It does not claim quantitative stability, finite decidability, non-simple realization, a numerical certificate, formal verification or independent mathematical acceptance. The exact Euclidean-disk example checks conventions analytically. Independent review is requested.
