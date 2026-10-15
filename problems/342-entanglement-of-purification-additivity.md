# 342. Additivity of entanglement of purification

**Area:** Quantum information and correlation preparation

**Status:** 🔵 OPEN

**Last checked:** 2026-10-16

## Problem statement

Let $`A,B,C,D`$ be arbitrary finite-dimensional complex Hilbert spaces. A density operator is a positive semidefinite operator of trace one. For a density operator $`\rho_{AB}`$, define its entanglement of purification by

```math
E_P(A:B)_\rho=
\min_{A',B',\,\psi}
S\!\left(\mathop{\mathrm{Tr}}\nolimits_{BB'}|\psi\rangle\langle\psi|\right),
\qquad
\mathop{\mathrm{Tr}}\nolimits_{A'B'}|\psi\rangle\langle\psi|=\rho_{AB}.
```

The minimum ranges over finite-dimensional auxiliary spaces $`A',B'`$ and unit vectors $`\psi`$ on $`A\otimes A'\otimes B\otimes B'`$. Here $`\mathop{\mathrm{Tr}}\nolimits`$ with subsystem subscripts denotes partial trace, and

```math
S(\tau)=-\mathop{\mathrm{Tr}}\nolimits(\tau\log_2\tau),\qquad 0\log_2 0=0,
```

is the von Neumann entropy. The minimum is attained; no particular purification or auxiliary dimension is prescribed in the optimization.

For every pair of density operators $`\rho_{AB}`$ and $`\sigma_{CD}`$, is

```math
E_P(AC:BD)_{\rho\otimes\sigma}
=E_P(A:B)_\rho+E_P(C:D)_\sigma?
```

The left-hand side groups $`A,C`$ with one party and $`B,D`$ with the other, and allows arbitrary joint purifications. Products of separate minimizing purifications give the $`\le`$ direction. The question is whether strict inequality ever occurs. It concerns the ordinary von Neumann entropy and includes all mixed states; classical states and identical factors are special cases of this one question.

## Application

Two separated laboratories can prepare many copies of a correlated state using shared maximally entangled qubit pairs, local operations and a communication rate tending to zero. The optimal asymptotic number of pairs consumed per copy is

```math
E_P^\infty(A:B)_\rho
=\lim_{n\to\infty}\frac{1}{n}E_P(A^n:B^n)_{\rho^{\otimes n}}.
```

This is a cost for creating both classical and quantum correlations. General additivity would identify it with the one-copy quantity $`E_P`$. A rigorous counterexample would show that optimizing preparations jointly can save resources relative to separate purifications. The operational result concerns vanishing communication rate, with preparation error tending to zero.

## References

1. Barbara M. Terhal, Michał Horodecki, Debbie W. Leung and David P. DiVincenzo, *The entanglement of purification*, Journal of Mathematical Physics 43 (2002), 4286–4298, DOI [10.1063/1.1498001](https://doi.org/10.1063/1.1498001). [Author manuscript v3](https://arxiv.org/pdf/quant-ph/0202044v3), May 1, 2002, §I equation (1); §II Definition 1, Lemma 1 and Theorem 2.
2. Jianxin Chen and Andreas Winter, *Non-Additivity of the Entanglement of Purification (Beyond Reasonable Doubt)*, [preprint v1](https://arxiv.org/pdf/1206.1307v1), June 6, 2012. §I Definition 1 and the general additivity question; §II Theorem 3 and Corollary 4; §§III–IV numerical evidence and the remaining rigorous-proof question.
3. Shrobona Bagchi and Arun Kumar Pati, *Monogamy, polygamy, and other properties of entanglement of purification*, Physical Review A 91 (2015), 042323. [Author manuscript v3](https://arxiv.org/pdf/1502.01272v3), submitted November 15, 2015, §VI Theorem 2 and final paragraph. The product-purification upper bound is the relevant part here.
4. Shokoufe Faraji and Zahra Baghali Khanian, *Additivity Results for the Rényi-2 Entanglement of Purification*, [preprint v1](https://arxiv.org/html/2605.15439v1), May 14, 2026. §I equations (1)–(12), §III Theorem 32, §IV Proposition 33 and §V.
5. Amir-Reza Negari and Zahra Baghali Khanian, *Rényi Entanglement of Purification Is Non-additive*, [preprint v1](https://arxiv.org/html/2608.28897v1), August 28, 2026. §I, Theorems 1–3, Appendix C.2 and §V Outlook.

## Status review

**Resolution-source report (2026-10-16):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-16-prior-resolutions.md#aim-342). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-19)

**Literature check:** Open in cited literature; no later resolution located.

Chen–Winter explicitly formulate the general question and give strong numerical evidence against additivity for two-qubit Werner states. Their Theorem 3 proves a convexity property of the regularized quantity minus entropy. The numerical minimization supplies feasible upper bounds; the missing rigorous lower bound for the one-copy optimum is acknowledged in §IV. Their title therefore does not constitute a rigorous counterexample to the displayed equality. Bagchi–Pati prove the general upper-bound direction and retain the strict-inequality question.

The August 2026 Negari–Baghali Khanian preprint explicitly retains the von Neumann problem. Its analytic counterexamples apply to Rényi orders $`0\le\alpha<1`$. Appendix C.2 explains why the construction does not pass uniformly to $`\alpha=1`$. Its additivity theorem concerns $`\alpha\ge2`$ and a classical two-qubit factor. Its exact one-copy formula for classical two-qubit states does not solve the joint optimization for their tensor products. Faraji–Baghali Khanian prove order-two results for specified channel families; §V leaves the Werner-state channel reformulation unresolved. These results do not decide the general von Neumann equality.

The September 19 searches covered proofs, disproofs, numerical certificates, tensor-product formulations, author and citation chains, unrestricted dates, 2024–2026 results, and revisions or corrections. The cited full-text locations were read. ArXiv histories and author publication pages were checked; publisher texts were not line-compared. A separated adversarial self-pass passed on September 19; no independent agent or human review occurred. The [evidence ledger](../research/expansion-2026-09/candidates/entanglement-of-purification-additivity.json) records the exact comparisons and the distinction from the catalogue's [amplitude-damping additivity question](207-amplitude-damping-additivity.md), [quantum entropy cone](035-quantum-entropy-cone.md) and [NPT bound entanglement](032-npt-bound-entanglement.md).
