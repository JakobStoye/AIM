# 194. A uniform gap for the spin-one Heisenberg chain

**Area:** Quantum magnetism

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

For each even integer $`N\ge4`$, put a three-dimensional spin space at every site of a periodic chain. On $`\mathbb C^3`$, indexed by $`m=-1,0,1`$, define $`S^z|m\rangle=m|m\rangle`$, $`S^+|m\rangle=\sqrt{2-m(m+1)}|m+1\rangle`$ (zero at $`m=1`$), $`S^-=(S^+)^*`$, $`S^x=(S^++S^-)/2`$, and $`S^y=(S^+-S^-)/(2i)`$. Let

```math
H_N=\sum_{j=1}^{N}\sum_{a=x,y,z}S_j^aS_{j+1}^a,\qquad S_{N+1}^a=S_1^a.
```

Write $`E_0(N)<E_1(N)`$ for its lowest two distinct eigenvalues. Prove or disprove that there is a constant $`\Delta>0`$, independent of even $`N`$, such that $`E_1(N)-E_0(N)\ge\Delta`$.

## Application

A positive excitation threshold distinguishes an integer-spin quantum magnet from a gapless chain and underlies the robustness of the Haldane phase in magnetic materials.

## References

1. F. D. M. Haldane, [Continuum dynamics of the 1-D Heisenberg antiferromagnet: identification with the O(3) nonlinear sigma model](https://www.sciencedirect.com/science/article/pii/037596018390631X), Physics Letters A 93 (1983), 464–468: original physical gap prediction.
2. H. Tasaki, [The Ground State of the S=1 Antiferromagnetic Heisenberg Chain is Topologically Nontrivial if Gapped](https://arxiv.org/abs/2407.17041), preprint (2024; revised December 2024), introduction and Main results: explicitly unproved gap assumption, and a conditional topological theorem.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-periodic-spin-one-Haldane-gap-September-24-2026/paper.pdf), result family 268 (2026). Statement locator: `build/introduction.tex, thm:main and immediately following small-chain paragraph`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** Identical pure spin-one antiferromagnetic coupling-one Hamiltonian on even periodic rings and next distinct eigenvalue convention. The positive bound holds for every even N>=60. Taking the minimum with the finitely many positive finite-dimensional gaps N=4,...,58 gives the required all-N uniform positive gap.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-194) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** No corresponding complete Lean development was identified in the linked family record; no Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/194-haldane-gap.md).
