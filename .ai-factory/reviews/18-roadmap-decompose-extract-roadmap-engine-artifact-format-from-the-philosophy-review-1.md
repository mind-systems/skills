# Code Review: roadmap-decompose — extract `roadmap-engine` (artifact format)

**Plan:** `18-roadmap-decompose-extract-roadmap-engine-artifact-format-from-the-philosophy.md`
**Changed files reviewed (in full):** `src/skills/roadmap-engine/SKILL.md`, `src/skills/roadmap-decompose/SKILL.md`, plus the `.ai-factory/ROADMAP.md` diff.
**Nature of change:** skill-instruction (Markdown) content move — no executable code, no runtime, no migrations, no types. "Correctness" here means: content faithfully moved, no dangling cross-references, philosophy preserved, frontmatter valid.

## Verdict

The implementation executes the plan faithfully. Both skill files are correct and complete against Task 4's verification checklist. No blocking findings. One non-blocking observation about an orchestrator artifact in `ROADMAP.md` (below).

---

## Verification against the plan (Task 4 checklist)

- **(a) Engine body = decompose's removed format content, reflowed to prose.** ✔ The "Roadmap File Format" block + contract-line rules (engine lines 42–63) are **byte-identical** to decompose's removed lines 302–323 (confirmed from the diff). The two-tier note explanation (engine lines 22–40) is the same content reflowed from numbered steps into prose — note-format via `aif-note` (loaded once, never per task), `<NN>` scanned so it never collides, `<slug>` lowercase-hyphenated, the exact `` Spec: `.ai-factory/notes/<NN>-<slug>.md`. `` tag, "Why two tiers", and "Never write a full spec inline". No content dropped.
- **(b) decompose no longer holds the format block, contract-line rules, or the numbered Two-Tier Output procedure; no orphaned separators.** ✔ Both sections removed; a single `---` remains at line 282 separating Mode 3 from Critical Rules — the collapse was done cleanly, no doubled/dangling rules.
- **(c) decompose philosophy unchanged apart from the repointed references.** ✔ Step 0, Step 1 target/mode logic, Atomicity Gate blocks 1.3.1 and 2.4.1 (decision wording verbatim), all mode descriptions, exploration steps, and every `AskUserQuestion` block are intact.
- **(d) Engine has no Input Contract, Per-Task Render Procedure, modes, Atomicity Gate, or "does NOT own" list.** ✔ All removed. The engine is now purely a format explanation.
- **(e) Neither description asserts the false 3-caller set.** ✔ Engine description: "Currently loaded by roadmap-decompose; retained as forward-looking shared-format infra for the rest of the roadmap family." decompose intro/description/Rule 6 now say "rendered per `roadmap-engine`'s format."

### Dangling-reference sweep

- Grepped `src/` for `Two-Tier Output` — **zero** occurrences remain anywhere; all five decompose references (lines 136 / 187 / 198 / 208 / 210) were repointed to the engine's format, including the one embedded in the Step 2.4.1 gate block (line 198), whose gate logic stayed verbatim. ✔
- Grepped `src/` for `roadmap-engine` / `Roadmap File Format` — the only matches are the intended decompose→engine references and the engine's own heading. No external skill referenced the removed engine anchors (`Input Contract`, `Per-Task Render Procedure`, "does NOT own"). ✔
- Frontmatter valid: `name` matches directory for both; decompose's `argument-hint` stays quoted; engine `allowed-tools`/`user-invocable`/`disable-model-invocation` unchanged as planned. Both bodies well under the 500-line limit. ✔

---

## Non-blocking observation

### `.ai-factory/ROADMAP.md` — a second `---STOP---` fence now exists (orchestrator bookkeeping, not implementation code)

`---STOP---` is a long-standing orchestrator fence (present at a shifting line in every recent commit). This diff **added a new fence at line 47**, immediately after the milestone-18 entry, while the pre-existing fence (HEAD line 53) shifted down and remains at **line 55** (after the `aif-roadmap` milestone). The file therefore now carries **two** `---STOP---` fences (lines 47 and 55).

This is pipeline state, not part of milestone 18's authored scope (the plan only edits the two `SKILL.md` files), so it is not a defect in the implementation. But if the convention is a single fence marking the current batch boundary, the stale fence at line 55 is redundant and should be reconciled. **Recommend the human/orchestrator confirm the double fence is intended before committing** — it does not affect the skill changes either way. (`---STOP---` is also not a valid Markdown horizontal rule, but that is a pre-existing property of the convention, not introduced here.)

---

## Nitpicks (no action required)

- Engine line 20: "Load this skill once per chat, at each seam where a caller needs the format" reads slightly oddly ("once" + "at each seam"), but the intent — load once, consult at each seam — is clear and carried from the original wording.
- Engine's two-tier text describes note *creation* (`<NN>` scanned so it never collides); decompose Mode 2.5's in-place-update branch supplies its own note-handling override on top of the format. This split (format in engine, in-place policy in decompose) is exactly the reframe the plan intended and was accepted in plan-review round 2 — noted only for traceability.

REVIEW_PASS
