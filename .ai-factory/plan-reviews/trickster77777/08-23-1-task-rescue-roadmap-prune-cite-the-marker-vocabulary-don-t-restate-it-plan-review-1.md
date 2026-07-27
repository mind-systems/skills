# Plan Review: task-rescue & roadmap-prune — cite the marker vocabulary, don't restate it

**Plan:** `.ai-factory/plans/trickster77777/08-23-1-task-rescue-roadmap-prune-cite-the-marker-vocabulary-don-t-restate-it.md`
**Governing spec:** `.ai-factory/specs/trickster77777/86-marker-vocabulary-one-home.md` (roadmap task 23.1, `roadmaps/trickster77777.md:56`)
**Files Reviewed:** plan + 4 code files (`task-rescue`, `roadmap-prune`, `orchestrator-artifacts`, `task-rescue-audit`)
**Risk Level:** 🟢 Low

## Context Gates

- **Roadmap linkage** — PASS. Plan title matches roadmap task `23.1` under Phase 23; the plan's `Context` and `Guards` restate the contract line and its `Spec:` tag faithfully. Two-tier linkage (contract line ↔ spec 86) is intact.
- **Spec conformance** — PASS. The plan's four tasks map 1:1 onto the spec's change items: Tasks 1–3 = spec change item 1 (task-rescue Step 5.6 + "What NOT to do"); Task 4 = spec change item 2 (roadmap-prune `:65-66`). The user-ruled resolution ("option 2, no new capability for the audit skill") is carried verbatim into Task 2. All five spec guards are reproduced in the plan's Guards block.
- **Rules / Architecture** — PASS (WARN: no `.ai-factory/RULES.md` / `ARCHITECTURE.md` gate specific to this change). The change is a pure documentation/vocabulary-citation cleanup, directly serving the "one home per fact" discipline in the root CLAUDE.md and `reserved-words.md`. No module-boundary or dependency implications.

## Ground-truth verification

Every load-bearing claim in the plan was checked against the live files:

- **Line anchors are accurate.** `task-rescue/SKILL.md` `:429-432` = the two disposal branches; `:440-443` = the audit-attribution tail; `:475-479` = the "What NOT to do" bullet. `roadmap-prune/SKILL.md` `:65-66` = the resolution-session parenthetical `[fixed]` / `[routed → <path>]` / `[dismissed]`. All confirmed.
- **Retired-marker coverage is complete.** `grep -nE "\[audit-dismissed\]|\[promoted →|\[audit-corroborated\]|\[unrouted-reported\]"` over `task-rescue/SKILL.md` returns exactly five hits (`:430, :432, :441, :475, :477`) — every one falls inside a targeted range (Task 1 covers 430/432, Task 2 covers 441, Task 3 covers 475/477). The Verification "zero hits" gate is therefore reachable.
- **No stray restatements elsewhere.** A repo-wide grep for the retired forms finds them only in `orchestrator-artifacts` §6 (the home, guarded byte-identical) and in `task-rescue` (the target). No other skill/command/doc restates them — nothing is left inconsistent after the rewrite.
- **The false-attribution premise is real.** `task-rescue-audit/SKILL.md` is chat-only by explicit design (`:161` "Step 6 — Output (to chat only)"; `:204-205` "Write no file, ever"). It contains no marker vocabulary at all. So the current task-rescue text attributing `[audit-corroborated]`/`[unrouted-reported]` to it as a write responsibility is genuinely dead, and Tasks 2/3 correctly remove it.
- **The disposal-branch → §6 mapping is exact.** Rescue's "Routed" branch (new task+spec, or fold into a Step-5-repaired spec) maps cleanly to §6 `[routed → <path>]` ("routed into an open task's spec; `<path>` must resolve to an editable surface") — both the new-task spec and the rescued task's rolled-back spec are open/editable surfaces with a valid path. Rescue's "found moot / already handled" branch maps to §6 `[dismissed]` ("evaluated and found moot, stale, or already handled") near-verbatim. The vocabulary swap is semantics-preserving, as the spec requires.
- **The citation template exists.** `roadmap-prune/SKILL.md:53-55` ("do not redefine, cite the engine") is present and correct, so the "mirror this posture" instruction in Tasks 1 and 4 has a real, in-file model to copy.
- **Guards hold.** §6 (`orchestrator-artifacts`) deliberately keeps both the current and legacy marker lists (`:60-77`); the plan correctly leaves it untouched, and `task-rescue-audit` is correctly out of scope. The sidecar `step`-marker exclusion is well-founded — those live in §3 and `task-rescue`'s own closed-set table, a separate grammar.

## Critical Issues

None. The plan is accurate, completely covers the defect it targets, is faithfully scoped to its ratified spec, and its verification gates are all achievable.

## Positive Notes

- The plan pins exact line ranges *and* names the containing section for each edit, so line drift from applying Tasks 1–3 to the same file cannot misdirect the implementer.
- It correctly resists scope creep: §6 and `task-rescue-audit` are held byte-identical, and the "preserve disposal-branch semantics, change only marker naming" constraint keeps this a citation cleanup rather than a behavior change.
- Verification mirrors the spec's own verification block, including the `git diff` no-change assertion on the two guarded files.

## Deferred observations

- Affects: `orchestrator-artifacts` §6 (`src/skills/orchestrator-artifacts/SKILL.md:62-63`) — a future reconciliation, outside this task's guarded boundary. After this fix, `task-rescue` writes `[routed → <path>]` / `[dismissed]` at disposal time, but §6 characterizes those markers as "Written by the **resolution session** — the dedicated session the user opens from the parked prune's handoff." §6 is (correctly) held byte-identical by this task, so the one-home engine will describe the markers as the resolution session's while a second writer (rescue) also emits them. The current plan is right not to touch this — reconciling it means editing the guarded §6, a separate concern from vocabulary citation — but §6's writer attribution may eventually want to acknowledge rescue as a second, legitimate pin-writer.

- Affects: `task-rescue` Step 5.6 (`src/skills/task-rescue/SKILL.md:427-432`) — pre-existing two-branch structure, out of scope for a semantics-preserving citation task. §6 defines three current markers (`[fixed]`, `[routed → <path>]`, `[dismissed]`) but Step 5.6 offers only "routed" and "dismissed" branches, with no `[fixed]` path for the case where rescue's own spec+plan+code hand-fix directly closes a deferred observation's gap this session. The plan faithfully preserves the existing two-branch shape (as its spec mandates), so this is not a defect it should fix; noting it only so a later pass can decide whether Step 5.6 needs a `[fixed]` disposition.

PLAN_REVIEW_PASS
