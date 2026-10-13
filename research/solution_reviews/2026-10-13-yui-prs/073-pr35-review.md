# PR35: Vlasov-Maxwell literature update

Date:2026-10-13. [PR35](https://github.com/MColbrook/AIM/pull/35), JohnDriscollAcademic. Reviewed head:`3912ba635fc113f45d9ceac7d5c631a26d100033`. This is an independent AI review of an eight-line literature update, not a new complete-proof audit.

## Content and disposition

All proposed lines and links were checked. The published OpenAI theorem at `1581d4cbdd69a0faf34b2089614fe2a814316a6a`, `build/sections/introduction.tex` labels `eq:data` and `thm:global`, has exactly the original one-species three-dimensional relativistic normalization, nonnegative compact smooth particle data, bounded-smooth finite-energy fields and both Gauss constraints. It gives smoothness and compact phase-space support on every finite horizon and classical uniqueness, without size, symmetry or neutrality restrictions. This supports the same complete-target source comparison already committed in AIM `1b7c7fd251c1643bb41f0e3cef38704bcef410fd`.

AIM073 is already Solved with pinned manuscript PDF, theorem comparison and upstream Lean-scope links. The PR's append-only update duplicates that information and would follow historical open-status text in its old base. Close as already addressed, with an explanatory reply and this source clarification retained. No manuscript PDF is copied into AIM.

## Lean distinction

The [upstream scope documentation](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/362.md) describes a formalization scope. The file it actually links, [ComparatorChallenges/VlasovMaxwell.lean](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/ComparatorChallenges/VlasovMaxwell.lean), is a comparator target: its final `global_classical_solution` theorem ends in `by sorry`. The checked raw-source SHA256 is `67941fd3f10cf129d42dc4ef6ea6b8585fb90ad942108d7d71827ce9960b9cf5`. Consequently that file does not establish public kernel verification. The maintained AIM page now states this explicitly. No local successful Linux replay, theorem proof or transitive permitted-axiom output is being asserted.

This absence concerns the proposed Lean-verification wording, not a demonstrated gap in the published manuscript. The PR supplies no independent proof package to classify as partial mathematical progress. AIM073 keeps its existing Solved status under the published-resolution criterion, with the previous statement-level review scope disclosed.
