# Plan: frontmatter: `Skill` joins `allowed-tools` wherever the body loads via the Skill tool

## Context
Close the body-vs-grant gap: every `src/skills/*/SKILL.md` (and `src/commands/*.md`) whose body instructs invoking the Skill tool must list `Skill` in `allowed-tools`, so headless orchestrator runs actually inject the engine into context instead of denying the load.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Execution-time inventory (verify before editing — files are in flux)
Re-run the grep-driven audit at execution time; do not trust this static list blindly. As of planning, the audit surfaced these **gaps** (body invokes the Skill tool, `allowed-tools` omits `Skill`):

| File | Current `allowed-tools` | Body Skill-tool invocation |
|------|------------------------|----------------------------|
| `src/skills/roadmap-prune/SKILL.md` | `Read Write Edit Bash(git *) Bash(rm *) Glob Grep` | `:20` load `orchestrator-artifacts` |
| `src/skills/milestone-rescue/SKILL.md` | `Read Write Edit Glob Grep Bash(git *) AskUserQuestion` | `:33` load `orchestrator-artifacts` |
| `src/skills/milestone-rescue-audit/SKILL.md` | `Read Glob Grep Bash(git *)` | `:38` load `orchestrator-artifacts` |
| `src/skills/roadmap-engine/SKILL.md` | `Read` | `:34` load `note` (`via the Skill`↵`tool` — prose-only, line-wrapped) |

Already carry `Skill` (no edit): `roadmap-outline`, `roadmap-decompose`, `roadmap-decompose-skeleton`, `roadmap-test-coverage`, `command-handoff`.

Out of scope: `src/agents/editor.md` (agent definition, not `src/skills/*` or `src/commands/*`; already grants `Skill`).

## Tasks

### Phase 1: Grant alignment

- [x] **Task 1: Re-run the grep-driven audit and confirm the gap set**
  Files: (read-only) `src/skills/*/SKILL.md`, `src/commands/*.md`
  Start from the `loads:` declarers (`grep -rn "^loads:" src/skills/*/SKILL.md src/commands/*.md`), then `grep -rn "Skill tool" src/skills/*/SKILL.md src/commands/*.md` plus a multi-line sweep for the wrapped `via the Skill\ntool` form. For each hit, check whether its `allowed-tools` line already contains `Skill`. The gap set must match the four files in the inventory table above; reconcile any drift before proceeding. A skill whose body never invokes the Skill tool gets no edit.

- [x] **Task 2: Append `Skill` to the four `allowed-tools` lines** (depends on Task 1)
  Files: `src/skills/roadmap-prune/SKILL.md`, `src/skills/milestone-rescue/SKILL.md`, `src/skills/milestone-rescue-audit/SKILL.md`, `src/skills/roadmap-engine/SKILL.md`
  In each file, edit only the `allowed-tools:` line — append a single space + plain `Skill` at the end. Exact results:
  - `roadmap-prune`: `allowed-tools: Read Write Edit Bash(git *) Bash(rm *) Glob Grep Skill`
  - `milestone-rescue`: `allowed-tools: Read Write Edit Glob Grep Bash(git *) AskUserQuestion Skill`
  - `milestone-rescue-audit`: `allowed-tools: Read Glob Grep Bash(git *) Skill`
  - `roadmap-engine`: `allowed-tools: Read Skill`
  Plain, unscoped `Skill` only — no `Skill(<name>)` form (unverified frontmatter syntax). Do not touch `name`, `description`, `argument-hint`, or `loads:`. Every body byte-identical. Never touch `upstream/ai-factory/`.

- [x] **Task 3: Verify the pairing invariant** (depends on Task 2)
  Files: (read-only) `src/skills/*/SKILL.md`, `src/commands/*.md`
  Confirm: (1) every file whose body invokes the Skill tool now carries `Skill` in `allowed-tools` — zero files with the instruction and without the grant; (2) `git diff` shows only `allowed-tools` lines changed (four lines, four files), nothing else.
