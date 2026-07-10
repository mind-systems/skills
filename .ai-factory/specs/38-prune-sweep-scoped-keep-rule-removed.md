# roadmap-prune: sweep only the pruned tasks' specs; the keep-recent rule is removed

## Current state

`src/skills/roadmap-prune/SKILL.md` Step 5 (`:206`) captures the `Spec:` tag path of **every** `[x]` line — "both the lines being pruned and any `[x]` lines kept as recent context" — and `:208` `rm -f`s every captured path. Two defects:

1. **Kept tasks lose their specs.** A `[x]` line retained in the roadmap survives the prune with its spec deleted and its `Spec:` tag dangling — a line whose full specification no longer exists anywhere at HEAD.
2. **The keep-recent rules decide for the user.** Two automatic retentions exist: Step 1 (`:72-74`) carves the prune slice as "all `[x]` except the most recent N that provide active context" (N "usually 0–5" — discretionary, which is why it has rarely been seen to fire), and Step 6 (`:224-226`) "always retain the last phase header **and its 2 most recent `[x]` tasks**" — a phase-grammar rule that has never fired yet but would, together with defect 1, leave two spec-less tasks on its first live run.

## Change

- **Both task retentions are deleted.** Step 1's slice becomes "all `[x]` tasks" (the ~20-lines-of-context framing and the "most recent N" heuristic go); Step 6's "2 most recent `[x]` tasks" clause goes. The user may explicitly name tasks to keep — at invocation or at the confirmation step; only an explicit user instruction retains a line.
- **The last-phase-header retention survives** — it is the numbering anchor (the engine continues phase numbers from the file-wide maximum; deleting the last header would reset the sequence). The header is retained even when emptied of tasks; only the "and its 2 most recent `[x]` tasks" half of the Step 6 sentence dies.
- **The sweep is scoped to what is actually deleted.** Step 5 captures the `Spec:` tag paths of the lines being pruned **only**; a user-kept `[x]` line keeps both its roadmap line and its spec file untouched — the tag stays valid at HEAD.

## Files & types

- edit `src/skills/roadmap-prune/SKILL.md` — Step 5 capture rule (`:206`) + wherever the keep-recent retention is stated (task-deletion step)

## Guards

- Capture-before-delete ordering stays; "no tag → skip, never synthesize" stays verbatim.
- The four-artifact-dir sweep (`plans/`, `plan-reviews/`, `reviews/`, `patches/` — whole dirs) is unchanged: kept tasks' pipeline artifacts still go, their content stays reachable through the Step 4.1 snapshot hash; only **spec** deletion becomes scoped.
- The deferred-observations gate is 1.8.1's territory — untouched here.
- Step 4.1 snapshot, `## Features` anchoring, commit policy — untouched.

## Verification

- `grep -n -i "recent context\|kept" src/skills/roadmap-prune/SKILL.md` → the retention rule is gone; capture speaks only of pruned lines.
- Dry-run on a roadmap where the user names one `[x]` task to keep: the delete-list contains every pruned line's spec and **not** the kept line's; after the run the kept line's `Spec:` tag resolves.
- Dry-run with no keeps: every `[x]` line and every captured spec goes — no silent survivors.
