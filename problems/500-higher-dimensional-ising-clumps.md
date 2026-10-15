# 500. Ergodicity of higher-dimensional Ising clumps

**Area:** Applied topology and Markov-chain sampling

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

For $`d\ge2`$, let $`Q_z=z+[-1/2,1/2]^d`$, $`z\in\mathbb Z^d`$. A finite collection $`C`$ of these cubes is a *clump* if its union $`|C|`$ is contractible and regular. Here regular means that each $`x\in|C|`$ is either an interior point or has $`(B_\varepsilon(x)\cap|C|)\setminus\{x\}`$ contractible for every sufficiently small $`\varepsilon>0`$.

Use the state space $`\mathcal C_d`$ of all clumps containing the pinned cube $`Q_0`$. A cube $`Q\ne Q_0`$ may be removed from $`C`$ when $`C\setminus\{Q\}`$ is a clump and there is a strong deformation retraction

```math
H:|C|\times[0,1]\longrightarrow|C|
```

onto $`|C\setminus\{Q\}|`$, with $`H(Q\times[0,1])\subseteq Q`$. Addition is the inverse of such a removal. Each allowed addition has rate $`p_\uparrow\in(0,1]`$, and each allowed removal has rate $`p_\downarrow\in(0,1]`$.

Does the resulting continuous-time Markov chain satisfy the following extension of the planar theorem? For every $`d\ge2`$, it is irreducible on **all** of $`\mathcal C_d`$, and there is a finite positive constant $`\kappa(d)`$ such that, whenever $`\beta=p_\uparrow/p_\downarrow<1/\kappa(d)`$, it is nonexplosive and ergodic with stationary law

```math
\Pi_\beta(C)=Z_d(\beta)^{-1}\beta^{\#C},\qquad Z_d(\beta)=\sum_{C\in\mathcal C_d}\beta^{\#C}<\infty?
```

This is the higher-dimensional extension requested in Conjecture 6.9 of [1]. No assertion about a sharp threshold or a mixing-time rate is required.

## Application

These dynamics sample random geometric shapes while preserving topology. Irreducibility would ensure that every admissible pinned shape is accessible; ergodicity would justify long-run sampling from the size-weighted ensemble in higher dimensions.

## References

1. Y. Baryshnikov and E. Onaran, [Ising disks: topology preserving Glauber dynamics](https://doi.org/10.1007/s41468-026-00248-w), Journal of Applied and Computational Topology **10** (2026), article 16. Definitions 3.1–3.2 and 4.1–4.4, Lemma 4.3, §6, Theorem 6.5 and Conjecture 6.9; [author preprint](https://arxiv.org/abs/2410.22611).

## Status review

Reviewed 15 October 2026 against the original target in [PR #94](https://github.com/MColbrook/AIM/pull/94). A dimension-four counterexample refutes all-state irreducibility of the higher-dimensional clump dynamics.

[Proof or source](../research/solutions/500-higher-dimensional-ising-clumps/paper/cube_dynamics.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/500-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** For every positive choice of allowed rates, an admissible contractible regular four-dimensional clump has boundary group different from the singleton and lies in a distinct move component.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Known cases:** Theorem 6.5 of [1] proves the planar case. Lemma 4.3 and Corollary 4.5 show that the permitted removal and addition tests can be expressed locally.

**Remaining target:** The stated theorem in dimensions $`d\ge3`$, retaining all regular contractible clumps containing the pinned cube. Restricting the state space to the component already reachable from one cube would omit the central irreducibility question.

The published July 2026 paper states this extension as a conjecture. Searches on 23 September 2026 found no matching solution or announced counterexample.
