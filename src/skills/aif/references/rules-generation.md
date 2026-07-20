# Rules Generation

**Create `.ai-factory/RULES.md` from codebase evidence:**

Analyze the codebase as a search for **counter-defaults** — branded/opaque types, serialization quirks, forbidden operations, non-obvious invariants — not as a style-inventory pass. Ground truth in the code shows what *is*; it never shows what must *never* change, so that second thing is what this file exists to carry.

A rule earns its line in `RULES.md` iff **both**:
- **(a)** the executor would do otherwise by its own defaults, and
- **(b)** code alone cannot teach it.

Every emitted rule **carries its why** — the incident or invariant behind it. This is the costliest instruction surface per line in the whole system: the orchestrator reads this file mandatorily at Step 0 of all four agents with override authority, treating every line as mandatory. A line that fails either gate is pure ongoing cost with no benefit.

**Excluded anti-pattern:** generic language/style conventions the agent already follows by default are **not** rules and must never be emitted — this includes case styles (`snake_case`, `PascalCase`, `UPPER_SNAKE_CASE`), formatting, idiomatic naming, and boilerplate error/logging idioms. These fail gate (b): code alone teaches them, so a generated rule restating them is waste, not guidance.

When the codebase surfaces no counter-default, the correct result is a **near-empty file** — header note plus nothing. The criterion admits nothing rather than manufacturing rules to fill sections.

Create `.ai-factory/RULES.md` with only the rules that pass the filter above. Use fixed **English** headings and service text in this file:

```markdown
# Project Base Rules

> Counter-defaults the executor would otherwise violate by its own defaults, each with its why. Generic style/formatting conventions are deliberately excluded. If the codebase has no counter-default, this file stays empty below this note — that is the correct result, not a gap to fill in.

## Data Types

- Proto numeric fields are carried as strings, not native ints — why: cross-language proto codegen silently truncates int64 on JS clients.

## Identifiers

- Entity IDs use branded/opaque types (e.g. `UserId`), never raw `string` — why: prevents accidental mixing of unrelated entity IDs at compile time.

## Migrations

- No hand-written SQL migrations — all schema changes go through the generator — why: hand-written migrations previously drifted from the ORM schema and broke a prod rollback.
```

*The sections and rules above (modeled on `tradeoxy_core/RULES.md`) are illustrative of the **genre** only, not a literal scaffold — generation must substitute the target project's own counter-defaults. Never emit these literal proto/branded-ID/migration rules into a project that has no protos, branded IDs, or migrations. Emit a section only where a real counter-default was found; an idiomatic or greenfield project correctly yields just the header note with no sections below it.*
