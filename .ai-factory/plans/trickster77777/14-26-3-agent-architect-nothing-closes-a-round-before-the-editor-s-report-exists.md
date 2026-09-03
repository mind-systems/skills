# Plan: 26.3 — agent-architect: nothing closes a round before the editor's report exists

## Context
`src/skills/agent-architect/SKILL.md` describes reconciling against the editor's report and drafting the apply work-order out of what survives reconciliation, but never states what may not leave before a report exists — the ordering is inferable from exposition order alone. This task inserts one standalone `##` section that states the invariant, names all three closing artifacts, and gives its reason.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Insert the section

- [x] **Insert the new `##` section at the named boundary**
  Files: `src/skills/agent-architect/SKILL.md`
  Insert one new `##` section immediately after the end of `## Relay on the marker; author a prompt in exactly one case` and immediately before the `## Review in parallel, reconcile before the apply order` heading. Verified fresh in the file: the relay section opens at line 94 and its last paragraph ends `…and an unmarked answer is yours to hold, not to forward.`; `## Review in parallel, reconcile before the apply order` opens at line 176. Anchor the insertion on those two heading strings, not on line numbers.

  Use the section text pinned verbatim by the spec (`.ai-factory/specs/trickster77777/92-nothing-closes-a-round-before-the-report.md` § "The change") — heading `## Nothing closes a round before the editor's report exists` plus its three paragraphs. Do not paraphrase, re-order, or re-word it; copy it exactly as the spec's fenced block gives it. Separate it from its neighbours by a single blank line each side, matching the file's existing section spacing.

  Per the spec's guards: this is an additive insertion only. No existing sentence in any section is altered, amended, or absorbed — the `::` marker mechanics, the before-mark/after-mark split, the enrichment gating, the skill-expansion rule, and the two channel-message formats (`REPORT-ONLY` / `APPLY-EDIT`) stay byte-identical. Do not fold the rule into the reconcile paragraph or the work-order-authoring paragraph it constrains, and do not touch `src/agents/editor.md` or `src/skills/architect-editor-engine/`.

  Register note: the section states behavior and its reason in the present tense — it narrates no incident and no history, matching every other section in this file.

- [x] **Verify the insertion** (depends on Insert the new `##` section at the named boundary)
  Files: `src/skills/agent-architect/SKILL.md`
  Run `grep -n "^## " src/skills/agent-architect/SKILL.md` and confirm `## Nothing closes a round before the editor's report exists` appears between `## Relay on the marker; author a prompt in exactly one case` and `## Review in parallel, reconcile before the apply order`. Run `git diff --stat` — exactly one file changed — and `git diff` — insertions only, no line of any existing section removed or reworded.

  Read the inserted section back and confirm the four content checks the spec names: all three closing artifacts (summary, verdict, apply work-order) are named explicitly; the work-order is stated to close a round "as finally as a verdict" despite being "addressed to the editor rather than the user"; the guard that the architect's own parallel pass runs through the wait (what defers is the announcement, never the work) is present; and the rule's own reason — the editor's independence, agreement otherwise indistinguishable from an echo — is stated rather than implied.

## Notes for the implementer

- The contract line's citations `:76-79` and `:149-150` are stale: sibling tasks 26.4 (`27ab9cb`) and 26.1 (`451c6b3`) both edited this file before this task and shifted the line numbers. Both passages themselves are intact — resolve them by section plus opening words, never by number:
  - the reconcile sentence — "Once the editor's report returns, reconcile your independent read against it…" — in `## Relay on the marker; author a prompt in exactly one case`;
  - the work-order-authoring sentence — "Draft the apply work-order only for what survives reconciliation, and only after the user's explicit go." — in `## Review in parallel, reconcile before the apply order`.

  These two are the paragraphs the guard above protects: the rule is never folded into either of them. Note that `## Relay on the marker…` also contains a *different* apply-work-order sentence ("You author your own prompt in exactly one case: the **apply work-order**, once the user has confirmed the edits."); it is not the one the spec cites, and it is likewise left untouched. Resolve every position in this task by heading string or quoted text, never by line number.
- The spec pins the section text exactly. Nothing in this task requires authoring prose; the only judgment call is placement, and the spec fixes that too — before `## Review in parallel…`, so the rule reads as governing every `::` relay rather than as scoped to a review-shaped target.
