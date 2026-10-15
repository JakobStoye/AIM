# Target comparison for AIM 424

Original problem: [Reality of the spectrum for a spherical strip with PT-symmetric boundary conditions](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/424-spherical-pt-robin-real-spectrum.md), revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

The manuscript's equations (1)--(2) define exactly the original operator and domain. Theorem 1.1 gives an affirmative answer for every triple in the original question.

| Original requirement | Manuscript location | Coverage |
|---|---|---|
| Every real half-width `0 < a < pi/2` | Introduction; Theorem 1.1 | The interval is fixed arbitrarily throughout; neither excluded endpoint is added. |
| Every real `alpha` | Theorem 1.1; Section 3.3 | The exact boundary determinant is nonzero at every nonreal spectral parameter for every real alpha. |
| Every integer `m` | Propositions 2.3--2.4 | Nonzero integer modes use the positive Fourier comparison; the zero mode uses the first-order factorization. The potential depends on m squared, so both signs are included. |
| Original potential | Introduction before equation (1) | Both the original fraction and its identical secant-squared expression are displayed. |
| Complex Lebesgue `L2(-a,a)` and exact `H2` domain | Introduction, equations (1)--(2) | Both endpoint derivatives are coordinate derivatives, with the original opposite real Robin signs. |
| All spectral indices | Section 2; Lemmas 3.1--3.2 | Strict Robin/Dirichlet interlacing and the canonical products are proved analytically for the full spectra. |
| Entire spectrum contained in the real line | Theorem 1.1; final proof in Section 3.3 | Every nonreal parameter has a unique bounded `L2`-to-`H2` inverse; the realization is dense and closed. |

The argument does not replace the spherical potential by the comparison operator. It retains the exact curvature term and endpoint coefficients. The theorem concerns each separated operator; it makes no parameter-uniform resolvent or singular-endpoint claim.

The problem note's equation (2) and Krejcirik--Siegl's Section 4.4.2 identify the same family. Their zero-potential and sufficiently-large-real-part results are credited in the Introduction. The new manuscript supplies the all-index comparison and the remaining low-spectrum argument; it does not infer priority from a literature search.

The package is a complete solution claim offered for independent mathematical review. Its proof is analytic, with no numerical or formal-verification premise.
