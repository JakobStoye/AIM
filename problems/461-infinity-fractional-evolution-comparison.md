# 461. Comparison for viscosity solutions of infinity-fractional diffusion

**Area:** Nonlinear parabolic PDEs; stochastic games

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Fix $`n\ge2`$, $`1/2<s<1`$ and $`T>0`$. For a unit vector $`e`$ set

```math
D_e^s\phi(x)=C_s\int_0^\infty\frac{\phi(x+re)+\phi(x-re)-2\phi(x)}{r^{1+2s}}\,dr,
```

where $`C_s>0`$ is fixed. Consider $`u_t=\Delta_\infty^s u`$ on $`\mathbb R^n\times(0,T)`$ with bounded uniformly continuous initial data. Use the following viscosity convention: at a test contact with nonzero spatial gradient the right-hand side is $`D_e^s\phi`$, $`e=\nabla\phi/|\nabla\phi|`$; at a zero-gradient contact, subsolutions satisfy $`\phi_t\le\sup_{|e|=1}D_e^s\phi`$, and supersolutions satisfy $`\phi_t\ge\inf_{|e|=1}D_e^s\phi`$. In every test, patch the test function with the tested solution outside a spatial neighborhood of the contact point.

For bounded continuous viscosity sub- and supersolutions $`u,v`$, attaining their initial data uniformly, does

```math
u(\cdot,0)\le v(\cdot,0)\quad\Longrightarrow\quad u(x,t)\le v(x,t)\quad\text{for all }(x,t)\in\mathbb R^n\times[0,T]?
```

No radial symmetry or monotonicity is assumed.

## Application

Comparison would make the continuum evolution associated with a non-Brownian tug-of-war game uniquely determined by its initial payoff.

## References

1. F. del Teso, J. Endal, E. R. Jakobsen and J. L. Vázquez, *Evolution driven by the infinity fractional Laplacian*, Calc. Var. PDE **62**, 136 (2023), viscosity definition, Theorem 2.6 and §§7, 9. [Article](https://doi.org/10.1007/s00526-023-02475-w); [preprint](https://arxiv.org/abs/2210.06414).

## Status review

Reviewed 15 October 2026 against the original target in [PR #154](https://github.com/MColbrook/AIM/pull/154). The specified relaxed infinity-fractional subsolution–supersolution comparison fails, even with identical smooth initial data.

[Proof or source](../research/solutions/461-relaxed-infinity-fractional-comparison/paper.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/461-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** The specified relaxed infinity-fractional subsolution–supersolution comparison fails, even with identical smooth initial data.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

The paper constructs viscosity solutions but leaves their general uniqueness/comparison unresolved. Its comparison theorem requires one solution to be classical, and its explicit classical families have special symmetry or monotonicity. Searches on 2026-09-22 for infinity-fractional parabolic comparison, uniqueness and later work of the authors found no result covering two arbitrary viscosity solutions with the stated zero-gradient convention. The local infinity heat equation and the stationary nonlocal equation are different problems.
