# Target comparison: AIM 482

Target: [Unconditional uniqueness for entropy-dissipating reaction-diffusion](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/482-entropy-reaction-diffusion-renormalized-uniqueness.md),
repository revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

The manuscript gives a negative answer by one admissible instance. On the
unit ball in R3, with two species and both diffusivities equal to one, take

```math
 f(a,b)=(-b^2(a-b),b^2(a-b)),\qquad
 (a_0,b_0)=(10000/|x|,0).
```

| Target requirement | Witness and manuscript location |
|---|---|
| Smooth bounded domain, d>=2; N>=2; positive diffusivities | Unit ball in R3, N=2, diffusivities 1; Section 1 / Theorem 1.2 |
| Locally Lipschitz reaction and quasi-positivity on missing-species faces | Polynomial reaction; f_1(0,b)=b^3>=0 and f_2(a,0)=0; Section 1 |
| Entropy sign for every positive state, with one fixed mu | mu=(0,0); -b^2(a-b)(log a-log b)<=0; equation (3) |
| No additional growth assumption | The cubic polynomial is an allowed member of the stated class |
| Nonnegative finite L1 log L initial vector | (C/|x|,0) in dimension 3, C=10000; Theorem 1.2 and its proof |
| Two global solutions with identical initial data | (m,0) and (m-b,b); Sections 2-3 prove global construction and the strong L1 initial trace |
| L^infinity_t L1_x and sqrt(u_i) in L2_t H1_x for every finite T | Conserved scalar heat total and regularized entropy estimate; Section 4 |
| Exact compact-gradient renormalizations, every smooth space-time test, initial term and Neumann condition | Definition 1.1 reproduces this class; the final proof passes all test identities from positive time to zero |
| Failure of equality almost everywhere without a strong comparison solution | The positive lower bound in Theorem 1.2 holds on a positive-measure space-time set; the initial fuel is unbounded |

The explicit subsolution is used until time 1/4 to witness nonzero difference;
both solutions exist for every positive time. The construction uses the
unbounded initial-data class allowed by the target. It does not make a
nonuniqueness claim for bounded initial concentrations.

This is a complete counterexample claim submitted for independent review.
Catalogue classification and acceptance are left to the maintainers.
