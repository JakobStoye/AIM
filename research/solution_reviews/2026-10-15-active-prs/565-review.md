# AIM 565: independent review of PR #105

Date: 2026-10-15. Reviewer: OpenAI Codex, independent AI review in the receiving repository; no human review or Lean verification is asserted.

PR: [#105](https://github.com/MColbrook/AIM/pull/105). Reviewed head: `b5f09f361de0b7d745f3412dc392507fc4c30039`.

Outcome: **Solved** — A square pyramid is a counterexample to the proposed Macbeath-center asymmetry inclusion.

Proof: [macbeath_counterexample.pdf](../../../research/solutions/565-macbeath-center-asymmetry/paper/macbeath_counterexample.pdf). The original problem page, complete manuscript, target comparison, package README and other supplied explanatory material were compared.

## Mathematical audit

For the pyramid $`0\le z\le1`$, $`|u|,|v|\le1-z`$, the overlap of the body with its point reflection has rectangular horizontal sections. Translating the center off the vertical axis cannot increase either section overlap length, and decreases the product on a nonempty interval whenever the overlap is positive. Thus it suffices to optimize the explicit axial volume; centers outside the permitted height interval give zero volume.

Direct integration gives $`V(t)=\frac83[(1-t)^3-(1-2t)^3]`$ on $`[0,1/2]`$ and $`V(t)=\frac83(1-t)^3`$ above it. The claimed $`\alpha=(3-\sqrt2)/7`$ is the unique maximizer. In particular the factorization $`V(\alpha)-V(t)=\frac83(t-\alpha)^2(3+2\sqrt2-7t)`$ proves strict maximality on the first interval; monotonicity handles the other one. The off-axis strictness proves uniqueness over all possible centers, as required by the definition.

Reflecting the apex through this center with the conjectured one-third factor gives height $`(5-4\sqrt2)/21<0`$. It therefore lies outside the pyramid. One such point suffices to contradict the proposed inclusion, with the specified unique Macbeath center rather than another symmetry center. The argument and all constants are self-contained.

## References and scope

[Ivanov's versioned primary text](https://arxiv.org/html/2403.14761v3), Conjecture2.1, was checked for the Macbeath functional, uniqueness requirement and exact dimensional inclusion. The citation metadata/version matches. No other external theorem is needed for the explicit volume calculation and counterexample.

## Delivery checks

The complete two-page PDF was visually inspected, including its formulas and citation; the submitted source and explanatory documents were read. No numerical search or Lean result is being treated as a proof.
