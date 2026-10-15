# AIM 610: independent review of PR #107

Date: 2026-10-15. Reviewer: OpenAI Codex, independent AI review in the receiving repository; no human review or Lean verification is asserted.

PR: [#107](https://github.com/MColbrook/AIM/pull/107). Reviewed head: `b8c005ee5480e2030ae189b2035d3eb9e24401a2`.

Outcome: **Solved** — An explicit45-dimensional reflexive polytope violates the conjectured facet bound.

Proof: [manuscript.pdf](../../../research/solutions/aim-610-reflexive-facet-counterexample/paper/manuscript.pdf). The original problem page, complete manuscript, target comparison, package README and other supplied explanatory material were compared.

## Mathematical audit

In a fixed orthant the clipped cube $`R_{m,r}=\{x:|x_i|\le1,\ \sum_i|x_i|\le r\}`$ has vertices precisely those vectors with exactly $`r`$ nonzero coordinates, each equal to $`\pm1`$. Perturbing two fractional coordinates excludes a fractional vertex, and a vertex with fewer nonzero coordinates lies on a segment. Thus there are exactly $`2^r\binom mr`$ vertices. The inequality description and a direct separation argument identify its polar as the convex hull of the coordinate vectors and all sign vectors divided by $`r`$.

For the height-one base and height-minus-one apex pyramid $`T(R)`$, the polar inequalities give exactly $`\mathop{conv}((2R^*,-1)\cup\{(0,1)\})`$. Each iteration doubles all previous polar coordinates and adds an integral apex; primal coordinates remain integral throughout. Taking $`r=2^k`$ clears the initial denominators after $`k`$ iterations. The proof provides the entire primal and polar generating sets and verifies full dimension and an interior origin. Hence the resulting polytope and its polar are lattice polytopes in the standard dual lattices, as reflexivity requires.

Taking $`m=40,r=32,k=5`$ gives dimension45 and polar vertex count $`2^{32}\binom{40}{32}+5`$. Every listed base vertex remains a pyramid vertex. Polarity gives a bijection between these vertices and facets of the dual polytope, proved by an exposing hyperplane argument. Independent integer recomputation gives $`F=330303106984181765`$ and $`F^2-6^{45}=5154504949354948553223060244660249>0`$. This establishes the full counterexample alternative; it asserts no minimal counterexample dimension.

## References and scope

[Nill's original text](https://arxiv.org/pdf/math/0405448v1), Conjecture5.2, states the unrestricted reflexive vertex bound; duality converts it to the requested facet bound. The [Mori–Mori–Ohsugi primary paper](https://arxiv.org/html/2511.22981) and [Haase–Melnikov](https://arxiv.org/pdf/math/0406485v1) have the cited titles and contextual statements. The construction does not rely on the general reflexive-embedding theorem: integrality, polarity and facet counting are proved directly.

## Delivery checks

All four PDF pages, including the exact arithmetic and bibliography, were visually inspected. Complete ancillary prose and target comparison were read. The integer comparison was independently rerun using Python's arbitrary-precision integers. No Lean certificate is claimed.
