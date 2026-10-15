# AIM 461: proposed comparison counterexample

Kaiwen Jin — yui.ui.siki@gmail.com

[Manuscript](paper.pdf) · [Editable source](paper.tex) · [Target comparison](TARGET_COMPARISON.md)

Theorem 1 gives a negative answer to the specified comparison implication for
every dimension n >= 2, every 1/2 < s < 1, every positive normalization C_s,
and every finite T > 0. A bounded radial viscosity subsolution and supersolution
have the same smooth compactly supported initial data, attained uniformly,
but cross at a positive time before T. The proof is analytic and self-contained
apart from standard Fourier inversion and integration theorems.

The convention matters: zero-gradient upper tests use the supremum of symmetric
directional integrals, and lower tests use the infimum, with each test patched
to the tested function outside its local spatial neighborhood. This result
concerns that convention. It does not construct two distinct full solutions.

The original target is [Problem 461 at revision a153f469ee0ea64e876b2ad97c79d252c19a3e22](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/461-infinity-fractional-evolution-comparison.md).

## Rebuild

With a standard TeX Live installation containing the packages named in the
source, run in this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex
```

No numerical computation or code certificate is a premise of the result.
Compilation checks the document build, not mathematical correctness.

## AI use and review

OpenAI Codex assisted with the construction, proof development, source checks,
and writing. The argument and manuscript received internal AI checks, including
fresh-context AI reading and referee feedback on one draft, followed by one
AI-assisted revision. These are AI checks on a shared host, not independent
human review.
No separate detailed AI review report is submitted. Independent mathematical
review is requested; posting does not establish novelty or repository acceptance.

The manifest records the four substantive files. Its own bytes and the checksum
file are excluded from its entries to avoid self-reference. SHA256SUMS covers
those four files and PUBLIC_MANIFEST.json. Catalogue classification is left to
maintainer review.
