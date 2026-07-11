# Plan: 1.9.1 — aif: rules generation gets the counter-default entry filter

## Context
The rules-generation step of `aif` currently emits generic style conventions the executor already follows. This milestone adds a counter-default **entry filter** so `rules/base.md` only ever holds rules the executor would otherwise violate, that code alone cannot teach, each with its why.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

All changes land in the single rules-generation block of `src/skills/aif/SKILL.md` (the `**Create .ai-factory/rules/base.md from codebase evidence:**` section, currently ~lines 144–183, and its mirror inside Mode 1 Step 7 item 6, ~line 242). Config machinery (config.yaml helper, MCP, CLAUDE.md-first ordering), other modes' skeletons, and any already-generated project rules files stay untouched — this task changes only *what the rules artifact is allowed to say*.

### Phase 1: Entry filter + anti-pattern

- [x] **Task 1: State the two-part entry filter with the why-requirement**
  Files: `src/skills/aif/SKILL.md`
  In the `**Create .ai-factory/rules/base.md from codebase evidence:**` block, replace the current instruction (which tells the agent to detect naming/module/error/logging/test patterns and emit them wholesale) with the admission criterion from the spec. State it as the gate the generated file must satisfy: **a rule earns its line iff (a) the executor would do otherwise by its own defaults, AND (b) code alone cannot teach it** (ground truth shows what *is*, never what must never change). Every emitted rule **carries its why** — the incident or invariant behind it. Frame the codebase analysis as a search for counter-defaults (branded/opaque types, serialization quirks, forbidden operations, non-obvious invariants), not a style-inventory pass. State that when the codebase surfaces no counter-default, the correct result is a near-empty file — the criterion admits nothing rather than manufacturing rules to fill sections (Task 3 carries the same rule into the template). Reference the composition-model reasoning already cited in the spec (`.ai-factory/specs/41-aif-rules-counter-default-filter.md`) so the "costliest instruction surface" motive is explicit in the skill text.

- [x] **Task 2: Name generic style conventions as the excluded anti-pattern** (depends on Task 1)
  Files: `src/skills/aif/SKILL.md`
  In the same block, add an explicit exclusion: generic language/style conventions the agent already follows by default — case styles (`snake_case`, `PascalCase`, `UPPER_SNAKE_CASE`), formatting, idiomatic naming, boilerplate error/logging idioms — are **not** rules and must not be emitted. Name them as the anti-pattern (with these concrete examples) so generation stops producing them. This is the criterion's contrapositive made loud, so a rule failing gate (b) is recognizably rejected.

### Phase 2: Template rewrite

- [x] **Task 3: Rewrite the `rules/base.md` template examples to the passing genre** (depends on Tasks 1–2)
  Files: `src/skills/aif/SKILL.md`
  Rewrite the fenced `# Project Base Rules` template (SKILL.md:156–183) so it no longer seeds boilerplate. Specifically:
  - **Remove the `## Naming Conventions` block** (Files/Variables/Functions/Classes placeholders) and any other placeholder that invites style-inventory output.
  - **Remove the `## Control Flow` block** (SKILL.md:176–178). Unlike the other sections it is not a `[detected pattern]` placeholder but a fully-written, always-emitted prose rule ("Prefer flat, readable control flow over deeply nested conditionals. Use guard clauses, early `return`/`continue`…"). It fails both gates of the new filter — the executor already prefers guard clauses/early returns by default (gate a), and code alone teaches this style (gate b) — so it is exactly the boilerplate the milestone deletes and must not survive in the reshaped template.
  - **Replace the example rows with counter-default rules in the passing genre** — each a rule + its why, modeled on the `tradeoxy_core/RULES.md` examples cited in the spec (e.g. proto numerics carried as strings, branded/opaque UUID types, no hand-written migrations). Reshape sections so each holds only counter-defaults-with-why. **Mark these examples as illustrative, not literal scaffold:** they show the *genre*, and generation must substitute the target project's own counter-defaults — never emit the tradeoxy proto/UUID/migration rules into a project that has no protos, branded IDs, or migrations (that would reintroduce the "rule the executor can't act on" problem from the other direction). State this in the template (e.g. via the header note) so an implementer does not bake them in as fixed content.
  - **Make the empty result valid:** because the filter (a ∧ b) yields few or zero rules for an idiomatic/greenfield project, the template and the reshaped instruction must state that a near-empty `rules/base.md` — header note plus nothing — is the **correct** output when the codebase has no counter-default. Generation must not manufacture rules to fill sections.
  - **Rewrite the header note** `> Auto-detected conventions from codebase analysis. Edit as needed.` — it describes the old raw-detection dump and contradicts the new genre; replace it with a note that names the genre (counter-defaults the executor would otherwise violate, each with its why). Keep the file's fixed **English** headings.
  - **Update the Mode 1 Step 7 item 6 mirror** (SKILL.md:242–244): "Write `.ai-factory/rules/base.md` with detected conventions in English" → replace "detected conventions" with the filtered-genre wording, preserving the trailing "in English" (the filtered genre still emits English headings/text).

  Verification (single scope): `grep -i "PascalCase\|snake_case\|UPPER_SNAKE"` over the fenced `# Project Base Rules` template block only (SKILL.md:156–183, not the instruction prose) returns **zero** — the anti-pattern examples from Task 2 live in the instruction block, not the template, so a template-scoped grep is a clean pass/fail gate.
