# AIM 461: independent audit of PR #154

Date: 2026-10-15. Reviewer: independent OpenAI Codex AI context; no human or Lean verification is claimed.

Pinned submission: [70a827b3bf2a2a810f7f378d6945dcce7e84def3](https://github.com/MColbrook/AIM/pull/154), compared with the original a153f469ee0ea64e876b2ad97c79d252c19a3e22 target and current problem page.

**Decision:** Solved. The specified relaxed infinity-fractional subsolution–supersolution comparison fails, even with identical smooth initial data.

**Scope:** The entire manuscript, bibliography, package README, target comparison, AI disclosure and ancillary build/manifest material were read. The analytic proof was independently reconstructed; submission-internal AI reviews were not treated as evidence of correctness. Every submitted PDF page was visually inspected in the maintainer-rendered contact sheets. No clipping, missing mathematics, unreadable glyphs or broken cross-reference was found. Package hash and independent rebuild results are recorded separately by the maintainer.

The convention in AIM461 is essential and is retained: at a zero gradient the upper-test inequality uses the supremum over symmetric directions, and the lower-test inequality uses the infimum, with local tests patched to the actual spatial tail. The theorem constructs a subsolution and a supersolution; it does not assert two full solutions or a failure for a stronger game operator.

The two thin annuli of width epsilon=10^-12 have centers at radii one and three. At radius two the radial fractional integral b is O(epsilon), whereas a tangent line meeting the inner annulus has an integral at least 2a, with a proportional to sqrt(epsilon). I checked the tangent geometry and endpoint estimates. The modification q=b+chi(a-b) has q>b only where the initial radial profile is zero and q is locally constant equal to a. This flatness makes the enlarged relaxed upper envelope applicable precisely where the chosen time derivative exceeds the radial value.

U=F+tQ-Mt^2 then satisfies the selected radial inequality outside that flat region and the tangent-direction upper inequality inside it, with one finite Hessian operator bound controlling all t errors. V is the radial lift of the even one-dimensional fractional heat evolution. Its Fourier formula has the given normalization and uniform initial trace. Every radial directional integral equals the one-dimensional value, including at noncentral critical radii; at the origin all directions agree. Hence V satisfies both relaxed envelopes. Comparing each patched smooth contact function with the tested smooth function transfers these pointwise inequalities to every viscosity test.

At 2e_1 the initial derivatives satisfy U_t=a>b=V_t. The explicit second-time-derivative remainder supplies a strictly positive crossing time below any prescribed finite T. Both functions are bounded and continuous on the full cylinder with the same uniformly attained compactly supported initial data.

The primary [del Teso–Endal–Jakobsen–Vázquez source](https://arxiv.org/html/2210.06414v1), Definitions 4.1 and 4.3, was checked for these exact weak zero-gradient envelopes. The [Bjorland–Caffarelli–Figalli paper](https://arxiv.org/abs/1011.1966v2) is credited for the related elliptic phenomenon, not substituted for this evolution construction. The Fourier inversion and the radial heat identity are proved with explicit constants in the submission. The argument covers every admitted n>=2 and 1/2<s<1.
