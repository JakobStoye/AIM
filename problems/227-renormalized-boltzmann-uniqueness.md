# 227. Uniqueness of entropy-admissible renormalized Boltzmann solutions

**Area:** Rarefied-gas kinetics

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

On $`\mathbb T^3_x\times\mathbb R^3_v`$, consider $`\partial_tf+v\cdot\nabla_x f=Q(f,f)`$, with hard-sphere collisions

```math
Q(f,f)(v)=\int_{\mathbb R^3}\int_{\mathbb S^2}|(v-v_*)\cdot\omega|\,[f(v')f(v_*')-f(v)f(v_*)]\,d\omega\,dv_*,
```

where $`v'=v-[(v-v_*)\cdot\omega]\omega`$ and $`v_*'=v_*+[(v-v_*)\cdot\omega]\omega`$; all factors have the same $`(t,x)`$.

Are two nonnegative renormalized solutions with the same initial datum necessarily equal almost everywhere? Use the DiPerna–Lions finite-mass, finite-energy, finite-entropy class: on every finite time interval, $`\int f(1+|v|^2+|\log f|)\,dx\,dv`$ is bounded, $`Q(f,f)/(1+f)\in L^1_{\mathrm{loc}}`$, and

```math
(\partial_t+v\cdot\nabla_x)\beta(f)=\beta'(f)Q(f,f)
```

holds distributionally for every $`C^1`$ renormalization with $`|\beta'(z)|\leq C/(1+z)`$. Require the initial trace in $`L^1`$, conservation of mass and momentum, the energy inequality, and the entropy inequality $`H(f_t)+\int_0^tD(f_s)ds\leq H(f_0)`$, where $`H(f)=\int f\log f`$ and $`D(f)=-\int Q(f,f)\log f\geq0`$ is interpreted by its nonnegative collision integral.

## Application

This asks whether the natural large-data kinetic theory determines one gas evolution from its initial distribution, without assuming the regularity needed for classical solutions.

## References

- Ronald J. DiPerna and Pierre-Louis Lions, [*On the Cauchy problem for Boltzmann equations: Global existence and weak stability*](https://annals.math.princeton.edu/1989/130-2/p03) (1989), main existence and weak-stability results: the renormalized solution framework.
- Gayoung An and Donghyun Lee, [*Optimal $`C^{1/2}`$ regularity of the Boltzmann equation in non-convex domains*](https://doi.org/10.1007/s40818-026-00243-5) (2026), introduction: explicitly retains general renormalized uniqueness as open.
- Rafael Galeano Andrades and Mario Almanza Caro, [*Uniqueness of solutions to Boltzmann equations*](https://arxiv.org/abs/2006.08011) (2020 preprint), §2, Theorem 2.1 and subsequent contraction assumptions: a claim screened during the status check.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Nonuniqueness-with-local-conservation-for-the-hard-sphere-Boltzmann-equation-October-5-2026/paper.pdf), result family 363 (2026). Statement locator: `build/paper/01-introduction.tex, thm:main and def:admissible`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete counterexample to the original target.

**Statement comparison:** Two distinct global solutions have the same datum, exact target hard-sphere |(v-v*) dot omega| normalization, all weighted Q+ and Q- locally integrable, strong L1 initial traces, all five local conservation laws and entropy dissipation. The paper renormalizes F/M for a fixed Maxwellian. Locally integrable unrenormalized transport/collision equation gives the beta(F) chain rule along characteristics; conserved mass and kinetic energy turn relative entropy into the target absolute entropy inequality. The datum is rough, so this does not resolve smooth-data AIM074.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-227) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/363.md). docs/363 covers the earlier periodic renormalized nonuniqueness theorem, not the later full local-conservation refinement. Comparator BoltzmannNonuniqueness; no local kernel log inspected. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/227-renormalized-boltzmann-uniqueness.md).
