# Code review 2 (re-review) — 16.1 Rename milestone-rescue → task-rescue, milestone-rescue-audit → task-rescue-audit

## Code Review Summary

**Files Reviewed:** full `git diff HEAD` (17 files) + both renamed `SKILL.md` re-read in full + all cross-reference targets re-read at their cited lines + plan + spec 71 + ROADMAP
**Risk Level:** 🟢 Low — the single finding from review 1 is fixed cleanly, and the full mechanical suite was re-derived from disk rather than carried from the prior pass

## Verdicts on review-1 findings

### Finding 1a — unplanned doctrinal paragraph at `docs/philosophy/skill-cycle.md:45` — **FIXED**

Re-read the file. The ~200-word paragraph asserting *"задачи над скилами не сходятся чаще кодовых при том же ревьюере"* is gone. Current content at and around the cited line:

```
43  Остановка на лимите итераций оставляет артефакты на диске. `task-rescue` диагностирует
    глубину корня (task-spec? план? код?), чинит на эту глубину и откатывает sidecar …
44
45  ## Тесты — `roadmap-test-coverage`
```

Line 45 is now the next section heading; the section ends at line 43 exactly as it did before the task. `git diff HEAD -- docs/philosophy/skill-cycle.md` confirms the file's entire change set is now **4 lines, identifier-only** — the heading (41), the body prose (43), and the two diagram rows (70–71) — matching plan Task 7's scope verbatim. The revert was surgical: no collateral edits, no whitespace damage.

### Finding 1b — unplanned cross-reference sentence at `docs/philosophy/skill-composition-model.md:49` — **FIXED**

Re-read the file. The added sentence pointing at `skill-cycle.md` is gone. Current content at the cited line:

```
47  Проверка существует, но она динамическая: ревью процессов и живые прогоны. …
48
49  ## Что специфицировать, а что доверить исполнителю
```

Line 49 is the original section heading, and line 47 flows directly into it. `git diff HEAD --stat -- docs/philosophy/skill-composition-model.md` returns **empty** — the file is byte-identical to HEAD and no longer appears in `git status` at all. It is correctly back outside the task's file boundary, where the plan and spec 71 both leave it.

**No dangling reference resulted from the revert.** The two additions were a reciprocal pair; both are gone, so neither side points at a removed section.

## Full re-verification (re-derived from disk this pass)

| Check | Result |
|---|---|
| `grep -rIn 'milestone-rescue' src active docs CLAUDE.md` | ✅ zero hits |
| Full-repo sweep excl. `.git`/`.ai-factory`/`upstream` | ✅ zero files |
| `name:` matches directory | ✅ `task-rescue` (L2), `task-rescue-audit` (L2) |
| `loads:` byte-identical | ✅ `orchestrator-artifacts roadmap-engine` (L14); `orchestrator-artifacts` (L16) |
| Symlink git mode | ✅ both `120000` |
| Symlink targets | ✅ `../../src/skills/task-rescue`, `../../src/skills/task-rescue-audit` — correct depth |
| Dereference (`ls -L`) | ✅ both resolve to a real `SKILL.md` |
| Old symlink names gone | ✅ `ls active/skills/ \| grep -c milestone` → 0 |
| `orchestrator-artifacts` L7 + L44 | ✅ both updated — incl. the sidecar-prose ref spec 71 omitted |
| `reserved-words.md:11` / `using-the-language.md:35` | ✅ identifier substituted, surrounding sentences intact |
| `skill-cycle.md` arrow column | ✅ char 42 across 61–64, 67, 70, 71, 74, 77 — uniform |
| `CLAUDE.md` tree `#` column | ✅ char 35 across 48–59 (L50 the pre-existing outlier at 41, untouched) |
| Frozen `.ai-factory` history | ✅ negative control passes — 12 files still carry the old names |
| `ROADMAP.md:21` still `[ ]` | ✅ expected; the orchestrator marks it at commit |

**Both `SKILL.md` bodies re-confirmed identifier-only.** Normalizing old and new identifiers to a common placeholder and diffing pre/post returns *identical* for both files this pass — no prose drifted into either body, so the Phase-17.3 boundary is intact.

**Behavioral check discharged with evidence.** This session's skills manifest lists **`task-rescue`** and **`task-rescue-audit`** under their new names carrying the updated description text (including audit's "Run right after `task-rescue`"). Both resolve and load — the wrong-relative-depth failure the plan singled out as the one silent breakage did not occur.

## New issues

None. The revert introduced no regressions, and no new surface changed since review 1.

## Deferred observations

- Affects: Phase 17.3 (`ROADMAP.md:29`) — Both skill bodies still title themselves `# Milestone Rescue` and `# Milestone Rescue Audit`, and the bare word `milestone` remains throughout both — including in `task-rescue-audit`'s `description:`, which is always-loaded context. None of it is the hyphenated identifier, so every grep in this task passes clean. 16.1's green verification is evidence about the **identifier only**; 17.3 should not read it as prose coverage. [dismissed — already handled: verified live, both H1s now read "# Task Rescue"/"# Task Rescue Audit" and no bare "milestone" remains outside the exempt "milestone failed" trigger; 16.1 + 17.3 landed this]
- Affects: orchestrator repo — Orchestrator task `8.2` is `[x]` from the doc-first pass and its docs already publish `/task-rescue` and `/task-rescue-audit`; with 16.1 landing the two repos are consistent. Someone on that side should confirm any gate conditioned on "skills 16.1 is `[x]`" is genuinely discharged rather than left dangling on an already-completed task. Outside this repo's boundary. [dismissed — verified in the orchestrator repo: task 8.2 is [x], its re-pointed gate (skills 16.1 [x] + task-rescue* on disk) is genuinely satisfied, not dangling]
- Affects: whoever curates the philosophy docs — The reverted paragraph was well-written and its cross-references were correctly formed; the objection was venue, not quality. If the convergence-cost argument is wanted, it needs its own roadmap task — and its central empirical claim (skill tasks converge more slowly than code tasks at the same reviewer) deserves a reviewer, since nothing in the repo measures it today. [dismissed — optional future work nobody has claimed; no roadmap task requests the convergence-cost argument]

REVIEW_PASS
