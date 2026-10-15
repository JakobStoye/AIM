# Comparison with AIM problem 383

Target: [Continuity of finite-cluster mass at the onset of Flory gelation](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/383-flory-gelation-mass-continuity.md), revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

Manuscript: [Continuity of finite-cluster mass at the onset of Flory gelation](paper/flory_onset.pdf), by Kaiwen Jin. This is a full solution claim awaiting independent review.

| Original requirement | Manuscript location and result | Scope |
| --- | --- | --- |
| Every real exponent `0 < alpha < 1` | Section 1 and Theorem 1; all estimates retain this range | Full range |
| Continuous symmetric nonnegative kernel comparable above and below to `x^alpha y + x y^alpha` | Equations (1)–(2) and Theorem 1 | Same hypotheses |
| Continuous positive limiting gel kernel `ell`, with `K(x,y)/y -> ell(x)` and the given two-sided bounds | Equation (2), weak equation (3), and Theorem 1 | Same hypotheses; the proof uses only the upper bound on `ell` |
| Every finite nonnegative initial measure with unit first moment | Section 1 and Theorem 1 | No higher moment added |
| Every family of finite nonnegative measures with nonincreasing number and mass satisfying the original compact-test Flory identity | Equation (3) and the preceding solution definition; Lemma 2 derives the bounded-test extension | Same solution class; no selection or uniqueness requirement |
| Finite positive gelation time `T_g = inf {t : m(t) < 1}` | Theorem 1 | Same hypothesis; no separate existence assertion |
| `m(T_g)=1`, right limit one, and continuity at `T_g` | Theorem 1; right continuity from equation (8), exclusion of a jump in the closing proof | Full conclusion |
| Justification of unbounded-moment and endpoint operations | Lemma 2; bounded cutoff Lemma 3; dominated concave-test passage and pregelation tail monotonicity in Lemma 4; bounded exponential tests in Lemma 5 | Uses only finite particle number and first moment |
| Uniformity needed for the terminal tail contradiction | Lemma 5, equation (13): its positive retention constant is independent of the diverging size scale `R`; the closing proof fixes `A,d` before taking `R` large | Explicit uniform bound |
| Relation to the cited prior result | Section 1 credits Fournier–Laurençot, Proposition 2.3 and its following question, for the after-gelation result and the unresolved endpoint; Section 2 proves the concave-test estimate used here | No external research theorem is required as an unproved step of the submitted proof |

The manuscript does not claim uniqueness, a quantitative onset rate, a particle-system theorem, independent human certification, formal verification, or repository acceptance. It adds only the public paper and source; catalogue classification is left to maintainer review.
