## Code Review Summary

**Files Reviewed:** 1 plan + 2 target skills (`roadmap-outline/SKILL.md`, `aif-docs/SKILL.md`)
**Risk Level:** 🟢 Low

### Context Gates
- **Architecture** (`.ai-factory/ARCHITECTURE.md` present): PASS — change is confined to `src/skills/` (the "ours" layer) and the plan explicitly forbids touching `upstream/ai-factory/`. No boundary or dependency implications; frontmatter token edits don't alter the skill graph (`loads:` fields untouched).
- **Rules** (`.ai-factory/RULES.md`): absent — WARN (optional file, not blocking).
- **Roadmap** (`.ai-factory/ROADMAP.md`): PASS — plan title matches milestone line 73 verbatim ("frontmatter tool hygiene: drop `Questions` pseudo-tool; fix aif-docs Bash rule syntax"), which names `Spec: .ai-factory/notes/41-frontmatter-tool-hygiene.md`.
- **Governing spec** (note 41): PASS — the plan reproduces the spec's two edits, "frontmatter-only", "don't touch the body", and "never touch the upstream mirror" constraints faithfully.
- **Downstream linkage**: PASS — milestone line 81 (`roadmap-outline: slim to philosophy-only`) explicitly instructs "don't reintroduce ... the `Questions` pseudo-tool", corroborating that removal (not retention) is the intended end state.

### Verification of plan claims against the codebase
- `Questions` token exists at exactly line 5 in both `roadmap-outline/SKILL.md` and `aif-docs/SKILL.md` — confirmed. It appears nowhere else in either body (the only other `Questions` hit repo-wide is `note/SKILL.md:65` "## Open Questions", an unrelated heading). Removing it from `allowed-tools` breaks no body reference.
- The exact source strings the plan quotes for replacement match the files byte-for-byte, including the `Bash(mkdir, npx, python)` comma form and the surrounding tokens (`AskUserQuestion`, `Skill`, `WebFetch`, `WebSearch`).
- Line numbers cited (line 5 in both) are correct.
- The corrected per-command glob syntax `Bash(mkdir *) Bash(npx *) Bash(python *)` matches the established convention already used elsewhere in the repo — `roadmap-test-coverage/SKILL.md:13` uses `Bash(npx *)`, `Bash(python *)`, `Bash(mkdir *)`. The fix is consistent, not novel.
- The plan's assertion that the 1/2/3 menus already run via `AskUserQuestion` is verified: `aif-docs` uses `AskUserQuestion:` at lines 137/191/247/511 and `roadmap-outline` at lines 48/59/89/119. Both retain `AskUserQuestion` in `allowed-tools`, so no dialog regresses.

### Critical Issues
None.

### Minor Notes
- Commit message "Drop non-existent Questions tool and fix aif-docs Bash rule syntax" complies with the repo's commit conventions (imperative, sentence case, no type prefix). A single commit for two edits is fine here — both are one concern (frontmatter tool hygiene), so no body is needed.
- Scope discipline is good: the plan proactively flags `aif-docs`' >500-line body as a known accepted deviation and keeps it out of scope, matching spec note 41 §"What NOT to do".

### Positive Notes
- Every replacement string is exact and unambiguous, so the implementing agent has zero guesswork — the edits are mechanical `old → new` swaps.
- Correctly distinguishes the two independent defects in `aif-docs` (dead `Questions` token vs. malformed `Bash` rule) and fixes both in one coherent edit.
- Faithful to the two-tier artifact chain: contract line → spec note 41 → plan, with no drift.

PLAN_REVIEW_PASS
