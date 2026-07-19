# Plan review 2 — 16.1 Rename milestone-rescue → task-rescue, milestone-rescue-audit → task-rescue-audit

## Code Review Summary

**Files Reviewed:** plan (9 tasks) + 9 target files + spec 71 + ROADMAP (Phases 16/17) + plan-review 1 + cross-repo sweep
**Risk Level:** 🟡 Medium (three pinned measurements are wrong; every other value re-derived clean)

### Context Gates

- **ARCHITECTURE** (`.ai-factory/ARCHITECTURE.md`, present) — **OK.** Re-derived the graph independently: `grep -rn '^loads:.*rescue' src/skills/*/SKILL.md src/commands/*.md` returns nothing, so both skills are tops and no caller's forward graph changes. `orchestrator-artifacts` is the only hardcoded reverse marker naming them (Task 6); `roadmap-engine`'s is grep-based and correctly untouched.
- **RULES** (`.ai-factory/RULES.md`) — **WARN: absent.** Nothing to check against. Non-blocking.
- **ROADMAP** — **OK.** `ROADMAP.md:21` is the `[ ] 16.1` contract line carrying `Spec: .ai-factory/specs/71-rescue-skills-rename.md`; the plan's `# Plan:` heading matches it. Spec walked to its leaves.
- **Phase-17 collision check** — **OK, and it favours the plan.** `ROADMAP.md:29` (17.3) explicitly owns `task-rescue`/`task-rescue-audit` body prose and self-gates "after the Phase-16 rename", so the plan's deferral of prose is the roadmap's own sequencing, not an omission. `ROADMAP.md:27` (17.1) owns `orchestrator-artifacts` lines 28–29/49/68/73 — disjoint from Task 6's lines 7 and 44. No task anywhere in the roadmap owns `docs/reserved-words.md` or `docs/using-the-language.md`, which strengthens Task 5: it is the only pass those two files get, so dropping it would leave a nonexistent skill named in always-loaded context permanently.

### Both plan-review-1 findings are properly closed

- The circular citation is gone. The three assumptions are now re-stated as the plan's own ground-truth findings in `DEVIATION: <spec said / file showed / done>` form (lines 9–22), with line 7 stating explicitly that no prior review is cited or relied on. Correct fix, and deviation 3 now flags itself as a judgement call for the implementer to confirm rather than asserting ratification.
- The cross-repo framing is inverted correctly (line 91): the skills repo is now named as the known-divergent trailing half of a doc-first rename, not as running ahead of a pending handoff.

### Verified against ground truth

Every line number, count, and path in the plan was re-derived from the files, not carried from review 1. All match exactly:

| Claim | Verified |
|---|---|
| Task 2 — 5 refs at `2, 151, 439, 440, 476` | ✅ exact |
| Task 3 — 4 refs at `2, 9, 32, 167`; line 9 inside `description:` | ✅ exact |
| Task 6 — `orchestrator-artifacts` lines `7` and `44` | ✅ exact; 44 is the third live ref spec 71 omits — deviation 1 is a real catch |
| Task 7 — `skill-cycle.md` lines `41, 43, 70, 71` (6 occurrences) | ✅ exact |
| Task 8 — `CLAUDE.md` lines `36, 57, 78, 193` (7 occurrences) | ✅ exact |
| Task 5 — `reserved-words.md:11`, `using-the-language.md:35` | ✅ exact |
| `loads:` at lines `14` / `16`, to stay byte-identical | ✅ exact |
| Symlinks git-tracked (mode `120000`), relative `../../src/skills/<name>` | ✅ both confirmed |
| Seven target files are the complete live set | ✅ full-repo sweep excluding `.git`/`.ai-factory`/`upstream` returns exactly those files; `README.md`, `AGENTS.md`, `src/commands/`, `src/agents/`, `src/global/CLAUDE.md`, `scripts/`, sakshi root `CLAUDE.md`, and `orchestrator/` all clean |
| `ROADMAP.md:27` carries the live 17.1 scope-exclusion note | ✅ exact, and the plan's reasoning for leaving it is right |

### Critical Issues

**1. All three pinned column measurements are wrong (plan lines 68, 74).**

The plan presents these as measured facts and tells the implementer to hold those columns. Measured character positions (1-indexed, counting the box-drawing and Cyrillic characters as one column each):

| Plan claims | Actual |
|---|---|
| `skill-cycle.md` arrow column **44** | **42** (lines 61–64, 67, 70, 71, 74, 77 all at 42) |
| `CLAUDE.md:57` `#` column **45** | **35** (lines 48, 49, 51, 52, 55, 56, 58, 59 all at 35) |
| "the two blocks genuinely differ by one" | they differ by **seven** (42 vs 35) |

The *actionable* instruction — "add 5 spaces, do not move the arrow" — is correct regardless, since both names shorten by exactly 5. But the plan wraps that instruction in three fabricated-precise numbers and an explicit warning ("verified by measurement", "don't carry either number to the other file"), which invites the implementer to verify against them. The failure mode is concrete: an implementer who trusts "column 44" over "+5 spaces" measures 42 on lines 70–71 and pads by 7 to reach the stated column, silently breaking the alignment of exactly the two rows this section exists to protect — and the plan itself notes that no grep in Task 9 can catch a broken diagram.

*Fix:* correct the numbers to 42 and 35 and drop the "differ by one" rationale (replace with "the two blocks differ — measure each file, never carry a number across"), **or** delete the absolute columns entirely and keep only the self-verifying rule: both names shorten by 5, so add 5 spaces and leave the arrow where it is.

**2. `CLAUDE.md:58` is wrongly excluded from the shared column (plan line 74).**

The plan states "(Lines 50 and 58 sit at their own offsets already and are not touched.)" Line 50 does sit at its own offset (column 41). Line 58 sits at column **35** — the shared column, same as 48, 49, 51, 52, 55, 56 and 59. It is correctly *not edited* (it carries no `milestone-rescue`), so nothing breaks, but the parenthetical misdescribes the block an implementer is being asked to preserve. Fold it into the shared-column list, or just say "only line 57 is edited; every other row in the block already sits correctly."

**3. Task 9's behavioral check is not executable in the session that performs the rename (plan line 87).**

Task 9 requires invoking `/task-rescue` and `/task-rescue-audit`. `~/.claude/skills` → `/Users/max/projects/sakshi/skills/active/skills` (verified), and Claude Code resolves the skills manifest at session start. An agent that renames the symlinks and then invokes `/task-rescue` in the same session is asking for a skill that did not exist when the manifest was built — it will fail to resolve, and the old `/milestone-rescue` entry may still resolve from the stale manifest while now pointing at a deleted path.

This matters because the plan singles this check out as the one that catches wrong-relative-depth links — the failure that passes every static check. As written the implementer gets a false failure and either reports the rename broken or, more likely, quietly drops the check as unreliable. Either way the one non-redundant behavioral guard is lost.

*Fix:* state that the behavioral check runs in a **fresh session** after Tasks 1–8 are staged, and that a "skill not found" result inside the renaming session is expected and not evidence of failure. If a fresh session is not available to the implementer, say so and mark the check as handed to the next session rather than passed.

### Positive Notes

- **The DEVIATION rewrite is exemplary.** Each of the three now cites what the spec said, what the file showed, and what was done — and deviation 3 explicitly refuses to launder a judgement call as settled, telling the implementer to confirm it and noting that dropping Task 5 leaves the spec's verification passing either way. That is the honest shape for a scope-expanding call.
- **Deviation 1 is a real catch against the governing spec.** `orchestrator-artifacts/SKILL.md:44` is a live identifier reference spec 71's Scope misses, and the plan correctly reasons that the spec's own grep cannot reach zero without it — code over description, applied to a spec that is wrong on a fact rather than on intent.
- **Task 9's filesystem instruments have the right threat model.** `grep -r` neither follows symlinks nor matches on filenames, so a surviving `active/skills/milestone-rescue` would pass every textual check while `~/.claude/skills` still loaded it — hence `ls active/skills/ | grep -c milestone`. `ls -L` catches the wrong-depth link that `ls -l` prints as plausible. `git status --porcelain` catches an unstaged `git rm`. Each instrument is matched to a specific failure, and the plan says which.
- **The frozen-history negative control** (`grep .ai-factory/` must *still* return hits) fails loudly if history was wrongly rewritten — a failure no positive check would surface.
- **Phase 2's independence claim is accurate** — Tasks 5–8 touch only files `git mv` does not move and read nothing Phase 1 writes; the stated parallelism is real.
- **The `ROADMAP.md:27` exclusion is correctly reasoned** — a scope-exclusion note about ownership, not a live identifier, and outside 16.1's file boundary.

## Deferred observations

- Affects: Phase 17.3 (`ROADMAP.md:29`, skill-body prose conformance) — Both `SKILL.md` H1 titles remain `# Milestone Rescue` (line 17) and `# Milestone Rescue Audit` (line 19), and the bare word `milestone` appears 30 times in the first body and 9 in the second. None is the hyphenated identifier, so every grep in Task 9 passes clean while the rendered skill still titles itself with a retired reserved word. Correctly outside 16.1 — spec 71 binds naming not spelling, and 17.3 explicitly owns the rescue pair and self-gates on the Phase-16 rename landing first. Worth pinning that 16.1's zero-hit grep is evidence about the *identifier* only, and whoever plans 17.3 should not read 16.1's green verification as coverage of the prose. [dismissed — already handled: verified live, both H1s now read "# Task Rescue"/"# Task Rescue Audit" and no bare "milestone" remains outside the exempt "milestone failed" trigger; 16.1 + 17.3 landed this]
- Affects: orchestrator repo — Per plan line 91, orchestrator task `8.2` is already `[x]` from a doc-first pass while its docs already publish `/task-rescue` and `/task-rescue-audit`. I did not open the orchestrator-side handoffs, so this is attributed to the plan rather than verified here: once 16.1 lands, someone on that side should confirm any gate conditioned on "skills 16.1 is `[x]`" is genuinely discharged rather than left dangling on an already-completed task. Outside this repo's file boundary, so 16.1 cannot close it. [dismissed — verified in the orchestrator repo: task 8.2 is [x], its re-pointed gate (skills 16.1 [x] + task-rescue* on disk) is genuinely satisfied, not dangling]

---

Three findings, all in Phase 2/3's verification scaffolding rather than the rename itself: three wrong pinned column numbers presented as measured, one misdescribed line in the `CLAUDE.md` tree block, and a behavioral check that cannot run in the session that performs the rename. The nine tasks' line numbers, counts, file set, and graph reasoning were re-derived independently and are correct throughout, and both plan-review-1 findings are properly closed.
