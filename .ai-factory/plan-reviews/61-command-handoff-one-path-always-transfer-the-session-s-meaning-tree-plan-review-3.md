## Code Review Summary

**Files Reviewed:** 1 plan (`plans/61-…meaning-tree.md`) against 3 code artifacts — `src/skills/note/SKILL.md`, `src/commands/command-handoff.md`, governing spec `specs/15-…meaning-tree.md`
**Risk Level:** 🟢 Low

Scope: plan review round 3. Resolved the reference tree: `ROADMAP.md:133` → spec 15 (working-tree-modified, read in full) → the two code files. Re-verified every line anchor the plan cites against the live files, re-ran the spec's grep gates against both targets, and confirmed the round-2 blocking defect is closed.

### Context Gates
- **Architecture** (`ARCHITECTURE.md` — "Composition: mechanism vs policy") — **PASS.** `note` is the load-once engine; Task 1 broadens it strictly additively (a new caller-directive override, no behavior removed), and `command-handoff` (caller/policy) delegates mechanism to `note` rather than inlining it — the direct-`Write`/hand-numbering drift is *removed*, not reproduced. `loads:` edges unchanged.
- **Rules** (`.ai-factory/RULES.md`) — not present; gate skipped.
- **Roadmap** (`ROADMAP.md:133`) — **PASS.** Milestone line's `Spec:` tag resolves to spec 15; the plan's Context, four-task set, and verify checks mirror spec §1 (engine clause) and §2 (caller collapse), incl. the spec's grep #8 completeness gate and the boundary-neutral guard. Linkage explicit.
- **Skill-context** (`.ai-factory/skill-context/aif-review/SKILL.md`) — absent; no project overrides.
- **Engine-safety guard** — verified live: `grep -rn "^loads:.*\bnote\b" …` returns exactly `roadmap-engine` and `command-handoff`. `roadmap-engine` passes `note` **no** verbosity directive (`grep -ni "verbosity\|concis\|findings-focus" src/skills/roadmap-engine/SKILL.md` → empty), so the Rule-2 broadening is inert for it — the plan's "existing callers byte-identical" guarantee holds.

### Round-2 defect — CLOSED
Round 2's one blocking finding was that spec grep #8 was set as **Task 3's** final gate while two of its match sites (`:119` `register`, `:123` `chat mode`/`note mode`) are owned by **Task 4**, so the gate was guaranteed to false-fail at Task 3. This plan fixes it exactly as recommended:
- Task 3 verify (`:47`) now explicitly **defers** the whole-file grep #8 to Task 4, keeping only its `<NN>`/numbering grep plus a *scoped* check of its own sites, and states the reason (`register`/`chat mode`/`note mode` still legitimately match at `:119`/`:123` until Task 4).
- Task 4 verify (`:52`) runs spec grep #8 **verbatim** as the "whole-change final gate," expecting empty after the last task clears `:119`/`:123`.
The dependency ordering and site ownership are now consistent with the gate's timing.

### Verified accurate (spot-checks that could have sunk the plan)
- **All line anchors correct** against the live files: note `:32`/`:33`/`:62`/`:105`; handoff `:5-7`/`:8`/`:13`/`:15-17`/`:19-23`/`:25`/`:51`/`:53`/`:55`/`:117`/`:119`/`:121`/`:123`/`:129`/`:131`/`:140-146`/`:148-164`/`:151-153`/`:155`.
- **Grep #8 sites are exhaustively partitioned** across the four tasks with clean, non-overlapping ownership — I enumerated every live match and mapped it: `:15-17`+`:19-23`+`:25`+`:129` (Task 2 delete), `:53`/`:117`/`:131` headings (Task 2 reword), `:51`/`:151-153` (Task 2/3 reword), `:121` (Task 3 collapse), `:140-146` (Task 3 delete), `:119`/`:123` (Task 4). No site is orphaned; none is double-owned. Task 2 explicitly hands `:121` to Task 3 rather than partially deleting it.
- **All `proportional` sites are covered**: `:55`/`:119`/`:123`/`:155` by Task 4, and `:135` (the "Verbosity directive = the proportionality policy" hook line) is naturally replaced by Task 3's new verbosity/fidelity directive when it rewrites the delegation hooks — with Task 4's `grep -ni "proportional" → nothing` as the safety net.
- **Note Rule-2 three-site fix** (`:33`, `:62` clause A, `:62` clause B) matches spec §1 exactly; Rule-text `:105` is left intact as the default, so no hook-vs-text contradiction is reintroduced. The verify correctly expects the grep to still *match* (`:33` keeps "other Important Rules — file paths, English") but with no clause naming findings-focus as always-on — an inspection check, not an empty-return check, consistent with spec verify #5.
- **Step-1 double-mining gap** that deleting `:25` opens is pre-empted by Task 3 (`:38`) — Step 1 is reframed as `note`'s mining lens (blank placeholders for grid / free-form body directive for prose), not an agent action. This is the milestone-55 failure mode; the plan closes it before it can recur.
- **`:57`** (the read-first-map paragraph) is correctly **excluded** from the proportionality deletion — it is not proportionality prose, matching spec §36's actual site list (`:55`/`:119`/`:123`).
- **Boundary-neutral framing** preserved with its `grep -ni "compact"` guard (Task 3, `:46`); no literal token target introduced (the "~200k" metaphor is carried as prose, not a number).

### Critical Issues
None. No missing steps, no wrong path/API assumption, no missing migration, no architectural violation. The four dependency-ordered tasks (Task 1 engine → Task 2 frontmatter/axes → Task 3 composition → Task 4 gate) preserve the spec's "one atomic contract" — the engine clause and caller rewrite ship together. `allowed-tools` intentionally unchanged (unused, not newly granted) per spec §44.

### Positive Notes
- The grep-as-completeness-gate discipline is applied consistently and the round-2 sequencing fix is precise — the plan now names *which* task owns *which* residual match and why, rather than asserting a single blanket gate.
- The fixed-invariant statement is placed at the Step-2 opener, before the shape-specific headings, so it governs both grid and prose shapes.
- Task boundaries on the shared `:121`/`:131`/`:140-146` region are explicitly declared non-overlapping, avoiding the double-ownership thrash that looped milestone 60.
- Settings (no tests / minimal logging / no docs) are appropriate for agent-instruction markdown with no runtime surface; `note`'s description already lists "handoffs."

## Deferred observations
- Affects: spec 15 §36 (a future re-plan, outside this milestone's file boundary) — The self-check gate is *replaced* wholesale by the abstract tree-completeness question, discarding the current gate's operational (a) execute-next-step / (b) avoid-every-logged-mistake / (c) per-subsystem-completeness scaffolding. The plan faithfully implements the governing spec's "replace the gate" instruction, so this is not a plan defect; flagging only in case a later iteration wants tree-completeness to *subsume and restate* those three concrete tests rather than drop them — a spec-level judgment the plan cannot make.

PLAN_REVIEW_PASS
