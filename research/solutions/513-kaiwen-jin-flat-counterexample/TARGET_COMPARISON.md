# Correspondence with AIM 513

Original target: [pinned problem statement](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/513-aspherical-motion-planning-center.md).
The manuscript [main.pdf](paper/main.pdf) supplies a counterexample to the
universal equality, with no additional assumption on the original question.

| Original requirement | Result in the finished paper | Scope |
|---|---|---|
| Closed, connected manifold | Proposition 2, Section 2: free finite quotient of T^5 | Fulfilled |
| Oriented | Proposition 2: each affine generator has determinant +1 | Fulfilled |
| Aspherical | Proposition 2: universal cover is R^5, which is contractible | Fulfilled |
| Dimension n>=3 | Theorem 1 and matrix (2): n=5 | Admissible counterexample |
| G=pi_1(M) | Section 2: explicit affine deck group Gamma; identified with the real Bott realization in Kamishima--Masuda Lemma 3.1 | Same group |
| z=dim_Q(Z(G) tensor_Z Q) | Proposition 2: central translations lie in a fixed two-dimensional plane and contain two independent unit translations, so z=2 | Exact rank |
| Ordinary unreduced two-endpoint TC | Section 1 definition and final proof use Farber's ordinary path-fibration domain count | Same convention |
| Formula TC(M)=2n+1-z | Theorem 1: proposed value 9, but TC(M)>=10 | Equality disproved |
| Prove the formula or construct a counterexample | Explicit closed oriented aspherical M satisfies all premises and violates the conclusion | Complete counterexample alternative |
| Public imported tools | Section 2 cites Kamishima--Masuda equation (3.1)/Lemma 3.1; Section 3 displays Lemma 2.1's ring and applies Farber Theorem 7 | Source hypotheses and notation shown |

The decisive calculation is Lemma 3, equation (5), on pages 2--3:

```math
\bar a\bar b\bar d^{5}\bar e^{2}
=abcd\otimes abcde+abcde\otimes abcd\ne0.
```

There are nine zero-divisor factors, so the cited unreduced lower bound is 10.
The proof does not need an exact TC value or a new universal replacement formula.
