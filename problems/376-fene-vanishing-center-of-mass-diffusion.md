# 376. The zero center-of-mass diffusion limit for kinetic FENE fluids

**Area:** Polymer kinetics; singular diffusion limits

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`x\in\mathbb T^3`$, $`q\in B_1(0)\subset\mathbb R^3`$, $`\nu>0`$, $`k>2`$, $`U(q)=-k\log(1-|q|^2)`$ and $`M=Z^{-1}e^{-U}`$. For $`\varepsilon>0`$ consider

```math
u_t+u\cdot\nabla_xu-\nu\Delta_xu+\nabla_xp=\nabla_x\cdot\tau,\quad\nabla_x\cdot u=0,
```



```math
\psi_t+u\cdot\nabla_x\psi=\varepsilon\Delta_x\psi+\nabla_q\cdot\left[\nabla_q\psi+\psi\nabla_qU-(\nabla_xu)q\psi\right],\qquad \tau=\int_{B_1}q\otimes\nabla_qU\,\psi\,dq,
```

with zero configuration-space flux. Fix smooth divergence-free $`u_0`$ and $`\psi_0=M g_0`$, where $`g_0`$ is smooth and bounded above and below by positive constants and $`\int_{B_1}\psi_0(x,q)\,dq=1`$. Can global finite-entropy weak solutions $`(u_\varepsilon,\psi_\varepsilon)`$ be chosen so that, along some $`\varepsilon_j\downarrow0`$, they converge to a global weak solution of exactly the same system with $`\varepsilon=0`$? Require $`u_{\varepsilon_j}\to u`$ strongly in $`L^2`$ on finite time intervals, $`\psi_{\varepsilon_j}\rightharpoonup\psi`$ weakly in $`L^1`$ there, and convergence of the stress and transport fluxes to those computed from $`(u,\psi)`$ in distributions, with no additional defect. Finite entropy means $`\int\psi\log(\psi/M)<\infty`$ and the usual kinetic-fluid entropy inequality.

## Application

Center-of-mass diffusion represents translational Brownian motion of polymer molecules. The limit tests whether omitting this small physical effect is consistent with the full kinetic fluid model for large data.

## References

1. T. Dębiec and E. Süli, [*On a Class of Generalised Solutions to the Kinetic Hookean Dumbbell Model for Incompressible Dilute Polymeric Fluids: Existence and Macroscopic Closure*](https://doi.org/10.1007/s00205-025-02115-x), Archive for Rational Mechanics and Analysis 249 (2025), article 43, §1, discussion of FENE center-of-mass diffusion and its unresolved zero-diffusion limit.
2. N. Masmoudi, [*Global existence of weak solutions to the FENE dumbbell model of polymeric flows*](https://arxiv.org/abs/1004.4015), Inventiones Mathematicae 191 (2013), 427–500, global existence without center-of-mass diffusion.

## Status review

Reviewed 15 October 2026 against the original target in [PR #138](https://github.com/MColbrook/AIM/pull/138). The conditional-density argument establishes a subsequential vanishing-center-of-mass-diffusion limit for the complete stated periodic three-dimensional FENE target.

[Proof or source](../research/solutions/376-fene-vanishing-center-of-mass-diffusion/paper/main.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/376-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** For arbitrary prescribed data in the stated smooth bounded-positive normalized class, every nu>0 and k>2, selected global positive-diffusion solutions have a subsequence converging to the identical full noncorotational zero-diffusion system, with strong L2 velocity, strong L1 density and stress, the original fluxes, initial data and initial-time entropy inequality.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

Checked on 22 September 2026 using FENE weak-solution convergence as center-of-mass diffusion tends to zero. The 2025 primary paper explicitly says that this passage from diffusive to nondiffusive weak solutions is unknown. Existence at each fixed diffusion value and Masmoudi's separate construction at zero diffusion do not supply convergence. Vanishing solvent-viscosity limits, small perturbations of equilibrium, and macroscopic FENE-P approximation results change the limit or the model. No large-data kinetic compactness theorem giving the displayed defect-free limit was located.
