# Comparison with Problem 463

Target: [Calderón–Zygmund estimates for general concave nonlocal equations](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/463-concave-nonlocal-calderon-zygmund.md), revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

The submitted result is an analytic counterexample to the proposed estimate over the general kernel class. The manuscript uses `sigma = 2s`. For every strict ellipticity pair `0 < lambda < Lambda` and every finite `p > max(2,n/sigma)`, Theorem 1.1 contradicts any proposed constant depending only on the stated parameters. Consequently no finite large-p threshold yields the asserted estimate for this general class. The equal-constant isotropic class is outside the negative assertion.

| Original requirement | Manuscript location | Comparison |
| --- | --- | --- |
| `n >= 2`, `0 < s < 1` | Introduction and Theorem 1.1; `sigma = 2s` | Every original dimension and order; the proof uses `n > sigma`, automatic here. |
| Any even measurable translation invariant kernels between the two power-law bounds | Equations (1.1), (2.2), (2.3), Section 2 | Exact pointwise bounds with the same fixed constants. Kernels depend only on the jump variable and can be smooth away from zero. Compact finite dimensional disk controls are allowed index sets. |
| Sign convention `I = inf_a(-L_a)` with positive `L_a` | Equation (1.2), Section 2 | Exact agreement, including the symmetric-integral factor. |
| Bounded viscosity solutions in the unit ball, smooth right side | Proposition 4.1 and following paragraph | The examples are globally smooth bounded classical solutions with smooth bounded right side. Positivity of kernels gives the viscosity touching inequalities. |
| Interior `W^(2s,p)` norm: Slobodeckij for noninteger order and ordinary Sobolev at order one | Introduction; Proposition 4.1; final proof in Section 5 | All three order regimes are handled in precisely those spaces. |
| Constant uniform over kernel families and depending on the right side only through its `Lp` norm | Theorem 1.1 and Proposition 4.1 | Kernel families vary along the construction while ellipticity constants stay fixed. The forcing tends to zero in `Lp`; its stronger norms are not bounded uniformly. |
| A finite threshold valid for every sufficiently large finite p | Theorem 1.1, Section 5 | Failure for every finite `p > max(2,n/(2s))` rules out each proposed finite threshold at strict ellipticity. No endpoint claim is made. |
| Full global supremum term on the right | Proposition 4.1 and concentrated potentials in Section 5 | Convergence and boundedness hold on the whole space, not just the interior domain. |

The proof is analytic. No numerical experiment, formal proof certificate, human review or upstream acceptance is claimed. The references in the introduction provide context and restricted comparisons; the construction and the Riesz-potential identity are proved in the manuscript.
