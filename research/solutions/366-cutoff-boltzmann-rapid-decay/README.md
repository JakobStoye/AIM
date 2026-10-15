# Loss of rapid velocity decay for the cutoff Boltzmann equation

By Kaiwen Jin (contact: yui.ui.siki@gmail.com).

This package contains an analytic construction concerning the literal rapid-velocity-decay conclusion of [AIM problem 366](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/366-cutoff-boltzmann-continuation.md).

Theorem 1.1 constructs a nonnegative homogeneous radial smooth solution from Gaussian data, with mass one, uniformly finite energy and upper entropy, and a positive `r^-6` tail at every positive time. Corollary 5.1 explains the endpoint consequence. The solution itself continues smoothly in the weighted continuous space `X_6`. The claim concerns loss of rapid velocity decay; it does not establish local derivative blowup or resolve a conservative, energy-admissible, or positive-time Schwartz continuation problem. No novelty claim is made.

- [Complete manuscript](paper/main.pdf)
- [Editable LaTeX source](paper/main.tex)
- [Target comparison](TARGET_COMPARISON.md)
- [AI use and review disclosure](AI_USE.md)
- [File manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS)

## Build

The manuscript is a standalone LaTeX file with an inline bibliography and no external assets. With a standard TeX Live installation, run from this package directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/main.tex
```

This compiles the paper; it is not a mathematical proof verifier. There are no numerical experiments, proof-critical computed certificates or formal-proof files in this analytic contribution.

Independent mathematical review is requested. Package availability, compilation and AI feedback do not imply acceptance or mathematical certification.
