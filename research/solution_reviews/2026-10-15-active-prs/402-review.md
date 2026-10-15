# AIM 402: independent audit of PR #159

Date: 2026-10-15. Reviewer: independent OpenAI Codex AI context; no human or Lean verification is claimed.

Pinned submission: [404bb40f6a5f795b8c61ff2abc0b3914dd003e0b](https://github.com/MColbrook/AIM/pull/159), compared with the original a153f469ee0ea64e876b2ad97c79d252c19a3e22 target and current problem page.

**Decision:** Solved. The exact product-L2 logarithmic interpolation inequality holds for the two distinct Caputo orders and every initial pair.

**Scope:** The entire manuscript, bibliography, package README, target comparison, AI disclosure and ancillary build/manifest material were read. The analytic proof was independently reconstructed; submission-internal AI reviews were not treated as evidence of correctness. Every submitted PDF page was visually inspected in the maintainer-rendered contact sheets. No clipping, missing mathematics, unreadable glyphs or broken cross-reference was found. Package hash and independent rebuild results are recorded separately by the maintainer.

Theorem 1 treats the original common Dirichlet Laplacian, the exact diagonal/off-diagonal reaction terms, all 0<alpha_1<alpha_2<1, every T>0 and arbitrary signed or complex L2 pairs. The exponents remain exactly 1-t/T and t/T; no positivity assumption on the initial data is introduced.

For each Dirichlet eigenvalue lambda, put q=lambda-1>-1. The Laplace resolvent retains both distinct initial factors. Its negative-axis jump matrix W=M^(-*) B M^(-1)/pi is real symmetric positive definite. The keyhole integral includes a positive-axis rank-one residue precisely when q<1; the singular q=1 case is separately integrable. These facts yield F=I-GA for the modal fundamental matrix.

Finite-time invertibility was reconstructed in all three regimes. If q>1, A and the Laplace-mixture matrix are positive. If q<1, the corrected symmetric matrix has a negative direction inherited from A^(-1), while on the residue kernel it is strictly positive, so its two eigenvalues have opposite signs. If q=1, the rank-one determinant formula gives a strictly positive mixture integral. Thus neither growing low modes nor lambda=2 are excluded.

For q>=2, conjugation by A^(1/2) yields a positive decreasing matrix S. Its Laplace bound gives ||F(t)||<=M/(1+q t^b). Restricting the positive jump integral to r in [1,2] gives a lower singular-value bound c/q at T, uniformly over all high modes. Convexity of -log(1+q t^b) produces the exact t/T interpolation exponent. Finitely many remaining modes are controlled by compact-time continuity and invertibility. Parseval followed by Hölder sums the modal inequalities for arbitrary infinite superpositions with one constant independent of the data. No simultaneous diagonalization of the time derivatives is used.

The precise open example is displayed in [Chorfi, §5](https://arxiv.org/pdf/2506.19954v1). The [Li–Huang–Liu mixed-order framework](https://arxiv.org/abs/2209.03767), published DOI 10.1007/s13540-023-00149-0, permits the same moderately coupled smooth elliptic system; its Definition 1 and Theorem 1 justify the mild framework. The fundamental-matrix construction, invertibility and uniform-frequency bounds are all proved here. Common-order results by Chorfi–Maniar–Yamamoto and Feng–Liu–Lu are credited as benchmarks and not falsely used for unequal orders.
