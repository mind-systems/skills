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

## Dependency model

Skills invoke other skills by name (`/aif-skill-generator`, `/aif-architecture`). There is no import graph — invocations are runtime text instructions, not code dependencies. Keep coupling minimal and explicit.

## Key constraints

- `name` in frontmatter = directory name (enforced by validator)
- `argument-hint` values with `[...]` must be quoted in YAML
- External skills are scanned before use; built-in `aif*` skills are not
