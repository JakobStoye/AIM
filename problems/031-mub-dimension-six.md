# 031. The maximum number of mutually unbiased bases in dimension six

**Area:** Quantum information and matrix design

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Determine $`M(6)`$, the largest integer $`r`$ for which there exist orthonormal bases $`B_a=\{u_{a1},\ldots,u_{a6}\}`$ of $`\mathbb C^6`$, $`1\le a\le r`$, with

```math
|\langle u_{ai},u_{bj}\rangle|^2=\frac16\quad(a\ne b,\ 1\le i,j\le6).
```

In particular, decide whether four such bases exist. The known general bounds are $`3\le M(6)\le7`$; constructions in prime-power dimensions do not settle dimension six.

## Application

Mutually unbiased measurements distribute information evenly between incompatible observables. They are used in quantum tomography, uncertainty relations and communication protocols.

## References

1. P. Horodecki, Ł. Rudnicki and K. Życzkowski, [Five open problems in quantum information](https://arxiv.org/abs/2002.03233), 2020; published in PRX Quantum 3 (2022), 010101. MUB problem.
2. M. Cárdenes Wuttig and J. Tindall, [A Complete Classification of Complex Hadamard Matrices of Order Six](https://arxiv.org/abs/2608.18053), 2026, v2. Recent classification relevant to, but distinct from, simultaneous MUB construction.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026/The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026.pdf), result family 266 (2026). Statement locator: `build/sections/introduction.tex, thm:main; manuscript Section 7 and Appendix A; build/sections/execution.tex, execute:finite-theorem and execute:observed`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** The stated computer-assisted theorem excludes four arbitrary complex orthonormal bases in C6, without restricting the second Hadamard matrix to a known family, and concludes N(6)=3. It depends on the published binary64 arithmetic/compiler and complete-execution certificate conditions; no execution was reproduced by this agent. Section 7 reports a completed 4 October 2026 run with all 100 invocations accounted and no final unresolved records. Its native source/archive paths are named but those verification directories are absent from the pinned public preprints tree; the run was not independently reproduced.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-031) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/266.md). docs/266 only proves at most five bases and supporting Fourier cancellation. It does not prove N(6)=3 or exclude four. No AIM Lean-verified status is asserted.

**Evidence limitation:** Published observed-execution report checked. Referenced native code and computation archive not present under this folder in the pinned public tree; no independent run or compiler-semantics audit.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/031-mub-dimension-six.md).
