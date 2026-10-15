# 126 — Pansu's isoperimetric conjecture in the Heisenberg group

**Area:** Sub-Riemannian geometric optimization

**Status:** 🔵 OPEN

**Last checked:** 2026-10-16

## Problem statement

On $`\mathbb R^3`$ with coordinates $`(x,y,t)`$, put $`X=\partial_x-\frac y2\partial_t`$ and $`Y=\partial_y+\frac x2\partial_t`$. For a measurable set $`E`$ define horizontal perimeter by

```math
P_H(E)=\sup\left\{\int_E(Xa+Yb)\,dx\,dy\,dt:
a,b\in C_c^1(\mathbb R^3),\ a^2+b^2\le1\right\}.
```

For $`R>0`$ define the bubble

```math
B_R=\left\{x^2+y^2<R^2,\quad
|t|<\tfrac14\left(r\sqrt{R^2-r^2}+R^2\arccos(r/R)\right)\right\},
\qquad r=\sqrt{x^2+y^2}.
```

Does every measurable $`E`$ of finite positive Lebesgue volume and finite horizontal perimeter satisfy $`P_H(E)\ge P_H(B_R)`$ when $`|E|=|B_R|`$? This asks for global optimality among all finite-perimeter sets, without symmetry or boundary-regularity assumptions.

## Application

The Heisenberg geometry is a basic model of constrained motion. A sharp perimeter inequality quantifies the least boundary cost for a prescribed accessible volume and controls related diffusion inequalities.

## References

1. L. Capogna, D. Danielli, S. D. Pauls and J. T. Tyson, *An Introduction to the Heisenberg Group and the Sub-Riemannian Isoperimetric Problem* (Birkhäuser, 2007), [Progress in Mathematics 259](https://doi.org/10.1007/978-3-7643-8133-2), Chapter 8, p. 152, equation (8.4) and the accompanying conjecture. Gives the bubble profile in this normalization.
2. R. L. Frank and B. Helffer, *On Courant and Pleijel theorems for sub-Riemannian Laplacians* (2025), [Journal de l'École polytechnique — Mathématiques 12](https://doi.org/10.5802/jep.307), §11.4. Retains Pansu's conjecture and reviews conditional results; its vector-field normalization differs by a central-coordinate scaling.

## Status review

**Resolution-source report (2026-10-16):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-16-prior-resolutions.md#aim-126). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-08)

**Literature check:** Open in cited literature; no later resolution located.

The 2025 treatment explicitly distinguishes the conjectured sharp constant from established bounds. Results for symmetric sets or sufficiently regular candidate minimizers leave the unrestricted class above unresolved. Searches included “Pansu conjecture Heisenberg isoperimetric solved 2025 2026” and “Heisenberg bubble global finite perimeter minimizer”. No general resolution was located.
