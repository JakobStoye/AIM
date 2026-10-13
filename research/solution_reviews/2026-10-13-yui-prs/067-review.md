# AIM 067: independent review of PR #45

**Date:** 2026-10-13. **Reviewer:** OpenAI Codex, independent AI argument audit during maintainer review; no human or Lean verification is asserted.

**PR:** [#45](https://github.com/MColbrook/AIM/pull/45). **Audited head:** `7d51782d7f43f71724d3caa92e8f256572286359`. **Target revision:** `c9929805cece044705abaaebe1cebddac1ba11a6`.

**Direct proof:** [Source manuscript](https://github.com/MColbrook/AIM/blob/7d51782d7f43f71724d3caa92e8f256572286359/research/solutions/067-burgers-shock-uniform-control-time/paper/main.tex).

All source sections, ancillary mathematical claims and bibliography entries were read and independently reconstructed. This audit does not rely on the submission's own AI checks.

## Exact target

The target asks for the exact infimum of times at which the worst-case original L2 boundary null-control cost stays bounded as viscosity vanishes. The proof retains all L2 initial data, the centered shock, one left Dirichlet actuator and the original control norm. It proves bounded cost for every $`T>4\sqrt2L`$ and divergent cost for every $`0<T<4\sqrt2L`$. These strict-side statements determine the requested infimum; the value of the cost at equality is not needed.

## Complete independent argument audit

1. Integration by parts gives the correct adjoint and left observed flux $`\varepsilon z_x(-L)`$. Conjugation by the hyperbolic cosine gives the stated self-adjoint Dirichlet Schrodinger operator. Its first-order factors yield the Robin problem; the zero Robin mode is explicitly annihilated and is not counted as a Dirichlet eigenfunction. There is one positive slow Dirichlet mode below $`1/(4\varepsilon)`$, and all fast roots obey the monotone phase equation and stated uniform brackets (source lines 145-231).
2. The boundary-normalized fundamental solution is entire in the spectral parameter, including its apparent zero singularity. The left derivative is exactly one. Opposite-end fast derivatives alternate with the stated signs. The hyperbolic-cosine weight gives the uniform fast spatial norm bound; the slow-mode expression gives a bounded norm and eigenvalue tending to zero. Fixed-viscosity regular Sturm-Liouville theory and the explicit graph-norm estimates give complete spectral approximation and derivative-trace convergence (233-357).
3. The exact Dirichlet determinant has order at most one-half, positive value at zero, and simple positive eigenvalue zeros. The Wronskian identity proves simplicity. Hadamard factorization therefore has no nonconstant exponential factor. Evaluating its derivative at a fast root and its value at the negative root gives the separation product. The displayed elementary bounds yield a uniform all-index estimate $`d_k^{-1}\le C\varepsilon e^{D\eta_k}`$ (361-455).
4. The signed inverse of the exponential Cauchy Gram matrix was checked by its partial-fraction identity. Its coefficient-functional norm is $`\sqrt{2\lambda_k}/d_{k,N}`$. The all-index determinant bound, eigenfunction norms and square-root concavity give an absolutely summable Gaussian bound for the fast terminal map. For $`T>2\sqrt2D`$ this map has norm at most $`C\varepsilon^{-1/2}e^{-(T-2\sqrt2D)/(4\varepsilon)}`$ times the half-line observation norm (457-528).
5. The Laplace transform places finite fast observations in the appropriate Hardy model space. The actual constant-one Bernstein theorem applies because the inner product's boundary derivative is bounded by $`2\sum\lambda_k^{-1}<2D`$. Thus $`\|tf\|\le2D\|f\|`$, controlling the tail beyond T and giving uniform finite-time comparison for $`T>2D`$ (530-597).
6. The infinite fast Blaschke product converges, is inner, and has boundary phase converging to $`e^{-2iDy}`$ because $`\sum\lambda_k^{-1}\to D`$ and the cubic reciprocal sum tends to zero. Dominated convergence gives strong convergence of both boundary multiplication operators, and hence of the model projections. Any bounded weak limit of fast observations is supported in $`[0,2D]`$. If fast observations could approximate the slow exponential on a longer observation interval, finite-time comparison would bound them on the half-line; a weak limit would equal one on $`(0,T)`$ while supported in $`[0,2D]`$, a contradiction. This provides a uniform slow-mode separation, not an assumed spectral gap (599-678).
7. Slow-mode separation controls the slow coefficient and the fast measured norm by the complete observed flux. Combining this with the uniform fast bound gives the full upper observability estimate. Graph-norm approximation extends it to every fixed-viscosity adjoint test (680-701).
8. For the lower bound, take a column of the inverse fast Gram matrix with $`N=\lfloor\varepsilon^{-2}\rfloor`$. Its temporal coefficients alternate, and the opposite-end eigenfunction derivatives have complementary signs. A uniform Volterra-series estimate gives a common endpoint layer of width $`O(\varepsilon^2)`$ in which every product has the same sign and each spatial mode is at least $`s/(4\varepsilon)`$ in modulus. Keeping the first term is therefore a valid lower bound without assuming orthogonality of the adjoint eigenfunctions (703-762).
9. The fast eigenvalue brackets bound the first separation product by the explicit shifted quadratic product. The infinite product is evaluated with the actual hyperbolic-sine product, and the tail removed at N is bounded uniformly. This gives $`d_{1,N}\le C\varepsilon^{-5}e^{-D/(\sqrt2\varepsilon)}`$. Combining it with the coherent layer estimate gives the stated $`\varepsilon^{13/2}`$ cost prefactor and exponent $`(4\sqrt2L-T)/(4\varepsilon)`$, which diverges at every strict lower time (764-812).
10. The appendix constructs the original transposition solution for arbitrary L2 data and controls using fixed-viscosity backward tests, spacetime L2 estimates and a continuous terminal functional. Riesz representation on the closure of observed fluxes converts upper observability into an actual null control with the claimed original norm; the reverse duality gives the lower cost bound. No closedness of the original observation range is assumed. The scaling identity preserves both initial and control norms (815-909).

## References and ancillary claims

All six bibliography entries were checked. Laheurte's publisher record gives the cited 2026 SIAM metadata and the previous distinct lower/upper bounds. The actual recent Koike-Laheurte preprint has the cited authors/title and model-space method; it treats constant drift, whereas the manuscript explicitly derives the shock determinant and signs. Baranov-Jaming-Kellay-Speckbacher's actual Theorem 5.2 has constant one with the required bounded boundary derivative hypothesis. Teschl's actual second edition supplies the regular separated self-adjointness, discrete complete spectrum and Hilbert-space facts under the established hypotheses. Weikard's actual Section 6.4.3 states the Hadamard factorization used, with polynomial degree zero at order below one. NIST supplies the convergence/product facts and the hyperbolic-sine product. No sharp uniform-time theorem for shocks is imported without proof.

Primary evidence: [Laheurte publisher record](https://epubs.siam.org/doi/full/10.1137/25M1723311), [Koike-Laheurte](https://arxiv.org/html/2609.35355v1), [Bernstein theorem](https://arxiv.org/html/2304.02385v2), [Teschl](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf), [Weikard](https://www.uab.edu/cas/mathematics/images/Documents/weikard-complex-analysis.pdf), [NIST product](https://dlmf.nist.gov/4.36).

## Decision

**Solved - exact value $`T_{\mathrm{unif}}/L=4\sqrt2`$ established by a complete independent argument audit.** No substantive gap or missing target clause remains. The equality-time cost and nonlinear or off-center shocks are expressly not claimed.

## PDF consistency and layout

All rendered manuscript pages, including the second contact sheet where present, were visually inspected. The title, author, theorem/proof structure, conclusions and bibliography agree with the audited source. No clipped equations, blank pages or unresolved references were observed. Package hashes and repository checks are separate maintainer integration work.

## Ancillary package content

The package README, exact-target comparison, AI-use disclosures, manifests and reproduction guidance were inspected. Their mathematical scope agrees with the manuscript, and none claims human or Lean verification. Maintainer integrity checks cover the listed files. There is no executable proof certificate or numerical experiment used as a proof premise.
