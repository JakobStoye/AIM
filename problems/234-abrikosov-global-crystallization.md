# 234. Global optimality of the Abrikosov triangular lattice

**Area:** Superconductivity and Coulomb crystallization

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`\mathcal A_1`$ consist of planar vector fields $`E`$ satisfying, distributionally,

```math
\mathop{\mathrm{div}}\nolimits E=2\pi\left(\sum_{p\in\Lambda}\delta_p-1\right),\qquad\mathop{\mathrm{curl}}\nolimits E=0,
```

where $`\Lambda\subset\mathbb R^2`$ is locally finite and $`\sup_{R\geq1}\#(\Lambda\cap[-R,R]^2)/R^2<\infty`$. The fields are locally square-integrable away from the points. Fix smooth cutoffs $`0\leq\chi_R\leq1`$, equal to one on $`[-R+1,R-1]^2`$, supported in $`[-R,R]^2`$, with uniformly bounded gradient. Define

```math
W(E)=\limsup_{R\to\infty}\frac1{4R^2}\lim_{\eta\downarrow0}\left[\frac12\int_{\mathbb R^2\setminus\bigcup_{p\in\Lambda}B(p,\eta)}\chi_R|E|^2\,dx+\pi\log\eta\sum_{p\in\Lambda}\chi_R(p)\right].
```

Let $`\Lambda_\triangle=\sqrt{2/\sqrt3}\,[\mathbb Z(1,0)+\mathbb Z(1/2,\sqrt3/2)]`$ and let $`E_\triangle`$ be the mean-zero periodic field in $`\mathcal A_1`$ associated to it. Is $`W(E)\geq W(E_\triangle)`$ for every $`E\in\mathcal A_1`$? No periodicity is required of competitors.

## Application

The energy describes the microscopic arrangement of vortices in type-II superconductors and point charges in a neutralizing background. Global optimality would derive the observed triangular pattern without assuming a lattice in advance.

## References

- Sylvia Serfaty, [*Ginzburg–Landau vortices, Coulomb gases, and Abrikosov lattices*](https://doi.org/10.1016/j.crhy.2014.06.001) (2014), Theorem 1 and Conjecture 1: optimality among lattices and the open global extension.
- Simona Rota Nodari and Sylvia Serfaty, [*Renormalized energy equidistribution and local charge balance in 2D Coulomb systems*](https://math.nyu.edu/~serfaty/REG_V12.pdf) (2013 manuscript), §1.1, Definitions 1, 3 and 4: precise admissible fields and renormalized-energy normalization; the introduction states the unresolved crystallization question.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Triangular-minimality-for-planar-Coulomb-renormalized-energy-September-23-2026/paper.pdf), result family 090 (2026). Statement locator: `Theorem thm:main; definitions eq:cutoffs, eq:admissible, eq:local-energy, eq:whole-energy`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** This companion is a separate direct theorem matching the Sandier-Serfaty/Abrikosov target. It uses the same divE=2*pi(sum delta-1), curlE=0, unit background, fixed-width smooth square cutoffs, puncture limit before limsup, self-energy pi*log(eta), normalization 4R^2, and covolume-one triangular field. Its density bound on centered disks is equivalent to AIM square growth bound by disk-square inclusions and local finiteness. The source derives local Lq (q<2) from the equations and permits nonperiodic competitors and infinite energies.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-234) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/090.md). Family090 Lean docs cover Gaussian minorants/universal nonnegative pair energies and circle packing, not this renormalized Coulomb field theorem; no full AIM234 Lean certificate established. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/234-abrikosov-global-crystallization.md).
