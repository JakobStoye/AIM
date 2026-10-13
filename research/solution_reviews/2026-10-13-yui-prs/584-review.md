# Independent review of AIM 584: nonextension to a branched ray

**Date:** 2026-10-13  
**Submission:** [PR #80](https://github.com/MColbrook/AIM/pull/80), Kaiwen Jin  
**Reviewed head:** `0415b9d841373ea4b7bd78b9d5e84adc9c569b6d`  
**AIM statement:** problem 584 at `c9929805cece044705abaaebe1cebddac1ba11a6`  
**Reviewer:** independent Codex AI review in the maintainer's session; separate from the submission's development. No human or Lean verification is claimed.  
**Decision:** **Solved by a computer-assisted nonexistence proof**.

[Manuscript](../../solutions/584-four-color-branched-ray/paper/main.pdf) · [Source](../../solutions/584-four-color-branched-ray/paper/main.tex)

## Target comparison

The proof concerns exactly a root with two one-vertex leaves and one infinite ray. It assumes proper four colors, independence of arbitrary sets at distance greater than one, color symmetry, and a common stationary reflection-invariant line law on every ordered path. The line law is arbitrary; the proof does not prescribe the Holroyd--Liggett law. It establishes nonexistence on this graph, and restriction extends the obstruction when either finite arm is lengthened. No obstruction on a fixed finite truncation is asserted.

## Analytic premises independently checked

One-site colors are uniform, and nonadjacent endpoint/neighbor sets are jointly independent: apply the arbitrary-set independence property successively to a singleton and the remaining set. Color permutations fixing specified endpoint colors give the correct two- and three-site specified-color probabilities. For the star, all three neighbors are jointly uniform independent, and the unused root colors are equiprobable. These are probabilities of particular assignments, not orbit masses.

Summing a deleted line site separates its left and right blocks by distance two. Summing a leaf gives the indicated line marginal; summing the root makes both leaves independent of the ray and supplies the factor 1/16. Deleting a ray site likewise separates the prefix from the suffix. Properness sets exactly the prohibited adjacent-color words to zero. Reflection is used only for line words; ordered leaves are retained. All multiplicities over the four actual colors are included.

The crucial infinite-ray inequality was reconstructed directly. For a specified connected prefix event E, let P be its probability, Q the probability of E followed by a specified color c, and a_n the probability of E followed by n vertices avoiding c. Properness permits dropping the immediate predecessor when the last vertex has color c; all remaining restricted vertices are then at distance at least two from it. Thus:

```math
a_n=a_{n-1}-\frac14 a_{n-2},\qquad
a_n=2^{-n}\big((n+1)P-2nQ\big).
```

Nonnegativity for arbitrarily large n implies Q at most P/2. This uses the actual infinite continuation and is valid for a branched prefix as well as a line prefix, including P=0.

## Exact finite calculation and its semantics

The entire submitted `probability_rules.py` and `verify_certificate.py` implementations were inspected before execution (362 source lines). Canonicalization is legitimate under color relabeling and line reflection, and retains the leaf order. The short-cylinder system contains all its stated marginal and erasure identities. Exact Gaussian elimination attains rank 78; every redundant original equation is rechecked after substitution. It yields the five displayed short entries, alpha and gamma intervals, and no gamma coefficient in line entries.

The only nonlinear products required at the stated lengths have both nonfixed factors in the short table: line factors each have length four or five; a branched prefix has two or three ray vertices and the line suffix length four or five. Their product is therefore affine in the four actual moments alpha, gamma, alpha squared, and alpha times gamma. No gamma squared term is needed, and no assumption is made that arbitrary choices of those moments realize a process.

Every nonnegative expression has a verified probabilistic or algebraic meaning: a specified cylinder probability, its independent-set upper bound, a moment and its upper bound, the proved half-prefix inequality, or the square of alpha minus a fixed rational center. The independent vertex sets are odd line positions or both leaves plus odd ray positions. Repeated specified colors do not weaken independence. Each multiplier is checked nonnegative, and all coefficients are accumulated as exact fractions.

The replay returns 8,245 weighted equations, 7,244 nonnegative expressions, 8,298 probability/moment symbols, and zero nonzero coefficients. The resulting constant is negative with exact positive margin:

```math
D=\frac{4663173554073621650668701}{229601458397122150289899520}>\frac1{50}.
```

The sum of nonnegative expressions and zero identities cannot equal this negative constant. This independently audited rule-to-probability mapping, together with the exact arithmetic replay, completes the nonexistence proof. A passing arithmetic replay alone would not have sufficed without the analytic and semantic audit above.

## Reproduction and ancillary material

In the submitted package at the reviewed head, with Python 3.12.14:

```text
python -B src/verify_certificate.py certificate/farkas.json
python -B -m unittest discover -s test -v
```

The certificate replay returned `EXACT_CERTIFICATE_REPLAY_PASSED` and all 12 tests passed. Controls include the published line recursion, star marginal values, independent-set bounds, leaf-order retention, short affine entries, invalid adjacency/deletion rejection, and deliberate corruptions of multipliers and the claimed margin. The certificate SHA-256 is `c64ca628b2ea2b324a840827ef7571b9d68f2a8fd4039c7c0baab43581bf4f67`, matching the manuscript. The decimal margin and timings are informational; no tolerance or optimizer enters the proof.

## Reference audit

Both manuscript references were checked. [Holroyd and Liggett, arXiv:1403.2448v4 (2015)](https://arxiv.org/html/1403.2448v4) has the claimed stationary one-dependent four-coloring and reflection/color symmetry in Theorem 4; the published article is Forum of Mathematics, Pi 4 (2016), e9. [Liggett and Tang, arXiv:1804.06877v3 (2023)](https://arxiv.org/html/1804.06877v3) explicitly distinguishes the prescribed-line obstruction after Proposition 1.4 and asks the unrestricted extension question in Section 6, item 1. Its published metadata, Annals of Applied Probability 33(6A) (2023), 4341--4365, match the AIM source. The misleadingly broad wording of the source abstract does not replace the precise proposition/question checked in its body. The submission respects that distinction. The new tail recurrence and finite certificate are derived directly and need no uncited external theorem.

## Conclusion and scope

The original unrestricted-line target is completely ruled out under its stated symmetries and dependence condition. `Solved` is supported by this documented independent AI audit of the analytic premises, finite rule generation, exact certificate and concluding contradiction. It is a computer-assisted mathematical proof, not Lean verification or a claim of external human review.

## Rendered PDF check

All 6 pages of the supplied main PDF were visually inspected against the source presentation. Titles, theorem statements, mathematical tables/equations, proof structure and bibliography agree; no clipped content or unresolved references were found. Root package checks separately parsed all pages and checked payload and archive hashes. Rendering is supplementary artifact evidence, not mathematical or formal verification.
