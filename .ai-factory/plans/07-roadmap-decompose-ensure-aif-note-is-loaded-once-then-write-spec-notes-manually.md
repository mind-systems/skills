# Plan: roadmap-decompose — ensure aif-note is loaded once, then write spec notes manually

## Context
Replace decompose's per-task `aif-note` invocation (introduced by commit `0bfa177`) with one rule: ensure `aif-note` was invoked at least once in the chat so its note-writing instructions are in context, then write each spec note manually with `Write`. The two-tier shape, contract line, `Spec:` tag, char budget, and Atomicity Gate stay unchanged.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Rewrite the note-writing mechanism

- [x] **Task 1: Rewrite the "Two-Tier Output (per task)" procedure**
  Files: `src/skills/roadmap-decompose/SKILL.md`
  In the `## Two-Tier Output (per task)` section (~lines 284–298):
  - Keep step 1 (Draft the full spec) as-is.
  - **Reword step 2 (Apply the Atomicity Gate)** — it currently ends "…run this whole procedure independently for each **(two note invocations + two contract lines, sequentially)**." Drop the per-task-invocation wording: change the parenthetical to "two notes + two contract lines" (remove "invocations" and "sequentially").
  - Replace current step 3 (**"Invoke the `aif-note` skill via the Skill tool…pass the task name as `$1`…supply that task's drafted spec text as the subject so aif-note does not blend it with sibling tasks…"**) and step 4 (**"Capture the note path aif-note reports back…"**) with two new steps:
    1. *Ensure `aif-note` is loaded:* if the `aif-note` skill has **not** yet been invoked in this chat, invoke it once now (via the Skill tool) so its note-writing instructions are in context; if it **has** already been invoked, do **not** invoke it again.
    2. *Write the spec note manually* with the `Write` tool, following aif-note's in-context instructions — to `.ai-factory/notes/<NN>-<slug>.md` (determine `<NN>` by scanning existing files in `.ai-factory/notes/`; `<slug>` = lowercase, hyphenated task name). Use that path verbatim in the `Spec:` tag.
  - Keep step 5 (Write the contract line) unchanged.
  - **Delete the "Sequential invocations only" paragraph** (it describes per-task aif-note calls). Replace with a short rule: `aif-note` is invoked **at most once per chat** to load its instructions, never per task; when writing several notes, scan existing note numbers first so `<NN>` never collides.
  - **Remove the "subject so aif-note does not blend siblings" cruft entirely** — aif-note has no such parameter.
  - **Do not add any note-format description of decompose's own** — the note structure comes from aif-note's in-context instructions. Add nothing beyond what existed before commit `0bfa177`.
  - Keep the "Why two tiers" and "Never write a full spec inline" paragraphs unchanged.

- [x] **Task 2: Reconcile every remaining `aif-note` / "note invocation" mention** (depends on Task 1)
  Files: `src/skills/roadmap-decompose/SKILL.md`
  Update each location below so it matches the load-once + manual-`Write` mechanism — wording only, no behavior beyond Task 1. This list is exhaustive (confirmed via grep); leave none behind:
  - **Frontmatter `description`** (~lines 3–8): change "the full spec persisted as a per-task note written by aif-note" to reflect that decompose writes the note manually following aif-note's note format.
  - **Intro sentence under `# Decompose`** (~line 16): "…a contract line in the roadmap and a full spec note written by `aif-note`." → reword like the frontmatter (note written manually following aif-note's format).
  - **Mode 1, Step 1.3 rules** (~line 105): "do **not** invoke `aif-note` yet; **note invocations** happen after the user confirms in Step 1.4" → "do not write the notes yet; notes are written after confirmation in Step 1.4."
  - **Mode 1, Step 1.3.1 Atomicity Gate** (~line 115): "both receive **note invocations** at Step 1.4 after confirmation." → "both receive notes at Step 1.4 after confirmation."
  - **Mode 1, Step 1.4** (~line 136): the finalize sentence says "invoke `aif-note` with that milestone's drafted full spec, capture the note path, and replace the placeholder…". Reword to: ensure aif-note is loaded once (per Two-Tier Output), write each confirmed milestone's spec note manually with `Write`, then replace the `` Spec: `<note pending>`. `` placeholder with the real note path.
  - **Mode 2, Step 2.4** (~line 187): "run the **Two-Tier Output** procedure — invoke `aif-note` to write the spec note" → "run the **Two-Tier Output** procedure to write the spec note".
  - **Mode 2, Step 2.4.1 Atomicity Gate** (~lines 193, 197): "before the **note invocation** — apply the gate" → "before writing the note — apply the gate"; "A split produces **two note invocations** + two contract lines." → "A split produces two notes + two contract lines."
  - **Mode 2, Step 2.5** (~lines 208–210): the note-handling rule says "instruct `aif-note` to **update** the named note file in place…" / "invoke `aif-note` normally to create a new note". Reword to manual `Write`: if the milestone already carries a `Spec:` tag, update the named note file in place with `Write` (tag unchanged); if it has no tag, write a new note (per Two-Tier Output) and add the `Spec:` tag. aif-note stays loaded once via the procedure, not re-invoked here.
  - **Contract-line rule** (~line 321): "Always end with the `Spec:` tag pointing at the aif-note-written note file" → "pointing at the spec note".
  - **Critical Rule 6** (~line 332): "a spec note written by `aif-note`" → "a spec note written manually following aif-note's note format".
  - **Do not modify the `aif-note` skill** in any way. Keep `Skill` in `allowed-tools` (still needed for the one-time aif-note load) and `Write` (used for the notes); `Glob` is already present for scanning `.ai-factory/notes/`.

## Notes for the implementer
- Spec source of truth: `.ai-factory/notes/16-task-decompose-inline-notes-aif-note-format.md`.
- The note's "revert `0bfa177` then re-add" is a *suggested* path; the file has since moved from `.claude/skills/` to `src/skills/`, so a literal `git revert` would touch unrelated paths — prefer the targeted in-place edits above, which produce the same end state.
- **aif-note's in-context template is a research-summary shape** (`Key Findings / Details / Open Questions`), not the `Current state / Target / Guards / Verify` shape of existing spec notes. This is inherited from `0bfa177` and the spec note puts note format out of scope — write the notes per aif-note's template and do **not** "improve" it (doing so would violate the "no note-format of its own" guard).
- Guards: aif-note invoked at most once per chat; no per-task invocation anywhere; decompose carries no note-format of its own; two-tier shape, contract line, `Spec:` tag, char budget, and Atomicity Gate all unchanged.
