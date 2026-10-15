# 040. Uniformly effective algebraic multigrid for diagonally dominant systems

**Area:** Numerical PDE solvers and preconditioning

**Status:** 🔵 OPEN

**Last checked:** 2026-10-16

## Problem statement

Let $`M\in\mathbb R^{n\times n}`$ be symmetric, $`M_{ij}\le0`$ for $`i\ne j`$, and $`M_{ii}\ge\sum_{j\ne i}|M_{ij}|`$. Require every row with equality to be connected, through nonzero off-diagonal entries, to a row with strict inequality. For a fixed positive integer $`c`$, assume $`|M_{ij}|\le n^c`$ and $`n^cM_{ij}\in\mathbb Z`$. These conditions make $`M`$ positive definite.

Construct an algebraic multigrid algorithm, with explicitly specified smoothing, interpolation and coarse-grid operators, whose setup takes $`\widetilde O(\mathop{\mathrm{nnz}}\nolimits M)`$ operations and whose symmetric approximate-inverse action $`z\mapsto Zz`$ takes $`O(\mathop{\mathrm{nnz}}\nolimits M)`$ operations, with

```math
aM^{-1}\preceq Z\preceq bM^{-1}
```

for constants $`0<a\le b<\infty`$ independent of $`n`$ and $`M`$. Here $`\preceq`$ is the positive-semidefinite order, $`\mathop{\mathrm{nnz}}\nolimits`$ counts nonzeros and $`\widetilde O`$ suppresses logarithms in $`n`$; constants may depend on fixed $`c`$.

## Application

This would give a uniformly convergent multilevel solver for a broad class of diffusion and network discretizations, with work proportional to the sparse input size per cycle.

## References

1. J. Xu and L. Zikatanov, [Algebraic multigrid methods](https://doi.org/10.1017/S0962492917000083), Acta Numerica 26 (2017), 591–721. Framework and convergence theory.
2. N. Amsel et al., [Linear Systems and Eigenvalue Problems: Open Questions from a Simons Workshop](https://arxiv.org/abs/2602.05394), 2026; Definitions 2.1–2.2 and Problem 2.3.

## Status review

**Literature check:** Open in cited literature; no later resolution located

Checked on **2026-09-08**. Problem 2.3 explicitly requests this AMG guarantee. General nearly linear Laplacian solvers do not automatically provide the specified multigrid structure. No subsequent solution was located.

Searches included: `SWCDDM multigrid 2026`; `SWCDDM multigrid`; `algebraic multigrid universal diagonally dominant open problem`. This is a documented literature check, not a certification that no solution exists.

**Qualified resolution-source report (2026-10-16):** [Public-source composition and exact locators](../research/literature_reports/2026-10-16-prior-resolutions.md#aim-040). The AI-prepared comparison allows high-probability randomized setup and non-Galerkin coarse matrices in exact randomized real arithmetic. The probability convention is an explicit interpretation, not a condition quoted from Problem 2.3, which the workshop source still lists as open. The report specifies the source-to-target translation and its limits; a deterministic guarantee is not established. The original statement and Open badge remain for maintainer review.
