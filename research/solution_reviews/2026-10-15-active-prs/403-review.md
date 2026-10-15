# AIM 403: independent audit of PR #160

Date: 2026-10-15. Reviewer: independent OpenAI Codex AI context; no human or Lean verification is claimed.

Pinned submission: [1957fa687fa60c26c51fd16017b91f43c4e60e14](https://github.com/MColbrook/AIM/pull/160), compared with the current problem page and its cited a153f469ee0ea64e876b2ad97c79d252c19a3e22 statement.

**Decision:** Solved. The norm control cost has liminf T log C_S(T,L) at least L^2/pi, strictly excluding the proposed L^2/4 coefficient.

**Scope:** The entire submitted manuscript, package README, target comparison, disclosure and build instructions were read. This mathematical report is separate from the maintainer package checksum, rebuild and PDF-render records; it does not claim visual checks that have not been recorded.

The boundary sign and normalization were independently derived from the smooth single-mode transposition pairing. For an exactly H-minus-one unit first sine mode, all null controls necessarily have one fixed nonzero first moment and zero higher moments. After modulation and centering, their entire transform F satisfies F(0)=1, zeros at $`\pi^2(n^2-1)/L^2`$, and growth at most $`K_Te^{T|\mathop{\rm Im}z|/2}`$. The initial-state normalization changes only a positive constant independent of T.

Jensen's formula on circles gives the angular growth contribution Tr/pi because the integral of absolute sine is four. Extra zeros can only strengthen the lower bound. Radii containing zeros are handled by limits of zero-free radii and a fixed finite selected sum, avoiding any boundary-zero assertion. At radius $`\pi^2N^2/L^2`$, the prescribed product is exactly $`(N-1)!(N+1)!/2`$. The elementary logarithmic factorial estimate gives $`\log K_T\ge2N-4\log N-2-\pi TN^2/L^2`$. Choosing the floor of $`L^2/(\pi T)`$ loses at most one half in the exponential and yields the stated positive constant times $`T^{7/2}e^{L^2/(\pi T)}`$ for the whole small-time interval.

Taking the infimum over controls and then the original full unit-sphere supremum is legitimate because a single unit initial state supplies a lower bound; the proof consistently uses the control norm, not its square. No upper-cost theorem is needed for the contradiction to the proposed coefficient.

The primary 2025 Lissy source Sections 3.1–3.2 was checked and uses precisely complex H-minus-one initial states and L2 Dirichlet controls, with the stated conjecture and upper comparison. Miller's paper is historical context. Lissy's 2015 author manuscript is cited only for the old lower comparison; its direct host was unavailable in this audit, but the same lower coefficient is explicitly confirmed in the accessible 2025 primary source. The finite entire-function proof supplies its own normalized Jensen formula and needs no unverified specialized input. This access limit concerns the historical locator, not the new bound.

**PDF visual check:** Every submitted PDF page was subsequently inspected in the maintainer-rendered contact sheets. No clipped content, missing mathematics, unreadable glyph or broken cross-reference was found. The independent rebuild and checksum evidence is recorded separately.
