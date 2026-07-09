## Code Review Summary

**Files Reviewed:** 1 plan (`plans/61-…meaning-tree.md`) against 3 code artifacts — `src/skills/note/SKILL.md`, `src/commands/command-handoff.md`, governing spec `specs/15-…meaning-tree.md`
**Risk Level:** 🟢 Low

Scope: plan review only. The plan targets two files (`note` engine + `command-handoff` caller), one contract, as spec 15 dictates. I resolved the reference tree: ROADMAP line 133 → spec 15 (working-tree-modified, read the diff) → the two code files. All line-number anchors the plan cites were checked against the actual files.

### Context Gates
- **Architecture** (`ARCHITECTURE.md` "Composition: mechanism vs policy") — **PASS.** `note` is the load-once engine; the plan broadens it *strictly additively* (Task 1) and keeps `command-handoff` (policy/caller) in control, delegating mechanism rather than inlining it. No engine content is copied into the caller. `loads:` edges unchanged.
- **Rules** (`.ai-factory/RULES.md`) — not present; gate skipped.
- **Roadmap** (`ROADMAP.md:133`) — **PASS.** The milestone line's `Spec:` tag resolves to spec 15; the plan's Context, task set, and verify checks mirror the spec's §2 collapse and §1 engine clause. Linkage is explicit.
- **Skill-context** (`.ai-factory/skill-context/aif-review/`) — absent; no project overrides to apply.
- **Engine-safety guard** — verified live: `grep -rn "^loads:.*\bnote\b" …` returns exactly `roadmap-engine` and `command-handoff`, matching the plan's Task 1 claim. `roadmap-engine` passes `note` only a destination (and template) hook, never a verbosity directive, so the Rule-2 broadening is inert for it — the plan's "existing callers byte-identical" guarantee holds.

### Verified accurate (spot-checks that could have sunk the plan)
- All cited line numbers are correct: note `:32`/`:33`/`:62`/`:105`; handoff `:5-7`/`:8`/`:13`/`:15-17`/`:19-23`/`:25`/`:51`/`:53`/`:55`/`:117`/`:119`/`:121`/`:123`/`:129`/`:131`/`:140-146`/`:148-164`/`:151-153`/`:155`.
- The plan folds in the spec's latest edits (working-tree diff): the reword-headings bullet (`:53`/`:117`/`:131`), the `:121` narrative direct-write clause as a *second* copy of the milestone-60 drift, and verify grep #8. Plan ↔ spec are in sync.
- The plan correctly **excludes** `:57` (the "read-first map scopes to the next step" paragraph) from the proportionality deletion. Spec's *problem statement* loosely lists `:57` as a proportionality site, but §36 (the change) lists only `:55`/`:119`/`:123` — and `:57` is genuinely not proportionality. The plan follows the correct set; the anti-collapse/per-subsystem intent survives in the self-check's clause (c). Good catch that the plan didn't over-delete.
- Task 3 correctly identifies and closes the **Step-1 double-mining gap** that deleting the `:25` dispatch opens — reframing Step 1 as `note`'s mining lens (skeleton placeholders / free-form directive) rather than an agent action. This is the subtle failure mode the milestone-55 refactor removed, and the plan pre-empts its recurrence.
- Rule 2's overridability is expressed the same way Rule 1's already is (hook `:33` + line `:62`), leaving Rule-text `:105` intact as the default — internally consistent, no hook-vs-text contradiction reintroduced.

### Critical Issues
None. No missing steps, no wrong path/API assumptions, no missing migration, no architectural violation. The decomposition into 4 dependency-ordered tasks within one plan preserves the spec's "one atomic contract" (engine + caller ship together).

### Minor Issue (non-blocking)
- **`command-handoff.md` (plan Tasks 2 & 3 verify blocks):** No task runs the spec's grep #8 verbatim. Spec verify #8 —
  `grep -niE "register|note mode|chat mode|destination axis|note destination|Write.*(direct|itself)"` —
  is the one the spec explicitly elevates as *"the completeness gate … what a single enumeration pass kept missing."* The plan splits it: Task 2's grep covers `register|note mode|chat mode|destination axis|note destination` but drops the `Write.*(direct|itself)` alternation, and Task 3's verify uses the `<NN>`/numbering grep plus prose ("no user-facing mode dispatch remains"). The *substance* is fully specified — Task 3 explicitly deletes both direct-write clauses (`:121` narrative + `:140-146`) and says "leave no clause asserting any shape `Write`s directly / bypasses `note`" — so the work will be done. What's missing is the plan carrying the spec's emphasized completeness grep as its final gate. Given this milestone's entire history is greps catching what enumeration missed, the fix is trivial: have Task 3's verify run spec grep #8 verbatim (expecting empty). Recommend adding it; not a blocker.

### Positive Notes
- Exhaustive-sites discipline applied consistently — the plan repeatedly names the grep as the completeness check rather than a reading pass, and enumerates every restatement of each drift (Rule-2 in three spots; the milestone-60 direct-write in *two* distinct spots `:121` and `:140-146`; proportionality across `:55`/`:119`/`:123`/`:155`).
- The invariant statement is placed at the Step-2 opener *before* the shape-specific headings, so it correctly governs both grid and prose shapes.
- "Do not encode a literal token target (the ~200k is metaphor)" is carried faithfully; boundary-neutral framing preserved with its `grep -ni "compact"` guard.
- Settings (no tests / minimal logging / no docs) are appropriate — these are agent-instruction markdown files with no runtime surface, and `note`'s description already lists "handoffs."

## Deferred observations
- Affects: spec 15 §36 (a future re-plan, not this milestone's file boundary) — The self-check gate is *replaced* wholesale by the abstract tree-completeness question, discarding the current gate's operational (a) execute-next-step / (b) avoid-every-logged-mistake / (c) per-subsystem-completeness scaffolding. The plan faithfully implements the governing spec's "replace the gate" instruction, so this is not a plan defect. Flagging only in case a later iteration wants the tree-completeness framing to *subsume and restate* those three concrete tests rather than drop them — a spec-level judgment outside this plan's control. [audit-dismissed]
