# Local no-slip Navier--Stokes equations under stochastic parabolicity

**Maintainer review, 15 October 2026: partial progress.** Section 3.3 invokes the original KKW comparison theorem without the compatible fractional right-inverse estimates required by the 2013 Kunstmann--Weis erratum. The full local existence and continuous-dependence claim is therefore not established by this submission. The [independent AI review](../solution_reviews/2026-10-15-active-prs/458-review.md) records the precise gap, verified uniqueness for existing solutions, and the zero/small-noise cases. The original argument below is retained as a proposed proof.

Kaiwen Jin, 16 October 2026.

This package submits a complete analytic solution claim for [AIM Problem 458](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/458-stochastic-navier-stokes-no-slip-local.md), fixed target revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`. It awaits independent mathematical review.

Theorem 1.1 treats every bounded smooth three-dimensional domain, every positive viscosity, and every finite smooth solenoidal boundary-tangent noise family satisfying the stated stochastic parabolicity condition. It asserts an adapted local solution with an almost surely positive lifetime, continuity in the requested Besov space, the requested time-integrated no-slip Sobolev regularity, uniqueness throughout that path class, and continuous dependence in probability after common stopping. No additional noise-amplitude smallness or interior rank restriction is imposed.

- [Submitted manuscript with maintainer note, PDF](paper/paper.pdf).
- [Editable LaTeX source](paper/paper.tex).
- [Requirement-by-requirement comparison](TARGET_COMPARISON.md).
- [Content manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS).

The linear argument combines explicit channel and full-torus models with localization through the Stokes energy form, negative-order pressure estimates and a quantitative square-root comparison. An adapted cutoff and stopped energy argument give the nonlinear conclusions. All arguments needed for the claim are in the manuscript and its public cited sources. This is a pure analytic contribution; no numerical experiment, computer-assisted certificate or formal proof is asserted. The broader rough or infinite-noise no-slip problem and global three-dimensional regularity are outside its scope.

## Rebuild

With a standard LaTeX installation and `latexmk`, run from `paper/`:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex
```

The source requires only standard LaTeX packages and no additional assets. The submitted PDF was built with pdfTeX from TeX Live 2025; its final log has no unresolved citations/references or layout warnings. All 20 pages were read and visually checked. These artifact checks do not certify the mathematics.

## AI use and review

OpenAI Codex was used extensively for developing the argument, checking sources, drafting and author checks. Two additional fresh Codex contexts reviewed the same fixed earlier draft, one as a reader and one as a referee, without the author checks or each other's report. The author revised their local exposition findings and checked the final version. These were same-provider AI checks on a shared host, not human peer review or formal verification. No separate detailed AI review report is submitted. Independent mathematical review is requested.
