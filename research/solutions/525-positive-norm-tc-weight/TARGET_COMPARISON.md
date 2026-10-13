# Target comparison for AIM 525

Target: [problem 525](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/525-positive-norm-tc-weight.md), revision a153f469ee0ea64e876b2ad97c79d252c19a3e22. The comparison refers to the complete [manuscript](paper/counterexample.pdf), especially Theorem 1, Lemma 1 and equations (1)--(2).

| Original requirement | Manuscript result and location | Scope |
| --- | --- | --- |
| Closed, connected, oriented aspherical $`n`$-manifold | Theorem 1 takes $`M=\Sigma_2\times\Sigma_2`$, with the product orientation; its proof verifies these properties. | One admissible $`n=4`$ counterexample. |
| $`2\le k\le n`$ | Theorem 1 uses $`n=k=4`$. | Within the original range. |
| Rational homology class with positive homological $`\ell^1`$ seminorm | Theorem 1 uses $`\alpha=[M]_{\mathbb Q}`$ and proves $`\|\alpha\|_{1,\mathbb Q}\ge24>0`$. | Rational cycle infimum as specified. Real simplicial volume is used only for a lower bound. |
| $`\bar u=\mathop{\mathrm{pr}}\nolimits_2^*u-\mathop{\mathrm{pr}}\nolimits_1^*u`$ | Defined before Theorem 1 and used in equation (2). | Same class and sign. |
| Compact-open path space and actual endpoint fibration | Equation (1) and its preceding definition use that topology and fibration. Lemma 1 proves continuity of the actual local path sections. | Same fibration and topology. |
| Unreduced genus counts open sets admitting local sections | The first paragraph fixes that convention; Lemma 1 constructs three such sets. | $`\mathop{\mathrm{genus}}\nolimits(F^*e_M)\le3`$; no exact-genus assertion is needed. |
| Integer weight supremum, tested against all topological spaces $`Y`$ | Equation (1) gives the definition. The counterexample uses the permitted choice $`Y=M`$, $`F(z)=(z,h(z))`$, $`h(x,y)=(x,b)`$. | Failure of the universal vanishing property is witnessed by this one $`Y,F`$. |
| A freely chosen nonzero $`u\in H^k(M;\mathbb Q)`$ with weight at least $`k`$ | For **every** nonzero $`u\in H^4(M;\mathbb Q)`$, equation (2) gives $`F^*\bar u=-u\ne0`$, using the same $`F`$. Together with Lemma 1 this gives weight at most 2. | No class choice meets the requested bound. The existential quantifier is refuted. |
| Prove the assertion or give a counterexample | Theorem 1 provides an admissible positive-norm manifold for which the conclusion fails for all nonzero degree-four classes. | Complete counterexample alternative to the universal assertion. |

The positive real simplicial volume is Bucher-Karlsson's Corollary 3, p. 2 of [arXiv:math/0703587v2](https://arxiv.org/abs/math/0703587v2). Rational cycles extend to real cycles without changing their chain norm. Asphericity and ordinary (co)homology facts use Hatcher's *Algebraic Topology* ([consulted electronic text, copyright 2002](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/hatchat.pdf)): Examples 1B.2 and 1B.5, p. 88; Example 1B.14, pp. 93--94; Theorem 3.5, p. 203; and Theorem 3.30, p. 241.

The explicit local-section proof is an application of the existing genus approach expressed by Macías-Virgós--Mosquera-Lois Theorems 2.8 and 3.19 in [arXiv:1810.12591v3](https://arxiv.org/abs/1810.12591v3), pp. 5 and 10--11. Sectional weight is credited to Farber--Grant, Definition 29 of [Symmetric motion planning](https://arxiv.org/abs/math/0610857v1). The particular surface product, endpoint map and degree-four calculation connect these inputs to the original question.

The claim is a natural-language analytic counterexample. The automated checks and reviews used in preparing it are not formal verification, independent human review, or catalogue acceptance.
