# AIM 635: independent review of PR #114

Date: 2026-10-15. Reviewer: OpenAI Codex, independent AI review in the receiving repository; no human review or Lean verification is asserted.

PR: [#114](https://github.com/MColbrook/AIM/pull/114). Reviewed head: `062917a6f33965d876974e7d9df3e22ae6feec33`.

Outcome: **Solved** — Bounded pairwise intersections force a mod-two area four-cycle with area tending uniformly to zero.

Proof: [main.pdf](../../../research/solutions/635-bounded-crossing-heilbronn/paper/main.pdf). The original problem page, complete manuscript, target comparison, package README and other supplied explanatory material were compared.

## Mathematical audit

Finite piecewise-smooth injective arcs have planar measure zero by decomposition into Lipschitz pieces. Pairwise intersection bounds give a finite planarization, including multiple meetings and shared endpoints. Crossing parity is constant on each face and adds modulo two under addition of original-edge cycles. Thus the area used is exactly the measure of the odd-parity region, as in the target, without imposing that a drawn cycle be a Jordan curve.

Fixing an edge $`ab`$ gives $`n-2`$ triangle parity regions. The symmetric difference of two such triangles is a nonzero original four-cycle: only the common edge cancels, leaving four distinct original edges. For any $`r`$ triangle regions, their drawing uses $`2r+1`$ arcs. Subdivision at meetings produces at most the number of arcs plus twice the total pairwise meeting count in edges; at an $`h`$-way meeting, $`h\le2\binom h2`$ justifies the same bound. Euler's formula bounds the number of complementary faces and hence parity-membership patterns by $`10kr^2`$. Other edges in the full drawing do not create new bit patterns for this selected family.

Choosing $`s`$ with $`2^s>10ks^2`$, a family that shattered $`2^s`$ points would contain $`s`$ coordinate-indicator regions realizing all binary patterns, contradicting the quadratic bound. The shattering dimension is thus at most $`D=2^s-1`$. The submission proves the finite trace bound inductively, including repeated sample points. If all $`m=n-2`$ regions had symmetric-difference area above $`12\log m/m^{1/D}`$, sample $`\lfloor m^{1/D}/2\rfloor`$ points from the finitely many parity cells with their area weights. A union bound gives a sample on which all $`m`$ traces differ, but the trace count is strictly below $`m`$. Hence a close pair exists. Sampling finite weighted cells avoids a hidden continuum measurability assumption.

The small-$`n`$ branch has area bound one and supplies any original triangle or four-cycle as applicable. The displayed large-$`n`$ bound tends to zero for fixed $`D`$; its exponent may be extremely small but remains positive. The conclusion covers every allowed drawing uniformly, including cycles whose parity area happens to vanish. It does not claim an embedded empty-face bound for nonsimple drawings.

## References and scope

[Hubard–Suk](https://arxiv.org/pdf/2212.01311v1), Proposition5.1 and the subsequent bounded-intersection question, were checked for the mod-two area notion and unrestricted-drawing obstruction. [Zeng](https://arxiv.org/pdf/2308.04742v3), Corollary1.2, really concerns a small plane4-face in the simple-drawing case, as distinguished in the introduction. Assouad is correctly credited for the set-system context, but the needed dual-shattering and trace bounds are proved directly. Morris's planar Euler formula and Tao's elementary measure context are standard and match their uses; the pinned AIM statement is the submitted target.

## Delivery checks

All five PDF pages, complete target comparison and ancillary prose were read and visually inspected. The argument uses original edges throughout after planarization is used solely to count regions. No simulation, numerical area calculation or Lean certificate is asserted.
