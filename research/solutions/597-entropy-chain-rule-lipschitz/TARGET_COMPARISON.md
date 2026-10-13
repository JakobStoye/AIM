# Target comparison for AIM 597

Original statement: [Entropy chain rule on nonsmooth nonconvex Lipschitz domains](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/597-entropy-chain-rule-lipschitz.md). Target revision: `c9929805cece044705abaaebe1cebddac1ba11a6`.

Submitted result: Theorem 1.1 of [An entropy chain rule on bounded Lipschitz domains](paper/manuscript.pdf), with its complete proof in Sections 2–4. The submission claims the affirmative alternative for the entire target. Independent mathematical review is requested.

| Original requirement | Result and location in the manuscript | Coverage |
| --- | --- | --- |
| Every bounded Lipschitz domain in dimension d >= 1, including domains that are both nonsmooth and nonconvex | Section 1 and Theorem 1.1; Proposition 3.1 uses local Lipschitz graph charts and ordinary reflection in dimension one | Full original geometry; convexity and boundary smoothness are not assumed |
| Arbitrary T > 0, potential V in C2 of the closed domain, pi = exp(-V) | Section 1 before equation (1); Section 4, equation (17) | Same time horizon, regularity and normalization |
| Nonnegative density in C([0,T]; L1 with its weak topology), with fixed positive mass | Theorem 1.1, pages 1–2; Lemma 2.1 and the reflected density extension | Same data class and actual time representative |
| Prescribed F in L1((0,T) x Omega; R^d) | Theorem 1.1; F is retained in Proposition 3.1 and the final identity | Arbitrary original flux; no optimal-flux substitution |
| Precise no-flux continuity equation for every C1 test on the closed spacetime domain, including endpoint terms | Equation (2); extension to Lipschitz spatial tests in equation (11) | Same weak boundary condition; no extra normal-trace assumption |
| Finite initial weighted entropy with 0 log 0 = 0 | Equation (1), Theorem 1.1 and the initial-time passage in Section 4 | Same initial hypothesis; finiteness at every subsequent time is proved |
| Finite kinetic action with the prescribed quotient convention on vacuum | Equation (3) and the conventions preceding Theorem 1.1; normalized convolution bounds (8) | Same action and vacuum convention |
| Finite weighted Fisher information, including square-root H1 regularity almost everywhere in time | Equation (3) and its following sentence; multiplier identity and estimate (17) | Same assumption; no density bounds |
| Entropy absolutely continuous on [0,T] | Theorem 1.1 and the final paragraph of its proof | Entire closed interval; equations (4) and the Section 4 limit use the actual endpoint values |
| Exact almost-everywhere derivative paired with the prescribed flux | Equations (4)–(5), supported by local identity (7), global identity (12) and potential restoration | Full asserted derivative, with the stronger identity for every 0 <= s <= t <= T |
| Vacuum integrand (F/sqrt(rho)) dot (2 grad sqrt(rho) + sqrt(rho) grad V), normalized flux zero on vacuum | Equation (4) and its following convention; Lemma 2.1 handles vacuum in the mollification limit | Exact prescribed interpretation and L1 integrability |
| No additional density or logarithmic-gradient approximation assumption | Theorem 1.1; fixed-truncation cancellation in Section 3 and truncation removal in Section 4 | Full remaining target |

Public dependencies are used in their explicitly stated forms. Hajłasz's lecture notes, Corollary 21 and Theorems 18 and 31, supply level-set gradient vanishing, the absolute continuity on lines characterization, and bi-Lipschitz Sobolev composition. The manuscript explains their product and even-reflection applications. The three other references describe earlier convex, smooth nonconvex and Dirichlet-boundary chain rules; their restrictions are stated in Section 1 and are not imported as unprovided assumptions. The bibliography fixes the arXiv versions and cited theorem numbering.

The added argument is the prescribed-flux Lipschitz graph reflection and the cancellation of localization terms before removing the entropy truncation. The statement requires an entropy chain rule; the submission establishes that claim analytically.

AI use and review: OpenAI Codex developed and checked the analytic manuscript and its cited interfaces. No separate detailed AI review is included, and independent mathematical review is requested.
