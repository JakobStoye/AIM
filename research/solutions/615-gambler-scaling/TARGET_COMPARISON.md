# AIM 615: correspondence with the original target

Original problem: [Fourth-order diffusion approximation for three-player ruin](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/615-gambler-scaling.md), repository revision `c9929805cece044705abaaebe1cebddac1ba11a6`.

Proof: [manuscript](paper/gambler_scaling.pdf), [editable source](paper/gambler_scaling.tex).

| Original requirement | Manuscript location and result | Scope |
|---|---|---|
| Positive integer capitals A, B, C; N=A+B+C | Section 1, Theorem 1 | Every fixed positive triple |
| Uniform surviving pair, fair coin, one-unit transfer, removal at zero | Sections 1 and 2: six equally likely steps and two-player boundary payoff (1) | Exact original process |
| Winner listed last; each order in S3 | Section 1 definition and relabeling at the end of the proof | All six orders |
| Brownian scaling limit | Section 2, equation (2), from Diaconis--Ethier Theorem 4.1 | Exact limit under q=2z/M-1 |
| Absolute error O((nN)^-4) as integer n tends to infinity | Theorem 1 and final bound in Section 4 | Complete infinite scaling ray; no additional hypothesis |
| Constant may depend on proportions and order | Final coefficient K N^4/(B^2+BC+C^2)^2, after relabeling | Permitted dependence only |
| Known cubic bound is insufficient | Section 1 credits Denisov--Wachtel Proposition 5 | The manuscript adds the angular defect, explicit barrier and finite comparison |
| Imported harmonic theorems | Section 2: HFT Theorems 4.12, 2.3, 2.4, 1.27--1.28 and Corollary 1.10 | Affine subtraction gives zero traces; reflected corner functions are bounded; derivative balls are uniform after normalization |

The proof is analytic. No numerical experiment or finite certificate is a premise. It does not assert a leading error coefficient, optimality, a biased process or a four-player extension.

Status: complete solution claim submitted for review. A successful build or agreement from an AI reviewer does not establish mathematical acceptance.
