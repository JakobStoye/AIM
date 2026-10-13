# AIM 386: independent review of PR #54

**Date:** 2026-10-13. **Reviewer:** OpenAI Codex, an independent AI argument audit during maintainer review; no human or Lean verification is asserted.

**PR:** [#54](https://github.com/MColbrook/AIM/pull/54). **Audited head:** `6b03556d5c8ba561a30fb600d7bc0348074361dc`. **Target revision:** `c9929805cece044705abaaebe1cebddac1ba11a6`.

**Direct proof:** [Source manuscript](https://github.com/MColbrook/AIM/blob/6b03556d5c8ba561a30fb600d7bc0348074361dc/research/solutions/386-slow-surface-schrodinger-observability/paper/exterior_observability.tex).

All source sections, ancillary mathematical claims and bibliography entries were read and audited independently of the submission's own AI checks.

## Exact target

The manuscript retains the specified annulus, surface coefficient $`1/2`$, bulk coefficient $`1`$, outer Dirichlet condition and full gradient energy. Exact smooth compatible solutions have energy one and observation tending to zero at each fixed positive time. Complex solutions are permitted by the Schrodinger target.

## Complete independent argument audit

1. The angular Hilbert space retains both the radial bulk and surface coordinate. Its densely defined closed nonnegative form yields bulk action $`-v''-r^{-1}v'+n^2r^{-2}v`$ and surface action $`n^2v(1)/2-v'(1)`$, with the correct inner outward-normal sign. The operator domain is $`H^2`$ with the outer zero trace and no extra Robin constraint on arbitrary domain elements (source lines 112-171).
2. Form positivity, Cauchy-Schwarz, the bulk equation and a one-dimensional endpoint identity prove the outer derivative trace estimate with explicit frequency factors and otherwise uniform constants (174-200).
3. Compactness of bounded $`H^1`$ sequences on the collar ending at $`5/4`$ gives a normalized form minimizer. Its modulus and ODE uniqueness give a positive ground profile. Rayleigh bounds place its eigenvalue between $`n^2/2`$ and $`n^2/2+Cn`$. The eigenvalue-dependent inner relation is derived from the form (208-256).
4. Substitution $`y=\sqrt r\,u`$ gives an ODE potential at least $`\kappa^2n^2`$ throughout the collar at large order. The hyperbolic-sine comparison has the correct maximum-principle sign and gives exponential decay away from the inner boundary. Bulk mass is $`O(n^{-1})`$, leaving surface mass at least $`1/2`$. ODE and fixed-length difference identities bound every derivative needed after cutoff (258-317).
5. The cutoff preserves the inner relation and gives an interior-supported residual with norm $`O(n^2e^{-cn})`$ and operator-image norm $`O(n^4e^{-cn})`$. Successive operator images remain smooth and interior-supported. Induction places the initial state in every operator power domain, proving smoothness and all compatibility identities for its exact unitary evolution (321-365).
6. Graph-norm Duhamel comparison bounds the exact evolution's difference from the stationary approximate evolution both in norm and after applying the operator. Since the approximate state's outer derivative is zero, the trace estimate gives exact flux $`O(tn^4e^{-cn})`$. Retained surface energy is at least $`n^2/4`$, giving energy-normalized observation $`O_T(n^6e^{-2cn})`$. This is a bound for exact solutions, not just a small-residual assertion (367-398).

## References and ancillary claims

All four references were checked. Mercado-Morales' publisher record confirms authors/title, SIAM JCO 61(6), 2023, pages 3501-3525 and DOI. The pinned preprint's Theorem 1.9 inherits its faster-surface assumptions. The actual survey distinguishes this Schrodinger regime from the negative wave result. Teschl's actual second edition, GSM 157 (2014), Theorems 2.14 and 5.1 give the closed-form representation and unitary evolution; the submission establishes their hypotheses. The compactness facts apply to its minimizing sequence. The AIM reference is correct. No additional quasimode theorem is missing: the decay, graph trace and power-domain arguments are internal.

Primary evidence: [Mercado-Morales publisher record](https://epubs.siam.org/doi/10.1137/21M1439407), [author preprint](https://arxiv.org/html/2301.02573v1), [survey](https://arxiv.org/html/2505.14795v1), [Teschl](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf).

## Decision

**Solved - negative answer by complete independently audited exact solutions.** No substantive gap or target restriction remains. No weaker-norm optimality, stabilization-rate or Lean claim is made. Packaging checks are separate integration work.

## PDF consistency and layout

All rendered manuscript pages were inspected in the all-page contact sheet; title, author, theorem/proof structure, final conclusions and bibliography agree with the audited source. No clipped equations, blank pages or unresolved references were observed. The maintainer integration also checks the complete package hashes.

## Ancillary package content

The package README, exact-target comparison, AI-use disclosures, manifests and reproduction guidance were inspected. Their mathematical scope agrees with the manuscript, and none claims human or Lean verification. Maintainer integrity checks cover the listed files. There is no executable proof certificate or numerical experiment used as a proof premise.
