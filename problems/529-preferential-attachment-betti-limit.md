# 529. Limiting Betti-number distributions in preferential-attachment networks

**Area:** Applied topology and random networks

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Fix integers $`q\ge2`$, $`m\ge2q`$ and a real $`\delta>-m`$ such that

```math
x=\frac{m+\delta}{2m+\delta}<\frac1{2q}.
```

Start with two vertices joined by $`m`$ parallel edges. At each time $`t\ge3`$, add vertex $`t`$ and $`m`$ edges, sequentially. Given the graph after the first $`a-1`$ new edges, choose the old endpoint $`v<t`$ of edge $`a`$ with probability

```math
\frac{d_{t,a-1}(v)+\delta}{2m(t-2)+(a-1)+(t-1)\delta},\qquad 1\le a\le m,
```

where $`d_{t,a-1}(v)`$ is its current degree, counting multiplicity. There are no self-loops. Let $`X_T`$ be the clique complex of the underlying simple graph at time $`T`$, and set $`\beta_q(T)=\dim_{\mathbb Q}H_q(X_T;\mathbb Q)`$.

Does

```math
\frac{\beta_q(T)}{\mathbb E\beta_q(T)}\ \xrightarrow[T\to\infty]{\mathrm d}\ W_{q,m,\delta}
```

hold for a nondegenerate random variable? Determine the limiting law, or disprove this assertion. In particular, establish or refute the proposed power-law tail and, where it holds, determine its exponent. One precise tail formulation to test is regular variation:

```math
\lim_{z\to\infty}\frac{\Pr(W_{q,m,\delta}>uz)}{\Pr(W_{q,m,\delta}>z)}=u^{-\alpha(q,m,\delta)},\qquad u>0,
```

for some positive $`\alpha(q,m,\delta)`$.

This formulates the distributional question in [1] within the strict polynomial-growth regime. The expectation is over graph generation, rather than an empirical average across simulated networks. Regular variation is a precise version of the paper's numerical power-law suggestion, not an already established property.

## Application

Limit distributions would calibrate the variability of higher-order connectivity statistics in growing networks with hubs. They would support uncertainty assessments when observed topological features are compared with a preferential-attachment null model.

## References

1. C. Siu, [The Topological Behavior of Preferential Attachment Graphs](https://doi.org/10.1137/24M1693179), SIAM Journal on Applied Algebra and Geometry **9**(2), 432–455 (2025). [Author preprint, arXiv:2406.17619v2](https://arxiv.org/abs/2406.17619v2), §1.2, Definitions 3.1/3.3, Theorem 4.1, §§9–10.
2. C. Siu, G. Samorodnitsky, C. L. Yu and R. He, [The asymptotics of the expected Betti numbers of preferential attachment clique complexes](https://doi.org/10.1017/apr.2024.66), Advances in Applied Probability **57**(3), 940–968 (2025).

## Status review

Reviewed 15 October 2026 against the original target in [PR #100](https://github.com/MColbrook/AIM/pull/100). The normalized high-dimensional Betti numbers converge to an explicitly described nondegenerate law with all positive moments, excluding the proposed power-law tail.

[Proof or source](../research/solutions/529-preferential-attachment-betti-limit/paper/main.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/529-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** For the precise sequential affine preferential-attachment model, every q>=2 and m>=2q with x<1/(2q) has the stated full-sequence distributional limit; its normalized random variable is positive, nondegenerate and has every positive moment.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

The expectation has order $`T^{1-2qx}`$ in this regime [2]. Theorem 4.1 of [1] bounds the random Betti number between $`T^{1-2qx}/\omega(T)`$ and $`\omega(T)T^{1-2qx}`$ with probability tending to one, for every $`\omega(T)\to\infty`$. These order estimates do not identify a distributional limit. The simulated tail exponents in [1] are evidence, not proofs.

Checks on 24 September 2026 found no matching solution or announcement in the primary literature, indexed arXiv/Zenodo/GitHub searches, the author's publication page, or the official Palomar search API. Limit theorems for spatial age-dependent connection models concern a different graph law.
