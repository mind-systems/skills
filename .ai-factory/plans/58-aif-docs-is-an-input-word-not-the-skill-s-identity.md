# Plan: aif-docs: ТЗ is an input word, not the skill's identity

## Context
De-thread the Russian abbreviation **ТЗ** from `aif-docs`'s identity, description, and Core Principles (replacing it with `governing spec`), keeping it only as a recognized input trigger — a behavior-identical rename/reframe pass over `src/skills/aif-docs/SKILL.md` alone.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Reframe doctrine wording

- [x] **Task 1: Rewrite the frontmatter `description`**
  Files: `src/skills/aif-docs/SKILL.md`
  On `:3`, drop the "living ТЗ —" lead, keep the governing-spec gloss, and extend the trigger list with the two Russian input triggers. Set the `description` to exactly:
  `Generate and maintain project documentation as a present-tense governing spec of behavior, protocols, data flows, and connections — split by topic in the configured docs directory, with a lean README (plus its onboarding relatives) as the exception. Use when user says "create docs", "write documentation", "update docs", "generate readme", "document project", "напиши ТЗ", or "техническое задание".`
  This is the one place ТЗ survives — as an input word, folded into the "Use when user says…" list.

- [x] **Task 2: Rewrite the H1 title** (depends on Task 1)
  Files: `src/skills/aif-docs/SKILL.md`
  Replace the `:13` H1 `# Docs - ТЗ & Documentation Generator` with exactly:
  `# Documentation Generator`

- [x] **Task 3: Rewrite the identity paragraph** (depends on Task 2)
  Files: `src/skills/aif-docs/SKILL.md`
  Replace the `:15` identity paragraph (both ТЗ occurrences) with exactly:
  `Generate, maintain, and improve project documentation as the project's **governing spec** — present-tense behavior, protocols, data flows, and connections — landing on a lean README + detailed docs-directory structure. README and its onboarding relatives (CHANGELOG.md, CONTRIBUTING.md, LICENSE) are the exception to that genre, not its center.`

- [x] **Task 4: Rewrite the Core Principles opener** (depends on Task 3)
  Files: `src/skills/aif-docs/SKILL.md`
  Replace the `:19` Core Principles opening sentence (both ТЗ occurrences) with exactly:
  ``Everything written under the resolved docs directory (`paths.docs`, default: `docs/`) is governing-spec genre — behavior, protocols, data flows, connections, stated in present tense — whether the code behind it exists yet or not. Only the onboarding surface (README + its relatives) is exempt from that genre.``

### Phase 2: Verify

- [x] **Task 5: Verify the reframe** (depends on Task 4)
  Files: `src/skills/aif-docs/SKILL.md`
  Run `grep -rin "ТЗ" src/skills/aif-docs/SKILL.md src/skills/aif-docs/references/` and confirm matches appear **only** inside the `description` trigger list on `:3` — zero in the H1, identity paragraph, Core Principles, or anywhere in the body/`references/`. Confirm the identity paragraph and Core Principles read in plain English via "governing spec". Do **not** edit anything else — this task is verification only.

## Guards (apply to every task)
- Do **NOT** touch the referent-conditional dual-write logic — Step 1 (`:70`), Step 2.1 staleness (`:318`), Step 4 Technical Accuracy checks (`:369-374`). That is the real feature; the reframe must not alter the ahead-of-code / shipped-behavior capability.
- No new mode, no lead/lag meta-commentary, no fork, no size/state-machine/`--web`/checklist changes. Reframe-only.
- Do not edit `references/` — they contain zero ТЗ; the verify grep spans them only as a safety net.
- Never edit `upstream/ai-factory/`; `aif-docs` stays ours / never-overwrite.
