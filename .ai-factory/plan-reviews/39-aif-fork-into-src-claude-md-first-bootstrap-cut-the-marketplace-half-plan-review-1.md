## Code Review Summary

**Artifact Reviewed:** Plan `39-aif-fork-into-src-claude-md-first-bootstrap-cut-the-marketplace-half.md`
**Files the plan targets:** `src/skills/aif/SKILL.md` (forked from `upstream/ai-factory/aif/SKILL.md`, 777 lines), `active/skills/aif`, repo `CLAUDE.md`
**Risk Level:** 🟡 Medium

### Context Gates

- **Roadmap linkage (PASS):** The plan is anchored to ROADMAP line 89 (milestone 39) and spec note 50. The plan's `## Assumptions` section correctly recognizes that the ROADMAP line supersedes note 50 (line frames a *recognizable rework / cut the marketplace half*; note 50 framed *targeted edits only, marketplace untouched*) and explicitly follows the line. This is the right precedence per the review policy ("the ROADMAP line governs"). Note 52 (retire DESCRIPTION.md) and note 41 (drop `Questions` pseudo-tool) are also honored. **WARN (non-blocking):** the plan resolves the note-50-vs-line divergence itself rather than reconciling the note first — acceptable for a plan, but note 50 on disk still says the marketplace stays; a downstream reader of note 50 alone would be misled. Not a plan defect.
- **Architecture / RULES gate:** `.ai-factory/ARCHITECTURE.md` exists; no `RULES.md`. The plan respects the repo's core architectural invariants: `upstream/ai-factory/aif` stays pristine (Task 1), the `active/` symlink repoints to `src/` (Task 1), and repo `CLAUDE.md` bookkeeping moves `aif` from "upstream originals used as-is" to the reconcile-by-diff list (Task 9). The forked skill correctly lives under `src/skills/` outside `.claude/`. **PASS.**
- **≤500-line constraint (WARN):** see Critical Issue #2.

### Critical Issues

**1. Unresolved `{{skills_dir}}` / `{{settings_file}}` template placeholders survive in the KEPT sections — runtime breakage.**
The upstream skill is written for the skills.sh installer, which substitutes `{{skills_dir}}` and `{{settings_file}}` at install time. This repo forks skills directly into `src/` and loads them via the `active/` symlink (`~/.claude/skills/aif` → `active/skills/aif` → `src/skills/aif`) — **there is no substitution step.** Every other forked skill in `src/` (verified: `aif-docs`) contains **zero** `{{...}}` placeholders and uses resolved/relative reference paths.

The plan explicitly keeps the config machinery *"verbatim"* (Tasks 2, 3, 7) and the MCP section, but verbatim retention preserves broken placeholder paths in sections that are NOT cut:
- Config write (kept): `node ~/{{skills_dir}}/aif/references/update-config.mjs --template ~/{{skills_dir}}/aif/references/config-template.yaml ...` — upstream lines 212–213 and 378. This is executed via `node` in Bash **from the project cwd**, so it needs an absolute path; a literal `~/{{skills_dir}}/...` fails at runtime, breaking the core `config.yaml` write.
- MCP config target (kept): `` `{{settings_file}}` `` — upstream lines 394, 519, 717.

No task addresses resolving these. **This is a missing step.** The fork must resolve `{{skills_dir}}` → the real load path (`~/.claude/skills/aif/references/update-config.mjs`, consistent with how forked skills are actually reached) and decide the concrete `{{settings_file}}` target for the MCP section. Recommend adding an explicit sub-step to Task 2 or Task 3: "Resolve all surviving `{{skills_dir}}`/`{{settings_file}}` placeholders to concrete paths — no forked `src/` skill carries install-time mustache tokens." Note that `config-template.yaml` and `update-config.mjs` themselves are correctly copied verbatim (they contain no such tokens); only the *SKILL.md invocation lines* need path resolution.

**2. Mode-1 next-steps menu offers four slash commands that are not in the active set — Task 8 only removes three of the dead references.**
Task 8 removes `/aif-plan`, `/aif-implement`, `/aif-roadmap` from the completion summary. But the Mode-1 "also suggest next steps" block (upstream lines 752–768) offers `/aif-rules`, `/aif-build-automation`, `/aif-ci`, `/aif-dockerize` in an `AskUserQuestion` multi-select, and says "invoke the selected skills sequentially." **None of these four are in the active set** (active `aif*` = `aif`, `aif-architecture`, `aif-skill-generator`, plus our `aif-docs`). Selecting them would invoke skills that don't resolve — the same class of defect note 36 fixed elsewhere ("remove stale pipeline references"). Task 8's wording ("keep only real next steps such as `/aif-docs`, `/aif-architecture`") gestures at this but only enumerates the three summary-line commands to cut. **Broaden Task 8** to explicitly prune the Mode-1 `AskUserQuestion` block down to the real, active next steps (`/aif-docs` is the only survivor there; `/aif-rules`/`-build-automation`/`-ci`/`-dockerize` are not active).

### Non-Critical Issues

**3. ≤500-line target may be hard to hit; the fallback risks behavior loss (WARN).** Upstream is 777 lines. The enumerated cuts (Security ~55, Project Context ~22, Skill Acquisition ~18, DESCRIPTION templates ~40, fat AGENTS.md ~50, language ceremony ~20, localized-heading placeholders, completion trim) total roughly 220–250 lines, and Task 4 adds a ~25–30-line CLAUDE.md section. That lands near ~560–600 — likely still over 500, because the large MCP section (~120 lines, upstream 517–639) and the config-machinery section are kept intact. Task 8's fallback ("tighten prose ... until it fits") then applies pressure precisely to the kept-verbatim sections. Flag: the config-machinery and MCP matrix are contract-sensitive (the note stresses "template verbatim / managed keys unchanged"); tightening must stay in reworked prose, not in those. Consider stating explicitly that the ≤500 tightening budget excludes the verbatim config/MCP text.

**4. `## Artifact Ownership` is edited by both Task 5 and Task 8 (LOW).** Task 5 says "retarget the `## Artifact Ownership` block" (DESCRIPTION → CLAUDE.md); Task 8 says "Update `## Artifact Ownership` to name `CLAUDE.md` instead of `DESCRIPTION.md`." Harmless overlap, but assign the edit to one task to avoid a redundant no-op or contradictory phrasing.

**5. `language.artifacts` becomes a written-but-unused config key (LOW, acceptable).** Task 7 removes all `language.artifacts`-driven templating (artifacts are now always English) but keeps the config machinery verbatim, so `language.artifacts` remains a managed key still written to `config.yaml`. This is a deliberate, reasonable trade-off (avoid touching `update-config.mjs`/template), but it leaves a dead key. Worth one sentence in Task 7 acknowledging the key is retained-but-unconsumed so a later reader doesn't "fix" it by re-wiring artifact localization.

### Positive Notes

- **Correct precedence handling.** The plan's explicit `## Assumptions / spec reconciliation` block resolving the ROADMAP-line-vs-note-50 divergence is exactly the discipline the review policy asks for, and it names the one boundary to confirm with the user (retain `/aif-skill-generator` custom generation or not).
- **Accurate line references.** Spot-checked cut anchors are correct: Security Scanning 16–71, Project Context 73–94, Skill Acquisition 96–113, DESCRIPTION steps (Mode 1 Step 4 @328 / Mode 2 Step 4 @428 / Mode 3 Step 5 @507), fat AGENTS.md 643–708. Task authors clearly read the target file.
- **Clean dependency chain and commit grouping.** Tasks 1→9 are linearly ordered with correct `depends on` links; the 3-commit split (fork+cut / CLAUDE.md-first rework / repo bookkeeping) is coherent and commit messages follow the no-type-prefix convention.
- **Repo `CLAUDE.md` bookkeeping (Task 9) is precise** — all three edits (drop from "used as-is" list, add to reconcile-by-diff with the correct `diff -rq` command, keep out of the "ours, never synced" list) match the current file state exactly.
- **CLAUDE.md-first design aligns with adjacent milestones.** The generated `## Documentation` index in Task 4 dovetails with note 48 (aif-docs now maintains that same CLAUDE.md section in the same `| Doc | What it covers |` format) — the two skills agree rather than collide.

### Verdict

Two must-fix items before implementation: resolve the surviving `{{skills_dir}}`/`{{settings_file}}` placeholders in the kept sections (Critical #1 — genuine runtime break, and a missing step), and broaden Task 8 to prune the Mode-1 dead-skill menu (Critical #2). The rest is solid.
