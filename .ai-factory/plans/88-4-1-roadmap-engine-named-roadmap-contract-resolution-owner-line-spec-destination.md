# Plan: 4.1 — roadmap-engine: named-roadmap contract — resolution, owner line, spec destination

## Context
Adds the multiuser "Named roadmaps" mechanism to `roadmap-engine`: how "my roadmap" resolves (argument → derived slug → default), the owner-line collision guard, the test sibling rule, and where a named roadmap's specs land — mechanism only, defaults byte-stable, `note` untouched.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Named-roadmaps section

- [x] **Task 1: Add the "Named roadmaps" section to the engine**
  Files: `src/skills/roadmap-engine/SKILL.md`
  Insert one new `## Named roadmaps` section (mechanism only, no policy, no caller names — per the spec's caller-agnostic guard). Place it after the `## The two-tier artifact` section and before `## Roadmap File Format`, so target-file resolution reads before the format that renders into it. The section states all five items verbatim to the governing spec (`.ai-factory/specs/43-engine-named-roadmap-contract.md`):
  1. **Resolution order** for the roadmap in play: explicit argument (path or filename) wins always → "my roadmap" only when the user asks for it or context names it (the engine never infers multiuser mode) at `.ai-factory/roadmaps/<slug>.md` → default `.ai-factory/ROADMAP.md`.
  2. **Slug derivation:** local-part of `git config user.email`, lowercased, every non-alphanumeric run collapsed to a single hyphen (worked example `kg.wmservice@gmail.com` → `kg-wmservice`); fallback = slugified `user.name` when email is unset.
  3. **Owner line:** first line of every named roadmap is `> Owner: <full email>`, written at creation; every resolution of "my roadmap" verifies it against the current git identity; mismatch → hard stop naming the owner and the two exits (fix git identity / pass the roadmap name explicitly). No silent fallback.
  4. **Test sibling:** a named roadmap's test roadmap is `.ai-factory/roadmaps/<slug>-tests.md`, always derived from the roadmap in play (never independently from identity); same owner line, same single-writer.
  5. **Spec destination:** a named roadmap's spec notes land in `.ai-factory/specs/<slug>/`, passed through `note`'s existing destination hook; per-directory numbering as already built. The default roadmap keeps flat `.ai-factory/specs/`. Add one clause: for a named roadmap the contract line's `Spec:` tag carries the same `<slug>/` subdirectory — it reflects the exact path `note` returns (`.ai-factory/specs/<slug>/<NN>-<slug>.md`), so readers resolving through the tag reach the note. This clause lives only in the new section (item 5), which the byte-stability guard leaves free; the flat template at the two-tier section stays byte-identical (Task 2 does not touch it).
  Guard: engine stays caller-agnostic — do not name outline/decompose/skeleton/rescue/pin-gaps/test-coverage in the new text.

- [x] **Task 2: Add the named-destination variant to the two-tier section's two `.ai-factory/specs/` sites** (depends on Task 1)
  Files: `src/skills/roadmap-engine/SKILL.md`
  `## The two-tier artifact` hardcodes the flat destination `.ai-factory/specs/` in **two physically separate clauses, in different paragraphs eight lines apart** — both must gain the named-destination variant **in place** (they cannot be merged into one sentence without restructuring surrounding prose, which would itself break byte-stability):
  1. The `<NN>`-scan clause (~lines 28–29): `` `<NN>` scanned against `.ai-factory/specs/` so it never collides `` → scanned against the destination in play (`.ai-factory/specs/` default, `.ai-factory/specs/<slug>/` named).
  2. The `note`-destination clause (~lines 36–37): "pass destination `.ai-factory/specs/` via `note`'s destination hook; per-directory numbering happens there" → pass `.ai-factory/specs/` for the default roadmap or `.ai-factory/specs/<slug>/` for a named one, via the same hook.
  Both sites genuinely require the variant: if the destination clause stays unconditional, a named roadmap's specs route to the flat dir, contradicting Task 1 item 5. The spec guard names only "the `<NN>`-scan sentence," but correctness requires the destination clause to gain the identical variant since it too hardcodes `.ai-factory/specs/`. Edit only these two clauses; the rest of the section — including the flat contract-line tag template at :32 — stays byte-identical. These two are the only edits outside the new section.

- [x] **Task 3: Verify guards and byte-stability** (depends on Task 2)
  Files: `src/skills/roadmap-engine/SKILL.md`
  Confirm the change satisfies the spec's guards: (a) a project with no `.ai-factory/roadmaps/` sees zero behavior change — a dry read of the resolution with no argument and no "my roadmap" request yields `.ai-factory/ROADMAP.md`; (b) `note` is not touched (destination is an existing hook value); (c) no caller names leaked into the new section; (d) `grep -n "Owner:" src/skills/roadmap-engine/SKILL.md` hits the contract; (e) no orchestrator-path wording added (out of scope). Fix any drift found; no separate report file.

## Notes
- Edit `src/skills/roadmap-engine/SKILL.md` only — no other file, and not `note`.
- Do not restate the roadmap-family callers or their routing here; those widen in milestones 4.2/4.3.
