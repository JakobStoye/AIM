# Comparison with AIM 380

Target: [immutable problem statement](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/380-strong-kpp-critical-extinction.md), revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

Submitted argument: [manuscript](paper/main.pdf), Theorem 1.1, Lemmas 2.1 and 3.1, and the final proof in Section 3.

The original assertion is universal over the allowed dimensions, domains and reactions. An admissible example with a positive bounded classical solution at equality is therefore a counterexample to the full assertion.

| Original requirement | Submitted witness and proof location |
| --- | --- |
| Dimension `d >= 2` | `d = 21`, Section 1, equation (3). No assertion for every dimension is needed to refute the universal implication. |
| Connected unbounded domain | Region between `z = +/- arccos(-50/(1000+|x|^2))`, Lemma 2.1. It contains the entire midplane and the straight width-pi slab. |
| Uniform `C^{2,gamma}` boundary charts | All graph derivatives are bounded, the graphs are separated, and common radius `1/4` charts have uniform bounds; Lemma 2.1. This holds for every fixed `0 < gamma <= 1`. |
| `f` in `C^{1,gamma}([0,infinity))` | Equation (4): `f(s)=s-s^2` on `[0,1]`, `f(s)=1/s-1` on `[1,infinity)`. Matching first derivatives and bounded globally Lipschitz derivative; Theorem 1.1 and its proof. |
| Zeros at 0 and 1, positive derivative at 0, prescribed signs | The same equation has `f'(0)=1`, is positive between 0 and 1 and negative above 1. |
| Strictly decreasing `f(s)/s` on `(0,1]` | Quotient `1-s` on that interval. |
| Compact-test spectral equality `lambda_1(Omega)=f'(0)` | Lemma 2.1 proves the lower bound with horizontal Hardy energy and sliced interval energy, and the upper bound with explicit compact tests in the contained slab. Both give 1. |
| Bounded positive classical solution | Lemma 3.1 gives a positive strict subsolution `v`; the final proof produces `U` with `v <= U <= 1`, interior `C^2` regularity and `-Delta U=f(U)`. |
| Pointwise zero Dirichlet values | The uniform comparison function in the last paragraph gives continuous extension by zero at every boundary point. Thus `U` lies in `C^2(Omega)` intersected with `C(closure(Omega))`. |
| No periodicity or geometric convergence assumption required | None is used as an extra hypothesis on the source target. The witness itself is explicitly defined globally. |

The violated conclusion is nonexistence of a bounded positive classical equilibrium. The construction does not establish uniqueness, an optimal dimension, a full dimension classification, or a dynamical theorem for arbitrary initial data. The manuscript credits the related Hardy-potential and nonuniform-domain constructions of Rossi and Tough and the critical question of Berestycki and Graham; no priority certificate is claimed.

This comparison is a reading map, not an independent proof audit. The complete mathematical argument is in the manuscript.
