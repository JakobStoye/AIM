# 425. Excess Floquet multiplicity for complex periodic Schrödinger equations

**Area:** Periodic wave media and nonselfadjoint spectral theory

**Status:** 🔵 OPEN

**Last checked:** 2026-10-16
## Problem statement

Let $`q\in L^1_{\mathrm{loc}}(\mathbb R;\mathbb C)`$ have period $`a>0`$. For $`-u''+qu=\lambda u`$, let $`c,s`$ have initial values $`(c,c')=(1,0)`$ and $`(s,s')=(0,1)`$ at $`x_0`$. Write $`M(\lambda)`$ for the period monodromy matrix and $`\Delta(\lambda)=\mathop{\mathrm{tr}}\nolimits M(\lambda)`$. For each $`\lambda`$, define $`d(\lambda)`$ as its zero order in $`\Delta^2-4`$, and $`p(x_0,\lambda),r(x_0,\lambda)`$ as its zero orders in $`s(x_0+a,x_0,\lambda)`$ and $`c'(x_0+a,x_0,\lambda)`$; a nonzero value has order zero. Put $`p_i=\min_{x_0\in[0,a]}p`$ and $`r_i=\min_{x_0\in[0,a]}r`$.

Can $`d(\lambda)>p_i(\lambda)+r_i(\lambda)`$ occur when $`M(\lambda)=I`$ or $`M(\lambda)=-I`$? Equivalently, can positive excess multiplicity coexist with two linearly independent periodic or antiperiodic solutions? Either an example or a universal impossibility theorem resolves the question.

## Application

No direct application is identified in this entry. The mathematical significance is to determine which excess spectral multiplicities can coexist with two independent periodic or antiperiodic solutions of a complex periodic Schrödinger equation, clarifying its spectral degeneracies.

## References

1. R. Weikard, [Open problem for complex-valued periodic potentials](https://nsa.fjfi.cvut.cz/problems/04_AIM_2015/2015-27/2015-27_AIM_Weikard.pdf), AIM problem 2015-27, p. 1.
2. F. Gesztesy and R. Weikard, [Picard potentials and Hill’s equation on a torus](https://doi.org/10.1007/BF02547336), *Acta Mathematica* **176** (1996), 73–107, Floquet and multiplicity framework cited by the problem note.

## Status review

**Resolution-source report (2026-10-16):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-16-prior-resolutions.md#aim-425). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-22)

**Literature check:** Open in cited literature; no later resolution located.

The excess is nonnegative, and in the real selfadjoint case positivity forces geometric multiplicity one. Searches through the review date for Weikard’s problem, complex Hill monodromy excess multiplicity, and subsequent periodic-potential papers found no resolution in the stated complex class. Classification results for special elliptic finite-gap potentials are narrower.
