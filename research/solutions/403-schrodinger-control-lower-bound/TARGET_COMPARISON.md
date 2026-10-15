# Comparison with Problem 403

Source: [the original statement](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/403-schrodinger-sharp-fast-control-exponent.md), repository revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

| Original requirement | Paper location and result | Scope |
|---|---|---|
| Every fixed L>0 | Theorem 1; L-dependent positive c_L | Identical interval quantifier |
| i y_t+y_xx=0 on (0,T)x(0,L) | Equation (1) | Identical coefficient and normalization |
| Complex states and controls | Section 1 and the sesquilinear pairing in Section 2 | Identical scalar field |
| Dirichlet control at x=0, zero value at x=L | Equation (1), boundary calculation (6) | Identical boundary geometry |
| Transposition solutions | Section 2, endpoint identity (6), explicit smooth adjoint tests | Necessary identity at the original solution regularity |
| H^-1-unit initial data and full supremum | Equations (2), (8), final paragraph of the proof | One exactly unit witness lower-bounds the entire original supremum |
| L2 norm cost | Equations (2), (11), (16), (17) | Norm retained throughout |
| All T decreasing to zero | Theorem 1 covers 0<T<=L^2/(2pi) | Whole small-time interval |
| Proposed limit L^2/4 | Theorem 1, equations (4)-(5) | Negative answer: liminf >= L^2/pi > L^2/4 |
| Allowed constant dependence | Theorem 1 and (17) | c_L depends only on fixed L and Sobolev norm |

The paper does not assert the true sharp coefficient or existence of the limit. Its proof is self-contained apart from standard Cauchy–Schwarz, the integral norm inequality and Jensen's formula, whose exact normalized form is displayed in Section 3. All cited historical comparisons have exact version/section/theorem locators.

Status: solution claim awaiting independent review. AI assistance and the review circumstances are disclosed in the README and manuscript.
