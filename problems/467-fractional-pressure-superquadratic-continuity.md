# 467. Continuity for degenerate fractional-pressure porous-medium flow

**Area:** Nonlocal PDEs; degenerate diffusion regularity

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Fix $`N\ge2`$, $`m>2`$ and $`0<s<1`$.

On $`\mathbb R^N`$ use the model

```math
u_t=\nabla\cdot(u^{m-1}\nabla p),\qquad p=(-\Delta)^{-s}u,
```

where the inverse fractional Laplacian has Fourier multiplier $`|\xi|^{-2s}`$. Take nonzero, nonnegative $`u_0\in L^1\cap L^\infty`$ with compact support. By a bounded energy weak solution mean a nonnegative distributional solution with the initial trace $`u_0`$, continuous into $`L^1`$ with its weak topology, conserving $`\int u_0`$, and satisfying $`\|u(t)\|_\infty\le\|u_0\|_\infty`$, locally integrable flux, and

```math
\frac12\|(-\Delta)^{-s/2}u(t)\|_2^2+
\int_0^t\!\int u^{m-1}|\nabla(-\Delta)^{-s}u|^2
\le\frac12\|(-\Delta)^{-s/2}u_0\|_2^2.
```

Use also the dissipative $`L^q`$ inequalities, for every $`q>1`$,

```math
\|u(t)\|_q^q+\frac{4q(q-1)}{(m+q-1)^2}\int_0^t\|(-\Delta)^{(1-s)/2}u^{(m+q-1)/2}\|_2^2\,dr\le\|u_0\|_q^q.
```

Does every bounded energy weak solution admit a representative continuous on $`\mathbb R^N\times(0,\infty)`$? Continuity must hold across the boundary of the set $`\{u>0\}`$, not merely inside that set.

## Application

Continuity would justify a well-defined evolving density and interface for nonlocal infiltration laws whose mobility degenerates strongly at vacuum.

## References

1. D. Stan, F. del Teso and J. L. Vázquez, *Porous medium equation with nonlocal pressure* (2018), Definition 2.1, Theorems 5.1–5.5, Remark 7 and §7. [Author preprint](https://arxiv.org/abs/1801.04244).
2. D. Stan, F. del Teso and J. L. Vázquez, *Existence of weak solutions for a general porous medium equation with nonlocal pressure*, Arch. Ration. Mech. Anal. (2019), existence and energy estimates. [Author preprint](https://arxiv.org/abs/1609.05139).
3. F. del Teso and E. R. Jakobsen, *A Convergent Finite Difference-Quadrature Scheme for the Porous Medium Equation with Nonlocal Pressure*, Found. Comput. Math. (2026), §2's review of the PDE theory. [Article](https://doi.org/10.1007/s10208-026-09752-y).

## Status review

Reviewed 15 October 2026 against the original target in [PR #153](https://github.com/MColbrook/AIM/pull/153). For 1/2<s<1 and m>2 an existing bounded energy weak solution cannot have the requested global jointly continuous representative.

[Proof or source](../research/solutions/467-fractional-pressure-continuity-counterexample/paper/main.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/467-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** Full negative answer; a concrete admissible parameter/data witness is N=2,m=3,s=3/4,u0=indicator of the unit ball.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

Section 7 of the survey identifies continuity of weak solutions beyond $`m=2`$ as unresolved. Searches on 2026-09-22 for continuity, Hölder regularity and superquadratic mobility found no theorem covering this class. The known $`m=2`$ Hölder theory and regularity of $`u_t+(-\Delta)^s(u^m)=0`$ do not apply: the latter places the nonlinearity inside a different operator. This is a regularity question rather than another uniqueness or existence entry.
