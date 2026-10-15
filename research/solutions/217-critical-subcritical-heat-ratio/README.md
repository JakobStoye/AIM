# A smooth counterexample to critical–subcritical heat-kernel comparison

Kaiwen Jin — [yui.ui.siki@gmail.com](mailto:yui.ui.siki@gmail.com)

This research note proposes a complete negative answer to [AIM Problem 217](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/217-critical-subcritical-heat-ratio.md), at repository revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`. It is submitted for independent mathematical review.

Theorem 1.1 constructs one pair of smooth bounded real potentials on the Euclidean line. Both Friedrichs Schrödinger operators are nonnegative with spectral bottom zero. At the fixed distinct points `(0,1)`, the numerator heat kernel has finite time integral and the reference kernel has infinite time integral; the reference operator has no nonzero square-integrable zero mode. Nevertheless, the diagonal quotient at `(0,0)` has infinite limsup. Thus the compact singleton `{(0,0)}` contradicts the proposed locally uniform limit without an ordering assumption on the potentials.

The numerator is one fixed nonnegative compact bump. The reference construction selects a small heat-kernel value from each finite approximation with a positive spectral gap, then protects that value by placing later changes sufficiently far away. Infinitely many distant unit intervals restore criticality in the single final potential. The time is chosen after each individual gap, and the protection radius is chosen after that time. The proof uses no common positive lower bound on the finite-stage gaps. Appendix A supplies the one-dimensional Dirichlet and Green-kernel argument.

## Materials

- [Complete nine-page manuscript](paper/main.pdf)
- [Editable LaTeX source](paper/main.tex)
- [Comparison with every original requirement](TARGET_COMPARISON.md)
- [File hashes and purposes](PUBLIC_MANIFEST.json)

This is an analytic construction. It uses no numerical experiments, proof-critical computation, or formal proof code. The result concerns the unordered-potential question; it does not establish a failure of the ordered-perturbation results cited in the manuscript. No priority claim is made.

## Rebuilding the paper

A standard TeX installation needs `amsmath`, `amssymb`, `amsthm`, `mathtools`, `lmodern`, `microtype`, `geometry`, and `hyperref`. From this directory:

```sh
mkdir -p build
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build paper/main.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build paper/main.tex
```

The result is `build/main.pdf`. The supplied PDF was built with pdfTeX 1.40.27 (TeX Live 2025). Rebuilding requires only the supplied source and standard TeX packages. PDF creation dates and identifiers may change; the manifest identifies the supplied artifact. The exported source was also built in isolation, and the supplied PDF's nine pages, references, and links were checked. Compilation checks document integrity, not mathematical correctness.

## AI use and review

OpenAI's Codex assisted in developing and writing the argument and checking cited passages. Codex also performed internal AI reviews of the argument and manuscript. A reader review and a referee review examined the same manuscript draft before one localized revision of exposition and bibliographic details. No separate detailed AI report is submitted. These checks do not constitute human review, formal verification, or acceptance by the problem repository. Independent mathematical review is requested. This package adds materials; catalogue classification is left to the maintainers.
