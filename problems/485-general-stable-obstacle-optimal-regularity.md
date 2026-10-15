# 485. Optimal obstacle regularity for stable jump kernels with only angular integrability

**Area:** Nonlocal obstacle problems; anisotropic jump processes

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`n\ge2`$, $`0<s<1`$, and $`0<\lambda\le\Lambda`$. Let $`a\in L^1(\mathbb S^{n-1})`$ be nonnegative and even, with

```math
\int_{\mathbb S^{n-1}}a(\theta)\,d\theta\le\Lambda,\qquad \inf_{e\in\mathbb S^{n-1}}\int_{\mathbb S^{n-1}}|e\cdot\theta|^2a(\theta)\,d\theta\ge\lambda.
```

Set $`K(y)=a(y/|y|)|y|^{-n-2s}`$ and

```math
\mathcal E_a(w)=\frac14\int_{\mathbb R^n}\int_{\mathbb R^n}|w(x)-w(x+y)|^2K(y)\,dy\,dx.
```

For any nonnegative $`\phi\in C_c^\infty(\mathbb R^n)`$, let $`u`$ be the unique minimizer of $`\mathcal E_a`$ over

```math
\{w\in L^{2n/(n-2s)}(\mathbb R^n):\mathcal E_a(w)<\infty,\ w\ge\phi\text{ almost everywhere}\}.
```

This is the finite-energy obstacle solution associated with $`Lu=\mathop{\mathrm{p.v.}}\nolimits\int(u(x)-u(x+y))K(y)\,dy`$. Does a constant $`C=C(n,s,\lambda,\Lambda)`$ always exist such that

```math
\|u\|_{C^{1,s}(\mathbb R^n)}\le C\|\phi\|_{C^3(\mathbb R^n)}?
```

Here the left side is $`\|u\|_\infty+\|\nabla u\|_\infty+\sup_{x\ne y}|\nabla u(x)-\nabla u(y)|/|x-y|^s`$. There is no assumption that $`a`$ belongs to any $`L^p`$ with $`p>1`$, or that the kernel is positive in every direction.

## Application

Nonlocal obstacle equations describe optimal stopping for jump processes and equilibria constrained by contact. The estimate would control sensitivity of the value or displacement gradient when jump directions are highly concentrated and have only integrable angular intensity.

## References

1. X. Fernández-Real and X. Ros-Oton, [*Integro-Differential Elliptic Equations*](https://doi.org/10.1007/978-3-031-54242-8), Progress in Mathematics 350, Birkhäuser (2024), §4.6.2, Open Question 4.3, and Theorem 4.5.1; [author draft](https://arxiv.org/abs/2411.12455), pp. 297 and 302.
2. X. Ros-Oton and M. Weidner, [*Obstacle problems for nonlocal operators with singular kernels*](https://arxiv.org/abs/2308.01695), Annali della Scuola Normale Superiore di Pisa, Classe di Scienze 27 (2026), 535–588, Theorem 1.3 and the open-problem paragraph immediately following it; DOI [10.2422/2036-2145.202309_010](https://doi.org/10.2422/2036-2145.202309_010).
3. X. Ros-Oton and M. Weidner, [*Optimal regularity for nonlocal elliptic equations and free boundary problems*](https://arxiv.org/abs/2403.07793), preprint (2024), equations (1.1)–(1.2) and Theorem 1.3.

## Status review

Reviewed 15 October 2026 against the original target in [PR #165](https://github.com/MColbrook/AIM/pull/165). The full support-independent global C^(1,s) obstacle estimate holds for the stated integrable angular-density class.

[Proof or source](../research/solutions/485-general-stable-obstacle-optimal-regularity/paper/main.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/485-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** The full support-independent global C^(1,s) obstacle estimate holds for the stated integrable angular-density class.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

Checked on 22 September 2026 using general stable obstacle regularity, angular $`L^1`$ kernels, and later 2025–2026 optimal-regularity results. The book explicitly asks for the general stable class. The singular-kernel paper proves the stated type of estimate under $`a\in L^p(\mathbb S^{n-1})`$ with $`p>n/(2s)`$ and expressly leaves mere $`L^1`$ ellipticity unresolved. Its 2026 journal publication is the publication of that result, not a removal of the angular-integrability hypothesis. The third paper allows nonhomogeneous radial behavior but retains two-sided pointwise comparison with the fractional-Laplacian kernel. That assumption excludes the angular concentrations here. No result removing the stronger angular assumption was located. This target uses a smooth obstacle and rough angular intensity; it is distinct from lowering the obstacle's smoothness for a pointwise elliptic kernel, and from the auxiliary positive-harmonic-profile classification in cones.
