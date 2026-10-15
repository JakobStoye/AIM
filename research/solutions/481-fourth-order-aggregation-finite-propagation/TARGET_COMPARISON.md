# Comparison with the original AIM 481 target

Source: [original problem at the fixed repository revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/481-fourth-order-aggregation-finite-propagation.md). The submitted result is Theorem 1.1 of the [finished manuscript](paper/main.pdf), with proof in Sections 2–4 and Appendix A.

| Original requirement | Submitted statement and argument |
| --- | --- |
| Every integer $`d\ge2`$ and every $`\chi>0`$ | Theorem 1.1 has exactly these ranges. The small entropy exponent depends on $`d`$ and remains strictly within the finite-exponent Sobolev range. |
| Every compactly supported, nonnegative $`\rho_0\in H^1(\mathbb R^d)`$ with mass one | Exactly the datum class in Theorem 1.1. Positive floors and smoothness occur only in an auxiliary construction and are removed. |
| A nonnegative global, narrowly continuous probability-valued curve with finite second moment and the prescribed initial value | Theorem 1.1 and the original minimizing movement construction in Section 2.1. A common global subsequence is retained. |
| $`L^\infty(0,T;H^1)\cap L^2(0,T;H^2)`$ on every finite horizon | Stated in Theorem 1.1; the construction bounds are displayed in (2.3)–(2.4). |
| The exact weak identity for every compact $`C^2`$ test and every pair of time endpoints | Equation (1.2), with the same sign, coefficient $`\chi`$ and three integrands as the problem. |
| One finite radius for almost every point of the entire spacetime interval $`(0,T)`$ | Theorem 1.1; the local entropy bound (4.1) and the superlinear tail recurrence (4.8) force the exterior spacetime tail to be zero beyond a finite radius. |
| The same curve for all finite horizons | The fixed countable cutoff family and integer-horizon argument at the end of Section 4. |

The equation is

```math
\partial_t\rho=-\nabla\cdot(\rho\nabla\Delta\rho)-\chi\Delta(\rho^2).
```

For every $`\phi\in C_c^2(\mathbb R^d)`$ and $`0\le a<b`$, the submitted identity is

```math
\int\phi[\rho(b)-\rho(a)]
=-\int_a^b\!\int\bigl(\rho\Delta\rho\Delta\phi+\Delta\rho\nabla\rho\cdot\nabla\phi+\chi\rho^2\Delta\phi\bigr)\,dx\,dt.
```

The comparison uses the problem's explicit Sobolev requirements. Definition 2.1(i) of the pinned CEFF preprint also writes a spatial infinity endpoint in dimension two. The manuscript distinguishes that extra wording and uses the common $`H^1/H^2`$ estimates and their finite-exponent consequences; no spatial infinity endpoint is claimed. This omits no clause of the AIM statement above.

The submission does not assert weak uniqueness, a quantitative radius law, or a conclusion for every possible weak solution. It presents a full-target solution claim for independent mathematical review. AI assistance and the actual review limits are disclosed in [AI_USE.md](AI_USE.md); no human, Lean, novelty or repository-acceptance certificate is asserted.
