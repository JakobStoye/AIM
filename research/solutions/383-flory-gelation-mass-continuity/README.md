# Continuity at the onset of Flory gelation

This package submits a complete analytic solution claim for [AIM problem 383](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/383-flory-gelation-mass-continuity.md), at target revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

For every weak Flory solution in the stated kernel class, with `0 < alpha < 1`, a finite initial measure and unit first moment, Theorem 1 proves that the finite-cluster mass is continuous at every finite positive gelation time and equals one there. The proof uses bounded and concave test functions together with a time-dependent exponential tail estimate. It requires no higher initial moment, uniqueness, or particle approximation.

- [Complete paper](paper/flory_onset.pdf)
- [Editable LaTeX source](paper/flory_onset.tex)
- [Comparison with the full target](TARGET_COMPARISON.md)
- [Payload manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS)

Author: Kaiwen Jin. Contact: yui.ui.siki@gmail.com.

## Build

The manuscript is standalone and has an inline bibliography. With a standard TeX Live installation containing the listed packages, run from this directory:

```sh
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper paper/flory_onset.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper paper/flory_onset.tex
```

No numerical experiments, computational certificates or formal proof files are part of this analytic result. The source builds with only the public files and standard LaTeX packages.

## AI use and review

AI tools assisted the mathematical development, checking and writing. An AI reader and an AI referee examined an anonymous earlier draft in fresh contexts, followed by one author revision and final artifact checks. These are internal AI reviews, not independent human review or formal verification. No detailed review report is submitted. Independent mathematical review is requested; this package does not claim upstream acceptance.

The argument credits the concave-test method of Fournier and Laurençot. The paper proves the endpoint estimate it needs directly. It makes no priority claim based on an unsuccessful literature search.
