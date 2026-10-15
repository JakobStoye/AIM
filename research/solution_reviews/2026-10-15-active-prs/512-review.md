# AIM 512: independent review of PR #95

Date: 2026-10-15. Reviewer: OpenAI Codex, independent AI review in the receiving repository; no human review or Lean verification is asserted.

PR: [#95](https://github.com/MColbrook/AIM/pull/95). Reviewed head: `566560482b63bbfcaf289efdf231991f9b4c2a7c`.

Outcome: **Solved** — The proposed join is the homotopy type of the ordinary strict spherical Rips complex throughout a nonempty interval after the first transition.

Proof: [main.pdf](../../../research/solutions/512-kaiwen-jin-spherical-rips-first-transition/paper/main.pdf). The original problem page, complete manuscript, target comparison, package README and other supplied explanatory material were compared.

## Mathematical audit

The distinction between the abstract Rips complex and a metric thickening is essential here. The proof uses ordered labelled tuples, allows repetitions, and realizes only face identifications; the strict comparison is applied to that model.

At the first diameter, a positive minimal relation among at most $`n+2`$ sphere points and the pairwise inner-product bound force a regular simplex with uniform coefficients. Writing any additional point in its simplex frame gives nonnegative coefficients whose sum and sum of squares both equal one, so that point is a simplex vertex. Thus the critical tuple stratum consists exactly of complete words in a rotated regular simplex. Its complement in each closed tuple sublevel is both closed and open. Positive weak slope off that stratum, compactness on positive diameter bands, and a deformation below a hemispherical scale show that the complementary realization is weakly equivalent to the original sphere through the normalized physical barycenter.

The complete-word complex relative to its incomplete words maps to a simplex relative to its boundary by adding repeated-label barycentric coordinates. Concatenation with a fixed complete word proves the pair comparison. Although a chosen inverse need not be equivariant, the comparison map is equivariant, so the associated-bundle comparison remains valid. The degreewise partition gives a pushout, and the relative full-word cells make its attaching inclusion a cofibration. The unordered regular-simplex parameter is exactly $`SO(n+1)/A_{n+2}`$; the alternating stabilizer follows from orientation. In physical coordinates, the simplex bundle is radially a trivial disk bundle. Its positive radial boundary function is bounded above and below uniformly, including continuity at the zero section. The boundary map becomes the sphere projection, and its pushout is the asserted join.

For the strict right interval, the stationary-diameter theorem supplies a gap uniform over all numbers of labels. Definable mapping-cylinder collars at the critical value are needed only one tuple degree at a time. Composing each collar equivalence with a noncritical deformation reaches every scale in that uniform gap. The inclusions commute with faces even though chosen inverse homotopies do not; fat realization therefore preserves the levelwise equivalences. Both final spaces have CW type, so the resulting weak-equivalence zigzag gives a homotopy equivalence. This proves the full target rather than only the closed endpoint or a connectivity bound.

## References and scope

The proof-critical primary texts were checked: [Mémoli–Wang](https://arxiv.org/html/2609.33009v1), Propositions 2.5, 2.6 and 2.9, Theorems 4.5 and 5.1; [Ji–Meng](https://arxiv.org/html/2309.03142v3), Lemma 4.3; [Corvellec](https://msp.org/pjm/1999/187-2/pjm-v187-n2-p04-s.pdf), Theorem 2.4; and [Ebert–Randal-Williams](https://arxiv.org/pdf/1705.03774v2), Theorem 2.2. In particular, the spectrum gap covers all labels, the collar respects function values, and realization requires no compatible choices of inverse homotopies. The AAF and ABV versioned metadata and their distinct thickening/ordinary-complex context agree with the bibliography. The Lim–Mémoli–Okutan comparison is credited through the explicit MW comparison. Standard CW approximation and Whitehead are used with their CW hypotheses.

## Delivery checks

The complete eight-page rendered PDF was visually inspected, including bibliography and equations; no clipping or unresolved references were seen. Complete manuscript, target comparison and ancillary prose were read. No numerical experiment or Lean certificate is needed or claimed.
