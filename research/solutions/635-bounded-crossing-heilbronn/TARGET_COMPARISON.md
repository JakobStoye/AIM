# Target comparison for AIM 635

Target: [635. Small mod-two area cycles in drawings with bounded pairwise intersections](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/635-bounded-crossing-heilbronn.md), repository revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

Submitted result: Theorem 1 of *Small mod-two area four-cycles in drawings with bounded pairwise intersections*, by Kaiwen Jin, dated October 14, 2026. All locations below refer to the [supplied manuscript](paper/main.pdf).

| Original requirement | Result and manuscript location | Scope |
| --- | --- | --- |
| Drawings of $`K_n`$ entirely in the unit square, for every integer $`n\ge3`$ | Section 1 defines $`Q=[0,1]^2`$ and the same admissible drawings. Theorem 1 covers every $`n\ge3`$; Section 3 treats the finite initial range, including $`n=3`$. | Full. |
| Distinct vertices; injective piecewise smooth original edge arcs avoiding other vertices | Section 1 retains these hypotheses. Section 2 proves their union is null in planar Lebesgue measure without a uniform length or derivative bound. | Same data class; no extra metric regularity bound. |
| Transverse interior crossings; each pair of distinct original edges meets at most $`k`$ times, counting shared endpoints | Section 1 retains the meeting convention. Lemma 2 counts actual subdivisions of $`2r+1`$ original arcs. An $`h`$-way meeting contributes at most $`2\binom h2`$ arc incidences; endpoint meetings only enlarge the pair count. | Full, including multiple crossings at one point. |
| A nonempty subset of original edges with even degree at every original vertex; disconnected cycles permitted | Section 1 uses this exact $`\mathbb F_2`$-cycle definition. Equation (3) and the paragraph following it show that two distinct triangles through $`ab`$ differ in four distinct original edges, with degree two at their four vertices. Section 3 uses a triangle for $`n=3`$. | Full. For $`n\ge4`$ the result supplies a connected abstract four-cycle, a permitted strengthening. |
| Area defined by generic-path crossing parity; no Jordan-domain requirement | Section 1 defines the same area. Section 2 gives parity linearity in (2), measurability, and $`A(t_i+t_j)=\mu(R_i\triangle R_j)`$ in (3). | Full. The drawing of the four-cycle may cross itself, and its parity area may be zero. |
| For every fixed $`k\ge2`$, a function $`\varepsilon_k(n)\to0`$ uniformly over all admissible drawings | Theorem 1 selects an integer $`s`$ with $`2^s>10ks^2`$ and sets $`D=2^s-1`$, $`m=n-2`$. Formula (1) gives $`\varepsilon_k(n)=1`$ for $`m<4^D`$, and $`\min\{1,12\log(m)/m^{1/D}\}`$ otherwise. Section 3 proves the area bound and the limit. | Full. All constants and thresholds depend only on $`k`$, not the drawing. |
| The remaining target allows edge pairs to cross repeatedly, beyond simple drawings | Lemma 2 explicitly uses the fixed pairwise meeting cap rather than a simple-drawing assumption. Lemmas 3-4 and Section 3 then establish the required vanishing-area conclusion. | Full fixed-$`k`$ target. No optimal rate or geometrically simple cycle is claimed. |

## Public dependencies and attribution

The principal geometric input is Euler's formula for a finite connected plane multigraph, [Joy Morris, Theorem 15.2.1](https://www.cs.uleth.ca/~morris/Combinatorics/html/sect_planar-EulerFla.html). Lemma 2 applies it to the actual curved union after all meetings are subdivided; parallel edges are allowed.

The classical set-system duality and finite trace inequality are credited to [Assouad, *Densite et dimension*](https://doi.org/10.5802/aif.938), Proposition 2.12 (pp. 246-247) and Lemma 1.8 (p. 240). The needed forms are proved in Lemmas 3 and 4, so the paper does not require an omitted set-system proof. The basic measure conventions are recorded in [Tao, Section 1.2 of the author's preliminary version](https://terrytao.wordpress.com/wp-content/uploads/2012/12/gsm-126-tao5-measure-book.pdf); the zero-area assertion for the edge arcs is also proved in Section 2.

The background claims use [Hubard--Suk, arXiv:2212.01311v1, Section 5, Proposition 5.1](https://arxiv.org/abs/2212.01311v1), for the obstruction without a uniform intersection bound, and [Zeng, arXiv:2308.04742v3, Theorem 1.1 and Corollary 1.2](https://arxiv.org/abs/2308.04742v3), for the simple-drawing case. Neither background result is asserted here to cover the fixed repeated-meeting target directly. The supplementary argument is the simultaneous parity-pattern bound for triangles through a common edge and its use to produce a close pair and an original four-cycle.

The source uses verified public references and states the full argument. No numerical or formal evidence is needed or offered. This comparison documents a complete solution claim; independent mathematical review remains requested.
