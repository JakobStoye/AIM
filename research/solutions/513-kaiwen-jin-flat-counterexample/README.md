# AIM 513: an oriented flat counterexample

Complete counterexample claim by **Kaiwen Jin** (`yui.ui.siki@gmail.com`),
submitted for mathematical review. This package addresses
[problem 513](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/513-aspherical-motion-planning-center.md)
at AIM revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

The paper constructs a closed connected oriented flat five-manifold with
contractible universal cover and centre rank two. The proposed formula gives
`TC(M)=9`, while a nonzero product of nine degree-one zero divisors gives
ordinary unreduced `TC(M)>=10`. This is the counterexample alternative of
the full target. The exact value of `TC(M)` is not asserted.

| Material | Purpose |
|---|---|
| [Complete paper](paper/main.pdf) | Three-page note containing the full construction and proof |
| [Editable source](paper/main.tex) | Standalone LaTeX source with embedded bibliography |
| [Target comparison](TARGET_COMPARISON.md) | Every original premise and the failed equality |
| [Verification](VERIFICATION.md) | Actual document checks and reproduction command |
| [Manifest](PUBLIC_MANIFEST.json), [SHA-256 sums](SHA256SUMS) | File inventory and integrity |

The proof credits the real Bott cohomology presentation of Kamishima and
Masuda and the zero-divisor lower bound of Farber. It contains the complete
fixed ring calculation and requires no computational certificate or numerical
experiment. It makes no unqualified novelty claim.

To rebuild the PDF with an installed LaTeX distribution:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/main.tex
```

OpenAI Codex assisted with construction search, algebraic checks and drafting;
the manuscript contains the AI-use statement. No separate detailed AI review
report is submitted. Independent mathematical review is requested.
Catalogue classification is left to the receiving maintainers.
