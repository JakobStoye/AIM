# 434. Second-order Sobolev regularity of p-harmonic functions beyond the Cordes range

**Area:** Degenerate elliptic PDE regularity

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13
## Problem statement

For every $`p\ge5`$, every open $`\Omega\subset\mathbb R^3`$, and every weak solution $`u\in W^{1,p}_{\mathrm{loc}}(\Omega)`$ of $`\mathop{\mathrm{div}}\nolimits(|\nabla u|^{p-2}\nabla u)=0`$, must $`u\in W^{2,2}_{\mathrm{loc}}(\Omega)`$? Thus every distributional second derivative is required to belong locally to $`L^2`$, including neighborhoods of critical points where $`\nabla u=0`$.

## Application

Second derivatives control spatial changes of gradients in nonlinear conduction. Their square integrability supports sensitivity estimates and error analysis in regions where the constitutive law degenerates.

## References

1. P. Lindqvist, [Notes on the p-Laplace Equation](https://jyx.jyu.fi/bitstreams/2a8cbc94-58e9-4e75-94d6-0f1f5bc22ac1/download), second edition, University of Jyväskylä Report 161 (2017), §11, p. 93, “Second Derivatives,” and discussion preceding §4.
2. Q. H. Nguyen and L. X. Truong, [Higher Regularity of Homogeneous Gradient Compositions for p-Laplace-Type Equations](https://arxiv.org/abs/2608.11586), preprint (2026), Theorem 1.1 and comparison with unweighted derivative regularity.

## Status review

**Resolution reviewed 2026-10-13:** [Kaiwen Jin's manuscript](../research/solutions/434-p-harmonic-second-sobolev-derivatives/paper/main.pdf) establishes the full original target. Full unweighted local W2,2 regularity in dimension three for every finite p at least five.

**Independent review:** the [complete per-problem audit](../research/solution_reviews/2026-10-13-yui-prs/434-review.md) reconstructs the argument, compares its hypotheses and quantifiers with the original statement, and checks the cited sources and accompanying materials. The review was carried out by independent Codex AI agents during maintainer processing; it does not assert human peer review or Lean verification.

The reviewed submission is [PR #70](https://github.com/MColbrook/AIM/pull/70) at `2e3c856584ed33f10b88389dd0ff65b9518e88d6`. The original problem statement at `c9929805cece044705abaaebe1cebddac1ba11a6` was compared with its unchanged current form. The proof and documented independent audit meet the repository's **Solved** criterion; the original problem page and ID are retained.
