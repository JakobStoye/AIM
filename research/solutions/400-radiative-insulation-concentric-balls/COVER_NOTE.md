# 400: proposed resolution — concentric balls for radiative thermal insulation

Submitted by Kaiwen Jin for [AIM problem 400](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/400-radiative-insulation-concentric-balls.md), at target revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

Theorem 1.1 of the submitted manuscript presents an affirmative analytic proof of the full constrained concentric-ball inequality for the stated radiative potential. It covers every n >= 2, beta > 0, gamma >= 0 and R > 1, every bounded Lipschitz outer set and measurable heated set of the prescribed volume, and every allowed upper bound on total volume. The comparison includes outer radius 1 and unused insulation.

The proof rearranges the boundary potential, retaining its full singular variation. Section 3 obtains the radial lower cost. Section 4 constructs finite-jump upper approximations and removes their interior jumps by concavity when the whole tail potential is multiplied. The resulting competitor belongs to the original H1 problem on a concentric ball. Lemma 2.1 includes continuity at the bare-ball endpoint and attainment of the radial minimum.

Materials in this package:

- [Complete manuscript](paper/main.pdf) and [editable source](paper/main.tex).
- [Target comparison](TARGET_COMPARISON.md).
- [Package manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS).

OpenAI Codex assisted with the argument, algebra, references and drafting. One AI reader and one AI referee reviewed an anonymized earlier draft in fresh contexts on a shared host. No separate detailed AI report is submitted; independent mathematical review is requested. The argument is analytic and does not rely on numerical evidence, a computational certificate or Lean formalization.

The selected source builds from the included files. Build success and internal AI review do not constitute mathematical certification or maintainer acceptance. Please review this as a complete solution claim. This package-only PR adds the linked materials; catalogue classification is left to maintainer review.
