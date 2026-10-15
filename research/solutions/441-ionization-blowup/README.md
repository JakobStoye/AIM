# Finite-time blowup with positive ionization

This package accompanies a claimed negative answer to [AIM Problem 441](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/441-ionization-laser-envelope-global-regularity.md).

[The note](paper/ionization_blowup.pdf), by Kaiwen Jin, constructs one strictly positive ionization coefficient with `epsilon=c=c_g=1`, `K=2` and `alpha_5=0`, and a nonzero compactly supported smooth optical datum with zero initial density. The original coupled smooth solution has nonnegative density and a gradient norm tending to infinity at a finite time. One admissible witness negates the problem's universal global-continuation assertion. The coefficient and datum are selected by the proof; no explicit Cauchy threshold or numerical initial datum is supplied.

The argument uses the quantitative scalar profile construction of Donninger and Schörkhuber, arXiv:2406.16597v3, and the fixed-profile linear estimates of Zexing Li, arXiv:2304.02078v2. The note proves the additional coupled-profile, density-transport, contraction, localization and physical-Cauchy arguments. The companion arithmetic checks a finite set of coefficient and strict-margin inequalities; it does not rerun either published PDE proof.

- [Editable standalone LaTeX source](paper/ionization_blowup.tex)
- [Target comparison](TARGET_COMPARISON.md)
- [Exact-arithmetic reproduction and data provenance](code/README.md)
- [Recorded exact-arithmetic output](verification/exact_constants.json)
- [AI-use and review disclosure](AI_USE.md)

Run the finite calculation from this directory with an ordinary, unoptimized Python interpreter:

```sh
python3 code/check_constants.py
```

It needs only the Python standard library; Python 3.13.3 was used for the recorded replay. A changed coefficient input or a failed inequality makes the command fail. The script rejects `python -O`, which would disable assertions.

To rebuild the note with a LaTeX installation containing the standard packages used by the source:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/ionization_blowup.tex
```

The mathematical proof is in the note, with its public literature dependencies. This package supplies no Lean formalization or independent human verification. The contribution remains a solution claim pending external mathematical review.
