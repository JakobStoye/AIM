# AIM 455: a deterministic Hölder exponent with smooth transport noise

This package presents a complete affirmative solution claim for [AIM Problem 455](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/455-smooth-transport-spde-deterministic-holder-exponent.md), at repository revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

For the entire stated class of scalar Itô variational equations on the torus, Theorem 1.1 gives a deterministic positive exponent on every compact positive-time strip. The Hölder norm may be random and unbounded. The proof allows merely measurable nonsymmetric diffusion, progressively measurable smooth transport coefficients, countably many Brownian motions and noncommuting vector fields.

Read the [complete manuscript](manuscript.pdf) and the [target comparison](TARGET_COMPARISON.md). The [LaTeX source](manuscript.tex) contains the full published argument. Its additional step beyond the cited stochastic-flow and De Giorgi class results is a local constant affine normalization of the continuous inverse flow derivative. The resulting neighborhoods may depend on the realization, while the normalized regularity exponent is fixed.

Author: **Kaiwen Jin**, contact **yui.ui.siki@gmail.com**. This is an analytic proof claim. Its preparation and internal natural-language checks used OpenAI Codex; the manuscript discloses that assistance. Automated checks and fresh-context AI feedback do not constitute human peer review, formal verification or acceptance by the receiving repository. Catalogue classification is left to maintainer review.

## Rebuild

From this directory, with a LaTeX installation providing the packages named in `manuscript.tex`:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error manuscript.tex
```

The supplied PDF was built with TeX Live 2025, pdfTeX 1.40.27 and latexmk 4.86a. The proof is analytic and has no numerical-code or data dependency. The bibliography is included in the source.

## Files and integrity

The complete package allowlist is `README.md`, `TARGET_COMPARISON.md`, `manuscript.tex`, `manuscript.pdf`, `PUBLIC_MANIFEST.json` and `SHA256SUMS`. The manifest records hashes of the four substantive artifacts. `SHA256SUMS` covers those four files and the manifest, excluding its own self-hash.

```sh
shasum -a 256 -c SHA256SUMS
```
