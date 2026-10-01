## Plan Review Summary

**Plan:** `.ai-factory/plans/trickster77777/15-63-1-the-architect-comes-back-on-a-bare-invocation.md`
**Files targeted:** 1 (`src/skills/agent-architect/SKILL.md`)
**Risk Level:** 🟢 Low

### Context Gates

- **Roadmap — OK.** The contract line for 63.1 in `.ai-factory/roadmaps/trickster77777.md` (Phase 63, governing spec `docs/paired-loop.md`) lists five changes: the start decided by session id, the snapshot no longer carrying the buffer's path, removal of the handle-recovery block (keeping the liveness probe and the dead-editor rule), and matching wording in § "Your buffer is shared; you alone write it" and § "On every invocation". The plan has one task for each. The prerequisite 62.2 is `[x]` (commit `cd83d47`). The file carries 62.2's text as the plan assumes: the founding passage with `address.md`, the probe paragraph opening "On every start and every rehydration", and the clause "Either occasion writes the snapshot into your own folder".
- **Task spec — OK.** I read `.ai-factory/specs/trickster77777/176-…` in full. Every replacement in the plan maps to a passage pinned in the spec's "What must be true after" section, and the plan tells the implementer to copy those passages verbatim.
- **Governing spec — OK.** `docs/paired-loop.md` § "Where the memory lives" says the head reads its session id, finds the folder that holds it and rehydrates from the latest snapshot there. A session that no folder claims founds a new folder. The pinned founding passage and § "On every invocation" say the same thing. The old wording, where a start was decided by "whatever the user hands you", goes, as the doc's rule "Any text the user adds is the work, never the way home" requires.
- **Downstream (64.1) — OK.** Spec 177 reads the file as specs 175 and 176 leave it. It quotes exactly the snapshot closing sentence this plan deletes and exactly the replacement sentence this plan writes into § "Your buffer is shared; you alone write it". The plan correctly leaves the pairing-role mentions to 64.1: the role-recording passage and the first sentence of § "Your buffer is shared".
- **Architecture — OK (no conflict).** `.ai-factory/ARCHITECTURE.md` only places `agent-architect` as the counterpart of the `editor` agent. The change moves no boundary.
- **Rules — WARN.** `.ai-factory/RULES.md` is not present, so there are no explicit conventions to check against.

### Verification of the plan against the file

- **Task 1 (founding passage).** The anchor "Second, the buffer — and which of two starts this is decides what you do:" appears once, starting mid-line in the first paragraph of § "Spawn once, message thereafter". The pinned replacement repeats that same opening clause, so replacing from the anchor through "Either way the buffer exists before any editor does." is exact. "By the probe this section describes" correctly points forward to the next paragraph, which the plan keeps unchanged. The first half of the paragraph also stays unchanged, including "it is where your buffer's path and rules are defined", which the verify step expects to survive.
- **Task 2 (snapshot paragraph).** All three edits (the dash clause, "records your buffer's path and", and the closing sentence) match the current text exactly. After them the paragraph closes on the supersession sentence, as the spec requires.
- **Task 3 (recovery block).** The cut point "recover no handle from a listing, for the same reason." appears once. The three paragraphs to delete ("A handle recovered this way…", "The liveness probe is unchanged:…", "Leaving both buffers live…") are identified by their opening words, so no line positions are involved. After the cut, "If the send fails, the editor is dead" still reads correctly after "attempting to send it to the recorded handle is the probe". The paragraph where the spawn writes the handle ("whichever of the two starts above you came through") still holds, because the two starts are now "folder found" and "no folder found".
- **Tasks 4–5.** Both targets are unique sentences or section bodies, and the replacements are the spec's pinned text.
- **Verify step.** I ran the sweep before any edit and walked through the expected results. `meta.json`, `naming a buffer`, `handoff below`, `re-point` and `recovered` occur in `agent-architect` only inside the removed text. "recovers" and "recover no handle" do not match `recovered`. After the edits, `buffer's path` matches only lines 36 and 125 of `agent-architect`. The "buffer's own path" sentence does not match that string, and the Relay-section mention breaks across a line, so it does not match either. The expectation in the plan is therefore exact. The `architect-editor-engine` matches (the re-read rule and the "rides alongside" sentence) stay true and are correctly left untouched.

### Critical Issues

None.

### Positive Notes

- Every edit is anchored by a unique string or an opening phrase, never by a line number.
- The plan separates this task from its neighbours carefully. It leaves 64.1's pairing-role text and the spawn-prompt pointer sentences alone, and it states why.
- The plan checks its 62.2 prerequisite against the file itself instead of relying on the roadmap checkbox.
- The verify step checks the actual grep results, not just whether the implementer reports success.

## Deferred observations

- Affects: `.ai-factory/specs/trickster77777/176-the-architect-comes-back-on-a-bare-invocation.md` / Phase 63 — the plan follows the spec and keeps 62.2's probe paragraph unchanged. That paragraph's failure branch says to "leave `address.md` as it was, or unwritten at a founding". Once the founding passage says "No folder found, for whatever reason, means you are a new head", the "as it was" branch can no longer happen: the folder is found only through a successful probe, so a failed probe always leads to a founding. It also means that a resumed head whose nonce probe fails once, for example because of a transcript flush delay, silently starts a new folder and leaves its own buffer behind. The only signal is the "mention in passing" that the probe failed. Whether that is acceptable, or whether a failed probe should block recognition differently, is a decision for the spec or governing-spec owner. It cannot be fixed inside this task, because the spec pins the probe paragraph unchanged. [routed → .ai-factory/roadmaps/trickster77777.md § Phase 69]

PLAN_REVIEW_PASS
