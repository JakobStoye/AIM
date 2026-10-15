# 413. Intercritical norm inflation for the dispersion-managed Schrödinger equation

**Area:** Nonlocal dispersive PDEs / nonlinear optics

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

On $`\mathbb R^3`$, consider the defocusing Gabitov–Turitsyn equation

```math
i\partial_tu-\Delta u+\int_0^1e^{-i\sigma\Delta}\left(|e^{i\sigma\Delta}u|^4e^{i\sigma\Delta}u\right)\,d\sigma=0.
```

For every $`\varepsilon>0`$, do there exist $`u_0\in\mathcal S(\mathbb R^3)`$ and a time $`t_\varepsilon`$ with $`0<|t_\varepsilon|<\varepsilon`$, lying in the smooth solution's interval of existence, such that

```math
\|u_0\|_{\dot H^{1/4}}<\varepsilon,\qquad \|u(t_\varepsilon)\|_{\dot H^{1/4}}>\varepsilon^{-1}?
```

Here $`u(0)=u_0`$, $`e^{i\sigma\Delta}`$ is the free Schrödinger group, and $`\|f\|_{\dot H^{1/4}}^2=\int|\xi|^{1/2}|\widehat f(\xi)|^2\,d\xi`$. This fixes one positive regularity strictly below the integrated scaling threshold $`s_i=1/2`$.

## Application

Dispersion management leads to an averaged, nonlocal wave equation for optical pulses. This higher-dimensional model asks whether fine-scale uncertainty can create arbitrarily large errors in very short propagation intervals; it tests the limits of stable prediction in the averaged equation.

## References

1. M. Kowalski, *On ill-posedness for the Gabitov–Turitsyn equation*, preprint (2025), equation (GT), Definition 1.3 and §6.4. [Full text](https://arxiv.org/html/2510.11887v1).
2. J. Kawakami and J. Murphy, *Small and large data scattering for the dispersion-managed NLS*, Discrete and Continuous Dynamical Systems 47 (2026), 256–285, introduction and scattering theorems. [DOI](https://doi.org/10.3934/dcds.2025118).
3. M.-R. Choi, Y. Hong and Y.-R. Lee, *Global existence versus finite time blowup dichotomy for the dispersion managed NLS*, Nonlinear Analysis 251 (2025), 113696, introduction and virial analysis. [DOI](https://doi.org/10.1016/j.na.2024.113696).

## Status review

Reviewed 15 October 2026 against the original target in [PR #132](https://github.com/MColbrook/AIM/pull/132). Schwartz Gaussian data give the exact requested homogeneous quarter-Sobolev norm inflation at nonzero arbitrarily short negative times.

[Proof or source](../research/solutions/413-intercritical-dispersion-managed-norm-inflation/paper/main.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/413-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** Schwartz Gaussian data give the exact requested homogeneous quarter-Sobolev norm inflation at nonzero arbitrarily short negative times.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

Kowalski explicitly leaves the intercritical regime unresolved. Failure of differentiability of the solution map, proved there, is weaker than the displayed norm inflation. The homogeneous norm and two-sided short time follow Definition 1.3; choosing s=1/4 avoids the conserved mass endpoint. Searches through 22 September 2026 found no proof or counterexample for this fixed defocusing model.
