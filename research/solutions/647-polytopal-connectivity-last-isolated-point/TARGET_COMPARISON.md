# Target comparison

Public target: [AIM 647 at revision a153f469ee0ea64e876b2ad97c79d252c19a3e22](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/647-polytopal-connectivity-last-isolated-point.md).

Submitted manuscript: *Connectivity when isolated vertices disappear in a convex polytope*, Kaiwen Jin, October 14, 2026. All locations below refer to the supplied nine-page manuscript.

| Original requirement | Manuscript result and location | Scope |
| --- | --- | --- |
| Every fixed integer d ≥ 3 | Theorem 1.1, page 1; final proof, Section 5 | Full target |
| Every fixed compact convex polytope A in R^d with nonempty interior | Theorem 1.1 and face geometry in Section 2, pages 1–3 | Full target, including arbitrary fixed edges and corner angles |
| Independent points uniformly distributed in A | Introduction and f_0 = 1/volume(A) in Section 2; binomial void and second-moment estimates in Section 3 | Same data class; no Poisson approximation assumption |
| Closed Euclidean graph, n ≥ 2 | Introduction, equation (1), and closed-ball convention in Section 2 | Same model and threshold conventions |
| L_n is the largest nearest-neighbour distance; M_n is the connectivity radius | Equation (1), page 1 | Exact definitions |
| Probability of exact equality L_n = M_n tends to one | Theorem 1.1; Propositions 3.1–3.3 and 4.2; Section 5, pages 8–9 | Complete affirmative solution claim |
| Apply component control at the random radius L_n | Proposition 3.2 excludes all medium separated subsets; Proposition 4.2 uses one fixed net for all s ≥ r_n; Section 5 uses Proposition 3.3 to place L_n above r_n | Uniform-radius argument supplied in the manuscript |
| Fixed-domain constants and asymptotic quantifiers | Section 2 conventions, Sections 3–4 fixed auxiliary choices, and Section 5 closing paragraph | Constants may depend on fixed A and d; no uniformity over varying polytopes claimed |

The claim is exact equality of the two radii with probability tending to one. A common leading scale or convergence of M_n/L_n alone is not used as a substitute for this conclusion.

## Imported results and their application

| Public source | Exact locator | Application in the manuscript |
| --- | --- | --- |
| R. J. Gardner, *The Brunn–Minkowski inequality*, Bulletin AMS 39 (2002), 355–405, [DOI](https://doi.org/10.1090/S0273-0979-02-00941-2) | Theorem 4.1 and equation (11), printed page 362 | Lemma 2.3 applies the full power inequality to nonempty compact sets E and C intersect B_1; E need not be convex or have positive volume. |
| M. D. Penrose, X. Yang and F. Higgs, *Largest nearest-neighbour link and connectivity threshold in a polytopal random sample*, J. Appl. Comput. Topol. 8 (2024), 1723–1750, [DOI](https://doi.org/10.1007/s41468-023-00154-5) | Section 3.4, results 3.13–3.17, definitions (3.20)–(3.21), territory definition following Proposition 3.15 | Section 2.1 restates the face-territory partition and supplies the exact local-cone, cube-count and normal-integral deductions. |
| Same Penrose–Yang–Higgs source | Lemma 3.14, Proposition 3.15; deterministic portion of the proof of Lemma 3.12, equation (3.18) | Section 4 uses unicoherence and the small-ball complement property. Lemma 4.1 supplies the separator argument in full. Proposition 4.2 then derives its own uniform-radius fixed-net probability bound. No supercritical-radius probability conclusion from Lemma 3.12 is imported. |
| Same Penrose–Yang–Higgs source | Remark 2.9 and the leading-scale results | Introduction states the distinction between a common leading scale and the exact target. These results are background rather than a premise for the hitting-time lift. |
| M. D. Penrose and X. Yang, *Fluctuations of the connectivity threshold and largest nearest-neighbour link*, [arXiv:2406.00647v3](https://arxiv.org/abs/2406.00647v3) (2024) | Theorem 1.1 and equation (1.5) | Introduction records the smooth-domain and planar convex-polygon results. They do not supply the general d ≥ 3 polytopal theorem proved here. |

The manuscript is a complete analytic argument. Its mathematical dependencies are the cited public geometric results and ordinary measure, compactness and probability facts. No numerical experiment or unpublished supplement is required to read the proof.

## Review boundary

This is a complete solution claim awaiting independent mathematical review. The public materials do not assert maintainer acceptance, a human review or formal verification. The target's catalogue status is left unchanged by the package submission.
