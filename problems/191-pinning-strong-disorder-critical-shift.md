# 191. Strong disorder versus a shifted pinning threshold

**Area:** Disordered polymers and adsorption

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`\tau=\{0=\tau_0<\tau_1<\cdots\}`$ be a renewal process with iid gaps satisfying

```math
P(\tau_1=n)=\frac{n^{-5/4}}{\sum_{m\ge1}m^{-5/4}}\quad(n\ge1).
```

Let $`(\omega_n)`$ be independent standard Gaussians, independent of $`\tau`$. Define

```math
Z_{N,h}^{\beta,\omega}=E_\tau\exp\!\left(\sum_{n=1}^N(\beta\omega_n+h)\mathbf1_{\{n\in\tau\}}\right),\qquad
F(\beta,h)=\lim_{N\to\infty}\frac1N\mathbb E_\omega\log Z_{N,h}^{\beta,\omega}.
```

Put $`h_c(\beta)=\inf\{h:F(\beta,h)>0\}`$. The normalized partition function $`W_N=Z_{N,-\beta^2/2}^{\beta,\omega}`$ is a nonnegative martingale; write $`W_\infty`$ for its almost-sure limit.

For every $`\beta>0`$, does $`P(W_\infty=0)=1`$ imply $`h_c(\beta)>-\beta^2/2`$?

## Application

The question asks whether strong randomness at the annealed adsorption threshold must measurably shift the true polymer-pinning transition.

## References

- [Quentin Berger, *Random Interfaces and Pinning Models*, lecture notes of 4 March 2026](https://www.math.univ-paris13.fr/~quentin.berger/documents/Random-Interfaces.pdf), §4.2, Conjecture 4.9.
- [Giambattista Giacomin, *Random Polymer Models* (Imperial College Press, 2007)](https://doi.org/10.1142/P504), monograph background for disordered renewal pinning.

## Status review

Reviewed 15 October 2026 against the original target in [PR #146](https://github.com/MColbrook/AIM/pull/146). For the specified Gaussian pinning model, strong disorder implies a strictly positive quenched–annealed critical-point shift.

[Proof or source](../research/solutions/191-pinning-strong-disorder-critical-shift/paper/manuscript.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/191-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** For the specified Gaussian pinning model, strong disorder implies a strictly positive quenched–annealed critical-point shift.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

This is a fixed Gaussian, renewal-exponent alpha=1/4 case of Berger's explicit conjecture for alpha≠0. The notes distinguish this unresolved pinning statement from recent resolutions of strong-versus-very-strong disorder for directed polymers in a bulk random environment.

Search topics checked on 2026-09-08: pinning strong very strong disorder coincide conjecture 2026; pinning martingale critical point shift alpha less than half.
