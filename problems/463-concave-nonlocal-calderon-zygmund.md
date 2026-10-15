# 463. Calderón–Zygmund estimates for general concave nonlocal equations

**Area:** Fully nonlinear nonlocal PDEs; integrable forcing

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Fix $`n\ge2`$, $`0<s<1`$, and $`0<\lambda\le\Lambda`$. Let $`\{K_a\}_{a\in A}`$ be any family of even measurable kernels satisfying

```math
\lambda|y|^{-n-2s}\le K_a(y)\le\Lambda|y|^{-n-2s}.
```

Set $`L_au(x)=\mathop{\mathrm{PV}}\nolimits\int[u(x)-u(x+y)]K_a(y)dy`$ and $`Iu=\inf_{a\in A}(-L_au)`$.

Is there a finite $`p_*=p_*(n,s,\lambda,\Lambda)`$ such that, for every $`p>\max\{2,p_*\}`$, bounded viscosity solutions of $`Iu=f`$ in $`B_1`$ with smooth $`f`$ satisfy

```math
\|u\|_{W^{2s,p}(B_{1/2})}\le C\bigl(\|u\|_{L^\infty(\mathbb R^n)}+\|f\|_{L^p(B_1)}\bigr),
```

where $`C`$ depends only on $`n,s,p,\lambda,\Lambda`$? Use the Slobodeckij Sobolev space for noninteger $`2s`$ and the ordinary Sobolev space when $`2s=1`$. The estimate must be uniform over the kernels and must not depend on stronger norms of $`f`$.

## Application

The estimate would quantify spatial regularity under integrable forcing for nonlinear effective diffusion and controlled jump models.

## References

1. X. Fernández-Real and X. Ros-Oton, *Integro-Differential Elliptic Equations*, Progress in Mathematics **350**, Birkhäuser (2024). [Book](https://doi.org/10.1007/978-3-031-54242-8); [author manuscript](https://arxiv.org/abs/2411.12455).

2. S. Kitano, *$`W^{\sigma,p}`$ a priori estimates for fully nonlinear integro-differential equations* (2022), Introduction and kernel hypotheses. [Author preprint](https://arxiv.org/abs/2207.06728).

## Status review

Reviewed 15 October 2026 against the original target in [PR #150](https://github.com/MColbrook/AIM/pull/150). The proposed kernel-uniform full-order Sobolev estimate fails at every finite sufficiently large p for strict ellipticity pairs.

[Proof or source](../research/solutions/463-concave-nonlocal-sobolev-counterexample/paper/manuscript.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/463-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** The proposed kernel-uniform full-order Sobolev estimate fails at every finite sufficiently large p for strict ellipticity pairs.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

Open Question 3.2 in §3.6.2 asks for this nonlocal $`W^{2s,p}`$ theory at sufficiently large $`p`$. The smooth-source estimate is a precise necessary form of that proposed theory and avoids ambiguity about viscosity solutions with discontinuous right sides. Searches on 2026-09-22 found restricted matrix-kernel and linear-operator estimates, but no estimate uniform over the general concave class. The separate ABP entry controls the maximum of a subsolution; here the target is a full-order Sobolev norm of solutions.
