# 429. An optimal Weyl remainder for interior transmission eigenvalues

**Area:** Transmission PDEs and wave scattering

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15
## Problem statement

Let $`\Omega\subset\mathbb R^d`$, $`d\ge2`$, be bounded, connected, with $`C^\infty`$ boundary, and fix a constant $`n>1`$. A nonzero number $`z`$ is an interior transmission eigenvalue if nonzero $`(u,v)`$ solve

```math
\Delta u+nzu=0,\quad\Delta v+zv=0\quad\text{in }\Omega,
```



```math
u=v,\qquad\partial_\nu u=\partial_\nu v\quad\text{on }\partial\Omega.
```

Use algebraic multiplicity for the closed transmission operator $`A(u,v)=(-n^{-1}\Delta u,-\Delta v)`$ on $`L^2(\Omega)\oplus L^2(\Omega)`$, with domain consisting of pairs whose distributional Laplacians lie in $`L^2`$ and whose Dirichlet and normal traces agree in the generalized trace sense. Algebraic multiplicity is the dimension of the Riesz spectral projection of $`A`$ around the nonzero eigenvalue. Let $`N(r)`$ count its nonzero eigenvalues with $`|z|\le r^2`$, including multiplicities. Must

```math
N(r)=\frac{\omega_d}{(2\pi)^d}|\Omega|(1+n^{d/2})r^d+O_{\Omega,n}(r^{d-1})\qquad(r\to\infty),
```

where $`\omega_d=|B_1|`$? This is the constant-index isotropic case of Vodev’s conjecture; no convexity is imposed.

## Application

Transmission eigenvalues describe frequencies at which an inclusion can fail to scatter selected incident waves. A sharp counting error measures how reliably mode density encodes the volume and refractive index.

## References

1. G. Vodev, [Asymptotic behavior of the transmission eigenvalues](https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/2045-04.pdf), *RIMS Kôkyûroku* **2045** (2017), 61–66, §7, Conjecture 1, equation (19).
2. V. Petkov and G. Vodev, [Asymptotics of the number of the interior transmission eigenvalues](https://www.math.u-bordeaux.fr/~vpetkov/publications/p-v2.pdf), *Journal of Spectral Theory* **7** (2017), §1, Theorem 1.1 and discussion of the remainder.

## Status review

Reviewed 15 October 2026 against the original target in [PR #142](https://github.com/MColbrook/AIM/pull/142). The constant-index transmission count has the sharp O(r^(d-1)) Weyl remainder at every sufficiently large exact radius.

[Proof or source](../research/solutions/429-transmission-eigenvalue-sharp-weyl-remainder/weyl_remainder.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/429-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** The constant-index transmission count has the sharp O(r^(d-1)) Weyl remainder at every sufficiently large exact radius.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

The conjecture asks to remove the positive power loss from the almost optimal $`O_\varepsilon(r^{d-1+\varepsilon})`$ remainder. Searches for transmission Weyl remainders, Vodev’s conjecture, and 2023–2026 asymptotics located general leading-term and special-geometry results, but no $`O(r^{d-1})`$ theorem for every smooth domain in this isotropic class.
