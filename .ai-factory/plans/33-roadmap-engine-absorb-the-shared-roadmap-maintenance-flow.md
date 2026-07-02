# Plan: roadmap-engine: absorb the shared roadmap-maintenance flow

## Context
Move the ~70% of interactive roadmap-maintenance *mechanism* (Step 0 context, create/update/check modes, dialogs, draft→confirm→notes finalization, progress review, check scan, summaries, mechanism-tier critical rules) that `roadmap-outline` and `roadmap-decompose` duplicate into `src/skills/roadmap-engine/SKILL.md` as one caller-agnostic "Roadmap maintenance flow" section with explicit hook points, leaving philosophy in the callers.

## Settings
- Testing: no
- Logging: none
- Docs: no

## Constraints (must hold for every task)
- **Single file only:** `src/skills/roadmap-engine/SKILL.md`. Do NOT touch `src/skills/roadmap-outline/SKILL.md` or `src/skills/roadmap-decompose/SKILL.md` (those are notes 44–45).
- **Caller-agnostic:** no skill names as callers anywhere (per note 38); use the word "entry", never "milestone"/"task"/"strategic"/"atomic".
- **No philosophy:** no atomicity gate, no 5–15 rule, no granularity definition, no two-tier discipline beyond linking to the existing format section. Granularity, per-entry gate, target-file routing, and extra update actions are HOOK POINTS the caller supplies — the engine only names the hooks.
- **Register:** shared instruction content the calling agent applies (same prose register as the existing "The two-tier artifact" / "Roadmap File Format" sections). NOT rigid pseudo-code.
- **Load-once discipline** restated for the new section.
- **Body ≤ 500 lines** — verify at the end.

## Tasks

### Phase 1: Author the maintenance-flow section

- [x] **Task 1: Add the "Roadmap maintenance flow" section scaffold — intro, Step 0, mode determination, hook points**
  Files: `src/skills/roadmap-engine/SKILL.md`
  Append a new top-level section `## Roadmap maintenance flow` after the existing "Roadmap File Format" section. Write:
  - A one-paragraph intro: this is the shared interactive flow for creating/updating/checking a roadmap file that the calling philosophy applies; the caller stays in control and supplies the hook points listed below; restate load-once (the flow, like the format, stays in context once loaded — never re-invoke per entry or per mode).
  - **Hook points (caller-supplied)** subsection, listed explicitly: (a) granularity — what one entry is and its rules; (b) an optional per-entry gate applied to each drafted entry before its contract line is written; (c) target-file routing — which file the flow reads/writes (`$TARGET_FILE`); (d) extra update-mode actions beyond the built-in menu. State the engine holds none of these.
  - **Step 0 — Project context:** read `.ai-factory/DESCRIPTION.md` and `.ai-factory/ARCHITECTURE.md` if present (tech stack, architecture/conventions, module boundaries).
  - **Mode determination:** argument `check` → check mode (requires `$TARGET_FILE` to exist); else `$TARGET_FILE` absent → create mode, present → update mode. State the target-file choice itself is the caller's routing hook — the engine never infers it.
  Keep "entry" language throughout. Adapt the wording from the callers' Step 0 / Step 1 but strip all granularity/skill-name specifics.

- [x] **Task 2: Write Create mode and Update mode (caller-agnostic)** (depends on Task 1)
  Files: `src/skills/roadmap-engine/SKILL.md`
  Under the new section add two subsections, generalized from the callers' Mode 1 / Mode 2:
  - **Create mode:** gather input (argument as primary input; else the interactive what/priorities dialogs via `AskUserQuestion` — keep the two-question dialog shape); explore codebase (`Glob`/`Grep` + `git log --oneline -20`); draft the roadmap **in memory** per the two-tier artifact format with `` Spec: `<note pending>`. `` placeholders on contract lines; before writing each drafted entry's contract line, apply the caller's per-entry gate hook if one is supplied; confirm with the user (save / add / modify / rewrite menu); only **after** "save" confirmation write the spec notes, replace each placeholder with the real `` Spec: `.ai-factory/notes/<NN>-<slug>.md`. `` tag, then write `$TARGET_FILE`. Entries removed or rewritten during confirmation receive no note — only the confirmed set gets notes.
  - **Update mode:** read current state (`$TARGET_FILE`, `DESCRIPTION.md`, brief codebase check); with an argument apply the requested changes directly; without one present the action menu — review progress / add / reprioritize / save — noting the caller may register extra actions (hook d). Describe each built-in action generically: review-progress = scan codebase for evidence, propose `[x]` marks, apply on confirmation; add = explore per entry, produce two-tier artifacts (applying the per-entry gate hook), insert in logical order; reprioritize = reorder in `$TARGET_FILE`. Finish with the update summary block (Total entries / Completed X/N / Next up). Use `$TARGET_FILE` and "entry" — no "milestone"/"task".

- [x] **Task 3: Write Check mode + mechanism-tier critical rules** (depends on Task 2)
  Files: `src/skills/roadmap-engine/SKILL.md`
  - **Check mode:** non-interactive scan (generalized from callers' Mode 3). Requires `$TARGET_FILE`; if absent, tell the user to run create mode first. For each open `- [ ]` entry: determine what evidence would prove it done, search with `Glob`/`Grep` + `git log --oneline --all -30`, score done / partial / not-started, report the three groups, mark confirmed-done entries `[x]` on confirmation, leave partial/not-started unchanged, print the completed X/N + next-up summary.
  - **Critical rules (mechanism):** add a short rules list holding only the mechanism-tier rules moved here: `$TARGET_FILE` is the source of truth — read before modifying; never remove entries silently — confirm before removing; completed entries stay `[x]` in the list until `roadmap-prune`. Explicitly note philosophy-tier rules (granularity, per-entry gate, two-tier discipline) stay with the caller. Keep "entry" language and no skill-caller names (`roadmap-prune` is the downstream pruner, allowed as it is not a caller — reference matches the existing callers' rule 4 wording).

### Phase 2: Frontmatter + verification

- [x] **Task 4: Update frontmatter description and verify constraints** (depends on Task 3)
  Files: `src/skills/roadmap-engine/SKILL.md`
  - Extend the frontmatter `description` to mention it now also holds the shared caller-agnostic maintenance flow (create/update/check), keeping it ≤1024 chars and still caller-agnostic and load-once. Do not change `name`, `loads`, or `allowed-tools` values by requirement — but note the flow text references `Write`, `Edit`, `Glob`, `Grep`, `Bash(git *)`, `AskUserQuestion`, `Skill`; leave `allowed-tools: Read` as-is since the engine describes mechanism the caller executes (the callers already declare those tools) — do NOT widen tools unless a later task explicitly requires it.
  - Verify: run `wc -l src/skills/roadmap-engine/SKILL.md` (must be ≤ 500); grep the new section for banned words (`milestone`, `atomic`, `strategic`, `roadmap-outline`, `roadmap-decompose`, `roadmap-decompose-skeleton`) and confirm none appear as caller/philosophy references; confirm the two-tier format and Roadmap File Format sections are unchanged except for links pointing the flow at them.

## Commit Plan
- **Commit 1** (after task 4): "Absorb shared roadmap-maintenance flow into roadmap-engine"
