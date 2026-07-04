## Plan Review Summary

**Files Reviewed:** 1 plan (targets `src/skills/milestone-rescue-audit/SKILL.md`)
**Risk Level:** 🟡 Medium

### Context Gates
- **Architecture** (`.ai-factory/ARCHITECTURE.md`, "Composition: mechanism vs policy"): PASS. The plan adds a `loads: orchestrator-artifacts` edge — a philosophy skill (the audit) loading a mechanism engine — which is exactly the declared composition pattern. The engine already carries its reverse-graph marker (`orchestrator-artifacts/SKILL.md` §"load-once engine"), so the new caller edge is well-formed. No content is inlined from the engine; the plan repeatedly says "reference the engine, do not redefine," honoring the load-once contract.
- **Rules** (`.ai-factory/RULES.md`): WARN — file not present; gate skipped.
- **Roadmap** (`.ai-factory/ROADMAP.md`): PASS. Milestone under review is line 113, spec-tagged `.ai-factory/specs/04-audit-reads-deferred-observations.md`. The plan's `# Plan:` heading matches the contract line verbatim. Linkage intact.
- **Spec tree**: The governing engine spec (`05-orchestrator-artifacts-engine.md`, referenced as the dependency) has landed — `src/skills/orchestrator-artifacts/SKILL.md` exists and is symlinked into `active/skills/`. The dependency "engine task lands first" is satisfied. The marker grammar (§6), `## Deferred observations` format (§5), dedup rule, and pinned-definition the plan defers to all exist in the engine.

### Critical Issues
None — no security, migration, or runtime-crash defects.

### Issues

**1. (Medium) Cold-rescue loses its structured task identifier — `$1` is repurposed to the mode, but nothing replaces the dropped slug channel.**
Task 1 changes `argument-hint` from `"[milestone slug | leave empty if artifacts already in context]"` to `"[rescue|prune]"`, and Task 2 defines `$1 ∈ rescue|prune`. This mirrors spec Edit 1 faithfully. But the skill's own (unchanged) description advertises cold runs — *"or cold on any looped/outlier task"* — and the current Inputs block keeps *"If run cold, locate and read them before Step 1."* Previously the slug arrived as the argument; now the argument is the mode, so a cold `rescue` invocation (`/milestone-rescue-audit rescue`) has no structured way to name which task to audit. The plan rewrites Inputs (Task 2) but does not say how cold rescue identifies its target. This is within the milestone's file boundary (Task 1/Task 2 both touch the argument model), so it is a finding, not a deferred observation.
*Recommendation:* add one clause to Task 2's Inputs rewrite — e.g. an optional trailing slug (`$2`) for cold rescue, or an explicit statement that cold rescue identifies the target from the user's prose plus a Glob over `plan-reviews/`/`reviews/`. Either keeps `$1` as the mode (no spec contradiction) while restoring the cold-run affordance.

**2. (Low) Task 1's parenthetical shows a contradictory `allowed-tools` "result" that still contains `Write`.**
Task 1 reads: *"(result: `Read Write Edit Glob Grep Bash(git *)` — keep `Write` only if already present; current line is `Read Glob Grep Bash(git *)`, so make it `Read Edit Glob Grep Bash(git *)`). Do not add `Write`."* The first quoted "result" string includes `Write`; the final instruction correctly excludes it (current line has no `Write`, and spec Edit 4 grants only `Edit`). A careless implementer could copy the first string and add `Write`, violating the spec the plan itself cites. Tighten the parenthetical so the only literal target string is `Read Edit Glob Grep Bash(git *)`.

### Positive Notes
- **Faithful spec mapping.** Tasks 1–6 map cleanly onto spec Edits 1–4 plus the Constraints and What-NOT-to-do lists; nothing in the spec is dropped and nothing is invented beyond it.
- **Correct line/path references.** `milestone-rescue/SKILL.md:14` and `roadmap-prune/SKILL.md:11` both are the `loads: orchestrator-artifacts` line; the current `allowed-tools` line 13 is `Read Glob Grep Bash(git *)` as stated; the "see `milestone-rescue`" pointer to delete exists (line 31). All verified.
- **Sound Edit-not-Write reasoning.** The plan correctly justifies granting `Edit` rather than `Write`: promotion only ever appends into an *existing* file (prune promotes only when `Affects:` resolves to an existing path), and marker suffixes are append edits — both expressible via `Edit`. Consistent with spec Edit 4.
- **Prune-mode premise is grounded, not assumed.** `roadmap-prune` Step 0 (line 41) already names "run `milestone-rescue-audit` in prune mode" as the resolution when its read-and-refuse gate finds unpinned entries. This milestone closes a contract the sibling skill has already declared — the cross-file coupling is consistent on both sides.
- **Correct scan surface for prune mode.** Scanning `plan-reviews/` + `reviews/` (the two review genres that carry `## Deferred observations`, per engine §5) matches `roadmap-prune`'s gate surface, including the `ROADMAP_TESTS` parity note (prune gate line 53).
- **Single-file, sequential, one commit** with a compliant commit message (imperative, sentence case, no type prefix, no period).

## Deferred observations
- Affects: `.ai-factory/specs/04-audit-reads-deferred-observations.md` — Issue 1 above is inherited from spec Edit 1's decision to make `argument-hint` `"[rescue|prune]"`. If the planners decide cold-run task identification is genuinely out of scope for this skill (e.g. cold rescue is expected to always run warm-after-`milestone-rescue`), the cleaner fix is to prune the "or cold" affordance from the skill's description at the spec tier rather than patch it in the plan — that decision sits with whoever owns spec note 04, not this milestone's implementer.
