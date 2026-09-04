# The phase note gets its readers

## Current state (grounded, read fresh)

`src/skills/roadmap-decompose/SKILL.md` hook (a) Granularity, `:26`, states what an entry is and how it is numbered. It names no phase preamble and no read of one: decomposition starts from the phase header and the conversation, never from what the phase itself records.

`src/skills/task-rescue/SKILL.md:61-63` reads the phase header for a `Governing spec:` reference — "If present, read every named document in full before proceeding to Step 2 — this is unconditional, not suspicion-based. If the task is under no phase, or no `Governing spec:` is named, proceed as today." `:541` forbids a semantic diagnosis without that read, "never suspicion-gated". Both know one pointer only.

Task 28.1 puts a second pointer on the phase header: `Phase note:`, whose file states exactly what diverges now. Nothing reads it. The governing spec says how the phase must become; the note says what it is now — and the note is the closer of the two to a root cause.

## The change

1. `src/skills/roadmap-decompose/SKILL.md`, hook (a) Granularity: before decomposing a phase, read its preamble. Where it names `Governing spec:` documents or a `Phase note:`, read those files in full before writing the first task — unconditional, never suspicion-gated. The read runs once per phase, at the moment the phase's first entry is drafted — in create mode, in the add action, and in the "Decompose existing" action (hook (d), `:73`) for the target task's phase — never once per entry: hook (a) is the shape the engine applies to every entry (`roadmap-engine` `:189`, `:242`), so the instruction states its own unit. This is the first governing-spec read decompose ever performs; it gains both pointers, not the note alone.

2. `src/skills/task-rescue/SKILL.md`: the read at `:61-63` and the rule at `:541` extend from `Governing spec:` alone to `Governing spec:` and `Phase note:`, in the same unconditional shape. The existing exit stays word-for-word in substance: under no phase, or with neither named, proceed as today. Three more sentences in that file rest on the Step 1 read being the governing spec alone and widen in the same edit: the step title at `:58` ("Read the phase's governing spec") names both pointers; the Step 3 judgment at `:143` ("judge the recurring findings against it") lets the note's statement of what diverges now stand beside the governing spec's statement of how it must become as a baseline a finding is judged against; the no-wholesale-copy rule at `:356` covers both files.

## Files & types

- edit: `src/skills/roadmap-decompose/SKILL.md` — hook (a) Granularity
- edit: `src/skills/task-rescue/SKILL.md` — the Step 1 read and its title, the Step 3 judgment, the Step 5 copy rule, and the rule under `## What NOT to do`

## Guards

- Runs after 28.1, which defines the `Phase note:` token. Before it, there is no token to read.
- `Phase note:` is byte-exact wherever it appears — capital P, lowercase n, colon.
- Modify nothing else: not `roadmap-outline-deep`, `note`, `roadmap-engine`, `roadmap-outline` or `roadmap-prune`.
- No new `loads:` edge. Reading a file named on a phase header is a read, not a skill invocation.
- A pointer whose file is absent is reported as a finding, never skipped silently — in both skills, for both pointers.
- The two pointers are not interchangeable and the wording keeps them apart: the governing spec states how the phase must become, the phase note what diverges now.

## Verification

Counts against a whitespace-normalized read of the named file — never a line-oriented `grep`.

- `Phase note:` in `src/skills/roadmap-decompose/SKILL.md` → at least 1, byte-exact
- `src/skills/roadmap-decompose/SKILL.md` states the read's unit — once per phase, at its first drafted entry — and names the "Decompose existing" action → checked by reading
- `Phase note:` in `src/skills/task-rescue/SKILL.md` → at least 2, byte-exact; and by reading, not by count: the Step 1 title names both pointers, the Step 3 judgment at `:143` and the copy rule at `:356` name the phase note, and the absent-file branch is stated
- `Governing spec:` stays at both sites in `task-rescue/SKILL.md`, the read and the rule → at least 1 at each; the second pointer joins it, never replaces it
- `git diff HEAD --stat -- src/ active/ docs/ CLAUDE.md` lists exactly `src/skills/roadmap-decompose/SKILL.md` and `src/skills/task-rescue/SKILL.md` and nothing else
- No count above is trusted as evidence until it was taken by the normalized method named at the head of this section
