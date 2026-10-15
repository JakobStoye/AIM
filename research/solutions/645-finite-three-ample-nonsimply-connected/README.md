# A finite three-ample complex with a nontrivial fundamental group

This package submits a finite existence construction for
[AIM 645](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/645-finite-three-ample-nonsimply-connected.md)
at problem revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

Theorem 1 gives a three-ample simplicial complex on 32,768 vertices, of
dimension at most three, with a simplicial retraction onto a four-cycle.
Its fundamental group therefore contains a copy of the integers.

Read the [manuscript](paper/finite_three_ample.pdf), its
[editable source](paper/finite_three_ample.tex), and the
[target comparison](TARGET_COMPARISON.md). The proof uses a finite product
of independent marks and a finite union bound; it does not depend on a
sampled instance, numerical code or a computer-generated certificate.
The vertex count is an upper bound from the construction, with no minimality
or efficient-search claim.

To build the standalone source with a standard LaTeX installation:

```sh
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error finite_three_ample.tex
```

The bibliography supplies primary sources and precise theorem/example
locators. SHA256SUMS and PUBLIC_MANIFEST.json identify the included files.

Author: Kaiwen Jin. Manuscript contact: yui.ui.siki@gmail.com.
OpenAI Codex assisted with developing the argument, source checks and drafting.
A complete draft also received a manuscript referee review and a separate
reader check from fresh OpenAI Codex conversations. These were same-vendor AI
checks in a shared workspace; no independent human review or Lean verification
is claimed. Independent mathematical review is requested. This package makes a complete
solution claim; catalogue classification and acceptance are for maintainer
review.
