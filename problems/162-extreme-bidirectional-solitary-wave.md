# 162. An extreme solitary wave for the bidirectional Whitham system

**Area:** Nonlinear water-wave models

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`K`$ be the convolution kernel on $`\mathbb R`$ whose Fourier transform is $`\widehat K(\xi)=\tanh\xi/\xi`$, extended continuously at zero. Does there exist $`c>1`$ and an even continuous profile $`v:\mathbb R\to(0,\infty)`$, smooth away from zero, strictly decreasing for $`x>0`$, and tending to zero at infinity, such that

```math
K*v=c^2v-\frac{3c}{2}v^2+\frac12v^3,\qquad v(0)=c\left(1-\frac1{\sqrt3}\right)?
```

The associated surface profile is $`\eta=cv-v^2/2`$, with $`\eta(0)=c^2/3`$. These profiles yield a traveling solution $`(\eta(x-ct),v(x-ct))`$ of

```math
\partial_t\eta+\partial_x(K*v+\eta v)=0,\qquad\partial_tv+\partial_x(\eta+v^2/2)=0.
```

## Application

The question asks whether this bidirectional model has a solitary wave at its limiting crest height, a basic test of its treatment of extreme water waves.

## References

1. Mats Ehrnström, Ola I. H. Mæhlen and Kristoffer Varholm, *On the precise cusped behaviour of extreme solutions to Whitham-type equations*, Annales de l’Institut Henri Poincaré C 42 (2025), 125–162. [Article](https://doi.org/10.4171/AIHPC/104). Equations (1.2)–(1.3), §4 and Remark 4.8 explicitly leave extreme solitary-wave existence open.

2. Dag Nilsson and Yuexun Wang, *Solitary wave solutions to a class of Whitham–Boussinesq systems*, Zeitschrift für angewandte Mathematik und Physik 70 (2019), article 70. [Paper](https://arxiv.org/abs/1810.03405). Main theorem constructs small solitary waves.

## Status review

Reviewed 15 October 2026 against the original target in [PR #126](https://github.com/MColbrook/AIM/pull/126). An extreme solitary wave exists for the exact bidirectional Whitham model.

[Proof or source](../research/solutions/162-extreme-bidirectional-solitary-wave/paper/manuscript.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/162-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** The full prescribed positive, symmetric, monotone, zero-tail critical-crest traveling profile exists.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

Searches for “Whitham Boussinesq extreme solitary existence 2026” and “bidirectional Whitham highest solitary waves” located small-amplitude existence and periodic extreme waves, but no extreme solitary-wave construction for this specific system. Existence of highest solitary waves for the unidirectional Whitham equation is already known and is not the question recorded here.
