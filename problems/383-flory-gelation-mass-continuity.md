# 383. Continuity of finite-cluster mass at the onset of Flory gelation

**Area:** Coagulation equations; sol–gel phase transitions

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`0<\alpha<1`$ and let $`K:(0,\infty)^2\to[0,\infty)`$ be continuous and symmetric. Assume that for some $`0<c<C<\infty`$ and continuous $`\ell>0`$,

```math
c(x^\alpha y+xy^\alpha)\le K(x,y)\le C(x^\alpha y+xy^\alpha),\quad\lim_{y\to\infty}K(x,y)/y=\ell(x),\quad cx^\alpha\le\ell(x)\le Cx^\alpha.
```

Let $`\mu_0`$ be a finite nonnegative measure on $`(0,\infty)`$ with $`\int x\,d\mu_0=1`$. A Flory solution is a family of finite nonnegative measures with nonincreasing particle number and mass $`M_1(t)=\int x\,d\mu_t`$, satisfying for every $`\phi\in C_c([0,\infty))`$

```math
\langle\mu_t,\phi\rangle=\langle\mu_0,\phi\rangle+\frac12\int_0^t\!\iint K(x,y)[\phi(x+y)-\phi(x)-\phi(y)]\,d\mu_s(x)\,d\mu_s(y)\,ds-\int_0^t(1-M_1(s))\langle\mu_s,\ell\phi\rangle\,ds.
```

For every such solution whose gelation time $`T_g=\inf\{t:M_1(t)<1\}`$ satisfies $`0<T_g<\infty`$, must $`M_1`$ be continuous at $`T_g`$, with $`M_1(T_g)=\lim_{t\downarrow T_g}M_1(t)=1`$?

## Application

Mass missing from finite clusters represents a macroscopic gel. Continuity would mean that this giant component starts with zero mass and grows continuously, rather than appearing with a finite jump.

## References

1. N. Fournier and P. Laurençot, [*Marcus–Lushnikov processes, Smoluchowski's and Flory's models*](https://arxiv.org/abs/0706.2057), Stochastic Processes and their Applications 119 (2009), 167–189, §2, Assumption $`(A_\alpha)`$, Definition 2.2, Proposition 2.3 and the explicit open question immediately following it.
2. D. Heydecker and R. I. A. Patterson, [*Bilinear Coagulation Equations*](https://arxiv.org/abs/1902.07686), preprint, revised version (2019), Definition 1, Theorem 1 and §7.1, continuity for bilinear conserved-type kernels.
3. N. Fournier, [*On gelation for the Smoluchowski equation*](https://arxiv.org/abs/2501.03867), Comptes Rendus Mathématique 363 (2025), 583–591, finite-time gelation criteria; DOI [10.5802/crmath.738](https://doi.org/10.5802/crmath.738).

## Status review

Reviewed 15 October 2026 against the original target in [PR #148](https://github.com/MColbrook/AIM/pull/148). Finite-cluster mass is continuous and equals one at every finite positive onset of Flory gelation in the stated kernel class.

[Proof or source](../research/solutions/383-flory-gelation-mass-continuity/paper/flory_onset.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/383-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** Full affirmative answer for every weak solution and every 0<alpha<1, with only finite particle number and first moment.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

Checked on 22 September 2026 using continuity at gelation for strongly gelling Flory kernels and later bilinear-coagulation results. Fournier–Laurençot prove continuity strictly after gelation but explicitly leave the onset open. Heydecker–Patterson prove continuity under a bilinear representation in additive conserved particle types. General kernels in the displayed class do not possess that representation; even $`x^\alpha`$ is not additive under the merger $`x+y`$. The 2025 finite-gelation theorem determines occurrence, not continuity of mass at onset. No result covering the full stated kernel class was located.
