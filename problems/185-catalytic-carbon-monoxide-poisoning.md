# 185. Selection of the carbon-monoxide poisoning phase

**Area:** Catalytic surface reactions

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Consider states $`0`$ (vacant), $`1`$ (CO) and $`2`$ (oxygen) on $`\mathbb Z^2`$. A vacant site becomes $`1`$ at rate $`p`$. Each unordered nearest-neighbor pair in state $`(0,0)`$ changes to $`(2,2)`$ at rate $`q/4`$, and each pair containing one $`1`$ and one $`2`$ changes to $`(0,0)`$ at rate $`r/4`$. Each pair also exchanges its states at rate $`\gamma`$. Assume $`p>q>0`$, $`0<r<\infty`$ and $`0<\gamma<\infty`$.

Let the initial site states be independent and identically distributed with $`P(\eta_0(0)=1)>0`$. For every such initial law and every choice of the parameters above, is it true that, for every finite $`K\subset\mathbb Z^2`$,

```math
\lim_{t\to\infty}P(\eta_t(x)=1\text{ for all }x\in K)=1?
```

## Application

A surface poisoned by CO can no longer oxidize the pollutant. The statement asks whether sufficiently large CO input selects this absorbing phase from every independent initial mixture with positive CO density.

## References

- [Rick Durrett, *Interacting Particle Systems: Ideas, Techniques, Applications*, book manuscript of 2 September 2026](https://sites.math.duke.edu/~rtd/PASTA/PASTA0902.pdf), §5.4, Open Problem 5.4.6.
- [Rick Durrett and Glen Swindle, *Coexistence results for catalysts* (1994)](https://doi.org/10.1007/BF01192836), model and poisoning estimates.

## Status review

Reviewed 15 October 2026 against the original target in [PR #144](https://github.com/MColbrook/AIM/pull/144). The stirred catalytic model poisons to CO almost surely at every site for every admitted iid law with positive CO density.

[Proof or source](../research/solutions/185-catalytic-carbon-monoxide-poisoning/paper/manuscript.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/185-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** The stirred catalytic model poisons to CO almost surely at every site for every admitted iid law with positive CO density.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

The book proves clustering into the two poisoned states under translation-invariant initial laws, but leaves selection of the CO state open. This entry takes independent positive-CO-density initial laws and positive finite stirring, within the setting of the original conjecture. Strict $`p>q`$ avoids the borderline parameter. Reaction rate $`r`$ is finite; results for monatomic arrivals or instantaneous reactions address different models.

Search topics checked on 2026-09-08: catalytic surface CO poisoning Durrett Swindle open problem; catalyst model poisoning convergence 2026; Grannan Swindle monatomic instantaneous reaction versus diatomic finite reaction.
