# 088. Absence of an infinite cluster at criticality in three-dimensional percolation

**Area:** Random media

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Independently retain each nearest-neighbor edge of $`\mathbb Z^3`$ with probability $`p`$. Let $`\theta(p)=\mathbb P_p(0\leftrightarrow\infty)`$ and $`p_c=\inf\{p\in[0,1]:\theta(p)>0\}`$, where $`0\leftrightarrow\infty`$ means that the open connected component containing the origin has infinitely many vertices. Prove or disprove

```math
\theta(p_c)=0.
```

The graph is the ordinary cubic lattice with only edges of Euclidean length one. This excludes long-range, hierarchical, slab and dependent percolation models.

## Application

The question asks whether the onset of macroscopic connectivity in a simple model of a porous medium is continuous.

## References

- [Tom Hutchcroft, *Power-law bounds for critical long-range percolation below the upper-critical dimension* (Probability Theory and Related Fields, 2021), introduction and discussion of nearest-neighbor percolation on Z³](https://doi.org/10.1007/s00440-021-01043-7).
- [Hugo Duminil-Copin, Vladas Sidoravicius and Vincent Tassion, *Absence of infinite cluster for critical Bernoulli percolation on slabs* (2014 preprint), introduction](https://www.ihes.fr/~duminil/publi/2014criticalslab.pdf).

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Critical-bond-and-site-percolation-on-the-cubic-lattice-September-24-2026/paper.pdf), result family 213 (2026). Statement locator: `Theorem 1.1, PDF page 1; Introduction theorem label thm:main, introduction.tex lines 17-22.`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** The theorem explicitly treats independent nearest-neighbor Bernoulli bond percolation on the ordinary cubic lattice Z^3 at its separately defined bond critical parameter. Almost surely no infinite cluster implies theta(p_c)=0. The additional site result is unnecessary for AIM coverage.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-088) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/213.md). CriticalZ3 comparator defines the cubic nearest-neighbor bonds and product Bernoulli law and states all critical clusters finite. Main comparator declaration uses sorry; no local verification claimed. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/088-critical-percolation-three-dimensions.md).
