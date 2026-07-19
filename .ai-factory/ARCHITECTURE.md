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

The repo also hosts slash commands under `src/commands/` (e.g. `command-handoff`), and an agent-definitions category under `src/agents/` (the `editor` paired-loop subagent; its architect counterpart is the `agent-architect` skill living in `src/skills/`) — parallel to `src/skills/` and `src/commands/`.

Three zones keep provenance clean: `src/` holds skills, commands, and agent skills we authored or reworked; `upstream/ai-factory/` is a pristine mirror of `lee-to/ai-factory` (refreshed by `scripts/sync-upstream.sh`, never hand-edited); `active/` is the curated working set — per-item symlinks into `src/` or `upstream/` — and is the only layer `~/.claude/skills`, `~/.claude/commands`, and `~/.claude/agents` point at.

## Dependency model

Skills invoke other skills by name (`/aif-skill-generator`, `/aif-architecture`). There is no import graph — invocations are runtime text instructions, not code dependencies. Keep coupling minimal and explicit.

## Composition: mechanism vs policy

A skill is a unit of content loaded into context, not a compiled object. Every loaded line is a recurring token cost, so abstraction is never free at runtime — the opposite of compiled code, where a delegating layer compiles away. This inverts the rule for extraction: factor a capability into its own skill only when it carries **shared content** — a mechanism, rule, or format used by two or more callers. A skill that only routes to other skills, with no content of its own, is negative value.

Two kinds of skill follow, mirroring the classic separation of mechanism and policy:

- **Engine (mechanism)** — the shared *how*: a procedure, format, or render step, with no decision of its own.
- **Philosophy (policy)** — the *what* and *whether*: a gate, lens, or strategy that decides. `roadmap-decompose`'s atomicity gate is policy.

A philosophy skill invokes an engine for mechanism; the engine holds no policy and never drives. Control stays with the caller — the engine renders when handed work, the way a strategy varies independently of the context that runs it. A shared skill is loaded once for its content (load-once), never re-loaded per item. `roadmap-decompose` invoking `roadmap-engine` for the two-tier artifact format is this pattern: the caller keeps control, the loaded engine supplies shared content.

## Key constraints

- `name` in frontmatter = directory name (enforced by validator)
- `argument-hint` values with `[...]` must be quoted in YAML
- External skills are scanned before use; built-in `aif*` skills are not

## Features (roadmap-prune v2)

A single skill's own capability accumulates no row here — each skill is enumerated under `src/` with its per-file git history. The table records the cross-cutting capabilities and foundations that no single skill holds alone — what the system does across many skills or the whole fleet — plus the prune ledger.

| Feature | Hashes |
|---------|--------|
| **Foundation** | |
| Reserved-words language — the semantic contract every skill body, `description:`, roadmap, and spec is written in; specified in `docs/reserved-words.md` (+ `docs/skill-description-field.md`, how it loads) and mandated from the root CLAUDE.md. | a379ac9 039bf45 |
| Manage a project's coordination-layer tree — from one authoring system, hold every project's CLAUDE.md tree and `.ai-factory/` to the harness wiring contract: drive a convention across the whole fleet, detect and repair drift, cold-rehydrate any leaf from its own tree. Model: `docs/sakshi-harness/sakshi-harness.md`. | 0aa7a99 |
| Multiuser roadmaps — per-developer named roadmaps (`.ai-factory/roadmaps/<slug>.md`, slug from git `user.email`), the `> Owner:` single-writer line, the family's target-file resolution order, and per-roadmap spec/artifact subdirectories; the default single `ROADMAP.md` layout stays valid unchanged. Model: `docs/philosophy/multiuser-roadmaps.md`. | b2272fe |
| Governing-spec-leads-code doctrine — the global CLAUDE.md recognizes two doc modes: a governing spec states intended behavior and leads its code; a description lags, and code wins. | 94ad78d |
| AGENTS.md is a symlink to CLAUDE.md — the one-line-pointer form is retired; the convention lives in the global CLAUDE.md and the `aif` generator that emits `ln -sfn CLAUDE.md AGENTS.md`. | c02c3c0 |
| **Internal** | |
| Roadmap drop history | 2d2f3f6, 902f7d9, 5348761 |
