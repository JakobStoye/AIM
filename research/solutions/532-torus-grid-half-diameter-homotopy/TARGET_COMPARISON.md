# Target comparison for AIM 532

Target: [problem 532 at revision a153f469ee0ea64e876b2ad97c79d252c19a3e22](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/532-torus-grid-half-diameter-homotopy.md).

Result: Theorem 1 of [Torus-grid Vietoris–Rips complexes at half the diameter](paper/torus-grid-half-diameter.pdf), by Kaiwen Jin.

| Original requirement | Manuscript location and result | Coverage |
|---|---|---|
| Vertex set (Z/2kZ)^2 | Section 1 defines T_(n,n), then fixes n=2k | Exact |
| Sum of the two periodic coordinate distances | Section 1 defines delta_n and d | Exact metric and normalization |
| Subsets of diameter at most k | Section 1 defines the closed clique/Rips complex and K=VR(T_(n,n);k) | Equality is included; no open-threshold substitution |
| Every integer k>=3 | Theorem 1; all lemmas work uniformly with k>=3 and n=2k | Entire prescribed range |
| Homotopy equivalence S^3 wedge 4k copies of S^(2k−1) | Theorem 1 and its closing proof in Section 4 | Full homotopy type over the entire range |
| Actual homotopy, rather than matching Betti numbers | Section 4 proves simple connectivity, applies Hurewicz and homology Whitehead, then uses Lemma 3 to restore the sphere summands | Analytic upgrade supplied |
| Sphere number and dimension | Lemma 2 identifies 2n adjacent-row/column bands; Lemma 3 restores 2n spheres of dimension n−1 | 2n=4k and n−1=2k−1 |

The theorem is the affirmative alternative allowed by the problem. There is no additional hypothesis, conditional case or remaining k in the target. The previously known case k=2 is mentioned for context and is outside the assigned range. The cross-polytope calculation at radius 2k−1 is a different scale and is not used as a resolution of this target.

## Public dependencies

The proof is complete in the manuscript using the following public results. These sources provide tools; none is cited as an existing proof of the half-diameter formula.

| Source and exact locator | Use in this manuscript |
|---|---|
| Adams, Adetowubo, Barriga-Acosta, Feng and Sterling, [Vietoris–Rips complexes of torus grids, arXiv v2](https://arxiv.org/abs/2502.07134v2), Corollary 4.3, p.10 | Integer Manhattan Rips complexes as nerves of open balls, used for rectangles in Lemma 7 |
| Same source, Lemma 5.7, p.14 | Homotopy type of a subcomplex union when both intersection inclusions are null, used for facet splitting and cylinders |
| Björner, Topological methods, Handbook of Combinatorics vol.2 (1995), Theorem 10.6(i), p.1850 | Finite subcomplex good-cover nerve theorem for bands and cylinder star intersections |
| Same chapter, Theorem 10.7, p.1850 | Nerve theorem for the finite open convex-ball cover in Lemma 7 |
| Hatcher, Algebraic Topology (2002), Theorem 4.8, p.349 | Cellular approximation and connectivity from the wedge of spheres; preservation of fundamental group under high-dimensional facet removal |
| Same book, Section 2.2, pp.149–150 | Natural Mayer–Vietoris sequences for subcomplex unions, used in Lemma 9 |
| Same book, Theorem 4.32, pp.366–367, and Corollary 4.33, pp.367–368 | Hurewicz and homology Whitehead, used for cylinder contractibility and K^- equivalent to S^3 |

The original conjecture is Question 8.6, p.19 of the Adams et al. author version. Its Table 1 reports finite-case evidence; the present proof addresses all k>=3.

## Evidence and review scope

This is a complete analytic solution claim. OpenAI Codex assisted proof exploration, writing and source checking. The source was compiled and the six-page PDF checked for content, references and layout. These checks establish artifact integrity, not community acceptance. No numerical or formal certificate is asserted. Independent human mathematical review remains requested.
