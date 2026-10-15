# AIM 645: a finite three-ample complex

**PR:** [116](https://github.com/MColbrook/AIM/pull/116). **Head:** `c70ec0a591029633fd15aa2568c3b71e9adbd3fe`. **Review date:** 2026-10-15. **Decision:** Solved.

Independent Codex AI review in the maintainer's session, without participation in preparing the submission; no human or Lean verification is claimed. The entire three-page source/PDF, README and target comparison were examined against the current and pinned AIM statement.

[Proof](../../solutions/645-finite-three-ample-nonsimply-connected/paper/finite_three_ample.pdf).

The permitted sets are downward closed and have at most four vertices, with labels lying in one vertex or edge of a four-cycle. Requiring all lower marks yields an actual simplicial complex. The four designated edges survive, and projection to their four-cycle is simplicial with a section in every outcome. Thus retaining the retract does not depend on a successful random sample.

For an arbitrary set U of at most three vertices, a missing label q leaves the opposite label t able to cone every permitted face of U. This includes repeated labels and the case where the two other labels are nonadjacent, since no permitted face contains both. Each candidate outside U and outside the section has at most seven unfixed cone marks. Conditioning on the entire induced complex on U only uses internal marks. Candidate cone-mark sets are disjoint, giving genuine conditional independence. Requiring exactly the marks of an arbitrary subcomplex A gives exact link equality; face closure of A proves inclusion and a zero cone mark proves exclusion. Empty A and noninduced A are included.

For each U the failure probability is at most 128 times $`(127/128)^{8188}`$. The union bound over all U is at most $`2^{54}(127/128)^{8188}<2^{-9}<1`$, since the 128th power of 127/128 is less than one-half and 8188 exceeds 128 times 63. Thus some finite outcome realizes every request simultaneously. Its simplicial retract induces an injection from the circle fundamental group. Connectivity follows independently from the two-vertex extension request. The result meets every finite three-ampleness quantifier, with no flag assumption.

All three references were checked against primary texts: [Farber](https://arxiv.org/pdf/2301.07404), Example 2.5, actually asks for a finite example; [Barmak v1](https://arxiv.org/pdf/2103.03952v1), Theorem 1 and Example 6, give the infinite comparison and four-cycle model, not the finite conclusion; [Hatcher](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf), Theorem 1.7 and printed p.34, supply the circle group and functoriality. Bibliographic identities and cited scope agree. The probability estimate and construction are self-contained, so a sampled face list is unnecessary. All three rendered PDF pages are legible and consistent with the complete source. Build/integrity receipts are recorded separately during integration.

No unresolved gap was identified. The number 32,768 is an existence upper bound, with no minimality or efficient sampling claim.
