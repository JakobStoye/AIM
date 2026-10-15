# 521. Six-point persistence on the Euclidean two-sphere

**Area:** Applied topology and geometric data analysis

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`S^2=\{x\in\mathbb R^3:\|x\|_2=1\}`$, equipped with chordal Euclidean distance. For any six-element subset $`X\subset S^2`$ and $`x\in X`$, let $`r_1(x)\ge r_2(x)`$ be the largest and second-largest of the five distances from $`x`$ to $`X\setminus\{x\}`$, counting ties. Set

```math
b(X)=\max_{x\in X}r_2(x),\qquad d(X)=\min_{x\in X}r_1(x).
```

Define

```math
\mathcal P=\{(b(X),d(X)):X\subset S^2,\ |X|=6,\ b(X)<d(X)\}.
```

Prove or refute the Gómez–Mémoli conjecture

```math
\mathcal P=\left\{(b,d):0<b<d\le2,\quad d\le\frac{2b}{\sqrt3}\ \text{or}\ \frac{4b^2(3-b^2)}{4-b^2}\le d^2\right\}.
```

The denominator is positive because $`b<d\le2`$.

Equivalently, $`\mathcal P`$ is the set of nonzero degree-two persistence pairs obtainable from samples of at most six points on $`S^2`$: at scale $`t`$, the Vietoris–Rips complex includes every simplex of diameter at most $`t`$. With coefficients in any field, such a sample has either no degree-two interval or the single interval $`[b(X),d(X))`$; fewer than six points cannot contribute one.

## Application

Persistence sets combine the topological summaries of many small samples. Characterizing this basic spherical example would give an exact benchmark for geometric shape descriptors computed from subsamples, whose cost can be much lower than that of the full data set.

## References

1. M. Gómez and F. Mémoli, [Curvature Sets Over Persistence Diagrams](https://doi.org/10.1007/s00454-024-00634-0), Discrete & Computational Geometry **72**, 91–180 (2024), Definitions 3.10 and 4.1, Theorem 4.4, Proposition 5.24 and Conjecture 5.25, pp.151–153. [Preprint](https://arxiv.org/abs/2103.04470).
2. The authors’ [persistence-curv-sets implementation](https://github.com/ndag/persistence-curv-sets).

## Status review

Reviewed 15 October 2026 against the original target in [PR #170](https://github.com/MColbrook/AIM/pull/170). Negative for the displayed region

[Proof or source](https://arxiv.org/pdf/2103.04470v5) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/170-source-scope-review_90_114.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** For b(X)<d(X), each vertex has exactly one distance greater than b: its farthest distance is at least d>b and its second farthest is at most b. Symmetry makes these farthest-neighbor edges a perfect matching of the six vertices into three pairs. Choose any two pairs as four points. Their matching diagonals have lengths at least d and all four cross-pair side lengths are at most b. Euclidean Ptolemy gives d²<=2b². The literal proposed right-hand side includes(1,2): its second branch has4*1*(3−1)/(4−1)=8/3<=4. But4>2, so no six-point sample can realize this pair. This completely refutes the displayed equality.

The source's Proposition5.24 opening formula itself also omits a restriction that its proof then uses: branchC is defined with sqrt2<=b<=sqrt3. Thus this is not solely a transcription mistake newly introduced by the catalogue, but it may be a missing-domain typographical issue in the published proposed region. The submitted report correctly limits itself to the literal formula and does not purport to solve the corrected exclusion problem. The status text must preserve that distinction instead of saying that every natural corrected Gómez–Mémoli conjecture has been refuted.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Resolution-source report (2026-10-15):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-15-prior-resolutions.md#aim-521). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-24)

Proposition 5.24 realizes every pair in the displayed proposed region. The unresolved direction excludes additional pairs from arbitrary six-point configurations; numerical samples support it but do not prove it. This is a finite-sample chordal question, distinct from the full-sphere Vietoris–Rips transition in problem 522.

Searches on 24 September 2026 found no matching solution or announcement, including indexed arXiv, Zenodo, GitHub and Palomar searches.
