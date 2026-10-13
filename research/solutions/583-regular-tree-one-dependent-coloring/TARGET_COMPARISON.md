# Target comparison: AIM 583

Original target: [Problem 583 at revision c9929805cece044705abaaebe1cebddac1ba11a6](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/583-regular-tree-one-dependent-coloring.md).

Submitted result: Theorem 1.1 of [Symmetric one-dependent colorings of regular trees](paper/main.pdf), by Kaiwen Jin. It gives the positive existence alternative for every integer d >= 3 with

```math
q(d)=2^{2d+16}d^2(2^d-1)9^{d-1}.
```

All locations below refer to this manuscript and its [source](paper/main.tex).

| Original requirement | Manuscript location | Coverage in the submitted argument |
|---|---|---|
| Infinite connected d-regular tree, every integer d >= 3 | Theorem 1.1, Section 4 | A single law on the full countable vertex set is constructed for every stated degree. |
| A finite integer q = q(d) | Equation (1); Lemmas 2.1 and 3.2 | The explicit integer is fixed by d before any finite set is considered; both estimates are uniform in forest size. |
| Almost surely different endpoint colors on every edge | Proposition 3.1; final paragraph of Section 4 | Monochromatic edges have zero finite-law weight. Countability gives simultaneous properness on all edges. |
| Independence of complete restrictions to every finite A, B at distance greater than one | Section 4, displayed factorization | Every coloring of the induced union has weight p_(A union B)(x,y) = p_A(x)p_B(y), since there is no edge between the sets. This is independence of the full vectors. |
| Invariance under every graph automorphism | Proposition 3.1; Section 4 | Slot symmetry removes incident-edge order, parity conjugation removes the bipartition choice, and equality of finite-dimensional laws gives invariance of the whole law. |
| Invariance under every permutation of the q color names | Proposition 3.1; Section 4 | Letter permutations act by isometries on the word space and permute the tensor family; the resulting whole law has full palette symmetry. |
| No finite-range factor or bounded-round algorithm requirement | Theorem 1.1 and the entire construction | The solution object is an exact probability law; no implementation-model restriction is assumed. |
| Settle existence for every d >= 3, or exhibit an impossible degree | Theorem 1.1 | The claimed resolution is existence for all degrees in the question. |

The finite-law step is a complete analytic argument: Section 2 supplies a bounded inverse and quantitative tensor estimates; Section 3 proves nonnegative normalized projective laws, including deletion of internal vertices and strict positivity on every proper finite forest. Section 4 invokes Kallenberg's first edition (1997), Theorem 5.16, printed p. 92, for the probability extension and Proposition 2.2, printed p. 25, for law uniqueness. Finite discrete coordinate spaces satisfy the Borel-space hypotheses.

The paper proves its tree estimates directly and credits the earlier path method. It does not claim an optimal color count, a specified algorithmic realization, or recovery of a particular line law. This comparison records the scope of a complete solution claim; it does not confer maintainer acceptance or independent mathematical certification.
