# Target-to-theorem comparison

Frozen problem: [AIM Problem 434](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/434-p-harmonic-second-sobolev-derivatives.md), revision `c9929805cece044705abaaebe1cebddac1ba11a6`. Original statement file SHA-256: `8ff05527c9f495390c9eddbfb70466eca40d48e7f297bebb8ae7526244b2ce75`.

| Source clause | Manuscript location and coverage |
|---|---|
| Every finite real p >= 5, including p = 5 | Theorem 1.1; Section 3 coefficients and Proposition 4.1 are finite for each such p |
| Every open Omega subset R^3 | Theorem 1.1 and its proof use arbitrary compact interior balls only |
| Every real weak u in W^{1,p}_loc | Equation (2), Theorem 1.1 and the Sarsa regularization interface in its proof; local C1 regularity is a cited consequence, not a new hypothesis |
| Zero distributional p-Laplacian | The exact weak identity is equation (2); all smooth intermediate solutions have zero source |
| All unweighted distributional second derivatives in local L2 | Equation (24) bounds the full smooth Hessian; the following test-functional and Riesz argument identifies all nine limiting entries |
| Every critical-point neighborhood | Lemma 2.1 justifies zero extension and the distributional inequality; the final proof imposes no property of the limiting critical set |

The conclusion is an affirmative full-target theorem claim. It does not assert a bound uniform as p tends to infinity or a theorem in other spatial dimensions.

## Relation to cited results

Lindqvist's Section 11, p. 93 poses the second-derivative question beyond the classical Cordes range. Sarsa's Theorem 1.1 (arXiv:2009.10102v1, 2020) controls `|Du|^beta Du` with `beta > (p-5)/4` in dimension three. Its strict inequality excludes `beta = 0` throughout p >= 5; its Section 3 (3.2)-(3.4) supplies the smooth approximation used here. Haarala and Sarsa's global theorem has the same restricted Cordes exponent range. These results are credited rather than presented as the proposed new conclusion.

The additional argument in the manuscript is Lemma 2.1, the curvature correction (15)-(16), the source-free level topology and boundary estimate (17), and the uniform radial iteration (20)-(23). This is a combination requiring substantive supplementary proof, not a direct citation or elementary relabeling of a known full-target theorem. A bounded literature search is not evidence of exhaustive novelty.

## Review and evidence boundary

The manuscript is AI-assisted and submitted for independent mathematical review. Its complete analytic argument is public; file-integrity and compilation checks are reproducibility evidence. An AI check or a filed pull request does not constitute maintainer acceptance or a human proof certification. No numerical evidence is used to infer the theorem.
