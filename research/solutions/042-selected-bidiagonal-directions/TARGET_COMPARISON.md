# Comparison with problem 042

This comparison uses the accompanying finished manuscript and the
[original public problem at its fixed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/042-accurate-bidiagonal-svd.md).
The contribution is an analytic floating-arithmetic construction, accompanied
by research software and ordinary finite numerical validation.

| Original requirement | Finished manuscript | Scope and interpretation |
| --- | --- | --- |
| Real upper bidiagonal input, including signed entries | Section 2; Theorem 2.1 | The stored binary64 input is the mathematical input. Reducible, singular and repeated-value cases are included. |
| Any k distinct requested ordered ranks | Section 2 and Algorithm 1 | 1 <= k <= n; output order follows the caller's requested ranks. Repeated values allow the stated orthonormal-basis freedom. |
| Unit left and right vectors | Equation (1), Theorem 2.1 | A nonzero floating carrier x represents the exact direction x/sqrt(x^T x). This convention is explicit; the raw array is not claimed to have exactly unit norm. |
| Nonnegative estimates and ordered-value accuracy | Theorem 2.1, equation (2); Section 6 | The common error constant is 128 for represented unit directions. |
| Both singular-vector equations | Theorem 2.1, equation (3); Section 6 | Both residuals are at most 128 n epsilon \|\|B\|\|_2, including the zero-value branch. |
| Separate left and right orthogonality, independent of gaps/clusters | Theorem 2.1, equation (4); Sections 4 and 6 | Pairwise inner products are at most 128 n epsilon. The common near-zero cut handles the mixed left-direction products. |
| O(nk) arithmetic work | Algorithm 1 cost discussion; Theorem 2.1; Sections 3-6 | Fixed-format interpretation: O(p^4 nk) operations on O(p)-bit numbers, conservatively O(p^6 nk) bit work. This is O(nk) in n,k after fixing p; no precision-uniform O(nk) claim is made. |
| Small epsilon n; exclude overflow/underflow | Section 2 | epsilon=2^-p, integer 16 <= p <= 53, n epsilon <= 1/64. Correct rounding, protected exact indices and power-of-two scaling are specified. Binary64 input/output storage is fixed. |
| Actual floating arrays | Corollary 6.1 | Raw arrays satisfy value/residual/orthogonality bounds with conservative constant 256 and squared-norm defect at most 8 epsilon. This is distinct from exact unit-direction semantics. |
| Public mathematical dependencies | References [4]-[5] at their printed theorem locators | The finite-dimensional spectral theorem and Cauchy derivative estimate are used under the stated finite-dimensional/analytic hypotheses. The construction and rounding bounds are in the manuscript. |

The sufficient core precision is 67584+2880p bits, or 220224 bits at p=53.
The paper claims a fixed-format complexity construction, not practical speed
superiority. The Python/C++ implementation has finite allocation, index and
resource limits, documented separately. Its optional exact rational checker
validates an individual original input/output pair at additional cost; tests
and the two fixed matrices do not prove the universal theorem.

The claim is submitted for independent mathematical review under the explicit
arithmetic and represented-direction conventions above. No extension to
complex matrices, formal verification, independent human certification, or
repository acceptance is asserted.
