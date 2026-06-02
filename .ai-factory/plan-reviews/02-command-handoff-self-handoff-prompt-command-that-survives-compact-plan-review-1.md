# Plan Review — command-handoff (self-handoff prompt command that survives /compact)

**Plan:** `.ai-factory/plans/02-command-handoff-self-handoff-prompt-command-that-survives-compact.md`
**Risk Level:** 🟢 Low

## Context Gates

- **Architecture (`.ai-factory/ARCHITECTURE.md`):** PASS. The doc currently opens with "This repo produces skills" and frames everything through skill anatomy. The plan's Task 4 explicitly closes the divergence by registering `.claude/commands/` as a second hosted artifact type. Alignment is handled, not ignored. ✅
- **Rules (`.ai-factory/RULES.md`):** Not present — skipped (WARN, non-blocking). Relevant conventions are instead enforced in `CLAUDE.md` (quoted `argument-hint` brackets, English content, never auto-commit, upstream-sync custom-skill protection) and the plan respects all of them.
- **Roadmap (`.ai-factory/ROADMAP.md`):** PASS. The work maps 1:1 to the in-flight milestone *"command-handoff: self-handoff prompt command that survives /compact"* and to its spec note `12-task-command-handoff.md`. Linkage is explicit. ✅

## Codebase Verification

I verified the plan's assumptions against the live repo:

- ✅ `.claude/commands/` exists and is empty — plan correctly says "author only the file, do NOT mkdir".
- ✅ `~/.claude/commands` → `~/projects/skills/.claude/commands` symlink exists — plan correctly says "do NOT ln".
- ✅ `~/.claude/skills` symlink mirrors the same whole-dir pattern, so the commands setup is architecturally consistent with the existing skills setup.
- ✅ `.ai-factory/notes/` exists with notes `01`–`15`; next prefix is `16`. The plan's "scan `[0-9][0-9]-*.md`, increment highest" rule matches `aif-note`'s numbering verbatim.
- ✅ `aif-note/SKILL.md` confirms the plan's rationale for NOT routing through it: aif-note reshapes content into its own `# Topic / Key Findings / Details / Open Questions` template, which would destroy the handoff skeleton.
- ✅ `README.md` "Setup (one-time, per machine)" currently has only the skills symlink — Task 3's target text exists as described.
- ✅ `CLAUDE.md` has both the "Repository Structure" tree and "Upstream Sync" custom-skills list — Task 2's targets exist as described. Editing the existing tree (rather than introducing a new one) does not violate the global "no file/directory trees" rule.
- ✅ File paths and slash-command frontmatter fields (`description`, `argument-hint`, `allowed-tools`, `$ARGUMENTS`) are all valid for Claude Code commands.

## Critical Issues

None. No missing migrations, no security holes, no incorrect paths or API misuse. The command writes only under `.ai-factory/notes/` with a derived slug — no injection or sensitive-data surface.

## Minor Issues / Suggestions

### 1. `mkdir` is used but not pre-approved in `allowed-tools` (WARN)
Task 1 instructs the note path to run `mkdir -p .ai-factory/notes`, but the specified frontmatter is `allowed-tools: Read Write Glob Bash(ls *)` — it pre-approves `ls` but **not** `mkdir`. This contradicts the task's own stated rationale ("pre-approves to skip permission stalls"): the `mkdir` call would still trigger a permission prompt. (The same gap exists in spec note 12, so it's inherited, not introduced.)

Resolve one of two ways during implementation:
- Add `Bash(mkdir *)` to `allowed-tools` (matches `aif-note`, which lists both `Bash(ls *)` and `Bash(mkdir *)`); **or**
- Drop the `mkdir` step entirely — `.ai-factory/notes/` already exists and Claude Code's `Write` auto-creates parent directories, making `mkdir` redundant. This keeps `allowed-tools` minimal.

Either is fine; just make the body and `allowed-tools` agree.

### 2. `Glob` + `Bash(ls *)` are partially redundant (informational)
Both are listed for scanning existing `<NN>` notes. One tool suffices (Glob alone can enumerate `[0-9][0-9]-*.md`). Harmless, but the implementer could trim to whichever the command body actually uses, to keep `allowed-tools` tight.

## Positive Notes

- The plan faithfully implements spec note 12 and the roadmap milestone — no scope drift.
- Correctly distinguishes **command vs skill** and avoids the `aif-` prefix, protecting the upstream-synced namespace.
- The "do NOT route through aif-note" decision is well-justified and verified against the actual aif-note template.
- Two-phase structure with explicit dependencies (Tasks 2–4 depend on Task 1) is clean and matches the atomic-task discipline used elsewhere in this repo.
- Anticipates the doc-divergence problem (ARCHITECTURE.md vs CLAUDE.md) and the fresh-machine setup gap (README symlink) — both are genuine consequences of adding a new artifact type, and both are addressed.

The plan is solid; the only actionable item is the small `mkdir`/`allowed-tools` consistency fix, which is non-blocking.

PLAN_REVIEW_PASS
