# 112. Arbitrarily large Steklov frequency with a prescribed embedded boundary

**Area:** Geometric design of boundary-loaded media

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`d\ge1`$ and $`m\ge d+2`$. Fix a smooth compact connected embedded $`d`$-dimensional submanifold $`\Sigma\subset\mathbb R^m`$ without boundary, and assume that it bounds at least one smooth compact connected embedded $`(d+1)`$-dimensional submanifold. Let $`\mathcal F(\Sigma)`$ be the set of all such fillings $`\Omega\subset\mathbb R^m`$ with $`\partial\Omega=\Sigma`$, equipped with their induced Euclidean metrics. Prove or disprove

```math
\sup_{\Omega\in\mathcal F(\Sigma)}\sigma_1(\Omega)=\infty
```

for every such $`\Sigma`$, where $`\sigma_1`$ is the first positive eigenvalue of $`\Delta_\Omega u=0`$, $`\partial_\nu u=\sigma u`$. No bound is imposed on the filling’s volume or topology.

## Application

The boundary’s position and geometry are fixed, while the interior material surface can change. This asks whether those boundary data alone impose a ceiling on the lowest vibration frequency.

## References

1. B. Colbois, A. Girouard, C. Gordon and D. Sher, [Some recent developments on the Steklov eigenvalue problem](https://doi.org/10.1007/s13163-023-00480-3), Revista Matemática Complutense 37 (2024), §4.6, Open Question 4.52: prescribed-boundary submanifold problem.
2. B. Colbois, A. Girouard and K. Gittins, [Steklov eigenvalues of submanifolds with prescribed boundary in Euclidean space](https://arxiv.org/abs/1711.06458), preprint (2017), Theorem 1.11: upper estimates also depending on filling volume.
3. B. Colbois, A. Girouard and A. Métras, [Hypersurfaces of Euclidean space with prescribed boundary and small Steklov eigenvalues](https://arxiv.org/abs/1811.11463), preprint (2018), abstract and main theorem: the opposite, small-eigenvalue construction.

## Status review

Reviewed 15 October 2026 against the original target in [PR #135](https://github.com/MColbrook/AIM/pull/135). The affirmative result covers every admissible prescribed embedded boundary, including curves and filling codimension one.

[Proof or source](../research/solutions/112-fixed-embedded-boundary-steklov/paper/manuscript.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/112-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** For every d>=1 and m>=d+2, every fixed admissible embedded boundary admits smooth Euclidean-induced fillings with arbitrarily large first positive Steklov eigenvalue.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

The survey explicitly asks whether a fixed boundary permits unbounded first eigenvalues. The codimension and existence hypotheses above retain the nontrivial filling setting. Available volume-dependent upper bounds do not answer it when volume is free; constructions with eigenvalues tending to zero answer a different extremum.

**Search audit:** “Steklov prescribed embedded boundary arbitrarily large first eigenvalue”; “Colbois Girouard Gittins Open Question 4.52 2026”. Searches included proof, counterexample, and 2025–2026 updates. No later resolution of the stated problem was located; this is a literature review, not a proof of openness.
