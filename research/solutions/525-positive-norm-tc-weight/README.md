# AIM 525: proposed counterexample

This package contains a short analytic counterexample to [Maximal TC weight from positive homological norm](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/525-positive-norm-tc-weight.md), at target revision a153f469ee0ea64e876b2ad97c79d252c19a3e22.

For the closed oriented genus-two surface $`S`$, the four-manifold $`M=S\times S`$ is aspherical and its rational fundamental class has homological $`\ell^1`$ seminorm at least 24. Every nonzero $`u\in H^4(M;\mathbb Q)`$ nevertheless satisfies $`\mathop{\mathrm{wgt}}\nolimits_{\mathrm{TC}}(1\times u-u\times1)\le2<4`$. One continuous endpoint map works for every choice of $`u`$; the paper supplies three actual local sections and the nonzero pullback calculation.

- [Complete manuscript](paper/counterexample.pdf)
- [Editable standalone LaTeX source](paper/counterexample.tex)
- [Original-target comparison](TARGET_COMPARISON.md)
- [File manifest](MANIFEST.json)

The argument applies existing results on surface-product simplicial volume and genus to this question. It credits Bucher-Karlsson, Macías-Virgós and Mosquera-Lois, Farber and Grant, and classical topology sources. No new general genus method or priority claim is made.

To compile the standalone source, run:

    latexmk -pdf -interaction=nonstopmode -halt-on-error paper/counterexample.tex

The result is analytic and uses no numerical experiment or proof-critical computation. The supplied PDF and source must agree with the manifest. Compilation checks the document, not mathematical correctness.

Author and manuscript contact: Kaiwen Jin, yui.ui.siki@gmail.com. OpenAI Codex assisted with the argument, source checks, writing, and automated manuscript reviews. No separate detailed AI report is submitted. Independent mathematical review is requested; this package is a counterexample claim awaiting that review.
