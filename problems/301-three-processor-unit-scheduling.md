# 301. Exact complexity of unit-job precedence scheduling on three processors

**Area:** Scheduling and operations research

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`G=(J,E)`$ be a directed acyclic graph with $`n`$ vertices, one for each job, and let $`T`$ be a nonnegative integer supplied in binary. Every job takes exactly one unit of time on any of three identical processors. A job must finish before any of its successors begins. Jobs cannot be interrupted; each processor runs at most one job at a time; all jobs are available at time zero subject to the precedence constraints.

Decide whether there is a schedule that completes all jobs by time $`T`$. Equivalently, does there exist a map $`s:J\to\{0,\ldots,T-1\}`$ such that

```math
s(v)\ge s(u)+1\quad((u,v)\in E),\qquad
|\{j\in J:s(j)=t\}|\le3\quad(0\le t<T)?
```

Determine the computational complexity of this decision problem, conventionally written $`P3\mid\mathrm{prec},p_j=1\mid C_{\max}`$. In particular, is it solvable by a deterministic algorithm polynomial in the input length, or can NP-completeness be established under polynomial-time many-one reductions? No dichotomy between these outcomes is assumed. The number of processors is fixed at three, while the job graph and deadline are unrestricted input. The goal is exact feasibility, not an approximation to the minimum completion time.

## Application

Precedence edges represent dependencies between computational tasks or project activities. Fixing three identical processors removes machine heterogeneity and numerical processing-time encoding, isolating the algorithmic difficulty created by dependencies and limited parallelism. Resolving exact tractability would clarify when an optimal schedule can be computed efficiently for this basic resource-allocation model.

## References

1. Jesper Nederlof, Céline M. F. Swennenhuis and Karol Węgrzycki, *A Subexponential Time Algorithm for Makespan Scheduling of Unit Jobs with Precedence Constraints*, SODA 2025, 535–552. [Published paper](https://research-portal.uu.nl/ws/portalfiles/portal/254249631/1.9781611978322.16.pdf), §1 Open Question 1 and Theorem 1.1; §9 Theorem 9.1.
2. Syamantak Das and Andreas Wiese, *A Simpler QPTAS for Scheduling Jobs with Precedence Constraints*, ESA 2022, 40:1–40:11. [Published paper](https://doi.org/10.4230/LIPIcs.ESA.2022.40), §1. The arXiv upload appeared in 2025.
3. Christina Büsing, Maurice Draeger and Corinna Mathwieser, *Parameterized Complexity of Scheduling Unit-Time Jobs with Generalized Precedence Constraints*, IPEC 2025, 7:1–7:16. [Published paper](https://doi.org/10.4230/LIPIcs.IPEC.2025.7), §5 and Theorem 13.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/paper.pdf), result family 124 (2026). Statement locator: `Theorem thm:main; deterministic multitape time O((L+2)^150020)`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** Arbitrary explicitly listed DAG, nonpreemptive unit-length jobs and exactly three identical machines agree. Its slot values 1..T equal AIM start times plus one. The theorem treats n>=1 and 1<=T<=n: AIM extra cases are immediate in polynomial time (n=0 feasible, T=0 with n>0 infeasible, T>=n feasible by topological sequential schedule). Thus binary arbitrary deadline and empty input add no unresolved case.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-301) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/124.md). Actual main_theorem proves one finite machine and binary-input polynomial bound for nonempty n and normalized deadlines; the trivial edge-case adapter is not a separately replayed AIM theorem. No local verification record. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/301-three-processor-unit-scheduling.md).
