# AIM 411: comparison with the full original target

Target:
[Continuity of states driven by bounded admissible inputs](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/411-bounded-input-state-continuity.md),
revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.
The [manuscript](paper/continuity.pdf) contains the entire submitted proof.

| Original requirement | Manuscript location and result | Coverage |
| --- | --- | --- |
| Arbitrary Banach state and input spaces `X,U` | Section 1, Theorem 1; both real and complex fields are included | Full; no geometric or separability assumption |
| `A` generates a strongly continuous semigroup | Section 1 retains the original generator and semigroup | Identical |
| Resolvent-norm completion `X_{-1}` and compatible extended semigroup | Section 1 defines the same completion and the canonical injection and extended resolvent | Identical |
| Bounded `B:U -> X_{-1}` | Section 1, equation (1) | Identical |
| Every finite horizon and every strongly measurable essentially bounded input | Equation (1) explicitly quantifies over the original input class | Full |
| Endpoint in `X` with a bound independent of the input | Equation (1), with `K_T` depending on the system and horizon | Identical admissibility assumption |
| Original Bochner convolution state at each time | Theorem 1 states exactly that convolution and assigns zero at time zero | Identical |
| Norm continuity on the whole closed interval | Theorem 1 and the last part of its proof in Section 3 | Full, including time zero and the terminal left limit |
| No additional space geometry or input regularity | Lemma 2 constructs a separable state subspace separately for each fixed input; the pasted input in Section 3 is strongly measurable and bounded | No added hypothesis |
| Stronger conclusion, not an extra premise | Equation (3) proves uniform decay of the full control operator norm on the input unit ball | Zero-class admissibility; no quantitative rate claimed |

The two central intermediate results are Lemma 2 (actual state-norm separable
range and weak compactness of a fixed-input scalar multiplier) and Lemma 3
(norm countable additivity). Section 3 supplies the disjoint-interval
contradiction and the fixed-earlier-state continuity argument.

The imported scalar Grothendieck mapping result is
González--Kania, arXiv:2102.03838v3, Theorem 3.1.1 and Proposition 4.1.5.
The Orlicz--Pettis and Pettis measurability theorems are in Diestel,
*Sequences and Series in Banach Spaces*, Chapter IV, pages 24--25.
The extrapolation conventions are those of Weiss (1989), Definition 3.1,
Proposition 3.3 and Remark 3.4. Their hypotheses and uses are stated in the
manuscript. Preußler--Schwenninger, arXiv:2605.12121v1, Corollary 4.10 and
the discussion after Corollary 4.11 supply the cited geometric prior cases.

The submission covers the entire represented-convolution problem printed
in AIM 411. The original axiomatic formulation of Weiss's question can be
broader; no claim about input maps lacking the stated `B`-convolution
representation is made. This comparison records a complete solution claim,
not human peer review, formal verification or upstream acceptance.
