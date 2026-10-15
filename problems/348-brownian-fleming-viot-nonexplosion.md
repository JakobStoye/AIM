# 348. Non-explosion of Brownian Fleming–Viot systems in arbitrary domains

**Area:** Interacting particles and conditioned diffusion

**Status:** 🔵 OPEN

**Last checked:** 2026-10-16

## Problem statement

Let $`d\ge2`$, let $`D\subset\mathbb R^d`$ be a nonempty bounded connected open set, and fix an integer $`N\ge3`$. No regularity assumption is imposed on $`\partial D`$. Start $`N`$ labelled particles at any deterministic configuration $`x=(x_1,\ldots,x_N)\in D^N`$; coincident starting positions are allowed.

Between resampling events the particles move as independent standard Brownian motions, with generator $`\tfrac12\Delta`$. When a particle first reaches $`\partial D`$, choose one of the other $`N-1`$ particles uniformly and move the exiting particle instantly to its current position. The remaining particles stay where they are. Continue with independent Brownian increments and fresh uniform choices, conditional on the new configuration. This is the Brownian Fleming–Viot particle system with hard killing and uniform resampling.

Let $`\tau_0=0`$ and let $`\tau_k`$ be the time of the $`k`$th resampling event. The construction defines the system up to

```math
\tau_\infty=\lim_{k\to\infty}\tau_k.
```

Before this limit, simultaneous boundary exits have probability zero. **Is it always true that**

```math
\mathbb P_x(\tau_\infty=\infty)=1
\qquad\text{for every }d,D,N,x\text{ as above}?
```

Equivalently, must there almost surely be only finitely many resampling events in every finite time interval? The population size remains $`N`$ throughout the construction; the possible failure is accumulation of infinitely many events at a finite time. The question concerns each fixed finite $`N`$, with no drift, reflection or change to the resampling rule.

## Application

Resampling lets a particle population approximate the distribution of a diffusion conditioned to remain inside a region: a path that exits is replaced by a surviving path's current state. For Brownian motion this connects the particle method to the heat equation with absorbing, or Dirichlet, boundary conditions. Related stationary particle methods approximate quasi-stationary distributions and the first Dirichlet eigenfunction. Non-explosion is a prerequisite for running the prescribed continuous-time simulation for any finite duration. Removing geometric boundary assumptions would extend this foundation to irregular regions. Accuracy, convergence to equilibrium and large-population limits require their own hypotheses and estimates.

## References

- [Krzysztof Burdzy, *My favorite open problems*](https://sites.math.washington.edu/~burdzy/open_mathjax.php), Problem 6: the bounded-domain formulation, the earlier proof error and the positive two-particle result. The page is undated; accessed September 19, 2026.
- [Mateusz Kwaśnicki, *Fleming–Viot couples live forever*, Probability Theory and Related Fields 188 (2024), 1385–1408](https://link.springer.com/article/10.1007/s00440-023-01247-z); [full published text](https://d-nb.info/1321707789/34), Theorem 1.1, Remark 1.2 and Corollary 1.4.
- [Mariusz Bieniek, Krzysztof Burdzy and Sam Finch, *Non-extinction of a Fleming-Viot particle model*, Probability Theory and Related Fields 153 (2012), 293–332](https://link.springer.com/article/10.1007/s00440-011-0372-5); [arXiv:0905.1999v1, May 13, 2009](https://arxiv.org/pdf/0905.1999v1), Theorem 5.1, Remark 5.2, Example 5.3, Theorems 7.1–7.2 and Theorem 8.2. These locators refer to the inspected preprint; published numbering differs.
- [Krzysztof Burdzy, Robert Hołyst and Peter March, *A Fleming-Viot particle representation of the Dirichlet Laplacian*, Communications in Mathematical Physics 214 (2000), 679–703, author manuscript](https://digital.lib.washington.edu/server/api/core/bitstreams/b0fd8430-4c30-4b35-bc2f-be4064c7f256/content), Theorem 1.1 and its proof, equation (2.1), for the historical claim whose proof error is discussed in the later sources.
- [Mariusz Bieniek, Krzysztof Burdzy and Soumik Pal, *Extinction of Fleming-Viot-type particle systems with strong drift*, Electronic Journal of Probability 17 (2012), paper 11, 1–15](https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/1770/1770-9325-2-PB.pdf), §1 and Theorems 1.1–1.2.
- [Denis Villemonais, *General approximation method for the distribution of Markov processes conditioned not to be killed*, ESAIM: Probability and Statistics 18 (2014), 441–467](https://numdam.org/item/10.1051/ps/2013045.pdf), Hypothesis A(N), Theorem 2.2, Hypotheses 3.1 and 3.4, and Theorem 3.6.
- [Lucas Journel and Pierre Monmarché, *Uniform convergence of the Fleming–Viot process in a hard killing metastable case*, Annals of Applied Probability 35 (2025), 1019–1048; arXiv:2207.02030v3, November 21, 2024](https://arxiv.org/pdf/2207.02030v3), Assumptions 1–2 and Theorems 1–2.

## Status review

**Resolution-source report (2026-10-16):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-16-prior-resolutions.md#aim-348). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-19)

**Literature check:** Open in cited literature; no later resolution located.

Open in cited literature; no later resolution located as of 2026-09-19. Burdzy's Problem 6 explicitly poses the bounded-domain question. Kwaśnicki's independently authored Remark 1.2 retains the question for more than two particles. His Corollary 1.4 establishes non-explosion for two Brownian particles from every interior initial configuration, including coincident positions; the almost-everywhere qualification in the more general Theorem 1.1 is therefore not a remaining Brownian obstruction.

The unrestricted claim in Burdzy–Hołyst–March has an acknowledged proof error. Bieniek–Burdzy–Finch identify the faulty induction leading to equation (2.1); Kwaśnicki and Burdzy's problem page explicitly retain the unsolved remainder. The preprint's Theorem 5.1 proves non-explosion for bounded Lipschitz domains with a sufficiently small Lipschitz constant depending on $`N`$ and $`d`$. Its polyhedral theorem treats two particles. These results do not cover arbitrary rough domains with $`N\ge3`$.

Villemonais's general approximation theorem assumes non-explosion for its approximating particle systems. His separate sufficient criterion requires a twice continuously differentiable boundary-distance function in a boundary neighbourhood, or an appropriate regular substitute. Approximating an irregular domain by regular ones does not establish non-explosion of the original fixed-$`N`$ construction. Journel–Monmarché's later convergence theorems impose a $`C^2`$ boundary and further conditions on a drift potential. The extinction examples of Bieniek–Burdzy–Pal use singular drift and therefore do not disprove the Brownian question.

The [evidence record](../research/expansion-2026-09/candidates/brownian-fleming-viot-nonexplosion.json) records source access, theorem comparisons, current searches and the separated A61 adversarial self-review. No independent agent or human review was performed. This is one non-explosion family, covering all particle numbers and dimensions in the statement. Entry [319](318-selected-brownian-population-genealogy.md) concerns large-population ancestry under a different branching-and-selection rule; entries [273](272-reaction-network-positive-recurrence.md) and [315](314-contact-process-nonamenable-weak-survival.md) concern different stochastic dynamics.
