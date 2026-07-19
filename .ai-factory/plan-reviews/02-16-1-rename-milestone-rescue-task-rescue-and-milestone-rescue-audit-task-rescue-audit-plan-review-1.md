# Plan review 1 — 16.1 Rename milestone-rescue → task-rescue, milestone-rescue-audit → task-rescue-audit

## Code Review Summary

**Files Reviewed:** plan (9 tasks) + 7 target files + spec 71 + ROADMAP + cross-repo orchestrator artifacts
**Risk Level:** 🟡 Medium (one provenance defect; the mechanical content is sound)

### Context Gates

- **ARCHITECTURE** (`.ai-factory/ARCHITECTURE.md`, present) — **OK.** The rename touches no `loads:` edge; both skills are tops (nothing loads them), confirmed by grep — no caller's forward graph changes. `orchestrator-artifacts`' reverse-graph marker is a hardcoded list and is correctly updated (Task 6); `roadmap-engine`'s is grep-based and correctly left alone. The "declarations are the map" invariant survives intact.
- **RULES** (`.ai-factory/RULES.md`) — **WARN: absent.** No project rules file; nothing to check against. Non-blocking.
- **ROADMAP** — **OK.** Task linkage is explicit: contract line 21 (`16.1`, `[ ]`) carries `Spec: .ai-factory/specs/71-rescue-skills-rename.md`, which exists and is walked below. The plan's `# Plan:` heading matches the contract line verbatim.
- **Governing spec chain** — walked to the leaf. Spec 71 → its Scope/Guards/Verification → the seven live files on disk. Cross-repo: orchestrator handoffs 06/07 and spec `trickster77777/28` read, since the orchestrator side ran doc-first.

### Verified against ground truth (all confirmed correct)

Every count, line number, and measurement in the plan was independently re-derived. All match:

| Claim | Verified |
|---|---|
| Task 2 — 5 refs in `milestone-rescue/SKILL.md` at 2, 151, 439, 440, 476 | ✅ exact |
| Task 3 — 4 refs in `milestone-rescue-audit/SKILL.md` at 2, 9, 32, 167 | ✅ exact; line 9 is indeed inside `description:` |
| Task 6 — `orchestrator-artifacts` lines 7 and 44 | ✅ exact; line 44 is the third reference the spec omits — assumption 1 is correct, and without it the spec's own grep cannot reach zero |
| Task 7 — `skill-cycle.md` 4 lines / 6 occurrences (41, 43, 70, 71) | ✅ exact |
| Task 8 — `CLAUDE.md` 4 lines / 7 occurrences (36, 57, 78, 193) | ✅ exact |
| Task 5 — `reserved-words.md:11`, `using-the-language.md:35` | ✅ exact |
| `loads:` fields at lines 14 / 16, to stay byte-identical | ✅ exact |
| Symlinks git-tracked, relative, `../../src/skills/<name>` form | ✅ both confirmed |
| `README.md`, `AGENTS.md`, `src/commands/`, `src/agents/`, `src/global/CLAUDE.md`, `.claude/*.json`, `scripts/`, sakshi root `CLAUDE.md` all clean | ✅ swept independently — zero hits |

**Diagram alignment measurements are correct**, and this is the plan's strongest section. `skill-cycle.md` lines 70–71 carry their `←` at 1-indexed column 44, matching the `→` column on lines 61–64, 67, 74, 77; lines 65–66 and 75–76 are a separate nested column and are correctly excluded. `CLAUDE.md:57`'s `#` sits at column 45, matching 51/52/55/56, with 50 and 58 correctly excluded. Both names shorten by exactly 5 characters, so the "+5 spaces, don't move the arrow" instruction holds the column in both files. This is the one class of breakage no grep in Task 9 could catch, and the plan both identified it and measured it rather than asserting it.

**Task 9's filesystem check is genuinely well-reasoned.** The `ls active/skills/ | grep -c milestone` guard exists because `grep -r` neither follows nor matches on symlink names — a surviving `active/skills/milestone-rescue` would pass every textual check while `~/.claude/skills` still loaded it. The `ls -L` dereferencing form catches the wrong-relative-depth link that `ls -l` prints as plausible. The `git status --porcelain` check catches an unstaged `git rm`. Correct threat model, correct instruments.

### Critical Issues

**1. Three scope-expanding assumptions are justified by a plan-review that does not exist (plan lines 11, 13).**

The plan states *"**Ruled in scope by plan-review 1**"* (line 11) and *"All three assumptions were verified against the files and confirmed by plan-review 1, which also swept the repo independently and found the plan's seven target files to be the complete set of live surfaces"* (line 13).

`.ai-factory/plan-reviews/` contains only the three `8.1` reviews. There is no plan-review for 16.1 — **this file is plan-review 1.** The citation is circular: the plan claims prior ratification from the very artifact now being written.

This matters because of what it is holding up. Task 5 edits `docs/reserved-words.md` and `docs/using-the-language.md` — two files **outside spec 71's Scope list and outside its verification grep** (which is scoped to `docs/philosophy/skill-cycle.md`, not `docs`). That is a real deviation from the governing spec, and the plan's only stated authority for it is the nonexistent review. An implementer reading line 11 would treat a settled question as already adjudicated and skip the judgement.

*Fix:* delete both citations and re-state the three assumptions as the implementer's own ground-truth findings, in the `DEVIATION: <spec said / file showed / done>` form. The substance needs no change — see below.

**On the merits, Task 5 is right and should stay.** I verified it independently: both files are `@`-imported into every session via the sakshi root `CLAUDE.md`, so after the rename they would name a nonexistent skill in always-loaded context — a governing spec disagreeing with code, which is a defect to reconcile, not a stale doc to leave. And both sentences are *about* the fixed-form axis, not about the example, so they stay true under the substitution. The finding is the false provenance, not the task.

**2. The closing line's cross-repo claim is stale (plan line 80).**

The plan closes: *"The orchestrator repo invokes these skills by name; that cross-repo update is a separate handoff and is out of scope here."* Ground truth: the orchestrator side **already landed** — its task `8.2` is `[x]`, and `docs/how-it-works.md:25` / `docs/non-convergence.md:37` already carry `/task-rescue` and `/task-rescue-audit`. Per orchestrator spec `trickster77777/28` and handoff 07, this was a deliberate **doc-first** execution: the docs lead as governing spec, and skills 16.1 is *the reconciliation that brings the skills repo to the names the docs already carry*.

Out-of-scope is the correct call, so nothing in Tasks 1–9 changes. But the framing inverts the direction of the dependency: this task is not "ahead of" a pending handoff, it is the trailing half of a rename whose governing docs are already published. Until it lands, the skills repo is the known-divergent side. Re-word to say so — an implementer who believes the orchestrator work is still pending may hesitate on ambiguity that the orchestrator docs have already resolved.

### Positive Notes

- **Assumption 1 is a genuine catch.** Spec 71 lists only the reverse-graph marker for `orchestrator-artifacts`; line 44 ("its only skill-side writer") is a live prose reference to the identifier that the spec misses. The plan found it, and correctly noted that the spec's own verification grep cannot reach zero without it. This is exactly the ground-truth-over-description discipline working.
- **Assumption 2** (references counted per line, not per occurrence) resolves the spec's "×4" ambiguity by giving exact line numbers — the right way to close a counting hole rather than restating it.
- **Phase 2's independence claim is accurate.** Tasks 5–8 touch only files `git mv` does not move and read nothing Phase 1 writes; the stated parallelism is real.
- **Task 9's behavioral check is correctly argued as non-redundant** with the symlink check — a wrong-depth link passes every static check and fails silently at load. Naming *why* a check is not redundant is what stops it being dropped as duplication later.
- **Frozen-history negative control** (`grep .ai-factory/` must *still* return hits) is the right shape: it fails loudly if history was wrongly rewritten, which no positive check would catch.
- **The `ROADMAP.md:27` exclusion is correctly reasoned.** That live `[ ]` 17.1 contract line does contain `milestone-rescue`, but as a scope-exclusion note ("the `milestone-rescue` name refs are Phase 16's") — a statement about ownership, not a live identifier. Leaving it, and explaining why the Task 9 grep is scoped away from `.ai-factory/`, is correct on both counts.

## Deferred observations

- Affects: Phase 17.3 (skill-body prose conformance) — Both `SKILL.md` H1 titles remain `# Milestone Rescue` (line 17) and `# Milestone Rescue Audit` (line 19), and the word `milestone` appears 27 times in the first body and 8 in the second. None contains the hyphenated identifier, so every grep in Task 9 passes clean while the rendered skill still titles itself with a retired reserved word. This is correctly out of 16.1's boundary — spec 71 explicitly binds naming, not spelling, and the plan itself names Phase 17.3 as the owner — but it is worth pinning that 16.1's zero-hit grep is *not* evidence the bodies are conformant, only that the identifier is. Whoever plans 17.3 should not read 16.1's green verification as coverage of the prose. [dismissed — already handled: verified live, both H1s now read "# Task Rescue"/"# Task Rescue Audit" and no bare "milestone" remains outside the exempt "milestone failed" trigger; 16.1 + 17.3 landed this]
- Affects: orchestrator repo (handoff 07) — Handoff 07 re-points orchestrator task 8.2's gate to "run when skills 16.1 is `[x]` **and** `skills/src/skills/task-rescue*` exist on disk", but 8.2 is already `[x]` from the doc-first pass. Once 16.1 lands, someone on the orchestrator side should confirm that gate is genuinely discharged rather than left as a dangling condition on a completed task — it is outside this repo's file boundary, so 16.1 cannot close it. [dismissed — verified in the orchestrator repo: task 8.2 is [x], its re-pointed gate (skills 16.1 [x] + task-rescue* on disk) is genuinely satisfied, not dangling]

---

Two findings, both in the plan's prose rather than its mechanics: a citation of a nonexistent review propping up a real spec deviation, and a stale cross-repo framing. The nine tasks themselves — line numbers, counts, column measurements, verification instruments — were re-derived independently and are correct throughout.
