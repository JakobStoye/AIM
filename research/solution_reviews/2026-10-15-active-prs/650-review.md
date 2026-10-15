# AIM 650: the first path Betti number central limit theorem

**PR:** [117](https://github.com/MColbrook/AIM/pull/117). **Head:** `6dd971c850a3088134f2fccb747b26a1a027eef2`. **Date:** 2026-10-15. **Decision:** Solved.

Independent Codex AI review in the maintainer's session; the reviewer did not develop this submission. This is not human peer review or Lean verification. The entire six-page source/PDF and every ancillary prose document, including REFERENCES and AI_USE, were examined against the pinned/current target.

[Proof](../../solutions/650-random-digraph-path-betti-central-limit/manuscript.pdf).

The incidence rank gives the exact identity B=M-n+C-R without connectivity. I reconstructed the nonregular two-chain spanning family by grouping paths by ordered endpoints: a present shortcut allows individual triangles; an absent shortcut requires zero-sum path coefficients; diagonal endpoints require differences of reciprocal paths. This retains, rather than silently discards, diagonal boundary terms.

The overcomplete family is monotone under adding an edge, including triangles created by adding their shortcut. Rank changes are therefore bounded by the number of new generators in a fixed ambient edge-coordinate space. For two root-containing diamonds sharing one free vertex, the simple four-cycle support has at most one other common edge beyond the root; hence at least five nonroot directed coordinates are required. The two/shared-zero cases require at least three/six. The displayed multiplicities bound all root positions and orders. Reciprocal generators use an independent reverse-edge indicator and disjoint reciprocal pairs. Combining their second moments gives the stated bound in terms of $`np^2+n^2p^3`$, which tends to zero throughout the full requested sequence range. The martingale proof of the Bernoulli variance inequality is valid and supplies negligible variance of R.

The fixed-vertex component estimate uses a tree upper count, absent cut edges, and a geometric series as nq tends to infinity. It does not claim the whole graph is connected. Removing the root unordered edge and dividing by its absence probability correctly bounds the squared directed-edge change in C. This proves negligible component variance even below the connectivity window.

Consequently the true-centered Betti number differs from the true-centered binomial edge count by an error small in L2 relative to its standard deviation. The reverse triangle inequality gives the actual variance asymptotic and eventual positivity. The characteristic-function Taylor remainder is uniformly bounded by the displayed third-derivative estimate; the binomial variance diverges. Transfer to the actual denominator and Levy continuity prove precisely the target, for arbitrary sequences satisfying its two limits.

All three references and REFERENCES.md were checked: [Chaplin](https://arxiv.org/pdf/2111.13493), Conjecture B.2 and Section 3.3, give the actual nonregular target/background; [Dobler v1](https://arxiv.org/pdf/2111.01603v1), Theorem 1.1, has the stated real-Borel continuity theorem. The [author-hosted Chatterjee notes](https://souravchatterjee.su.domains/stat310a-lecture-notes.pdf) were downloaded independently after the web reader failed; Proposition 5.11.1, printed pp.53-54, indeed gives the standard normal characteristic function under the printed convention. Journal/preprint metadata and source locators agree, with no missing mathematical premise. All six PDF pages were visually inspected and are legible and consistent with the source; build/hash receipts are separate integration evidence.

No unresolved gap was identified. This proves the rational rank statement, not an absence-of-torsion result.
