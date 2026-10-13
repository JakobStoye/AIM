# 010. The Mercedes-star partition of a disk

**Area:** Spectral partitions

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`B=\{x\in\mathbb R^2:|x|<1\}`$. Among triples of pairwise disjoint nonempty connected open subsets $`(D_1,D_2,D_3)`$ of $`B`$, minimize $`\max_i\lambda_1(D_i)`$, where $`\lambda_1`$ is the first Dirichlet eigenvalue. Prove or disprove that the three sectors obtained by three radii separated by angles $`2\pi/3`$ attain the minimum. Equivalently, is

```math
\inf_{(D_1,D_2,D_3)}\max_i\lambda_1(D_i)=j_{3/2,1}^2?
```

Here $`j_{3/2,1}`$ is the first positive zero of the Bessel function $`J_{3/2}`$. The optimization is over all such triples, with no prescribed interface topology or symmetry.

## Application

This provides a concrete three-cell benchmark for partition algorithms used to balance fundamental modes. It isolates the finite-cell geometry behind asymptotic honeycomb design.

## References

1. V. Bonnaillie-Noël and B. Helffer, [On spectral minimal partitions: the disk revisited](https://www.math.ens.psl.eu/~bonnaillie/articles/BoHe13.pdf), Annals of the University of Bucharest, mathematical series (2013), introduction.
2. G. Berkolaiko, Y. Canzani, G. Cox and J. L. Marzuola, [Homology of spectral minimal partitions](https://doi.org/10.1112/jlms.70065), Journal of the London Mathematical Society 111 (2025), introduction and disk example; [preprint](https://arxiv.org/abs/2406.04225).

## Status review

**Resolution reviewed 2026-10-13:** [Kaiwen Jin's manuscript](../research/solutions/010-mercedes-disk-partition/paper/mercedes_partition.pdf) establishes the full original target. The unrestricted three-cell disk partition minimum equals the Mercedes-sector eigenvalue and is attained.

**Independent review:** the [complete per-problem audit](../research/solution_reviews/2026-10-13-yui-prs/010-review.md) reconstructs the argument, compares its hypotheses and quantifiers with the original statement, and checks the cited sources and accompanying materials. The review was carried out by independent Codex AI agents during maintainer processing; it does not assert human peer review or Lean verification.

The reviewed submission is [PR #60](https://github.com/MColbrook/AIM/pull/60) at `533508074cd44bc0117d6a936853db0d259e25e2`. The original problem statement at `c9929805cece044705abaaebe1cebddac1ba11a6` was compared with its unchanged current form. The proof and documented independent audit meet the repository's **Solved** criterion; the original problem page and ID are retained.
