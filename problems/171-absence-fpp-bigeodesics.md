# 171. Absence of doubly infinite minimizing paths in planar first-passage percolation

**Area:** Optimal transport through random media

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Assign independent mean-one exponential times to the nearest-neighbor edges of $`\mathbb Z^2`$, and let $`T(x,y)`$ be the minimum path time. A bigeodesic is an injective path $`(v_k)_{k\in\mathbb Z}`$ such that, for every pair of integers $`i<j`$,

```math
\sum_{k=i}^{j-1}\tau_{\{v_k,v_{k+1}\}}=T(v_i,v_j).
```

Is the probability that any bigeodesic exists equal to zero? There is no restriction on its direction, and both ends lie in the full plane.

## Application

A bigeodesic would be an indefinitely extending optimal transport channel in a disordered medium. Excluding such channels clarifies the geometry of optimal routes.

## References

- [Antonio Auffinger, Michael Damron and Jack Hanson, *50 Years of First-Passage Percolation* (AMS University Lecture Series 68, 2017); author manuscript](https://sites.math.duke.edu/~rtd/FPP/50yrsFPP.pdf), §4.5, Question 31.
- [Barbara Dembin, Dor Elboim and Ron Peled, *Coalescence of Geodesics and the BKS Midpoint Problem in Planar First-Passage Percolation* (2024)](https://doi.org/10.1007/s00039-024-00672-z), introduction and bigeodesic discussion.
- [Michael Damron and Jack Hanson, *Bigeodesics in first-passage percolation* (2015 preprint)](https://arxiv.org/abs/1512.00804), directional and conditional results.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/main.pdf), result family 212 (2026). Statement locator: `Theorem 1.1, PDF page 1; Introduction theorem label thm:main, 01-introduction.tex lines 24-37.`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** The no-bigeodesics theorem rules out all injective doubly infinite nearest-neighbor minimizing paths simultaneously for every nonnegative nonatomic iid weight law satisfying E[min(X1,X2,X3,X4)^2]<infinity. Mean-one exponential weights satisfy this hypothesis (their minimum has rate4 and finite second moment). No direction restriction or shape assumption occurs.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-171) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/212.md). Family212 selected Lean docs only cover differentiability of limit shapes; no bigeodesic comparator is linked. No full AIM171 formalization/verification supported. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/171-absence-fpp-bigeodesics.md).
