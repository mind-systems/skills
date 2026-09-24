# Plan: 57.3 — the skeleton takes the bead

## Context
`src/skills/roadmap-decompose-skeleton/SKILL.md`'s Lens 1 cuts a skeleton seam because the surface becomes testable; this task makes it cut on the polymorphism unit's own event — a kind gaining a second member — and declares the new dependency in the file's `loads:` field. One file, two pinned edits plus one consequence repair. The unit it loads, `src/skills/polymorphism-philosophy/SKILL.md`, exists on disk with an `active/skills/` symlink (task 57.2 landed), so the sequencing precondition the contract line names is satisfied.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## What the spec pins, and the one thing it does not

Both edits are given verbatim in `.ai-factory/specs/trickster77777/158-the-skeleton-takes-the-bead.md` § "The change" — the replacement Lens 1 block and the replacement `loads:` line. Copy them; they are the deliverable, not a sketch to re-derive. The spec also enumerates what stays verbatim: Lens 2, Lens 3, Steps 2–4, and the Critical Rules list including restraint items 5 and 6.

The spec's one claim that ground truth contradicts, and how this plan resolves it:

**The "Load-once / dependencies" section carries a count that this task's own change falsifies.** The spec says that section "stays accurate and gains no restatement of the third dependency there." The second half is a ruling and this plan honours it — no third bullet, no prose naming `polymorphism-philosophy` there; the `loads:` field is the one place a new engine dependency is declared, per CLAUDE.md § "Dependencies and the skill graph". The first half is not accurate after the change: the section's lead sentence reads "Everything reusable is delegated to **two** shared skills, each loaded **once per chat** via the `Skill` tool", and the new Lens 1 loads a third skill once per chat by the same mechanism. The word `two` is a census of a set this very diff grows — precisely the number `docs/counts-go-stale.md` rules out, and the subject of the phase directly above this one in the same roadmap (56.1, 56.2).

So the repair is to delete the count, not to restate the dependency: the sentence stops counting, the bullet list stays at two entries, and the spec's ruling stands untouched. The fix sits inside this task's own file, in a sentence made false by this task's own edit — in-boundary by the review engine's own test, so it is a task here rather than an observation left for someone else.

Not touched, deliberately: the `description:` frontmatter field ("shares a type surface and needs splitting before implementation"). The spec's change list is exhaustive and does not name it, and the phrase is not falsified by the new Lens 1 — a kind gaining a second member *is* a statement about a type surface. Rewriting always-loaded description text is its own decision and is not this task's.

## Tasks

### The lens

- [x] **Replace Lens 1's body and restraint clause**
  Files: `src/skills/roadmap-decompose-skeleton/SKILL.md`
  In § "Step 1: Apply the three lenses", replace the whole `**Lens 1 — Skeleton (primary).**` paragraph *and* its single `- Restraint:` bullet with the two-part block pinned in the task spec § "The change": the lens paragraph ordering `polymorphism-philosophy` loaded once via the `Skill` tool and its question applied to the target task(s), extracting a **skeleton task** where it fires (interfaces, types, abstract classes only — **no implementation bodies**; the scaffold the TDD lens writes tests against), plus the restraint bullet ending "The question is the gate; it fires only on the event, never on style."
  Hold to these, all of them confirmed against the file and its neighbours:
  - **Do not restate the question's wording.** No "to add a third kind, how many places must change", no trigger/exemption text. The loaded skill stays in control of its own content — the same discipline Critical Rule 2 states and Lens 2 already follows ("apply its silent-failure discriminator to that surface", never a copy of the discriminator). This is also why the new Lens 1 leans on nothing about `polymorphism-philosophy` beyond its name.
  - **Match Lens 2's load phrasing.** Lens 2 reads "Load `test-philosophy` once via the `Skill` tool, then apply its silent-failure discriminator to that surface"; Lens 1's new first sentence is the same construction against `polymorphism-philosophy`. Keep the backticked skill name and the `Skill` tool capitalised as Lens 2 has it.
  - **Bold markers survive the replacement** — `**Lens 1 — Skeleton (primary).**`, `**skeleton task**`, `**no implementation bodies**`. They are the file's own naming granularity; other sections address the lens by that name.
  - **Re-wrap to the destination, do not paste the spec's line breaks.** The spec renders the replacement as a blockquote with the paragraph and the restraint bullet each on one long line; the target file is hard-wrapped throughout (today's Lens 1 block sits at 81–90 columns, its restraint bullet continues at a two-space indent, and the file's longest line anywhere is 96). Insert the block wrapped to that convention — ≤ ~90 columns, two-space continuation on the bullet. **Verbatim here means the words and their order, not the newlines:** the text is byte-identical to the spec's pinned wording, the whitespace and line breaks conform to the file. One consequence to expect: a phrase of the new text may then span a line break, so any later grep against this block matches per line, never per sentence.
  - Nothing above (§ "Targeting", § "Step 0") and nothing below (Lens 2's first word onward) moves by a byte.

- [x] **Declare the dependency in `loads:`** (depends on Replace Lens 1's body and restraint clause)
  Files: `src/skills/roadmap-decompose-skeleton/SKILL.md`
  In the frontmatter, `loads: roadmap-engine test-philosophy` becomes `loads: roadmap-engine test-philosophy polymorphism-philosophy` — space-separated, appended last, existing two names and their order unchanged. `loads:` is a machine-resolved frontmatter field: the names are identifiers and must match the skill directory names byte-for-byte. No other frontmatter field changes — `name`, `description`, `argument-hint`, `disable-model-invocation`, and `allowed-tools` (which already includes `Skill`, so the new load needs no tool added) all stay as they are.
  The engine side of the coupling is already in place: `src/skills/polymorphism-philosophy/SKILL.md` carries its load-once engine sentence and the reverse-graph grep line, and names `roadmap-decompose-skeleton` as its caller. After this edit that reverse-graph grep resolves for the first time — nothing further is owed on the engine's side.

### The consequence inside the same file

- [x] **Drop the stale count from the "Load-once / dependencies" lead sentence** (depends on Declare the dependency in `loads:`)
  Files: `src/skills/roadmap-decompose-skeleton/SKILL.md`
  In § "Load-once / dependencies", the sentence "Everything reusable is delegated to two shared skills, each loaded **once per chat** via the `Skill` tool and never re-invoked per task:" loses the word `two` — "Everything reusable is delegated to shared skills, each loaded **once per chat** via the `Skill` tool and never re-invoked per task:". That is the whole edit.
  Explicitly out of scope, per the task spec's ruling: do **not** add a `polymorphism-philosophy` bullet to that list, do not mention it anywhere in that section, and do not reword the two existing bullets (`roadmap-engine`, `test-philosophy`) or the paragraph that follows them ("This skill does **not** call `roadmap-decompose` at runtime…"). The rationale is in § "What the spec pins, and the one thing it does not" above and stays there — this edit is ordered by the plan, so applying it is following the plan, not departing from it. No `DEVIATION` annotation is owed: that annotation records the file on disk contradicting the plan, and here there is no such contradiction to record.

### Verification

- [x] **Re-run the spec's sweep and confirm the invariant** (depends on Drop the stale count from the "Load-once / dependencies" lead sentence)
  Files: none — read-only check
  Run the task spec's own re-runnable sweep from the repo root:
  ```
  grep -rln "genuinely makes the surface testable\|loads: roadmap-engine test-philosophy$" .
  ```
  **The one path that must disappear is `src/skills/roadmap-decompose-skeleton/SKILL.md`** — the new Lens 1 contains neither phrase, and the `loads:` line no longer ends in `test-philosophy`. That is the whole invariant.

  Everything else the sweep returns is a hit by design, and the count is not the test. Run as written from the repo root it returns four paths today: the target, this task's spec (`158-…md`), the phase note (`151-…md`), and **this plan file**, which matches on the grep command quoted in this very block rather than on either passage. After the edit, three remain. Judge each returned path by the spec's own **rule** — *does this file quote one of the two passages as ground truth for its own standing claim about the present?* — and not by whether it was on a list:
  - The spec and the phase note quote the pre-task wording as the state they describe. A spec and a phase note describe a moment, not the present. Correct, leave them.
  - This plan, and any plan-review or other run artifact of this task that happens to carry the pattern, match self-referentially — they contain the sweep command or discuss the passage, they do not assert it. Equally not findings.
  - A path that is none of these **and** quotes a passage as a live claim: stop and report it, do not edit it. The spec's blast radius states no such file exists in the repository.

  Do not "fix" the grep pattern and do not edit any matching artifact to make the output tidier.
