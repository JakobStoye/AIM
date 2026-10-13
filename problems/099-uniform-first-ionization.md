# 099. Uniform boundedness of the first atomic ionization energy

**Area:** Atomic spectroscopy

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

For $`Z>0`$ and $`N\ge1`$, let $`E(N,Z)`$ be the infimum of the spectrum of

```math
H_{N,Z}=\sum_{j=1}^N\left(-\frac12\Delta_{x_j}-\frac Z{|x_j|}\right)+\sum_{1\le i<j\le N}\frac1{|x_i-x_j|}
```

on the antisymmetric space $`\bigwedge^N L^2(\mathbb R^3;\mathbb C^2)`$, with its standard quadratic-form realization. Set $`E(0,Z)=0`$.

For neutral atoms with integer $`Z\ge1`$, the first ionization energy is

```math
I_1(Z)=E(Z-1,Z)-E(Z,Z).
```

Prove or disprove that $`\sup_{Z\in\mathbb N}I_1(Z)<\infty`$. The nuclear mass is infinite and electron spin has exactly two states.

## Application

This is a precise question about the energy needed to remove the outermost electron. It concerns a spectral energy difference, distinct from the maximum number of bound electrons.

## References

1. J. P. Solovej, [A new look at Thomas–Fermi Theory](https://arxiv.org/abs/1601.00497), Molecular Physics 114 (2016), discussion of the ionization conjecture and equation defining $`I_m(Z)`$: explicit bounded-ionization-energy problem.
2. J. P. Solovej, [The ionization conjecture in Hartree–Fock theory](https://doi.org/10.4007/annals.2003.158.509), Annals of Mathematics 158 (2003), introduction and main results: approximate-model comparison.
3. J. P. Solovej, [Mathematics of complex atoms and the periodic table](https://www.math.uci.edu/node/38671), research colloquium abstract (15 May 2026): current explicit open-status statement.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Uniform-excess-charge-for-Coulomb-molecules-and-the-outer-radius-of-neutral-atoms-September-24-2026/paper.pdf), result family 263 (2026). Statement locator: `build/sections/01-introduction.tex, cor:first-ionization`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** The first-ionization corollary proves universal two-sided positive bounds for neutral integer-Z atoms with exactly the target kinetic and spin normalization. Its upper bound settles the whole supremum question.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-099) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/263.md). docs/263 explicitly excludes fixed-m convergence; the selected comparators do not establish the first-ionization bound. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/099-uniform-first-ionization.md).
