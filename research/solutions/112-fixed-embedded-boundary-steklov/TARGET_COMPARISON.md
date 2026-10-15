# Correspondence with AIM Problem 112

Target: [Arbitrarily large Steklov frequency with a prescribed embedded boundary](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/112-fixed-embedded-boundary-steklov.md), repository revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

Result: [Large Steklov eigenvalues with a prescribed embedded boundary](paper/manuscript.pdf), Theorem 1.1. The note claims the affirmative alternative for the complete problem statement. The following map uses that finished manuscript and the public target.

| Original requirement | Result and location in the paper | Coverage |
| --- | --- | --- |
| Every integer $`d\geq1`$ and $`m\geq d+2`$ | Theorem 1.1; Proposition 2.3 requires filling dimension $`n=d+1\geq2`$ and $`m>n`$; Section 3 treats $`n\geq3`$ and $`n=2`$ | Entire stated dimension/codimension range, including filling codimension one |
| Arbitrary smooth compact connected embedded $`\Sigma^d\subset\mathbb R^m`$, without boundary, admitting at least one smooth compact connected embedded filling | Theorem 1.1; Section 3.1 starts from any such filling. Section 3.2 constructs orientable fillings for every embedded curve and then adds local handles | Every admissible prescribed boundary; no symmetry, unknot or special-position condition |
| The same ambient $`\mathbb R^m`$ and exact boundary $`\partial\Omega=\Sigma`$ | Lemma 2.2 and Proposition 2.3 fix the initial embedding on a neighborhood of the whole boundary; both applications use embeddings into the original ambient space | Pointwise prescribed ambient boundary, not merely an isometric boundary copy |
| Smooth compact connected embedded $`(d+1)`$-dimensional filling | Lemma 2.2 proves smooth embedding and global injectivity; Section 3 takes the image of a compact connected filling | All original regularity, domain topology and embeddedness requirements |
| The final metric is Euclidean induced | Theorem 1.1; Proposition 2.3; Section 3.2 restores original coordinates after the topological graph construction | No replacement of the final ambient metric |
| First positive Steklov eigenvalue with $`\Delta u=0`$, $`\partial_\nu u=\sigma u`$ | Introduction defines $`0=\sigma_0<\sigma_1`$; Section 2 gives the quotient and explicitly translates the source indexing | Same boundary-value problem and first positive eigenvalue |
| For every fixed admissible $`\Sigma`$, the supremum over all such fillings is infinite | For each $`A>0`$, Theorem 1.1 and the end of Section 3 yield $`\sigma_1(\Omega)>A`$; the paragraph after Theorem 1.1 states the equivalent supremum | Complete affirmative conclusion; no bound is claimed uniformly over $`\Sigma`$ |
| No volume or topology bound | Theorem 1.1 and its following paragraph; Section 3.1 keeps one filling, while Section 3.2 permits arbitrarily large genus | No additional bound imposed |

The collar width and approximation parameters may depend on the chosen intrinsic metric and threshold. No limit of the final embedded domains is required. Constants in the surface source estimate are independent of its genus index, as stated where used.

## Imported results and the added application

| Public dependency | Exact role and paper location | Applicability |
| --- | --- | --- |
| [Colbois–El Soufi–Girouard, arXiv:1701.04125v2](https://arxiv.org/abs/1701.04125v2), Theorem 1.1(ii) | Intrinsic fixed-boundary unboundedness in filling dimension at least three, Section 3.1 | Applied to the initial filling; its first positive index is explicitly translated |
| [Colbois–Girouard–Raveendran, arXiv:1612.07665v1](https://arxiv.org/abs/1612.07665v1), Theorem 7 and Section 6.4, Figure 5, Remark 37 | Connected-boundary high-genus surface metrics, Section 3.2 | The note explains the orientable gluing choice, exact length scaling and extension of the boundary arclength map |
| [Eliashberg–Mishachev, author-hosted text](https://virtualmath1.stanford.edu/~eliash/Public/257B-2020/intro.pdf), Lemmas 21.3.1 and 21.6.1; Lemma 17.5.1(c),(d) and its endpoint-relative remark | Primitive decomposition and local embedding approximation, Lemma 2.2 | The note supplies the relative-face application, smooth amplitudes, global separation and finite error argument for every $`m>n`$ |
| Hirsch, *Differential Topology*, Section 6.2 and Theorems 4.5.1, 8.1.3, 3.2.7 and 9.3.7; Seifert, *Über das Geschlecht von Knoten*, Section 1 | Collars, smooth topology and arbitrary-curve fillings, Sections 2.3 and 3.2 | The note gives the projection, graph extension, local handle and boundary-map arguments at their uses; full bibliographic links are in the paper |
| [Girouard, joint work with Polymerakis, Oberwolfach Report 36/2023](https://ems.press/content/serial-article-files/47475), printed p. 2075 | Earlier announcement of the same relative Nash–Kuiper mechanism | Credited in the abstract and introduction; no priority or new-mechanism claim |

The note's added work is the written relative smooth approximation and its exact-boundary application throughout the stated codimension range, including arbitrary embedded curves. It is an analytic proof claim. Independent mathematical review remains requested; document compilation and successful filing do not imply acceptance.
