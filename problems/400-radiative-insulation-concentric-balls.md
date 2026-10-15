# 400. Concentric-ball optimality for thermal insulation with radiative heat transfer

**Area:** Elliptic PDEs / nonlinear boundary laws

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Fix $`n\ge2`$, $`\beta>0`$, $`\gamma\ge0`$ and $`R>1`$, and put

```math
\Theta(s)=\beta\left(s^5/5+\gamma s^4+2\gamma^2s^3+2\gamma^3s^2\right).
```

For a bounded Lipschitz open set $`\Omega\subset\mathbb R^n`$ and a measurable $`K\subset\Omega`$, define

```math
E_\Theta(K,\Omega)=\min_{\substack{v\in H^1(\Omega),\ 0\le v\le1\\v=1\ {\rm a.e.\ on}\ K}}\left(\int_\Omega|\nabla v|^2dx+\int_{\partial\Omega}\Theta(v)d\mathcal H^{n-1}\right).
```

Writing $`\omega_n=|B_1|`$, is the inequality

```math
E_\Theta(K,\Omega)\ge\min_{1\le r\le R}E_\Theta(B_1,B_r)
```

valid whenever $`|K|=\omega_n`$ and $`|\Omega|\le\omega_nR^n`$? For $`r=1`$ the right side uses $`K=\Omega=B_1`$, so unused insulation is allowed.

## Application

The boundary law represents Stefan–Boltzmann radiation into an environment at nonnegative temperature. The inequality would justify spherical designs when both the heated body and the amount of insulating material can be arranged freely.

## References

1. D. Bucur, M. Nahon, C. Nitsch and C. Trombetti, *Shape optimization of a thermal insulation problem*, Calculus of Variations and Partial Differential Equations 61 (2022), article 186, equations (1), (3), (4), Theorems 1–3 and the open question after Remark 4. [Full text](https://doi.org/10.1007/s00526-022-02298-1).
2. F. Della Pietra, C. Nitsch and C. Trombetti, *An optimal insulation problem*, Mathematische Annalen 382 (2022), 745–759, §1 energy formulation and §5 open shape questions. [Full text](https://doi.org/10.1007/s00208-020-02058-6).

## Status review

Reviewed 15 October 2026 against the original target in [PR #128](https://github.com/MColbrook/AIM/pull/128). Concentric-ball optimality for the full radiative insulation law.

[Proof or source](../research/solutions/400-radiative-insulation-concentric-balls/paper/main.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/400-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** The displayed inequality holds for every original dimension, parameter choice, measurable core and bounded Lipschitz outer set, including unused insulation.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

The primary source singles out radiative heat transfer as an unresolved instance of its constrained-volume concentric-ball question. It proves the quadratic convection law, all penalized-volume problems, and some inactive-constraint cases; those results do not establish the displayed inequality for the radiative law under an arbitrary volume budget. Searches through 22 September 2026 for nonlinear radiative insulation shape optimization and later work by the authors found no resolution.
