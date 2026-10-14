# Mathematical referee report

**Manuscript:** *A degree-three counterexample for the normalized upper Laplacian*, by Kaiwen Jin, dated 14 October 2026.

**Reviewer:** OpenAI Codex. This fresh reviewing instance did not prepare the construction, proof, or manuscript. The manuscript discloses preparation using the same vendor's Codex system. This is an AI review, with shared vendor and training limitations. The filesystem was shared and unrestricted: the reading boundary was observed by conduct, without technically enforced isolation. No human referee or formal verification was involved in this review.

**Review date:** 14 October 2026.

**Reviewed version:** the complete LaTeX source and all six pages of the supplied PDF.

- Source SHA-256: `f5180d8c41ce247f208d06ce9083e5d857766605330a93112c76b37d64a59404`.
- PDF SHA-256: `04ab95ce34fe237151970387cc21295d7c3f9d2f438ed2cdf6792f701a4c1572`.

Locations below use the supplied PDF's printed pages and equation numbers; `manuscript.tex` locators refer to the reviewed source. No other submitted mathematical material was consulted.

## Assessment

**Recommendation: no major objection found within the reviewed scope.** I have no required minor correction to report. This recommendation concerns a short theoretical note for the AIM problem repository; it is not a journal decision or a novelty determination.

The paper constructs an explicit countable pure three-dimensional complex of maximum triangle degree three whose usual coboundary is bounded below on the entire degree-weighted triangle cochain space. It thereby gives both a strictly positive spectral lower bound and a trivial square-summable kernel. These are the two distinct conclusions needed to contradict the two universal assertions as formulated in the specified version of Problem 643. Infinite incidence at every edge is stated prominently and is allowed by that formulation.

The substantive point is the control of the full space. The disjoint square-summable fillings alone control only attachment triangles. The second estimate, using the body coboundary equations and the binary-tree gradient, controls the complementary triangle coordinates. I checked this completion rather than inferring coercivity from the fillings or from absence of an exhibited kernel vector.

## Claims and mathematical examination

| Claim | Location | Examination and result |
|---|---|---|
| The recursive construction is an abstract countable pure complex, with one degree-one triangle and all others of degree three. | Section 2, pp. 2–3; `manuscript.tex:112–174`. | The copy labels distinguish new vertices and faces; only the bridge target is an old triangle. The E, V, and initial-triangle cases exhaust the facets and give the asserted degrees. No surviving objection. |
| Each attachment target has a filling of squared counting norm four, through the bounded top adjoint. | Section 3, pp. 3–4, (7)–(10); `manuscript.tex:194–248`. | The signs, finite boundary identity, tail norm, and final degree factors agree. The limit uses a bounded operator, without applying a lower boundary at an infinitely incident edge. No surviving objection. |
| The coboundary controls every triangle coordinate with the displayed constant. | Section 4, pp. 4–5, (11)–(16); `manuscript.tex:253–323`. | Orthogonal fillings give the target bound; the three-cycle matrix and the parent/child maps give the V bound. Their sum gives precisely the stated constant. No surviving objection. |
| The spectral enclosure holds on the full Hilbert space and refutes both source assertions. | Theorem 1, p. 1; completion, p. 5; `manuscript.tex:63–81` and `manuscript.tex:325–356`. | Boundedness, self-adjointness, coercivity, and the two-sided resolvent criterion are used correctly. Both degree comparisons use d = 3 and D = 3. No surviving objection. |

The following possible failures were specifically tested against the paper's actual reasoning.

**Additional cofaces from later attachments.** Reuse of apex vertices makes this a real issue to check. A body in a new copy has only two old vertices; it cannot contain an old triangle. A bridge has only its prescribed apex triangle as an old triangle. New non-target triangles contain a vertex labelled by their own copy, which also distinguishes them from earlier triangles and from new triangles in other copies. Consequently each E triangle gains exactly its own child bridge, and no V triangle gains an uncounted later coface. At a tree root, a V triangle has two body cofaces and one bridge; away from the root it has three body cofaces. The argument on pp. 2–3 addresses this attack.

**A cocycle supplied by a lower face.** The usual finite-support construction from a finitely incident edge cannot be invoked here: every edge is shown to acquire infinitely many triangle cofaces (p. 3; `manuscript.tex:171–174`). More decisively, the subsequent estimate addresses arbitrary members of H, including any square-summable cocycle that might arise by cancellation. No nonzero such cochain is left outside its coordinate partition. This is not an assertion that the example settles a separately restricted locally finite problem.

**Incorrect weights or an unjustified infinite-chain boundary.** In (7), division by the actual triangle degree is required. This produces a target of value 1/m(F), whose H pairing with f is exactly f(F). The leaf remainder in Section 3 has squared weighted norm 2 to the power minus N, and the filling tail has squared counting norm 3 times 2 to the power minus N. Both vanish. At N = 0 the formula reduces to the single bridge and remains valid. The passage to (10) therefore takes place through the bounded top adjoint. The paper does not assume continuity of a lower boundary operator that its infinite edge incidences would put in question.

**Loss of the uncontrolled V coordinates.** Equations (11)–(12) alone would be insufficient. In the stated orientations, a body boundary gives e_q − e_p plus the child-minus-parent difference of g, agreeing with (13). The displayed matrix has B*B = 3I − J and norm at most square-root three. On the counting binary tree, the parent-value map has norm square-root two times the vertex norm, while the child-value map has norm at most the vertex norm. The reverse triangle inequality thus gives the positive constant square-root two minus one. This survives direct sums over copies. The final weighted V bound and target bound sum to (16) on all of H.

**Confusing a zero kernel with exclusion of zero from the spectrum.** The paper proves a uniform lower bound, then uses the adjoint and closed-range argument to obtain resolvents outside the claimed interval (p. 5). The same bound applies to the relevant adjoint operators. This addresses surjectivity as well as injectivity. The spectral claim therefore does not rest solely on the kernel computation.

These checks support the stated recommendation. They are a referee's examination of the written argument, not an independent construction of another proof.

## Exact bibliography and citation checks

The two entries and all citation occurrences were checked on 14 October 2026 against the precise public versions cited. The authoritative records used were the [versioned AIM file](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/643-low-degree-simplicial-zero-spectrum.md), the [arXiv v1 record](https://arxiv.org/abs/1412.5406v1), and its [original PDF](https://arxiv.org/pdf/1412.5406v1). No later title or theorem numbering was substituted for the cited preprint.

The identity ledger below separates ten asserted fields. A URL is counted as one complete field; its version, owner, and path were checked rather than merely tested for reachability.

| Entry and source location | Field as printed | Authoritative comparison | Result |
|---|---|---|---|
| [1], p. 6; `manuscript.tex:361` | MColbrook/AIM problem repository | Versioned repository owner and name are MColbrook/AIM. | Match |
| [1]; `manuscript.tex:362–363` | *643. Zero in the upper-Laplacian spectrum of low-degree simplicial complexes* | Exact words and order match the versioned file heading. | Match |
| [1]; `manuscript.tex:363` | Revision `a153f469` | Correct eight-character abbreviation of the full revision in the link. | Match |
| [1]; `manuscript.tex:364` | Complete GitHub URL | Resolves to the stated file at `a153f469ee0ea64e876b2ad97c79d252c19a3e22`. | Match |
| [2], p. 6; `manuscript.tex:366` | R. Rosenthal | The v1 record and title page identify Ron Rosenthal; the initial is accurate. | Match |
| [2]; `manuscript.tex:367` | *Simplicial branching random walks and their applications* | Exact title words and order match v1. | Match |
| [2]; `manuscript.tex:368` | arXiv identifier 1412.5406 | Identifies the cited work. | Match |
| [2]; `manuscript.tex:368` | Version v1 | The record and original PDF identify the first version. | Match |
| [2]; `manuscript.tex:368` | 2014 | The recorded v1 submission date is 17 December 2014. | Match |
| [2]; `manuscript.tex:369` | Complete versioned arXiv URL | Identifies the same work and v1. | Match |

Presentation normalization was limited to joining line breaks and replacing the verified author's first name by its printed initial. No substantive title words, author order, dates, or versions were changed. Neither entry asserts journal volume, issue, page, DOI, or edition fields requiring further comparison.

There are **two bibliography entries, ten identity fields, two citation occurrences, and two citation-to-source links**. The two occurrences contain four content assertions checked below. All ten fields and all four assertions matched; there were zero mismatches, zero unverified identity or cited-content items, and no excluded entries or uses.

| Manuscript use | Claimed content | Exact source location and content check | Result |
|---|---|---|---|
| p. 1; `manuscript.tex:37–42`, [2] | Relation to expected signed particle counts | V1 p. 3 defines the signed expectation; Lemma 3.2 on p. 11 gives its operator evolution. Section 2, Example 2.7(2) and (2.5), p. 7, supplies the matching weights and normalization. | Match |
| Same occurrence, [2, Theorem 1.1] | Spectral measure for regular arboreal complexes | The theorem is present on pp. 3–4 for A₀ = I − Δ⁺ on that class. | Match |
| Same occurrence, [2, Conjecture 4.3] | A proposed endpoint eigenvalue for general low degree | The numbered conjecture is present on p. 20 with the codimension-one degree bound at most d. | Match |
| p. 1; `manuscript.tex:44–61`, [1] | Precise two-assertion problem and operator domain | The versioned problem statement, lines 9–35, agrees on the spaces, usual coboundary, degree bounds, full-space spectrum, and permission for infinite lower incidence. | Match |

The spectrum implication for d = D = 3 is the manuscript's own deduction. It is not being attributed verbatim to either source. I did not audit the entire proof of Rosenthal's spectral-measure theorem, on which the new construction does not depend.

## Presentation, scope, and limits

The abstract, main theorem, construction, estimates, and concluding spectral argument describe the same object and Hilbert-space realization. The abstract states both the advance and the infinite-incidence feature. For readers familiar with simplicial cochains and bounded Hilbert-space operators, the notation is introduced in a usable order: E and V encode the face partition, the filling identity leads to the target estimate, and e and g are locally recalled before the final argument. I found no missing prerequisite or cross-reference that changed the interpretation of the proof.

All six supplied PDF pages were read and visually inspected. The equations, theorem and lemma labels, bibliography, and disclosure are legible; I found no clipping, overlap, or visible undefined reference. The source and supplied PDF agreed in the examined mathematical content. I did not regenerate the PDF or inspect a compiler log, so this report makes no claim about a reproducible source build.

The review covered the whole submitted note and both of its references. Public-source reading was limited to those cited works, with the relevant definitions and passages; it was not an exhaustive search for later or uncited results. No broader priority claim, journal fit, human-referee agreement, authorship inference, or formal result is established by this report. Numerical code and experiments are not part of the paper's evidence. No unresolved mathematical or citation objection was identified within this boundary, and no revision request is required by this round.
