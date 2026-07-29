# Plan: roadmap-prune Step 7.5 — widen the citation grep to the `Task N` / `task N.M` forms

## Context
Step 7.5's report-only plan-layer citation scan misses the leak shape that actually dominates in practice (`# Task N:` section comments and inline `task N.M` coordinate cites), so widen its shape list — in both the item-3 prose and the `grep -rInE` invocation — with two new alternations.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Widen the Step 7.5 citation scan

- [x] **Task 1: Add the two alternations to the item-3 prose shape list**
  Files: `src/skills/roadmap-prune/SKILL.md`
  In Step 7.5 item 3 (`~:375`), extend the prose list of citation shapes from
  `` `Phase [0-9]`, `note [0-9]{2}`, `\.ai-factory/(specs|notes)`, `ROADMAP`, `Plan [0-9]` ``
  by appending two more shapes: `` `Task [0-9]` `` (the capitalized `# Task N:` section-comment form) and `` `task [0-9]+\.[0-9]+` `` (the lowercase decimal-coordinate form, e.g. `fixed in task 2.2`). Keep the surrounding sentence wording ("Grep (read-only) for citation shapes: …") and the "guidance, not contract" note that follows byte-identical — only the enumerated shape list grows.

- [x] **Task 2: Add the two alternations to the `grep -rInE` invocation** (depends on Task 1)
  Files: `src/skills/roadmap-prune/SKILL.md`
  In the fenced `bash` block inside Step 7.5 item 3 (`~:379-382`), extend the ERE pattern so it reads exactly:
  ```bash
  grep -rInE "Phase [0-9]|note [0-9]{2}|\.ai-factory/(specs|notes)|ROADMAP|Plan [0-9]|Task [0-9]|task [0-9]+\.[0-9]+" \
    <target repo root> --exclude-dir=.ai-factory --exclude-dir=.git
  ```
  Preserve the `--exclude-dir=.ai-factory --exclude-dir=.git` flags and the `<target repo root>` placeholder exactly — only the two alternations `|Task [0-9]|task [0-9]+\.[0-9]+` are appended to the quoted pattern. Do not reorder or alter the five pre-existing alternations.

### Phase 2: Verify the widened pattern

- [x] **Task 3: Confirm the widened scan surfaces the leak and preserves the existing matches** (depends on Task 2)
  Files: `src/skills/roadmap-prune/SKILL.md` (no edit — verification only)
  Run the widened command against the orchestrator repo root (`/Users/max/projects/sakshi/orchestrator`) and confirm: (a) it now surfaces `# Task N:` section-comment lines the pre-change pattern missed — e.g. `tests/test_main.py:260` (`# Task 1: …`) and `tests/test_agents.py:17` (`# Task 1: …`); (b) the five pre-existing shapes still match (no regression); (c) `grep -E` accepts the pattern without an ERE error.

## Guards / do NOT touch
- Steps 0–7 (except Step 7.5 item 3) and Step 8 stay byte-identical; the Commit section stays byte-identical.
- The scan stays report-only — never gates, never edits, never blocks; its placement in the step sequence is unchanged.
- Scope stays whole-repo — do not narrow it to the pruned task's touched files.
- `src/global/CLAUDE.md:18` (the home rule) is untouched: the scan is a deliberate, permanent report-only superset of the home rule, not a divergence to be mirror-restored here (§5 / cross-artifact coupling in the spec).
