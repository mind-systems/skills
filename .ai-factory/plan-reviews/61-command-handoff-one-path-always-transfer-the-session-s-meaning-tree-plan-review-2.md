## Code Review Summary

**Files Reviewed:** 1 plan (`plans/61-…meaning-tree.md`) against 3 code artifacts — `src/skills/note/SKILL.md`, `src/commands/command-handoff.md`, governing spec `specs/15-…meaning-tree.md`
**Risk Level:** 🟡 Medium (one verify-sequencing defect; substance is sound)

Scope: plan review round 2. Resolved the reference tree: `ROADMAP.md:133` → spec 15 (working-tree file, read in full) → the two code files. Re-verified every line anchor the plan cites against the live files, and re-ran the spec's grep gates. Round-1's only open item (spec grep #8 not carried as a gate) *was* addressed — but placed in the wrong task, which produces the finding below.

### Context Gates
- **Architecture** (`ARCHITECTURE.md` — "Composition: mechanism vs policy") — **PASS.** `note` is the load-once engine; Task 1 broadens it strictly additively and `command-handoff` (caller/policy) delegates mechanism rather than inlining it. `loads:` edges unchanged.
- **Rules** (`.ai-factory/RULES.md`) — not present; gate skipped.
- **Roadmap** (`ROADMAP.md:133`) — **PASS.** Milestone line's `Spec:` tag resolves to spec 15; the plan's Context, task set, and verify checks mirror spec §1 (engine clause) and §2 (caller collapse). Linkage explicit.
- **Skill-context** (`.ai-factory/skill-context/aif-review/`) — absent; no project overrides.
- **Engine-safety guard** — verified live: `grep -rn "^loads:.*\bnote\b" …` returns exactly `roadmap-engine` and `command-handoff`. `roadmap-engine` passes `note` no verbosity directive, so the Rule-2 broadening is inert for it — "existing callers byte-identical" holds.

### Verified accurate
- Line anchors all correct against live files: note `:32`/`:33`/`:62`/`:105`; handoff `:5-7`/`:8`/`:13`/`:15-17`/`:19-23`/`:25`/`:51`/`:53`/`:55`/`:117`/`:119`/`:121`/`:123`/`:129`/`:131`/`:140-146`/`:148-164`/`:151-153`/`:155`.
- Task 1's three-site Rule-2 fix (`:33`, `:62` clause A, `:62` clause B) plus the template-hook free-form reword matches spec §1 exactly; Rule-text `:105` left intact as the default, so no hook-vs-text contradiction is reintroduced.
- Task 3 pre-empts the **Step-1 double-mining gap** that deleting `:25` opens — reframing Step 1 as `note`'s mining lens (blank placeholders / free-form directive) rather than an agent action. Correct handling of the milestone-55 failure mode.
- Task 2/3 boundary on `:121` is clean and explicitly non-overlapping (Task 2 leaves it to Task 3; Task 3 collapses it in full, including the narrative direct-write clause as the *second* copy of the milestone-60 drift alongside `:140-146`).
- The plan correctly excludes `:57` (read-first-map paragraph) from the proportionality deletion — that paragraph is not proportionality, matching spec §36's actual site list (`:55`/`:119`/`:123`).

### Critical Issues

**1. Spec grep #8 is placed as Task 3's final gate, but two of its match sites are owned by Task 4 — the gate cannot return empty at Task 3's completion.**
Task 3's verify (plan `:47`) says: *"run the spec's completeness gate (spec verify #8) verbatim as this task's final check — `grep -niE "register|note mode|chat mode|destination axis|note destination|Write.*(direct|itself)"` … returns nothing."*
But that pattern currently matches, among others:
- `:119` — "The proportionality principle applies to both regist**ers**…" (matches `register`), which the plan deletes in **Task 4** (`:51`, "proportionality prose at `:119`").
- `:123` — "In **chat mode** this gate applies… In **note mode** this gate applies…" (matches `chat mode`/`note mode`), whose mode-dispatch tail the plan deletes in **Task 4** (`:51`).

Task 3 touches neither `:119` nor `:123` — Task 4 does, and Task 4 runs *after* Task 3. So an implementing agent that runs Task 3's gate literally will see it fail (matches on `:119` and `:123`), then either (a) pull Task 4's `:119`/`:123` deletions forward into Task 3 — stepping on Task 4's declared scope and muddying the dependency ordering — or (b) treat Task 3 as incomplete and thrash. Given this milestone's entire history is grep-gates catching what enumeration misses (the plan says so at `:47`), a completeness gate that is *guaranteed to false-fail at its assigned task* is a real defect, not cosmetic.

Fix (within the plan's own file boundary): move the verbatim spec grep #8 to **Task 4's** verify as the whole-change final gate (Task 4 is the last task and is the one that clears the last `register`/`chat mode`/`note mode` matches). Task 3 can keep its `<NN>`/numbering grep and a *scoped* check of its own sites, but the "returns nothing" whole-file gate belongs after Task 4. Alternatively, have Task 4 re-run grep #8 as its final check — but then Task 3's "returns nothing" claim must be softened to "returns only the Task-4-owned `:119`/`:123` lines," or it is simply false as written.

### Positive Notes
- Exhaustive-sites discipline is applied consistently and the plan names the grep (not a reading pass) as the completeness check at each drift — Rule-2 in three spots, the milestone-60 direct-write in two (`:121` + `:140-146`), proportionality across `:55`/`:119`/`:123`/`:155`.
- The fixed-invariant statement is correctly placed at the Step-2 opener, before the shape-specific headings, so it governs both grid and prose shapes.
- "No literal token target (the ~200k is metaphor)" and spec 14's boundary-neutral framing (with its `grep -ni "compact"` guard) are carried faithfully.
- Settings (no tests / minimal logging / no docs) are appropriate for agent-instruction markdown with no runtime surface.

## Deferred observations
- Affects: spec 15 §36 (a future re-plan, outside this milestone's file boundary) — The self-check gate is *replaced* wholesale by the abstract tree-completeness question, discarding the current gate's operational (a) execute-next-step / (b) avoid-every-logged-mistake / (c) per-subsystem-completeness scaffolding. The plan faithfully implements the governing spec's "replace the gate" instruction, so this is not a plan defect; flagging only in case a later iteration wants tree-completeness to *subsume and restate* those three concrete tests rather than drop them — a spec-level judgment the plan cannot make. [audit-dismissed]
