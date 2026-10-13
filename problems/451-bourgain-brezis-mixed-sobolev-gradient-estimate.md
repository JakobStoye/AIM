# 451. A mixed Sobolev estimate for reconstructing a scalar potential

**Area:** Elliptic potential reconstruction and critical function spaces

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13
## Problem statement

For every integer $`d\ge2`$, is there $`C_d<\infty`$ such that every real $`\psi\in C^\infty(\mathbb T^d)`$ with $`\int_{\mathbb T^d}\psi=0`$ satisfies

```math
\|\psi\|_{H^{1/2}(\mathbb T^d)+W^{1,1}(\mathbb T^d)}\le C_d\|\nabla\psi\|_{H^{-1/2}(\mathbb T^d;\mathbb R^d)+L^1(\mathbb T^d;\mathbb R^d)}?
```

Here $`\mathbb T^d=\mathbb R^d/\mathbb Z^d`$ has unit volume, $`\|u\|_{H^s}^2=\sum_{k\in\mathbb Z^d}(1+4\pi^2|k|^2)^s|\widehat u(k)|^2`$, $`W^{1,1}`$ has its usual norm, and $`\|u\|_{X+Y}=\inf_{u=a+b}(\|a\|_X+\|b\|_Y)`$. The vector-valued norms use Euclidean length and the sum of component Fourier energies.

## Application

The estimate would recover a potential from a gradient containing both rough integrable and fractional-Sobolev components. It is tied to phase lifting in circle-valued fields and to critical elliptic estimates used in superconductivity models.

## References

1. J. Bourgain and H. Brezis, [On the equation div Y = f and application to control of phases](https://sites.math.rutgers.edu/~brezis/PUBlications/171-J.pdf), *Journal of the American Mathematical Society* **16** (2003), 393–426, equation (1.16), p. 397.
2. H. Brezis, [Some of my favorite open problems](https://doi.org/10.4171/RLM/1008), *Rendiconti Lincei — Matematica e Applicazioni* **34** (2023), §7, Open Problem 7.1; [author PDF](https://sites.math.rutgers.edu/~brezis/PUBlications/234.pdf).

## Status review

**Resolution reviewed 2026-10-13:** [Kaiwen Jin's manuscript](../research/solutions/451-mixed-sobolev-counterexample/paper/main.pdf) establishes the full original target. Explicit real smooth mean-zero two-dimensional counterexample sequence for the exact mixed sum-norm estimate.

**Independent review:** the [complete per-problem audit](../research/solution_reviews/2026-10-13-yui-prs/451-review.md) reconstructs the argument, compares its hypotheses and quantifiers with the original statement, and checks the cited sources and accompanying materials. The review was carried out by independent Codex AI agents during maintainer processing; it does not assert human peer review or Lean verification.

The reviewed submission is [PR #69](https://github.com/MColbrook/AIM/pull/69) at `c27cd2a4b9a1f4a11d0f4cda8b33b233695260da`. The original problem statement at `c9929805cece044705abaaebe1cebddac1ba11a6` was compared with its unchanged current form. The proof and documented independent audit meet the repository's **Solved** criterion; the original problem page and ID are retained.
