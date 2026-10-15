# 627. Smallest orders for periodic multidimensional Costas arrays

**Area:** Combinatorial signal design

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Write $`[a]=\{1,\ldots,a\}`$. Let $`m\ge2`$, $`1\le m-k\le k`$, and let $`n_1,\ldots,n_m\ge2`$ be integers satisfying

```math
n=\prod_{i=1}^{k}n_i=\prod_{i=k+1}^{m}n_i.
```

For a bijection

```math
\varphi:\prod_{i=1}^{k}[n_i]\longrightarrow\prod_{i=k+1}^{m}[n_i],
```

let $`S=\{(x,\varphi(x))\}`$ be its graph and extend it periodically to

```math
\widetilde S=S+(n_1\mathbb Z\times\cdots\times n_m\mathbb Z).
```

Assume that, for every $`t\in\mathbb Z^m`$, all nonzero ordered difference vectors between points of

```math
\widetilde S\cap\left(t+\prod_{i=1}^{m}[n_i]\right)
```

are distinct. Must $`n=2^k`$, equivalently $`n_1=\cdots=n_k=2`$?

This is the periodic multidimensional Costas-array conjecture of Rubio and Torres. The differences in each window are ordinary integer vectors; they are not reduced modulo the side lengths.

## Application

Distinct displacement vectors limit ambiguity in multidimensional correlation patterns used in radar, optical communication and digital holography. The conjecture would restrict which array shapes can retain this property under every shift of a periodically repeated pattern.

## References

1. I. Rubio and J. Torres, [Multidimensional Costas Arrays and Their Periodicity](https://arxiv.org/abs/2208.02378), *IEEE Transactions on Information Theory* **69**(8) (2023), 5032–5040, [DOI](https://doi.org/10.1109/TIT.2023.3264951), Sections 3–4, Definitions 2–4 and Conjecture 1.
2. I. Rubio and J. Torres, [Circular Costas maps: a multidimensional analog of circular Costas sequences](https://arxiv.org/abs/2210.16661), *Cryptography and Communications* **15** (2023), 941–958. The circular-map results concern a different injection-based definition.

## Status review

Reviewed 15 October 2026 against the original target in [PR #124](https://github.com/MColbrook/AIM/pull/124). A six-point periodic four-dimensional Costas array disproves the universal order restriction.

[Proof or source](../research/solutions/627-periodic-costas/paper/main.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/627-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** A six-point periodic four-dimensional Costas array disproves the universal order restriction.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Known cases:** The assertion holds in dimensions two and three. Odd orders cannot satisfy the periodic condition in any dimension. The source also supplies nonexistence criteria for additional even-order shapes and examples of periodic arrays of size $`2\times2\times4`$.

**Remaining target:** Prove the assertion for arbitrary dimensions at least four, or give a periodic array exceeding the proposed minimum order.

Current exact-title, author and conjecture searches found no matching general proof or announcement. The solved circular-array conjectures and a 2026 conference talk about nonsurjective periodic injections do not cover this bijective setting. Public GitHub, Zenodo and Palomar checks are recorded, including noisy results and search limits; no recent comprehensive status survey was located.
