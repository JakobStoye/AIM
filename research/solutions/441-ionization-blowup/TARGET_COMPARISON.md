# Comparison with AIM 441

Target: [the immutable problem statement at revision a153f469ee0ea64e876b2ad97c79d252c19a3e22](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/441-ionization-laser-envelope-global-regularity.md).

The question is universal over all its allowed coefficients and Schwartz initial pairs. The note claims its negation through the single admissible witness in Theorem 1.1.

| Original requirement | Result and location in the note | Relation |
| --- | --- | --- |
| Space is R^3 with an elliptic Laplacian in all three coordinates | Original system (1.1), Sections 2-4 | Same domain and operator |
| Positive epsilon, c, c_g and alpha_4; alpha_5 nonnegative; integer K at least 2 | Theorem 1.1 selects epsilon=c=c_g=1, alpha_4=delta>0, alpha_5=0, K=2 | One admissible parameter tuple suffices for a counterexample |
| Every Schwartz initial pair with nonnegative density | Section 4.2 constructs nonzero u_0 in C_c^infinity and rho_0=0 | The constructed pair lies in the required class |
| The actual coupled system, including the density equation and optical transport | Sections 3.3 and 4.3 retain the exact moving-frame density translation and reconstruct the physical equations | No uncoupled substitution |
| Local smooth solution with all H^m regularities, m at least 3 | Sections 4.3-4.4 prove physical H^1 uniqueness, recover L^2, and show smooth persistence for every fixed m before T | Same Cauchy solution and solution class |
| Nonnegative electron density | Formula (4.11) gives rho(t,x)=delta integral_0^t abs(u)^4 | Preserved throughout the smooth lifespan |
| Continuation for all nonnegative times | Formula (4.13) proves finite-time divergence of the L^2 gradient norm | Rules out global C_t H^3 continuation and hence the stated universal conclusion |

The imported scalar inverse and linear estimates are identified with their precise versioned sources in Sections 2.1 and 3.1. Their hypotheses are verified in Section 2.4. The new coupling arguments are proved in the note. Appendix A and the exact-arithmetic supplement cover only the stated finite coefficient inequalities. No failure for every parameter, explicit full Cauchy threshold, open-set stability, formal verification or external acceptance is claimed.
