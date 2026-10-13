# 584. Extending a symmetric one-dependent four-color law across a branch

**Area:** Applied probability and random graph coloring

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`G`$ have vertices $`\{o,a,b,v_1,v_2,\ldots\}`$ and edges $`oa`$, $`ob`$, $`ov_1`$ and $`v_jv_{j+1}`$ for $`j\ge1`$. Thus two arms of the three-arm star have length one and the third is infinite.

Can there exist a random proper four-coloring $`X`$ of $`G`$ and a stationary proper four-coloring $`Y=(Y_j)_{j\in\mathbb Z}`$ such that both are one-dependent, both laws are invariant under all permutations of the color names, $`Y`$ is also reflection-invariant, and for every ordered simple path $`(w_1,\ldots,w_m)`$ in $`G`$,

```math
(X_{w_1},\ldots,X_{w_m})\ \stackrel{\mathrm{law}}=\ (Y_1,\ldots,Y_m)?
```

Here one-dependence means that restrictions to vertex sets at graph distance greater than one are independent. Prove nonexistence or construct such a pair $`(X,Y)`$. The line law $`Y`$ is not prescribed to be the known Holroyd–Liggett law.

This is the minimal branched-ray case of [1, Section 6, question 1]. Nonexistence on $`G`$ implies nonexistence when either finite arm is extended, by restriction.

## Application

The question asks whether a symmetric random assignment with no dependencies beyond adjacent sites can remain locally identical to a line process when a network acquires a branch. It probes a precise obstruction to transferring one-dimensional random scheduling and coloring constructions to networks.

## References

1. T. M. Liggett and W. Tang, [One-dependent colorings of the star graph](https://doi.org/10.1214/22-AAP1920), *Annals of Applied Probability* **33**(6A) (2023), 4341–4365. Proposition 1.4, its following discussion, and Section 6, question 1; [author manuscript](https://arxiv.org/abs/1804.06877).

## Status review

**Resolution reviewed 2026-10-13:** [Kaiwen Jin's manuscript](../research/solutions/584-four-color-branched-ray/paper/main.pdf) establishes the full original target. Complete nonexistence proof on the two-leaf branched ray for an arbitrary symmetric common line law.

**Independent review:** the [complete per-problem audit](../research/solution_reviews/2026-10-13-yui-prs/584-review.md) reconstructs the argument, compares its hypotheses and quantifiers with the original statement, and checks the cited sources and accompanying materials. The review was carried out by independent Codex AI agents during maintainer processing; it does not assert human peer review or Lean verification.

The reviewed submission is [PR #80](https://github.com/MColbrook/AIM/pull/80) at `0415b9d841373ea4b7bd78b9d5e84adc9c569b6d`. The original problem statement at `c9929805cece044705abaaebe1cebddac1ba11a6` was compared with its unchanged current form. The proof and documented independent audit meet the repository's **Solved** criterion; the original problem page and ID are retained.
