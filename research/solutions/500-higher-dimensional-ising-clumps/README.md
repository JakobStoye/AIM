# AIM 500: a four-dimensional counterexample

This package presents a counterexample to the all-dimensional extension in
[AIM Problem 500](https://github.com/MColbrook/AIM/blob/1b7c7fd251c1643bb41f0e3cef38704bcef410fd/problems/500-higher-dimensional-ising-clumps.md),
at revision `1b7c7fd251c1643bb41f0e3cef38704bcef410fd`.

For the stated cube-supported strong-deformation-retraction moves, every
regular four-dimensional clump is a PL manifold with boundary, and each
permitted move preserves the boundary's homeomorphism type. A contractible
four-manifold with nontrivial boundary fundamental group can be realized as
an admissible finite lattice-cube union containing the pinned cube. It cannot
communicate with the singleton cube, whose boundary is a three-sphere.
The chain is therefore reducible in dimension four for every positive choice
of the stated rates.

- [Complete manuscript (PDF)](paper/cube_dynamics.pdf)
- [Standalone LaTeX source](paper/cube_dynamics.tex)
- [Comparison with the full original target](TARGET_COMPARISON.md)
- [SHA-256 checksums](SHA256SUMS)

The argument uses Lickorish's embedded contractible four-manifold and
Boege--Hinojosa--Verjovsky's hypersurface cubulation theorem. The manuscript
proves the intervening local-link, attachment, boundary-preservation,
whole-cell realization and exact regularity statements. All source identities
and theorem locators are given in the paper. This is an analytic existence
argument; it does not supply explicit cube coordinates, numerical evidence,
or a formal proof project.

Status: AI-assisted natural-language proof claim submitted for mathematical
review. Codex checked the complete argument and cited-source applicability; a separate fresh Codex context reviewed the full manuscript and original-target correspondence, finding one minor citation-placement issue and no major objection. The final citation repair and two wording clarifications were checked by the authoring context. No independent human review, formal verification
or repository acceptance is claimed. The separate dimension-three question
is left open. If the all-state size-weighted law is normalizable, the paper
also explains why the chain started at the singleton cannot converge to it;
normalization and nonexplosion themselves are not refuted.

To rebuild with a standard TeX installation and `latexmk`:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=paper paper/cube_dynamics.tex
sha256sum -c SHA256SUMS
```

The checksums identify the supplied files. A regenerated PDF can have a
different hash because of TeX versions and creation metadata. The supplied
PDF was compiled and all seven pages were inspected. The source uses only
standard TeX packages and has no external assets or private inputs.

Author: Kaiwen Jin. Manuscript contact: yui.ui.siki@gmail.com. The paper
contains an AI-use statement.
