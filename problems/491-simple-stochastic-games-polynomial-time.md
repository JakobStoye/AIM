# 491. Polynomial-time solution of simple stochastic games

**Area:** Stochastic control, formal verification and algorithmic game theory

**Status:** 🟡 PARTIAL

**Last checked:** 2026-10-13

## Problem statement

Consider a finite directed simple graph $`G=(V,E)`$ with a partition

```math
V=V_{\max}\sqcup V_{\min}\sqcup V_{\mathrm{rand}}\sqcup\{0,1\}.
```

The vertices $`0`$ and $`1`$ are sinks. Every other vertex has exactly two outgoing edges, and every vertex has a directed path to at least one sink. A nonsink vertex $`o`$ is the starting state.

A token moves along the edges. At a vertex in $`V_{\max}`$, player Max chooses its next edge; at a vertex in $`V_{\min}`$, player Min chooses. At a vertex in $`V_{\mathrm{rand}}`$, an independent fair coin selects one of the two outgoing edges. The players observe the current state and the preceding play. Max receives payoff one if the token eventually reaches sink $`1`$, and zero otherwise, including when play continues forever.

A pure positional strategy selects one outgoing edge at every vertex controlled by that player. For strategies $`\sigma`$ of Max and $`\tau`$ of Min, let $`\mathbb P_o^{\sigma,\tau}`$ denote the law of the resulting Markov chain, with the sinks treated as absorbing. Define

```math
v(o)=\max_\sigma\min_\tau
\mathbb P_o^{\sigma,\tau}
\bigl(\text{the token eventually reaches }1\bigr).
```

Optimal pure positional strategies exist, so allowing strategies with memory or randomized choices does not change this value.

**Does a deterministic polynomial-time algorithm decide whether $`v(o)>1/2`$ for every such game?** More precisely, if $`L`$ is the bit length of the explicit adjacency-list encoding, vertex types and starting state, seek one algorithm and constants $`C,c>0`$, independent of the input, which always return the correct answer within $`C(L+1)^c`$ steps.

The equality case $`v(o)=1/2`$ requires a negative answer. All three vertex counts can grow. The graph-path assumption does not guarantee eventual absorption under every pair of strategies; no such stopping promise is imposed. This is the binary reachability decision formulation in [1, §2.2], counted as one problem.

## Application

The graph can represent a finite system with controlled decisions, adversarial environmental choices and random transitions. Its value measures the best guaranteed probability of reaching a specified goal despite the adversary. Computing this threshold is a basic capability in probabilistic verification and controller synthesis [2, 6]. A polynomial algorithm would give a worst-case efficiency guarantee for explicitly represented models; the number of states needed to encode a physical system could still be large.

## References

1. Bernd Gärtner, Sebastian Haslebacher and Hung P. Hoang, *Sinks and Ladders: ARRIVAL and SSG with Two Vertices per Level*, FUN 2026, LIPIcs 366, 19:1–19:16, published May 15, 2026. [Publisher record](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FUN.2026.19); [full text](https://drops.dagstuhl.de/storage/00lipics/lipics-vol366-fun2026/html/LIPIcs.FUN.2026.19/LIPIcs.FUN.2026.19.html). Introduction, §§2–2.2 and Theorem 2.
2. Hugo Gimbert and Florian Horn, *Solving Simple Stochastic Games with Few Random Vertices*, Logical Methods in Computer Science 5(2:9) (2009), 1–17. [Published PDF](https://lmcs.episciences.org/1119/pdf). §§1.1–1.3, Theorem 1.1, Theorem 3.4 and conclusion.
3. Xi Chen, Yuhao Li and Mihalis Yannakakis, *The Mystery Deepens: On the Query Complexity of Tarski Fixed Points*, [arXiv:2604.00268v1](https://arxiv.org/html/2604.00268v1), March 31, 2026; preprint. §1, Theorems 1–2 and Corollary 1.
4. Andrei Feodorov and Sebastian Haslebacher, *Faster Approximate Fixed Points of $`\ell_\infty`$-Contractions*, [arXiv:2604.01006v1](https://arxiv.org/html/2604.01006v1), April 1, 2026; preprint. Theorems 1.1–1.2 and §1, “Implications for Condon’s and Shapley’s Stochastic Games.”
5. Manuel Bodirsky, Georg Loho and Mateusz Skomra, *Reducing Stochastic Games to Semidefinite Program Feasibility*, [arXiv:2411.09646v2](https://arxiv.org/html/2411.09646v2), December 2, 2025; expanded preprint. §§1–2.2, Definition 1, Corollary 11 and Theorem 12. The ICALP 2025 conference version has the title *Reducing Stochastic Games to Semidefinite Programming*, LIPIcs 334, 145:1–145:15.
6. Edon Kelmendi, Julia Krämer, Jan Křetínský and Maximilian Weininger, *Value Iteration for Simple Stochastic Games: Stopping Criterion and Learning Algorithm*, CAV 2018, 623–642; [accessible author version, arXiv:1804.04901v1](https://arxiv.org/html/1804.04901v1), April 13, 2018. §§1–2, Algorithm 1 and §4.3, Theorem 4.2.
7. Lei Huang and Toniann Pitassi, *Automatizability and Simple Stochastic Games*, ICALP 2011, Part I, LNCS 6755, 605–617; [author PDF](https://www.cs.utoronto.ca/~toni/Papers/automatizability.pdf). §§1–2 and §3, Theorem 5 and Corollary 1.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Turn-Based-Stochastic-Mean-Payoff-Games-in-Deterministic-Quasipolynomial-Time-October-5-2026/stochastic-mean-payoff-games.pdf), result family 104 (2026). Statement locator: `Theorem thm:main and explicit simple-stochastic-game reduction in section 1`.

## Status review

**Known cases:** A deterministic quasipolynomial-time algorithm decides the reachability threshold, including the strict comparison requested here after the rational-value gap reduction described in the review. Polynomial algorithms were already known when the number of random vertices is fixed and for the stopping ladder class; see references 1–2.

**Remaining target:** Obtain a fixed polynomial-time algorithm for all encoded inputs. Quasipolynomial running time does not meet that requirement.

**Statement comparison:** The deterministic algorithm has bit time 2^O((log(L+2))^2), which is quasipolynomial, not a fixed polynomial. The source explicitly reduces reachability >=1/2 to nonnegative expectation-of-liminf mean payoff with absorbing rewards +/-1, including nonabsorbing plays. AIM strict >1/2 is also obtainable: pure positional SSG values are rational with denominator at most 3^n by integer linear systems and Hadamard; positive 2v-1 is >=3^-n. Multiply all +/-1 rewards by 2*3^n and subtract 1 from every edge, so nonnegative mean payoff holds iff v>1/2. This has polynomial encoding length and preserves the quasipolynomial bound.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-491) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/104.md). Docs104 formalize only randomized ordinary mean-payoff and a finite Truffet counterexample. They do not declare a formalization of this deterministic stochastic algorithm or AIM491. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/491-simple-stochastic-games-polynomial-time.md).
