# Comparison with AIM 010

Target: [The Mercedes-star partition of a disk](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/010-mercedes-disk-partition.md), statement revision `c9929805cece044705abaaebe1cebddac1ba11a6`.

Write B for the open unit disk, lambda_1 for the variational first Dirichlet eigenvalue, and j_(3/2,1) for the first positive zero of J_(3/2). The submitted claim is

```math
\inf_{(D_1,D_2,D_3)}\max_i\lambda_1(D_i)=j_{3/2,1}^2,
```

where the infimum is over every triple in the original statement. The three sectors of opening 2 pi / 3 attain equality.

| Original requirement | Manuscript location | Coverage |
| --- | --- | --- |
| Open planar unit disk | Section 1 and Theorem 1 | B is exactly the unit disk; no radius rescaling is used. |
| Every triple of pairwise disjoint nonempty connected open subsets | Theorem 1; Sections 3--4 | The same homeomorphism is applied to all three cells and preserves each admissibility property. |
| First Dirichlet eigenvalue on arbitrary open sets | Equation (1) and its following paragraph | The compact-smooth Rayleigh infimum agrees with the H_0^1 convention; no smooth-boundary definition is required. |
| Universal lower bound for the maximum | Lemma 3; equations (11)--(13); Section 4 | If all three eigenvalues were strictly smaller, three transformed tests would violate Proposition 2. This contradiction proves the lower bound for every triple. |
| No prescribed interface topology, symmetry or regularity | Proposition 2 and Sections 3--4 | No interface description is used. Compact tests and the arbitrary-open spherical theorem suffice. |
| No assumption that the cells cover the disk | Section 1; Proposition 2; Section 4 | Neither the stated spherical class nor the test comparison imposes coverage. |
| Cells or test supports may meet the origin | The common logarithmic cutoff in Section 4 | The cutoff changes tests inside their own cells and converges in H^1; the cells themselves are preserved. |
| Exact Bessel value | Section 2, before equation (2) | Official identities 10.47.3 and 10.49.3 identify the first positive zero of sin z - z cos z with j_(3/2,1). |
| Equal sectors separated by radii at 2 pi / 3 attain the infimum | Final part of Section 4 | The separated trial function and four explicit cutoff estimates give the sector upper bound. The universal lower bound completes attainment. |

The imported spherical result is Proposition 2: the largest first eigenvalue of any admissible spherical triple is at least 15/4. Its cited interface is Soave--Terracini, [arXiv:1404.7288v2](https://arxiv.org/abs/1404.7288v2), Definition 1, equation (10) and Theorem 1.10 at N=3. The theorem number refers explicitly to v2. Helffer--Hoffmann-Ostenhof--Terracini, [arXiv:0903.3326v1](https://arxiv.org/abs/0903.3326v1), Theorem 1.1 and equation (1.9), provides the earlier sharp spherical result. The manuscript distinguishes this input from the restricted disk comparison in Berkolaiko--Canzani--Cox--Marzuola, [arXiv:2406.04225v1](https://arxiv.org/abs/2406.04225v1), Theorem 1.8.

The full target is claimed; no admissible subclass is omitted and no additional hypothesis or uniqueness assertion is introduced. The proposed proof is analytic and uses no computational certificate. Its correctness and catalogue classification are submitted for independent mathematical and maintainer review.
