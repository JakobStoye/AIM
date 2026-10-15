# 520. Coarse Hilbert embeddings of persistence diagrams

**Area:** Applied topology and metric geometry

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`\mathcal D`$ be the space of all finite multisets of points $`(b,d)\in\mathbb R^2`$ with $`b<d`$, including the empty multiset. There is no common cardinality or coordinate bound. Put $`\Delta=\{(t,t):t\in\mathbb R\}`$ and use the $`\ell^\infty`$ distance in the plane. For $`1\le p\le2`$, define

```math
W_p(D,E)^p=\min_{\substack{D'\subseteq D,\ E'\subseteq E\\\phi:D'\to E'\text{ bijective}}}\left(\sum_{x\in D'}\|x-\phi(x)\|_\infty^p+\sum_{x\in D\setminus D'}\mathop{\mathrm{dist}}\nolimits_\infty(x,\Delta)^p+\sum_{y\in E\setminus E'}\mathop{\mathrm{dist}}\nolimits_\infty(y,\Delta)^p\right),
```

where subsets and matchings respect multiplicity.

Determine for which $`p\in[1,2]`$ there exist a Hilbert space $`H`$, a map $`F:\mathcal D\to H`$, and finite-valued nondecreasing functions $`\rho_-,\rho_+:[0,\infty)\to[0,\infty)`$ such that

```math
\lim_{t\to\infty}\rho_-(t)=\infty,\qquad
\rho_-(W_p(D,E))\le\|F(D)-F(E)\|_H\le\rho_+(W_p(D,E))
```

for every $`D,E\in\mathcal D`$. The map and control functions may depend on $`p`$, but must work for all diagrams simultaneously.

## Application

Persistence diagrams summarize topological features of data. Hilbert-space representations permit statistical and learning methods; the lower control above would ensure that arbitrarily separated diagrams cannot collapse to a bounded distance in the representation.

## References

1. N. Pritchard and T. Weighill, [Coarse Embeddability of Wasserstein Space and the Space of Persistence Diagrams](https://doi.org/10.1007/s00454-024-00674-6), Discrete & Computational Geometry **74**, 358–373 (2025), §§2–3, Theorem 24 and §6. [Preprint](https://arxiv.org/abs/2307.12884).
2. P. Bubenik, [A Hilbert space embedding of persistence diagrams and barcodes](https://arxiv.org/abs/2608.08858v1), 2026.
3. [Persistence Spheres: a Bi-continuous Linear Representation of Measures for Partial Optimal Transport](https://arxiv.org/abs/2603.15384v1), 2026, §§7–8.

## Status review

Reviewed 15 October 2026 against the original target in [PR #103](https://github.com/MColbrook/AIM/pull/103). The unrestricted persistence-diagram space has no coarse embedding into Hilbert space for every p in the remaining interval[1,2].

[Proof or source](../research/solutions/520-kaiwen-jin-coarse-persistence-diagrams/paper/main.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/520-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** Nonembeddability for all finite persistence diagrams with no cardinality or coordinate restriction, under each W_p metric with 1<=p<=2.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

Reference [1] explicitly leaves $`1\le p\le2`$ open and proves equivalence to the corresponding question for probability measures on the plane with finite $`p`$th moment. Known negative results for $`p>2`$, and positive results under a fixed cardinality bound, do not settle this question.

The landscape embedding [2] uses a different ground distance, while [3] gives Hilbert results on classes with specified growth and moment control. Neither supplies the required global controls for the metric above. Searches on 24 September 2026 found no matching resolution or announcement, including indexed arXiv, Zenodo, GitHub and Palomar searches.
