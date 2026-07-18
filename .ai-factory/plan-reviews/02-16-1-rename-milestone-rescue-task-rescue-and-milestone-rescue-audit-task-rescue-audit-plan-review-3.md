# Plan review 3 — 16.1 Rename milestone-rescue → task-rescue, milestone-rescue-audit → task-rescue-audit

## Code Review Summary

**Files Reviewed:** plan (9 tasks) + 7 target files + spec 71 + ROADMAP (Phases 16/17) + plan-reviews 1–2 + cross-repo sweep (orchestrator docs, roadmap 8.2)
**Risk Level:** 🟢 Low — every value re-derived from the files independently; all three plan-review-2 findings closed and the corrections verified as correct, not merely applied

### Context Gates

- **ARCHITECTURE** (`.ai-factory/ARCHITECTURE.md`, present) — **OK.** Re-derived the graph rather than carrying it: `grep -rn '^loads:' src/skills/*/SKILL.md src/commands/*.md | grep -i rescue` returns only the two skills' *own* `loads:` lines (`orchestrator-artifacts roadmap-engine` at `milestone-rescue/SKILL.md:14`, `orchestrator-artifacts` at `milestone-rescue-audit/SKILL.md:16`). Nothing loads them — they are tops, exactly as spec 71 and the contract line state, so no caller's forward graph changes. `orchestrator-artifacts` holds the only hardcoded reverse marker naming them; `roadmap-engine`'s is grep-based and correctly left alone.
- **RULES** (`.ai-factory/RULES.md`) — **WARN: absent.** Nothing to check against. Non-blocking.
- **ROADMAP** — **OK.** `ROADMAP.md:21` is the `[ ] 16.1` contract line carrying `Spec: .ai-factory/specs/71-rescue-skills-rename.md`; the plan's `# Plan:` heading matches it. Spec 71 walked to its leaves.
- **Phase-17 boundary** — **OK, and it ratifies the plan's deferral.** `ROADMAP.md:29` (17.3) names `task-rescue`, `task-rescue-audit` in the post-rename form and self-gates "after the Phase-16 rename, or folded into it", explicitly owning `milestone`→`task` prose and `spec note`→`task spec` (~17 places) in the rescue pair. `ROADMAP.md:27` (17.1) owns `orchestrator-artifacts` lines 28–29/49/68/73 — disjoint from Task 6's lines 7 and 44, and its parenthetical "the `milestone-rescue` name refs are Phase 16's" confirms the split from the other side. No task anywhere owns `docs/reserved-words.md` or `docs/using-the-language.md`, which is what makes Task 5 load-bearing.

### All three plan-review-2 findings are closed — corrections independently re-measured

I re-measured rather than accepting the plan's revised numbers. All three now match ground truth:

| Was wrong in review 2 | Plan now says | Measured |
|---|---|---|
| arrow column 44 | **42** (plan line 70) | ✅ 42 — lines 61–64, 67, 70, 71, 74, 77 all at char col 42 |
| `CLAUDE.md:57` `#` column 45 | **35** (plan line 78) | ✅ 35 |
| "the two blocks differ by one" | "never carry a number across" (42 vs 35) | ✅ the framing is now correct |
| line 58 wrongly called an outlier | folded into the shared-column list; "only line 57 is edited" | ✅ 58 is at 35; line 50 is the sole outlier, at **41**, exactly as the plan states |
| behavioral check unrunnable in-session | plan lines 91–95: fresh session mandatory, in-session "skill not found" declared expected, fallback is "handed to the next session, not passed" | ✅ `~/.claude/skills` → `…/sakshi/skills/active/skills` confirmed; the stale-manifest reasoning holds |

The nested-column exclusion in Task 7 is also correct: lines 65–66 and 75–76 measure 45/41/40/40 — genuinely a separate column, correctly untouched.

### Verified against ground truth

Every line number, count, and path re-derived from the files, not carried from earlier reviews:

| Claim | Verified |
|---|---|
| Task 2 — 5 refs at `2, 151, 439, 440, 476` | ✅ exact |
| Task 3 — 4 refs at `2, 9, 32, 167`; line 9 inside `description:` | ✅ exact — line 9 is in the always-loaded description, as the plan flags |
| Task 5 — `reserved-words.md:11`, `using-the-language.md:35` | ✅ exact; both files confirmed `@`-imported by the sakshi root `CLAUDE.md` |
| Task 6 — `orchestrator-artifacts` lines `7` and `44` | ✅ exact; 44 is the third live ref spec 71's Scope omits |
| Task 7 — `skill-cycle.md` lines `41, 43, 70, 71` = 6 occurrences | ✅ exact |
| Task 8 — `CLAUDE.md` lines `36, 57, 78, 193` = 7 occurrences | ✅ exact (1+2+2+2) |
| `loads:` at lines `14` / `16`, to stay byte-identical | ✅ exact |
| Symlinks git-tracked, relative, two levels | ✅ both mode `120000`; `../../src/skills/<name>` matches every sibling |
| Seven target files are the complete live set | ✅ full-repo sweep excluding `.git`/`.ai-factory`/`upstream` returns exactly those seven; `README.md`, `AGENTS.md`, `src/commands/`, `src/agents/`, `src/global/CLAUDE.md`, `scripts/`, `.claude/*.json`, sakshi root `CLAUDE.md` all clean |
| Cross-repo (plan line 99) | ✅ orchestrator `8.2` is `[x]` at `trickster77777.md:51`, states "executed doc-first by owner decision" and names skills 16.1 as the reconciliation; `how-it-works.md:25` and `non-convergence.md:37` already publish `/task-rescue` and `/task-rescue-audit` |

### Critical Issues

None.

### Positive Notes

- **The column corrections were made the right way.** The plan did not just swap 44→42 and 45→35; it demoted both to "as a cross-check only" and stated the precedence explicitly — "If a measurement conflicts with the '+5 spaces' rule, the rule wins." That inverts review 2's failure mode at the root: the self-verifying rule now governs and the absolute numbers cannot mislead even if a future edit shifts them.
- **The characters-not-bytes warning is a real trap correctly named.** Both blocks mix box-drawing and Cyrillic, so byte offsets do run higher and vary line to line — `skill-cycle.md`'s arrow column is 42 characters but well past that in bytes. An implementer reaching for `awk index()` would have measured a different number and "corrected" a correct block. The plan names the tool that lies and the reading to trust.
- **Deviation 1 is a genuine catch against the governing spec.** `orchestrator-artifacts/SKILL.md:44` is a live identifier reference spec 71's Scope misses, and the plan's reasoning is the decisive one — the spec's *own* verification grep cannot reach zero without it, so the spec is internally inconsistent and the file wins. Ground truth applied to a spec that is wrong on a fact rather than on intent.
- **Deviation 3 refuses to launder a judgement call.** Task 5 expands scope beyond spec 71, and the plan says so in bold, tells the implementer to confirm rather than assume, and notes that dropping Task 5 leaves the spec's stated verification passing either way. The escape hatch is real and costless — the honest shape for a scope-expanding call.
- **Task 9's instruments each have a named threat model.** `grep -r` neither follows symlinks nor matches filenames, so a surviving `active/skills/milestone-rescue` would pass every textual check while `~/.claude/skills` still loaded it — hence `ls active/skills/ | grep -c milestone`. `ls -L` catches the wrong-depth link `ls -l` prints as plausible. `git status --porcelain` catches an unstaged `git rm`. The frozen-history *negative* control (`grep .ai-factory/` must **still** hit) fails loudly on a wrongly-rewritten history — a failure no positive check surfaces.
- **Phase 2's independence claim is accurate.** Tasks 5–8 touch only files `git mv` does not move and read nothing Phase 1 writes; the stated parallelism is real. Task 4's dependency on Task 1 is correctly declared — creating the symlinks first would leave them dangling.
- **The `ROADMAP.md:27` exclusion is correctly reasoned and correctly scoped.** It is a statement about which task owns those refs, not a live identifier — and 17.1 rewrites that region on its own pass.

## Deferred observations

- Affects: Phase 17.3 (`ROADMAP.md:29`, spec `.ai-factory/specs/72-cleanup-coupling-one-dictionary.md`) — Both `SKILL.md` H1 titles remain `# Milestone Rescue` and `# Milestone Rescue Audit`, and `milestone-rescue`'s `description:` still carries "Also checks downstream milestones" and the trigger phrase "milestone failed", while `milestone-rescue-audit`'s opens "Outside-view audit of a milestone that looped". None is the hyphenated identifier, so every grep in Task 9 passes clean while always-loaded description text still names a retired reserved word. Correctly outside 16.1 — spec 71 binds naming not spelling, and 17.3 explicitly owns the rescue pair and self-gates on the Phase-16 rename landing first. Worth pinning that 16.1's zero-hit grep is evidence about the *identifier* only; whoever plans 17.3 should not read 16.1's green verification as coverage of the prose, and should note the trigger phrases sit in the routing surface, so changing them is a behavior question rather than a spelling one.
- Affects: orchestrator repo — Verified this round rather than attributed: orchestrator `8.2` is `[x]` with its docs already publishing `/task-rescue` and `/task-rescue-audit`, so between now and 16.1 landing the two repos are knowingly divergent and the orchestrator docs are the side that leads. Once 16.1 lands, someone on that side should confirm no gate was left conditioned on "skills 16.1 is `[x]`" in a way that silently passed while the skills repo still carried the old names. Outside this repo's file boundary, so 16.1 cannot close it.

---

Round 3 finds no issues. All three plan-review-2 findings are closed, and the corrections were re-measured independently rather than accepted: the arrow column is 42, the tree column is 35, line 58 sits on the shared column and is correctly folded into it, and the behavioral check now mandates a fresh session with the in-session false failure declared expected. The nine tasks' line numbers, occurrence counts, file set, symlink form, and graph reasoning all re-derive clean from the files, and the cross-repo claim about orchestrator 8.2 was verified at its source.

PLAN_REVIEW_PASS
