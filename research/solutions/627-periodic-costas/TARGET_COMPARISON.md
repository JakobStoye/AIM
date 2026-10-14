# Comparison with AIM 627

Original target:
[Smallest orders for periodic multidimensional Costas arrays](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/627-periodic-costas.md),
revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

The note gives a counterexample to the complete universal necessity assertion.
It uses `m=4`, `k=2`, side lengths `(2,3,2,3)` and order `n=6`.

| Original requirement | Location and witness |
|---|---|
| `m >= 2`, with remaining target allowing dimension at least four | Theorem 1: `m=4` |
| `1 <= m-k <= k` | Construction and final paragraph: `m-k=k=2` |
| Every side length at least two | Side lengths `(2,3,2,3)` in Theorem 1 |
| Equal products of input and output sides | Both products are `2*3=6` |
| A bijection on the entire coordinate boxes | Table 1 lists all six distinct inputs and all six distinct outputs |
| Graph extended by the stated period lattice | Theorem 1 defines `S` and `L=2Z x 3Z x 2Z x 3Z` |
| Every offset in `Z^m` | The proof fixes arbitrary `t in Z^4`; the explicit remainder representatives include negative offsets |
| Distinct nonzero ordered ordinary integer differences | Table 2 and reversed pairs distinguish all 30 ordered pairs; fixed binary-coordinate signs carry ordinary difference equality back to the same pair |
| Differences are not reduced modulo every side length | Binary differences remain ordinary signed integers; modulo-three residues are only a sufficient auxiliary test within the proof |
| Failed conclusion `n=2^k` | `6 > 4 = 2^2`; the second input side is three |

One admissible counterexample refutes the universal assertion. The proof does
not restrict that assertion to a bounded positive range and does not rely
on a finite sample of translated windows.

The original definition and conjecture are attributed to Rubio and Torres,
*Multidimensional Costas Arrays and Their Periodicity*, Definitions 2--4 and
Conjecture 1, [arXiv:2208.02378v1](https://arxiv.org/abs/2208.02378v1).
The earlier [4 October 2026 disproof announcement by shivm](https://prove2.me/theorems/f2732909-8aec-45d0-afe0-8943f5d2c80e)
is acknowledged; its underlying negative proof was not inspected, and no
novelty or priority is claimed for this note.
