# Target comparison for AIM 572

Original problem: [Counting Ehrhart quasipolynomials of half-integral polygons](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/572-half-integral-ehrhart-count.md).

The submission claims the full stated formula. The manuscript and all supplied verification files are provided for independent checking; no novelty or upstream acceptance is asserted.

| Original requirement | Manuscript coverage | Scope |
| --- | --- | --- |
| Every integer i >= 2 | Theorems 1.1 and 2.1; final proof in Section 7 | Same quantifier |
| Convex two-dimensional polygons with vertices in (1/2)Z^2 | Definition and normalization in Sections 1-2 | Integral polygons included |
| Exactly i interior lattice points and at least two boundary lattice points | Signature classification in Section 2 | No collinearity restriction |
| Count distinct entire functions on nonnegative integer dilates | Constituent formula (2.1), collapse criterion (2.2), injective signature correspondence | Period collapse counted once |
| E(i) = (9i^3+72i^2+175i+106)/2 | Theorem 1.1 and Section 7 | Claimed full target |
| Reproducible computational inputs | Section 6 and numerical_case/README.md | Exact certificate inputs and fixed source-set comparisons supplied |

The contribution combines analytic necessity and uniform polygon witnesses with exact rational inequality certificates. For i=2,...,16, it uses the complete published classification of Bohnert and Springer and the full-function dataset [version 1.0.0](https://doi.org/10.5281/zenodo.13928298). Five published minimum-width maxima are also imported. Catalogue completeness and those global maxima remain cited external dependencies; the companion does not independently reconstruct them. Finite code checks do not replace the all-parameter arguments.

The manuscript bibliography identifies eight sources and their versions. AI assistance is disclosed at its end. One AI manuscript referee review informed a revision of the reproduction instructions; that review is not independent mathematical certification or human review.

Use the root README for normal/optimized tests, certificate replay, optional pinned HDF5 dependencies and complete fixed-data retrieval/comparison. The matching 25-member companion archive is also included under its manuscript-cited filename.
