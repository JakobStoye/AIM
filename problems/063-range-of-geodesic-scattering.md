# 063 — Characterizing realizable geodesic scattering data

**Area:** Geometric inverse problems and data consistency

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Fix a smooth disk $`M`$ and a boundary metric $`h`$. Write $`B_h^*\partial M=\{(x,\eta)\in T^*\partial M:|\eta|_h<1\}`$. Every smooth simple metric $`g`$ inducing $`h`$ gives a scattering map $`\alpha_g:B_h^*\partial M\to B_h^*\partial M`$: extend $`\eta`$ to the inward unit covector, follow its geodesic, and record the exit point and tangential exit covector. Simplicity means strictly convex boundary and unique smoothly varying geodesics between points.

Give necessary and sufficient conditions, expressed entirely in terms of a proposed boundary map $`A`$ and $`h`$, for $`A=\alpha_g`$ for some such $`g`$. The conditions must give an intrinsic characterization rather than restate the existence of an interior metric.

## Application

A range characterization would identify which measured ray directions can arise from a smooth medium and supply consistency tests for reconstruction.

## References

1. G. P. Paternain, M. Salo and G. Uhlmann, *Geometric Inverse Problems: With Emphasis on Two Dimensions* (2023), §15.1, problem 2. [Open problems chapter](https://doi.org/10.1017/9781009039901.018).
2. Jan Bohr and Gabriel P. Paternain, *The Transport Oka–Grauert Principle for Simple Surfaces*, Journal de l'École polytechnique — Mathématiques **10** (2023), 727–769. [DOI](https://doi.org/10.5802/jep.231).

## Status review

**Resolution reviewed 2026-10-13:** [Kaiwen Jin's manuscript](../research/solutions/063-geodesic-scattering/paper/geodesic_scattering.pdf) establishes the full original target. Qualitative intrinsic necessary-and-sufficient characterization of all simple Riemannian scattering maps for the fixed boundary metric.

**Independent review:** the [complete per-problem audit](../research/solution_reviews/2026-10-13-yui-prs/063-review.md) reconstructs the argument, compares its hypotheses and quantifiers with the original statement, and checks the cited sources and accompanying materials. The review was carried out by independent Codex AI agents during maintainer processing; it does not assert human peer review or Lean verification.

The reviewed submission is [PR #66](https://github.com/MColbrook/AIM/pull/66) at `70fea40cdc7c8555a835feab3ff4882a1fcf7139`. The original problem statement at `c9929805cece044705abaaebe1cebddac1ba11a6` was compared with its unchanged current form. The proof and documented independent audit meet the repository's **Solved** criterion; the original problem page and ID are retained.
