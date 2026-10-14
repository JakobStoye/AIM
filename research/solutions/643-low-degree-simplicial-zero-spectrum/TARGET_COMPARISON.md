# Comparison with AIM Problem 643

Target: [Zero in the upper-Laplacian spectrum of low-degree simplicial complexes](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/643-low-degree-simplicial-zero-spectrum.md), revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

Submitted result: Theorem 1 of [the manuscript](paper/degree_three_counterexample.pdf). The contribution is a complete analytic counterexample claim to each of the two universal assertions.

| Original requirement | Result and manuscript location | Scope |
| --- | --- | --- |
| Nonempty pure simplicial complex, dimension at least two, possibly infinite | Theorem 1 and Section 2 construct a countable nonempty pure complex of dimension three by taking the downward closure of explicit tetrahedra. | An admissible infinite object; no cell-complex surrogate. |
| Only codimension-one degree is bounded | Lemma 2 proves that one triangle has degree one and every other triangle degree three, so the maximum is three. Every edge has infinitely many triangle cofaces. | No finite-incidence hypothesis on lower faces is introduced. |
| Full triangle cochain space with weights equal to actual degrees; tetrahedron cochains use counting measure | Section 1 defines the prescribed spaces; equation (5) gives the complete triangle partition and equation (7) the weighted adjoint. | Exactly the full space, without projection or a cohomological restriction. |
| Usual alternating coboundary and its normalized upper Laplacian | Sections 1 and 3 define the operator and prove its bounded extension and adjoint. | Same operator and normalization as the target. |
| First assertion: maximum degree at most dimension plus one implies zero in the spectrum | Here three is at most four; Theorem 1 and the final resolvent argument give spectrum contained in `[1/C,4]`, with `C>0`. | Zero is absent from the full spectrum; first assertion disproved. |
| Second assertion: maximum degree at most dimension implies a nonzero square-summable kernel | Here three is at most three; Theorem 1 gives zero kernel. | Second assertion disproved separately by the same example. |
| Quantifiers and uniformity | Sections 3-4 prove the filling limit, orthogonal estimates and tree gradient bound with a single explicit constant valid for every cochain. | One admissible dimension-three counterexample negates each universal all-dimensions statement. |
| Complete public proof and dependencies | The finite boundary expansions, strong adjoint limit, complete coordinate estimate and Hilbert-space resolvent criterion are proved in the manuscript. | No proof-critical computation or privately supplied theorem is required. |
| Literature credit | Section 1 cites Rosenthal, arXiv:1412.5406v1, Theorem 1.1 and Conjecture 4.3, for motivation and the source question. | Background citation; not an imported premise. No novelty or priority certification is asserted. |

The manuscript does not claim counterexamples in every dimension or in a class with finite lower-face incidence. Those additional conclusions are unnecessary to refute the two assertions as stated.

The accompanying AI review describes its exact manuscript version and source checks. An AI review and a successful artifact build are distinct from human verification or acceptance by the repository.
