# A four-dimensional periodic Costas array of order six

This package gives a six-point bijection `[2] x [3] -> [2] x [3]` and a
self-contained proof that every translated `2 x 3 x 2 x 3` window of its
periodic extension has distinct nonzero ordered ordinary integer differences.
The order is six, exceeding the proposed value `2^2 = 4`.

It addresses the counterexample alternative in
[AIM problem 627](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/627-periodic-costas.md).
The proof uses the bijective definition of Rubio and Torres, with ordinary
integer differences in every window.

- [Manuscript](paper/main.pdf).
- [LaTeX source](paper/main.tex).
- [Original-target comparison](TARGET_COMPARISON.md).
- [File manifest](PUBLIC_MANIFEST.json) and [SHA-256 checksums](SHA256SUMS).

An earlier [Prove2Me record by shivm](https://prove2.me/theorems/f2732909-8aec-45d0-afe0-8943f5d2c80e),
dated 4 October 2026, announces a disproof of the same conjecture. The proof
and witness underlying that record have not been inspected here. The note
credits the announcement and makes no novelty or priority claim.

Author: Kaiwen Jin. Contact: yui.ui.siki@gmail.com.
OpenAI Codex assisted with the example, proof, drafting and auxiliary integer
checks, and provided separate reader and referee passes on the draft.
Independent mathematical review is requested; submission or an AI review is
not community acceptance.

The proof is analytic and its complete finite table is printed in the note.
It does not require software, private proof supplements or numerical data.
With a standard LaTeX installation, the source can be rebuilt from this package:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error paper/main.tex
```

The original point table is the whole construction; no claim of minimality,
classification or enumeration is made.
