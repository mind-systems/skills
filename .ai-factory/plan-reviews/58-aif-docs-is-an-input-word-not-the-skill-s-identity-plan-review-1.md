## Code Review Summary

**Files Reviewed:** 1 plan (`src/skills/aif-docs/SKILL.md` as the sole target)
**Risk Level:** 🟢 Low

### Context Gates

- **Roadmap (WARN → clear):** The plan's `# Plan:` heading matches ROADMAP.md line 127, `- [ ] **aif-docs: ТЗ is an input word, not the skill's identity**`, whose `Spec:` tag points to `.ai-factory/specs/12-aif-docs-tz-input-not-identity.md`. Milestone linkage is present and correct.
- **Governing spec (clear):** All four exact target strings in the plan (Tasks 1–4) are byte-for-byte identical to the strings pinned in spec note 12, items 1–2. The plan's Guards section reproduces the spec's Guards faithfully (referent-conditional logic untouched, no new mode/lead-lag, no `references/` edits, upstream mirror never touched).
- **Architecture / Rules:** No `.ai-factory/ARCHITECTURE.md` boundary or `RULES.md` convention is crossed — this is a single-file wording reframe within an existing "ours / never-overwrite" skill. Skill-graph gate: `aif-docs` declares no `loads:` and nothing loads it (verified by grep), so there is no reverse-graph contract to honor; the reframe is genuinely isolated.

### Critical Issues

None.

### Verification of codebase assumptions (all confirmed)

- **ТЗ occurrence census:** `grep` over `src/skills/aif-docs/` returns exactly four matches — `:3` (description), `:13` (H1), `:15` (identity paragraph, twice), `:19` (Core Principles opener, twice). These are precisely the four spots the plan targets. `references/` contains zero ТЗ, matching the plan's claim that the verify grep spans them only as a safety net.
- **Line numbers:** `:3`, `:13`, `:15`, `:19` in the plan match the live file exactly. Guard references also verified: Step 1 referent logic is at `:70`, Step 2.1 staleness carve-out at `:318`, Step 4 referent-conditional Technical Accuracy checks at `:369-374`. All correct.
- **Behavior-identical claim holds:** The four replacements swap `ТЗ` → `governing spec` and drop the H1's stale "Docs -" prefix without touching any Step/mechanism. The dual-write feature (spec-ahead-of-code vs. shipped-behavior) lives entirely in the guarded lines, which the plan explicitly forbids editing.
- **Frontmatter `description`:** The new string is ~470 chars, well under the 1024-char cap. Dropping the "living ТЗ —" appositive leaves a clean single em-dash construction ("as a present-tense governing spec … connections — split by topic …") that reads correctly. ТЗ survives only as the two Russian input triggers appended to the "Use when user says…" list, exactly as the spec's re-anchoring intent requires.
- **No stale mirrors:** The old description text ("living ТЗ") and H1 ("Docs - ТЗ") appear nowhere else in the repo except the plan, roadmap line, and spec note — no CLAUDE.md doc-index row or other file duplicates them, so no secondary edit is needed. The CLAUDE.md skill-list description regenerates from frontmatter at load time.

### Positive Notes

- Every replacement string is pinned verbatim, so the orchestrator guesses nothing — the correct pattern for a rename pass.
- Task dependencies (1→2→3→4→5) are ordered and the final task is verification-only with a concrete grep, matching the spec's Verify section.
- Guards correctly protect the actual feature (referent-conditional dual-write) from being misread as removable alongside the label — this is the exact failure mode the spec warns about.
- Scope discipline is explicit: no fork, no size/state-machine/`--web`/checklist changes, no `references/` edits, upstream mirror untouched.

PLAN_REVIEW_PASS
