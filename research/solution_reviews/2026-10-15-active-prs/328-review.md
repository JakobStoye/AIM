# AIM 328: independent audit of PR #145

Date: 2026-10-15. Reviewer: independent OpenAI Codex AI context; no human or Lean verification is claimed.

Pinned submission: [54df545617bc9696104d2802bc3a91eb903445b2](https://github.com/MColbrook/AIM/pull/145), compared with the current problem page and its cited a153f469ee0ea64e876b2ad97c79d252c19a3e22 statement.

**Decision:** Solved. An exact positive-edge ultrametric three-leaf example for the symmetric twenty-state model violates the proposed Fitch accuracy inequality.

**Scope:** The entire submitted manuscript, package README, target comparison, disclosure and build instructions were read. This mathematical report is separate from the maintainer package checksum, rebuild and PDF-render records; it does not claim visual checks that have not been recorded.

The four specified positive lengths give equal root-to-leaf height because $`\log16+\log(5/4)=\log20`$. The exponential of the exact rate-one generator is $`\Pi+\lambda(I-\Pi)`$, so the edge signals are respectively 1/20, 1/16 and 4/5. Root conditioning is removed by label symmetry, preserving the uniform-root model.

The four mutually exclusive cherry events were recalculated. Their probabilities are 1437/20000, 11723/20000, 513/10000 and 2907/10000, which sum to one. Conditional branch independence makes the outgroup leaf independent of this entire set. Literal intersection/union recursion gives payoffs 439/800, 39/800, 153/400 and 13/400; the full child set is retained without prematurely breaking ties. Their weighted sum is 38829/400000, below every leaf's 39000/400000 by 171/400000. Thus no asymptotic sequence, topology inference, zero edge or non-clock assumption enters the counterexample.

The complete supplementary standard-library code was read and replayed with Python 3.12.14. Independent enumeration of all 160000 assignments returned exactly the same Fraction result, total probability one and positive deficit. This supplements the finite displayed proof.

The cited primary author versions of Fischer–Thatte and Herbst–Fischer were located and their scope distinguished from this twenty-state example; Li–Steel–Zhang's DOI and bibliographic identity match the cited conjecture. These are historical comparisons; the submitted calculation does not import a probabilistic theorem from them. The reference list is sufficient for the actual proof. The universal problem is disproved by r=20; no per-alphabet classification is claimed.

**PDF visual check:** Every submitted PDF page was subsequently inspected in the maintainer-rendered contact sheets. No clipped content, missing mathematics, unreadable glyph or broken cross-reference was found. The independent rebuild and checksum evidence is recorded separately.
