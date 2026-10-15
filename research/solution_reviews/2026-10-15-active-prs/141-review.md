# AIM 141: independent audit of PR #141

Date: 2026-10-15. Reviewer: independent OpenAI Codex AI context; no human or Lean verification is claimed.

Pinned submission: [bc5fd6bac773c5e925e18853bfc4b647fe22a090](https://github.com/MColbrook/AIM/pull/141), compared with the current problem page and its cited a153f469ee0ea64e876b2ad97c79d252c19a3e22 statement.

**Decision:** Solved. A fixed five-dimensional polynomial STLC system has no finite jet guaranteeing STLC with the same bounded controls.

**Scope:** The entire submitted manuscript, package README, target comparison, disclosure and build instructions were read. This mathematical report is separate from the maintainer package checksum, rebuild and PDF-render records; it does not claim visual checks that have not been recorded.

The target quantifies over all analytic systems in dimensions at least three. One fixed example in dimension five therefore suffices. The original system is fixed before choosing the Taylor order, its drift vanishes at zero, its two controlled fields remain constant, and the perturbation is polynomial with identical complete N-jet.

The dependency on the previous AIM 417 manuscript was checked by reading its full source, rather than relying on its catalogue badge. Its quartic identity follows from integrating $`ff''f'^2`$; the logarithmic estimate follows from two truncated absolutely continuous weights, with the low-energy part at most half of $`A`$. The concentrating $`s^{3/4}`$ profile has logarithmically growing fourth-power derivative integral and constant critical energy, and its endpoint corrections and amplitude rescaling give both signed closed loops with bounded controls. The Gram-matrix steering of the remaining four coordinates compensates the continuous fourth displacement, giving an actual Euclidean neighborhood, rather than merely two axis directions.

For the new perturbation, let $`a=\max|g|`$ on any trajectory returning the other coordinates to zero. If the original negative contribution could dominate the critical energy, the logarithmic estimate forces $`A<T^9e^{-1/(6a)}/4`$. A 1-Lipschitz excursion attaining height $`a`$ costs at least $`a^{2k+1}/(2k+1)`$. The exponential bound by $`(2k)!6^{2k}a^{2k}`$, followed by $`a\le T`$, makes that cost dominate for all sufficiently small durations, uniformly over every measurable control. The remaining degenerate cases have nonnegative displacement directly. Taking the union over all durations at most the given time cannot reach any negative fourth-axis point. This establishes non-STLC, with no trajectory-selection or switch-count assumption.

References: Jafarpour v7, Conjecture 1.1 on PDF p.3, was checked against the actual universal finite-jet question; its polynomial-growth theorem is background, not an extra premise. The Jin versioned proof was reconstructed as above. Hunter Appendix 3.A supplies the standard absolutely continuous integration calculus used in both notes. No missing nonstandard theorem is used. The manuscript expressly avoids claiming a classification in dimensions three and four.

**PDF visual check:** Every submitted PDF page was subsequently inspected in the maintainer-rendered contact sheets. No clipped content, missing mathematics, unreadable glyph or broken cross-reference was found. The independent rebuild and checksum evidence is recorded separately.
