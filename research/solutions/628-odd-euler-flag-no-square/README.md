# Odd Euler characteristic for flag-no-square four-manifolds

Kaiwen Jin — yui.ui.siki@gmail.com

This package presents a proposed complete solution to
[AIM problem 628](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/628-odd-euler-flag-no-square.md).
The manuscript constructs an actual closed connected PL four-manifold of odd
Euler characteristic with a finite flag-no-square triangulation. Orientability
is not required by the target.

The construction folds a punctured manifold along an antipodal boundary map.
A geometric short-path bound and a twisted double preserve the global clique
and no-square conditions. The resulting Euler characteristic is
`2 chi(Y) - 3`, where `Y` is a finite manifold quotient of the regular
hyperbolic simplicial tessellation used in the paper.

- [Complete manuscript](paper/odd_euler_flag_no_square.pdf)
- [Editable LaTeX source](paper/odd_euler_flag_no_square.tex)
- [Original-target comparison](TARGET_COMPARISON.md)

The argument is analytic and uses the public references stated in the manuscript.
No numerical computation or undisclosed certificate is required to apply its
proof. To rebuild the PDF from this directory with a standard TeX installation:

```sh
latexmk -norc -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/odd_euler_flag_no_square.tex
```

OpenAI Codex assisted with the construction, mathematical checking and writing.
Independent mathematical review is requested. This submission adds the
mathematical materials; catalogue classification remains with the maintainers.

PUBLIC_MANIFEST.json lists the mathematical content files and their SHA256
hashes. SHA256SUMS additionally binds that manifest.
