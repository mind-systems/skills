# Architecture

This repo produces skills. A skill is a directory with a `SKILL.md` at its root.

## Skill anatomy

```
<skill-name>/
├── SKILL.md          # required — frontmatter + instructions (≤ 500 lines)
├── references/       # long-form docs referenced from SKILL.md
├── scripts/          # executable helpers (Python, Bash)
└── templates/        # output templates used during skill execution
```

## Skill categories

| Prefix | Role |
|--------|------|
| `aif-*` | AI Factory lifecycle (plan, implement, review, …) |
| *(none)* | Domain skills (detangle, ui-ux-pro-max, …) |

The repo also hosts slash commands under `src/commands/` (e.g. `command-handoff`), symlinked to `~/.claude/commands` for global availability.

## Dependency model

Skills invoke other skills by name (`/aif-skill-generator`, `/aif-architecture`). There is no import graph — invocations are runtime text instructions, not code dependencies. Keep coupling minimal and explicit.

## Composition: mechanism vs policy

A skill is a unit of content loaded into context, not a compiled object. Every loaded line is a recurring token cost, so abstraction is never free at runtime — the opposite of compiled code, where a delegating layer compiles away. This inverts the rule for extraction: factor a capability into its own skill only when it carries **shared content** — a mechanism, rule, or format used by two or more callers. A skill that only routes to other skills, with no content of its own, is negative value.

Two kinds of skill follow, mirroring the classic separation of mechanism and policy:

- **Engine (mechanism)** — the shared *how*: a procedure, format, or render step, with no decision of its own.
- **Philosophy (policy)** — the *what* and *whether*: a gate, lens, or strategy that decides. `roadmap-decompose`'s atomicity gate is policy.

A philosophy skill invokes an engine for mechanism; the engine holds no policy and never drives. Control stays with the caller — the engine renders when handed work, the way a strategy varies independently of the context that runs it. A shared skill is loaded once for its content (load-once), never re-loaded per item. `roadmap-decompose` invoking `aif-note` for note format is this pattern: the caller keeps control, the loaded skill supplies shared content.

## Key constraints

- `name` in frontmatter = directory name (enforced by validator)
- `argument-hint` values with `[...]` must be quoted in YAML
- External skills are scanned before use; built-in `aif*` skills are not
