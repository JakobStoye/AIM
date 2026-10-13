# AIM 562: proposed complete analytic solution

Kaiwen Jin, *Least singular values of independent random tensor columns*.
Contact: yui.ui.siki@gmail.com.

Theorem 1 claims that independent tensor columns with mutually independent,
centered, unit-variance K-subgaussian scalar coordinates satisfy

```math
\mathbb P\{s_{\min}(A)\ge c_K\varepsilon n^{d/2}\}\to1
```

for each fixed epsilon in (0,1/2], when d^2 log(n)/n tends to zero and
m=floor((1-epsilon)n^d). The constant depends only on K.

- [Complete manuscript](paper/main.pdf)
- [Editable LaTeX source](paper/main.tex)
- [Target comparison and source roles](TARGET_COMPARISON.md)
- [Original frozen problem](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/562-tensor-singular-value.md)

This is a complete solution claim awaiting independent mathematical review.
It is not an upstream acceptance or a formal proof. The manuscript includes
its full analytic argument and all required public dependencies.

AI assistance supported argument development, literature checks, calculation
checks and manuscript preparation. No separate detailed AI review report is
submitted. Independent mathematical review is requested.

## Building the manuscript

With a standard LaTeX installation providing the packages used in main.tex:

```sh
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The source is standalone; no private supplement or additional data is needed.
There are no numerical results or code claims. Public-manifest content hashes
identify the exact submitted files.
