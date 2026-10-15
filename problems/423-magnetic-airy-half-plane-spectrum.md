# 423. Nonempty spectrum for a magnetic complex Airy operator at every field strength

**Area:** Magnetic spectral PDEs and superconductivity

**Status:** 🟡 PARTIAL

**Last checked:** 2026-10-15
## Problem statement

For each real $`c\ne0`$, let $`\Omega=\{(x,y)\in\mathbb R^2:y>0\}`$ and consider the Dirichlet realization

```math
A_c=-\partial_x^2-\left(\partial_y-\frac{i x^2}{2}\right)^2+i c y
```

on $`L^2(\Omega)`$, with domain

```math
D(A_c)=H^1_0(\Omega)\cap\{u:A_cu\in L^2(\Omega)\},
```

where $`A_cu`$ is understood distributionally. Is $`\sigma(A_c)\ne\varnothing`$ for every $`c\ne0`$? The issue is the intermediate values of $`|c|`$, beyond the small- and large-parameter regimes.

## Application

This operator arises in linear stability analysis of superconductivity with electric currents and a spatially varying magnetic field. Nonempty spectrum determines whether a spectral threshold exists for the normal state.

## References

1. Y. Almog, [Magnetic Schrödinger operator](https://nsa.fjfi.cvut.cz/problems/04_AIM_2015/2015-02/2015-02_AIM_Almog_2.pdf), AIM nonselfadjoint spectral theory problem 2015-02, p. 1.
2. B. Helffer, [On spectral problems related to a time dependent model in superconductivity with electric current](https://doi.org/10.5802/jedp.56), *Journées Équations aux Dérivées Partielles* (2009), Exposé 3, 1–16, discussion of the Almog–Helffer–Pan magnetic models.

## Status review

Reviewed 15 October 2026 against the original target in [PR #136](https://github.com/MColbrook/AIM/pull/136). Verified domain clarification: the printed ordinary Sobolev restriction is nonclosed; the intended closed magnetic spectral problem is not settled.

[Proof or source](../research/solutions/423-ordinary-sobolev-magnetic-airy-domain-clarification/paper/domain-correction.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/423-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Known cases:** Verified domain clarification: the printed ordinary Sobolev restriction is nonclosed; the intended closed magnetic spectral problem is not settled.

**Remaining target:** Prove nonempty spectrum for every intermediate nonzero field strength for the natural closed magnetic Dirichlet realization.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Known cases:** Nonempty spectrum is established for sufficiently small and sufficiently large nonzero field strengths.

**Remaining target:** Nonempty spectrum for every nonzero field strength, including all intermediate magnitudes.

**Literature check:** Open in cited literature; no later resolution located.

Almog records nonempty spectrum for sufficiently small and sufficiently large $`|c|`$. Searches through the review date for this magnetic half-plane operator, Almog–Helffer–Pan spectral nonemptiness, and later complex Airy papers did not locate a proof for every nonzero $`c`$. Empty-spectrum results for the nonmagnetic complex Airy operator do not apply.
