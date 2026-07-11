# Config Persistence

**Git workflow detection (if `config.yaml` is missing or the `git:` section is incomplete):**

1. Check whether the project uses git:
   - If `.git` exists - set `git.enabled: true`
   - If `.git` does not exist - set `git.enabled: false` and `git.create_branches: false`
2. If git is enabled, detect the default/base branch from git metadata:
   - Prefer `origin/HEAD`
   - Fallback to remote metadata (`git remote show origin`)
   - Fallback to `main`
3. If git is enabled, ask whether full plans should create a new branch (sets `git.create_branches`):

```
AskUserQuestion: How should full plans behave in git?

Options:
1. Create a new branch (Recommended) - a full plan creates a branch and saves as a branch-scoped file
2. Stay on the current branch - a full plan still gets written, but without creating a new branch
```

**Persist resolved settings in `.ai-factory/config.yaml`:**

- Never reconstruct `config.yaml` from memory or by free-writing YAML text.
- Always use `~/.claude/skills/aif/references/update-config.mjs` with `~/.claude/skills/aif/references/config-template.yaml` as the canonical source.
- Write or update `.ai-factory/config.yaml` after `CLAUDE.md` is generated.
- This write MUST happen before `rules/base.md`, MCP config, `AGENTS.md`, and before invoking `/aif-architecture`.
- Ensure `.ai-factory/` exists before writing the payload or target file.
- First write a temporary payload file (for example `.ai-factory/config.update.json`) via `Write`.
- Then invoke the helper:

```bash
node ~/.claude/skills/aif/references/update-config.mjs \
  --template ~/.claude/skills/aif/references/config-template.yaml \
  --target .ai-factory/config.yaml \
  --payload .ai-factory/config.update.json
```

- Use `mode: "create"` when `.ai-factory/config.yaml` does not exist.
- Use `mode: "merge"` when `.ai-factory/config.yaml` already exists.
- Preserve `language.technical_terms` from existing config when present; otherwise set it to `keep` when writing config.
- In `set`, include only values explicitly resolved in the current run and that must be written now.
- In `fillMissing`, include canonical defaults that should be backfilled only when the key or section is missing or incomplete.
- Managed keys for this helper are limited to:
  - `language.ui`
  - `language.artifacts`
  - `language.technical_terms`
  - `paths.*` (including current schema keys such as `paths.qa`)
  - `workflow.*`
  - `git.enabled`
  - `git.base_branch`
  - `git.create_branches`
  - `git.branch_prefix`
  - `git.skip_push_after_commit`
  - `rules.base`
- Never normalize or overwrite `rules.<area>` entries — those are managed by area-specific rules tooling outside this skill.
- The helper must preserve comments, blank lines, section order, inline comments, unknown sections, custom user values outside targeted keys, and the commented `rules.*` examples from the template.
- If the helper reports an unsafe structure or invalid payload, STOP. Do **not** fall back to free-form YAML generation.
- After the helper succeeds, remove the temporary payload file.

**Payload shape:**

```json
{
  "mode": "create|merge",
  "set": {
    "language.ui": "en",
    "language.artifacts": "en",
    "language.technical_terms": "keep",
    "paths.qa": ".ai-factory/qa/"
  },
  "fillMissing": {
    "git.branch_prefix": "feature/",
    "rules.base": ".ai-factory/rules/base.md"
  }
}
```

- Initial create: pass the resolved canonical values through `set`.
- Rerun merge: use `set` only for values re-resolved in this run; use `fillMissing` for canonical defaults that should be restored only when absent or incomplete.
