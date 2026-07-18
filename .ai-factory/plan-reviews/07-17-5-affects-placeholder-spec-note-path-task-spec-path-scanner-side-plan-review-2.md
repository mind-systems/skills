# Plan Review: 17.5 — `- Affects:` placeholder: `spec-note path` → `task-spec path` (scanner side)

## Code Review Summary

**Files Reviewed:** 1 plan + target file `src/skills/orchestrator-artifacts/SKILL.md`, task spec `.ai-factory/specs/73-affects-placeholder-task-spec-path.md`, `.ai-factory/ROADMAP.md:31`, `skills/CLAUDE.md`, `docs/using-the-language.md`
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture (`.ai-factory/ARCHITECTURE.md`)** — OK. The change is a one-field rename inside an engine skill; no boundary, `loads:` edge, or reverse-graph marker is touched. Task 0 explicitly enforces the engine-caller grep that `skills/CLAUDE.md` § "Dependencies and the skill graph" requires before editing an engine.
- **Rules (`.ai-factory/RULES.md`)** — not present; no gate. The governing conventions in force (`docs/reserved-words.md`, `docs/using-the-language.md` § "Protocol tokens are a different axis") are honored: the rename touches vocabulary (`spec-note` → the registry name `task spec`), while every scanned literal is held byte-identical.
- **Roadmap** — OK. The plan maps to `.ai-factory/ROADMAP.md:31` (`17.5`), and its `Spec:` tag resolves to `.ai-factory/specs/73-affects-placeholder-task-spec-path.md`, which exists and matches the plan clause for clause.

### Verified Against Ground Truth

Every factual claim in the plan checks out against the files:

- `SKILL.md:53` is `## 5. `## Deferred observations` section`; the entry placeholder is on lines 55–56, wrapped mid-placeholder exactly as the plan describes (`- Affects: <phase / spec-note path /` ⏎ `"unknown"> — <observation>`). The field to change sits on line 55 — correct.
- `spec-note` occurs exactly once in `src/`, `docs/`: `orchestrator-artifacts/SKILL.md:55`. (The other repo occurrence is the roadmap contract line `ROADMAP.md:31` itself, which names the task and must not change — the plan correctly leaves it alone.)
- `grep -c '## Deferred observations'` is currently `2` (lines 5 and 53), so Task 2's "→ 2, unchanged" is the right expected value. Line 5 is the frontmatter `description:` field — the plan's "the description prose" names it accurately, and its separate guard "do not touch the frontmatter (`description:`…)" points the same way, so the two instructions converge rather than conflict.
- `task-spec path` currently has zero occurrences in the file, so Task 2's "line 55 only" is a valid post-condition, not a pre-existing match.
- The byte-length claim holds: `spec-note path` and `task-spec path` are both 14 bytes, so the wrap column of line 55 genuinely does not move and the "do not reflow" instruction is achievable.
- Task 0's expected grep result is confirmed: the only `Affects:` references outside the target are `roadmap-prune/SKILL.md:61` and `task-rescue-audit/SKILL.md:60` (both naming it as a target field only) and `docs/using-the-language.md:35` (naming the token with the placeholder elided). No caller reads the inner field text — the engine's contract is unaffected.
- Cross-repo lockstep is real, not asserted: the spec names the emitter-side spec path and commit `8f34644` with `reviewer.md:108` reading `task-spec path`, and pins the identical field string `<phase / task-spec path / "unknown">` on both sides. The pair converges on the shared pin, so scanner-side-last is safe.
- Editing `src/skills/orchestrator-artifacts/SKILL.md` is the correct path — `active/skills/` holds a symlink into `src/`, so the working set follows automatically with no second write.

### Critical Issues

None.

### Positive Notes

- The plan's guard list is a faithful, non-lossy restatement of the spec's guards, including the subtle one: the per-side tail difference (`— <observation>` here as a format description vs. `— <one-paragraph observation>` in the emitter as a length instruction) is explicitly marked "recorded difference, not drift. Do not 'harmonize' it." That is exactly the failure mode a well-meaning implementer would walk into.
- Task 0 is not ceremony — it converts a CLAUDE.md obligation into an executable pre-check with a stated expected result *and* an explicit stop condition ("if any caller does depend on the inner field, stop and report"), so a surprise halts the run instead of being absorbed.
- Task 2's verification set is well-chosen: three positive/negative content checks plus a `git diff` shape check that would catch any collateral reflow the content greps would miss. The closing instruction — "correct the edit rather than adjusting the check" — forecloses the usual escape hatch.
- The scope fence ("this is the sanctioned unfreeze of exactly one field frozen by task 17.1; it is not a licence to re-edit the rest of the file") correctly anticipates that the implementer will be reading a file certified conformant by a prior task and might be tempted to keep going.

PLAN_REVIEW_PASS
