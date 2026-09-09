# Review — 33.1 four durable surfaces stop naming the handoff

## Code Review Summary

**Files Reviewed:** 4 changed (`src/skills/roadmap-engine/SKILL.md`, `src/skills/roadmap-outline/SKILL.md`, `src/skills/roadmap-prune/SKILL.md`, `src/skills/orchestrator-artifacts/SKILL.md`) + 3 new artifacts under `.ai-factory/` (plan, sidecar, plan-review). Diff is 5 insertions / 5 deletions.
**Risk Level:** 🟢 Low

### What changed, checked line by line against the task spec

- `roadmap-engine:86` — `<direction preamble: source spec links, hard rules, gating for this direction>`. Byte-identical to the string the spec's change item 1 prescribes. The rest of the format block is untouched: the `## <Direction name>` header above, the `### Phase N` intro below, and the three contract-line examples are unchanged in the diff, and the fenced block still closes correctly.
- `roadmap-outline:40` — `Links to task specs are allowed as plain markdown links inside the`, with `:41` untouched, so the sentence reads exactly as change item 2 prescribes and still ends "no formal `Spec:` tag, no invented task specs." The line is left short (64 code points) rather than re-flowed, which is what the spec's line-break guard requires.
- `roadmap-prune:284` — `preamble: `roadmap-outline` permits unrelated task-spec links in that`. Only the enumeration narrowed. Read as a whole (`:281–286`), the rationale still carries all three of its clauses: keying on the literal `Phase note:` token "and on nothing else — never on a link's position in a preamble"; those links living "in that same prose"; and "this skill holds `Bash(rm *)`, so a positional key would follow one of those to a deletion." The safety argument is intact at full force.
  One grammatical hazard specific to collapsing an enumeration to a single member does not fire here: "one of those" still has a plural antecedent ("task-spec links"), so the sentence stays well-formed. The narrowed claim is also still true of the surface it describes — `roadmap-outline-deep`'s `Phase note:` pointer is itself a `.ai-factory/specs/…` link, and other task-spec links are permitted in the same prose, so the confusable-link risk the rationale guards against is real, not hypothetical.
- `orchestrator-artifacts:68–69` — writer clause reads "Written by the **resolution session** — the dedicated session the user opens when a prune parks — at the moment it disposes of an observation:". Matches change item 4 verbatim. Line 67 is unchanged and the bullet list at `:71–74` is untouched, so the two em-dash appositive still reads as one and the marker literals below are byte-identical.

### Protocol tokens and cross-file couplings

- No scanned literal moved. `## Deferred observations` (`orchestrator-artifacts` § 5), the entry form `- Affects: …`, the markers `[fixed]` / `[routed → <path>]` / `[dismissed]`, the legacy marker list, the PASS signals, and the `Phase note:` / `Spec:` tags are all outside the diff.
- Reverse-graph sweep for anything that depended on the removed words: `grep -rn "resolution session" src docs` returns `roadmap-prune:64`, `task-rescue:557`, `task-rescue:686` — all three name the session and cite `orchestrator-artifacts` § 6 for the grammar rather than restating the writer's provenance, so none dangles. `grep -rn "direction preamble" src docs` returns only `roadmap-engine:86`: the format block is the single home of that line, so nothing else needed the same edit.
- The trigger phrasing is consistent with its own home rather than invented: `roadmap-prune:59` says the prune is "**parked**, not engineered around", and `docs/sakshi-harness/skill-cycle.md:59` describes the same park → `command-handoff` → resolution-session sequence. The clause stops naming the artifact, not the event, so the cycle doc is not contradicted.
- Sibling repo: `orchestrator` defines nothing about the status-marker writer in code, prompts, or docs — the only hit anywhere in it is `.ai-factory/handoffs/04-…:32`, that repository's own plan layer, correctly left alone per the spec's guard. Its CLAUDE.md scopes the mirror obligation to directory layout, artifact naming, PASS signals, sidecar fields and review-section format; the writer's provenance is none of the five, so no lockstep change is owed and `orchestrator-artifacts` § 7 stays true.

### Verification — the spec's own checks, run

- case-insensitive `handoff` occurrences: `roadmap-engine` **0**, `roadmap-outline` **0**, `orchestrator-artifacts` **0** (1 each before); `roadmap-prune` **4** (5 before), the survivors being two on `:61` (`/command-handoff`, "the handoff"), one on `:63` (`.ai-factory/handoffs/`), one on `:447` ("never swept") — exactly the four the spec names, all of them the act of handing off.
- Residual-content checks, so an over-deletion cannot pass as a narrowing: the format block's preamble line **1**; `roadmap-outline`'s grant line **1**; its "no formal `Spec:` tag, no invented task specs" **1**; prune's three rationale clauses **1** each; the status-marker grammar naming the resolution session as writer and a parked prune as trigger **1** each.
- `git diff HEAD --stat -- src/` lists exactly the four named files and nothing else; `git status --porcelain` shows no change outside `src/` and `.ai-factory/`, so `docs/`, `CLAUDE.md` and `active/` are untouched. `agent-architect` and `roadmap-test-coverage`'s `$HANDOFF_LIST` are outside the diff, as their guards require.
- Line-break guard: the three single-line sites changed exactly one line each; `orchestrator-artifacts` changed the two lines its phrase spanned. New `:68` measures 86 Unicode code points against that file's longest existing line of 96 — inside the file's wrap range, so leaving it unwrapped is right. No paragraph was re-flowed anywhere.
- All four targets are symlinked into `active/skills/` from `src/skills/`, so the edits go live with no `active/` change; all four are ours with no `upstream/ai-factory/` counterpart, so a re-sync cannot clobber them.

### Critical Issues

None.

### Positive Notes

- The narrowing kept the argument, not just the word count: prune's rationale still reaches its conclusion ("a positional key would follow one of those to a deletion") on task-spec links alone, which was the one way this task could have quietly weakened a `Bash(rm *)` safety rule.
- Removing `handoff` from `orchestrator-artifacts` without removing the trigger — "when a prune parks" instead of "from the parked prune's handoff" — keeps the clause operationally readable for the session that has to act on it, and borrows prune's own word for the state rather than coining a second one.
- The shortened lines were left short. Re-wrapping would have been the natural editing reflex and would have swelled three one-phrase diffs into paragraph rewrites.

## Deferred observations

- Affects: `src/skills/roadmap-outline-deep/SKILL.md` — `:119–120` justifies its `Phase note:` pointer as "already legal under `roadmap-outline`'s own rules — plain markdown links are permitted in intro/preamble prose". That paraphrase is now looser than the grant it cites, which after this task reads "Links to task specs are allowed…". Nothing breaks: the pointer it emits is a `.ai-factory/specs/<slug>/<NN>-<slug>.md` path, squarely inside the narrowed grant, and this task's boundary is the four named files. Worth tightening on whichever pass next touches that skill, since a further narrowing of the grant would strand the sentence. (The plan-review raised the same entry; one pin disposes of both.)
- Affects: `.ai-factory/specs/trickster77777/108-skills-stop-naming-the-handoff.md` — the coupling stays declared on one side only. `roadmap-prune:284` names `roadmap-outline` as the source of the permission its deletion-safety rationale rests on, but `roadmap-outline:40–41` says nothing about that permission being load-bearing elsewhere — the both-sides declaration CLAUDE.md § "Dependencies and the skill graph" asks for on invariants grep cannot derive. Correctly out of scope here (the spec pins "The remainder of the sentence is untouched"), and the exposure is mild: prune keys on the literal token, the conservative side, so losing the permission entirely would leave prune safe and only its cited rationale stale. Raised because the spec itself names the failure mode — "Remove the permission and the sentence cites something that no longer exists" — and nothing on the `roadmap-outline` side warns a future editor.

REVIEW_PASS
