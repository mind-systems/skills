---
name: roadmap-outline-deep
description: >-
  Second pass over phases `roadmap-outline` has already drafted: writes every
  drafted phase a phase note through `note`, stating what diverges now
  between the docs and the code, then compresses that phase's preamble to a
  short summary closed by an inline `Phase note:` pointer to the note — a
  phase already carrying a pointer is rewritten in place, never given a
  second note. Every drafted phase qualifies — there is no per-phase gate.
  Use when deepening a drafted phase before decomposition. Trigger: "deepen
  phase", "phase note".
argument-hint: "[phase or slug]"
disable-model-invocation: true
allowed-tools: Read Write Edit Glob Grep AskUserQuestion Skill
loads: roadmap-engine note
---

# Roadmap Outline Deep — Phase Note and Preamble Compression

A **second** pass over phases `roadmap-outline` has already drafted — one tier up from
`roadmap-decompose-skeleton`: it deepens the phase tier, it does not draft phases.
**Every** drafted phase qualifies — there is no per-phase gate, because a phase exists
precisely where the docs and the code diverge.

## Load-once / dependencies

This skill owns no reusable body of its own:

- `roadmap-engine` — supplies the roadmap format and the named-roadmap resolution
  order.
- `note` — supplies the note mechanism (mining, distillation, per-directory
  numbering, placement).

Each is loaded **once per chat** via the `Skill` tool, never re-invoked per phase.
This skill does **not** call `roadmap-outline` at runtime — the phases already exist.
It never reads or modifies the orchestrator.

## Targeting

Optional arg — a phase or slug (matching `argument-hint`). Default: infer the target
phase set from conversation context. Resolve the roadmap in play per
`roadmap-engine`'s named-roadmap resolution order (explicit argument → "my roadmap" →
default `.ai-factory/ROADMAP.md`).

## Workflow

### Step 0: Project context

**Read `.ai-factory/ARCHITECTURE.md`** if it exists. **Read the target roadmap** and
collect its `### Phase N` headers with their preambles. Then, for each target phase,
read the docs its header and preamble link — a `Governing spec:` line is one such
link and nothing more — and the code the phase is about, the modules, skills or files
it names, down to the leaf. What is not yet as those docs say is the phase; it is
visible only there, never from a doc's own prose about itself.

### Step 1: Write the phase note

The note is written through `note` with all three of its caller hooks supplied:

- **Destination directory** — the roadmap's own spec directory, the same
  destination and the same per-directory numbering task specs already use:
  `.ai-factory/specs/<slug>/` for a named roadmap, flat `.ai-factory/specs/` for the
  default roadmap. This is `roadmap-engine`'s "Named roadmaps" § "Spec destination"
  routed through `note`'s destination hook — do not restate its mechanics here, and
  never introduce a new directory.
- **Template** — a short statement, in words, of what is not yet as the docs say —
  this and this — with links to those docs; that is the essence of the phase and what
  decomposition cuts tasks from. Never a copy of the doc. Where no doc says how it
  must be, the note says so in one line; the pass never writes under `docs/` and
  never invents a link.
- **Verbosity directive** — short: a few sentences more than the preamble, grounded
  in the docs and code read at Step 0, a `file:line` where a claim needs one, never a
  transcript of the conversation.

The note is written **per phase**. `note` returns the exact path it wrote; Step 2
uses that path verbatim in the `Phase note:` pointer.

**Re-run rule — one note file per phase, forever.** `note` only ever mints a *new*
numbered file; it exposes no update-in-place path. Since this pass has no per-phase
gate and a roadmap routinely grows new phases after a deepening pass, invoking `note`
unconditionally on every run would leave a superseded note behind on every re-run —
orphaned the moment Step 2 repoints the preamble, and invisible to `roadmap-prune`,
which only ever captures the path the current pointer names. So:

- **Where a phase preamble already carries a `Phase note:` pointer, rewrite the note
  in place at the path that pointer names** — with `Write`/`Edit` directly, never
  through `note` — and leave the pointer byte-identical. The in-place rewrite
  produces the same note the template and verbosity directive above describe — same
  content contract — only written through `Write`/`Edit` instead of through `note`.
- **Invoke `note` only for a phase that has no pointer yet.**
- Never a second note file for one phase, and never a second `Phase note:` token in
  one preamble.

### Step 2: Compress the preamble and attach the pointer

This skill holds the pointer format itself, being its only caller — do not push it
into `roadmap-engine` or `roadmap-outline`.

- **Budget** — rewrite the phase preamble down to **~200–500 characters**, keeping
  the phase's gate and its `Phase note:` pointer. The note states what is not yet as
  the docs say, per Step 1's template — it is a short distillation, not a home for
  whatever the preamble sheds. Prose that is neither the gate nor that distillation
  is dropped deliberately, not relocated.
- **Pointer** — literal form `Phase note: [<title>](<path>)`, byte-exact token
  `Phase note:` (capital P, lowercase n), **closing the preamble line** — appended to
  the end of the preamble prose, never standing as a separate paragraph, so the
  preamble reads in one line the way a task contract line does. For example:
  `Phase note: [What diverges now](.ai-factory/specs/12-phase-note.md)`.
- **Path form** — `<path>` is repo-root-relative and begins with `.ai-factory/`, in
  the exact form the `Spec:` tag uses (e.g.
  `.ai-factory/specs/<slug>/<NN>-<slug>.md`), so `roadmap-prune`'s sweep joins it onto
  the target repo root unchanged. It is a pointer for agents, not an
  editor-resolvable link.
- **Header order** — where a phase header already carries `Governing spec:`, that
  line stays first and untouched; the `Phase note:` pointer sits on the preamble
  below it.

This form is already legal under `roadmap-outline`'s own rules — plain markdown links
are permitted in intro/preamble prose, and its three prohibitions (checkbox bullet,
contract line, formal `Spec:` tag) do not reach an inline link. `roadmap-outline`
itself is never edited by this skill.

## Critical Rules / What NOT to do

1. Do not call `roadmap-outline` at runtime.
2. Do not draft, renumber, reorder, or delete phases — this pass only deepens
   existing ones.
3. Do not copy `roadmap-engine`'s or `note`'s machinery into this skill — load them.
4. Do not write under `docs/` and never invent a `docs/` link — where no doc says
   how it must be, the note says so in one line.
5. Do not emit a checkbox, a contract line, or a `Spec:` tag at the phase tier.
6. Do not mint a second note file for a phase that already carries a `Phase note:`
   pointer — rewrite in place at the path the existing pointer names and leave the
   pointer byte-identical. Never a second `Phase note:` token in one preamble.
7. Do not touch task lines — that is `roadmap-decompose`'s tier.
8. This skill plans only; the orchestrator implements in a separate run.
