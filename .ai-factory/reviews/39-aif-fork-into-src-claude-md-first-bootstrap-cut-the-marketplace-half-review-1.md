# Code Review — Milestone 39: aif fork into `src/`, CLAUDE.md-first bootstrap

**Reviewed:** `git diff HEAD` + full read of new/changed files
**Files:** `src/skills/aif/SKILL.md` (new, 496 lines), `src/skills/aif/references/{update-config.mjs,config-template.yaml}` (new), `active/skills/aif` (symlink repointed), `CLAUDE.md` (repo bookkeeping)
**Risk:** 🟡 Low–Medium — one ordering defect, the rest are polish/consistency leftovers. No security issues.

## Verified correct

- **Symlink repoint:** `active/skills/aif` → `../../src/skills/aif` ✓; `upstream/ai-factory/aif` untouched.
- **References verbatim:** `diff -q` shows `update-config.mjs` and `config-template.yaml` byte-identical to upstream. ✓
- **Placeholder resolution (plan Critical #1):** `grep '{{'` on the new SKILL.md returns nothing. `{{skills_dir}}` → `~/.claude/skills/aif/references/…` (lines 95–98, 240 — resolves through `~/.claude/skills` → `active/skills/aif` → `src/skills/aif`, correct for a `node` call from the project cwd); `{{settings_file}}` → `.mcp.json` (lines 245, 322, 460); `{{skills_cli_agent_flag}}` gone. ✓
- **Cuts:** Security Scanning, Project Context/aif-evolve, Skill Acquisition, DESCRIPTION.md generation, fat AGENTS.md template, skills.sh install/scan steps, Python-probe ceremony — all absent. ✓ `## AGENTS.md Generation` collapsed to the one-line pointer (lines 446–454). ✓
- **Repo `CLAUDE.md` bookkeeping (Task 9):** `aif` dropped from "used as-is" (now two originals), added to reconcile-by-diff with the correct `diff -rq src/skills/aif upstream/ai-factory/aif`, and correctly kept out of the "ours, never synced" list. ✓
- **≤500 lines:** 496. ✓ Config-machinery and MCP matrix untouched by the diet, as the plan required.

## Findings

### 1. (Medium) Language resolution is ordered *after* CLAUDE.md generation — Mode 3 asks its first prompt in an unresolved `language.ui`
The milestone requires CLAUDE.md to be the first *artifact*. The implementation went further and pushed `language.ui` resolution to *after* CLAUDE.md generation in every mode (Mode 1 Step 2→3, Mode 2 Step 1→2, Mode 3 Step 1/2→3). Two consequences:

- **Concrete contradiction (Mode 3):** Step 1 "Ask Project Description" ends with *"Ask this prompt in resolved `language.ui`"* (line 296), but `language.ui` is only resolved in Step 3 (line 300). On a fresh empty directory there is no config/AGENTS/CLAUDE/RULES to read, so at Step 1 the resolved value is undefined — the instruction references state that does not exist yet.
- **Resolution-chain pollution (all modes):** `language.ui` resolves in the order `config.yaml → AGENTS.md → CLAUDE.md → RULES.md → chat/repository context → ask` (line 49). On a fresh project, config.yaml/AGENTS.md don't exist yet, so the just-generated **English** CLAUDE.md (line 33: "before … config.yaml") becomes the first existing source the resolver hits — inserted *ahead of chat/repository context*. Since artifacts are now always English by design (Task 7), that freshly-written English file can bias `language.ui` to English and short-circuit the chat-context/ask fallbacks. For a user who drives `/aif` in Russian, the run can end up communicating in English.

**Fix:** resolve `language.ui` *before* generating CLAUDE.md. Language resolution produces no artifact, so doing it first does not violate "CLAUDE.md is the first artifact." Reorder each mode to: resolve language → generate CLAUDE.md → config.yaml → … This also removes the Mode 3 Step 1 contradiction. (Upstream resolved language first in every mode; the reorder is what introduced this.)

### 2. (Low) Stale references to non-active skills survive in kept sections — inconsistent with Task 8's dead-reference pruning
Task 8 pruned dead slash-command references from the completion summary and the Mode-1 menu, but three references to skills not in the active set remain elsewhere:
- Git-workflow question (lines 74, 80–81): the whole `AskUserQuestion` is framed as *"how should `/aif-plan full` behave in git"* — `aif-plan` is stored but not symlinked into `active/`.
- Line 118: *"Those belong to `/aif-rules`"* — `aif-rules` is not in the active set.

These sit inside the "config machinery kept verbatim" region, so this is a judgment-call boundary rather than a hard bug — the `git.create_branches` key they gate is legitimately managed. But the user-facing dialog names a skill the user cannot invoke, which is the same defect class note 36 addressed. Consider retargeting the git question's rationale to the config key itself (branch-on-full-plan behavior) without naming `/aif-plan`, and softening the `/aif-rules` aside.

### 3. (Low) Dangling anchor `#architecture-generation`
Line 247 links *"(see [Architecture Generation](#architecture-generation))"* but there is no `## Architecture Generation` heading — the architecture step lives under `## CRITICAL: Do NOT Implement`. Inherited from upstream (the same dead anchor existed there), but it is now in a file we own. Point it at the real section or drop the parenthetical.

### 4. (Low) Duplicate "Step 7" label
Mode 1's execute step is "Step 7: Execute" (line 235), and the global architecture step is also "**Step 7: Generate Architecture Document**" (line 475). Two different Step 7s. Upstream avoided the collision because Execute was Step 8 (DESCRIPTION.md removal renumbered it). Relabel the global one (e.g. "Final step") or fold it into Mode 1's Step 7.9, which already says the same thing.

### 5. (Low) Config-source prose path is inconsistent with the executed command
Line 87 names the canonical helper as `skills/aif/references/update-config.mjs` (no `~/.claude/` prefix), while the runnable command below (lines 95–98) and Mode 1 Step 7.4 (line 240) correctly use `~/.claude/skills/aif/references/…`. Not a runtime break (the executed lines are correct), but an agent skimming line 87 could read a bare relative path that wouldn't resolve from the project cwd. Align line 87 to `~/.claude/skills/aif/references/…`.

### 6. (Low) Stale trigger phrase in `description`
Frontmatter `description` still ends with `"what skills do I need"` (line 3), but skill acquisition/recommendation was cut. Harmless as a routing trigger, but it advertises a capability the skill no longer has. Optional: replace with a setup-oriented phrase.

## Notes
- Non-critical plan item #5 (dead `language.artifacts` key) is correctly implemented: line 47 documents it as written-but-unconsumed. ✓
- The generated `## Documentation` index format (`| Doc | What it covers |`, line 37) matches the format `aif-docs` maintains (note 48) — the two skills agree. ✓

Finding #1 is the only one that changes runtime behavior; #2–#6 are consistency/polish. None block, but #1 should be fixed before this ships.
