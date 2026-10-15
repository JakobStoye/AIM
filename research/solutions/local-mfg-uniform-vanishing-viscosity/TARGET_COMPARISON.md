# Target comparison for Problem 404

Target: [Uniform convergence of value functions in local mean-field games](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/404-local-mfg-uniform-vanishing-viscosity.md), fixed revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`. Manuscript: [Uniform vanishing-viscosity convergence for a local quadratic mean field game](paper/main.pdf), Theorem 1.1.

This comparison is between the displayed original problem and the completed manuscript.

| Original requirement | Manuscript location and conclusion | Scope |
| --- | --- | --- |
| Flat torus in every dimension `1 <= d <= 3` | Introduction, pp. 1-2; Theorem 1.1 on the volume-one torus `R^d/Z^d` | Same normalized periodic setting; all three dimensions |
| Every fixed `T > 0` | Theorem 1.1, p. 2 | Same; no small-horizon restriction |
| Smooth nonnegative probability initial density `m_in` | Theorem 1.1 uses `m_0`, with integral one and values in `[0,infinity)` | Same data, renamed `m_0` |
| Vacuum allowed; no strictly positive initial lower bound | Theorem 1.1 and pp. 1-2; density-gradient argument pp. 3-4, action convention p. 6, vacuum comparison pp. 10-11 | Same; auxiliary smoothed positivity on p. 9 is not an initial-data assumption |
| Smooth fixed terminal cost `g` | Equations (1.2), Theorem 1.1, uniform terminal trace (2.14) | Same |
| `-u_t - nu Delta u + |Du|^2/2 = m` and `m_t - nu Delta m - div(m Du) = 0` | Equation (1.1), with drift `-Du` and noise coefficient `sqrt(2 nu)` | Same signs, Hamiltonian, coupling and diffusion normalization |
| `m_nu(0)=m_in`, `u_nu(T)=g` | Equation (1.2); recovery (3.8) preserves the initial marginal exactly | Same endpoints |
| A single continuous `u` on `(0,T) x T^d` | Theorem 1.1; compactness after Proposition 2.1, p. 6; uniqueness in Section 4 | Same conclusion |
| Uniform convergence on every `[tau,T-tau] x T^d`, for every `0 < tau < T/2` | Equation (1.3), Theorem 1.1; concluding proof p. 11 | Same topology and every interior slab |
| Entire positive-viscosity family as `nu` decreases to zero | Last sentence of Theorem 1.1 and its concluding proof | Same; the result is not limited to one selected sequence |
| Constants in supporting estimates may depend on the fixed data | Section 2, p. 2: dependence on `d,T,m_0,g`, and on `tau` for `C_tau`; no dependence on `nu` | All limits hold for each prescribed data set and horizon |

The manuscript claims the full displayed Problem 404 conclusion. It answers the convergence portion of Tang-Zhang's broader question only for the quadratic Hamiltonian, linear local coupling, fixed terminal cost and dimensions at most three. No result for other Hamiltonians/couplings, higher dimensions or a convergence rate is claimed.

The public analytic dependencies are identified in the manuscript's eight-entry bibliography. Fixed-viscosity existence uses Cardaliaguet-Lasry-Lions-Porretta, Theorem 4.1 and its regularity conclusion, after the explicit rescaling on p. 2. The control formula uses Lawler, Theorem 3.7.1. The torus interpolation bridge uses Nirenberg, Lecture II (2.2)-(2.3), pp. 125-126, with the cutoff/absorption argument supplied on pp. 3-4. Weak extraction and convolution use Folland, second edition, Theorem 6.15 p. 190 and Theorem 8.14 pp. 242-243. Path-law compactness uses Anderson-Guionnet-Zeitouni, Appendix C, Theorems C.9/C.12 p. 430 of the linked author manuscript. Cardaliaguet's Section 4.3 and proof of Theorem 4.2 are credited for path/calibration/comparison ideas; the required specialization is proved in Sections 3-4 of this manuscript.

This is a submitted analytic proof claim for independent mathematical review. Maintainer classification and mathematical acceptance are separate from the package's document checks.
