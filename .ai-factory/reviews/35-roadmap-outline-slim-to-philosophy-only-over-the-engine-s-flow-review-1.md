# Review: roadmap-outline: slim to philosophy-only over the engine's flow

**Scope of code changes:** `src/skills/roadmap-outline/SKILL.md` (only code file changed; the plan `.md`/`.json` and plan-review are planning artifacts, not reviewed as code).

## What I checked

- Ran `git diff HEAD` and `git status`; read the full resulting `SKILL.md` (65 lines) and cross-checked it against `roadmap-engine/SKILL.md` (the flow contract), the sibling `roadmap-decompose/SKILL.md` (the already-landed template), and the spec (note 45).

### Contract / behavior checks — all pass

- **Frontmatter unchanged and correct.** `loads: roadmap-engine` present; `Skill` in `allowed-tools` (needed to load the engine); `AskUserQuestion`, `Glob`, `Grep`, `Bash(git *)`, `Write`, `Edit`, `Read` all still present — every tool the engine's flow exercises is available. No `Questions` pseudo-tool reintroduced (note 41), no `/aif-plan` / `/aif-implement` reference reintroduced (note 36). `name` still matches the directory.
- **Delegation header** mirrors decompose's phrasing ("Ensure `roadmap-engine` is loaded once this chat … run its **Roadmap maintenance flow** with the hooks below"). Load-once discipline respected.
- **All four hooks present and correctly typed:** (a) granularity carries the strategic lens (high-level goal, 5–15, phase-names, dependencies-first) plus the two parity carry-overs the engine's create flow lacks (first-run `[x]`, gather-input question phrased *"What are the major goals for this project?"* — matches the original Mode 1.1 wording); (b) explicitly registers **no** per-entry gate and forbids improvising one; (c) target always `.ai-factory/ROADMAP.md`; (d) no extra update actions. Matches the engine's hook slots (a)–(d) exactly.
- **No engine flow/format restated inline.** Mode machinery, dialogs, check scan, and summaries are all deleted; the mechanism-tier critical rules (read-before-modify, never-remove-silently, `[x]`-stays-until-prune) are dropped here since they now live in the engine — no duplication.
- **Size** ~55 body lines, within the 40–70 target.
- **Behavior-identical in every mode**: the interactive flow is now entirely the engine's; the only intended behavioral change (optional note at the strategic tier) is exactly what note 45 mandates, so "behavior-identical" holds for the flow itself.

## Observation (non-blocking, no change required)

The optional-spec-note rule in hook (a) is a caller **override** of engine mechanism, not a formal engine hook. The engine's Create-mode flow (roadmap-engine lines 133–154) unconditionally seeds every drafted contract line with a `` Spec: `<note pending>`. `` placeholder and, at save, instructs "write each confirmed entry's spec note, then replace its placeholder"; the Add action (line 179) likewise says "produce its two-tier artifacts." Outline's hook (a) tells the agent to skip the note and strip the `Spec:` tag when the contract line alone carries the milestone. Reconciling the two requires the agent to (1) not write the note and (2) remove the `<note pending>` placeholder so no dangling tag remains — the hook says "end the entry with no `Spec:` tag," which covers this, but it relies on the agent honoring the caller override against the engine's imperative text.

This is intended: note 45 explicitly frames it as a carve-out "the engine's create flow does not itself hold," and it mirrors how `roadmap-decompose` layers two-tier discipline over the same flow. No defect — the engine's own closing line ("Philosophy-tier rules … stay with the caller") sanctions caller overrides. Flagged only so the interaction between the placeholder-seeding step and the skip decision is visible if a future engine change tightens the note step into a hard requirement.

No bugs, security issues, or correctness problems found.

REVIEW_PASS
