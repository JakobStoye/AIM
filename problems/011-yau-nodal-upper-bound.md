# 011. Yau's sharp upper bound for nodal volume

**Area:** Eigenfunction geometry

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

For every closed connected $`C^\infty`$ Riemannian manifold $`(M,g)`$ of dimension $`d\ge2`$, does there exist $`C=C(M,g)`$ such that every nonzero real eigenfunction $`u`$ satisfying $`-\Delta_g u=\lambda u`$, $`\lambda>0`$, obeys

```math
\mathcal H^{d-1}_g\bigl(\{x\in M:u(x)=0\}\bigr)\le C\sqrt\lambda?
```

Here $`\mathcal H^{d-1}_g`$ is Hausdorff measure for the metric $`g`$. The constant must be uniform over all eigenvalues and all eigenfunctions, and no real-analyticity is assumed.

## Application

Nodal hypersurfaces are the stationary interfaces of high-frequency vibration patterns. A sharp bound quantifies their geometric complexity at the wavelength scale.

## References

1. A. Logunov, [Nodal sets of Laplace eigenfunctions: polynomial upper estimates of the Hausdorff measure](https://arxiv.org/abs/1605.02587), Annals of Mathematics 187 (2018), §1.
2. A. Logunov, [Nodal sets of Laplace eigenfunctions: proof of Nadirashvili's conjecture and of the lower bound in Yau's conjecture](https://arxiv.org/abs/1605.02589), Annals of Mathematics 187 (2018).
3. A. Logunov, E. Malinnikova, N. Nadirashvili and F. Nazarov, [The sharp upper bound for the area of the nodal sets of Dirichlet Laplace eigenfunctions](https://arxiv.org/abs/2104.09012), preprint (2021).

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Smooth-counterexamples-to-Yaus-nodal-upper-bound-in-dimensions-three-and-four-September-23-2026/paper.pdf), result family 350 (2026). Statement locator: `build/sections/introduction.tex, thm:main (S3 fixed-metric counterexample)`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete counterexample to the original target.

**Statement comparison:** One fixed smooth metric on the closed connected three-sphere has exact nonzero real Laplace eigenfunctions with positive eigenvalues tending to infinity and nodal area divided by $`\sqrt{\lambda}`$ tending to infinity. This refutes the universal target; the smooth-surface upper bound is an additional positive subcase.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-011) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/350.md). docs/350 describes fixed-metric counterexamples via SmoothYau (and a separate dimension-five YauCounterexample), as well as the surface theorem. No local kernel log inspected. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/011-yau-nodal-upper-bound.md).
