# Correspondence with AIM problem 300

Compared statement: [Interior smoothness of carrying simplices in competitive population maps](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/300-carrying-simplex-interior.md), revision `c9929805cece044705abaaebe1cebddac1ba11a6`.
Submitted argument: [Interior smoothness of carrying simplices for competitive population maps](paper/interior_smoothness.pdf), Kaiwen Jin, October 12, 2026; [editable source](paper/interior_smoothness.tex).

## Hypotheses and conclusion

| Original requirement | Manuscript location and treatment |
| --- | --- |
| Every integer d >= 3; C = [0,infinity)^d | Theorem 1, pp. 1-2. The proof fixes an arbitrary admissible map and dimension. |
| F_i(x) = x_i f_i(x); f is C1 on an open neighborhood of C | Theorem 1. This is the map used throughout Section 2. |
| f_i > 0 and every partial derivative partial_j f_i < 0 on all of C | Theorem 1, all i,j. Positivity preserves coordinate support; the strict derivative signs yield the positive matrix K in (6). |
| Positive axial fixed point q_i e_i on each axis | Theorem 1. Section 2.1 uses attraction and closedness to put these points on the simplex, then unorderedness gives Sigma subset [0,q] in (3). |
| rho(M(x)) < 1 on the entire closed box, M_ij = -x_i partial_j f_i/f_i | Theorem 1, (2). Section 2.1 proves that N = K diag(x) has the same characteristic polynomial, including at extinction faces, and constructs the continuous inverse A on that entire box. |
| The guaranteed compact, invariant, unordered carrying simplex, disjoint from zero, with continuous positive radial representation | Section 1, (1), and Section 2.1. Existence is inherited; the proof establishes regularity of this object. Compactness gives a positive minimum total population in (3). |
| The entire Sigma intersection (0,infinity)^d is a C1 embedded (d-1)-manifold | Theorem 1. Section 2.4 proves Frechet differentiability with continuous derivative, then the graph embedding and the exponential diffeomorphism give the conclusion. No restriction to fixed points or selected trajectories is made. |
| R is C1 on relative interior Delta | Theorem 1 and (21), p. 6, express R through the C1 logarithmic graph and positive logarithmic coordinates. |
| Only interior regularity; no boundary smoothness or transverse embedding assumed | Paragraph after Theorem 1 and Section 2.2. Auxiliary continuous matrix fields at boundary points are used solely for uniform estimates. |

The manuscript introduces no convexity, permanence, C2 regularity, boundary transversality, or uniform lower bound on each individual population.

## Imported results and additional argument

Baigent's *Carrying Simplices for Competitive Maps* supplies the existence framework (Theorem 1, author-manuscript p. 9), the homeomorphism onto the box image under AS3-AS4 (Lemma 16(1), p. 18), and the nonnegative inverse expansion in the proof of Lemma 15 (p. 18). [Author manuscript](https://homepages.ucl.ac.uk/~ucess29/resources/ICDEA_RPS.pdf); [published chapter](https://doi.org/10.1007/978-3-030-20016-9_1). The source's attraction property suffices for axial membership; the proof does not require a stronger source theorem about asymptotic completeness.

The added argument appears in Sections 2.2-2.4. The form A(x) = I + B(x) diag(x), with B uniformly positive and bounded, produces a common row mass bounded below by the minimum total population. This gives uniform contraction even along orbits approaching extinction faces. The two normalizations yield a continuous covector and eventual strict sign for every direction outside its kernel. Finite local inverse iterates transport contingent directions, and unorderedness excludes that strict sign. The resulting kernel constraint makes the globally Lipschitz logarithmic graph C1.

The other cited papers provide local fixed-point results, a convexity-dependent smoothness theorem, and prior use of logarithmic carrying simplices. They are credited for those precise scopes. The complete interior proof is contained in the submitted paper and its public dependencies.

## Evidence status

This is an analytic complete solution claim supported by the manuscript. Codex assistance is disclosed there. Fresh-context AI feedback and successful LaTeX compilation do not constitute human, formal, or upstream mathematical certification. Independent mathematical review is requested.
