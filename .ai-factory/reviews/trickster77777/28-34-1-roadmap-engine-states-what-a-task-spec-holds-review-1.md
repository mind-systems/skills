# Review — 34.1 `roadmap-engine` states what a task spec holds

## Code Review Summary

**Files Reviewed:** the whole diff — `src/skills/roadmap-engine/SKILL.md` (read in full, 322 lines, not just the two hunks); plus the plan, plan-reviews 1–2, the task spec `109-…`, the contract line and its `### Phase 34` header and direction preamble, the engine's nine callers (`grep -l "roadmap-engine" src/skills/*/SKILL.md src/commands/*.md`), `src/skills/note/SKILL.md`, `src/skills/roadmap-decompose/SKILL.md`, `docs/` in full for two-tier/task-spec prescriptions, `active/skills/roadmap-engine`, `upstream/ai-factory/`, and the sibling `orchestrator` repo.
**Risk Level:** 🟢 Low — two prose edits in one skill file, both byte-identical to what the plan pinned; nothing executable, no protocol token, no `loads:` edge, no caller contract broken that was not already known and scoped out.

### What landed

`git diff HEAD` shows exactly two hunks in one file, and `git status` lists no other source change (the remaining entries are this task's own plan, sidecar and plan-review artifacts):

1. `:46–49` — a new paragraph inserted after the **Why two tiers:** paragraph, blank line on each side:
   `**What a task spec holds:** three parts and nothing else — *what is true now*, read from the code with exact values, so the implementer does not re-derive it; *what must be true after*, in the code's own terms: which file, which text, which value; and *what breaks on contact*, enumerated rather than hedged.`
2. `:110` — the contract-line bullet now reads `- Full current-state / target / blast-radius detail lives in the task spec, not the contract line`.

### Verified against ground truth

Every check below was run against the file's bytes, not against the plan's or the spec's description of them:

- **Text fidelity.** The landed paragraph is character-for-character the plan's pinned text, including its four line breaks and its italics. The landed bullet is character-for-character the replacement text pinned in both the plan and the task spec's "The change".
- **Contract-line fidelity.** The paragraph tracks the contract line clause for clause: "what is true now, read from code with exact values" → "what must be true after, in the code's own terms" → "what breaks on contact, enumerated rather than hedged". It names three parts and adds nothing — no template, no section skeleton, no procedure.
- **Placement.** The **Why two tiers:** paragraph remains `:42–44` ending `is guidance, not a hard clamp.`; `:45` blank; the new paragraph `:46–49`; `:50` blank; `:51` opens `**Never write a full spec inline in the roadmap**`. Placement matches the spec's "placed after the **Why two tiers:** paragraph" exactly.
- **No collateral rewrite.** `:43`'s "the task spec holds the full implementation detail" survives verbatim — the sentence a mechanical implementer would have replaced. Its forward reference "The char budget below" still resolves past the insert to the budget bullet, now `:107`. The path/numbering/`Spec:`-tag paragraph and the `note`-format paragraph keep their text and their line breaks; no neighbouring line was re-wrapped.
- **Wrap.** The four new lines measure 83 / 85 / 81 / 56 Unicode code points (counted with the engine's own pinned command), inside the section's 90-column ceiling at `:43`. No trailing whitespace anywhere in the file.
- **Over-deletion foreclosed.** The guard-conditions bullet survives intact at `:106` (`- Name guard conditions ("do not touch X", "skip Y") only for real pitfalls…`), as do the other five bullets and the roadmap-format block's `key files/types/guards involved` template at `:98`. The word `guards` left one enumeration; it was not swept from the file.
- **No protocol token moved.** The `Spec:` tag literal, the roadmap file format block, the numbering rules and the **Counting characters** command are byte-identical to `HEAD`.
- **Body cap.** 317 → 322 lines, well inside the 500-line cap in CLAUDE.md § "Key constraints".
- **Markdown.** The emphasis spans that cross a soft line break (`*what must` / `be true after*`) are inside one paragraph and render as intended — valid CommonMark, not a broken span.
- **Guards honoured.** `src/skills/note/SKILL.md` is untouched and its template hook stays unset (no skill gained a template); nothing under `.ai-factory/specs/` was rewritten; `src/commands/command-pin-gaps.md` (34.2) and `docs/reserved-words.md` (34.4) are untouched, so the siblings are not anticipated; the new fact is stated in `roadmap-engine` and nowhere else — one home, intact.
- **Delivery.** `active/skills/roadmap-engine → ../../src/skills/roadmap-engine` resolves and the new paragraph reads live through it. There is no `upstream/ai-factory/roadmap-engine` (the only roadmap-ish upstream skill is the unrelated `aif-roadmap`), so `scripts/sync-upstream.sh` cannot clobber the edit.
- **Callers and cross-repo.** Swept the eight other callers and all of `docs/` for a second prescription of a task spec's contents: the only one is `src/skills/roadmap-decompose/SKILL.md:88–89`, the known out-of-scope restatement carried below. No `docs/` file prescribes a spec's parts. Neither the literal enumeration nor a prose equivalent appears anywhere in the sibling `orchestrator` repo — its planner prompts reach the task spec only through the `Spec:` tag — so no lockstep change is owed.

### Critical Issues

None.

### Positive Notes

- The one contradiction this landing knowingly leaves standing was declared *before* it landed — the plan states the string-vs-concept distinction, names the surviving file, and calls the end state unreconciled. Reviewing against that costs nothing to verify and leaves no false all-clear.
- The paragraph says only what a task spec holds. It does not smuggle in a section skeleton, a heading set, or a verification step — which is what the phase exists to stop, and the most available way this edit could have overshot.
- The bullet rewrite is minimal in exactly the right way: two members of an enumeration change, the trailing clause and the six sibling bullets do not, and the word `guards` keeps its unrelated home two bullets up.

## Deferred observations

- Affects: Phase 34 / `.ai-factory/specs/trickster77777/109-roadmap-engine-states-what-a-task-spec-holds.md` — `src/skills/roadmap-decompose/SKILL.md:88–89` now contradicts the engine it defers to: its hook (d) "Decompose existing" describes a full spec as "(what exists today, the exact change, files/types/methods to touch, guards, how to verify)" — four parts, including both members this task dropped — in the one mode dedicated to writing a task spec. The file is outside this task's contract-line boundary and no task in Phase 34 owns it; it wants a fifth task in the phase or a follow-up. Two upstream surfaces carry the same over-broad claim and would be repaired with it: the phase preamble at `.ai-factory/roadmaps/trickster77777.md:182` ("no skill prescribing a task spec's sections") and the spec's own Blast radius ("no skill or command restates it"). Exposure while it stands: an agent in that mode reads both surfaces and writes the verification bullets the phase exists to stop. (Carried forward from plan-review rounds 1 and 2, now verified against the landed file.)
- Affects: Phase 34 / `src/skills/roadmap-engine/SKILL.md` — § "The two-tier artifact" now says a task spec holds three parts and nothing else (`:46`) two paragraphs after saying it "follows `note`'s format" (`:36`), whose template hook stays unset and therefore still defaults to the standalone-note skeleton (Key Findings / Details / Open Questions) that the task spec's own Current state names as part of the problem. Nothing breaks in practice — `note`'s folder-style layer reads the recent siblings in `.ai-factory/specs/trickster77777/`, which already carry Current state / The change / Blast radius — and the contract line forecloses the template route by name, which is why this is not a finding. Raised because the residual tension is what a later reader trips on: the shape is stated in one place while the section skeleton is still inherited from another.

REVIEW_PASS
