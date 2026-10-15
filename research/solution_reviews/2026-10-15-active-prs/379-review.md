# AIM 379: independent audit of PR #149

Date: 2026-10-15. Reviewer: independent OpenAI Codex AI context; no human or Lean verification is claimed.

Pinned submission: [a9c98123bb0710a93ebaf1422f62b631e776189a](https://github.com/MColbrook/AIM/pull/149), compared with the original a153f469ee0ea64e876b2ad97c79d252c19a3e22 target and current problem page.

**Decision:** Solved. Universal strong-KPP uniqueness fails on a uniformly smooth connected unbounded domain in dimension 21.

**Scope:** The entire manuscript, bibliography, package README, target comparison, AI disclosure and ancillary build/manifest material were read. The analytic proof was independently reconstructed; submission-internal AI reviews were not treated as evidence of correctness. Every submitted PDF page was visually inspected in the maintainer-rendered contact sheets. No clipping, missing mathematics, unreadable glyphs or broken cross-reference was found. Package hash and independent rebuild results are recorded separately by the maintainer.

Theorem 1 supplies one admitted dimension, a homogeneous bounded C^(1,1/2) reaction, a uniformly C^(2,1/2) domain and the admitted Dirichlet parameter beta=0. A single such instance refutes the original universal assertion. It does not classify the other dimensions or Robin parameters.

I recomputed the radial amplitude and transverse-mode residuals in Lemma 3. For q=10^12+|x|^2, k=1-24/q, the corrected slow subsolution q^-1(phi+20000 q^-2 phi^2) overcomes the boundary-sign error that the uncorrected first mode would have. The two regimes phi<=1/4 and phi>=1/4 give positive residual with the displayed constants. B q^-2 phi is a supersolution for every B>0. The normal derivative of the slow barrier has the sign needed for its zero extension to be a weak subsolution.

The compact enlargement of the strip contains the stated large cube. Monotone exhaustion first gives U bounded below by q^-1 on the middle plane. A fixed compact collar bounds its boundary quotient, so one finite B makes the fast supersolution dominate U there. Taking the minimum outside that collar produces a global supersolution W decaying as Bq^-2. A small first cube eigenfunction, extended by zero with the correct derivative sign, gives a nonzero compact subsolution below W. A second exhaustion yields T<=W. At sufficiently large fixed q, U>=q^-1>Bq^-2>=T, giving two solutions of the same equation on the same domain.

Lemma 2 establishes the weak minimum and zero-extension properties and bounded-domain monotone iteration. The trace and local elliptic estimates apply on fixed true-boundary graph patches; diagonal convergence preserves the entire zero boundary. The two global graph components have bounded derivatives and a uniform positive separation, which supplies the required common chart radius. The above-one reaction extension matches its first derivative and has globally bounded Lipschitz derivative.

The precise original questions in [Berestycki–Graham](https://arxiv.org/abs/2212.06611v1), Conjecture 1.3, and their [2026 article](https://doi.org/10.1007/s00205-026-02168-6) are credited. [Rossi–Tough](https://arxiv.org/abs/2610.17121v1) is contextual: its locally analytic shrinking-obstacle domains are not assumed to have uniform charts. Standard weak Dirichlet solvability, local boundary estimates and Sobolev truncation tools are used in the classical uniformly elliptic constant-coefficient setting. No numerical evidence replaces the barrier estimates.
