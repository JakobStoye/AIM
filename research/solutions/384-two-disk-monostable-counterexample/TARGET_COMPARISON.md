# Comparison with AIM problem 384

Target: [the original problem at revision a153f469ee0ea64e876b2ad97c79d252c19a3e22](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/384-reaction-two-obstacle-uniqueness.md).

Submitted result: Theorem 3.1 in [the manuscript](paper/main.pdf). It supplies a counterexample to the universal assertion, rather than a uniqueness theorem for all parameters.

| Original requirement or conclusion | Manuscript location and result | Coverage |
| --- | --- | --- |
| Dimension `d >= 2` | Section 3 fixes `d = 2`. | One allowed dimension suffices to refute a universal assertion. |
| Two disjoint balls with positive finite radii | Equations (7)-(9) specify equal radius `R = 16,003,200,160`, centers `(±(R + 11/10), 0)` and gap `11/5`. | Both obstacles are finite disks and strictly disjoint. |
| `f` in `C^{1,gamma}([0,infinity))`, `0 < gamma < 1` | Section 2 and equation (3) give one explicit reaction with globally bounded, Lipschitz derivative. | The same reaction belongs to every prescribed Hölder class. |
| `f(0)=f(1)=0`, endpoint derivative signs, positivity on `(0,1)` and negativity above 1 | The paragraph following equation (3) verifies these properties, with derivatives `±1/100`. | All original reaction hypotheses are met; no decreasing growth quotient is assumed. |
| Equation on the full exterior, zero on both complete boundaries | Section 4 and Lemma A.1 construct and pass both bounded-domain exhaustions to the same full exterior. The explicit annular barrier preserves both full zero boundaries. | No truncated domain or condition at infinity replaces the stated problem. |
| Positive bounded classical solutions in `C^2(Omega) ∩ C(closure Omega)` | Theorem 3.1 and Lemmas A.1-A.3 give `0 < u,U < 1` and the required regularity. Stability excludes a zero minimizing limit. | Both equilibria satisfy the required solution class. |
| Exactly one solution for every admissible reaction and geometry | Equations (10), (18), and Section 4.4 give neck squared masses `<= 4500` and `> 5000`. | The two solutions are distinct, so universal uniqueness fails. |
| Public imported analytic tools | Section 4 cites Section 1.1 of Fernández-Real and Ros-Oton's author-hosted 2020-preface notes for Sobolev compactness, trace, truncation and Poincaré tools. Appendix A uses Theorem 1.5, Corollary 1.12, Proposition 1.13 and Theorem 2.12 in that exact version. | The manuscript includes the application, kernel normalization, comparison barrier, stability argument and separation proof; its reference explicitly distinguishes these locators from the later published edition. |

The result does not assert multiplicity for every reaction, every separation or every dimension. Those broader assertions are unnecessary for a counterexample to the question as stated. This is an analytic claim; no numerical or formal-proof evidence is represented as a substitute for its argument.
