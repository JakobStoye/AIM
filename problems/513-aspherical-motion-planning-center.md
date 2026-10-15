# 513. The centre-rank formula for aspherical motion planning

**Area:** Applied topology and robot motion planning

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`M`$ be a closed, connected, oriented aspherical manifold of dimension $`n\ge3`$: its universal cover is contractible. Put $`G=\pi_1(M)`$ and let $`Z(G)`$ be its centre. Define the rank of this abelian group by

```math
z=\dim_{\mathbb Q}\bigl(Z(G)\otimes_{\mathbb Z}\mathbb Q\bigr).
```

Use unreduced topological complexity: $`\mathop{\mathrm{TC}}\nolimits(M)`$ is the least number of open sets covering $`M\times M`$ on each of which the endpoint map

```math
e:C([0,1],M)\longrightarrow M\times M,\qquad e(\gamma)=(\gamma(0),\gamma(1)),
```

with the compact-open topology on the path space, admits a continuous section.

Does every such manifold satisfy

```math
\mathop{\mathrm{TC}}\nolimits(M)=2n+1-z?
```

Prove the formula or construct a counterexample. The target concerns ordinary two-endpoint motion planning, with no curvature assumption.

## Application

Topological complexity measures the minimum number of continuous local rules needed to plan paths between arbitrary configurations. This question asks whether, for aspherical configuration spaces, dimension and the centre of the fundamental group determine that number. It would give a direct algebraic way to predict unavoidable changes between planning rules.

## References

1. C. Neofytidis, [Topological complexity, asphericity and connected sums](https://doi.org/10.1007/s41468-025-00205-z), Journal of Applied and Computational Topology **9**, article 10 (2025), Question 5.8, p.16. [arXiv:2212.08962v2](https://arxiv.org/abs/2212.08962v2).
2. N. Daundkar, R. Santhanam and S. Thandar, [Higher topological complexity of Seifert fibered manifolds](https://arxiv.org/abs/2304.01274v3), revised 30 January 2026; Proceedings of the Royal Society of Edinburgh Section A, published online 16 February 2026.

## Status review

Reviewed 15 October 2026 against the original target in [PR #96](https://github.com/MColbrook/AIM/pull/96). An oriented flat five-manifold contradicts the universal centre-rank TC formula.

[Proof or source](../research/solutions/513-kaiwen-jin-flat-counterexample/paper/main.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/513-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** An admissible closed oriented aspherical5-manifold has centre rank2 but unreduced TC at least10, exceeding the predicted9.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

Reference [1] records supporting cases including tori, hyperbolic manifolds and circle bundles over hyperbolic surfaces. Its centreless question is included in this formula and is not counted separately. The displayed scope omits the already understood closed oriented surfaces.

Reference [2] gives further bounds and conditional exact computations for Seifert manifolds. Its hypotheses do not give the displayed formula for every aspherical manifold. Searches on 24 September 2026, including indexed arXiv, Zenodo, GitHub and Palomar records, located no matching general proof or counterexample.
