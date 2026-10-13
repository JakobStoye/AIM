# 615. Fourth-order diffusion approximation for three-player ruin

**Area:** Applied probability and diffusion approximation

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Three players start with positive integer capitals $`A,B,C`$. At each step, choose uniformly among pairs of surviving players, toss a fair coin, and transfer one unit from the loser to the winner. Remove a player when their capital reaches zero. Let $`P_{A,B,C}(\sigma)`$ be the probability of elimination order $`\sigma\in S_3`$, with the final winner listed last.

Write $`N=A+B+C`$ and let

```math
P^{\rm BM}_{A,B,C}(\sigma)=\lim_{m\to\infty}P_{mA,mB,mC}(\sigma),
```

whose existence follows from the Brownian diffusion limit. For every fixed $`A,B,C`$ and $`\sigma`$, is

```math
\left|P_{nA,nB,nC}(\sigma)-P^{\rm BM}_{A,B,C}(\sigma)\right|=O\!\left((nN)^{-4}\right)\qquad(n\to\infty)?
```

The implied constant may depend on the fixed capital proportions and elimination order. This is Conjecture 4.2(b) of Diaconis and Ethier.

## Application

Elimination probabilities enter fair allocation of tournament prizes. A quantitative diffusion approximation would certify the accuracy of replacing a large finite-state computation by a Brownian boundary-value problem.

## References

1. P. Diaconis and S. N. Ethier, [Gambler's Ruin and the ICM](https://doi.org/10.1214/21-STS826), *Statistical Science* **37**(3) (2022), 289–305. [Author manuscript](https://arxiv.org/abs/2011.07610), Section 4.1, Theorem 4.1 and Conjecture 4.2(b).
2. D. Denisov and V. Wachtel, [Harmonic measure in a multidimensional gambler's problem](https://doi.org/10.1214/24-AAP2069), *Annals of Applied Probability* **34**(5) (2024), 4387–4407. [Author manuscript](https://arxiv.org/html/2212.11526v1), Proposition 5 and the following paragraph.

## Status review

**Resolution reviewed 2026-10-13:** [Kaiwen Jin's manuscript](../research/solutions/615-gambler-scaling/paper/gambler_scaling.pdf) establishes the full original target. Full affirmative resolution of the exact target.

**Independent review:** the [complete per-problem audit](../research/solution_reviews/2026-10-13-yui-prs/615-review.md) reconstructs the argument, compares its hypotheses and quantifiers with the original statement, and checks the cited sources and accompanying materials. The review was carried out by independent Codex AI agents during maintainer processing; it does not assert human peer review or Lean verification.

The reviewed submission is [PR #81](https://github.com/MColbrook/AIM/pull/81) at `312df9569f5265fd7a85dfe7f7c1b5300cb5765b`. The original problem statement at `c9929805cece044705abaaebe1cebddac1ba11a6` was compared with its unchanged current form. The proof and documented independent audit meet the repository's **Solved** criterion; the original problem page and ID are retained.
