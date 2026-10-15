# AIM 042: selected bidiagonal singular directions

**PR:** [161](https://github.com/MColbrook/AIM/pull/161). **Reviewed head:** `951b78861d0a47ad35322f10454e51614d7691dd`. **Date:** 2026-10-15. **Decision:** Solved in the manuscript's explicitly specified fixed-format floating-arithmetic model.

Independent OpenAI Codex AI audit in the receiving repository. The complete fifteen-page manuscript, target comparison, README, manifests, table and figure were examined. This is an argument audit, with finite software checks separately identified; it is not human review or Lean verification.

[Proof](../../../research/solutions/042-selected-bidiagonal-directions/paper/main.pdf).

The target is selected ordered ranks for a real upper bidiagonal matrix, including reducible, singular and repeated-value cases, with both residual equations and separate orthogonality. The construction supplies those guarantees with constant128 for represented unit directions and256 for raw carriers. A carrier represents its exact normalized direction; the raw floating array has the separately stated norm defect. The arithmetic model fixes binary64 storage and16–53 target bits, assumes correctly rounded primitives and protected indices/scaling, and excludes overflow/underflow. Its work is explicitly O(p^4 nk) on O(p)-bit numbers, or a conservative O(p^6 nk) bit bound. O(nk) is the fixed-format dimension/count bound. There is no precision-uniform or practical-speed claim.

## Reconstruction

Scaling puts the Gram matrices in a fixed interval without rounding them at binary64 precision. The softened tridiagonal inertia count brackets an exact count by a diagonal perturbation; its possible nonmonotonicity does not invalidate the separated population search. Halving the populated interval gives a safe gap in logarithmically many count calls. Cached boundaries group only requested ranks, so a large spectral population does not require computing all its vectors.

The rational sign iteration has a finite uniform conditioning phase and a quadratic final phase. The inverse-branch partial fractions have positive weights and controlled pole clearance. Their coefficient and Gram-rounding bounds produce one common nearby positive filter. Its harmless positive rescaling preserves all selection scores and normalized columns. The selected shorting pivots are bounded below through the trace-of-inverse recurrence. Projector comparison controls every selected column without full vector reorthogonalization.

The semiseparable forward and reverse recurrences retain the complete inverse-square diagonal, including previously selected indices. The segment Woodbury identity, applied on a complex disk, bounds propagation and its derivative uniformly over an entire segment. This prevents an exponential-in-n accumulation of local errors. The stated local budgets fit the conservative precision67584+2880p. Normalized inner products and the streaming solves then give the claimed inner Gram accuracy.

The positive branch uses a normalized matrix image, while the near-zero branch selects left and right bases separately at one common spectral cut. In mixed left products, retaining the small norm of the near-zero left image cancels the apparent inverse-threshold loss; a crude operator-norm replacement would not suffice. Finite recovery and final component rounding preserve nonnegative values, requested-rank accuracy, both residuals, both orthogonality estimates and the raw norm-defect bound. These estimates were recomputed, including the zero-input and multiplicity cases.

## References and software evidence

All six references were checked at primary sources. Amsel et al.v3 identifies Problem3.8; Großer–Lang's2003 article and the2018 Marques–Demmel–Vasconcelos working note concern the relevant coupling difficulty, rather than proving this construction. Axler's fourth-edition Theorem7.29 is the real spectral theorem. Sutherland's2025 Lecture16 Theorem16.26 is Cauchy's formula, with the derivative consequence immediately following it. Boost1.89 documentation is implementation context for the declared primitive model, not a formal compiler certificate.

The external research implementation was checked out at immutable revision `627f07a898376e12ddba1e40d1d84c0610af639a`. Its26 tests passed in isolated Linux with Boost1.89 headers. All six fixed configurations (two matrices, auto/proof/diagnostic) were freshly replayed, and every exact rational instance checker passed. These small cases corroborate the implementation; they do not establish the universal theorem or its complexity. Runtime observations differ from the author's machine and are not substituted for asymptotic evidence.

The standalone manuscript rebuilt successfully and its text matched the submitted PDF. All fifteen rendered pages, the table and the residual figure were visually inspected. No unresolved mathematical gap was identified in the stated model.
