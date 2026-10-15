# A three-leaf counterexample for Fitch reconstruction under a molecular clock

This package gives a negative answer to the universal inequality in
[AIM Problem 328](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/328-fitch-ultrametric-ancestral-accuracy.md).

For the symmetric rate-one twenty-state model, the positive-edge ultrametric
three-leaf tree in Theorem 1 has Fitch accuracy 38829/400000, while each single
leaf agrees with the root with probability 39/400. The exact deficit is
171/400000. The complete finite analytic argument, including uniform final
tie breaking, is in the [paper](paper/main.pdf) and [editable source](paper/main.tex).
This single admissible example refutes the assertion quantified over all
integers r>=5; it does not classify every individual alphabet size.

- [Target comparison](TARGET_COMPARISON.md)
- [AI-use and review disclosure](AI_USE.md)
- [Exact-arithmetic verifier](code/exact_three_leaf.py)

## Reproduce the check

Python 3.10 or newer is sufficient; only the standard library is used.

```sh
python3 code/exact_three_leaf.py
```

The script checks both a four-event calculation and an independent sum over
all 160000 assignments to the four non-root vertices. It asserts total
probability one, accuracy 38829/400000, benchmark 39/400 and deficit 171/400000.
The displayed analytic calculation in the paper is the proof; this execution
is a reproducible consistency check, with exact rational arithmetic.

To build the editable paper with a LaTeX installation:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/main.tex
```

No external data or private supplement is needed. PUBLIC_MANIFEST.json and
SHA256SUMS bind the supplied files. Independent mathematical review is requested.
