# AIM 513: independent review of PR #96

Date: 2026-10-15. Reviewer: OpenAI Codex, independent AI review in the receiving repository; no human review or Lean verification is asserted.

PR: [#96](https://github.com/MColbrook/AIM/pull/96). Reviewed head: `4655a5f9b31788994fe60892844b8c3cec0f337b`.

Outcome: **Solved** — An oriented flat five-manifold contradicts the universal centre-rank TC formula.

Proof: [main.pdf](../../../research/solutions/513-kaiwen-jin-flat-counterexample/paper/main.pdf). The original problem page, complete manuscript, target comparison, package README and other supplied explanatory material were compared.

## Mathematical audit

Each affine generator squares to a coordinate unit translation. Modulo that lattice the generators form a free order32 action: the smallest selected index always has a half translation untouched by larger indices. The quotient is compact, connected, oriented (even row sums), flat and covered by R5. A central affine element must have linear part I because it commutes with every unit translation, and its vector must be fixed by each diagonal holonomy, forcing coordinates2,4,5 to vanish. Coordinates1 and3 supply two independent central translations, so the rational centre rank is exactly2. The published Bott ring uses columns of the displayed upper triangular matrix and produces precisely the five stated relations. Monic division proves all squarefree monomials independent. Recomputed u²=ab,u³=abc,u⁴=0, d⁴=abcd,d⁵=0; the odd binomial terms in bar(d)^5 are exactly the1/4 split. Multiplication by bar(a)bar(b)bar(e)^2 leaves abcd tensor abcde plus its transpose. Their bidegrees differ and both are nonzero. This is nine degree-one zero-divisor factors, so Farber's unreduced lower bound is10. No exact TC calculation is needed.

## References and scope

Kamishima–Masuda0807.4263v1 Lemma2.1, equation3.1 and Lemma3.1 were checked in the original text: the affine realization and cohomology presentation match the same matrix convention; orientation also matches Lemma2.2. Farber math/0111197v1 Theorem7 uses the unreduced strict-greater-than cup-length convention. Neofytidis2212.08962v2 Question5.8 is the stated centre-rank conjecture. All three references and normalizations match.

## Delivery checks

Read complete source and all three ancillary Markdown documents, including VERIFICATION.md. All three rendered PDF pages visually inspected. The ring calculation is printed in full; authoring search code is not required or invoked. No substantive mathematical correction identified.
