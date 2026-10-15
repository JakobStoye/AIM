# 241. Uniqueness of a hemispheric saddle profile on a magnetic sphere

**Area:** Curved-film micromagnetics

**Status:** 🟠 SOLUTION CLAIMED

**Last checked:** 2026-10-15

## Problem statement

For $`\kappa\geq4`$, consider the energy

```math
\mathcal E_\kappa(m)=\frac12\int_{S^2}[|\nabla_{S^2}m|^2+\kappa(1-(m(x)\cdot x)^2)]\,dS,
```

for unit magnetization fields $`m:S^2\to S^2`$. Write an axisymmetric field in spherical coordinates as $`m(\theta,\varphi)=(\sin h(\theta)\cos\varphi,\sin h(\theta)\sin\varphi,\cos h(\theta))`$.

Is there exactly one profile $`h\in C^\infty([0,\pi])`$, inducing a smooth map on the whole sphere, that satisfies

```math
h''+\cot\theta\,h'-\frac{\sin(2h)}{2\sin^2\theta}-\frac\kappa2\sin(2h-2\theta)=0\quad(0<\theta<\pi),
```



```math
h(0)=0,\qquad h(\pi)=2\pi,\qquad h(\pi-\theta)=2\pi-h(\theta)?
```

These boundary and reflection conditions specify the hemispheric class with one complete profile rotation; the corresponding map has degree zero.

## Application

Curvature can support magnetic configurations that differ from planar-film patterns. Uniqueness would determine whether two known constructions describe the same saddle configuration for a spherical shell.

## References

- Stephen Gustafson, Daniel Meinert and Christof Melcher, [*Saddle Point Configurations for Spherical Ferromagnets*](https://arxiv.org/html/2509.05159v2) (2025 preprint; 2026 publication), equation (2.6), Definition 3.1 and Remark 3.18: the model, the hemispheric class $`H_{0,2}`$, and the explicit uniqueness conjecture.
- Giovanni Di Fratta, Valeriy Slastikov and Arghir Zarnescu, [*On a sharp Poincaré-type inequality on the 2-sphere and its application in micromagnetics*](https://arxiv.org/abs/1901.04334) (2019), §1 and Theorem 2: comparison with radial ground states for the spherical micromagnetic energy.

## Status review

Reviewed 15 October 2026 against the original target in [PR #170](https://github.com/MColbrook/AIM/pull/170). Claim: two-profile counterexample claim; public dependency closure inspected, local Lean replay pending.

[Proof or source](https://prove2.me/theorems/2f49ead8-433f-4b5e-9fc9-c44349429863) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/170-source-scope-root.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Review boundary:** A frozen installable project with complete dependency pins, a successful local Lean replay and transitive axiom output remain unverified; all 19 public custom imports were retrieved and inspected, with no concrete assumption gap found.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Resolution-source report (2026-10-15):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-15-prior-resolutions.md#aim-241). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-13)

**Literature check:** Open in cited literature; no later resolution located.

Searched “Saddle Point Configurations spherical ferromagnets uniqueness 2026”, “spherical ferromagnet H_0,2 unique critical profile conjecture proof”, and the journal publication. Remark 3.18 expressly conjectures uniqueness for all $`\kappa\geq4`$. Existence and local continuation near the explicit $`\kappa=4`$ profile do not prove global uniqueness in this class. No later proof or counterexample was located.
