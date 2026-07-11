# roadmap-prune: pyramid pass — instructions-only enforced to the letter

## Current state

`src/skills/roadmap-prune/SKILL.md` (330 lines) already carries an "instructions only, no rationale prose" mandate from its own respec, but the body has since accreted procedure narration and protocol restatement around its real contracts: the pre-prune snapshot, the `Spec:`-tag capture-before-delete rule (no tag → skip, never synthesize), the four-artifact-dir sweep (`plans/`, `plan-reviews/`, `reviews/`, `patches/` — plain `rm`, no `git rm`), the ARCHITECTURE.md `## Features` anchor append, the emptied-phase/-direction header sweep (never renumber), the deferred-observations gate, and the exact commit policy (`Roadmap prune`, one commit, only on request).

## Change

One pyramid pass — compression to the mandate the skill already declares:

- **Verbatim-protected:** every contract listed above — the capture rule (as scoped by 1.8.2: pruned lines only), the sweep set, the anchor format, the never-renumber rule, the gate (with 1.8.1's refusal message), the commit policy line.
- **Closure rule — protection is by criterion, not enumeration:** *any* sentence stating a contract (capture, sweep, anchor, gate, commit, classification decision, edge path such as the first-ever-prune skip / section-create) is protected verbatim whether or not an inventory names it. Itemized lists in this spec or the plan are illustrative, never exhaustive; a contract-bearing sentence discovered mid-rewrite joins the protected set on the spot — it is not a plan defect and does not require re-planning.
- **Runs strictly after 1.8.1 and 1.8.2** — this pass compresses the file they leave behind and must not reintroduce the removed keep-recent rule or the audit hint.
- **Cut:** narration, rationale prose, restated `orchestrator-artifacts` protocol (link, never restate), any step an executor performs unprompted.
- Two-reader register.

## Guards

- **Behavior-identical** — same files deleted, same anchors written, same gate refusals, same commit; protected contracts byte-identical.
- Frontmatter and `loads:` unchanged.
- Live baseline before the next phase task: dry-run the capture+sweep plan (list, don't delete) on this repo's own completed tasks pre/post rewrite and compare the file sets.

## Verification

- `diff`: contracts byte-identical; removed hunks are narration only.
- Dry-run baseline: identical delete-list and anchor rows pre/post.
