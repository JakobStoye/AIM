# 139 — Sharp characterization of exactly trackable boundary heat fluxes

**Area:** PDE control / thermal flux tracking

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`\Omega\subset\mathbb R^d`$, $`d\ge2`$, be bounded and connected with smooth boundary. Fix $`T>0`$ and nonempty relatively open boundary patches $`\Gamma,\Sigma`$ with disjoint closures. For $`u\in L^2((0,T)\times\Gamma)`$ let $`y_u`$ be the transposition solution of

```math
\partial_ty_u-\Delta y_u=0,\qquad y_u(0,\cdot)=0,\qquad
y_u|_{\partial\Omega}=\mathbf1_\Gamma u.
```

Define the exactly trackable flux space

```math
\mathcal R_T=\{\partial_\nu y_u|_{(0,T)\times\Sigma}:
u\in L^2((0,T)\times\Gamma)\},
```

where $`\nu`$ is the outward normal. Characterize $`\mathcal R_T`$ by necessary and sufficient regularity and compatibility conditions on the target flux itself, including the sharp quantitative restrictions near $`t=0`$. Merely restating membership as existence of a control or an abstract dual inequality is not the requested function-space characterization.

## Application

The problem identifies precisely which temperature-flux histories can be imposed on an inaccessible boundary by heating a separate accessible boundary.

## References

1. J. A. Bárcena-Petisco and E. Zuazua, *Tracking Controllability for the Heat Equation* (2025), [IEEE Transactions on Automatic Control 70, 1935–1940](https://doi.org/10.1109/TAC.2024.3476174) ([author manuscript](https://arxiv.org/abs/2310.00314)), §II, paragraph after equation (16), and Lemma IV.2. Explicitly leaves the sharp trackable space open; gives sufficient Gevrey conditions in one dimension.
2. J. Apraiz, J. A. Bárcena-Petisco and J. Muñoz-Matute, *Tracking controllability on moving targets for parabolic equations* (2026), [arXiv:2603.28449](https://arxiv.org/abs/2603.28449), abstract and introduction. Extends approximate tracking to moving observation targets.

## Status review

**Resolution reviewed 2026-10-13:** [Kaiwen Jin's manuscript](../research/solutions/139-sharp-heat-tracking-range/paper/heat_tracking.pdf) establishes the full original target. Explicit target-only exact range characterization and sharp geometry-dependent initial-time evaluation scale.

**Independent review:** the [complete per-problem audit](../research/solution_reviews/2026-10-13-yui-prs/139-review.md) reconstructs the argument, compares its hypotheses and quantifiers with the original statement, and checks the cited sources and accompanying materials. The review was carried out by independent Codex AI agents during maintainer processing; it does not assert human peer review or Lean verification.

The reviewed submission is [PR #49](https://github.com/MColbrook/AIM/pull/49) at `b87f79b5a7bf638d4b2833a4245c014b11d76718`. The original problem statement at `c9929805cece044705abaaebe1cebddac1ba11a6` was compared with its unchanged current form. The proof and documented independent audit meet the repository's **Solved** criterion; the original problem page and ID are retained.
