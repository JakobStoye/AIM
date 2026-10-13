# 346. The near-linear bound for planar halving lines

**Area:** Computational geometry and parametric selection

**Status:** 🟡 PARTIAL

**Last checked:** 2026-10-13

## Problem statement

Let $`n\ge2`$ be even, and let $`P\subset\mathbb R^2`$ consist of $`n`$ distinct points, with no three collinear. A *halving line* is a line through two points of $`P`$ that leaves exactly $`(n-2)/2`$ of the remaining points in each of its two open half-planes. Count each such line once, and write $`h(P)`$ for their number. Define

```math
h(n)=\max_{\substack{P\subset\mathbb R^2,\ |P|=n\\P\text{ has no three collinear points}}}h(P).
```

Is it true that for every $`\varepsilon>0`$ there is a constant $`C_\varepsilon>0`$, independent of $`n`$ and $`P`$, such that

```math
h(n)\le C_\varepsilon n^{1+\varepsilon}
\qquad\text{for every even }n\ge2?
```

This is the near-linear halving-line conjecture of Erdős, Lovász, Simmons and Straus. The original statement uses $`e_m=h(2m)`$ and little-$`o`$ for every positive exponent increment; that formulation is equivalent to the uniform bound above. The point sets are arbitrary apart from general position. This is one planar counting problem, also expressible using halving edges or middle-level crossings in arrangements of straight lines.

## Application

Consider retaining the cheapest half of $`n`$ options whose costs are affine functions of one real parameter. For distinct slopes and no triple intersection, membership changes when two costs cross at the middle of the ordering. Under point-line duality, these events correspond to halving lines of the coefficient points. Thus the conjecture bounds how many changes a complete representation of these optimal choices must record. This is a foundational question about the size of the output in geometric selection and parametric optimization; its assertion does not itself supply an enumeration algorithm. Nivasch's dual formulation and Dey's arrangement analysis make this connection precise.

## References

1. P. Erdős, L. Lovász, A. Simmons and E. G. Straus, *Dissection Graphs of Planar Point Sets*, in *A Survey of Combinatorial Theory* (1973), pp. 139–149, [original paper](https://www.renyi.hu/~p_erdos/1973-07.pdf). Definition 4.4 and Conjecture 5.2, especially the latter's precise subpower assertion.
2. Edgardo Roldán-Pensado and Pablo Soberón, *A survey of mass partitions*, [arXiv:2010.00478v3](https://arxiv.org/html/2010.00478v3), preprint revised December 2, 2020, §5.1, Conjecture 5.1.1. Independent explicit formulation.
3. Gabriel Nivasch, *An Improved, Simple Construction of Many Halving Edges*, Contemporary Mathematics 453 (2008), pp. 299–305, [author manuscript](https://drive.google.com/uc?export=download&id=1HpaNqAkazvSNFwGFteDIK92C7EY6Lbl8). §1, manuscript pp. 1–3, equation (1.2), conjecture paragraph and dual setting.
4. Tamal K. Dey, *Improved Bounds for Planar k-Sets and Related Problems*, Discrete & Computational Geometry 19 (1998), pp. 373–382, [published paper](https://courses.cs.duke.edu/cps234/fall08/handouts/dey.pdf). Theorem 3.3 and §§4–4.1 distinguish line levels from general parametric matroid optimization.
5. Estrella Alonso, Mariló López and Javier Rodrigo, *An Improvement of the Upper Bound for the Number of Halving Lines of Planar Sets*, Symmetry 16 (2024), 936, [university copy](https://oa.upm.es/89576/1/10302927.pdf), DOI 10.3390/sym16070936. §2 and §3, Proposition 3 and Remark 1.
6. Javier Rodrigo, Mariló López, Danilo Magistrali and Estrella Alonso, *An Improvement of the Lower Bound on the Maximum Number of Halving Lines for Sets in the Plane with an Odd Number of Points*, Axioms 14 (2025), 62, [publisher PDF](https://mdpi-res.com/d_attachment/axioms/axioms-14-00062/article_deploy/axioms-14-00062-v2.pdf), DOI 10.3390/axioms14010062. §§2–4, Propositions 1–7.
7. Elizaveta Streltsova and Uli Wagner, *Levels in Arrangements: Linear Relations, the g-Matrix, and Applications to Crossing Numbers*, SoCG 2025, article 75, [proceedings paper](https://drops.dagstuhl.de/storage/00lipics/lipics-vol332-socg2025/LIPIcs.SoCG.2025.75/LIPIcs.SoCG.2025.75.pdf). §§1.1–1.2, Theorem 6 and Remark 7.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-power-saving-for-planar-halving-lines-September-25-2026/main.pdf), result family 183 (2026). Statement locator: `Theorem 1.1, PDF page 2; Power-saving halving theorem label thm:halving-power, introduction.tex lines9-16.`.

## Status review

**Known cases:** The manuscript improves the upper exponent for planar halving lines from $`4/3`$ to $`4/3-\varepsilon_0`$ for one absolute $`\varepsilon_0>0`$.

**Remaining target:** Reach an upper bound of order $`n^{1+\eta}`$ for every $`\eta>0`$, or disprove that near-linear target.

**Statement comparison:** The halving-power theorem counts exactly unordered pairs determining balanced straight lines of arbitrary even planar n-point sets with no three collinear. It gives an absolute fixed positive saving epsilon from4/3 for all sufficiently large even n; enlarging C covers finite smaller n. It neither supplies exponents1+eta for every eta>0 nor gives a disproof of that near-linear target.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-346) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/183.md). HalvingLines comparator states the same fixed power saving for general-position sets, and a separate all-level bound for a stronger generic condition. Main declaration uses sorry; no local verification claimed. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/346-planar-halving-lines.md).
