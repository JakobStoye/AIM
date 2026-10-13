# Comparison with the original AIM 527 target

Original statement: [527. Existence for adaptive porous flow with a negative drag jump](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/527-negative-jump-adaptive-flow.md), revision `c9929805cece044705abaaebe1cebddac1ba11a6`.

Submitted result: Theorem 1 of the [manuscript](paper/main.pdf), proved in
Section 4. The alternative established is affirmative weak existence for all
original data. This table is based on that manuscript and the public statement.

| Original requirement | Manuscript location and result | Coverage |
|---|---|---|
| Every dimension `d >= 2` and bounded connected Lipschitz domain | Section 2.1 and Theorem 1; Section 3.1 supplies a perpendicular wave direction in every such dimension | Full |
| Relatively open pressure/flux boundary partition up to surface measure zero | Section 2.1; Proposition 2 and the compact potential construction preserve the original affine constraints | Full |
| Every finite `r >= 2`, with `s = r/(r-1)` | Equation (1), Lemma 3, mixed moments in Lemma 7, and both summable norm series in Section 4 | Full |
| Continuous nondecreasing low/high laws, original high-branch growth, and `0 < phi2(1) < phi1(1)` | Equations (2)--(3) and Theorem 1; the high extension in equation (6) is auxiliary | All original hypotheses retained |
| Completely free vector transition drag from one global `L^s` field | Equation (3); the final proof takes `h = z 1_{|u|=1}` in `L^s` | Exact original law |
| `q` and normal-flux data in the stated `L^r` spaces, forcing in `L^s` | Section 2.1, the affine mass set in Section 2.2, auxiliary existence in Lemma 4, and rough-tail comparison in Lemma 9 | No extra boundedness or smoothness |
| Prescribed extension `P` in `W^{1,s}` and pressure in `P+V` when pressure is imposed | Section 2.1, Proposition 2, Lemmas 4--5, and pressure convergence in the final proof | Full |
| Pure-flux compatibility, `P=0` and mean-zero pressure | Equation (4), pressure normalization in Section 3.3 and final convergence in Section 4 | Full |
| `zeta = f - grad p` and the weak mass identity for every original test in `V` | Equation (5); every exact improvement has the original affine data, and the final strong limit preserves them | Full, with manuscript `z` equal to statement `zeta` |
| Existence without an energy-minimization requirement | Theorem 1 and its scope paragraph | Full affirmative alternative |

The extra conclusion `|u| >= 1` almost everywhere is a proved property of the
output. It is not an additional premise. The low branch is consequently unused
by the construction. The argument requires the original arbitrary transition
drag; it does not resolve a different model which restricts that drag to a
radial value, a selected branch or a convex combination.

The public dependencies are explicitly identified in the paper. The mixed
pressure/mass interface comes from Fumagalli--Patacchini (2022), Lemmas 4.1--4.2,
with the notation and boundary convention explained in Proposition 2.
Brezis's cited analysis statements give the needed compactness, density and
limit facts. Sorella--Tione's local finite-potential construction is credited;
the measurable-mask construction and global rough-data cutoff comparison are
proved in Sections 3.3--4, rather than imported from a global existence theorem.

No numerical experiment, computational certificate or Lean formalization is
used as evidence for the theorem. The complete mathematical evidence is the
manuscript and its public cited sources.
