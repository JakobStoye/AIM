# AIM 405: a half-power kinetic vanishing-noise rate

**PR:** [127](https://github.com/MColbrook/AIM/pull/127). **Date:** 2026-10-15. **Decision:** Solved. Reviewed head: `70f61fc9f49ac9ac53f07333308710e0984fc892`.

Independent OpenAI Codex AI audit; no human or Lean verification is claimed. The whole source, seven-page PDF, README, target comparison and package records were checked against the pinned and current target.

[Proof](../../../research/solutions/405-kinetic-mfg-vanishing-viscosity-rate/paper/main.pdf).

The proof works on the full torus times unbounded velocity space, for every stipulated minimizing pair and every diffusivity in(0,1]. No strict positivity, classical optimizer or bounded velocity truncation is added. Both square density costs and the perspective convention at vacuum are preserved.

The bounded rational moment test gives uniform second moments without assuming their time-integrability in advance. The kinetic Gaussian has the stated covariance and intertwines transport plus velocity diffusion; Jensen decreases all three costs and preserves the original initial trace, proving the noisy minimum is at most the inviscid minimum.

For the reverse comparison, the time-dependent shear convolution commutes exactly with kinetic transport and velocity derivatives. Positivity, a Gaussian lower bound, and finite Fisher information justify the entropy identity for the smoothed pair. The cutoff boundary terms vanish by action and second-moment estimates on the full velocity space. Expanding the current-flux action gives the entropy difference with the correct sign and a nonpositive Fisher remainder. Initial entropy contraction and the Gaussian entropy lower bound give a smoothing-independent excess of at most L times diffusivity.

Removing convolution is essential before applying inviscid minimality. The fluxes are weakly compact in L^(4/3); completing a square against compact continuous fields proves weighted action lower semicontinuity and zero flux at vacuum. Density convergence passes the original initial/terminal traces and both square costs. Thus the original noisy density has an admissible inviscid flux with cost at most E0+L times diffusivity. The midpoint identity then gives squared spacetime and terminal L2 differences at most4L times diffusivity, establishing exponent1/2 uniformly in diffusivity and independently of dimension.

The four bibliography entries and their roles were checked. Tang–Zhang's published section7 question4(b) is kinetic. Griffin-Pickering–Mészáros v3 supplies the correctly identified variational background. Benamou–Carlier–Di Marino–Nenna v2 equations(2.9)–(2.10) give the elliptic action/entropy/Fisher identity credited here; the kinetic weak version is proved in the submission. Brezis's cited weak compactness, Sobolev calculus, density and Hilbert representation are applied under their actual hypotheses. No imported theorem assumes unproved regularity of the minimizers.

The source rebuilt and its extracted text matched the PDF. All seven pages were visually inspected; no broken reference or missing formula appeared. No unresolved gap was identified. Existence of the stipulated minimizers and optimality of the exponent are not additional claims of this resolution.
