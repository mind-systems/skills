# Plan review 2 — 36.2 — the buffer's creation is conditional, and it moves to the architect's own start

## Code Review Summary

**Files Reviewed:** 1 plan + 7 ground-truth files (`src/skills/agent-architect/SKILL.md`, `src/skills/architect-editor-engine/SKILL.md` § "The architect's buffer", `docs/paired-loop.md` § "How the memory begins, and how it survives", specs 117/122/123, the roadmap phase 36 block, plan-review 1)
**Risk Level:** 🟢 Low — a single-file prose edit; every anchor a neighbouring task depends on is quoted and kept verbatim, and the three findings of review 1 are resolved in the plan text itself.

### Context Gates

- **Architecture — OK.** `.ai-factory/ARCHITECTURE.md` § "Composition: mechanism vs policy": no new `loads:` edge; nothing of the engine's content (path, numbering, zones, drain rule) is restated — creation names "the path and numbering the engine defines" and stops. The engine's reverse-graph marker ("Load this skill once at birth — the architect per the instruction in its own body") still resolves, and more literally than before: the instruction now sits at the architect's own start rather than at a deadline somewhere before the first channel-message.
- **Rules — WARN (missing optional files).** `.ai-factory/RULES.md` and `.ai-factory/skill-context/aif-review/SKILL.md` do not exist. Nothing to apply.
- **Roadmap — OK.** The plan heading matches `.ai-factory/roadmaps/trickster77777.md` `- [ ] **36.2 …**`, the first `[ ]` line of phase 36 (36.1 is `[x]`, commit `4eb7b0c` at HEAD). The contract line's four requirements — conditional rule, engine resident as part of the same start ahead of the buffer, handle write stays put as a write into an existing buffer, spec 117 — each map to a plan task. Spec 117 § "The change" and § "Blast radius" were read; the plan's fences against 36.1/36.4/36.5 follow them exactly. The governing spec section was read fresh: "The memory exists before the hands do", snapshot → same memory resumed, no pointer → new head creates first, then takes on a hand — the plan's draft carries all three and edits the doc not at all (the doc is ahead; docs → roadmap → code).
- **Neighbour-task collision — OK.** Spec 122 (36.4) attaches to `write its handle into the buffer` and widens "its content *is* the spawn prompt" — both kept verbatim. Spec 123 (36.5) edits the opening of the handoff sentence and § "On every invocation" — both byte-identical here. The bridge appositive ties the pointer to the *artifact* ("the handoff below that carries your buffer's path"), not to a compact, so 36.5's widening of the occasion leaves it true.

### Verified ground truth

Every claim under "Ground truth read for this plan" holds against the working tree at `4eb7b0c`: 253 lines; the six-paragraph order of § "Spawn once, message thereafter" (lines 32–95); the three by-name references to the heading (lines 23, 110, 228); the engine as sole home of `.ai-factory/notes/<NN>-architect-buffer.md`; `if it does not exist yet`, `Before that first channel-message`, and `work alone on the unit` each occurring exactly once and only in `agent-architect/SKILL.md` (nothing under `src/`, `docs/`, or CLAUDE.md quotes them); `active/skills/agent-architect → ../../src/skills/agent-architect`; `Skill` already in `allowed-tools`; the tree clean apart from the plan's own untracked files. The worked drafts wrap within 76 columns (measured). `head` occurs 0 times in the file today; the start draft introduces "ahead", so the verification check as worded ("`head` as a name for the architect") is the right one — a word-boundary grep returns 0.

### Review-1 findings — resolved

1. **Snapshot ↔ handoff bridge** — the start draft now reads "a memory snapshot naming a buffer — the handoff below that carries your buffer's path — means you work in that buffer"; the guard explains why the bridge names the artifact and not the occasion; the verification task greps that `handoff` and `memory snapshot` share a sentence. Resolved.
2. **"head" as a second name for the architect** — the "work alone" draft is now "you work alone — holding your buffer, no editor's hand yet — on the unit named"; the guard forbids introducing "head"; the verification task checks for it. Resolved.
3. **"produced it" for the resumed start** — the spawn-moment draft now closes "whichever of the two starts above you came through", with the plan stating the reason (a resumed architect finds the buffer, it does not produce it). Resolved.

### Critical Issues

None.

### Findings

None.

### Positive Notes

- The plan reads the section as one sequence and states the resulting order explicitly in the verification task (start → work alone / spawn → handoff → spawn-moment → liveness → dead editor), so the implementer checks a shape, not just a set of greps.
- Deleting the old engine-load paragraph rather than keeping both is right: two load moments with two timings in one skill body would be exactly the drift the vocabulary contract exists to prevent, and every fact from the deleted paragraph is enumerated as re-homed in the start paragraph.
- The refusal to link `docs/paired-loop.md` from the skill (loaded in projects that do not carry the doc) and the refusal to restate the engine's path/numbering are both correct one-home-per-fact calls.
- Scope fences quote each neighbour's exact anchor from its spec, not from the roadmap line alone.

## Deferred observations

- Affects: `docs/paired-loop.md` § "How the memory begins, and how it survives" / phase 36 (36.4, 36.5) — After this task, an architect with no pointer is "a new architect" and creates a fresh buffer; but § "Spawn once, message thereafter"'s recovery paragraph already anticipates an architect that holds no pointer while a buffer with its handle exists ("recorded into a buffer whose path did not reach you — an auto-compact that fired before any handoff was written, or a handoff addressed elsewhere") and recovers the *handle* from `agent-<id>.meta.json`. In that case the architect now starts a new buffer, then re-addresses the old editor, which (after 36.4) still holds the old buffer's path and re-reads the old settled zone — the pair silently diverges on which file is the shared memory, with nothing crashing. The governing spec assigns the no-pointer case unconditionally to "a new head", so this task implements it faithfully; whether a recovered handle should also lead the architect back to the buffer it was recorded in — or whether 36.5's on-request snapshot is judged to make the window small enough — is a decision for the governing spec, not for this task's file boundary.

PLAN_REVIEW_PASS
