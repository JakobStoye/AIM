# 640. Coboundary expansion of random balanced Cayley complexes

**Area:** Applied topology / high-dimensional expansion
**Status:** ✅ SOLVED
**Last checked:** 2026-10-15

## Problem statement

Fix an integer $`k\ge2`$. For a finite group $`G`$, put

```math
D(G)=\sum_{\rho\in\widehat G}\dim\rho,
```

where $`\widehat G`$ indexes its irreducible complex representations. Form $`k+1`$ disjoint vertex sets $`V_i=\{i\}\times G`$. For $`A\subseteq G`$, let $`Y_{A,k}`$ contain the full $`(k-1)`$-skeleton of the join $`V_1*\cdots*V_{k+1}`$ and precisely the $`k`$-simplices

```math
\{(1,g_1),\ldots,(k+1,g_{k+1})\}\quad\text{with}\quad g_1\cdots g_{k+1}\in A.
```

Use simplicial cochains over $`\mathbb F_2`$, with coboundary $`\delta`$. For a cochain $`\phi`$, let $`|\phi|`$ count the faces on which it is nonzero, and write

```math
h_{k-1}(Y)=\min_{\phi\notin B^{k-1}(Y;\mathbb F_2)}
\frac{|\delta\phi|}{\min_{b\in B^{k-1}(Y;\mathbb F_2)}|\phi+b|},
\qquad B^{k-1}=\mathop{\mathrm{im}}\nolimits\delta_{k-2}.
```

Do constants $`C_k,\varepsilon_k>0`$ exist such that, for a uniformly random subset $`A\subseteq G`$ of size $`\lceil C_k\log D(G)\rceil`$,

```math
\Pr\{h_{k-1}(Y_{A,k})\ge\varepsilon_k\}\longrightarrow1
\quad\text{as }|G|\longrightarrow\infty?
```

The constants must work along every sequence of finite groups with orders tending to infinity. Counts in the expansion ratio are unnormalized.

## Application

Coboundary expansion controls how many local consistency checks a binary cochain violates relative to its distance from the coboundary space. This would give a general algebraic random construction with a quantitative guarantee for such checks.

## References

1. R. Meshulam, [Random balanced Cayley complexes](https://doi.org/10.1007/s41468-023-00137-6), Journal of Applied and Computational Topology **8** (2024), 1701–1721, Conjecture 8.1; §§1–2 and 8. [Author preprint](https://arxiv.org/abs/2211.02085).

## Status review

Reviewed 15 October 2026 against the original target in [PR #112](https://github.com/MColbrook/AIM/pull/112). Elementary abelian2-groups deterministically refute the proposed uniform random coboundary-expansion assertion.

[Proof or source](../research/solutions/640-random-balanced-cayley-obstruction/paper/main.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/640-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** For every fixed k>=2, all subsets A of the conjectured logarithmic size in sufficiently large binary vector groups have nonzero H^(k-1) over F2 and zero expansion.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Known cases:** The source proves an analogous real-coefficient spectral-gap estimate at this logarithmic sampling scale. In dimension one, that estimate and the graph Cheeger inequality give the corresponding coboundary-expansion conclusion.

**Remaining target:** The displayed binary-cochain bound in every fixed dimension $`k\ge2`$.

The proved real spectral gap does not supply the requested higher-dimensional bound over $`\mathbb F_2`$. Current searches found no matching solution or announcement. Results for different Cayley or balanced-product constructions do not establish the assertion for this specified random complex.
