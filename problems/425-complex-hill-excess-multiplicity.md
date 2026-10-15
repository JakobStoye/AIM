# 425. Excess Floquet multiplicity for complex periodic Schrödinger equations

**Area:** Periodic wave media and nonselfadjoint spectral theory

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15
## Problem statement

Let $`q\in L^1_{\mathrm{loc}}(\mathbb R;\mathbb C)`$ have period $`a>0`$. For $`-u''+qu=\lambda u`$, let $`c,s`$ have initial values $`(c,c')=(1,0)`$ and $`(s,s')=(0,1)`$ at $`x_0`$. Write $`M(\lambda)`$ for the period monodromy matrix and $`\Delta(\lambda)=\mathop{\mathrm{tr}}\nolimits M(\lambda)`$. For each $`\lambda`$, define $`d(\lambda)`$ as its zero order in $`\Delta^2-4`$, and $`p(x_0,\lambda),r(x_0,\lambda)`$ as its zero orders in $`s(x_0+a,x_0,\lambda)`$ and $`c'(x_0+a,x_0,\lambda)`$; a nonzero value has order zero. Put $`p_i=\min_{x_0\in[0,a]}p`$ and $`r_i=\min_{x_0\in[0,a]}r`$.

Can $`d(\lambda)>p_i(\lambda)+r_i(\lambda)`$ occur when $`M(\lambda)=I`$ or $`M(\lambda)=-I`$? Equivalently, can positive excess multiplicity coexist with two linearly independent periodic or antiperiodic solutions? Either an example or a universal impossibility theorem resolves the question.

## Application

No direct application is identified in this entry. The mathematical significance is to determine which excess spectral multiplicities can coexist with two independent periodic or antiperiodic solutions of a complex periodic Schrödinger equation, clarifying its spectral degeneracies.

## References

1. R. Weikard, [Open problem for complex-valued periodic potentials](https://nsa.fjfi.cvut.cz/problems/04_AIM_2015/2015-27/2015-27_AIM_Weikard.pdf), AIM problem 2015-27, p. 1.
2. F. Gesztesy and R. Weikard, [Picard potentials and Hill’s equation on a torus](https://doi.org/10.1007/BF02547336), *Acta Mathematica* **176** (1996), 73–107, Floquet and multiplicity framework cited by the problem note.

## Status review

Reviewed 15 October 2026 against the original target in [PR #170](https://github.com/MColbrook/AIM/pull/170). Affirmative example

[Proof or source](https://ems.press/content/serial-article-files/33923) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/170-source-scope-review_115_140.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** Fu uses full trace, exactly as AIM425. For tau=1/2+ib, Section3.1 finds b1 in (b_eta,1/(2sqrt3)) and b2 in (1/2,sqrt3/2) for which h(b)=e1^2+2e1*eta1+g2/12 vanishes. The printed sign changes and continuity prove existence without relying on the approximate decimal values. At either b, the explicit second solution has zero additive period, and the displayed monodromy is I. Lemma2.4 makes 4e1 a simple root of the spectral polynomial. Theorem2.1 then gives d(4e1)=1+2*p_i(4e1). The differentiable nonconstant-potential equality p_i=r_i in the actual Gesztesy–Weikard Theorem3.2 gives excess exactly1. Translate operator signs explicitly: use q(x)=6*wp(x+z0;tau)+2*wp(x+1/2+z0;tau), period a=1 and spectral value lambda=-4e1. This negates Fu’s operator, so the ODE, scalar monodromy and zero orders agree after the analytic spectral substitution. For example z0=ib/2 avoids every pole along the real line for both terms, yielding a smooth nonconstant complex periodic potential. The monodromy is conjugate to I in any canonical initial basis and hence still I. Periodicity means the minimum over all real basepoints equals the minimum over [0,1]. This proves precisely the requested existential counterexample to impossibility. The complete two published papers are imported, not newly formally certified.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Resolution-source report (2026-10-15):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-15-prior-resolutions.md#aim-425). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-22)

**Literature check:** Open in cited literature; no later resolution located.

The excess is nonnegative, and in the real selfadjoint case positivity forces geometric multiplicity one. Searches through the review date for Weikard’s problem, complex Hill monodromy excess multiplicity, and subsequent periodic-potential papers found no resolution in the stated complex class. Classification results for special elliptic finite-gap potentials are narrower.
