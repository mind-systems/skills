## Code Review Summary

**Change under review:** `src/skills/roadmap-prune/SKILL.md` only (the three plan/plan-review/JSON files under `.ai-factory/` are orchestrator bookkeeping, not code). Reviewed the full modified file against its governing spec `.ai-factory/specs/38-prune-sweep-scoped-keep-rule-removed.md`, the plan `75-1-8-2-…md`, and the roadmap contract line (`ROADMAP.md:169`).
**Risk Level:** 🟢 Low — a self-contained prompt-body edit; no executable code, no runtime/migration/type surface.

### What the change does
Removes both automatic keep-recent retentions from `roadmap-prune` and scopes the spec sweep to pruned lines only. The skill is agent-instruction text, so "runtime" is an agent following the steps; the review checks for contradictions, ambiguity, and stale cross-references that would misdirect that agent.

### Spec fidelity — all four tasks verified

- **Task 1 (Step 1, `:76-81`)** — OK. The "~20 lines of active context" framing and the "all `[x]` except the most recent N (N usually 0–5)" heuristic are gone; the slice is now "**all `[x]` tasks** … pruned by default," with the sole exception being an explicit user-named retention. The "history is preserved in git and ARCHITECTURE.md" reassurance is retained. `grep -i "most recent\|~20 lines\|except the most"` → zero hits.
- **Task 2 (Step 6, `:236-247`)** — OK. The "and its 2 most recent `[x]` tasks" clause is deleted (`grep "2 most recent"` → zero hits); the last-phase-header retention survives as the numbering anchor and is explicitly kept "even when the header is emptied of all its tasks." The emptied-phase caveat is reworded to "a phase that still holds a **user-kept** `[x]` task … keeps its header; the last phase header is kept regardless" — the ripple the plan anticipated is handled, and the coexistence with the emptied-phase sweep is unambiguous (the last header is exempt from deletion).
- **Task 3 (Step 5, `:213-222`)** — OK. Capture is scoped to "every `[x]` line **being pruned**"; a user-kept line's tag is explicitly not captured and its line + spec stay untouched. The two guard sentences flagged by plan-review-1 are both reconciled: the Step 5 trailer (`:220-222`) and the "What NOT to do" bullet (`:301-303`) now say "the **pruned** `[x]` lines' `Spec:` tags" and name the user-kept line alongside open `[ ]` tasks as never-touched. Preserved verbatim: capture-before-delete ordering (`:209`), "A `[x]` line with no `Spec:` tag … skip it, never synthesize a path," and the four-dir `rm -rf` sweep (`:217`, unchanged).
- **Task 4 (Step 7, `:268-269`)** — OK. The stale "intentionally kept as recent context" verify phrase is replaced with "explicitly kept by the user."

### Guards (spec § Guards)
- Capture-before-delete ordering intact (`:209`, `:213`). ✓
- "no tag → skip, never synthesize" verbatim (`:215-216`). ✓
- Four-artifact-dir sweep unchanged — kept tasks' pipeline artifacts still go, reachable via the Step 4.1 snapshot hash. ✓
- Deferred-observations gate (Step 0) untouched — 1.8.1 territory. ✓
- Step 4.1 snapshot, `## Features` anchoring, commit policy untouched. ✓

### Spec verification greps (run live)
- `grep -i "recent context\|kept"` → 6 hits, every one legitimate ("user-kept", "keeps its header", "explicitly kept by the user"); no automatic-retention language survives. ✓
- `grep "most recent"` / `grep "2 most recent"` → zero hits. ✓
Both scoped-sweep dry-runs the spec asks for hold by construction: with one named keep, its tag is never captured (its spec resolves at HEAD); with no keeps, every `[x]` line's tag is captured and swept — no silent survivors, and the last phase header remains as the anchor.

### Correctness / bug check
No contradictions or dead cross-references introduced. The last-phase-header retention and the emptied-phase sweep are explicitly reconciled (`:246-247`), so an agent cannot both "keep" and "delete" the final header. No other step assumed the removed keep-recent behavior. Frontmatter description ("deleting the pruned tasks from the roadmap") stays accurate. No scope creep into 1.8.3's pyramid pass — rationale prose is left intact.

## Deferred observations
- Affects: `roadmap-prune/SKILL.md:79-80` (Step 1) / the skill's flow — Step 1 offers retention "at invocation or **at the confirmation step**," but the skill has no discrete confirmation step (it runs Step 0→8 then commit-on-request; it does not load `roadmap-engine`'s draft→confirm flow). The only reliable retention channel is "at invocation," with the pre-commit working-tree state as an informal second chance. This wording is inherited verbatim from the ratified spec (`specs/38` § Change) and was flagged in both plan-reviews as not-a-defect; it is out of this milestone's file boundary. Not a blocker — noted so a future task that wants a real confirmation step knows it must add one.

REVIEW_PASS
