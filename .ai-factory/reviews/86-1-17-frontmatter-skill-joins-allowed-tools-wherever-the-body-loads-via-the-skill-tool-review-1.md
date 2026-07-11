# Review: 1.17 — `Skill` joins `allowed-tools` wherever the body loads via the Skill tool

## Scope
Frontmatter-only grant alignment. Reviewed `git diff HEAD` and each changed file in full.

## Changes verified
Four `allowed-tools` lines, one per file, plain unscoped `Skill` appended:
- `src/skills/milestone-rescue-audit/SKILL.md` → `Read Glob Grep Bash(git *) Skill`
- `src/skills/milestone-rescue/SKILL.md` → `Read Write Edit Glob Grep Bash(git *) AskUserQuestion Skill`
- `src/skills/roadmap-engine/SKILL.md` → `Read Skill`
- `src/skills/roadmap-prune/SKILL.md` → `Read Write Edit Bash(git *) Bash(rm *) Glob Grep Skill`

## Correctness checks
- **Bodies byte-identical.** `git diff` touches only the `allowed-tools:` line in each file; `name`, `description`, `argument-hint`, `loads:` untouched. ✓
- **Pairing invariant holds.** Every `loads:` declarer in `src/skills/*/SKILL.md` + `src/commands/*.md` whose body invokes the Skill tool now carries `Skill` in `allowed-tools`; zero files with the instruction and without the grant. Cross-checked all nine declarers — all `grant=yes` where `invokes=yes`. ✓
- **`roadmap-engine` (the line-wrapped `via the Skill`↵`tool` prose case) is covered** — the one gap a naive single-line grep would miss. ✓
- **No over-granting.** `command-handoff` already carried `Skill`; the four skills already carrying it (`roadmap-outline`, `roadmap-decompose`, `roadmap-decompose-skeleton`, `roadmap-test-coverage`) were not re-touched. No skill lacking a Skill-tool body invocation received a grant. ✓
- **`upstream/ai-factory/` untouched.** ✓
- **Grant form.** Plain `Skill`, no unverified `Skill(<name>)` scoping. ✓
- No runtime/type/migration surface — these are agent-frontmatter tool grants, inert until an interactive/headless run resolves them.

## Notes (non-findings)
- `src/agents/editor.md` invokes the Skill tool and already grants `Skill`; correctly left out of scope (agent def, not `src/skills/*`/`src/commands/*`).

REVIEW_PASS
