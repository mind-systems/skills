# Plan: 68.2 — the prune gate names a phase as a route target

## Context
`src/skills/roadmap-prune/SKILL.md` § "Step 0 — Deferred-observations gate" lists the parked prune's resolution in numbered parts. Its second part says the resolution session routes "into an **open** task's spec", which names one route target. Task 68.1 has already landed, and `orchestrator-artifacts` § "6. Status-marker grammar" now admits a second target, a phase, spelled `[routed → <roadmap path> § Phase N]`. This task brings that one sentence into line with the grammar, using the text pinned verbatim in `.ai-factory/specs/trickster77777/192-the-prune-gate-names-a-phase-as-a-route-target.md` § "What must be true after".

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Gate text

- [x] **Name a phase as a route target in the second resolution part**
  Files: `src/skills/roadmap-prune/SKILL.md`
  In § "Step 0 — Deferred-observations gate", in item 4 (the stop on an unpinned entry), the second nested resolution part currently reads:

  ```
     2. a **dedicated resolution session** works through the findings — fixing, routing
        into an **open** task's spec, or dismissing — and sets pins per
        `orchestrator-artifacts` § 6;
  ```

  Replace it with:

  ```
     2. a **dedicated resolution session** works through the findings — fixing, routing
        into an **open** task's spec or onto a phase, or dismissing — and sets pins per
        `orchestrator-artifacts` § 6;
  ```

  The only textual change is the insertion of ` or onto a phase` after `task's spec`. The phrase "and sets pins per" stays on the second line. That line is 85 characters, which fits the file's existing wrap (the first line of this part is about 87). Keep the indentation exactly as it is: three spaces before `2.` and six spaces on the continuation lines. Leave parts 1 and 3, and everything else in the step, unchanged. Do not restate the grammar's spelling of a phase target here; the sentence cites `orchestrator-artifacts` § 6 for that.

  Verify:
  - The three lines, joined with single spaces after their leading indentation is stripped, equal the spec's quote exactly: "a **dedicated resolution session** works through the findings — fixing, routing into an **open** task's spec or onto a phase, or dismissing — and sets pins per `orchestrator-artifacts` § 6;" (preceded by the item number `2.`).
  - `git diff src/skills/roadmap-prune/SKILL.md` shows one changed line and nothing else.

### Blast radius

- [x] **Confirm nothing else restates the route target** (depends on Name a phase as a route target in the second resolution part)
  Files: none (verification only)
  Run the sweep from the spec § "What breaks on contact":
  `grep -n -i "open\*\* task\|routing\|routed" src/skills/roadmap-prune/SKILL.md` and `grep -rn "open\*\* task" src/ docs/ CLAUDE.md`.
  Expected hits:
  - In `roadmap-prune/SKILL.md`, only the edited resolution part.
  - Across the repo, that same sentence plus `src/skills/orchestrator-artifacts/SKILL.md` § 6. Task 68.1 already updated § 6 to name both targets, so it needs no change here.
  - The spec also notes that `task-rescue` § "Step 5.6 — Pin disposed observations" and `command-handoff` do not depend on this sentence. Leave both untouched.

  If the sweep finds any other text that names an open task's spec as the only route target, stop and report it. Do not edit any file other than `src/skills/roadmap-prune/SKILL.md`.
