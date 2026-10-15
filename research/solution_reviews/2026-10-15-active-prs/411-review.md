# AIM 411: independent audit of PR #162

Date: 2026-10-15. Reviewer: independent OpenAI Codex AI context; no human or Lean verification is claimed.

Pinned submission: [b9b2b7c64b7a18bc805acca39e40aca6c0ab53b9](https://github.com/MColbrook/AIM/pull/162), compared with the current problem page and its cited a153f469ee0ea64e876b2ad97c79d252c19a3e22 statement.

**Decision:** Solved. Admissibility for all strongly measurable bounded inputs implies zero-class admissibility and norm-continuous convolution states on every closed finite interval.

**Scope:** The entire submitted manuscript, package README, target comparison, disclosure and build instructions were read. This mathematical report is separate from the maintainer package checksum, rebuild and PDF-render records; it does not claim visual checks that have not been recorded.

The main potential failure points are separability in the actual X norm, use of scalar rather than vector-valued Grothendieck theory, and the quantifier upgrade from one input to the whole input ball. All are addressed constructively.

For a fixed strongly measurable w, its values lie almost everywhere in a separable U0. The closed span E of semigroup orbits of $`R_{-1}BU_0`$ is separable and invariant. For every scalar multiplier, the resolvent of its admissible state lies in E. Since that resolvent image is in D(A), invariant difference quotients put its generator image in E too, hence the original state is in E. This proves actual X-norm range separability, not merely weaker extrapolation-norm separability.

González–Kania v3 Theorem 3.1.1(3) and Proposition 4.1.5 were checked in the primary full text: scalar L-infinity is Grothendieck and all its bounded operators to separable Banach spaces are weakly compact. This applies exactly to the fixed-w multiplier. For any disjoint sets and any subseries, the partial sums lie in a common weakly compact set; their extrapolation-space integrals converge in norm. Injectivity of X into X-minus-one identifies every weak cluster point, so the entire subseries converges weakly. The classical Orlicz–Pettis theorem gives norm convergence and norm countable additivity. The proof includes decreasing interval tails and null endpoints.

If uniform operator-norm decay failed, nearly optimal bounded inputs can be trimmed to pairwise disjoint intervals without losing half their state norm. Their countable pasted input remains strongly measurable with bounded norm and separable essential range. Applying the preceding vector measure to this one input forces those disjoint interval states to tend to zero, a contradiction. Thus the uniform small-time limit is proved rather than inferred from pointwise convergence.

Finally the convolution is split at a fixed earlier time. One fixed semigroup orbit is continuous, and both short tails are bounded by the proved small-time operator norm. This handles interior two-sided continuity, the initial endpoint and the terminal relative endpoint without assuming operator-norm continuity of S.

Weiss supplies the standard extrapolation conventions; Preußler–Schwenninger v1 Corollary 4.10 and its discussion were checked and accurately describe the previous partial geometric results. Diestel's cited classical results are Orlicz–Pettis and Pettis measurability; the proof uses their full Banach dual/strong measurability hypotheses and explicitly addresses the real-field reduction. This result concerns the given Bochner B-convolution representation; no broader axiomatic input-map conclusion is inferred.

**PDF visual check:** Every submitted PDF page was subsequently inspected in the maintainer-rendered contact sheets. No clipped content, missing mathematics, unreadable glyph or broken cross-reference was found. The independent rebuild and checksum evidence is recorded separately.
