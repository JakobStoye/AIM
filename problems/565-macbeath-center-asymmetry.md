# 565. Asymmetry at the Macbeath point of a convex body

**Area:** Convex geometry and geometric approximation

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`K\subset\mathbb R^d`$ be compact and convex with nonempty interior. Its Macbeath point is the unique maximizer $`p`$ of

```math
x\longmapsto\mathop{\mathrm{vol}}\nolimits_d\bigl(K\cap(2x-K)\bigr),
```

where $`2x-K=\{2x-y:y\in K\}`$ and $`\mathop{\mathrm{vol}}\nolimits_d`$ denotes Lebesgue volume.

Prove or disprove that every such convex body satisfies

```math
K-p\subseteq-d(K-p).
```

Equivalently, for every $`y\in K`$, the point $`p-(y-p)/d`$ must also belong to $`K`$. The center is prescribed by the maximal symmetric intersection; finding some other center with the inclusion does not answer the question.

## Application

The inclusion would make the volume-maximizing symmetric intersection a quantitatively central choice for polarity arguments. It could support sparse convex approximation and volume bounds in quantitative Helly-type results.

## References

1. G. Ivanov, [Quantitative Steinitz theorem and polarity](https://doi.org/10.1007/s00454-025-00743-4), *Discrete & Computational Geometry* **75** (2026), 1405–1413, Section 2, Conjecture 2.1. [arXiv:2403.14761](https://arxiv.org/abs/2403.14761).

## Status review

Reviewed 15 October 2026 against the original target in [PR #105](https://github.com/MColbrook/AIM/pull/105). A square pyramid is a counterexample to the proposed Macbeath-center asymmetry inclusion.

[Proof or source](../research/solutions/565-macbeath-center-asymmetry/paper/macbeath_counterexample.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/565-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** The explicit three-dimensional convex body has a unique Macbeath center whose reflected apex violates the proposed factor-three containment.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

The journal article defines this center using Macbeath's uniqueness theorem and states the displayed inclusion as Conjecture 2.1. Its proved polarity-center theorem concerns a center at which the vertices of a polar polytope sum to zero; it does not identify that center with the Macbeath point.

The issue is controlling asymmetry about this particular center. Searches of current literature and announcement registries found no matching proof or counterexample. Results concerning local Macbeath regions, Fricke–Macbeath surfaces or a different convex-body center do not settle this statement.
