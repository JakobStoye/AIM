# AIM 423: domain correction, with the intended spectral question remaining

**PR:** [136](https://github.com/MColbrook/AIM/pull/136). **Head:** `fb98d423513524bc2a4443454e5401a80a55d4c9`. **Date:** 2026-10-15. **Decision:** Partially resolved.

Independent Codex AI review in the maintainer's session, without preparation of the submission; no human or Lean verification is claimed. The complete three-page source/PDF, README and target comparison were examined against the current and pinned problem, the actual [Almog problem sheet](https://nsa.fjfi.cvut.cz/problems/04_AIM_2015/2015-02/2015-02_AIM_Almog_2.pdf) and the distinct [closed magnetic realization](https://arxiv.org/pdf/1410.5122v1). The package itself accurately discloses this limitation rather than asserting the intended spectral problem solved.

[Note](../../solutions/423-ordinary-sobolev-magnetic-airy-domain-clarification/paper/domain-correction.pdf).

## Verified argument

The compact packet at horizontal location R has width R to the minus one-half and carrier y-frequency R squared divided by two. After differentiation, cancellation with the vector potential leaves mismatch at most 9/32 times square-root R on its support. The displayed operator image has norm O(R) for each fixed c, whereas the ordinary y-derivative squared has its exact R-fourth/4 term. The real test functions eliminate the derivative cross term. All differential signs and scaling factors in the five-term image were recomputed.

For locations $`R_n=4^n`$ and coefficients $`R_n^{-3/2}`$, supports and their images are disjoint and locally finite. The functions converge in L2 with squared tail of order the sum of $`4^{-3n}`$, and their operator images converge with squared tail bounded by the sum of $`4^{-n}`$. The distributional image of the limit is the latter L2 function. Its ordinary y derivative cannot be square integrable: its squared norm would dominate one quarter of the divergent sum of $`4^n`$. Thus the stated ordinary H1_0 restriction is genuinely nonclosed, at every fixed real c, including all nonzero intermediate values. This failure occurs away from the Dirichlet boundary.

A bounded everywhere-defined inverse of a bijective shift would force the original graph closed, by passing limits through that inverse. Consequently the nonclosed restriction has empty bounded-inverse resolvent and spectrum equal to the complex plane under the explicitly stated convention. This is not a claim that every point is an eigenvalue.

## Why this is partial progress

The graph-limit argument concerns the literal ordinary Sobolev domain printed in the target. It does not concern the natural closed Dirichlet operator built from covariant magnetic derivatives and the potential-weighted form space. Replacing the ordinary derivative condition changes the operator. In particular, Section 3 of the note explicitly leaves the all-parameter spectral question for the closed realization unanswered. A convention-dependent spectrum for a nonclosed restriction cannot establish that intended missing intermediate-field theorem.

**Known cases:** Spectral nonemptiness for sufficiently small and sufficiently large nonzero field strengths remains the published result. The submission additionally proves that the printed ordinary H1_0 restriction is nonclosed for every fixed c, and explains the correct distinction from a closed magnetic Dirichlet realization.

**Remaining target:** Establish nonempty spectrum at every intermediate nonzero field strength for the natural closed magnetic Dirichlet realization. The submission proves no new parameter range for that operator.

## References and complete-content checks

All three bibliography entries are relevant. The actual one-page 2015 source uses the ordinary printed domain and states the small/large-field results. Almog--Helffer v1 defines the magnetic space and closed operator through equations (2.3), (2.4) and (2.24); the last explicitly requires the distributional image in L2 inside its form space. Brezis's density of compact smooth functions and uniqueness of locally integrable distributions are standard applications here; the note writes out the actual graph limit and resolvent argument, rather than importing a spectral theorem. No citation is being used to claim a missing closed-realization solution. All three rendered PDF pages were visually inspected and are legible and consistent with the source. Build/integrity receipts are maintained separately in integration.

## PR reply

This independent Codex AI audit verifies the explicit nonclosedness construction and its stated bounded-inverse-resolvent consequence. We are recording this as **partial progress/domain clarification**, rather than a full spectral solution: it concerns the printed ordinary H1_0 restriction, while spectral nonemptiness for the natural closed magnetic Dirichlet realization at intermediate nonzero field strengths remains unresolved. The problem will retain that remaining target, and the README/catalogue will preserve the distinction. No human or Lean verification is claimed.
