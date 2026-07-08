# aif-docs — ТЗ is an input word, not the skill's identity

**Target:** `src/skills/aif-docs/SKILL.md` only (its `references/` contain zero `ТЗ` occurrences — verified; the verify grep still spans both as a guard).

## The one complaint

Task 10 (`.ai-factory/specs/10-aif-docs-rewrite-tz.md`) branded the skill's **identity, description, and Core Principles** with the Russian abbreviation **ТЗ**, threading a Russian term through an otherwise all-English skill — four spots: the frontmatter `description` (`SKILL.md:3`), the H1 title (`:13`), the identity paragraph (`:15`, twice: "as the project's **ТЗ**" and "exception to the ТЗ genre"), and the Core Principles opener (`:19`, twice: "is ТЗ genre" and "exempt from that genre").

The capability that ТЗ was meant to name — write a present-tense governing spec **ahead of code** *or* describe **shipped code's** behavior, in one voice — is already implemented independently of the label: the referent-conditional logic in `Step 1: Determine Current State` (`:70`), the Step 2.1 staleness carve-out (`:318`), and the Step 4 referent-conditional Technical Accuracy checks (`:369-374`). The label carries **no mechanism** — it is pure branding, in the wrong language. This is the whole task: de-thread the term from the doctrine, keep it only as a recognized input word.

## The change

A **rename / reframe pass — behavior identical**. No step logic changes; only the four identity/description/principle wordings, plus one trigger-list addition.

**1. Replace `ТЗ` → `governing spec` in all four doctrine spots.** Exact target strings (pinned so the orchestrator guesses nothing):

- **`:3` (frontmatter `description`)** — drop the "living ТЗ —" lead; keep the governing-spec gloss and extend the trigger list (see item 2):
  > `Generate and maintain project documentation as a present-tense governing spec of behavior, protocols, data flows, and connections — split by topic in the configured docs directory, with a lean README (plus its onboarding relatives) as the exception. Use when user says "create docs", "write documentation", "update docs", "generate readme", "document project", "напиши ТЗ", or "техническое задание".`

- **`:13` (H1 title)** —
  > `# Documentation Generator`

- **`:15` (identity paragraph)** —
  > `Generate, maintain, and improve project documentation as the project's **governing spec** — present-tense behavior, protocols, data flows, and connections — landing on a lean README + detailed docs-directory structure. README and its onboarding relatives (CHANGELOG.md, CONTRIBUTING.md, LICENSE) are the exception to that genre, not its center.`

- **`:19` (Core Principles opener)** —
  > `Everything written under the resolved docs directory (\`paths.docs\`, default: \`docs/\`) is governing-spec genre — behavior, protocols, data flows, connections, stated in present tense — whether the code behind it exists yet or not. Only the onboarding surface (README + its relatives) is exempt from that genre.`

**2. Re-anchor ТЗ once, as an input *trigger* only.** The Russian term stays reachable so a user asking for a "ТЗ" still routes here — but it appears exactly once, in the `description`'s "Use when user says…" list (`"напиши ТЗ"`, `"техническое задание"`, folded into item 1's string above), never in the skill's self-description, principles, or body.

## Guards

- **Do NOT touch the referent-conditional dual-write logic** — Step 1 `:70`, Step 2.1 staleness `:318`, Step 4 `:369-374`. That is the actual feature; removing the ТЗ label must not be read as removing the ahead-of-code capability. This is the opposite of the intent — the skill keeps writing a spec for the not-yet-built and describing behavior in shipped code, unchanged.
- No new mode, no lead/lag meta-commentary (re-adding it re-creates the `3d` symptom task 10 killed).
- `references/` have zero `ТЗ` — do not invent edits there; the verify grep spans them only as a safety net.
- No fork, no size work, no state-machine / `--web` / checklist changes. Reframe-only.
- Never edit `upstream/ai-factory/`; `aif-docs` stays ours / never-overwrite in CLAUDE.md.

## Verify

- `grep -rin "ТЗ" src/skills/aif-docs/SKILL.md src/skills/aif-docs/references/` → matches **only** inside the `description` trigger list (the input-word occurrences on `:3`), zero in the H1, identity paragraph, Core Principles, or anywhere in the body/references.
- Skill identity + Core Principles read in plain English ("governing spec" / behavior-description); no Russian term threaded through the doctrine.
- Referent-conditional dual-write intact: a run against a **not-yet-built** feature still produces a present-tense governing spec **without arguing** that code must exist first; a run against **shipped** code describes behavior in the same voice — both identical to task 10's behavior.
- A user request phrased "напиши ТЗ" / "техническое задание" still routes to the skill (trigger list).
