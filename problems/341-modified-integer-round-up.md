# 341. The modified integer round-up conjecture for cutting stock

**Area:** Stochastic dynamics, reaction networks and applied optimization

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Fix a positive integer stock length $`W`$ and $`n\geq1`$ item types. Type $`i`$ has integer length $`1\leq\ell_i\leq W`$ and positive integer demand $`b_i`$. A cutting pattern is a vector in

```math
\mathcal P=\left\{a\in\mathbb Z_{\geq0}^{n}:
\sum_{i=1}^{n}\ell_i a_i\leq W\right\}.
```

Use every capacity-feasible pattern: there is no additional restriction $`a_i\leq b_i`$. Thus the relaxation below includes patterns containing more copies of an item than its demand, sometimes called *nonproper patterns*.

Let the minimum number of stock pieces needed to meet all demands be

```math
\begin{aligned}
z_{\mathrm{IP}}=\min\quad&\sum_{a\in\mathcal P}x_a\\
\text{subject to}\quad&\sum_{a\in\mathcal P}a_i x_a\geq b_i
\quad(1\leq i\leq n),\\
&x_a\in\mathbb Z_{\geq0}\quad(a\in\mathcal P).
\end{aligned}
```

Define $`z_{\mathrm{LP}}`$ by replacing the integer constraint with $`x\in\mathbb R_{\geq0}^{\mathcal P}`$. Each use of a pattern counts as one stock piece, including repeated uses.

Does every such instance satisfy

```math
z_{\mathrm{IP}}\leq\left\lceil z_{\mathrm{LP}}\right\rceil+1?
```

This is the modified integer round-up property (MIRUP) conjectured by Scheithauer and Terno. The ceiling is the least integer no smaller than its argument. The question requires the same additive one for arbitrary item types, lengths, capacity and demands. It compares the two optima and does not prescribe the time needed to find a packing.

## Application

Cutting stock models production from standard rolls or bars, including paper and metal cutting. Fractional pattern optimization supplies lower bounds used to assess production plans. MIRUP would place the true stock requirement within one piece of that rounded lower bound, uniformly over the order sizes. A counterexample would expose a larger systematic gap in this planning estimate. The statement concerns the classical one-dimensional model with one stock length and the stock-count objective; setup costs and machine-specific cutting restrictions require different models.

## References

1. Guntram Scheithauer and Johannes Terno, *The modified integer round-up property of the one-dimensional cutting stock problem*, European Journal of Operational Research 84(3) (1995), 562–571. [DOI](https://doi.org/10.1016/0377-2217%2895%2900022-I). Original attribution; publisher abstract checked. The full formulation here is also given in reference 2.
2. Renan Fernando Franco da Silva, Vinícius Loti de Lima, Rafael C. S. Schouery, Jean-François Côté and Manuel Iori, *Polynomial and Pseudopolynomial Algorithms for Two Classes of Bin Packing Instances*, [arXiv:2604.05152v2](https://arxiv.org/html/2604.05152v2), June 4, 2026, preprint. §1; §2, equations (1)–(3) and Property 2; §§3–5 and §7. Explicit integer-input model, nonproper-pattern convention and current conjecture statement.
3. Rebecca Hoberg and Thomas Rothvoss, *A Logarithmic Additive Integrality Gap for Bin Packing*, SODA 2017, 2616–2625. [DOI](https://doi.org/10.1137/1.9781611974782.172); [arXiv:1503.08796v1](https://arxiv.org/pdf/1503.08796), March 30, 2015. The accessed preprint's §1, equation (1), and §1.1, Theorem 2, pp. 1–3, give the pattern relaxation, conjecture and logarithmic additive bound.
4. Friedrich Eisenbrand, Dömötör Pálvölgyi and Thomas Rothvoß, *Bin Packing via Discrepancy of Permutations*, [arXiv:1007.2170v2](https://arxiv.org/pdf/1007.2170), February 2, 2012, journal-version manuscript. §6, Definition 1 and Theorems 11–12, pp. 12–16. Lower bounds for a specified class of rounding procedures.
5. Constantine Goulimis, *Counterexamples in the CSP*, [arXiv:2004.01937v3](https://arxiv.org/pdf/2004.01937), July 7, 2020, preprint; PDF title *Counterexamples in the Cutting Stock Problem*. §1; §2, p. 2; §5.1, pp. 6–7. Distinguishes integer rounding, modified integer rounding and a different conjecture about the number of distinct patterns.
6. John Martinovic, *A note on the integrality gap of cutting and skiving stock instances*, 4OR 20 (2022), 85–104, published online December 23, 2020. [Published article](https://link.springer.com/article/10.1007/s10288-020-00469-4), §2, Definition 3, and §4, Theorem 4. An improved bound under divisibility assumptions.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026.pdf), result family 118 (2026). Statement locator: `Theorem thm:unbounded-gap; Definition def:configuration-lp`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete counterexample to the original target.

**Statement comparison:** The source explicitly uses unrestricted numerical-size type patterns, whose multiplicities are limited by capacity rather than input demand; this is the exact nonproper-pattern LP in AIM. Set c=1: LP=B integer and OPT>B+1 refutes MIRUP without a ceiling ambiguity. Convert rational sizes to integer item lengths using a common denominator W; positive integer type demands are multiplicities. Removing excess items identifies integer covering optimum with packing optimum. This is an unconditional structural counterexample, independent of NP!=P.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-341) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/118.md). Actual main_results proves unbounded gaps with both typeLP and individualLP equal integer B. The relevant typeLP preserves unrestricted patterns. Integer-length scaling is a mathematical adapter. No local replay/axiom log. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/341-modified-integer-round-up.md).
