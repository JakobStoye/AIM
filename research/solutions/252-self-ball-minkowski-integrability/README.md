# Problem 252: a complete analytic solution claim

The manuscript proves the proposed rigidity implication for a smooth strongly convex planar norm: if its billiard in its own unit ball has the entire phase annulus foliated by continuous essential invariant curves, then the norm is induced by an inner product. The theorem assumes no additional finite symmetry.

This is a solution claim submitted for independent mathematical review. Catalogue classification and acceptance are left to the maintainers.

- [Complete manuscript](paper/minkowski_integrability.pdf)
- [Editable LaTeX source](paper/minkowski_integrability.tex)
- [Comparison with every original requirement](TARGET_COMPARISON.md)
- [Original problem at the fixed target revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/252-self-ball-minkowski-integrability.md)

The argument represents a norm chord as a strict support maximum of alternating signed areas on the unit ball and its rotated polar. Finite length-action maxima transfer to the alternating action. Averaging on both phase annuli gives a geometric inequality; a centro-affine parameter and the symmetric Blaschke--Santalo inequality force the unit ball to be an ellipse. The paper contains the full proof and cites its external theorem inputs.

The result is analytic. It does not use numerical evidence, a computational certificate, or a formal proof project.

Build the manuscript with a standard LaTeX installation containing `amsart`, `amsmath`, `amssymb`, `geometry`, and `hyperref`:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/minkowski_integrability.tex
shasum -a 256 -c SHA256SUMS
```

The delivered PDF was built using pdfTeX 1.40.27 (TeX Live 2025) and latexmk 4.86a. Compiling the source checks document construction, not the mathematical theorem.

AI use is disclosed at the end of the manuscript. OpenAI Codex assisted in developing the argument, checking references, and writing the text. The complete pre-revision manuscript was read in two fresh OpenAI Codex contexts: one checked comprehension and presentation; the other checked the argument and all seven cited sources. The mathematical reviewer reported no major objection within that scope. Four localized exposition suggestions were incorporated in one author revision. These were AI reviews on a shared host, with physical isolation unverified. No human review or formal verification is claimed. Independent mathematical review is requested; no separate detailed AI review report is submitted.
