# Finite-jet determination of small-time local controllability

This package gives an analytic counterexample to
[AIM Problem 141](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/141-finite-jet-small-time-control.md).

One fixed polynomial system on R^5 with two measurable controls in
[-1,1]^2 is small-time locally controllable. For every finite Taylor order N,
adding x_5^(2k) to its fourth drift equation, with 2k>N, gives a polynomial
system with the same complete N-jet and the same control set that is not
small-time locally controllable. A single admissible five-dimensional example
negates the universal statement; no separate result in dimensions three or
four is asserted.

Read the [paper](paper/main.pdf), its [editable source](paper/main.tex), and
the [target comparison](TARGET_COMPARISON.md).

The original controllable system and logarithmic estimate are credited to
Kaiwen Jin's earlier
[versioned note](https://github.com/yuiyuiui/AIM/blob/fff30eeb072395341d9944e4c75d5267b770f3b8/research/solutions/417-polynomial-reachable-growth-counterexample/paper/main.pdf),
Theorem 1 and Lemma 2. The present argument compares the actual auxiliary
coordinate's excursion with the positive integral cost of each high-order
perturbation, uniformly over all bounded measurable controls.

[Reproduction instructions](REPRODUCTION.md) explain how to rebuild the PDF.
The mathematical proof is analytic and does not depend on numerical data or
a computer-assisted certificate. AI assistance is disclosed in the paper.
Mathematical review is invited.
