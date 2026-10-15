# 482. Unconditional uniqueness for entropy-dissipating reaction–diffusion

**Area:** Reaction–diffusion PDEs; chemical kinetics

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`\Omega\subset\mathbb R^d`$, $`d\ge2`$, be bounded with smooth boundary, and let $`N\ge2`$, $`d_i>0`$. Let $`f:[0,\infty)^N\to\mathbb R^N`$ be locally Lipschitz, with $`f_i(z)\ge0`$ when $`z_i=0`$, and suppose some $`\mu\in\mathbb R^N`$ satisfies

```math
\sum_i f_i(z)(\log z_i+\mu_i)\le0\qquad(z_i>0).
```

No growth bound on $`f`$ is imposed. For nonnegative $`u_0`$ with $`\sum_i\int_\Omega u_{i,0}(1+|\log u_{i,0}|)<\infty`$, is the renormalized solution of

```math
\partial_tu_i=d_i\Delta u_i+f_i(u),\qquad\partial_\nu u_i=0,\qquad u_i(0)=u_{i,0},
```

unique?

Precisely, the comparison class consists of nonnegative $`u_i\in L^\infty(0,T;L^1)`$, $`\sqrt{u_i}\in L^2(0,T;H^1)`$ for every $`T<\infty`$, such that for each smooth $`\xi:[0,\infty)^N\to\mathbb R`$ with compactly supported $`D\xi`$, each smooth $`\psi`$ on $`\overline\Omega\times[0,T]`$, and almost every $`T`$,

```math
\begin{aligned}
\int_\Omega\xi(u(T))\psi(T)-\int_\Omega\xi(u_0)\psi(0)-\int_0^T\!\int_\Omega\xi(u)\partial_t\psi
={}&-\sum_{i,j}d_i\int_0^T\!\int_\Omega\psi\xi_{ij}(u)\nabla u_i\cdot\nabla u_j\\
&-\sum_i d_i\int_0^T\!\int_\Omega\xi_i(u)\nabla u_i\cdot\nabla\psi
+\sum_i\int_0^T\!\int_\Omega\xi_i(u)f_i(u)\psi .
\end{aligned}
```

Products of gradients are interpreted using $`\nabla u_i=2\sqrt{u_i}\nabla\sqrt{u_i}`$; the cutoff makes all displayed terms integrable. The question is equality almost everywhere of any two such solutions with the same initial data, without assuming that a bounded strong solution exists.

## Application

General reaction networks already admit global renormalized concentration fields. Uniqueness would make these weak predictions independent of the approximation used to construct them.

## References

1. J. Fischer, *Weak-strong uniqueness of solutions to entropy-dissipating reaction-diffusion equations*, Nonlinear Analysis **159** (2017), 181–207, Definition 2 and Theorem 7. [Author manuscript](https://arxiv.org/abs/1703.00730).
2. K. Fellner, J. Fischer, M. Kniely and B. Q. Tang, *Global renormalised solutions and equilibration of reaction–diffusion systems with nonlinear diffusion*, J. Nonlinear Sci. **33**, 66 (2023), Remark 1.4. [Article](https://doi.org/10.1007/s00332-023-09926-w).
3. A. Agresti, M. Kniely and B. Q. Tang, *Global classical solutions by transport noise for reaction–diffusion systems with entropy dissipation* (2026 preprint), §1.1. [Preprint](https://arxiv.org/abs/2608.13332).

## Status review

Reviewed 15 October 2026 against the original target in [PR #163](https://github.com/MColbrook/AIM/pull/163). The unrestricted finite-entropy renormalized reaction–diffusion uniqueness assertion is false.

[Proof or source](../research/solutions/entropy-cubic-nonuniqueness/paper.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/482-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** The unrestricted finite-entropy renormalized reaction–diffusion uniqueness assertion is false.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

Fischer proves uniqueness conditional on a strong solution, while the 2023 discussion and the August 2026 preprint explicitly retain unconditional uniqueness as unresolved. Searches on 2026-09-22 for renormalized reaction–diffusion uniqueness found further weak–strong results, including interface problems, but no unconditional theorem for this entropy class. This question fixes linear diffusion and concerns uniqueness; it does not restate the separate smooth-existence question for high-order mass-action reactions.
