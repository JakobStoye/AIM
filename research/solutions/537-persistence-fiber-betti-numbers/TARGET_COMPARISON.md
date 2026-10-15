# Comparison with AIM 537

Target: [537 - Betti numbers of a persistence fiber with no finite bars](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/537-persistence-fiber-betti-numbers.md), revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

Result: Theorem 1 of *The homology of a persistence fiber without finite bars* proves an isomorphism of ordinary F2 homology groups for every degree, and hence the exact requested Betti-number equality. The submitted result is an affirmative solution claim for the full target.

| Original requirement | Manuscript location | Coverage |
| --- | --- | --- |
| Every finite connected simplicial complex K | Section 1 setup; Theorem 1; its proof in Section 3 | Full; no dimension or size restriction. The empty-connected convention is treated in the final proof paragraph. |
| Ordinary unreduced homology over F2, and every q>=0 | Section 1 conventions; Theorem 1; Lemma 4 and final proof | Full, including degree zero and degrees beyond dim K. Reduced homology is auxiliary notation for acyclicity. |
| Barcode D_K with one H0 infinite bar at 1, beta_q(K) positive-degree infinite bars at 2, and no finite bars | Section 1 definition and criterion (1); Lemma 2 | Exactly the original graded barcode. |
| m=1 for vanishing positive Betti numbers and m=2 otherwise; I=[1,m+1] | Section 1; Lemma 2; Proposition 3 proof's max g<2 / max g=2 branches | Both cases covered. |
| Values assigned to all nonempty simplices with the face condition | Section 1 filter definition; Proposition 3 formula (2) | The whole all-simplex filter space is used. |
| Fiber topology inherited from I^{number of simplices} | Section 1; joint continuity in Lemma 2; compact-to-Hausdorff homeomorphism in Proposition 3 | The stated Euclidean subspace topology is preserved. |
| Equality of all Betti numbers with those of K | Theorem 1 and its final proof | Follows from all-degree homology isomorphisms. |

The original conjecture is attributed to Leygonie and Henselman-Petrusek, Conjecture 1, p.2044 of their 2024 article, in its preceding connected setting. The homological poset method is established prior work, credited to Bjorner, Wachs and Welker, Section 4 of the author manuscript linked in the bibliography. The needed additional persistence-space argument is the endpoint-preserving deformation in Lemma 2 and the exact homeomorphism, with inverse, in Proposition 3. Lemma 4 supplies a direct proof of the acyclic special case used for the face-poset comparison.

The proof does not require subcomplexes to be contractible and makes no homotopy-equivalence claim between F_K and K. It does not address arbitrary target barcodes, restricted lower-star filters or multiparameter fibers. No numerical extrapolation is used.
