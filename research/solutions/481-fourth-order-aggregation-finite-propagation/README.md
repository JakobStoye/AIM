# AIM 481: finite propagation in fourth-order aggregation–diffusion

**Status: solution claimed; independent mathematical review requested.**

This package contains a complete analytic proof for [AIM problem 481](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/481-fourth-order-aggregation-finite-propagation.md), at repository revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`. Theorem 1.1 covers every integer dimension $`d\ge2`$, every $`\chi>0`$, and every compactly supported nonnegative $`H^1(\mathbb R^d)`$ probability density. It constructs one global weak curve with the requested moment, Sobolev and integrated-identity properties, whose support stays in one finite ball throughout each finite time interval.

The claim concerns a selected solution. It supplies no uniqueness theorem for the fourth-order weak equation or quantitative growth law for the support radius. The exact clause-by-clause comparison is in [TARGET_COMPARISON.md](TARGET_COMPARISON.md).

## Manuscript

- [Complete manuscript, 18 pages](paper/main.pdf).
- [Editable, self-contained LaTeX source](paper/main.tex).
- [AI-use and review disclosure](AI_USE.md).
- [File manifest](PUBLIC_MANIFEST.json) and [SHA256 checksums](SHA256SUMS).

Author: Kaiwen Jin. Contact: yui.ui.siki@gmail.com.

## Rebuild

With a standard LaTeX installation and latexmk:

```sh
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The source includes its bibliography and has no additional manuscript inputs. It was checked with pdfTeX from TeX Live 2025 and latexmk 4.86a. This is a purely analytic result: the argument uses no numerical experiment or computed certificate.

## Review scope

Substantial AI assistance was used for exploration, proof drafting, source checking and exposition. Two fresh AI contexts supplied a reader report and a referee-style report on one frozen draft; the manuscript was then revised. These checks do not constitute independent human review or formal verification. No separate detailed AI review report is included. Repository acceptance and independent mathematical assessment remain pending.
