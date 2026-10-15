# AIM 474: independent audit of PR #157

Date: 2026-10-15. Reviewer: independent OpenAI Codex AI context; no human or Lean verification is claimed.

Pinned submission: [8a377b721755a4909aa7608b893abf0cc9c03c41](https://github.com/MColbrook/AIM/pull/157), compared with the original a153f469ee0ea64e876b2ad97c79d252c19a3e22 target and current problem page.

**Decision:** Solved. Every admitted complete manifold and positive point mass has a nonnegative distributional fractional porous-medium solution with the required positive-time continuity and initial trace.

**Scope:** The entire manuscript, bibliography, package README, target comparison, AI disclosure and ancillary build/manifest material were read. The analytic proof was independently reconstructed; submission-internal AI reviews were not treated as evidence of correctness. Every submitted PDF page was visually inspected in the maintainer-rendered contact sheets. No clipping, missing mathematics, unreadable glyphs or broken cross-reference was found. Package hash and independent rebuild results are recorded separately by the maintainer.

Theorem 1.1 covers the exact geometry, spectral fractional operator, all m>1, 0<s<1, every source point and every positive mass. It constructs one C((0,infinity);L1) solution, with the requested supremum-of-mass condition. It does not presume uniqueness or all-time mass conservation.

The bounded-data semigroup estimates give a mass bound, local smoothing and an integrable near-zero nonlinear flux bound F_A(t) tending to zero. The implicit Euler equation also gives the positive-time energy for u^m in the fractional form domain and the time derivative in its dual. These identities are established before taking point-source limits.

The new heat-average tests f_(H,j)=H^-1 integral_0^H P_r chi_j are bounded between zero and one, vanish at infinity, tend to one on compact sets and have fractional generator bounded by C H^(-s), uniformly in j. Pairing the Euler identity with them gives spatial tightness uniformly over the concentrating data and the entire finite time horizon. It does not assume the mass-conservation conclusion of the neighboring problem.

Positive-time compactness is obtained from monotone-power time shifts and the form-domain energy. The ordinary heat operator restricted to a compact set is Hilbert–Schmidt; finite-rank approximation and heat smoothing supply the actual local space-time compactness. At common good times, tightness upgrades local convergence to global L1. Nonlinear L1 contraction propagates Cauchy convergence uniformly to every later time, yielding one continuous positive-time curve. Strong L1 convergence of the powers on positive intervals passes the full nonlocal distributional term. The near-zero flux estimate gives the compact-test point trace, and tightness plus mass tending to A upgrades it to every bounded continuous test. No mass escapes at time zero.

The actual [Berchio–Bonforte–Grillo–Muratori primary text](https://arxiv.org/pdf/2109.10732v2), Assumption 2.1, Proposition 5.1, its Euler construction and Theorem 2.6(2.13), has exactly the semigroup and smoothing interface used. Smooth-domain Faber–Krahn implies its open-set convention by compact-test exhaustion. Grigor'yan's lower-Ricci stochastic-completeness criterion applies with the supplied comparison function. Euclidean measure-data results are credited as context, not substituted for this manifold limit. The nonlinear compactness, global convergence and all-test trace are proved here.
