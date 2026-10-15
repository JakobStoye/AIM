# CO phase selection for a stirred catalytic surface model

**Author:** Kaiwen Jin

**Contact:** yui.ui.siki@gmail.com

This package presents an affirmative solution claim for
[AIM Problem 185](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/185-catalytic-carbon-monoxide-poisoning.md),
at statement revision a153f469ee0ea64e876b2ad97c79d252c19a3e22.
For every fixed p>q>0 and finite positive reaction and stirring rates,
the exact catalytic process on Z2 converges locally to the all-CO phase
from every iid initial law of positive CO density.

- [Complete manuscript](paper/manuscript.pdf)
- [Editable LaTeX source](paper/manuscript.tex)
- [Correspondence with the original target](TARGET_COMPARISON.md)
- [Public file manifest](PUBLIC_MANIFEST.json)
- [File checksums](CHECKSUMS.txt)

The proof starts with the signed-density estimate of Durrett and Swindle,
then bounds the integrated reaction rate and every state change, including
unequal-state exchanges. Sitewise fixation, connectedness and the spatial
iid driving field select a deterministic color; the signed density excludes
oxygen. Each site's fixation time can differ. A common finite absorption
time for the infinite lattice and a parameter-uniform convergence rate are
not asserted.

The manuscript contains the full analytic argument, including the graphical
construction and the clock-counting identity. No numerical computation is
used in the proof. To build the PDF, run in the paper directory:

    latexmk -pdf -interaction=nonstopmode -halt-on-error manuscript.tex

The source uses standard LaTeX packages. The submitted PDF was built locally.
OpenAI Codex assisted with the argument and writing, as disclosed in the
manuscript. Independent mathematical review is requested; submission of this
package does not establish repository acceptance.
