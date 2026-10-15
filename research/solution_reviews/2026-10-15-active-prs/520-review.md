# AIM 520: independent review of PR #103

Date: 2026-10-15. Reviewer: OpenAI Codex, independent AI review in the receiving repository; no human review or Lean verification is asserted.

PR: [#103](https://github.com/MColbrook/AIM/pull/103). Reviewed head: `de58527e481c71125a9a1868c56b5843b76826da`.

Outcome: **Solved** — The unrestricted persistence-diagram space has no coarse embedding into Hilbert space for every p in the remaining interval[1,2].

Proof: [main.pdf](../../../research/solutions/520-kaiwen-jin-coarse-persistence-diagrams/paper/main.pdf). The original problem page, complete manuscript, target comparison, package README and other supplied explanatory material were compared.

## Mathematical audit

The key realization is exact on each finite family, with constants that disappear before the coarse obstruction is invoked. On an integer square grid, signed balanced vectors have an integral optimal transportation flow. Cancelling cycles and routing each shipment along unit taxicab-grid steps produces a flow whose off-diagonal cost for every power $`p\ge1`$ is its transport cost with the maximum norm. A sufficiently large common integer background supplies the intermediate mass at every grid vertex. Its size may depend on the finite family, which is allowed; the final exact metric identity does not.

For rational coefficients a common denominator is cleared and the diagram is rescaled by its negative $`1/p`$ power. Translation sufficiently far from the diagonal makes every unmatched-point deletion more expensive than completing the matching inside the bounded diagram grid. Hence the persistence metric is exactly the $`1/p`$ snowflake of the signed transport norm, rather than just comparable with an uncontrolled family-dependent distortion. The lower bound uses $`d^p\ge d`$ for distinct integer-grid points; the upper bound uses the unit flow. The integral coupling argument is justified by cycle elimination, not an assumption that every real optimizer is integral.

If a coarse Hilbert embedding existed, every finite subset of every rational grid-transport space would inherit the same two control functions. The Euclidean and maximum-norm transportation costs differ by at most $`\sqrt2`$, independently of grid size. Nowak's finite-subset criterion preserves these controls. Countability puts each resulting image in a separable Hilbert space and hence in $`L^2`$. Rounding every real balanced vector to a rational one within transport distance one then changes distances by at most two; this produces common controls on all the real grid-transport spaces. Naor–Schechtman's Theorem3.7 forbids precisely that family of controls. No bounded-cardinality diagram space is asserted to fail to embed.

## References and scope

The actual [Naor–Schechtman author text](https://web.math.princeton.edu/~naor/homepage%20files/planar-earthmover.pdf), Theorem3.7, was checked for its signed balanced grid spaces and uniform coarse-$`L^2`$ statement. [Nowak](https://arxiv.org/pdf/math/0404401), Theorem3.4 and its negative-kernel proof, supplies the needed unchanged finite-subset controls. [Pritchard–Weighill](https://link.springer.com/article/10.1007/s00454-024-00674-6) identifies exactly the remaining interval and the all-finite-diagram convention. The Andoni–Naor–Neiman reference has correct authors/title/arXiv metadata and serves as surrounding context rather than an unproved reduction.

## Delivery checks

All five manuscript pages and bibliography were visually inspected. The complete target comparison and ancillary material were read. This is an analytic proof; no numerical or Lean verification is claimed.
