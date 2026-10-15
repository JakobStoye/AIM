# 338. Decidability of local asymptotic stability for polynomial ODEs

**Area:** Nonlinear control and algorithmic verification

**Status:** 🔵 OPEN

**Last checked:** 2026-10-16

## Problem statement

An input consists of a positive integer $`n`$ and a polynomial vector field

```math
f\in\mathbb{Q}[x_1,\ldots,x_n]^n,\qquad f(0)=0,
```

given by a finite list of monomials with exactly encoded rational coefficients and nonnegative integer exponents. Dimension and degree may vary. Consider the autonomous continuous-time system $`\dot x=f(x)`$ on $`\mathbb{R}^n`$. Write $`\phi(t,x_0)`$ for its unique maximal classical solution from $`x_0`$, and use the Euclidean norm.

The equilibrium $`0`$ is **locally asymptotically stable** when both conditions hold:

1. For every $`\varepsilon>0`$, some $`\delta>0`$ has the following property: every $`x_0`$ with $`\|x_0\|<\delta`$ gives a solution defined for all $`t\geq0`$ with $`\|\phi(t,x_0)\|<\varepsilon`$ for all $`t\geq0`$.
2. Some $`r>0`$ has the following property: every $`x_0`$ with $`\|x_0\|<r`$ gives a solution defined for all $`t\geq0`$ and satisfying $`\lim_{t\to\infty}\phi(t,x_0)=0`$.

**Open question:** Does a Turing algorithm exist that halts on every such finite input and correctly decides whether these two conditions hold? This is the local-asymptotic-stability version of Arnold's polynomial stability question, explicitly discussed in [1, §3].

There is no prescribed running-time bound, homogeneity assumption or promise about the linearization. The negative output means failure of local asymptotic stability; a stable but nonattracting equilibrium must also receive that output. Global existence for initial conditions far from the origin is not assumed. Equivalent finite binary encodings do not change the existence of a terminating decision algorithm.

## Application

In a nonlinear control model, an equilibrium represents a desired operating state. Local asymptotic stability asks whether sufficiently small state disturbances remain small and eventually decay. Polynomial vector fields give finite algebraic descriptions of nonlinear interactions and arise in closed-loop models, reaction systems and local approximations. The question concerns whether exact automatic verification can always finish for this model class.

A positive answer would establish a general decision method, potentially with prohibitive cost. An undecidability result would identify a fundamental limit on universal verification. Neither outcome alone designs a stabilizing controller. When a polynomial comes from approximating another model, transferring its stability conclusion requires a separate justification.

## References

1. Amir Ali Ahmadi and Pablo A. Parrilo, *Stability of Polynomial Differential Equations: Complexity and Converse Lyapunov Questions*, [arXiv:1308.6833v1](https://arxiv.org/pdf/1308.6833v1), August 30, 2013, preprint. §2, stability definitions; §3, rational-input question, Theorem 3.1, Lemma 3.2 and Corollary 3.3.
2. Jun Liu and Maxwell Fitzsimmons, *A Globally Asymptotically Stable Planar Homogeneous Polynomial Vector Field With No Polynomial Lyapunov Function*, [arXiv:2607.16171v1](https://arxiv.org/html/2607.16171v1), July 17, 2026, preprint. §I; Theorem II.2; §IV-C and conclusion.
3. Amir Ali Ahmadi and Bachir El Khadir, *On Algebraic Proofs of Stability for Homogeneous Vector Fields*, [arXiv:1803.01877v4](https://arxiv.org/pdf/1803.01877v4), revised August 16, 2018. Cited preprint: Theorem 4.3 and its following hierarchy; §5.
4. Milan Korda, *Stability and performance verification of dynamical systems controlled by neural networks: algorithms and complexity*, [arXiv:2102.02273v5](https://arxiv.org/html/2102.02273v5), revised September 24, 2022. Cited preprint: §2 model and §3.2, Theorem 3 and proof.
5. Daniel S. Graça, Jorge Buescu and Manuel L. Campagnolo, *Computational bounds on polynomial differential equations*, Applied Mathematics and Computation **215**(4) (2009), 1375–1385. [Institutional author manuscript](https://sapientia.ualg.pt/bitstreams/5e035076-6f0c-4622-980d-14060d6c33a4/download), §5, Theorems 22–23 and proof.
6. Sicun Gao, Soonho Kong and Edmund M. Clarke, *Revisiting the Complexity of Stability of Continuous and Hybrid Systems*, [arXiv:1404.7169v4](https://arxiv.org/pdf/1404.7169v4), revised June 4, 2014. Cited preprint: §§3.1–3.2, §4.1 and §4.3.
7. Min Wu, Zhengfeng Yang and Wang Lin, *Exact Asymptotic Stability Analysis and Region-of-Attraction Estimation for Nonlinear Systems*, Abstract and Applied Analysis **2013**, Article 146137. [Publisher full text](https://onlinelibrary.wiley.com/doi/10.1155/2013/146137), published April 4, 2013; §3.1 and §4.3, Algorithm 9.

## Status review

**Resolution-source report (2026-10-16):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-16-prior-resolutions.md#aim-338). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-18)

**Literature check:** Open in cited literature; no later resolution located.

Open in cited literature; no later resolution located as of 2026-09-18. The exact local version is stated in [1]. The independently authored July 2026 paper [2] explicitly retains the algorithmic question. Arnold's original 1976 contribution was not directly read; the formulation uses the full scholarly restatement in [1].

Strong NP-hardness already holds for homogeneous cubic fields [1, Theorem 3.1]. This concerns computational cost and does not prove undecidability. Linear stability and local exponential stability are decidable [1, Lemma 3.2 and Corollary 3.3]. Exponential stability requires a uniform exponential decay bound, whereas the target permits slower convergence and includes equilibria where linearization is inconclusive.

For homogeneous systems, [3, Theorem 4.3] gives a necessary and sufficient hierarchy of rational Lyapunov certificates. Searching certificate degrees does not provide a stopping rule when stability fails. The counterexample in [2] excludes polynomial and local real-analytic certificates for a stable cubic field, while supplying a rational certificate. It therefore settles a different converse-Lyapunov conjecture, without resolving the existence of every possible stability algorithm.

Theorem 3 of [4] proves undecidability for a **discrete-time** system with ReLU feedback. Theorems 22–23 of [5] concern finite-time blow-up of a specified trajectory, with a different coefficient presentation. Neither inspected result supplies a reduction to the neighbourhood property above. The bounded, positive-tolerance decisions in [6] and the fixed-degree certificate searches in [7] likewise have different success criteria; Algorithm 9 explicitly allows failure to find a certificate.

Unrestricted and recent resolution, counterexample, correction and version searches, theorem comparisons and access limits are recorded in the [evidence ledger](../research/expansion-2026-09/candidates/polynomial-local-stability-decidability.json). Several sources are cited as exact preprint versions. Wiley's text conversion omitted formula images; its complete degree-bound and failure-branch prose was accessible. This review does not certify all cited proofs or rerun formalizations.

The [arbitrary-switching problem](332-switched-linear-stability-decidability.md) concerns products of multiple linear maps in discrete time. [Generic static output feedback](319-generic-static-output-feedback-stabilization.md) concerns existence of a stabilizing gain, and [continuous Skolem](263-continuous-skolem-decidability.md) concerns a specified linear trajectory hitting a hyperplane. None states this nonlinear equilibrium decision problem. Global, homogeneous and fixed-degree variants are not counted separately.

A publication refresh on September 18, 2026 rechecked status and upstream duplicates; see the [batch 5 audit](../research/expansion-2026-09/batch-05-review.md). No matching later resolution was located.
