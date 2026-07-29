# roadmap-prune Step 7.5: widen the citation grep to the `Task N` / `task N.M` forms

Handoff 04 (`.ai-factory/handoffs/04-plan-citation-rule-is-narrower-than-the-leak.md`) traced the plan-citation leak's real shape against orchestrator-side ground truth. Step 7.5's citation scan and the home rule at `src/global/CLAUDE.md:18` both enumerate the same shapes — `Phase N`, note number, `ROADMAP`/`Plan`, `.ai-factory/` path — but the shape that actually dominates in practice is neither: `# Task N:` section comments (45 occurrences across `orchestrator/tests/`) and inline `task N.M` roadmap-coordinate citations. This task widens only the scan's shape list; the home rule's wording is a separate, undecided surface and stays untouched here.

## Current state (grounded, verified live today)

`src/skills/roadmap-prune/SKILL.md` Step 7.5 (`~:366-388`) is a report-only plan-layer citation scan — never gates, never edits, never blocks — run over the whole target repo tree (excluding `.ai-factory/` and `.git/`). Its grep set, stated in both the item-3 prose and the `grep -rInE` invocation: `Phase [0-9]`, `note [0-9]{2}`, `\.ai-factory/(specs|notes)`, `ROADMAP`, `Plan [0-9]`.

Handoff 04 found this set misses the shape that leaks in practice: `orchestrator/tests/test_agents.py:260` reads `# Task 5: RED case -- semver ordering (fixed in task 2.2)` — a section-comment citation of a roadmap coordinate that is already dangling (`2.2` fixed the sort; phase 2 has since been pruned from the orchestrator's own roadmap). This is one of 45 `# Task N:` section comments across `orchestrator/tests/` (`test_agents.py` 18, `test_main.py` 13, `test_roadmap.py` 7, `test_runtime.py` 5, `test_notify.py` 2), against zero occurrences of that form in `orchestrator/*.py`. Neither the scan nor the home rule (`src/global/CLAUDE.md:18`) names this shape.

## The change (Step 7.5 only)

Add two alternations to **both** the item-3 prose shape list and the `grep -rInE` invocation:

- `Task [0-9]` — the capitalized section-comment form (matches `# Task N:`).
- `task [0-9]+\.[0-9]+` — the lowercase decimal-coordinate form (matches inline citations like `fixed in task 2.2`).

Resulting command pattern:

```bash
grep -rInE "Phase [0-9]|note [0-9]{2}|\.ai-factory/(specs|notes)|ROADMAP|Plan [0-9]|Task [0-9]|task [0-9]+\.[0-9]+" \
  <target repo root> --exclude-dir=.ai-factory --exclude-dir=.git
```

**Why two forms, not one:** capital `Task [0-9]` catches the `# Task N:` section-comment shape; the lowercase form requires the decimal (`[0-9]+\.[0-9]+`) so the common word "task" alone doesn't flood the scan with false positives — this mirrors how the existing set already varies case and precision per term (`Phase` capital and bare, `note` lowercase and two-digit).

**Note:** this spec specifies a change to `roadmap-prune`; it is not implemented by this note — the orchestrator implements it later from this spec plus the roadmap contract line.

## Guards / do NOT touch

- Steps 0–7 (except Step 7.5 item 3) and Step 8 stay byte-identical.
- The Commit section stays byte-identical.
- Preserve `--exclude-dir=.ai-factory --exclude-dir=.git` exactly — the directional boundary (the plan layer citing itself stays legitimate) rests on it.
- The scan stays report-only: never gates, never edits, never blocks; its placement in the step sequence is unchanged.
- Scope stays whole-repo — it already is (the scan is not scoped to the pruned task's own touched files); do not narrow it.
- `src/global/CLAUDE.md:18` (the home rule) is untouched by this task.

## Cross-artifact coupling — the scan is a deliberate, permanent superset of `CLAUDE.md:18`

The home rule (`CLAUDE.md:18`) states the *meaning* — code never cites the plan layer or an `.ai-factory/` path — and deliberately stays general: it does not enumerate `Task N` / docstrings, and by decision it will not. This scan's shape list is operational by contrast: after this task it nets `Task N` / `task N.M` on top of everything the home rule names, so the scan is a report-only **superset** of the home rule. That is the settled design, not a temporary divergence awaiting a mirror-restore — the home carries the meaning, and each consumer (this scan; `orchestrator/prompts/implementer.md`) operationalizes it for its own context. The superset is permitted by Step 7.5's own "false positives are acceptable" clause — a heads-up net, not a proof, and a superset heads-up is strictly safer than a matching-but-narrower one. A future reader must not mistake the asymmetry for a defect or a regression.

## Verification

- Run the widened command against the orchestrator repo root (`/Users/max/projects/sakshi/orchestrator`) and confirm it now surfaces `tests/test_agents.py:260` (and the other `# Task N:` lines) that the pre-change pattern missed.
- Confirm the five pre-existing shapes (`Phase [0-9]`, `note [0-9]{2}`, `\.ai-factory/(specs|notes)`, `ROADMAP`, `Plan [0-9]`) still match — no regression.
- Confirm the pattern is valid ERE (`grep -E` accepts it without error).

## Files & types

- edit: `src/skills/roadmap-prune/SKILL.md` — Step 7.5, item-3 prose list and the `grep -rInE` invocation, only.
