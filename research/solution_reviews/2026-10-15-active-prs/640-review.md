# AIM 640: independent review of PR #112

Date: 2026-10-15. Reviewer: OpenAI Codex, independent AI review in the receiving repository; no human review or Lean verification is asserted.

PR: [#112](https://github.com/MColbrook/AIM/pull/112). Reviewed head: `3d9df8678f27469a74af9ca2d81ec5ec11157316`.

Outcome: **Solved** — Elementary abelian2-groups deterministically refute the proposed uniform random coboundary-expansion assertion.

Proof: [main.pdf](../../../research/solutions/640-random-balanced-cayley-obstruction/paper/main.pdf). The original problem page, complete manuscript, target comparison, package README and other supplied explanatory material were compared.

## Mathematical audit

Squarefree Boolean monomials of degree at most $`k`$ are linearly independent as functions on $`\mathbb F_2^d`$, by induction on supports. Their function space has dimension $`N_k(d)=\sum_{j\le\min(k,d)}\binom dj`$. Vanishing on $`A`$ imposes at most $`|A|`$ conditions.

Expanding a polynomial at the sum of $`k+1`$ vertex labels assigns each monomial term to a fixed omitted vertex part: its degree is at most $`k`$, so at least one part is unused. Those assigned terms define a cochain on the complete join's codimension-one faces. Its coboundary is exactly the polynomial of the total label. If the polynomial vanishes on $`A`$, the cochain is a cocycle on the sampled Cayley complex. If that cocycle were a boundary there, it would be the same boundary on the complete join, since the complexes have identical lower skeletons. Applying the coboundary again on the complete join would make the polynomial vanish at every possible total label. Evaluating at $`(t,0,\ldots,0)`$ gives the zero function, proving injectivity. Repeated group labels occupy distinct join parts and are legitimate vertices, so this evaluation does not require a nonexistent simplex.

Thus cohomology dimension is at least $`N_k(d)-|A|`$. A nonzero class has zero coboundary numerator and strictly positive distance from boundaries, so it gives expansion exactly zero under the stipulated unnormalized convention. Every irreducible complex representation of a binary vector group is one dimensional: commuting involutions split into common sign eigenspaces. Therefore $`D(G)=2^d`$. For fixed $`k\ge2`$ and any fixed proposed constant, the logarithmic sample size is eventually smaller than $`N_k(d)`$ and is an admissible subset size. The obstruction holds for every such subset, not merely with probability bounded away from one.

## References and scope

[Meshulam's primary manuscript](https://arxiv.org/html/2211.02085v1), Sections1–2 and Conjecture8.1, was checked for the ordered group-product convention, complete lower skeleton, cochain expansion and definition of $`D(G)`$. The binary groups have orders tending to infinity as required; one fixed allowed dimension already contradicts universal constants. The submitted algebraic obstruction is self-contained and does not assume a probabilistic independence statement.

## Delivery checks

All three manuscript pages, complete target comparison and ancillary material, including AI_USE.md, were read and visually inspected. No numerical experiment or Lean replay is used.
