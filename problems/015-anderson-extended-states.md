# 015. Extended states in the three-dimensional Anderson model

**Area:** Disordered quantum transport

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

On $`\ell^2(\mathbb Z^3)`$ define

```math
(H_\eta\psi)(n)=\sum_{|m-n|_1=1}\psi(m)+\eta V_n\psi(n),
```

where $`(V_n)`$ are independent uniform random variables on $`[-1,1]`$ and $`\eta>0`$. Prove or disprove that there exist $`\eta_0>0`$ and a nonempty open interval $`I\subset(-6,6)`$ such that, for every $`0<\eta<\eta_0`$, almost surely the restriction of $`H_\eta`$ to its spectral subspace for $`I`$ is purely absolutely continuous and $`I\subset\sigma(H_\eta)`$.

## Application

The assertion gives a rigorous conducting spectral phase for a standard model of an electron moving through a weakly disordered three-dimensional solid.

## References

1. B. Simon, [Schrödinger operators in the twenty-first century](https://web.ma.utexas.edu/mp_arc-bin/mpa?yn=00-78), in Mathematical Physics 2000 (2000), pp. 283–288, Problem 1.
2. F. Hernández, [Lecture notes on Quantum Diffusion and Random Matrix Theory](https://arxiv.org/abs/2511.04380), preprint (2025), §1.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/paper.pdf), result family 261 (2026). Statement locator: `build/01-introduction.tex, thm:main and eq:energy-windows`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** For d=3 the theorem gives a fixed I=(-6+e2/2,-6+e2) inside (-6,6), a positive disorder threshold, I contained in spectrum and pure absolute continuity almost surely for each fixed coupling. A stated parity unitary flips the hopping sign to the target convention.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-015) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/261.md). docs/261 only proves the planar spectral set; it covers neither the 3D absolute-continuity target nor planar pure-point type. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/015-anderson-extended-states.md).
