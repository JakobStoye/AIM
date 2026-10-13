# Target comparison for AIM 582

Target: [Full Sobolev invertibility range for Hausdorff-measure screen operators](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/582-fractal-screen-sobolev-invertibility.md), revision `c9929805cece044705abaaebe1cebddac1ba11a6`.

Submitted result: *Failure of Sobolev surjectivity for a screen with accumulating gaps*, Theorem 1.1. The target explicitly asks for a proof or disproof. One admissible counterexample suffices for its universal assertion.

| Original requirement | Result and location in the manuscript | Scope |
| --- | --- | --- |
| $n\in\{1,2\}$ and $n-1<d\le n$ | Section 1 uses $n=d=1$, hence $t_d=1/2$ | Admissible case for the disproof alternative |
| Nonempty compact $d$-set with two-sided Hausdorff bounds for all $x\in\Gamma$, $0<r\le1$ | Equation (1) gives the set; Lemma 1.2 proves bounds $r/16$ and $2r$ | All points and radii, including the accumulation point |
| Positive quotient traces, zero $L^2$ pivot and negative pivot duals | Section 1 definitions and equation (2); equation (15) lifts the charge using the original adjoint trace | Same spaces and compatible embeddings |
| Original Hausdorff Helmholtz integral and continuous extensions | Equation (3); Section 4 proves equation (20) by energy-space density approximation | Same outgoing kernel and original operator |
| Fixed arbitrary $k>0$ | Theorem 1.1 and its proof hold for every $k>0$; the charge and $\alpha$ are independent of $k$ | No limit $k=0$ and no uniform-in-$k$ constant asserted |
| Every $|t|<t_d$ | A nonempty subinterval $\alpha<t<1/2$ fails surjectivity | Enough to disprove the universally quantified interval |
| Bounded linear isomorphism | Boundedness is retained from Caetano et al., Proposition 4.7; energy injectivity and density nonmembership exclude every smoother preimage of the constructed data | Failure of surjectivity, rather than a redefinition of the operator |
| No self-similarity or separation hypothesis | The admissible compact 1-set in equation (1) has infinitely many gaps | No assumption absent from the original target is imposed |
| Full remaining target or permitted alternative | Theorem 1.1 disproves the all-screen statement through $n=d=1$ | The assertion restricted to $d<n$, an optimal threshold, and prescribed incident-wave data remain unaddressed |

## Imported public results

The manuscript gives exact references and supplies the supplementary geometric, measure and operator arguments in Sections 2–4.

| Source | Exact locator used | Applicability |
| --- | --- | --- |
| Caetano, Chandler-Wilde, Gibbs, Hewett and Moiola, *A Hausdorff-measure boundary element method for acoustic scattering by fractal screens*, Numerische Mathematik 156 (2024), 463–532, [DOI](https://doi.org/10.1007/s00211-024-01399-7); cited preprint [2212.06594v2](https://arxiv.org/abs/2212.06594v2) | Theorem 2.7 and Section 2.4 footnote 7; Lemma 4.3 and equations (45)–(46); Theorem 4.6; Proposition 4.7 | Trace/dual identification and compatibility, energy injectivity, literal integral representation and boundedness; apply with $n=d=1$ and the original strict exponent ranges |
| Chang, Wang and Wu, *On the spectral theory of positive operators and PDE applications*, DCDS 40(6) (2020), 3171–3200, [DOI](https://doi.org/10.3934/dcds.2020054) | Theorem 1.5, pp. 3174–3175 | Compact positive ideal-irreducible operator on the real Banach lattice $L^2(Q)$; Lemma 2.1 establishes those hypotheses |
| Rodriguez (lecturer), Lin (notes), *18.102: Introduction to Functional Analysis*, MIT, Spring 2021 | Theorems 180 and 184, pp. 90–93 | Hilbert orthogonal decomposition and Riesz representation for the gradient-norm space in Lemma 2.1 |
| Nonnenmacher, *Lecture Notes for the course Distributions and Partial Differential Equations*, Paris-Saclay, September 2022 | Proposition 1.9.11 and Remark 1.9.12, printed pp. 60–61 | A one-dimensional positive distribution is a locally finite measure; Lemma 3.1 separately proves the planar line-support reduction and finite mass |
| NIST DLMF, version 1.2.8, release 2026-09-15 | Equations [10.2.2](https://dlmf.nist.gov/10.2#E2), [10.4.3](https://dlmf.nist.gov/10.4#E3) and [10.8.2](https://dlmf.nist.gov/10.8#E2) | The actual $J_0$, $Y_0$, $H_0^{(1)}$ formulas imply the $C^1$ correction in equation (18), for fixed positive $k$ |
| Chandler-Wilde et al., *Integral Equation Methods for Scattering by Multifractal Obstacles*, [2605.19540v1](https://arxiv.org/abs/2605.19540v1) | Proposition 4.10, pp. 25–26 | Background only: a local regularity interval under further geometric hypotheses; not a premise proving the counterexample |

The bounded source search did not establish a previously published proof of this full counterexample. This is not a priority or novelty claim. The cited spectral and trace theorems alone do not supply the screen, charge or Helmholtz conclusion constructed in the manuscript.
