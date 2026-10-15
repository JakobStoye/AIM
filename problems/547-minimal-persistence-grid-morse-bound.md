# 547. Minimal persistence grids versus homological Morse lower bounds

**Area:** Applied topology and inverse persistent homology

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Fix a field $`\Bbbk`$, an integer $`n\ge1`$, and a finite nonempty simplicial complex $`K`$ of dimension $`d`$. A filter assigns a vector $`f(\sigma)\in[0,1]^n`$ to every nonempty simplex, with $`f(\tau)\le f(\sigma)`$ coordinatewise whenever $`\tau\subseteq\sigma`$. Set

```math
K_u=\{\sigma\in K:f(\sigma)\le u\},\qquad M^q_u=H_q(K_u;\Bbbk),\qquad \mathbf M=(M^0,\ldots,M^d),
```

using ordinary unreduced homology and the maps induced by inclusions.

Let $`\xi_i^q(u)`$ be the multiplicity of a generator at grade $`u`$ in homological position $`i`$ of a minimal free resolution of the persistence module $`M^q`$. Here a free summand at $`u`$ is $`\Bbbk`$ at all grades $`v\ge u`$ and zero elsewhere, with identity maps between nonzero spaces. Equivalently, compute these multigraded Betti numbers after restricting to a finite grid determining the module and regrading its coordinate sets into $`\mathbb Z^n`$. Thus $`\xi_0^q`$ counts minimal generators, $`\xi_1^q`$ counts minimal relations, and higher $`i`$ count higher syzygies. Set $`\xi_i^q=0`$ for $`q<0`$ or $`q>d`$.

Define

```math
G_j=\bigcup_{q=0}^d\{u_j:\xi_0^q(u)+\xi_1^q(u)>0\},\qquad G=G_1\times\cdots\times G_n.
```

This is the minimal grid determining the entire tuple $`\mathbf M`$, not a chosen sampling grid. Boundary values $`0`$ and $`1`$ are included only if they occur in these coordinate sets. Put

```math
b_q(u)=\max\left\{0,\ \xi_0^q(u)+\xi_1^{q-1}(u)-\sum_{p=1}^{n-1}\xi_{p+1}^{q-p}(u)\right\},
```



```math
\mathcal L(\mathbf M)=\sum_{u\in G}\sum_{q=0}^d b_q(u).
```

Must every such filter satisfy

```math
|G_j|\le\mathcal L(\mathbf M)\qquad\text{for every }j=1,\ldots,n?
```

This is the conjecture in Remark 5.12 of [1]. The tuple must arise from a filter on a finite simplicial complex; the question is not asserted for arbitrary unrelated persistence modules. Filters may assign equal coordinate values to distinct simplices.

## Application

The question concerns information lost when filtrations are replaced by persistent homology. Let $`m`$ be the number of nonempty simplices of $`K`$. Reference [1] bounds the dimension of the space of filters realizing $`\mathbf M`$ by both $`nm-\sum_j|G_j|`$ and $`\frac n2(m-\mathcal L(\mathbf M))`$. Since $`\mathcal L(\mathbf M)\le m`$, the conjecture would guarantee that the latter bound is at least as strong. This would clarify how multigraded algebra controls ambiguity in inverse persistent homology; it does not by itself give a reconstruction algorithm.

## References

1. H. A. Harrington, U. Tillmann and M. Torras-Pérez, [The fiber of multiparameter persistent homology for simplicial complexes](https://arxiv.org/abs/2608.04640v1), preprint, version 1, 5 August 2026. See Lemma 1.23, Definitions 1.28 and 2.9, Definition 5.7, Proposition 5.9, Lemma 5.10 and Remark 5.12, pp.42–44.

## Status review

Reviewed 15 October 2026 against the original target in [PR #104](https://github.com/MColbrook/AIM/pull/104). The proposed Morse quantity bounds the largest coordinate size of the canonical minimal persistence grid.

[Proof or source](../research/solutions/547-minimal-persistence-grid-morse-bound/paper/grid_morse_bound.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/547-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** For every finite complex and the prescribed n-parameter persistence modules, L is at least max_j |G_j|, including dimension zero.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Known cases:** Reference [1] records the inequality for one parameter. It proves that a filter injective in every coordinate has $`|G_j|=\mathcal L(\mathbf M)=m`$, using Lemmas 4.21 and 5.10. These are cases of the displayed target.

**Remaining target:** Establish the inequality, or find a counterexample, for general multiparameter filters with coordinate coincidences. The higher-syzygy subtraction in $`b_q`$ prevents the minimal-presentation description of $`G`$ from immediately proving the bound.

The latest arXiv version found at the check date is v1, which explicitly poses the conjecture. No matching resolution or announcement was found. This is distinct from [problem 538](537-persistence-fiber-betti-numbers.md), which asks for the homology of a particular fiber, rather than a bound on minimal-grid sizes.
