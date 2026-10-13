# AIM 494 target comparison

Target: [494. Universality of the interleaving distance over arbitrary fields](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/494-interleaving-distance-universality.md),
repository revision `c9929805cece044705abaaebe1cebddac1ba11a6`.

The original assertion quantifies over every field, every parameter count
n>=1, every ordinary homology degree i>=0, every i-stable extended
pseudometric on all module isomorphism classes, and all realizable pairs.
Its explicit alternative permits an i-stable distance and a realizable
pair violating the asserted inequality.

Theorem 1 of the paper meets that negative alternative: n=4, i=0, and a
bounded 0-stable pseudometric d_0 on all four-parameter module classes, with
ordinary-H_0 realizable M,N for which d_0(M,N)=3>d_I(M,N)=1. The construction
works separately over every field, so it includes prime and non-prime fields.

| Original requirement | Paper location | Exact coverage |
|---|---|---|
| Field k, n>=1, i>=0 | Theorem 1; Section 4 | A counterexample at n=4 and i=0 for every field refutes the universally quantified assertion. |
| Ordinary singular homology | Proposition 3; Section 4 | H_0 is naturally free on path components; discrete three-point functions realize the pair. |
| Arbitrary functions | Proposition 3 | The proof uses sublevel inclusions only and assumes no continuity. The witness functions are continuous. |
| Metric on all module isomorphism classes | Proposition 2; Section 3 | Intrinsic finite coordinate-support multiset, exceptional feature for other modules, and a bounded metric pullback. |
| Extended pseudometric axioms | Section 3 | Symmetry, diagonal, and triangle for support shifts, matching, exceptional extension, and cap. |
| Stability for every space and every pair of functions | Proposition 3 | Full uniform perturbation bound, including infinite component colimits, zero/infinite perturbation, and empty space. |
| No finite-dimensionality hypothesis | Proposition 3 | Infinite colimits are treated by the exceptional feature; finite colimits allow infinite-dimensional sublevel homology. |
| Realizable violating pair | Section 4 | Functions on a discrete space of three points; exact distances 1 and 3. |

The birth vectors, inverse matrices, and free-module algebraic separation are
credited to Bjerkevik's arXiv:1609.02086v3, Example 5.2, equation (15), p. 17,
and Example 5.3, p. 18. The required supplement is the intrinsic support
construction and its all-input ordinary-H_0 stability. The paper reproduces
the finite calculations explicitly.

The paper addresses ordinary degree zero. It does not prove positive-degree
universality over arbitrary fields and does not contradict universality for
distances required to be stable in every homology degree. No reduced-homology
or one-parameter convention is substituted for the frozen statement.

The manuscript was developed and checked with OpenAI Codex assistance by
the same AI assistant. Independent human mathematical review is requested;
this submission does not claim that such review has occurred.
