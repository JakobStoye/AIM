# Signed-data null control of a two-phase Stefan interface

This package proposes a complete solution to [AIM Problem 258](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/258-global-two-phase-stefan-control.md), at revision `c9929805cece044705abaaebe1cebddac1ba11a6`.

Theorem 1 treats every positive rod length, pair of diffusivities, latent-heat coefficient and terminal time; every interior initial and target interface position; and arbitrary real smooth initial temperatures compactly supported in their phases. Two bounded Dirichlet controls drive both temperatures exactly to zero and the interface to the prescribed position, while the interface remains strictly interior and C1 throughout. The zero-extended temperatures are continuous into L2. No sign or smallness assumption is imposed, and no common control-cost bound is asserted.

The proof first constructs a short uncontrolled signed-data solution analytic for positive time. It identifies that solution with the interface-centered series of Colle, Loheac and Takahashi, then uses Gevrey cutoffs and a convex interpolation of the interface position to finish the control. The source's sign-restricted main controllability theorem is not used to cover the arbitrary-sign initial class.

- [Complete manuscript](stefan_signed_control.pdf)
- [Editable source](stefan_signed_control.tex)
- [Requirement-by-requirement comparison](TARGET_COMPARISON.md)
- [File checksums](MANIFEST.json)

This is an analytic argument. It uses no numerical experiment, computational certificate or formal proof project. The standalone source builds with a standard TeX Live installation:

```sh
pdflatex -interaction=nonstopmode -halt-on-error stefan_signed_control.tex
pdflatex -interaction=nonstopmode -halt-on-error stefan_signed_control.tex
```

OpenAI Codex assisted with developing the argument, checking sources and preparing the manuscript. The submitted claim requests independent mathematical review. No detailed AI review report is included. Catalogue classification is left to the maintainers.

Author: Kaiwen Jin. Manuscript contact: `yui.ui.siki@gmail.com`.
