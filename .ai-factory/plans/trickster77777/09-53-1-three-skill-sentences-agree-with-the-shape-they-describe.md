# Plan: 53.1 — three skill sentences agree with the shape they describe

## Context
Three sentences in three files still describe a shape the family has moved away from. This task replaces each one with the after-text pinned verbatim in the task spec `.ai-factory/specs/trickster77777/0205-three-skill-sentences-agree-with-the-shape-they-describe.md` § "What must be true after". The phase note `.ai-factory/specs/trickster77777/147-sentences-that-outlived-their-shape.md` says no document governs these sentences, so no doc is edited. There is no `.ai-factory/RULES.md`.

Blast radius: I re-ran the spec's three sweeps while planning, and they match the spec's finding.
- `grep -rn "how to verify" src/ docs/ CLAUDE.md` finds two places. One is the hook's line in `src/skills/roadmap-decompose/SKILL.md`, which is a target. The other is `docs/what-a-task-carries.md` ("a spec that also says how to verify hands the implementer a job"). That is prose about the retired shape and already agrees with the change, so it stays.
- `grep -rn -i "enumerat" src/ docs/ CLAUDE.md` finds the two target sentences in `src/commands/command-pin-gaps.md`. In the same file it also finds § "Blast-radius holes" ("never the sweep's own enumeration of what it found"), which agrees with the new wording and stays. The other hits are unrelated: `roadmap-prune`, `aif-docs/references/REVIEW-CHECKLISTS.md`, `ui-ux-pro-max` Python `enumerate`, the global `CLAUDE.md`, and the repo `CLAUDE.md` index.
- `grep -rn "Decompose existing\|Load-once" src/ docs/ CLAUDE.md` finds the following, all of which stay:
  - The hook heading in `roadmap-decompose`.
  - A citation of the hook by name in `roadmap-decompose`. It does not quote the hook's parenthesis.
  - The "Load-once / dependencies" sections of `roadmap-outline-deep` and `roadmap-decompose-skeleton`. Each describes its own loads.
  - The word "Load-once" in `roadmap-engine`'s description.
- In the skeleton section, the count word "only the three lenses below" and the gloss in its parenthesis are not edited.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Rewrite the three sentences verbatim from the spec

- [x] **Drop "how to verify" from the "Decompose existing" hook**
  Files: `src/skills/roadmap-decompose/SKILL.md`
  The sentence is in § "(d) Extra update action — "Decompose existing"". It now reads, over two lines:
  ```
  Register an added update-menu action: expand a vague task into a full spec (what
  exists today, the exact change, files/types/methods to touch, guards, how to verify).
  ```
  Replace it with the following. The first line does not change. Only the second line gets shorter, and "guards" stays.
  ```
  Register an added update-menu action: expand a vague task into a full spec (what
  exists today, the exact change, files/types/methods to touch, guards).
  ```
  Leave the rest of the hook alone, including the "Task-spec-handling rule" bullets.

- [x] **Say "recording" / "records" in the two `command-pin-gaps` sentences**
  Files: `src/commands/command-pin-gaps.md`
  This file does not hard-wrap, so each paragraph is one physical line. Make two in-line word swaps and change nothing else:
  1. In the paragraph that opens with **The shape it repairs toward:**, change `and a blast-radius hole by enumerating *what breaks on contact*.` to:
     ```
     and a blast-radius hole by recording *what breaks on contact*.
     ```
  2. In the paragraph that opens with **What the pass never writes:**, change `it pins values and enumerates breakage, and it never authors a verification check` to:
     ```
     it pins values and records breakage, and it never authors a verification check
     ```
  Do not touch § "Blast-radius holes". Its "never the sweep's own enumeration of what it found" stays.

- [x] **Add `polymorphism-philosophy` to the skeleton's load list**
  Files: `src/skills/roadmap-decompose-skeleton/SKILL.md`
  In § "Load-once / dependencies", add a third bullet right after the `test-philosophy` bullet, and before the blank line and the paragraph "This skill does **not** call `roadmap-decompose` at runtime…". The spec gives the bullet's text as one sentence. Wrap it the way the existing bullets are wrapped, with a two-space continuation indent. The two lines below are 85 and 84 characters, which is within the file's column.
  ```
  - `polymorphism-philosophy` — the question Lens 1 puts to each task: to add a third
    kind, how many places must change, fired only when a kind gains its second member.
  ```
  Do not edit the section's opening paragraph ("only the three lenses below (targeting, skeleton, TDD, concurrency, ordering/fusion, restraint)…"), the `loads:` frontmatter, or Lens 1.
