# Target comparison for AIM 402

Original statement: [Logarithmic convexity for two coupled subdiffusion orders](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/402-mixed-order-fractional-logarithmic-convexity.md), revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

Proposed resolution: Theorem 1 of [the manuscript](manuscript.pdf). The claim covers the complete original target. It is submitted for independent mathematical review.

| Original requirement | Manuscript result and location | Scope |
|---|---|---|
| Every bounded smooth domain in any spatial dimension | Section 1 and Theorem 1; the proof uses the positive discrete Dirichlet spectrum. | Same |
| Homogeneous Dirichlet conditions | Section 1 and the spatial eigenbasis in the proof of Theorem 1. | Same |
| The two original equations, including all diagonal and off-diagonal reactions | Equation (1); Section 2 sets `q=lambda-1`, giving the exact modal matrix. | Identical |
| Every `0<alpha1<alpha2<1` and every `T>0` | Theorem 1; the proof writes `a=alpha1`, `b=alpha2`. | Same |
| Caputo initial-value convention | Section 1 defines the derivative and the mild formulation; the transform (4) retains both different initial-value factors. | Same |
| Every product-L2 initial pair and every mild solution | Theorem 1 and its final proof; spectral projection identifies every mode, and the infinite sequence estimate retains arbitrary signed or complex mixtures. | Same; real data included |
| The product-L2 norm | Definition in Section 1; Parseval and Holder in the final proof use the sum of squared component norms. | Identical |
| All `0<t<T`, with exponents `1-t/T` and `t/T` | Equation (2), the modal interpolation estimate, and the final proof. | Identical |
| One finite constant depending only on the domain, orders and final time | Lemma 4 gives estimates uniform over every real `q>=2`; the final proof combines these with finitely many lower modes. | Same |
| No implicit exclusion of growing or critical modes | Proposition 3 includes `-1<q<1` and separately `q=1`, corresponding to the possible eigenvalue `lambda=2`. | Complete |
| Unbounded frequencies and arbitrary infinite superpositions | Uniform Lemma 4 and the infinite Holder sum in the proof of Theorem 1. | Complete analytic argument |
| Imported public results | Li--Huang--Liu, Definition 1 and Theorem 1, supply the mixed-order mild framework; all two-dimensional invertibility and frequency-uniform estimates are proved in the manuscript. | Specified source hypotheses specialize to the given Laplacian and constant reaction |

Chorfi's 2025 Section 5, problem 1 asks for similar logarithmic convexity results for these equations. The manuscript states and proves the precise homogeneous-Dirichlet product-L2 formulation recorded by AIM 402. The common-order result of Chorfi--Maniar--Yamamoto and the common-order coupled framework of Feng--Liu--Lu are credited as benchmarks, rather than asserted to prove the different-order system directly.

The submission makes no claim that the multiplicative constant is one or optimal, or that this proof covers general nonsymmetric or spatially varying coupling. Those statements are not part of the original target.
