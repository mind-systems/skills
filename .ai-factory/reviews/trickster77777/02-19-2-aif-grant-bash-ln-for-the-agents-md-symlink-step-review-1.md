# Code Review: 19.2 — aif: grant `Bash(ln *)` for the AGENTS.md symlink step

## Summary

**Files changed:** 1 product file (`src/skills/aif/SKILL.md`, one line) + 3 pipeline artifacts (plan, plan sidecar, plan-review)
**Risk Level:** 🟢 Low
**Verdict:** No findings.

The whole product-surface diff is a single frontmatter token:

```diff
-allowed-tools: Read Glob Grep Write Bash(mkdir *) Skill AskUserQuestion
+allowed-tools: Read Glob Grep Write Bash(mkdir *) Bash(ln *) Skill AskUserQuestion
```

## Verification performed

Each claim was checked against the live file, not against the plan's description of it.

- **The grant matches the command it exists for.** `Bash(ln *)` is a prefix pattern; the only shell invocation in the skill is `ln -sfn CLAUDE.md AGENTS.md` (`src/skills/aif/SKILL.md:161`), which begins with `ln ` and matches. The gap the task names is genuinely closed.
- **No sibling gap left behind.** Swept the file for every shell-command shape (`ln|mkdir|rm|cp|mv|node|npx|git|test|cat|touch|chmod|find|ls` at line start): `ln` at L161 is the *only* hit in the file. There is no second ungranted command riding along, and no now-orphaned grant introduced.
- **The follow-on rule in the same section needs no additional grant.** L164 says that if `AGENTS.md` already exists as a regular file it must be replaced by the symlink. This does **not** require a separate `rm` grant — the `-f` in `ln -sfn` unlinks an existing destination itself. The content-folding half of that rule ("fold that into `CLAUDE.md` first") uses Read/Write, both already granted. So the section is fully covered by the post-change grant list, with nothing broader needed.
- **Minimal grant, honored literally.** `Bash(ln *)` and nothing else; no entry was widened, and no `Bash(*)` appears. This matches both the spec guard and the contract line's explicit prohibition.
- **19.1's edit is preserved.** `Bash(node *update-config.mjs*)` is absent from the post-change line — the retired grant was not reintroduced. The shared-L5 hazard between 19.1 and 19.2 resolved correctly in the ordering that actually occurred.
- **Scope guard respected.** `## AGENTS.md Generation` (L156–164) is byte-identical to HEAD; the diff touches nothing outside frontmatter L5. Every other frontmatter field (`name`, `description`, `argument-hint`) is unchanged, and `name: aif` still matches the directory name as the authoring constraint requires.
- **The change actually reaches the runtime.** `active/skills/aif` is a symlink to `../../src/skills/aif`, and reading the frontmatter *through* the active path shows the new grant. Since `~/.claude/skills` points at `active/`, the edit is live for real `/aif` runs rather than sitting only in the source layer — this is the step that would have silently no-op'd the task had the skill not been in the active set.
- **YAML integrity.** `allowed-tools` remains an unquoted space-separated scalar containing parentheses and `*` but no YAML metacharacter that would change parsing (no `:` followed by space, no leading `[`/`{`). The one field in this frontmatter that *does* need quoting, `argument-hint: "[project description]"`, is untouched and still quoted.

## Runtime-breakage check

Nothing to break. This is a declarative permission grant on a markdown frontmatter field — no code path, no migration, no type surface, no concurrency, no I/O ordering. The change is strictly permission-widening by exactly one narrowly-scoped pattern, so the only behavioral delta is the intended one: the symlink step no longer raises a prompt and no longer stalls a headless orchestrator run. There is no input by which the new pattern grants a command the task did not intend — `Bash(ln *)` cannot match anything but an `ln` invocation.

## Notes (non-blocking, no action required)

- `Bash(mkdir *)` is now a grant with no corresponding `mkdir` in the skill body. It is pre-existing, out of this task's scope, and harmless; flagging only so it is not mistaken for collateral of this edit. Worth a future cleanup task at most.

REVIEW_PASS
