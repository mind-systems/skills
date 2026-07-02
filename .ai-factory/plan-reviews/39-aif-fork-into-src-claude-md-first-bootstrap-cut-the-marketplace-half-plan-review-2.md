## Code Review Summary

**Artifact Reviewed:** Plan `39-aif-fork-into-src-claude-md-first-bootstrap-cut-the-marketplace-half.md` (revision 2)
**Files the plan targets:** `src/skills/aif/SKILL.md` (forked from `upstream/ai-factory/aif/SKILL.md`, 778 lines), `src/skills/aif/references/*`, `active/skills/aif`, repo `CLAUDE.md`
**Risk Level:** 🟢 Low

### Review-1 follow-up (both must-fix items resolved)

- **Critical #1 (unresolved `{{skills_dir}}`/`{{settings_file}}` placeholders) — FIXED.** The plan now carries an explicit Assumptions clause ("Install-time mustache tokens must be resolved to concrete paths") and a dedicated sub-step in Task 3 that resolves `{{skills_dir}}` → `~/.claude/skills/aif/references/…` (upstream ~212–213, ~378), `{{settings_file}}` → `.mcp.json` (upstream ~394, ~519, ~717), and notes `{{skills_cli_agent_flag}}` vanishes with the cut install lines. The backstop assertion — `grep '{{' src/skills/aif/SKILL.md` must return nothing — is exactly the right closing gate. I cross-checked every `{{…}}` occurrence in the upstream file (lines 53, 59, 63, 104, 105, 212, 213, 378, 388, 390 for `skills_dir`; 104, 386 for `skills_cli_agent_flag`; 394, 519, 717 for `settings_file`): each is either inside a cut section or explicitly resolved by Task 3. Complete.
- **Critical #2 (Mode-1 dead-skill next-steps menu) — FIXED.** Task 8 now explicitly targets the Mode-1 `AskUserQuestion` multi-select (upstream ~752–768), removes `/aif-rules`, `/aif-build-automation`, `/aif-ci`, `/aif-dockerize` (none active), keeps `/aif-docs` as the only survivor, and collapses to a plain recommendation if the menu empties to one option. Correct.
- **Non-critical #3/#4/#5 — all addressed.** ≤500 tightening budget now explicitly excludes the verbatim config/MCP text (Task 8); `## Artifact Ownership` is assigned to Task 5 only with Task 8 told not to touch it; the written-but-unconsumed `language.artifacts` key is acknowledged in Task 7.

### Context Gates

- **Roadmap linkage (PASS).** Plan is anchored to ROADMAP line 89 (milestone 39) and spec note 50. The `## Assumptions / spec reconciliation` block correctly asserts the ROADMAP line governs over note 50 where they diverge (line = "cut the marketplace half / rework recognizably"; note 50 = "targeted edits only, marketplace untouched") and follows the line. Note 52 (retire DESCRIPTION.md) and note 41 (drop the `Questions` pseudo-tool) are honored. **WARN (non-blocking, unchanged from review-1):** note 50 on disk still says the marketplace stays, so a reader of note 50 alone is misled — a plan is entitled to resolve this, but the note is now stale. Not a plan defect.
- **Architecture / RULES gate (PASS).** `.ai-factory/ARCHITECTURE.md` exists; no `RULES.md`. The plan honors the repo's core invariants: `upstream/ai-factory/aif` stays byte-pristine (Task 1 verifies), the `active/` symlink repoints to `src/` with the correct relative target (`../../src/skills/aif` from `active/skills/`), the fork lives under `src/skills/` outside `.claude/`, and repo `CLAUDE.md` bookkeeping moves `aif` to the reconcile-by-diff list (Task 9). The verbatim-copy discipline for `references/update-config.mjs` + `config-template.yaml` matches the "template verbatim / managed keys unchanged" contract.
- **≤500-line constraint (WARN):** see Non-Critical #4.

### Critical Issues

None. Both review-1 blockers are resolved and no new runtime-breaking issue was found.

### Non-Critical Issues

**1. Task 9 removes `aif` from the upstream trio but does not re-home it in the "our skills" enumeration — `aif` would vanish from the active-set paragraph (LOW).**
Repo `CLAUDE.md` line 62 reads: *"our skills — `detangle`, …, `observe-logs` — plus three upstream originals we use as-is: `aif`, `aif-architecture`, `aif-skill-generator`."* Task 9 item (1) only says "remove `aif` … (now two)." Taken literally, `aif` is deleted from the trio and not added anywhere, so a now-ours, still-active skill ends up listed in neither group of the active-set sentence. Add `aif` to the "our skills" list in that same sentence so it stays visible. (The parallel "Everything else in `src/skills/` is ours … sync never touches it" list at line 169 correctly must NOT get `aif` — the plan already gets that right.)

**2. Task 3's "Mode 1 Step 7–8" reference is imprecise, and the "Present Plan & Confirm" skills template isn't explicitly enumerated (LOW).**
The per-skill install+scan lines actually live in Mode 1 **Step 8 "Execute", sub-items 7–8** (upstream ~384–393), not in "Step 7–8" (Step 7 is "Present Plan & Confirm"). Separately, Step 7's plan template (upstream ~354–372) renders a `### Skills / From skills.sh / Generate custom` block that is pure marketplace content and needs pruning under the same "split the skills column out, keep MCP" instruction — the plan gestures at this ("remove 'Recommend Skills & MCP' … keep MCP detection") but doesn't name the Present-Plan template. The implementer reading the file will likely catch both, but tightening the reference would remove the ambiguity.

**3. Task 7 neutralizes `language.artifacts` but doesn't enumerate the Language-Resolution artifact list at upstream ~136 (LOW).**
Line 136 (`language.artifacts — use for … .ai-factory/DESCRIPTION.md, .ai-factory/rules/base.md, AGENTS.md, …`) both names the now-retired DESCRIPTION.md (Task 5) and drives the artifact-localization that Task 7 removes. Task 7's "remove … everywhere" is broad enough to cover it, but this specific line is neither cut by Task 5 nor named by Task 7. Worth an explicit mention so the DESCRIPTION.md reference and the artifacts-localization framing in the Language Resolution section are cleaned in the same pass.

**4. ≤500 lines remains tight; the fallback still pressures a real prose budget (WARN, unchanged in spirit).**
Rough arithmetic: upstream 778 − enumerated cuts (~250: Security ~55, Project Context ~22, Skill Acquisition ~18, DESCRIPTION templates ~40, fat AGENTS.md ~50, skills-recommendation/search/install ~30, language ceremony ~20, intro bullets + localized placeholders) + CLAUDE.md section (~30) ≈ **~558**. That leaves roughly ~55 lines to squeeze out of "reworked prose only" (Task 8 correctly fences off the verbatim config/MCP text). Achievable, but not comfortable — the kept MCP section (~120 lines, upstream 517–639) and the config machinery are both large and untouchable. If the CLAUDE.md/AGENTS.md/language/summary prose can't absorb the full ~55, the plan should say what gives (accept a small overage vs. re-scope) rather than silently pressuring the contract-sensitive text. No change strictly required — the constraint and its budget fence are stated — but flag that the target is at the edge.

**5. Cutting `/aif-skill-generator` custom-generation is a flagged judgment call, not a ROADMAP mandate (LOW, acceptable).**
The ROADMAP Cut list names "skills.sh install + both security-scan levels + Python-probe ceremony, skill-context/aif-evolve, localized headings, DESCRIPTION.md, fat AGENTS.md" — it does **not** explicitly name custom-skill generation, and `aif-skill-generator` *is* in the active set (so an invocation would resolve). The plan reads "cut the marketplace half" as including the generation hook because it was gated on "search skills.sh first, else generate," and flags the one boundary to confirm. That reading is defensible and the escape hatch is stated, so this is not a blocker; noting it so the orchestrator/user is aware a functional, active skill's invocation is being dropped by interpretation rather than by explicit instruction.

### Positive Notes

- **The revision is tightly responsive to review-1.** Every must-fix and every non-critical note from the prior round has a corresponding, correctly-scoped change — including the `grep '{{'` closing gate, which is the right way to make placeholder resolution verifiable rather than aspirational.
- **Placeholder accounting is now exhaustive and correct.** I independently mapped all `{{…}}` occurrences to cut-or-resolved; nothing is left dangling. The `{{skills_dir}}` → `~/.claude/skills/aif/references/…` resolution correctly follows the real symlink chain (`~/.claude/skills/aif` → `active/skills/aif` → `src/skills/aif`).
- **Clean dependency chain and commit grouping.** Tasks 1→9 are linearly ordered with correct `depends on` links; the 3-commit split (fork+cut / CLAUDE.md-first rework / repo bookkeeping) is coherent and the messages follow the no-type-prefix, sentence-case convention.
- **Repo `CLAUDE.md` reconcile-list bookkeeping (Task 9 items 2–3) matches the file exactly** — `aif-docs`/`aif-plan` are the current reconcile entries, the `diff -rq src/skills/aif upstream/ai-factory/aif` command is correct, and keeping `aif` out of the "ours, never synced" list is right.
- **CLAUDE.md-first design coheres with adjacent milestones** — the Task 4 `## Documentation` index (`| Doc | What it covers |`) matches the format aif-docs maintains (note 48), the AGENTS.md one-liner matches the standing global convention, and the update-not-clobber rule plus the explicit "no assumption that rich chat context is always present" caveat directly honor note 50's "What NOT to do."

### Verdict

The two review-1 blockers are resolved and no new critical or runtime-breaking issue remains. The five items above are all LOW/WARN bookkeeping refinements that the implementer can absorb without a re-plan. Approving.

PLAN_REVIEW_PASS
