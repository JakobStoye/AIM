# 394. Villani’s convex-injectivity-domain conjecture

**Area:** Optimal transport / Riemannian geometry

**Status:** 🔵 OPEN

**Last checked:** 2026-10-16

## Problem statement

Let $`(M,g)`$ be a smooth compact connected Riemannian manifold without boundary. Write

```math
I_x=\{v\in T_xM:\exists t>1\text{ with }d(x,\exp_x(tv))=t|v|_g\}.
```

For $`v\in I_x`$ and $`\xi,\eta\in T_xM`$, define

```math
S_{x,v}(\xi,\eta)=-\frac32\left.\partial_s^2\partial_t^2\frac{d^2(\exp_x(t\xi),\exp_x(v+s\eta))}{2}\right|_{s=t=0}.
```

Assume $`S_{x,v}(\xi,\eta)\ge0`$ whenever $`\langle\xi,\eta\rangle_g=0`$; this is the weak Ma–Trudinger–Wang condition. Must $`I_x`$ be convex for every $`x\in M`$? No hypothesis excluding focal points on the cut locus is imposed.

## Application

Injectivity-domain convexity is a geometric prerequisite for continuous transport maps. It links the nonlinear PDE used to redistribute mass on curved surfaces and manifolds to the underlying geometry.

## References

1. A. Figalli, T. Gallouët and L. Rifford, *On the convexity of injectivity domains on nonfocal manifolds*, SIAM Journal on Mathematical Analysis 47 (2015), 969–1000, Definition 1.1, Theorem 1.7 and the following Villani conjecture. [Author manuscript](https://cvgmt.sns.it/media/doc/paper/2531/MTWTCLNF_final.pdf).
2. G. Khan and J. Zhang, *When Optimal Transport Meets Information Geometry*, preprint (2022), Conjecture 3. [arXiv:2206.14791](https://arxiv.org/abs/2206.14791).

## Status review

**Resolution-source report (2026-10-16):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-16-prior-resolutions.md#aim-394). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-22)

**Literature check:** Open in cited literature; no later resolution located.

The SIAM theorem proves the conclusion under the additional nonfocal assumption; the 2022 survey retains the general statement as a conjecture. Searches through 22 September 2026 included Villani MTW convexity, injectivity domains, focal cut loci, and the authors’ later work. Special manifolds and stability results for already regular transport do not resolve the unrestricted implication.
