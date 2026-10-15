# AIM 529: Limiting Betti-number distributions

Proposed analytic resolution by **Kaiwen Jin** (`yui.ui.siki@gmail.com`).
The target is [AIM problem 529](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/529-preferential-attachment-betti-limit.md)
at repository revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

For every fixed `q >= 2`, `m >= 2q`, `delta > -m` with
`x = (m + delta)/(2m + delta) < 1/(2q)`, the manuscript claims a
nondegenerate limit for the finite rational Betti number normalized by its
ensemble mean. The law is `W = A/E[A]`, where `A` is the convergent weighted
sum of induced octahedral bases in an exact independent-Beta construction
of the prescribed sequential graph process. Theorem 2.2 specifies the
construction and proves convergence in `L1` after normalization by
`T^(1-2qx)`, together with the exact asymptotic ensemble mean.

The limiting law has every positive moment finite. This refutes the
proposed regularly varying upper tail with any finite positive exponent
throughout the strict regime. The paper does not determine an exact
upper-tail asymptotic or address the critical boundary `x = 1/(2q)`.

| Material | Purpose |
| --- | --- |
| [paper/main.pdf](paper/main.pdf) | Complete manuscript |
| [paper/main.tex](paper/main.tex) | Standalone editable source with bibliography |
| [TARGET_COMPARISON.md](TARGET_COMPARISON.md) | Clause-by-clause correspondence with the public target |
| `PUBLIC_MANIFEST.json`, `SHA256SUMS` | File inventory and content hashes |

The argument is analytic. It uses no numerical experiment, computer-assisted
certificate or proof-assistant formalization. Compile the standalone source
with a standard LaTeX distribution, for example `latexmk -pdf paper/main.tex`.

OpenAI Codex assisted extensively with the argument, literature checks and
manuscript preparation, as disclosed in the paper. AI manuscript review was
performed in fresh contexts of the same vendor, with physical filesystem
isolation unverified. No independent human review has been performed.
This is a complete mathematical claim offered for independent review;
submission and successful LaTeX compilation do not establish acceptance.
No separate detailed AI referee report is included.
