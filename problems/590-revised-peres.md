# 590. Can bound entanglement produce a device-independent secret key?

**Area:** Quantum information and cryptography

**Status:** 🟡 PARTIAL

**Last checked:** 2026-10-13

## Problem statement

Let $`\rho_{AB}`$ be a finite-dimensional bipartite bound-entangled state: it is entangled, but its distillable entanglement under local quantum operations and public classical communication is zero.

Prove or disprove that independent copies of $`\rho_{AB}`$ cannot yield a positive asymptotic secret-key rate in any device-independent quantum key distribution protocol. This is the revised Peres conjecture [1, Conjecture 11].

Device-independent security means that the shared output key must approach a uniform key independent of the adversary for every quantum realization consistent with the observed input-output statistics. Local measurements and classical public communication are allowed; the shared quantum resource is the supplied state. The target includes arbitrary protocols, beyond a fixed Bell test or one-way classical processing. Bell nonlocality alone is insufficient to answer this key-generation question.

## Application

The conjecture asks which entanglement resources can support cryptography when measurement devices are untrusted. It would separate ordinary secret-key distillation from key extraction certified solely by observed correlations.

## References

1. R. Arnon-Friedman and F. Leditzky, [Upper Bounds on Device-Independent Quantum Key Distribution Rates and a Revised Peres Conjecture](https://doi.org/10.1109/TIT.2021.3086505), *IEEE Transactions on Information Theory* **67**(10) (2021), 6606–6618. [Author manuscript](https://arxiv.org/pdf/2005.12325), Section III, Conjecture 11; Section II.A defines the security and rate framework.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Entanglement-with-zero-distillable-secret-key-in-local-dimension-ten-September-27-2026/paper.pdf), result family 272 (2026). Statement locator: `build/source/sections/introduction.tex, thm:main-state and operational-extension paragraph`.

## Status review

**Known cases:** The explicit dimension-ten PPT bound-entangled state has zero distillable secret key even with trusted devices, and therefore cannot yield a device-independent secret key. Reference [1, Section III.B] also rules out a specified one-way protocol using the Vertesi–Brunner state and measurements; that earlier result leaves arbitrary protocols open.

**Remaining target:** Decide the prohibition for every finite-dimensional bound-entangled state and arbitrary device-independent protocols.

**Statement comparison:** An explicit PPT entangled state on C10 tensor C10 has zero distillable secret key for arbitrary admitted completed protocols; PPT ensures bound entanglement. A positive device-independent key protocol would give a positive trusted-device key protocol, so this supplies a substantive affirmative case of the target, not its universal conclusion.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-590) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/272.md). docs/272 explicitly excludes the zero-distillable-secret-key statement; only PPT-composition consequences are formalized. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/590-revised-peres.md).
