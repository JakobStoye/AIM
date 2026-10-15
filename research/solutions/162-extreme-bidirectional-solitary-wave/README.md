# An extreme solitary wave for the bidirectional Whitham system

Kaiwen Jin — yui.ui.siki@gmail.com

This note proposes an affirmative resolution of
[AIM 162](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/162-extreme-bidirectional-solitary-wave.md)
at statement revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.
Theorem 1.1 constructs one positive, even, continuous solitary velocity profile
for the exact multiplier `tanh(xi)/xi`. The profile is smooth away from its
crest, strictly decreases to zero on the positive half-line, and reaches the
first critical height of the cubic traveling-wave equation. The reconstructed
surface and velocity solve both conservative equations in distributions and
classically away from the crest.

The construction passes from positive highest periodic waves with arbitrarily
large periods to the real line. A common continuity modulus and a fixed drop
from the critical height retain a nonconstant limit. A balance identity using
the kernel's finite first absolute moment excludes a positive limiting tail
without requiring an integrable profile. The result concerns existence at one
limiting speed; uniqueness, stability and an all-speed family are not claimed.

- [Complete manuscript, PDF](paper/manuscript.pdf)
- [Editable LaTeX source](paper/manuscript.tex)
- [Target comparison and source roles](TARGET_COMPARISON.md)
- [Payload manifest](PUBLIC_MANIFEST.json) and [SHA256 checksums](SHA256SUMS)

## Build

Run `make pdf` from this directory. The rebuilt PDF is
`build/manuscript.pdf`; the supplied PDF is `paper/manuscript.pdf`.
The source is self-contained, with an inline bibliography and no external
figures or data. It requires `latexmk`, `pdflatex` and the standard TeX packages
listed in the source. Compilation was checked with latexmk 4.86a and TeX Live
2025, with shell escape disabled. PDF timestamps may differ on rebuilding.

The argument is analytic. No numerical experiment, computational certificate
or formal proof project is needed to reproduce its mathematical claims.

## AI use and review

OpenAI Codex assisted extensively with exploration, proof drafting, source
inspection and manuscript preparation. Two additional AI contexts from the
same provider supplied a reader report and a referee report on an anonymous
draft, followed by one revision. These were AI reviews on a shared host.
The final manuscript includes its AI-use disclosure. No separate detailed
review report is submitted; independent mathematical review is requested.

`PUBLIC_MANIFEST.json` describes the five payload files. `SHA256SUMS` also
binds that manifest; the checksum file does not hash itself.
