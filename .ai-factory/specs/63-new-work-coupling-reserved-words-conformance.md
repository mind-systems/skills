# The "new work" coupling: one dictionary in the authoring skills

Task 17.2 of the One-dictionary direction. Governing spec: [reserved-words](../../docs/reserved-words.md). Naming-only conformance: retire synonyms for registry concepts; spelling is ordinary English (attributive hyphens stay, noun uses unhyphenated). Zero behavior change.

## Current state — per-file inventory (line numbers from the 2026-07-13 grep; re-verify by grep before editing)

**`roadmap-outline` (75 lines)** — carries the flagship:
- `description` line 3: "major **milestones**" describes the **product** → **`phases`** (outline produces `### Phase N` headers). The trigger word "milestones" in the same line's `Use when user says "roadmap", "project plan", "milestones", …` list **stays** — it matches user input, which the contract exempts.
- `spec note` (40) → **`task spec`**.
- **Already conformant, leave**: `contract line` (25), `Named roadmap` (53 — a reference to roadmap-engine's "Named roadmaps" section title; quoted section titles stay as written).

**`aif-docs` (271 lines)**:
- `spec note` (70) → **`task spec`**.
- "ROADMAP **milestone**" (70, "gather … from the stated user intent, task spec, or ROADMAP milestone") → **`ROADMAP phase`** (aif-docs' governing spec is phase-scoped).
- **Leave**: `governing spec` spellings (already plain-conformant); "this milestone" (26, 182) — a **mention**, a forbidden-phrase in the no-history detection list ("we changed", "was added", "this milestone"), not a unit-naming.

**`roadmap-decompose` (97 lines)** — flagship:
- `milestone`/`milestones`/`Milestones` → **`task`(s)** (decompose's product is the `N.M` task): `description` "atomic, granular milestones" (4) and "adding milestones that need to be implementation-ready" (8); body 17, 41, 75, 83; Critical-Rule heading line 92 "**Milestones** are atomic and specific" → "Tasks are atomic and specific". No milestone trigger — the `Use when` list already says "break down tasks / spec tasks / create tasks".
- `spec note` (18, 93) → **`task spec`**.
- **Already conformant, leave**: `contract line` (6 places), `two-tier` spellings, `named roadmap` (64, 70 — casing per grammatical position).

**`roadmap-decompose-skeleton` (148 lines)**:
- `milestone`/`milestones` → **`task`(s)** (skeleton splits tasks): 96, 98, 102, 122, 124, 125, 130.
- `spec note` (35, 117, 127) → **`task spec`**.
- **Already conformant, leave**: `contract line` / attributive `contract-line text` (132), `two-tier`, attributive `silent-failure`/`loud-failure`, generic "field" (91, "in the field" — idiom).

**`agent-architect` (119 lines)** — no synonym tokens. **Audit-clean → no change.**

**`editor.md` (88 lines)** — no synonym tokens. **Audit-clean → no change.**

**`command-pin-gaps` (26 lines)** — **audit-clean under the plain-form contract**: `contract line` (17) already conformant; "Named roadmaps" (17) is a quoted section-title reference; "field types" (21) generic. **No change.**

## Change

Retire the synonyms above (`milestone`→phase/task by producer, `spec note`→`task spec`). Behavior byte-identical.

## Files & types

`src/skills/{roadmap-outline,aif-docs,roadmap-decompose,roadmap-decompose-skeleton,agent-architect}/SKILL.md`, `src/agents/editor.md`, `src/commands/command-pin-gaps.md`. Frontmatter `name` / `loads:` / `allowed-tools` untouched (except the synonym tokens *inside* a `description:` value); no `references/` touched.

## Guards

- **Output-naming vs user-trigger.** In a `description:`, "milestone" naming the skill's **product** → `phase` (outline) / `task` (decompose); "milestone" inside a `Use when user says "…"` trigger list **stays** (the contract binds output, not user input). Only `roadmap-outline` has such a trigger.
- **milestone → phase or task by producer.** `roadmap-outline` produces phases → `phase`; `roadmap-decompose` / `-skeleton` produce and split tasks → `task`.
- **aif-docs' semantics untouched.** The two-doc-mode doctrine landed in Phase 13 (global CLAUDE.md); this task only swaps the two synonym tokens listed.
- **Detection-list mentions left.** aif-docs' no-history forbidden-phrase list ("this milestone") is a phrase to scrub, a mention — not a roadmap-unit naming.
- **Generic `field` left.** "in the field" (skeleton) and "field types" (pin-gaps) are idiom / data-fields, not the skill description field.
- **`agent-architect`, `editor`, `command-pin-gaps` land no change** — verify zero synonym tokens; their inclusion is a certification.
- Spelling is ordinary English — attributive hyphens and sentence-start/heading capitals stay. `loads:` edges + reverse-graph markers byte-identical; `` Spec: `` / `Governing spec:` tags + `.ai-factory/specs/` stay legacy; behavior byte-identical (a rename that changes an artifact's shape is a bug).

## Verification

- `grep -in 'spec note' src/skills/{roadmap-outline,aif-docs,roadmap-decompose,roadmap-decompose-skeleton}/SKILL.md src/commands/command-pin-gaps.md` → zero.
- `grep -inE '[^-]milestones?' src/skills/{roadmap-outline,roadmap-decompose,roadmap-decompose-skeleton,aif-docs}/SKILL.md` → only `roadmap-outline`'s user-trigger word and aif-docs' detection-list "this milestone".
- `grep -inE 'spec note|milestone' src/skills/agent-architect/SKILL.md src/agents/editor.md` → zero (audit-clean).
- Live: a `roadmap-outline` run emits `### Phase N` (never "milestone"); a `roadmap-decompose` run emits `N.M — task`; an `aif-docs` run still writes the governing-spec genre unchanged.
