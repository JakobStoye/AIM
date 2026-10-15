# AIM 525: independent review of PR #98

Date: 2026-10-15. Reviewer: OpenAI Codex, independent AI review in the receiving repository; no human review or Lean verification is asserted.

PR: [#98](https://github.com/MColbrook/AIM/pull/98). Reviewed head: `71a40d1b23893948a5e9e6f800130b198ee70f07`.

Outcome: **Solved** — A positive-norm surface product has no degree-four class of the proposed TC weight.

Proof: [counterexample.pdf](../../../research/solutions/525-positive-norm-tc-weight/paper/counterexample.pdf). The original problem page, complete manuscript, target comparison, package README and other supplied explanatory material were compared.

## Mathematical audit

The genus-two surface product is closed, connected, oriented and aspherical. Bucher–Karlsson's real simplicial volume is24; every rational representative is also a real representative with the same chain norm, so the required rational infimum is at least24 without assuming equality of coefficient-field infima. The map h(x,y)=(x,b) factors through a2-dimensional surface, hence kills every degree4 class. For F=(id,h), F*bar(u)=-u is nonzero for every nonzero u. Three disjoint-color unions of barycentric open stars cover the second surface and each contracts to the basepoint via its vertex and a fixed path. Keeping x fixed gives actual continuous compact-open path sections on the three product domains. Thus the same permitted F has pullback genus≤3 and nonzero pullback for all nonzero u, making the vanishing condition fail for every integer r≥3. Consequently weight≤2. This addresses the problem's existential quantifier for class choice.

## References and scope

Checked Bucher–Karlsson math/0703587v2 Corollary3, giving24(g-1)(h-1), and Neofytidis2212.08962v2 Question5.1(a) and Example5.7, the latter indeed includes TC=9 for two hyperbolic surfaces. Farber–Grant's sectional-weight convention and Macias–Virgos–Mosquera-Lois's distance/genus product statements have the quoted roles; the needed local sections are independently constructed in full. Hatcher's surface covers, cohomological dimension and duality are standard applicable facts. The five-entry bibliography covers the external inputs.

## Delivery checks

Read complete source, README and target comparison. Visually inspected all three PDF pages; complete formulas and references are present without clipping. The proof is analytic and requires no numerical certificate.
