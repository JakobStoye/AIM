# Mass conservation for fractional porous-medium flow on noncompact manifolds

This package proposes a complete resolution of [AIM problem 473](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/473-manifold-fractional-pme-mass-conservation.md), at repository revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

Theorem 2.2 proves conservation of total mass for every nonnegative weak dual solution in the stated class that belongs to spatial L1 at each finite time. It covers all the prescribed complete connected noncompact manifolds, dimensions at least two, exponents greater than one, and fractional orders strictly between zero and one. The initial datum is any nonnegative integrable function.

- [Complete manuscript](paper/mass_conservation.pdf)
- [Editable, standalone LaTeX source](paper/mass_conservation.tex)
- [Target comparison and source roles](TARGET_COMPARISON.md)
- [File manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS)

The proof derives a mass upper bound from ordered Green potentials, obtains global integrability of the nonlinear power on positive time intervals through heat-regularized energy, and then reads off mass equality through a conservative linear resolvent. The required linear heat and Green-potential estimates are credited in the manuscript.

Author: Kaiwen Jin. Contact: yui.ui.siki@gmail.com.

AI tools were used in argument development, drafting and internal review, as disclosed in the manuscript. No separate detailed AI review is submitted. Independent mathematical review is requested; publication of this package is a solution claim, not maintainer acceptance or formal verification.

This is a purely analytic contribution. It does not depend on numerical experiments, a computational certificate or a Lean project.

To rebuild the paper with a standard TeX installation, run the following twice from this directory:

```sh
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper paper/mass_conservation.tex
```

Only the paper, source and public target comparison are needed to read and assess the argument. The manifest identifies the supplied files; it is a content inventory, not a correctness certificate.
