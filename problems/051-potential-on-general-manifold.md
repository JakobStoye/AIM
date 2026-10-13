# 051 — Recover a potential on a general known Riemannian manifold

**Area:** Inverse boundary problems / anisotropic wave media

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`(M,g)`$ be any known compact connected smooth Riemannian manifold of dimension $`n\geq3`$ with smooth nonempty boundary. For real $`q\in C^\infty(M)`$, assume zero is not a Dirichlet eigenvalue of $`-\Delta_g+q`$. Define

```math
\Lambda_{g,q}f=\partial_{\nu_g}u|_{\partial M},\qquad
(-\Delta_g+q)u=0,\quad u|_{\partial M}=f.
```

Must $`\Lambda_{g,q_1}=\Lambda_{g,q_2}`$ imply $`q_1=q_2`$ for every such manifold and pair of potentials? The metric is fixed and known; the map is measured at the single frequency zero.

## Application

This separates recovery of an absorption or reaction coefficient from recovery of a known anisotropic background geometry in boundary imaging.

## References

1. *Dirichlet-to-Neumann Maps: Spectral Theory, Inverse Problems and Applications*, BIRS workshop report (2016), section “Variants of the anisotropic Calderón's problem.” [Report](https://www.birs.ca/cmo-workshops/2016/16w5083/report16w5083.pdf).
2. S. Ma, S. K. Sahoo and M. Salo, *The anisotropic Calderón problem at large fixed frequency on manifolds with invertible ray transform*, Journal of the London Mathematical Society **110** (2024), e13006, introduction. [Paper](https://doi.org/10.1112/jlms.13006); [preprint](https://arxiv.org/abs/2207.02623).

## Status review

**Resolution reviewed 2026-10-13:** [Kaiwen Jin's manuscript](../research/solutions/051-potential-on-general-manifold/paper/main.pdf) establishes the full original target. Full smooth real potential uniqueness on every known smooth manifold under the original nonresonance assumption.

**Independent review:** the [complete per-problem audit](../research/solution_reviews/2026-10-13-yui-prs/051-review.md) reconstructs the argument, compares its hypotheses and quantifiers with the original statement, and checks the cited sources and accompanying materials. The review was carried out by independent Codex AI agents during maintainer processing; it does not assert human peer review or Lean verification.

The reviewed submission is [PR #71](https://github.com/MColbrook/AIM/pull/71) at `8ac038c0eb03ee265826ad268aa458f7513ab27a`. The original problem statement at `c9929805cece044705abaaebe1cebddac1ba11a6` was compared with its unchanged current form. The proof and documented independent audit meet the repository's **Solved** criterion; the original problem page and ID are retained.
