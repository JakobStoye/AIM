# 424. Reality of the spectrum for a spherical strip with PT-symmetric boundary conditions

**Area:** Waveguides and nonselfadjoint boundary PDEs

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15
## Problem statement

For $`0<a<\pi/2`$, $`\alpha\in\mathbb R`$, and $`m\in\mathbb Z`$, put $`\beta=\tfrac12\tan a`$ and define on $`L^2(-a,a)`$

```math
H_{a,\alpha,m}u=-u''+\frac{8m^2-3-\cos(2x)}{8\cos^2x}\,u,
```



```math
D(H_{a,\alpha,m})=\{u\in H^2(-a,a):u'(\pm a)+(i\alpha\pm\beta)u(\pm a)=0\}.
```

Is $`\sigma(H_{a,\alpha,m})\subset\mathbb R`$ for every such triple? These separated operators represent the Laplace–Beltrami problem on a tubular neighborhood of the equator with the parity-and-time symmetric Robin conditions of the references.

## Application

Curved waveguides with balanced boundary gain and loss lead to nonselfadjoint modes. Spectral reality would identify a geometry in which this balance preserves real frequencies at every mode and boundary strength.

## References

1. P. Siegl, [PT-symmetric Laplace–Beltrami operator in the strip on a sphere](https://nsa.fjfi.cvut.cz/problems/01_ESF_2010/2010-10/2010-10_ESF_Siegl.pdf), ESF nonselfadjoint spectral theory problem 2010-10, equation (2).
2. D. Krejčiřík and P. Siegl, [PT-symmetric models in curved manifolds](https://arxiv.org/abs/1001.2988), *Journal of Physics A* **43** (2010), 485204, §4.4.2 and Propositions 4.3–4.4.

## Status review

Reviewed 15 October 2026 against the original target in [PR #139](https://github.com/MColbrook/AIM/pull/139). Purely real spectrum for every requested spherical strip width, real Robin parameter and integer mode.

[Proof or source](../research/solutions/424-spherical-pt-robin-real-spectrum/paper/spherical_robin_real_spectrum.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/424-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** Strict Robin--Dirichlet interlacing, the characteristic-ratio half-plane sign, and an actual bounded inverse off the real axis establish the full spectrum assertion.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

The paper proves reality for the comparison operator without its potential and for eigenvalues with sufficiently large real part. The remaining low-lying spectrum is the explicit question in the problem note. Searches for spherical PT Robin spectral reality and later Krejčiřík–Siegl work through the review date located no all-parameter proof or counterexample.
