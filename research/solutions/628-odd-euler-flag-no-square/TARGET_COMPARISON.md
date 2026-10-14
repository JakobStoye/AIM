# Correspondence with AIM 628

Target: [the immutable original statement](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/628-odd-euler-flag-no-square.md),
revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

Manuscript: *Odd Euler characteristic for flag-no-square four-manifolds*.
This comparison is based on that manuscript and the public original target.

| Original requirement | Manuscript result | Scope |
| --- | --- | --- |
| Existence of a manifold | Theorem 1 and its construction in Section 4 | One finite construction |
| Topological dimension four | Proposition 3 and Lemma 2 produce a PL four-manifold as an actual covering quotient | Full |
| Closed: compact without boundary | The twisted double is closed; its finite free quotient is closed | Full |
| Connected | The star sum, twisted double and quotient remain connected | Full |
| Odd Euler characteristic | End of Section 4: chi(Q)=2chi(Y)-3 | Full |
| Finite triangulation | Finite quotient seed, star sum, double and simplicial quotient | Full |
| Flag: every clique is a simplex | Lemma 2 lifts each quotient clique to a simplex upstairs | Global |
| No induced four-cycle | Lemma 2 uses displacement at least five to lift every four-cycle closed | Global |
| Orientability not required | Theorem 1 imposes no orientability requirement on the final manifold | Allowed scope retained |
| Actual manifold, not merely a pseudomanifold | Lemma 2 preserves vertex stars and the topological covering; Proposition 3 starts from a closed PL manifold | Full |
| No prescribed vertex link | The 600-cell link is a chosen ingredient of the construction | No extra hypothesis on the target |

The geometric bound in Lemmas 4–5 applies outside the deleted center, rather
than only within its link. Section 4 excludes shortcuts introduced by the finite
quotient or distant gluing. Proposition 3 treats multiple boundary excursions
and proves the displacement condition for all vertices of the double.

Public imported results are the regular tessellation quotients of Przytycki
and Świątkowski, the star-connected sum of Kalmanovich–Nevo–Sorcar, and the
600-cell coordinates and Coxeter chamber facts cited from Heckman's notes.
Their roles and exact versions are stated in the paper. The additional folding,
short-path and global quotient arguments are written there in full.
