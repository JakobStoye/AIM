# Comparison with AIM problem 396

Target: [Polynomial decay for KdV with three critical linear modes](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/396-critical-kdv-odd-mode-polynomial-decay.md), revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

The submitted manuscript, *Polynomial decay for the Korteweg–de Vries equation at length 14π*, claims the full target with exponent 1/2.

| Original requirement | Manuscript location and result | Coverage |
|---|---|---|
| Exact real equation y_t+y_x+y_xxx+y y_x=0 on (0,L), L=14π | Equation (1.1), Theorem 1.1 | Identical equation, normalization, scalar field and interval |
| y(t,0)=y(t,L)=y_x(t,L)=0 | Equation (1.1), generator domain (2.1), energy identities (2.4) and (4.1) | Identical boundary realization, with hidden traces for energy solutions |
| Usual energy class C([0,∞);L²)∩L²_loc([0,∞);H¹₀) | Definition preceding Theorem 1.1; Sections 2.1 and 4 | Same class; the mild realization and its public well-posedness sources are stated explicitly |
| Every real datum in one sufficiently small L² ball | Theorem 1.1; Proposition 4.1 | No sign, phase, initial-subspace or additional Sobolev restriction |
| Common δ,C,α>0 before the datum and time quantifiers | Proposition 4.1 chooses fixed times, constants and one δ; closing proof of Theorem 1.1 chooses C | Uniform in every permitted datum; α=1/2 |
| Every t≥0, including zero and intermediate times | Closing proof of Theorem 1.1 | Reciprocal-energy iteration, monotonicity and the initial bounded interval give the bound for all times |
| Three undamped modes and all their mixtures | Lemma 2.1, Proposition 3.2, the exhaustive split in Proposition 4.1 | Stationary mode, conjugate oscillatory pair, every phase and every stable/center mixture |

The complete original decay question follows by choosing the positive exponent α=1/2. The manuscript makes no claim for all critical lengths, large data or optimality of this exponent.

## Public mathematical dependencies

Rosier, Proposition 3.1, supplies the real linear contraction realization. Coron–Crépeau, Proposition 7 and Appendix A, supplies the linear mild maps and usual solution realization. Niu–Xiang, arXiv:2501.13640v2, Lemma 3.2, supplies small-data global existence and uniqueness. Standard one-dimensional Sobolev facts are cited to Brezis. The stable-complement estimate, exact mode classification, quadratic coefficients, whole-center lower bound, rough-data remainder, energy loss and all-time iteration are proved in the manuscript.

Nguyen's fixed-window decay argument is the methodological source. Its mixed-frequency limitation is addressed here by retaining the center forcing through Duhamel's formula and choosing only the stable response periodically. Niu–Xiang's near-critical-length theorem is cited for context, with its exclusion of the exact critical length preserved.
