# AIM 627: an order-six periodic Costas counterexample

**PR:** [124](https://github.com/MColbrook/AIM/pull/124). **Head:** `dd18040eb5e89b0fd13c6a233839e40783332b9c`. **Date:** 2026-10-15. **Decision:** Solved by counterexample.

Independent Codex AI review in the maintainer's session, without developing the submission; no human or Lean verification is claimed. The complete three-page source/PDF, README and target comparison were checked against the pinned/current target.

[Proof](../../solutions/627-periodic-costas/paper/main.pdf).

Both coordinate columns enumerate the entire two-by-three input/output box. I recomputed the 30 ordered differences, keeping the two binary signs and reducing only the two ternary coordinates. All 30 resulting keys are distinct, agreeing with the complete printed table and its reversed rows. In every translated window, the representative map is a bijection because each coordinate interval contains exactly one representative of each residue. Each binary coordinate changes differences by one fixed sign depending only on that window, while ternary differences retain their residues. Thus equality of ordinary differences in any window implies equality of the mixed key and hence of the original ordered pair. The argument covers every integer offset, including negative offsets; it never substitutes full toroidal difference uniqueness for the required ordinary-vector property.

As an additional independent exact control, a standard-library Python enumeration checked all 36 distinct coordinate-offset residues. Each window has six points and exactly 30 distinct nonzero ordered ordinary differences. This finite check supports the table, while the representative-map argument supplies the all-offset proof. The dimension is four, both products are six, every side is at least two, and input/output factor counts are two. Thus all premises hold and the conjectured conclusion four fails.

Both references were checked. [Rubio--Torres v1](https://arxiv.org/pdf/2208.02378v1) gives the actual bijective definitions and Conjecture 1. The [Prove2Me record](https://prove2.me/theorems/f2732909-8aec-45d0-afe0-8943f5d2c80e) really records shivm's earlier 4 October 2026 disproof announcement. That record is credited as an announcement only; its formal proof was not replayed, and this submission supplies its own short analytic witness. All three PDF pages, including both complete tables, were visually inspected and are legible and consistent with the source. Build/hash receipts are separate integration evidence.

No unresolved gap was identified. This is a complete counterexample to the universal necessity assertion, not a classification, minimality result or Lean-verified submission.
