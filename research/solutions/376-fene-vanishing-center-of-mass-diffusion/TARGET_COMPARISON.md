# Correspondence with AIM problem 376

Original statement: [The zero center-of-mass diffusion limit for kinetic FENE fluids](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/376-fene-vanishing-center-of-mass-diffusion.md), revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

Submitted manuscript: *Vanishing center-of-mass diffusion for the three-dimensional FENE dumbbell model*, Kaiwen Jin. Theorem 1.1 is the full-target claim. The locators below refer to the submitted manuscript and its public references.

| Original requirement | Manuscript location and claimed conclusion |
| --- | --- |
| Every nu > 0 and k > 2 on T^3 × B_1(0), with U(q) = −k log(1 − ‖q‖²) and normalized Maxwellian M | Section 1 fixes exactly these parameters, domain, and potential; Theorem 1.1 retains every such parameter. |
| Arbitrary prescribed smooth divergence-free initial velocity | Theorem 1.1 has no size restriction. Section 2.1 handles a nonzero conserved mean by a Galilean translation. |
| Smooth g_0 bounded above and below by positive constants, with configuration mass one | Theorem 1.1 uses this class, including smoothness on the open configuration ball without an extra boundary-derivative hypothesis. Sections 3.1–3.3 retain its trace. |
| Global finite-entropy solutions for positive diffusion | Section 2.1 adapts the fixed-positive-diffusion construction to periodic spatial form spaces and retains the usual initial-time coupled entropy inequality. |
| One subsequence tending to zero, giving a global weak solution of the identical zero-diffusion system | Sections 3–7 close the density correlation for the actual positive-diffusion family. Section 8 passes the full equations and diagonalizes over integer time intervals. |
| Strong L^2 velocity convergence on finite intervals | Section 2.2 proves finite-mode velocity compactness; Theorem 1.1 records the convergence. |
| Weak L^1 polymer-density convergence | Section 8 proves the stronger conclusion of strong L^1 density convergence. |
| Stress converges to the stress computed from the limiting density | Sections 2.2 and 8 use the uniform Hardy boundary tail and strong density convergence to obtain strong L^1 stress convergence. |
| Spatial transport has no extra defect | Sections 2.2 and 8 pass u_n psi_n by normalization, strong velocity convergence, and truncation. |
| Full configuration drag has no extra defect | Sections 5–7 identify and eliminate the relevant density covariance; Section 8 pairs strongly converging bounded configuration moments with weak L^2 velocity gradients. No corotational replacement is made. |
| Configuration diffusion and zero boundary flux | Sections 6.3 and 8 control configuration collars and pass the square-root diffusion product in the variational identity for tests on the closed ball. |
| Same initial data and usual kinetic-fluid entropy inequality | Section 8 passes the initial terms, gives weak time representatives and a strong initial density trace, and applies lower semicontinuity to the initial-time entropy inequality. |

The manuscript additionally claims strong L^1 density and stress convergence. It does not assume or claim strong convergence of the entire velocity gradient. The nonnegative Stokes defect in Section 5 controls stress-driven gradient oscillation, not the full viscous dissipation defect. An inequality starting at almost every positive time is stated only if that property is inherited from the selected positive-diffusion family; the usual inequality from the prescribed initial time is unconditional.

This is a complete analytic solution claim submitted for independent review. It is not a statement of upstream acceptance or formal verification.
