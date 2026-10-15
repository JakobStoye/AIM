# A finite-entropy counterexample for a reversible reaction-diffusion system

This package contains a proposed negative resolution of
[AIM 482](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/482-entropy-reaction-diffusion-renormalized-uniqueness.md).
The reversible reaction A+2B <-> 3B, with equal diffusion on a
three-dimensional ball, has two global renormalized solutions with the same
nonnegative finite-entropy initial concentrations (10000/|x|,0).

- [Manuscript](paper.pdf) and [editable LaTeX source](paper.tex).
- [Comparison with the complete target](TARGET_COMPARISON.md).
- `PUBLIC_MANIFEST.json` and `SHA256SUMS` identify the package files.

The proof is analytical. No numerical experiment, software library or
computer-assisted certificate is needed. With a standard TeX installation,
the paper can be built using `latexmk -pdf -halt-on-error paper.tex`.

The construction uses an unbounded initial concentration and an initially
absent species, both allowed by the frozen target. Independent mathematical
review is requested. OpenAI Codex assisted with the construction, calculations,
source work and manuscript preparation. No separate detailed AI review report
is included in this public package.
