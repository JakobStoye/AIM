# 193. A continuous strictly decreasing moment spectrum for Gaussian polymers

**Area:** Polymers in random media

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`(S_n)`$ be simple random walk on $`\mathbb Z^3`$ from zero and let $`\omega_{n,x}`$ be iid standard Gaussians independent of the walk. For $`\beta>0`$, set

```math
W_N^\beta=E_S\exp\!\left(\sum_{n=1}^N(\beta\omega_{n,S_n}-\beta^2/2)\right),\qquad
p^*(\beta)=\sup\{p\ge1:\sup_N\mathbb E_\omega[(W_N^\beta)^p]<\infty\}.
```

Write $`W_\infty^\beta`$ for the nonnegative martingale limit and define $`\beta_c=\sup\{\beta:P(W_\infty^\beta>0)=1\}`$. Is $`\beta\mapsto p^*(\beta)`$ a continuous strictly decreasing bijection from $`(0,\beta_c]`$ onto $`[5/3,\infty)`$? Continuity at $`\beta_c`$ means continuity from the left.

## Application

In this random polymer model, partition-function moments describe fluctuations across environments. The conjecture would describe how the threshold for uniformly bounded moments changes with disorder. It does not by itself identify the exact disorder threshold for bounded variance or settle boundedness at the moment threshold.

## References

- [Quentin Berger, *Random polymers in random environment: an introduction to disordered systems*, lecture notes of 16 April 2026](https://www.math.univ-paris13.fr/~quentin.berger/documents/Disordered-Polymers.pdf), §3.3.2, Conjecture 3.32.
- [Stefan Junk, *Local limit theorem for directed polymers beyond the L2-phase* (2023 preprint, revised 2025)](https://arxiv.org/abs/2307.05097), finite-support and moment-threshold progress discussed in the notes.

## Status review

Reviewed 15 October 2026 against the original target in [PR #143](https://github.com/MColbrook/AIM/pull/143). The Gaussian three-dimensional polymer moment threshold is a continuous strictly decreasing bijection onto [5/3,infinity).

[Proof or source](../research/solutions/193-directed-polymer-moment-spectrum/paper.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/193-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** The Gaussian three-dimensional polymer moment threshold is a continuous strictly decreasing bijection onto [5/3,infinity).

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

The 2026 notes explicitly conjecture the full moment-spectrum statement. Results excluding constant intervals under a finite-support disorder assumption do not apply to Gaussian disorder. Fixing dimension three and the Gaussian law avoids treating different parameter instances as separate entries.

Search topics checked on 2026-09-08: directed polymer Gaussian p star moment spectrum continuity strict monotonicity 2026; Junk moment critical point conjecture.
