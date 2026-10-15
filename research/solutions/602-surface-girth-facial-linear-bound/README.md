# A uniform linear bound for facial cycles on surfaces

Author: Kaiwen Jin.

This analytic research note proposes a complete affirmative answer to [AIM problem 602](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/602-surface-girth-facial-linear-bound.md), at repository revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

Theorem 1 states that a facial cycle has length at most `100000 g ell` in every finite simple graph of girth at least `ell >= 3` that is maximal for its fixed crossing-free embedding on an orientable surface with `g >= 1` handles or a nonorientable surface with `g >= 1` crosscaps. The constant is common to both surface types. The theorem includes disconnected graphs and noncellular embeddings. The cycle must form the entire boundary of one face.

The proof bounds equal-radius ball traces by controlling alternating disjoint shortest-path trees on a designated face. The fractional ball-packing theorem of Bousquet et al. and the hypergraph covering estimate of Ding, Seymour and Winkler then give O(g) centers. After subdivision, the girth condition makes the relevant balls trees; an Euler count bounds the number of short boundary runs.

## Materials

- [Complete paper](paper/manuscript.pdf) and [editable LaTeX source](paper/manuscript.tex).
- [Target comparison](TARGET_COMPARISON.md), including the exact imported theorem interfaces.
- [Manifest](PUBLIC_MANIFEST.json) and [SHA-256 checksums](SHA256SUMS).

The paper contains the complete analytic argument and cites its public mathematical dependencies. No numerical evidence, software experiment or formal proof is used.

## Build

Compile the standalone source twice with a standard TeX Live installation:

```sh
cd paper
pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex
pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex
```

The source uses standard LaTeX packages and an inline bibliography; no additional manuscript assets are needed. Local compilation and rendered-page checks validate the artifact, not the mathematical theorem.

## AI use and review

OpenAI Codex was used for literature searches, developing the argument, drafting and checking the mathematical text. An AI reviewer in a fresh Codex context read the unchanged eight-page manuscript and checked all five public references and 13 citation uses. The reviewer found no major objection and requested no correction. The reviewer did not participate in preparing the manuscript. This was one review by the same vendor, with an instructed reading boundary in a shared workspace and no hard filesystem isolation. No separate detailed AI report is submitted. Independent mathematical review is requested. This package is a complete solution claim; catalogue classification is left to maintainer review.

## Sources and credit

The original facial-cycle question and the quadratic girth bound are due to Axenovich, Kießle, Sagdeev and Zhukovskii. The ball-piercing and nearest-center strategy is credited to Pálvölgyi and Zólomy, who prove a linear girth bound for fixed orientable genus. The paper supplies a quantitative facial trace count and the topological/genus lifts needed for its uniform bound; the published hypergraph estimates are cited at their precise versions.

The target was selected from *AIM — Open Applied Problems*, curated by Steve Brunton, Matthew J. Colbrook, Maarten V. de Hoop, George Stepaniants, Alex Townsend and Rachel Ward, at the repository revision linked above. This submission makes no claim of optimal constants or novelty beyond the bounded source comparison in the paper.
