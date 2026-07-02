# roadmap-engine: absorb the shared roadmap-maintenance flow (modes, check, confirmation)

**Date:** 2026-07-02
**Source:** conversation context (skill-pipeline review)

## Key Findings

- `roadmap-outline` and `roadmap-decompose` are ~70% identical text: Step 0 context loading (DESCRIPTION/ARCHITECTURE), mode determination (create/update/check), gather-input dialogs, codebase exploration, draft-in-memory → confirm → notes-after-confirmation finalization, update-mode actions (review progress / add / reprioritize / save summary), and the whole check-mode scan. This is interactive roadmap-file maintenance **mechanism**, duplicated in two philosophy skills.
- Target model (user's): all roadmap philosophies (`roadmap-outline`, `roadmap-decompose`, `roadmap-decompose-skeleton`) call one engine, loaded once per session; once loaded, the format and flow are in context and later philosophies reuse them without re-invoking. The philosophies stay small, carrying only their lens — identical behavior across all of them, only granularity differs.
- This task extends the engine only. The callers keep their duplicated text until their own slim-down tasks land (notes 44, 45) — nothing breaks in the interim.

## Details

Add a new major section to `src/skills/roadmap-engine/SKILL.md` — "Roadmap maintenance flow" — holding the shared mechanism, caller-agnostic:

- **Step 0 — project context:** read `.ai-factory/DESCRIPTION.md` and `.ai-factory/ARCHITECTURE.md` if present.
- **Mode determination:** argument `check` → check mode (requires the target file); target file absent → create mode; present → update mode. The *target-file choice itself* is the caller's policy — the engine never infers it.
- **Create mode:** gather input (use argument as primary input; else the interactive what/priorities dialogs via `AskUserQuestion`), explore codebase (Glob/Grep/git log), draft the roadmap **in memory** with `` Spec: `<note pending>`. `` placeholders, confirm with the user (save / add / modify / rewrite), and only after confirmation write the spec notes, replace placeholders with real `Spec:` tags, and write the target file. Milestones removed during confirmation get no note.
- **Update mode:** read current state; with an argument apply changes directly; without one offer the action menu (review progress / add / reprioritize / save; the caller may add its own actions). Review-progress = scan codebase for evidence, propose `[x]` marks, apply on confirmation. Add = explore per item, produce two-tier artifacts, insert in logical order. Finish with the update summary block.
- **Check mode:** non-interactive scan — per open `[ ]` item determine what evidence would prove it done, search with Glob/Grep + `git log --oneline --all -30`, score done/partial/not-started, report, mark confirmed items.
- **Hook points (explicitly listed):** the calling philosophy supplies (a) the granularity — what one entry is and its rules; (b) any gate applied to each drafted entry before its contract line is written (e.g. an atomicity gate); (c) target-file routing; (d) extra update-mode actions. The engine holds no such policy.

Move the shared **critical rules** that are mechanism into the engine too (target file is source of truth — read before modify; never remove entries silently; completed entries stay `[x]` until `roadmap-prune`), leaving philosophy rules (atomicity, granularity, two-tier discipline references) in the callers.

### Constraints

- The engine stays caller-agnostic: no skill names as callers (per note 38), no granularity words like "strategic" or "atomic" in the flow text — "entry" only.
- Load-once discipline unchanged and restated for the new section.
- No changes to the two-tier artifact format or roadmap file format sections beyond linking the flow to them.
- Body ≤ 500 lines. `roadmap-outline` / `roadmap-decompose` files are NOT touched by this task.

## What NOT to do

- Do not put any decomposition or outlining philosophy (atomicity gate, 5–15 milestones rule, test-keyword routing) into the engine — those stay with the callers.
- Do not slim the caller skills here — that is notes 44 and 45, separately revertable.
- Do not turn the flow into rigid pseudo-code — it is shared instruction content the calling agent applies, same register as the existing format section.
