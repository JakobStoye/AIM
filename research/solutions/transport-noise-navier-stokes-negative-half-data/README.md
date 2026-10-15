# Transport-noise Navier--Stokes with negative-half Besov data

This package contains a proposed complete solution of
[AIM 457](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/457-stochastic-navier-stokes-negative-half-critical-data.md),
at target revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

Theorem 1.1 proves local well-posedness on R^3 for every deterministic
solenoidal initial velocity in the **inhomogeneous** space B^{-1/2}_{6,4},
for every prescribed finite smooth compactly supported solenoidal transport
family satisfying strict stochastic parabolicity. The heat-mild solution has
almost-sure C_t B^{-1/2}_{6,4} and L^4_t L^6_x regularity. Uniqueness holds
throughout that class, with initial-data continuity in probability in both
norms on common local intervals. No further noise or data smallness is assumed.

- [Complete manuscript](paper/paper.pdf)
- [Editable LaTeX source](paper/paper.tex)
- [Requirement-by-requirement target comparison](TARGET_COMPARISON.md)
- [Content manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS)

The proof uses the published linear stochastic Stokes maximal-regularity
result of Agresti and Veraar, with a separate nonlinear endpoint argument.
There is no numerical experiment, proof-critical computation, or code dependency.
The claim concerns local evolution in the stated spaces; it does not assert
global existence or an optimal initial-data space.

## Build

With a standard TeX Live installation and latexmk, from this package run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error paper/paper.tex
```

The only manuscript input is `paper/paper.tex`. The source uses standard
article, geometry, Latin Modern, AMS, mathtools, microtype and hyperref packages.
The distributed PDF is the reviewed author revision; compilation checks
artifact integrity and does not verify the mathematical proof.

## Contribution and review

Author: Kaiwen Jin. Contact: yui.ui.siki@gmail.com.
OpenAI Codex developed the argument and text, checked source applications,
and performed internal AI review and revision, including one fresh-context
reader and one fresh-context referee review of the same earlier draft.
These were same-vendor AI reviews on a shared host, without verified operating
system isolation. They are not independent human mathematical verification.
No separate detailed AI review report is submitted.

Evidence status: **Solution claimed**, pending independent mathematical review.
Posting this package does not imply acceptance by AIM or a journal.
