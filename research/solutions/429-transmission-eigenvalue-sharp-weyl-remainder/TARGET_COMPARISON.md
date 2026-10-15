# Comparison with AIM429

The target is [AIM429 at repository revision
a153f469ee0ea64e876b2ad97c79d252c19a3e22](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/429-transmission-eigenvalue-sharp-weyl-remainder.md).
The accompanying manuscript claims an affirmative resolution of its complete
stated target. Independent mathematical review is requested.

| Target requirement | Manuscript location and scope |
| --- | --- |
| All integer dimensions at least two | Theorem 1.1; the final dyadic sum uses exactly this lower bound |
| Every bounded connected domain with smooth boundary | Theorem 1.1 and Section 2; no convexity or connected-boundary condition |
| Every fixed constant refractive index greater than one | Theorem 1.1; constants may depend on the domain and index |
| Original transmission equations and equal Cauchy traces | Equations (1.1) and (1.2); the maximal distributional graph domain is retained |
| Algebraic multiplicity for the original closed operator | Equation (1.3), the realization comparison in Section 2, and the exact divisor identity in Section 3 |
| All nonzero complex energies in the closed modulus disk | Equation (1.3) and Section 5; an energy is counted once, including nonreal values |
| Sum of the two Dirichlet volume coefficients | Theorem 1.1: $`\omega_d(2\pi)^{-d}|\Omega|(1+n^{d/2})r^d`$ |
| Remainder of order radius to the power dimension minus one | Theorem 1.1 and the proof in Section 5 |
| Every sufficiently large exact radius, including spectral thresholds | The local multiplicity estimate in Section 4 and the annulus comparison in Section 5 remove the auxiliary contour shifts |

The energy variable is called `lambda` in the manuscript and `z` in the
problem page; the counting radius has the same meaning. The proof uses the
published Dirichlet-to-Neumann approximation and transmission index formula,
with the additional sector, logarithm and thin-strip estimates written out in
Sections 3 and 4. The radial example in Appendix A illustrates multiplicity
at common Dirichlet values and is not used to infer the arbitrary-domain
theorem.

The claim does not extend to variable indices, anisotropic principal parts,
or a remainder uniform as the index tends to one. These are outside the
stated target. No Lean or other kernel-checked proof is provided. The
manuscript's AI-use disclosure describes the assistance used; the package
does not assert independent human verification or upstream acceptance.
