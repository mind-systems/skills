# Handoff — task-rescue: sidecar rollback markers gain an iteration index

## 1. Frame

The sibling **orchestrator** repo is changing the sidecar `step` grammar. Today the two "artifact produced" markers are written bare — `"planned"` and `"implemented"`; orchestrator task **18.2** gives both an iteration index — `"planned:N"` and `"implemented:N"` — and **removes the bare forms entirely** (clean break, no legacy branch). `task-rescue` is the **only skill-side writer** of these markers (per `orchestrator-artifacts` §3), and its rollbacks write the bare values. Once 18.2 lands, a bare `"planned"` / `"implemented"` is no longer an accepted explicit resume point — the orchestrator drops it and falls through to its disk heuristic. This handoff is the paired skills-side change: write the indexed values and re-sync the grammar table. Rehydrate from the files named below; do not trust memory.

## 2. Why it must change

Orchestrator 18.2 (governing spec: `orchestrator/.ai-factory/specs/trickster77777/32-resume-carries-verify-iteration.md`) indexes both markers in `orchestrator/main.py` + `resume.py`:

- writes `f"planned:{n}"` (was bare `"planned"`) and `f"implemented:{n}"` (was bare `"implemented"`);
- adds `planned:N` / `implemented:N` branches to `_validate_sidecar_step` and **empties the bare always-valid tuple** — no bare fallback;
- dispatches `planned:N` → `("plan_review", N)` and `implemented:N` → `(verify_step, N)` in `_detect_step`.

So after 18.2 a sidecar carrying a bare `"planned"` or `"implemented"` is an **unrecognized** value: it passes validation, matches no dispatch branch, and degrades to the disk heuristic. In `task-rescue`'s rollbacks the heuristic *happens* to still reach the intended round (all plan-reviews/reviews are deleted at these depths → the no-artifact branches return attempt/iter 1), so it is not catastrophic — **but** the skill's explicit-marker contract is broken and its documented closed-set table becomes factually wrong. Fix for correctness and to keep the "mirrors the orchestrator" invariant honest.

The correct values are **`"planned:1"`** and **`"implemented:1"`**: both rollback depths delete *all* plan-review / review files for the slug (verified: spec+plan depth deletes all plan-reviews; spec+plan+code depth deletes all reviews), so the next round is 1. The rescue never needs a higher `N` — it never retains partial review artifacts at these depths.

## 3. Read-first map

- `src/skills/task-rescue/SKILL.md` — the only file to edit. Relevant spots below.
- `src/skills/orchestrator-artifacts/SKILL.md` §3 (Sidecar fields, line ~42) — delegates the closed set to task-rescue; **no content edit needed**, but confirm the delegation line still reads true after the table update.
- `orchestrator/.ai-factory/specs/trickster77777/32-resume-carries-verify-iteration.md` — the governing spec for the orchestrator side (the referent this mirror must match).
- `orchestrator/orchestrator/resume.py` — `_validate_sidecar_step` / `_detect_step`, the code the task-rescue table mirrors (post-18.2).

## 4. The exact change (task-rescue/SKILL.md)

`"planned"` → `"planned:1"` (spec+plan depth) and `"implemented"` → `"implemented:1"` (spec+plan+code depth), everywhere they appear; the grammar rows generalise to `"planned:N"` / `"implemented:N"`. `plan_reviewed` is unchanged (single-state, never indexed).

- **Depth summary block** (~lines 238–243): `sidecar step → "planned"` → `"planned:1"`; `sidecar step → "implemented"` → `"implemented:1"`.
- **spec+plan depth** (~line 292 procedure + its Emit): set `step` to `"planned:1"`; emit `… step set to "planned:1"; implementer session dropped.`
- **spec+plan+code depth** (~lines 314, 323, 326): "roll back to `"implemented:1"`"; set `step` to `"implemented:1"`; emit `Sidecar updated: step set to "implemented:1".`
- **Closed-set table** (~lines 361–364): change the two rows to
  `| "planned:N" | plan-review, attempt N | none — always valid |`
  `| "implemented:N" | review, iter N | none — always valid |`
  and add a one-line note that the rescue always writes **N = 1** (all prior-round artifacts are deleted at both depths); the bare `"planned"` / `"implemented"` forms are retired (no longer accepted by the orchestrator).
- **Always-valid guard** (~line 368): `"planned"` / `"implemented"` → `"planned:1"` / `"implemented:1"` (write `"planned:1"` only when the plan `.md` is present; `"implemented:1"` only when the plan `.md` is present and a non-empty working diff exists — guards unchanged, values gain the index).
- **Note paragraph** (~lines 370–374): `"planned"` (spec+plan depth) → `"planned:1"`; `"implemented"` (spec+plan+code depth) → `"implemented:1"`.
- **"Do not write" guard** (~line 462): `"planned"` or `"implemented"` → `"planned:1"` or `"implemented:1"`.

The table's own reminder already says it "mirrors `_validate_sidecar_step()` / `_detect_task_step()` in `orchestrator/resume.py` — if the orchestrator's accepted set changes, update this table" — this is exactly that update.

## 5. Sequencing

This change is only *correct* once orchestrator 18.2 is in effect. Ordering:
- **Before 18.2 lands:** bare `"planned"` / `"implemented"` still work; writing `"planned:1"` / `"implemented:1"` would be unrecognized by the *current* orchestrator (degrades to heuristic → also attempt/iter 1, so still non-fatal, but not explicit).
- **After 18.2 lands:** the `:1` forms are the correct explicit markers; the bare forms degrade.

Both the old and new orchestrator reach round 1 for these rollbacks either way (explicit marker or heuristic), so there is no hard breakage window — but land this **paired** with 18.2 so the skill's table never lies about the accepted set. Route it as a task in this repo's `.ai-factory/` (contract line + task spec) per the family's task-routing rule; it is a doc/skill edit, no code.

## 6. Current state

- Orchestrator side: Phase 18 of `orchestrator/.ai-factory/roadmaps/trickster77777.md` decomposes each fix spec-before-code — the marker work is **18.2.1** (grammar red tests, spec 34) → **18.2.2** (impl + sidecar migration, spec 32); the network work is **18.1.1**/**18.1.2** (specs 33/31). **Not yet implemented** (the orchestrator runs them separately). 18.2 covers **both** markers (`planned:N` + `implemented:N`) — the grammar this handoff mirrors is that pair; the 18.2.1/18.2.2 split is an orchestrator-side sequencing detail and does not change what `task-rescue` must write.
- The one wounded target sidecar (`repo-stats-herald/.ai-factory/plans/34-6-2-coordination-root-seeding.json`) is already hand-migrated to `"implemented:3"` — a data migration, unrelated to this skill change. No sidecar carries a bare `"planned"`, so there is no plan-side migration.
- Skills side: **nothing changed yet** — this handoff is the whole to-do.
