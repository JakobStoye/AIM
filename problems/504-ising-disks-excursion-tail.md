# 504. Exponential excursion tails for topology-preserving Ising disks

**Area:** Applied topology, stochastic geometry and rare-event sampling

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

For $`z\in\mathbb Z^2`$, put $`Q_z=z+[-1/2,1/2]^2`$. A finite collection $`C`$ of squares is a *clump* if its union $`|C|`$ is contractible and regular: every $`x\in|C|`$ is either interior or has $`(B_\varepsilon(x)\cap|C|)\setminus\{x\}`$ contractible for all sufficiently small $`\varepsilon>0`$.

Pin $`Q_0`$. A removal of $`Q\ne Q_0`$ is allowed if $`C\setminus\{Q\}`$ is a clump and $`|C|`$ strongly deformation retracts onto $`|C\setminus\{Q\}|`$ through a homotopy $`H`$ satisfying $`H(Q\times[0,1])\subseteq Q`$. Addition is the inverse move. Start the continuous-time chain $`C_t`$ at $`\{Q_0\}`$, with each allowed addition having rate $`\beta`$ and each allowed removal rate $`1`$.

Let $`a_n`$ count square-lattice self-avoiding polygons of enclosed area $`n`$, up to translation, and let $`\kappa=\lim_{n\to\infty}a_n^{1/n}`$ be their area growth constant. Fix $`0<\beta<1/\kappa`$. Let $`\zeta`$ be the first return time to $`\{Q_0\}`$ after the chain has left that state, and set

```math
\xi=\sup_{0\le t<\zeta}\#C_t.
```

Is the exact exponential excursion-height asymptotic

```math
\lim_{T\to\infty,\ T\in\mathbb N}\mathbb P(\xi\ge T)^{1/T}=\kappa\beta
```

valid for every such $`\beta`$?

Equivalently, for $`\mu=\mathbb E\zeta\in(0,\infty)`$ and $`\eta_T=\mu/\mathbb P(\xi\ge T)`$, the target is $`\lim_{T\to\infty}\eta_T^{1/T}=1/(\kappa\beta)`$.

## Application

The rate would quantify how rarely a topology-preserving shape sampler reaches a large number of cells during an excursion from its smallest state. It would also specify the exponential scale in the source's rare-event time normalization.

## References

1. Y. Baryshnikov and E. Onaran, [Ising disks: topology preserving Glauber dynamics](https://doi.org/10.1007/s41468-026-00248-w), Journal of Applied and Computational Topology **10** (2026), article 16. Definitions 3.1–3.2 and 4.1–4.4, §6, Definitions 7.1–7.3, Lemma 7.10 and Conjecture 7.11; [author preprint](https://arxiv.org/abs/2410.22611).

## Status review

Reviewed 15 October 2026 against the original target in [PR #92](https://github.com/MColbrook/AIM/pull/92). The exact exponential excursion-height rate is kappa*beta throughout the specified strict subcritical interval.

[Proof or source](../research/solutions/504-ising-disks-excursion-tail/paper/ising_disks_excursion.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/504-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** The full limit along all integer thresholds and the equivalent eta_T limit for every fixed 0<beta<1/kappa.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

Theorem 6.5 proves planar ergodicity in this parameter range. Lemma 7.10 gives only the lower bound $`\liminf\eta_T^{1/T}\ge1/(\kappa\beta)`$, equivalently the corresponding upper bound on the excursion-tail exponential rate. Conjecture 7.11 asks for equality. The already proved Poisson limit for suitably normalized rare events does not supply this missing normalization asymptotic.

This is distinct from [501](500-higher-dimensional-ising-clumps.md), which concerns irreducibility and ergodicity in higher dimensions. Searches on 23 September 2026, including indexed arXiv, Zenodo, GitHub and Palomar checks, located no matching solution or announcement.
