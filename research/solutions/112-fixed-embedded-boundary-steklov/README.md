# Large Steklov eigenvalues with a prescribed embedded boundary

Kaiwen Jin · [Manuscript](paper/manuscript.pdf) · [Editable source](paper/manuscript.tex)

This note proposes a complete affirmative resolution of [AIM Problem 112](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/112-fixed-embedded-boundary-steklov.md), at target revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.
For every integer $`d\geq1`$, every $`m\geq d+2`$, and every smooth compact connected embedded boundary $`\Sigma^d\subset\mathbb R^m`$ that admits a smooth compact connected embedded filling, Theorem 1.1 gives such a filling $`\Omega`$ with $`\partial\Omega=\Sigma`$ and $`\sigma_1(\Omega)>A`$ for each $`A>0`$. The ambient space and boundary subset are exact, and the metric on the final filling is induced by the original Euclidean metric. Volume and topology are unrestricted.

The proof transfers intrinsic large-eigenvalue metrics to smooth embeddings fixed near the boundary. It follows the relative Nash–Kuiper mechanism [announced by Girouard and Polymerakis](https://ems.press/content/serial-article-files/47475), printed p. 2075, and writes out the relative approximation and arbitrary-curve application. No priority or new-mechanism claim is made. Sections 2–3 contain the complete analytic argument and its cited dependencies. There are no numerical experiments or computer-assisted certificates.

The [target comparison](TARGET_COMPARISON.md) maps each original requirement to the paper. [Build instructions](BUILD.md) reproduce the PDF from the self-contained source. `PUBLIC_MANIFEST.json` describes the selected files; `SHA256SUMS` checks their integrity.

OpenAI's Codex assisted with the argument, source checking and writing. An earlier draft received two separate fresh-context Codex evaluations, one for reader comprehension and one for referee-style objections, followed by revision and final checks by the manuscript-preparation agent. These were AI evaluations; no independent human review or formal verification is claimed. No separate detailed AI review report is submitted. Independent mathematical review is requested. This is a proposed solution claim, and catalogue classification is left to the maintainers.
