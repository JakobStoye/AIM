# PR170: independent source applicability audit (AIM361,412,425,433,446,462)

Date:2026-10-15. Pinned head:ea9829b04eabe0017d8a968261335a44a7cc30ed. Reviewer:OpenAI Codex.

I read all six original/current target statements and the corresponding report entries, then checked the actual primary statements, hypotheses and named proof interfaces. Published resolutions are distinguished from recent complete claims. The applicability reductions below were reconstructed independently; this review does not imply a new whole-proof audit of every imported paper. No human or locally reproduced Lean verification is claimed.

## AIM 361

Recommended status: **Solution claimed**. Scope: **Full target**. Reported answer: Affirmative existence, claimed.

Evidence: Public September2026 preprint. Current versioned arXiv primary record has no journal-reference field; targeted publication searches did not establish a published version. This audit is a source-applicability review, not an independent audit of all93pages or the computational proof.

[Primary proof](https://arxiv.org/pdf/2609.09353v1).

Locations: Theorem1.3, printed p.8; mechanical entropy equations1.12–1.17, pp.6–7; Lemma6.1, pp.28–29; Section9, pp.56–58; AppendixD, pp.88–89.

The actual theorem states infinitely many distinct bounded entropy solutions with common Riemann data for a smooth pressure law. The state variable is (v,u), with flux (-u,p(v)). Lemma6.1 explicitly gives p′<0, not merely strict monotonicity, and the later perturbation preserves it. Consequently the characteristic speeds are distinct real numbers ±sqrt(-p′), and the mechanical entropy Hessian is diag(-p′,1); its flux up(v) has the exact compatibility identity. A bounded state region with closure away from vacuum is used, and the convex-integration scheme stays in fixed bounded neighborhoods of finitely many states; enlarge that compact set inside a convex open state domain. The pressure is not genuinely nonlinear globally, but AIM361 does not require genuine nonlinearity. Section9 makes the entropy production nonpositive on both fan edges and zero in the constitutive inclusion, giving a spacetime distributional inequality rather than jump-only Liu admissibility. It explicitly derives the strong local L1 initial trace from boundedness and the O(t)-width fan. Distinct solutions and the same initial datum are expressly asserted. Thus the source claim matches every target condition; its difficult rank-one geometry, gluing and computer assistance remain imported, unverified whole-proof dependencies.

Review level: Exact theorem and hypothesis match; full source proof not certified.

## AIM 412

Recommended status: **Solution claimed**. Scope: **Full target**. Reported answer: Negative, claimed.

Evidence: Public September2026 preprint. Current versioned arXiv primary record has no journal reference; targeted publication searches did not establish publication. The full model-space proof was not independently recertified.

[Primary proof](https://arxiv.org/pdf/2609.35355v1).

Locations: Cost definition equation2, p.2; Theorem1.3, p.4; scaling equation12 and Proposition2.1, p.7; Theorem4.1 and proof, pp.16–18.

The source defines the same supremum over the L2-unit initial-data ball of the minimal inflow L2 boundary control norm, with a zero Dirichlet condition at the other endpoint. Its transposition/observability formulation uses the correct epsilon-weighted derivative at x=0. Theorem1.3 states divergence, not merely failure of cost convergence to zero, for TM/L<2 and positive M. Choosing T=3L/(2M) therefore lies strictly above the target transport time yet contradicts the requested zero-cost limit. The scaling in equation12 multiplies the normalized cost by a fixed positive |M|^(-1/2), so it preserves divergence. I checked the lower-bound interface: Theorem4.1 keeps final adjoint L2 mass positive while its observed flux vanishes; Proposition2.1 converts this to divergence of exactly the target cost. Its finite-mode construction and future-flux lower bound agree with these quantifiers. No endpoint claim at T=2L/M is needed. The entire spectral model-space approximation proof is imported rather than independently certified.

Review level: Exact full-target counterexample claim, including boundary placement and cost normalization.

## AIM 425

Recommended status: **Solved**. Scope: **Full target**. Reported answer: Affirmative example.

Evidence: Published Journal of Spectral Theory13(2023),347–381, DOI10.4171/JST/453, confirmed on the EMS publisher page and actual PDF; supporting Acta Mathematica176(1996),73–107 primary PDF. The elementary source-to-target reduction was independently reconstructed.

[Primary proof](https://ems.press/content/serial-article-files/33923).

Locations: Fu definitions printed p.355, Theorem2.1/equation2.2 p.356, Lemma2.4 p.358, Section3.1 pp.364–366 and elliptic sign facts pp.362–363. Gesztesy–Weikard Theorem3.2/equation3.44 printed pp.88–89.

Fu uses full trace, exactly as AIM425. For tau=1/2+ib, Section3.1 finds b1 in (b_eta,1/(2sqrt3)) and b2 in (1/2,sqrt3/2) for which h(b)=e1^2+2e1*eta1+g2/12 vanishes. The printed sign changes and continuity prove existence without relying on the approximate decimal values. At either b, the explicit second solution has zero additive period, and the displayed monodromy is I. Lemma2.4 makes 4e1 a simple root of the spectral polynomial. Theorem2.1 then gives d(4e1)=1+2*p_i(4e1). The differentiable nonconstant-potential equality p_i=r_i in the actual Gesztesy–Weikard Theorem3.2 gives excess exactly1. Translate operator signs explicitly: use q(x)=6*wp(x+z0;tau)+2*wp(x+1/2+z0;tau), period a=1 and spectral value lambda=-4e1. This negates Fu’s operator, so the ODE, scalar monodromy and zero orders agree after the analytic spectral substitution. For example z0=ib/2 avoids every pole along the real line for both terms, yielding a smooth nonconstant complex periodic potential. The monodromy is conjugate to I in any canonical initial basis and hence still I. Periodicity means the minimum over all real basepoints equals the minimum over [0,1]. This proves precisely the requested existential counterexample to impossibility. The complete two published papers are imported, not newly formally certified.

Review level: Published-source resolution with independently checked sign, trace, zero-order and pole-avoidance reduction.

[Supporting primary proof](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6528-11511_2006_Article_BF02547336.pdf).

## AIM 433

Recommended status: **Solved**. Scope: **Full target**. Reported answer: Negative example for every p>2 and d>=3.

Evidence: Published JEMS27(2025),4845–4890, DOI10.4171/JEMS/1462; EMS confirms acceptance26September2022 and online publication23April2024. Actual46page journal PDF retrieved and theorem/construction interface read. Product-domain reduction independently proved.

[Primary proof](https://ems.press/content/serial-article-files/51447).

Locations: Theorem1.2 printed p.4847; restatement Theorem9.4 and construction interface pp.4886–4888.

The actual theorem supplies, for every p>1 other than2, a continuous planar distributional p-harmonic u in W^(1,p-1+epsilon), with infinite p-energy on every nonempty open subdomain. In particular for p>2 its local gradient and u belong to L^(p-1), and the nonlinear flux is L1. Theorem9.4 repeats the same claim; its strong-gradient limit and constitutive-inclusion passage have the stated interface. To match d>=3 choose Omega=B×(0,1)^(d-2) and U(x,z)=u(x), where B is the source ball. The weak gradient is (grad u,0); finite local product measure gives W^(1,p-1)_loc. For any smooth compactly supported test, integration over z produces a smooth compactly supported planar test; Fubini is valid for the L1 flux and reduces the equation exactly to the planar distributional equation. A product of compactly contained nonempty open sets has p-energy equal to its positive transverse volume times the infinite planar energy by Tonelli. Thus U is not locally W^(1,p), and changing representatives cannot change its weak gradient. There is no dimension or endpoint-integrability mismatch. This is an actual published counterexample plus an elementary extension, not an unreviewed new endpoint conjecture.

Review level: Published counterexample with independently reconstructed higher-dimensional application.

[Publication record](https://ems.press/journals/jems/articles/14297760).

## AIM 446

Recommended status: **Solution claimed**. Scope: **Full target**. Reported answer: Affirmative sharp bound, claimed.

Evidence: Public September/October2026 preprint. Current versioned arXiv primary record has no journal reference; targeted publication searches did not establish publication. Reading the short main argument does not certify all imported quasiconvexity-to-operator-norm implications.

[Primary proof](https://arxiv.org/pdf/2609.28311v2).

Locations: Corollary2/equation4, p.2; normalization equation3, p.2; Theorem1 and proof/Lemma4, pp.1–4.

The actual v2 PDF’s Corollary2 asserts equality of the norm on the unrestricted complex-valued Lp(C;C) space for every real1<p<infinity, with the two stated branches p-1 and1/(p-1). Equation3 defines the classical Fourier multiplier through S composed with dbar equals dz. For the catalogue disk-principal-value kernel -1/(pi*z^2), this is precisely the same Beurling multiplier, so restriction to smooth compactly supported complex inputs gives the requested estimate. The source is not confined to real, radial or other special inputs. Theorem1 establishes the periodic quasiconvex integrand statement, then explicitly imports Baernstein–Montgomery-Smith and related arguments to infer Corollary2. I read the actual main proof and projection lemma to identify the interface, but did not independently recertify those imported implications or all source dependencies. Thus this is a full solution claim awaiting complete independent audit/publication, not an established partial result or a justified Solved upgrade from source matching alone.

Review level: Exact full-operator theorem match; complete novel argument and imported implications not certified.

## AIM 462

Recommended status: **Solution claimed**. Scope: **Full negative answer to general question**. Reported answer: Negative for every strict ellipticity pair, claimed.

Evidence: Public12October2026 preprint. Current arXiv primary record has no journal reference, and targeted publication searches did not establish publication. The complete multiscale/adjoint construction is imported.

[Primary proof](https://arxiv.org/pdf/2610.16162v1).

Locations: Theorem1.1 printed p.3; operator convention pp.1–2; localization Proposition2.6 pp.7–8; fixed-coefficient limiting proof pp.13–14.

The theorem states, for every n>=1,0<sigma<2 and0<lambda<Lambda, one fixed even coefficient in the full ellipticity interval and smooth compactly supported nonnegative u_j,g_j in B1 with0<=g_j<=1, shrinking support measure, L_a u_j>=-g_j, and uniformly positive height on B_(1/4). Read sigma=2s. At each x, pointwise ellipticity gives 2*Mplus u_j>=L_a u_j, because the larger coefficient maximizes positive second differences and the smaller one minimizes their negative contribution. Thus f_j=-g_j/2 has sup norm at most1, is smooth, and gives the exact target Mplus inequality. Every finite-p norm of its negative part tends to zero, contradicting every positive-power estimate for the fixed parameters. Smooth u_j are valid upper-touch viscosity subsolutions: replacing u near an upper contact by the test can only increase the nonlocal extremal value. Exterior values are zero. The source’s limiting construction fixes the same coefficient after all stages rather than changing the operator with j; its localization has precisely the common lower height and bounded source interface. Equality lambda=Lambda is not claimed to fail and is unnecessary to refute the unrestricted general assertion. No actual parameter or norm restriction leaves a missing portion of this negative answer, but the new primary proof has not been independently recertified.

Review level: Exact counterexample applicability, including factor1/2, source support and viscosity convention; full source proof imported.
