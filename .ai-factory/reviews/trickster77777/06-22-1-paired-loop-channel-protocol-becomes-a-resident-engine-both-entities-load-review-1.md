# Code review — 22.1 paired-loop channel protocol becomes a resident engine

## Scope
Reviewed the four code artifacts of the task (planning artifacts under `.ai-factory/` excluded):
- **new** `src/skills/architect-editor-engine/SKILL.md`
- **modified** `src/skills/agent-architect/SKILL.md`
- **modified** `src/agents/editor.md`
- **new symlink** `active/skills/architect-editor-engine`

These are skills/agent definitions (executable runtime behavior), so "runtime correctness" is read as: does the pair behave coherently, and does the harness resolve/load the engine as designed.

## Spec verification (all pass)
Ran the spec's own static checks (spec §Verification):
- `active/skills/architect-editor-engine` → `../../src/skills/architect-editor-engine` ✔ (resolves).
- Retired phrases in `agent-architect/SKILL.md` — `grep` for "ending with \`::\`", "literal payload text", "apply it with arguments" → **zero hits** ✔ (both `::` occurrences, L56 and old L102, cleared).
- `REPORT-ONLY` / `APPLY-EDIT` named in both callers ✔ (7 lines in `agent-architect`, 6 in `editor.md`).
- `loads:` in `agent-architect` includes `architect-editor-engine` ✔ (L14), and `Skill` was added to `allowed-tools` (L13) — the plan-review-1 blocking issue is correctly resolved.
- Engine reverse-graph grep line literally includes `src/agents/*.md` ✔ (L29).
- `editor.md` instructs loading `architect-editor-engine` via the Skill tool as the first spawn action ✔ (L18–21).

Frontmatter is at the engine baseline (`user-invocable: false`, `disable-model-invocation: false`, `allowed-tools: Read`, no `loads:`) — model-invocable so the pair can load it via the Skill tool, not user-invocable; the engine appears in the live skills manifest, confirming it resolves. `::` grammar is fully contained in `agent-architect`; the engine carries none. The three design decisions the spec marks "do not re-litigate" are honored (hard format token, zero `::` in engine, review-section folded in as a special case).

## Findings

### Low — stale `apply it with arguments` example survives in `editor.md`, re-introducing the very word the task set out to purge
`src/agents/editor.md:50-51` still illustrates the pinned-skill-path case with the old phrasing:

> Either mode's target may arrive via a pinned skill path ("Read `…/SKILL.md` and **apply it with arguments**: …")

Under the new protocol the architect no longer sends that. Its REPORT-ONLY skill-expansion is now phrased "read and run `<SKILL.md>` with arguments … **as a report; write no files**" (`agent-architect/SKILL.md:97-101`). So the editor's canonical example quotes a message shape the architect never emits for a relayed skill, and it does so using the exact word — "apply" — that the task exists to eliminate, because a skill-expansion reading "apply" "misreads a research pass as an edit order" (spec §Current-state / handoff 03).

Impact is limited, not functional: the editor's mode is decided strictly by the opening `REPORT-ONLY`/`APPLY-EDIT` token, and the new report-only default (`editor.md:57-61`) explicitly states a pinned skill's write-capable default never promotes a round to apply. So behavior is preserved even with the stale example — this is a documentation-coherence drift, not a mode-selection bug.

Note this is within the spec's letter: spec item 3 for `editor.md` enumerated only the mode-tell rewrite, the first-spawn load, and the report-only default under the pinned-skill-path paragraph — it did not ask to rewrite this example, and the spec's verification grep for the retired phrase targeted `agent-architect` only. So it is not a spec violation. It is worth a one-line fix for coherence: change the editor's illustrative quote to the neutral/report phrasing (e.g. drop "apply it with arguments" in favor of "run it with arguments: …"), so the pair's two files describe the same message shape and the purged word does not linger in the editor's own default-mode example.

## Assessment
The implementation is faithful to the spec and internally coherent; the plan-review-1 blocking issue (`Skill` in `allowed-tools`) and both tightening issues (the anti-contamination reconciliation at `agent-architect` L79–84, and the scope-question carve-out reworked to marked-reply terms at L124–131) are all correctly landed. The single finding above is low-severity and non-blocking.
