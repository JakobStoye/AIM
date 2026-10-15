# AIM 467: independent audit of PR #153

Date: 2026-10-15. Reviewer: independent OpenAI Codex AI context; no human or Lean verification is claimed.

Pinned submission: [e8620ac7479efe6ff3de2e8fe2b963325886f82d](https://github.com/MColbrook/AIM/pull/153), compared with the current problem page and its cited a153f469ee0ea64e876b2ad97c79d252c19a3e22 statement.

**Decision:** Solved. For 1/2<s<1 and m>2 an existing bounded energy weak solution cannot have the requested global jointly continuous representative.

**Scope:** The entire submitted manuscript, package README, target comparison, disclosure and build instructions were read. This mathematical report is separate from the maintainer package checksum, rebuild and PDF-render records; it does not claim visual checks that have not been recorded.

The original assertion is universal over the given parameters and all bounded energy weak solutions. The strict admissible subrange $`1/2<s<1`$ suffices to refute it, provided existence in the exact full energy class is checked. Stan–del Teso–Vázquez's Theorem 2.2 in v3 supplies the same pressure and all-q energy inequalities with the exact coefficient and exponent. Their survey Theorem 5.1 and Remark 4 supply a global solution and initial-time estimates. Initial pressure energy is finite because N>2s.

The kernel derivative is locally integrable precisely in the used strict range; splitting at unit distance bounds the pressure gradient uniformly from the given L1/Linfinity norms. Thus the conservative flux obeys $`|F|\le Bu^{m-1}\le Vu`$. The moving halfspace test has the correct sign, uses only the exterior flux inequality, and spatial cutoffs disappear by global L1 flux integrability.

Assuming joint continuity, all supports on each finite slab are in a common compact box by that halfspace argument. Uniform time continuity makes the density at most epsilon outside any earlier supporting halfspace for a common short interval. The improved exterior speed is $`B\varepsilon^{m-2}`$. Summing on a finite partition and then sending epsilon to zero shows each of the 2N coordinate support extrema cannot increase. The modulus need only be uniform on each fixed finite slab, so no illicit infinite-time modulus is required.

The Fourier support coercivity proof was recalculated with its normalization: at most half the L2 mass can lie in the ball of radius determined by support volume. Conserved positive mass in a fixed box then bounds the dissipation of $`u^{(m+1)/2}`$ below by a fixed positive number at almost every later time. Its time integral contradicts the q=2 energy inequality.

Appendix A was checked to avoid a vacuous counterexample: smooth pairing traces plus weak L2 compactness define unique every-time slices, the halfspace argument gives common finite-slab supports, and bounded density lets arbitrary L-infinity tests be approximated in L1 on that support. Thus weak L1 continuity holds for one common representative. Lower semicontinuity and continuous cumulative dissipation extend each original energy inequality to every endpoint. The source assumptions exactly apply to the indicator datum. Caffarelli–Soria–Vázquez's DOI concerns the separately stated m=2 comparison. No claim for s<=1/2, a discontinuity at each time, or a particular interface location is needed or made.

**PDF visual check:** Every submitted PDF page was subsequently inspected in the maintainer-rendered contact sheets. No clipped content, missing mathematics, unreadable glyph or broken cross-reference was found. The independent rebuild and checksum evidence is recorded separately.
