# AIM 547: independent review of PR #104

Date: 2026-10-15. Reviewer: OpenAI Codex, independent AI review in the receiving repository; no human review or Lean verification is asserted.

PR: [#104](https://github.com/MColbrook/AIM/pull/104). Reviewed head: `78e2c3a174f566dcdb63a2c3579ffafb34e28a4c`.

Outcome: **Solved** — The proposed Morse quantity bounds the largest coordinate size of the canonical minimal persistence grid.

Proof: [grid_morse_bound.pdf](../../../research/solutions/547-minimal-persistence-grid-morse-bound/paper/grid_morse_bound.pdf). The original problem page, complete manuscript, target comparison, package README and other supplied explanatory material were compared.

## Mathematical audit

Reindexing consecutive coordinate values by integers preserves the free presentations and multigraded Betti numbers, so it is legitimate to work on the canonical finite grid. For one coordinate value $`t`$, choose a minimal grade $`u`$ where any homological degree has a generator or first relation on that coordinate slice. At every lower corner $`u-e_\alpha`$ with nonempty $`\alpha`$ avoiding the selected coordinate, minimality makes the relevant presentation identical to the one one step lower in that coordinate. Thus the induced module maps there are isomorphisms.

The Koszul complex at $`u`$ splits as the mapping cone of the selected-coordinate map. Its components in positive exterior degree are isomorphisms. Given a cycle, solving with that isomorphism explicitly removes it in degrees at least two. If its degree-zero component is injective, the same argument removes degree-one cycles. In the top simplicial dimension, homology maps under inclusions are injective because there are no chains one degree higher; this also covers ordinary zero-dimensional homology. Therefore the top-dimensional first-relation term at the chosen grade vanishes.

At least one of the selected generator or first-relation terms is positive. All subtractive higher-Koszul terms at that grade vanish by the cone argument, and the exceptional top-degree relation is absent. The defined nonnegative Morse summand at $`u`$ is consequently at least one. Distinct values $`t`$ in a fixed coordinate give distinct grades $`u`$. Summing shows $`L\ge|G_j|`$ for every coordinate and hence the asserted maximum. The proof uses the grid derived from all degrees' zeroth and first Betti supports, not a smaller hand-selected presentation grid.

## References and scope

The definitions and exact Morse quantity were compared with [Harrington–Tillmann–Torras-Pérez primary manuscript](https://arxiv.org/html/2608.04640v1), including the minimal-grid lemma, the Koszul convention, the quantity in Section1.4 and Remark5.12. The underlying Morse-inequality citation is contextual; the needed local cone calculation and top-dimensional injection are proved directly in this submission. No extra generic-position or dimension-positive hypothesis is introduced.

## Delivery checks

All four manuscript pages, formulas and references were visually inspected; complete ancillary prose and target comparison were read. No computational or Lean certificate is used.
