# Code Review: 5.5 — roadmap-engine: grants restored to what the flow does

## Scope
One code change: `src/skills/roadmap-engine/SKILL.md` line 10 frontmatter grant. (The other staged files are planning artifacts — plan, plan-review, sidecar JSON — not code.)

## Diff
```
-allowed-tools: Read Skill
+allowed-tools: Read Write Edit Glob Grep Bash(git *) Skill
```

## Verification against spec `54-engine-grants-restored.md`
- Grant string matches the spec's pinned value `Read Write Edit Glob Grep Bash(git *) Skill` exactly. ✅
- Change confined to line 10; `git diff` is exactly one line. ✅
- Body byte-identical — no hunks below the frontmatter. ✅
- Other frontmatter keys untouched (`name`, `description`, `user-invocable`, `disable-model-invocation`, `loads: note` all preserved). ✅

## Grant-vs-body alignment (no over/under-granting)
Every restored tool corresponds to an actual body usage:
- `Glob` — codebase structure exploration (SKILL.md:183, :276)
- `Grep` — implemented-features search (SKILL.md:184, :276)
- `Bash(git *)` — `git log --oneline -20` / `git log --oneline --all -30` (SKILL.md:184, :277)
- `Write`/`Edit` — writing/replacing `$TARGET_FILE` and spec notes (SKILL.md:187, :249, :251)
- `Read` — reads `$TARGET_FILE` before modifying (SKILL.md:308)
- `Skill` — loads `note` (`loads: note`)

No tool is granted without a corresponding use; no body-used tool is missing from the grant.

## Runtime considerations
None. This is a static frontmatter declaration; no migrations, types, or concurrency surface. YAML remains valid — `Bash(git *)` is an unquoted scalar with no YAML-special leading character, parses as a plain string token in the space-separated list, consistent with how the rest of the codebase writes such grants.

REVIEW_PASS
