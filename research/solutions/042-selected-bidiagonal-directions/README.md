# Selected bidiagonal singular directions: problem 042

Kaiwen Jin, October 15, 2026.

This package submits the analytic construction in
[the complete manuscript](paper/main.pdf), with [editable source](paper/main.tex),
for independent mathematical review. The [target comparison](TARGET_COMPARISON.md)
maps its statements to the original real-matrix problem at revision
`a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

Theorem 2.1 gives ordered singular-value accuracy, both residual equations and
separate left/right orthogonality, uniformly in singular-value gaps. Its exact
unit directions are represented by nonzero floating carriers via
`x/sqrt(x^T x)`; the raw arrays have the distinct bounds of Corollary 6.1.
The model fixes binary64 storage, target bits `16 <= p <= 53`, and
`n 2^-p <= 1/64`, with correctly rounded real primitives and protected indices
and power-of-two scaling, excluding overflow and underflow.

Work is `O(p^4 n k)` operations on `O(p)`-bit numbers, conservatively
`O(p^6 n k)` bit work. It is `O(n k)` in `n,k` after fixing the format.
The sufficient core precision is 220224 bits at `p=53`. Practical speed
superiority, a complex-matrix extension and a precision-uniform linear bound
are not asserted.

The research implementation is hosted separately:

- [Readable solver repository](https://github.com/yuiyuiui/rational-bidiagonal-svd)
- [Fixed source commit](https://github.com/yuiyuiui/rational-bidiagonal-svd/tree/627f07a898376e12ddba1e40d1d84c0610af639a) (`627f07a898376e12ddba1e40d1d84c0610af639a`)
- [Version 0.1.0 release](https://github.com/yuiyuiui/rational-bidiagonal-svd/releases/tag/v0.1.0)
- [Installation, tests and reproduction](https://github.com/yuiyuiui/rational-bidiagonal-svd/blob/627f07a898376e12ddba1e40d1d84c0610af639a/README.md)
- [Effective API parameters](https://github.com/yuiyuiui/rational-bidiagonal-svd/blob/627f07a898376e12ddba1e40d1d84c0610af639a/docs/API.md)
- [Fixed numerical cases and figures](https://github.com/yuiyuiui/rational-bidiagonal-svd/tree/627f07a898376e12ddba1e40d1d84c0610af639a/numerical_case)

The installed package passed 26 API tests. All six configurations of two fixed
matrices passed exact rational instance checks; the final public source also
passed its installed default call and exact check. These observations are
finite software validation and do not establish the universal theorem.

To rebuild the paper, use a standard TeX installation with the packages named
in `paper/main.tex`, then run `latexmk -pdf main.tex` from `paper/`. The source
uses only the included table and figure. The source-only isolated build was
checked against the distributed PDF.

AI agents assisted argument construction, implementation and writing under
the author's direction. A draft received fresh-context AI reader and referee
review, followed by one author revision. No detailed review report is submitted;
independent mathematical review is requested. These checks do not constitute
independent human certification, formal verification or repository acceptance.
Catalogue classification is left to maintainer review.
