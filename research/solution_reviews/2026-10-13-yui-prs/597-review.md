# AIM 597 — independent review of PR 68

- Date: 2026-10-13; submission: [PR 68](https://github.com/MColbrook/AIM/pull/68), Kaiwen Jin.
- Reviewed head: `6af624cf8fca3a9197fbf70ba82938b610e23cb7`.
- Proof: [PDF](../../solutions/597-entropy-chain-rule-lipschitz/paper/manuscript.pdf), [source](../../solutions/597-entropy-chain-rule-lipschitz/paper/manuscript.tex).
- Reviewer: independent Codex agent, separate from drafting/self-review; AI natural-language mathematical audit. No human or Lean certification.
- Verdict: **Solved**, exact prescribed-flux entropy chain rule on every bounded Lipschitz domain under the original estimates.

## Target and full proof check

The theorem preserves weak $`L^1`$ continuity at every time, fixed positive mass, the exact no-flux weak formulation, finite initial entropy and the weighted Fisher/action estimates. It permits vacuum and imposes no density bound, convexity, boundary smoothness or smooth-gradient approximation assumption. Its all-endpoint identity implies the requested absolute continuity and almost-everywhere derivative with the original prescribed flux.

Independently reconstructed the local lemma (lines 141–247). Writing $`v=\sqrt r`$ gives $`\nabla r=2v\nabla v`$ in $`L^1`$. The gradient vanishes on vacuum, and finite action makes the flux zero there. Weighted Cauchy–Schwarz bounds the squares of both normalized convolved factors by convolutions of their integrable original squares. Spatial differentiation almost everywhere at almost every time gives convergence off vacuum; the same bound gives convergence to zero on vacuum. Convolution in spacetime $`L^1`$ makes these square bounds uniformly integrable, hence the normalized factors converge strongly in local spacetime $`L^2`$. Their pairing converges in $`L^1`$. For fixed regularization, weak continuity and uniform mass give continuous spatially smooth densities and the distributional equation gives time absolute continuity in each compact smooth norm, so the ordinary truncated chain rule is legitimate. At each individual endpoint, spatial approximate identities converge in $`L^1`$ and the truncated entropy is Lipschitz. Bounded continuous truncated derivatives control the other flux term. Thus the local identity holds at every actual endpoint, not just almost every time.

The weak no-flux equation extends to ambient Lipschitz spatial tests by mollification: gradients remain bounded and converge almost everywhere in the domain, allowing dominated convergence against the $`L^1`$ flux. Its scalar time representative agrees at every time by weak continuity. In a Lipschitz graph chart the reflected density is even and the flux transforms by the derivative matrix

```math
A=\begin{pmatrix}I&0\\2\nabla g^T&-1\end{pmatrix},\qquad A^2=I.
```

This volume-preserving bi-Lipschitz involution preserves weak density continuity, bounds both energy factors, and gives $`\nabla\sqrt r(Rx)=A^T\nabla\sqrt\rho(x)`$. Folding compact tests proves the continuity equation across the chart boundary without assuming a normal trace for the rough flux. Its production pairing is invariant: $`(AF)\cdot(A^T\nabla u)=F\cdot\nabla u`$ because $`A^2=I`$. Orthogonality is not required. Reflecting the partition cutoff by the same map makes its pairing invariant too. The local identity therefore reduces to the upper-half identity. Summing the ambient partition cancels its gradient terms while the logarithmic derivative is still bounded; no unproved integrability of $`F\log\rho`$ is used.

The entropy truncations are nonnegative and increase monotonically to $`r\log r-r+1`$, including at zero. Their production is dominated by the product of the two $`L^2`$ factors. Taking the initial endpoint first proves finite entropy at every later time, then subtracting endpoint identities gives the all-time formula. The bounded potential contributes its weak continuity-equation identity. The exact weighted identity $`2\nabla\sqrt\rho+\sqrt\rho\nabla V=2\sqrt\pi\nabla\sqrt{\rho/\pi}`$ proves integrability of the final production and absolute continuity. All limit orders and vacuum conventions match the target.

## Every reference checked

- Cancès–Monsaingeon–Natale, Numerische Mathematik **158** (2026), 1513–1563, [DOI](https://doi.org/10.1007/s00211-026-01537-3), [primary cited v1](https://arxiv.org/html/2410.03367v1): authors/title and exact weak formulation/Fisher definitions match; its Proposition A.1 and convex-domain context are accurately distinguished.
- Casteras–Flaim–Monsaingeon, [arXiv:2512.05826v2](https://arxiv.org/html/2512.05826v2): title/authors/version and September 16, 2026 revision match. Its smooth nonconvex chain rules and the discussion leaving Lipschitz extensions open are background, not a theorem with silently dropped assumptions.
- Erbar–Meglioli, [arXiv:2408.05987v2](https://arxiv.org/html/2408.05987v2): title/authors/version match; its Dirichlet boundary dissipation functional and chain rule are correctly distinguished from this no-flux target.
- Hajłasz, *Sobolev spaces, theory and applications*, Jyväskylä summer course (1998), [author PDF](https://sites.pitt.edu/~hajlasz/Notatki/jyv-98c.pdf): downloaded and text-inspected after the browser fetch failed. Theorem 18 is the ACL characterization, Corollary 21 is vanishing gradient on a constant measurable set, and Theorem 31 is the bi-Lipschitz $`W^{1,p}`$ composition/chain rule, exactly as invoked. The reflection meets those hypotheses.

No missing essential reference, hidden regularity assumption or invalid reflection step remained.

## PDF and decision

Coordinator parsed/rendered all six pages; independently inspected the complete contact sheet. The theorem, local identity, boundary reflection, limiting formula and bibliography are complete and unclipped. Recommend accepting the package and marking **Solved**, recording independent AI review rather than human/Lean certification.


The package README and target comparison, including their AI-use disclosures, were also read. Their mathematical scope agrees with the manuscript and the original target; they introduce no separate executable proof or numerical certificate as a premise. Package hashes and repository integration are separate coordinating checks.
