# 321. Polynomial sample complexity for deletion-trace reconstruction

**Area:** Statistical inference and molecular data retrieval

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Fix a known deletion probability $`q\in(0,1)`$. An unknown string $`x=(x_1,\ldots,x_n)\in\{0,1\}^n`$ has known length $`n`$. A trace of $`x`$ is formed by deleting each bit independently with probability $`q`$ and concatenating the retained bits in their original order. The deleted positions are not reported. Let $`\mathcal T_n=\bigcup_{j=0}^n\{0,1\}^j`$, including the empty string, and denote the trace distribution by $`D_q(x)`$.

**For every fixed $`q\in(0,1)`$, do there exist finite constants $`C_q,k_q>0`$ such that, for every $`n\ge2`$, some decoder $`A_{n,q}`$ using $`m\le\lceil C_qn^{k_q}\rceil`$ independent traces satisfies**

```math
\inf_{x\in\{0,1\}^n}
\Pr\!\left[A_{n,q}(Y_1,\ldots,Y_m)=x\right]\ge\frac23,
\qquad Y_1,\ldots,Y_m\ \overset{\mathrm{iid}}{\sim}\ D_q(x)?
```

Here the decoder maps $`\mathcal T_n^m`$ to $`\{0,1\}^n`$, may use its own randomness, and must be the same decoder for every unknown string of length $`n`$. The probability includes that randomness and all deletions. There is no restriction on computation time. The constants may depend on $`q`$, which is fixed independently of $`n`$; a uniform polynomial as $`q`$ tends to one is not requested.

The target is exact recovery for every possible string. There is no random-source, sparsity, long-run, codebook or known-nearby-reference assumption. Replacing $`2/3`$ by any other fixed success probability strictly between $`1/2`$ and $`1`$ changes the sample requirement by at most a constant repetition factor. This is one problem family across fixed deletion probabilities.

## Application

Repeated molecular reads can lose symbols without identifying their original positions, making alignment part of the inference problem. The deletion model isolates how many independent observations are needed to recover a stored sequence despite that loss of synchronization. A polynomial bound would give a worst-case sample guarantee without designing the source string to be easy to reconstruct. This is a foundational question for DNA data retrieval: practical reads use a larger alphabet and also have substitutions and insertions, while a complete storage pipeline must cluster reads and decode error-correcting codes. A sample bound alone supplies neither a fast decoder nor a guarantee for all those additional effects.

## References

1. Anders Aamand, Allen Liu and Shyam Narayanan, *Near-Optimal Trace Reconstruction for Mildly Separated Strings*, ICALP 2025, LIPIcs 334, 3:1–3:20, [published paper](https://doi.org/10.4230/LIPIcs.ICALP.2025.3), abstract and §1, especially Theorem 1. Explicitly poses polynomial-trace sufficiency for unrestricted strings.
2. Jin Sima and Jehoshua Bruck, *Trace Reconstruction with Bounded Edit Distance*, [arXiv:2102.05372v2](https://arxiv.org/pdf/2102.05372v2), April 14, 2021. Preprint; §I, Theorem 1 and §V independently state the general gap while solving the bounded-reference case.
3. Arnav Burudgunte, Paul Valiant and Hongao Wang, *Quasipolynomial Trace Reconstruction*, [arXiv:2607.04073v1](https://arxiv.org/html/2607.04073v1), submitted July 5, 2026. Preprint; §2 Definitions 1–2, §8.2 Theorem 43 and §1's running-time discussion.
4. Zachary Chase, *New lower bounds for trace reconstruction*, Annales de l'Institut Henri Poincaré, Probabilités et Statistiques 57(2) (2021), 627–643, [DOI](https://doi.org/10.1214/20-AIHP1089); [author preprint](https://arxiv.org/pdf/1905.03031v2), July 23, 2020, §1 Theorem 1 and §2.
5. Vinnu Bhardwaj, Pavel A. Pevzner, Cyrus Rashtchian and Yana Safonova, *Trace Reconstruction Problems in Computational Biology*, [arXiv:2010.06083v1](https://arxiv.org/pdf/2010.06083v1), October 12, 2020, accepted author manuscript; §§I.B, IV and V. Defines worst-case sample complexity and explains the molecular-storage connection and modeling limits.
6. Xi Chen, Anindya De, Chin Ho Lee, Rocco A. Servedio and Sandip Sinha, *Polynomial-time trace reconstruction in the smoothed complexity model*, [arXiv:2008.12386v1](https://arxiv.org/pdf/2008.12386v1), August 27, 2020, author manuscript; §1.2 Theorem 1. The source string is randomly perturbed before traces are generated.
7. Xi Chen, Anindya De, Chin Ho Lee and Rocco A. Servedio, *Trace Reconstruction from Local Statistical Queries*, APPROX/RANDOM 2024, LIPIcs 317, 52:1–52:24, [published paper](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2024.52), §2.1 and §3 Theorem 6. Its lower bound restricts access to local statistical queries.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/paper.pdf), result family 122 (2026). Statement locator: `Theorem thm:main and thm:tv`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete counterexample to the original target.

**Statement comparison:** Definitions match known length n, fixed known deletion probability q in (0,1), independent complete deletion traces (including length), randomized decoder common to all binary strings, unrestricted computation and exact recovery. Set success s=2/3. For each fixed q, n^(c*log(q^3*log n)) eventually exceeds Cq*n^kq for every constants Cq,kq. Hence the requested polynomial-sample assertion is false at every fixed channel.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-321) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/122.md). Actual superpolynomial_sample_complexity and quantitative_sample_lower_bound agree with the unrestricted complete-trace target; inspected estimator definitions include decoder randomization. No successful local replay/axiom log. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/321-polynomial-trace-reconstruction.md).
