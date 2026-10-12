# Correspondence with AIM 559

Original statement: [AIM 559 at revision c9929805cece044705abaaebe1cebddac1ba11a6](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/559-univariate-trace-decidability.md). Manuscript: [Undecidability of unnormalized univariate trace inequalities](paper/trace_decidability.pdf).

| Original requirement | Manuscript location | Coverage |
|---|---|---|
| An input positive integer d and rational polynomial F | Theorem 1 and Section 3, formula (8), construct legal d=2k+2 and rational F_P from an arbitrary integer polynomial | Proves undecidability for the stated unrestricted input class |
| One real symmetric matrix | Section 1, formulas (1)-(2), and proof of Theorem 1 | One spectrum; every witness is a diagonal real symmetric matrix |
| Ordinary unnormalized traces | Section 1 convention; Lemma 2 sums and Section 3 linear forms | No division by n |
| Pure trace, no free matrix factor, scalar constant 1 | Section 1; Lemma 2 zero constants; Section 3 following (8) | Only positive power sums z_1,...,z_d; scalar constants never become tr(I) |
| Every n>=1, with unbounded n | Lemma 2, dimension-independent estimate (3)-(4), and witness size 1+sum m_i | Full universal size range; unbounded integer counts are essential |
| Every real spectrum | Lemma 2 whole-line bounded-region and tail proof; Lemma 3; final completed-square estimate | All off-node, negative, zero and arbitrarily large eigenvalues are covered |
| Exact nonnegativity, including equality | Final proof, completed square for valid discrete inputs and value <=-1 for a negative integer input | Both directions of the exact sign equivalence |
| Give a decision algorithm or prove undecidability | Theorem 1 and its final reduction | Undecidability alternative |

The sole imported undecidability interface is the integer-polynomial sign decision statement in Hatami and Norine, arXiv:1005.2382v3, Section 5, PDF p.11. The positive-integer convention is transferred to nonnegative integers by substituting u_i+1, as stated in Section 3. The new argument in Lemmas 2-3 and the final proof supplies the necessary uniform one-spectrum reduction.

The normalized-trace results and multivariate trace result cited in Section 1 provide context. The proof does not identify either convention with the original univariate target.

This is a complete solution claim submitted for mathematical review. No independent human or formal certification or upstream acceptance is asserted.
