# Plan Review — 34.1 `roadmap-engine` states what a task spec holds (round 2)

## Code Review Summary

**Files Reviewed:** plan (1) + target (1): `src/skills/roadmap-engine/SKILL.md`; plus the task spec `109-…`, the `### Phase 34` header prose and its direction preamble, the engine's nine callers (`grep -l "roadmap-engine" src/skills/*/SKILL.md src/commands/*.md`), `src/skills/roadmap-decompose/SKILL.md`, `src/skills/note/SKILL.md`, `docs/reference-by-name.md`, `orchestrator-artifacts`, the sibling `orchestrator` repo's planner prompts, and plan-review round 1
**Risk Level:** 🟢 Low — two pinned prose edits in one file, every positional and textual claim re-verified against the bytes; round 1's single critical issue is closed.

### Context Gates

- **Architecture** — PASS. `.ai-factory/ARCHITECTURE.md` § "Composition: mechanism vs policy" is undisturbed: no skill added or re-tiered, no `loads:` edge touched, the engine gains no decision of its own. Stating what a task spec holds is artifact *format* — the same tier as the already-present "Rules for writing a contract line" block — not the decomposition policy the engine explicitly hands back to its caller. Body cap intact: 317 lines today, 322 after.
- **Rules** — WARN (non-blocking). `.ai-factory/RULES.md` does not exist in this repo; nothing to check against. The governing conventions live in `CLAUDE.md`, `.ai-factory/ARCHITECTURE.md`, `docs/reserved-words.md`, `docs/using-the-language.md` and `docs/reference-by-name.md` — all checked below.
- **Roadmap** — PASS. `.ai-factory/roadmaps/trickster77777.md:184` is the first `- [ ]` line in the file — the seam — and it is 34.1, the task this plan targets; the plan's `# Plan:` heading matches the contract line's title verbatim. The `Spec:` tag resolves to `.ai-factory/specs/trickster77777/109-roadmap-engine-states-what-a-task-spec-holds.md`, which exists and was read in full. Phase 34 names no `Governing spec:` line, so the reference chain runs contract line → task spec → `src/skills/roadmap-engine/SKILL.md`, plus `docs/reference-by-name.md` for the bold lead-in.
- **Vocabulary** — PASS. Nothing edited is a protocol token: the `Spec:` tag, the roadmap-format block and the char-budget command stay byte-identical. `task spec`, `contract line` and `two-tier` are used at their registry meanings. `blast-radius` as the bullet's third member is pinned by the task spec itself and matches the word `command-pin-gaps` already uses for the concept, so it replaces a synonym rather than adding one.

### Round-1 finding: closed

Round 1's one critical issue was that the plan inferred "nothing else has to move" from a *string*-level sweep while a direct caller restates the dropped enumeration in prose. The revised plan states exactly what was verified and no more — "Verified at plan time, string-level only: the literal enumeration … occurs exactly once in the repository outside `.ai-factory/`" — then names `src/skills/roadmap-decompose/SKILL.md` § "(d) Extra update action" as a known, deliberately out-of-scope restatement, and closes with the explicit consequence: "the family is **not** reconciled when this task lands: the engine will say three parts while that caller still asks for guards and how to verify." A matching guard ("Do not repair `roadmap-decompose`") pins the non-action. That is the correct disposition — the boundary argument is real (this task's contract line names only `roadmap-engine`; 34.2 is `command-pin-gaps`, 34.3 the paired-loop trio, 34.4 the registry — none owns `roadmap-decompose`) — and the downstream reviewer now inherits an accurate picture instead of a false all-clear. Carried forward below as a deferred observation.

### Verified against ground truth

Every positional and textual claim re-checked against the file, not against the plan's or the spec's description of it:

- The **Why two tiers:** paragraph is exactly `:42–44`; `:44` is byte-exact `is guidance, not a hard clamp.`; `:45` is blank; `:46` opens `**Never write a full spec inline in the roadmap**`. Insertion point and the blank-line-on-each-side instruction are correct, and `:43`'s forward reference "The char budget below" still resolves past the insert to `:107`.
- `:105` is byte-exact `- Full current-state / target / guards / verify detail lives in the task spec, not the contract line`. The rewrite changes only the enumeration's third and fourth members and preserves the trailing clause.
- The string sweep reproduces: `grep -rn "current-state / target" --include="*.md" .` outside `.ai-factory/` returns exactly one hit, `src/skills/roadmap-engine/SKILL.md:105`.
- The named prose restatement is where the plan says it is: `src/skills/roadmap-decompose/SKILL.md:88–89`, "(what exists today, the exact change, files/types/methods to touch, guards, how to verify)".
- The pinned paragraph measures 83 / 85 / 81 / 56 code points — the ≤90 wrap instruction is satisfied exactly as pinned, so no neighbouring text needs re-wrapping. One nuance in the plan's supporting aside, not in its instruction: the section is hard-wrapped and its ceiling is 90 (`:43`), which is what the instruction rests on and is exact; the stated 59-column floor is loose — `:31` (`lowercase-hyphenated). A`) runs 24 columns mid-paragraph. The pinned text is the authority for its own line breaks, so nothing follows from this for the edit.
- Emphasis across a soft line break (`*what must` / `be true after*`) is valid CommonMark inside one paragraph — the italics render as intended after the hard wrap.
- The bold lead-in is justified rather than decorative: `docs/reference-by-name.md:13,15` names "a bold lead-in" as a unit of naming and cites `command-pin-gaps`'s bold-lead classes as the working example — which is exactly what 34.2 must address by name.
- Spec fidelity: the plan renders the spec's three bullets as one prose paragraph, arguing from the contract line and the spec both saying "one paragraph". The pinned wording tracks the contract line clause for clause; the bullet's replacement text is byte-identical to the spec's.
- Cross-repo: nothing is owed. The `orchestrator` repo reaches the task spec only through the `Spec:` tag (`orchestrator/orchestrator/prompts/planner.md:22`, `test-planner.md:19`) and prescribes none of its content.
- Delivery: `active/skills/roadmap-engine → ../../src/skills/roadmap-engine` is a live symlink and there is no `upstream/ai-factory/roadmap-engine`, so the edit goes live and a re-sync cannot clobber it. The working tree holds only this task's own untracked artifacts, so the `git diff HEAD --stat` post-condition is a clean signal.

### Critical Issues

None.

### Positive Notes

- Pinning the paragraph's full text, its line breaks and its insertion point leaves nothing for the implementer to re-derive on a change whose entire deliverable is four lines of prose.
- The plan keeps `:43`'s "holds the full implementation detail" and says why ("the new paragraph says what that detail is, it does not replace the sentence") — the one sentence a mechanical implementer would have rewritten, pinned shut.
- Naming what must *not* move — the third contract-line bullet, with the reasoning that a word leaving one enumeration is not a sweep of the word from the file — forecloses the over-deletion a `grep guards` would produce.
- Round 2's rewrite is a model of scoping a known defect out honestly: it distinguishes the string claim from the concept claim, names the surviving contradiction and its file, and states the unreconciled end state as the deliberate outcome rather than leaving it implicit.
- The guard "the engine is its one home" paired with the named 34.2 / 34.4 siblings holds one-home-per-fact across a phase where three tasks circle the same fact.

## Deferred observations

- Affects: Phase 34 / `.ai-factory/specs/trickster77777/109-roadmap-engine-states-what-a-task-spec-holds.md` — `src/skills/roadmap-decompose/SKILL.md:88–89` needs the reconciliation the engine's `:105` bullet gets here: its hook (d) parenthetical describes a full spec as "(what exists today, the exact change, files/types/methods to touch, guards, how to verify)", which after 34.1 contradicts the engine it defers to, in the one mode dedicated to writing a task spec. The plan is right that the file is outside this task's boundary and that no task in Phase 34 owns it — it wants a fifth task in the phase or a follow-up. Two upstream surfaces carry the same over-broad claim and would be repaired with it: the phase preamble at `.ai-factory/roadmaps/trickster77777.md:182` ("no skill prescribing a task spec's sections") and the spec's own Blast radius section ("no skill or command restates it"). The exposure while it stands is an agent in "Decompose existing" mode reading both surfaces and writing the verification bullets the phase exists to stop.
- Affects: Phase 34 / `src/skills/roadmap-engine/SKILL.md` — after this lands the section says a task spec holds three parts and nothing else two paragraphs after saying it "follows `note`'s format", whose template hook stays unset and therefore still defaults to the standalone-note skeleton (Key Findings / Details / Open Questions) that the task spec's own Current state names as part of the problem. `note`'s folder-style layer covers the gap in practice — the recent siblings in `.ai-factory/specs/trickster77777/` already carry Current state / The change / Blast radius — and the contract line forecloses the template route by name, which is why this is correctly not a finding here. Raised because the residual tension is what a later reader trips on: the shape is now stated in one place while the section skeleton is still inherited from another.

PLAN_REVIEW_PASS
