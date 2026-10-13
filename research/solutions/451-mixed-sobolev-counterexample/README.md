# A proposed counterexample to AIM 451

This note constructs real smooth mean-zero functions on the unit two-torus
with bounded gradient norm in `H^(-1/2) + L1` and scalar norm tending to
infinity in `H^(1/2) + W^(1,1)`. Theorem 1 shows that the proposed family fails already in dimension two,
refuting the universal assertion in
[AIM 451 at the submitted target revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/451-bourgain-brezis-mixed-sobolev-gradient-estimate.md).

- [Complete manuscript](paper/main.pdf)
- [Editable LaTeX source](paper/main.tex)
- [Target comparison](TARGET_COMPARISON.md)

The result is an analytic counterexample. It uses a finite reflected walk
encoded by step functions, separated normal scales and Poisson smoothing.
No numerical experiment or computational certificate is required for its
proof. The source is self-contained apart from the cited basic analysis
results.

To rebuild with a TeX installation containing the standard packages used in
the source:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -cd paper/main.tex
```

Author: Kaiwen Jin. Manuscript contact: yui.ui.siki@gmail.com.
OpenAI Codex assisted the construction, proof, source checks and writing.
Separate Codex contexts reviewed the manuscript argument, cited sources and
exposition; the writing context checked the resulting local revisions. These
were AI reviews. This is a complete solution claim submitted for independent
human mathematical review; catalogue classification is left to the maintainers. No detailed
AI review report accompanies the submission.
