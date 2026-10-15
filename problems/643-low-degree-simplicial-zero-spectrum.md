# 643. Zero in the upper-Laplacian spectrum of low-degree simplicial complexes

**Area:** Applied topology / spectral theory
**Status:** ✅ SOLVED
**Last checked:** 2026-10-15

## Problem statement

Let $`d\ge2`$ and let $`X`$ be a nonempty pure $`d`$-dimensional simplicial complex, possibly infinite. For a $`(d-1)`$-simplex $`\sigma`$, let $`\deg(\sigma)`$ count its incident $`d`$-simplices and put

```math
D=\sup_{\sigma\in X^{d-1}}\deg(\sigma).
```

Choose orientations and give $`(d-1)`$-cochains the Hilbert norm

```math
\|f\|^2=\sum_{\sigma\in X^{d-1}}\deg(\sigma)|f(\sigma)|^2.
```

Give $`d`$-cochains the counting-measure norm. The usual simplicial coboundary

```math
(\delta f)([v_0,\ldots,v_d])=
\sum_{i=0}^d(-1)^i f([v_0,\ldots,\widehat v_i,\ldots,v_d])
```

defines a bounded operator between these spaces. Let $`\Delta^+=\delta^*\delta`$ be the normalized upper Laplacian on $`(d-1)`$-cochains.

Prove or disprove the following two assertions:

1. If $`D\le d+1`$, then $`0\in\mathop{\mathrm{Spec}}\nolimits(\Delta^+)`$.
2. If $`D\le d`$, then $`\ker\Delta^+\ne\{0\}`$: zero is an eigenvalue with a nonzero square-summable cochain.

The spectrum is taken on the full cochain Hilbert space. No finite-degree assumption is imposed on lower-dimensional faces. Equivalently, the branching-walk operator $`A_0=I-\Delta^+`$ must have $`1`$ in its spectrum, and under the stronger degree bound must have a nonzero eigenvector at $`1`$.

## Application

The operator $`A_0`$ governs expected signed particle counts in simplicial branching random walks. The conjecture would connect a local incidence bound to the existence of spectral modes at the endpoint, extending the explicit regular-tree calculation to general complexes.

## References

1. R. Rosenthal, [Simplicial branching random walks](https://doi.org/10.1007/s41468-023-00148-3), Journal of Applied and Computational Topology **8** (2024), 1751–1791, Conjecture 4.2 and Theorem 1.2; §§2 and 3.1 define the operator. [Earlier preprint](https://arxiv.org/abs/1412.5406).

## Status review

Reviewed 15 October 2026 against the original target in [PR #115](https://github.com/MColbrook/AIM/pull/115). Counterexample on a countable pure three-complex: maximum triangle degree three, coercive normalized upper Laplacian on the full weighted space, and trivial kernel.

[Proof or source](../research/solutions/643-low-degree-simplicial-zero-spectrum/paper/degree_three_counterexample.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/643-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** Counterexample on a countable pure three-complex: maximum triangle degree three, coercive normalized upper Laplacian on the full weighted space, and trivial kernel.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Known cases:** The source establishes both conclusions for regular arboreal complexes. For finite complexes, nonzero coboundaries already lie in the upper-Laplacian kernel. More generally, a $`(d-2)`$-face incident to finitely many $`(d-1)`$-faces supplies such a finitely supported coboundary.

**Remaining target:** The two assertions for arbitrary infinite pure complexes with only the stated codimension-one degree bound, including complexes whose lower-dimensional faces have infinite incidence.

Current searches found no matching proof or announced solution. The source's separate conjecture for general arboreal complexes is a subcase of this target. Results about nontrivial spectral gaps under coverings or about modified branching processes with killing do not establish these assertions.
