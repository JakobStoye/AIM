# Independent AIM integration audit, 13 October 2026

Reviewer: separate Codex AI integration reviewer. Read-only repository audit; only this external report was written. This is an integration and theorem-scope check, not a fresh complete proof audit, execution reproduction, or Lean kernel replay.

AIM base: `c9929805cece044705abaaebe1cebddac1ba11a6`.
OpenAI source pin: `1581d4cbdd69a0faf34b2089614fe2a814316a6a`.

## Verdict

The integration passes the requested independent checks after the Sidorenko outcome correction described below. No remaining substantive integration defect was found. The coordinating agent owns final generated catalogue and full test-suite validation.

## Defect caught and corrected

AIM 585 initially had `Affirmative proof` in metadata and the complete-match table, plus a page sentence describing an affirmative resolution. Its own comparison correctly stated a finite simple unweighted graph counterexample and a complete negative resolution. The raw comparison omitted its outcome, allowing an affirmative default to invert the result.

This was reported immediately. The coordinating agent corrected metadata, page resolution, comparison outcome, and table. I independently rechecked those four surfaces: each now records a counterexample or a negative resolution. All 56 complete comparisons now have explicit outcomes: 49 affirmative proofs and seven counterexamples (011, 046, 206, 227, 321, 341, 585). Screening the remaining complete comparison prose found no further affirmative/counterexample inversion.

## Independent checks passed

- The 77 detailed comparisons consist of 56 complete matches, ten partial matches, and eleven excluded candidates. The 66 changed metadata IDs equal precisely the complete/partial comparison set.
- Every one of the 66 original Problem statement and Application sections matches the Git base after line-ending normalization. Every corresponding original-page SHA256 matches `page-preservation.json`. No problem file is removed.
- Page badges, metadata statuses, and review dates match: 56 Solved and ten Partially resolved, reviewed 2026-10-13. The ten partial pages (016, 028, 092, 098, 142, 337, 346, 487, 491, 590) all contain nonempty Known cases and Remaining target notes. No comparison asserts Lean verified, and every page explicitly limits this to AI statement-level review without a complete proof audit or fresh kernel replay.
- Numeric traps 261, 268, 213 and 325 retain both their original page text and original metadata. The distinct triangular Gaussian-energy and Mahler mappings are preserved.
- The 372 screened family IDs and constituent PDF lists match the upstream family export exactly. All 719 manuscript PDF paths are unique and exist in the untruncated pinned preprint tree. All comparison PDFs, companion PDFs and reader-facing external PDF links belong to that map. Every preservation-record PDF Git blob matches the pinned tree.
- All 115 inspected source files were independently checked against inspected SHA256, canonical SHA256 and Git blob hashes, using only the explicitly recorded CRLF normalization. Present upstream metadata files match their inventory SHA256 receipts.
- All 457 reader-facing pinned OpenAI URLs in updated pages and audit Markdown resolve in the combined preprint, scope-document, comparator and 39-module availability inventories. Local file links and explicit HTML anchors resolve. The new module receipt explicitly says upstream review status unchecked and kernel_replay_performed false. Module availability is not proof verification; the coordinating agent performed the immutable Git-blob API availability check.
- The cross-reference directory contains Markdown and JSON evidence only. No OpenAI PDF, TeX or Lean source was added there. Existing unrelated untracked local solution PDFs are outside this change.
- The README generator retains the new dated cross-reference and invitation to carefully checked human-authored explanations for AIM, explained. The generated README contains the invitation.

## High-risk scope spot checks

AIM 031's actual theorem is computer-assisted, conditioned on arithmetic/compiler assumptions and a complete execution. The page and report explicitly disclose that the referenced native archive is absent from the pinned public preprint directory and that no execution was reproduced; its Lean scope is only supporting partial work.

AIM 016's actual theorem supplies pure-point spectrum and a complete eigenbasis at every fixed positive disorder, while its introduction expressly disclaims exponential eigenfunction decay. The page remains Partial and identifies that exact remaining target.

AIM 098's actual theorem assumes strict binding, with an explicit caveat that adjacent-energy equality does not exclude a threshold eigenstate. The page remains Partial because the unchanged AIM definition includes threshold eigenvalues.

AIM 153 links both companion manuscripts. Their actual theorems cover 1 <= p <= 2 and 2 < p < infinity, respectively, with the same strong Sobolev approximation onto the fixed target. The two PDFs jointly cover the complete unchanged exponent range; neither boundary regularity nor equality is added to the target.

## Nonblocking presentation observation

Some imported statement-comparison prose uses plain ASCII notation rather than CONTRIBUTING's inline-math delimiters, for example AIM 153's `1<=p<=2` and `W1p`, and AIM 098's `-Delta/2` and `n<=Z+CM`. This is readable but would benefit from a typesetting pass. The original statement/application mathematical markup was preserved. No malformed new Markdown link or anchor was found.
