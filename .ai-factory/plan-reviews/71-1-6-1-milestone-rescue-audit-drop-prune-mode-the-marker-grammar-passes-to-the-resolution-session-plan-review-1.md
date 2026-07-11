## Plan Review Summary

**Files Reviewed:** plan (1 task-file, 2 tasks) against `milestone-rescue-audit/SKILL.md`, `orchestrator-artifacts/SKILL.md`, governing spec `specs/36-…`, roadmap line 1.6.1, ARCHITECTURE.md
**Risk Level:** 🟢 Low

### Context Gates
- **Architecture** (`.ai-factory/ARCHITECTURE.md`): PASS. The plan respects the engine/caller (mechanism vs policy) model — `orchestrator-artifacts` is a load-once engine, and Task 2 explicitly greps its three callers before touching § 6 and preserves the pinned/dedup contract they depend on. No boundary violation.
- **Rules** (`.ai-factory/RULES.md`): absent — gate skipped (no WARN; per-project rules live in consuming repos, not this meta-repo).
- **Roadmap** (`.ai-factory/ROADMAP.md`): PASS. Plan title matches the open `[ ]` line 1.6.1 verbatim and its `Spec:` tag resolves to `specs/36-audit-drops-prune-mode-grammar-resolution-session.md`. 1.6.1 is the live `[x]`/`[ ]` seam. Downstream ordering is coherent: 1.6.2 "runs strictly after 1.6.1" and 1.8.1 "Depends on 1.6.1", so the two stale pointers this task leaves are owned by a later, correctly-sequenced task.

### Critical Issues
None.

### Correctness check against the governing spec (36)
Verified clause-by-clause; the plan is a faithful, complete decomposition of the two-file scope:

- **Task 1 frontmatter** — `allowed-tools` drop of `Edit` → `Read Glob Grep Bash(git *)` is correct: the current line carries `Edit` (added by spec 04), so removing it makes the skill read-only exactly as the spec demands; `Bash(git *)`/`Glob`/`Grep` are retained for cold-run artifact discovery (note 40). `argument-hint` `"[task-slug]"` is properly quoted per the YAML-bracket rule. `loads: orchestrator-artifacts` kept. Description rewrite drops both prune trigger phrases and adds the invoke-on-smell trigger, wording consistent with spec 36 § Change bullet 1.
- **Task 1 body** — every current occurrence of the banned substrings (`prune`/`promote`/`marker`/`[audit-`) in the file maps to a plan instruction: Run-mode dispatch (33, 41–48), Inputs prune paragraph (63–65) + `$1`/`$2` complexity, Step 1 capture reword (89–97), Step 3 marking paragraph deletion (144–150) with the chat-only corroboration paragraph (135–142) correctly preserved, whole Prune-mode section (247–291), whole Write-contract section (294–309), and the What-NOT-to-do prune/marker/promote bullets + two rewords (313–338). The plan also catches that "roadmap-prune" itself contains the banned substring `prune` and instructs rewording the roadmap bullet to not name the skill. Coverage is exhaustive — nothing banned survives.
- **Task 2** — § 6 rewrite matches spec 36 exactly: active `[fixed]` / `[routed → <path>]` (path = an *open* task's spec) / `[dismissed]`, resolution-session as writer, and the four legacy tokens retired-but-pinned (lazy migration). Append-only, dedup, and "pinned = ≥1 marker" kept verbatim; the "only § 6 changes, everything else byte-identical" guard is stated. This preserves `roadmap-prune`'s gate computation (pinned still counts legacy markers).

The plan's own Verify lines mirror the spec's Verification section (whole-file zero-grep + § 6 content + gate correctness).

### Positive Notes
- The plan correctly identifies and *names* its two out-of-scope stale pointers up front (Context: `roadmap-prune:41-42` → owned by 1.8.1; `milestone-rescue`'s writer set → deferred), rather than silently leaving them or over-reaching past the spec's two-file boundary.
- Task 2's guard reproduces spec 36's engine-edit discipline (grep the three callers, byte-identical outside § 6) — the composition-model contract is honored.
- Relocating (not deleting) the "ensure `orchestrator-artifacts` is loaded once" instruction while stripping the "both modes rely on" phrasing keeps the load-once engine dependency intact after the mode collapse.

## Deferred observations
- Affects: `.ai-factory/ROADMAP.md` (no owning task) / `src/skills/milestone-rescue/SKILL.md` — this task retires `[promoted → <path>]` and `[audit-dismissed]` to legacy in § 6 and deletes `milestone-rescue-audit`'s prune mode, but `milestone-rescue/SKILL.md` still *actively writes* those two markers at in-session disposal (Step 5.6, lines 419–422, specs 09/13) and line 433 points entries it never evaluates to "`milestone-rescue-audit` prune mode" — a reference to the mode this task deletes. The plan is right to leave `milestone-rescue` untouched (spec 36 draws a hard two-file boundary and this fix requires editing a third file), so this is not a plan defect. Unlike the `roadmap-prune:41-42` pointer — explicitly owned by task 1.8.1 — no queued roadmap task currently owns reconciling `milestone-rescue`'s writer set / dangling prune-mode reference to the new resolution-session vocabulary. Whoever plans the next milestones should add that reconciliation task (paired with, or just after, 1.8.1) so `milestone-rescue` does not indefinitely instruct writing tokens the engine calls retired and pointing at a deleted mode.

PLAN_REVIEW_PASS
