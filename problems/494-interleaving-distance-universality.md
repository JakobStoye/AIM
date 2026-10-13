# 494. Universality of the interleaving distance over arbitrary fields

**Area:** Applied topology and multiparameter persistent homology

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`k`$ be a field, $`n\ge1`$ and $`i\ge0`$. An $`n`$-parameter persistence module is a functor $`M:(\mathbb R^n,\le)\to\mathrm{Vect}_k`$, where the order is coordinatewise. Write $`\mathbf1=(1,\ldots,1)`$, $`M(\varepsilon)_a=M_{a+\varepsilon\mathbf1}`$, and let $`\eta_M^{2\varepsilon}:M\to M(2\varepsilon)`$ be its structure morphism. Modules $`M,N`$ are $`\varepsilon`$-interleaved if there are natural transformations

```math
\varphi:M\to N(\varepsilon),\qquad \psi:N\to M(\varepsilon)
```

satisfying

```math
\psi(\varepsilon)\circ\varphi=\eta_M^{2\varepsilon},\qquad
\varphi(\varepsilon)\circ\psi=\eta_N^{2\varepsilon}.
```

Define $`d_I(M,N)`$ as the infimum of such $`\varepsilon\ge0`$, with value $`+\infty`$ if none exists.

For a topological space $`X`$ and a function $`f:X\to\mathbb R^n`$, let

```math
P_i(f)_a=H_i(\{x\in X:f(x)\le a\};k),
```

using ordinary singular homology and the maps induced by sublevel-set inclusions. Functions need not be continuous. Let $`\mathcal R_{n,i}(k)`$ consist of modules isomorphic to some $`P_i(f)`$.

Call an extended pseudometric $`d`$ on isomorphism classes of $`n`$-parameter modules **$`i`$-stable** if, for every $`X`$ and every pair $`f,g:X\to\mathbb R^n`$,

```math
d(P_i(f),P_i(g))\le\sup_{x\in X}\|f(x)-g(x)\|_\infty.
```

An extended pseudometric is symmetric, vanishes on the diagonal and satisfies the triangle inequality, but may take value $`+\infty`$ or vanish on distinct classes. The supremum for empty $`X`$ is zero.

**Conjecture.** For every field $`k`$, every $`n\ge1`$ and every $`i\ge0`$, each $`i`$-stable extended pseudometric satisfies

```math
d(M,N)\le d_I(M,N)\qquad\text{for all }M,N\in\mathcal R_{n,i}(k).
```

The interleaving distance itself is $`i`$-stable. Thus the assertion is its maximality among stable distances on realizable modules. The realizability restriction is part of the conjecture; no finite-dimensionality assumption is imposed. This is Lesnick's Conjecture 5.7 with its definition of $`i`$-universality made explicit.

## Application

Multiparameter persistent homology describes data while varying several thresholds, such as geometric scale and density. The conjecture asks whether the interleaving distance retains the greatest discrimination compatible with uniform perturbation stability, regardless of the coefficient field. It concerns the mathematical justification for comparing these descriptors; it would not supply an efficient distance-computation algorithm.

## References

1. S. Y. Oudot, *Persistence Theory: From Quiver Representations to Data Analysis*, AMS, 2015, §3.1.2, pp. 52–54. [Author-provided book](https://geometrica.saclay.inria.fr/team/Steve.Oudot/books/o-pt-fqrtda-15/surv-209.pdf).
2. M. Lesnick, *The Theory of the Interleaving Distance on Multidimensional Persistence Modules*, Foundations of Computational Mathematics **15** (2015), 613–650. [Published article](https://doi.org/10.1007/s10208-015-9255-y); [author manuscript](https://arxiv.org/abs/1106.5305), version 4, §§5.1–5.2, Theorem 5.5 and Conjecture 5.7.
3. M. B. Botnan and M. Lesnick, *An Introduction to Multiparameter Persistence*, [survey](https://arxiv.org/abs/2203.14289), version 2, 13 March 2023, Definition 6.6, Theorem 6.7 and Remark 6.8(4).
4. A. J. Blumberg and M. Lesnick, *Universality of the Homotopy Interleaving Distance*, Transactions of the American Mathematical Society **376** (2023), 8269–8307. [Article](https://doi.org/10.1090/tran/8738); [manuscript](https://arxiv.org/abs/1705.01690). Its universality theorem concerns filtered spaces and homotopy invariance.

## Status review

**Resolution reviewed 2026-10-13:** [Kaiwen Jin's manuscript](../research/solutions/494-degree-zero-interleaving-counterexample/paper/interleaving_counterexample.pdf) establishes the full original target. Negative: degree-zero universality fails for the unrestricted multi-parameter interleaving target.

**Independent review:** the [complete per-problem audit](../research/solution_reviews/2026-10-13-yui-prs/494-review.md) reconstructs the argument, compares its hypotheses and quantifiers with the original statement, and checks the cited sources and accompanying materials. The review was carried out by independent Codex AI agents during maintainer processing; it does not assert human peer review or Lean verification.

The reviewed submission is [PR #85](https://github.com/MColbrook/AIM/pull/85) at `22d05af29e9febd77cceb59298889c1c8ad64d96`. The original problem statement at `c9929805cece044705abaaebe1cebddac1ba11a6` was compared with its unchanged current form. The proof and documented independent audit meet the repository's **Solved** criterion; the original problem page and ID are retained.
