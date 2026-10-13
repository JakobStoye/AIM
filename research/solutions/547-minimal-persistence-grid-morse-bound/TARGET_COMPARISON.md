# Target comparison: AIM 547

Original target: [Minimal persistence grids versus homological Morse lower bounds](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/547-minimal-persistence-grid-morse-bound.md), at commit `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

Proposed result: [Theorem 2 of the manuscript](paper/grid_morse_bound.pdf), *Minimal persistence grids and homological Morse bounds*. The comparison below uses the manuscript and the public problem statement.

| Original requirement | Manuscript location and argument | Scope |
|---|---|---|
| Every finite nonempty simplicial complex and every coefficient field | Section 1 fixes arbitrary K and field; Theorem 2 retains them. Its proof uses finite-dimensional linear algebra and chain inclusions. | Full |
| Every integer n >= 1 | Theorem 2 has no upper restriction. Lemma 1 explicitly includes the one-parameter case. | Full |
| Every face-monotone filter, including equal coordinate values | Section 1 and Theorem 2 allow arbitrary coincidences. The proof chooses a minimal element of a finite coordinate slice, without coordinate injectivity. | Full |
| Entire homology tuple from the SAME filter, with ordinary unreduced homology | Section 1 defines all M^q from K_u and its inclusion maps. Section 3 uses the common dimension d to prove injectivity of H_d, including ordinary H_0 when d = 0. | Full |
| Canonical minimal grid from xi_0 and xi_1; no arbitrary sampling or automatically adjoined endpoints | Equation (1) uses exactly their union of supports across the tuple. The ordered integer regrading preserves those coordinate cardinalities. | Full |
| Exact max-zero lower bound with all higher-syzygy subtraction terms | Equations (2)-(3) and the display in Theorem 2 reproduce the prescribed formula. Lemma 1 eliminates higher terms only at the selected grades used in the counting proof. | Full |
| Every coordinate satisfies its cardinality bound | The proof of Theorem 2 assigns each value in a fixed G_j a distinct grade with positive contribution, then applies the same argument to each j. | Full |
| Verified imported mathematical inputs | Section 1 cites the canonical-grid definitions and integer regrading; Section 2 states the Betti/Koszul identity from Harrington--Tillmann--Torras-Perez, Section 1.4. Guidolin--Landi, Theorem 7.3 is cited for the existing Morse quantity. | Source statements checked |

This is a proposed analytic proof of the entire displayed target, including its remaining multiparameter case. Independent mathematical review is requested. The package does not assign a new catalogue status.
