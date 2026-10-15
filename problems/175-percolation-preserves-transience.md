# 175. Does supercritical percolation preserve transience?

**Area:** Diffusion in diluted networks

**Status:** 🟡 PARTIAL

**Last checked:** 2026-10-16

## Problem statement

Let $`G`$ be the Cayley graph of an infinite finitely generated group with a finite symmetric generating set. Assume simple random walk on $`G`$ is transient. For $`p>p_c(G)`$ retain each edge independently with probability $`p`$, where $`p_c(G)`$ is the infimum of parameters giving an infinite open component with positive probability. Must simple random walk on every infinite open component be transient, almost surely? Transience means that a walk starting at any vertex returns to it only finitely often almost surely.

## Application

Random deletion of conducting bonds can create trapping and bottlenecks. The question asks whether dilution above the connectivity threshold can change long-time diffusion from transient to recurrent.

## References

- [Russell Lyons and Yuval Peres, *Probability on Trees and Networks* (Cambridge, 2016; paperback 2021), online revision of 19 August 2026](https://rdlyons.pages.iu.edu/prbtree/book_pb.pdf), §6.9, Conjecture 6.44.
- [Itai Benjamini, Russell Lyons and Oded Schramm, *Percolation Perturbations in Potential Theory and Random Walks* (1999)](https://arxiv.org/abs/math/9804010), original general questions and partial results.

## Status review

**Resolution-source report (2026-10-16):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-16-prior-resolutions.md#aim-175). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-08)

**Known cases:** Supercritical percolation preserves transience on Euclidean lattices in transient dimensions and on the cited nonamenable classes.

**Remaining target:** Preservation of transience on every transient Cayley graph at every strictly supercritical parameter.

**Literature check:** Open in cited literature; no later resolution located.

The updated book retains the conjecture. It is known for Euclidean lattices in transient dimensions and for important nonamenable classes; those results do not cover all transient Cayley graphs. This entry restricts to strictly supercritical parameters and does not assert anything at criticality.

Search topics checked on 2026-09-08: `percolation transience Cayley conjecture 2025 2026; percolation preserves transience solved`. No later resolution of the exact statement was located; this is not a certification that no proof exists.
