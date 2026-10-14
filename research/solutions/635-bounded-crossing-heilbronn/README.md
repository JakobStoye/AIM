# Small mod-two area four-cycles

This package contains Kaiwen Jin's proposed complete resolution of [AIM problem 635](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/635-bounded-crossing-heilbronn.md), at revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

For every fixed meeting bound $`k\ge2`$, Theorem 1 gives an explicit function $`\varepsilon_k(n)\to0`$ such that every admissible drawing of $`K_n`$ in the unit square contains a nonzero original $`\mathbb F_2`$-cycle of mod-two area at most $`\varepsilon_k(n)`$. For $`n\ge4`$, the cycle is an abstract four-cycle of original edges. Its drawing may cross itself. The bound is not asserted to be optimal.

The argument compares triangles through one common edge. A quadratic bound on their simultaneous parity patterns gives a fixed shattering-dimension bound. The proved finite trace inequality and an elementary weighted sampling argument produce two close parity regions; their common edge cancels, yielding the required four-cycle. Classical set-system tools are credited in the paper and proved there in the forms used.

Read the [five-page manuscript](paper/main.pdf), [editable LaTeX source](paper/main.tex), and [target comparison](TARGET_COMPARISON.md). The proof is analytic and uses no numerical result, code, computational certificate or formal proof.

## Reproduce the PDF

The source is standalone and uses standard LaTeX packages. From this package directory:

```sh
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The supplied PDF was compiled with pdfTeX 1.40.27. Compilation and page inspection check the document, not the mathematical theorem. From the package directory, check the supplied files with:

```sh
shasum -a 256 -c SHA256SUMS
```

`PUBLIC_MANIFEST.json` records the selected content and hashes. `SHA256SUMS` also binds the manifest; it does not hash itself.

## AI use and review status

OpenAI Codex assisted in developing the argument, checking sources, and drafting and reviewing the manuscript. Review during preparation was by AI. This is a complete solution claim submitted for independent mathematical review; no human or formal verification is claimed. No separate detailed AI review report is submitted. Catalogue classification is left to maintainer review.

Author: Kaiwen Jin. Manuscript contact: [yui.ui.siki@gmail.com](mailto:yui.ui.siki@gmail.com).
