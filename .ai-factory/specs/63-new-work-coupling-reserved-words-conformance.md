# The "new work" coupling: conform the authoring skills to the reserved-words contract

Phase 10 of the Language-integration direction. Governing spec: [reserved-words](../../docs/reserved-words.md). Vocabulary-only: rename the reserved-word tokens in the authoring family's bodies to their canonical form, zero behavior change.

## Current state — per-file token inventory (grep, 2026-07-13)

**`roadmap-outline` (75 lines)** — carries the flagship:
- `description` line 3: "major **milestones**" describes the **product** → **`phases`** (outline produces `### Phase N` headers). The trigger word "milestones" in the same line's `Use when user says "roadmap", "project plan", "milestones", …` list **stays** — it matches user input, which the contract exempts.
- `spec note` (40) → **`task-spec`**; `contract line` (25) → **`contract-line`**; `Named roadmap` (53) → **`named-roadmap`**.

**`aif-docs` (271 lines)**:
- `governing spec` (line 3 description, line 15 body) → **`governing-spec`** — **token hyphenation only**. The docs-as-ТЗ *doctrine* (two doc modes) is Phase 13; do not touch aif-docs' semantics here.
- `spec note` (70) → **`task-spec`**.
- "ROADMAP **milestone**" (70, "gather … from the stated user intent, spec note, or ROADMAP milestone") → **`ROADMAP phase`** (aif-docs' governing-spec is phase-scoped).
- **Leave**: "this milestone" (26, 182) — a **mention**, a forbidden-phrase in the no-history detection list ("we changed", "was added", "this milestone"), not a unit-naming.

**`roadmap-decompose` (97 lines)** — flagship:
- `milestone`/`milestones`/`Milestones` → **`task`(s)** (decompose's product is the `N.M` task): `description` "atomic, granular milestones" (4) and "adding milestones that need to be implementation-ready" (8); body 17, 41, 75, 83; Critical-Rule heading line 92 "**Milestones** are atomic and specific" → "Tasks are atomic and specific". No milestone trigger — the `Use when` list already says "break down tasks / spec tasks / create tasks".
- `contract line` (5, 18, 29, 48, 84, 93) → **`contract-line`**; `spec note` (18, 93) → **`task-spec`**; `two-tier` / "Two-tier" (17, 29, 93) → **`two-tier`** (casing on 29); `named roadmap` / `Named roadmap` (64, 70) → **`named-roadmap`**.

**`roadmap-decompose-skeleton` (148 lines)**:
- `milestone`/`milestones` → **`task`(s)** (skeleton splits tasks): 96, 98, 102, 122, 124, 125, 130.
- `contract line` (35, 117, 122, 124) → **`contract-line`**; `spec note` (35, 117, 127) → **`task-spec`**; `two-tier` (35, 116) already ok.
- `silent-failure` (7, 37, 76, 97) / `loud-failure` (145) — already lowercase-hyphenated; verify, no change.
- **Leave**: "field" (91, "plan-review instead of in the field" — idiom, generic).

**`agent-architect` (119 lines)** — no reserved-word tokens. **Audit-clean → no change.**

**`editor.md` (88 lines)** — no reserved-word tokens. **Audit-clean → no change.**

**`command-pin-gaps` (26 lines)**:
- `contract line` (17) → **`contract-line`**; `Named roadmap` (17) → **`named-roadmap`**.
- **Leave**: "field types" (21, "enum names …, paths, field types" — generic).

## Change

Rename each token above to its canonical reserved-word form per `reserved-words.md`. Behavior byte-identical.

## Files & types

`src/skills/{roadmap-outline,aif-docs,roadmap-decompose,roadmap-decompose-skeleton,agent-architect}/SKILL.md`, `src/agents/editor.md`, `src/commands/command-pin-gaps.md`. Frontmatter `name` / `loads:` / `allowed-tools` untouched (except the reserved-word tokens *inside* a `description:` value); no `references/` touched.

## Guards

- **Output-naming vs user-trigger.** In a `description:`, "milestone" naming the skill's **product** → `phase` (outline) / `task` (decompose); "milestone" inside a `Use when user says "…"` trigger list **stays** (the contract binds output, not user input). Only `roadmap-outline` has such a trigger.
- **milestone → phase or task by producer.** `roadmap-outline` produces phases → `phase`; `roadmap-decompose` / `-skeleton` produce and split tasks → `task`.
- **`governing spec` is token-only here.** Hyphenate to `governing-spec`; the two-doc-mode doctrine is Phase 13 — aif-docs' semantics are not touched in this task.
- **Detection-list mentions left.** aif-docs' no-history forbidden-phrase list ("this milestone") is a phrase to scrub, a mention — not a roadmap-unit naming.
- **Generic `field` left.** "in the field" (skeleton) and "field types" (pin-gaps) are idiom / data-fields, not `skill-description-field`.
- **`agent-architect` + `editor` land no change** — verify zero tokens; their inclusion is a certification of the coupling's paired-loop half.
- Casing lowercase kebab even in headings; `loads:` edges + reverse-graph markers byte-identical; `` Spec: `` / `Governing spec:` tags + `.ai-factory/specs/` stay legacy; behavior byte-identical (a rename that changes an artifact's shape is a bug).

## Verification

- `grep -inE 'spec note|contract line|two tier|Two-tier|named roadmap|governing spec' src/skills/{roadmap-outline,aif-docs,roadmap-decompose,roadmap-decompose-skeleton}/SKILL.md src/commands/command-pin-gaps.md` → zero.
- `grep -inE '[^-]milestones?' src/skills/{roadmap-outline,roadmap-decompose,roadmap-decompose-skeleton,aif-docs}/SKILL.md` → only `roadmap-outline`'s user-trigger word and aif-docs' detection-list "this milestone".
- `grep -inE 'spec note|contract line|milestone|field' src/skills/agent-architect/SKILL.md src/agents/editor.md` → zero (audit-clean).
- Live: a `roadmap-outline` run emits `### Phase N` (never "milestone"); a `roadmap-decompose` run emits `N.M — task`; an `aif-docs` run still writes the governing-spec genre unchanged.
