# AIM 520: coarse Hilbert embeddings of persistence diagrams

Kaiwen Jin's note proves the negative classification for every p in [1,2] on the full space of finite persistence-diagram multisets, with the ell-infinity partial-matching Wasserstein metric and no common coordinate or cardinality bound.

- [Complete manuscript](paper/main.pdf)
- [Editable LaTeX source](paper/main.tex)
- [Target comparison](TARGET_COMPARISON.md)

The proof realizes finite rational signed grid families by diagrams using a common background, then applies Naor--Schechtman's signed-grid obstruction and Nowak's finite-subset criterion. The related finite snowflake observation attributed to Austin and Naor is credited in the manuscript.

Build the standalone paper with `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=paper paper/main.tex`. It uses standard LaTeX packages and includes its bibliography. No numerical computation or private supplement is a premise of the proof.

AI use: OpenAI Codex assisted with exploration, proof drafting, source retrieval and editing. The preparation includes fresh-context AI manuscript checks on the same vendor with a shared host filesystem; no independent human review is claimed. No separate detailed AI report is submitted. Independent mathematical review is requested.

This package is submitted as a complete solution claim. Catalogue classification is left to maintainer review.
