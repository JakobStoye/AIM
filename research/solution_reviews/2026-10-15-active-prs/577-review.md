# AIM 577: independent review of PR #90

Date: 2026-10-15. Reviewer: OpenAI Codex, independent AI review in the receiving repository; no human review or Lean verification is asserted.

PR: [#90](https://github.com/MColbrook/AIM/pull/90). Reviewed head: `d3d08ea6cb9b28c84245712fd29c50f5c091b370`.

Outcome: **Solved** — Affirmative norm convergence for the full repeated-GUE three-leg model.

Proof: [repeated_gue_three_legs.pdf](../../../research/solutions/kaiwen-jin-577/paper/repeated_gue_three_legs.pdf). The original problem page, complete manuscript, target comparison, package README and other supplied explanatory material were compared.

## Mathematical audit

The same scalar Gaussian coordinates are retained in both embeddings. Hilbert–Schmidt Gram matrices give the joint Choi norm 2/N, while the cross covariance at the identity is N^-2 times the cyclic permutation. Row/column factorization bounds every component covariance map by one. Structural induction then gives O(N^-2) convergence of every fixed deterministic covariance polynomial to its scalar value. These facts also give a direct independent route through JLNP Theorem B, since log^3(N^3)/N tends to zero. In the submitted route, the free semicircular replacement has the correct covariance and converges in norm; the quotient-algebra argument upgrades this to all matrix pencils. The Gaussian comparison retains the deterministic coefficient a0 and gives vanishing noise error. Countably many rational pencils and the linearization criterion yield the polynomial upper bound. Differentiating actual shared Gaussian coordinates gives trace variance O(N^-4), with uniform operator-norm moments justified by the same comparison. Expected word traces converge, and faithful trace powers yield the lower bound, also for non-self-adjoint P via P*P. All dimension and normalization factors were recomputed.

## References and scope

Primary versions checked: BBvH arXiv2108.06312v2 Theorem2.1, GK2604.14106v3 Corollary1.4 (the generation assumption is on the limiting base), JLNP2506.19940v3 covariance definitions and strong/weak convergence statements. Collins–Yuan2407.09065v1 and Chen–Garza-Vargas–van Handel2412.00593v3 are correctly identified as background rather than an independent-matrix theorem applied to dependent matrices. Haagerup–Thorbjørnsen's deterministic pencil and Gaussian Poincare tools have the stated role. No independence across N or full-operator-norm smallness of the cross map is assumed. The exact AIM577 target asks only this ordered pair on three sites, so omission of longer chains is no remaining part of this problem.

## Delivery checks

Read the complete source and both ancillary Markdown documents. Visually inspected all seven rendered PDF pages. No clipping, missing formula or unresolved citation was visible. Root independently rebuilt the source and compared PDF text. No computational or formal certificate is needed for this analytic proof.

Integrity clarification: exact canonical Git-blob checks confirm every submitted payload hash and byte count. The initial mismatch was caused by Windows CRLF checkout conversion. The LF attribute preserves the published bytes; no submitted hash repair is required. The rebuilt PDF text matches the submitted seven-page PDF.
