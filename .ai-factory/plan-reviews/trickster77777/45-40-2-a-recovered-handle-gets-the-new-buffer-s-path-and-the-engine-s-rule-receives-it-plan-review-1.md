## Plan Review Summary

**Plan:** `.ai-factory/plans/trickster77777/45-40-2-a-recovered-handle-gets-the-new-buffer-s-path-and-the-engine-s-rule-receives-it.md`
**Files Reviewed:** 6 (plan, task spec 129, `src/skills/agent-architect/SKILL.md`, `src/skills/architect-editor-engine/SKILL.md`, `src/agents/editor.md`, `docs/paired-loop.md`) plus the roadmap line, phase 40 header, spec 131 (40.4) and the origin deferred observation in review `34-36-2`.
**Risk Level:** 🟡 Medium

### Context Gates

- **Architecture** — `.ai-factory/ARCHITECTURE.md` present. The plan keeps the engine/lens split intact: the engine (`architect-editor-engine`) widens one mechanism sentence and gains no policy; the lens (`agent-architect`) gains policy only and references the mechanism by heading rather than restating it. No new `loads:` edge, no inlining of engine content. Aligned.
- **Rules** — `.ai-factory/RULES.md` absent. WARN (non-blocking, optional file).
- **Roadmap** — Task 40.2 sits directly at the seam of `.ai-factory/roadmaps/trickster77777.md` (40.1 `[x]`, 40.2 first `[ ]`); the plan heading matches the contract line; the plan's boundary (recovery paragraph + engine re-read sentence only; respawn paragraph left to 40.6; `editor.md` left to 40.3; the engine's buffer section left widened for 40.4 to anchor beside) matches spec 129 and the ordering spec 131 depends on. Governing spec `docs/paired-loop.md` is the one the phase header names, and the plan leans on its § "What crosses the channel" and § "How the memory begins, and how it survives" correctly. Aligned.

### Grounding check

Every anchor the plan uses is by name (paragraph-opening strings, heading names), and each resolves against the files as they stand: the recovery paragraph opens "Continue in the same conversation if the editor is still alive." and ends "…the id is the filename segment between `agent-` and `.meta.json`."; the next paragraph opens "If the send fails, the editor is dead"; the engine's sentence "The editor re-reads the settled zone when it changes, not once at birth." stands alone as its own paragraph in § "The architect's buffer"; line counts 320 / 45 are correct; `editor.md` and `docs/paired-loop.md` say what the plan says they say. The DEVIATION-style reading of the spawn sentence ("a later round sent via `SendMessage` never repeats it") is sound — the recovery naming carries a *different* path, so no conflict — and the plan rightly requires the new text to make that plain.

### Critical Issues

None that block on their own, but one missing step below must be closed before implementation.

### Issues

1. **Missing step — the recovered handle never reaches the new buffer.** (`src/skills/agent-architect/SKILL.md`, task 1, item 1.)
   The governing spec states the address exchange as symmetric: § "How the memory begins, and how it survives" — "Each half holds the other's address. At the moment a hand joins, its own address is recorded in the memory, and the memory's place is given to the hand in turn." The plan pins only the second half (the buffer's place goes to the hand). The first half has no home on the recovery path: the handle-write paragraph binds the write to "At the moment you spawn the editor", and recovery is not a spawn; the buffer section lists "the editor's handle" as state the buffer holds but times it "above", i.e. at the spawn. So an architect that follows this plan creates buffer B, names B to the recovered editor, and never records the recovered handle in B. The next snapshot then carries B's path, B holds no handle, and the very next recovery falls into the metadata fallback again — the same window this task exists to close, reopened one compact later.
   **Fix (within the plan's own boundary — the same recovery paragraph):** item 1 states that the recovered handle is written into your own new buffer in the same act as the naming — the write the spawn moment already makes, now made at recovery too — pointing at the handle-write paragraph by concept, not restating it. The guardrail "leave the handle-write paragraph byte-identical" stays as is; the new sentence lives in the recovery paragraph, which is what the spec bounds the edit to.

2. **Verification command as written will fail.** (task 1, "Verify with `grep -n "recovered\|own buffer" …` … sits inside the recovery paragraph and nowhere else".)
   `own buffer` already occurs in the conditional buffer rule: "you are a new architect and create your own buffer first" (verified: the grep hits that line today, before any edit). The "nowhere else" expectation is therefore wrong, and an implementer applying it literally would either report a false failure or "fix" the conditional rule the plan orders byte-identical. Replace the probe with a string unique to the new text (e.g. `recovered`, which has zero hits today) or state the one pre-existing hit as expected.

3. **Two framings of the recovered architect's identity in one instruction.** (task 1, item 1.)
   The item says both "you are a new architect" (the conditional rule's own framing, which must stay) and "the editor you recovered was spawned by an earlier run of this architect". An implementer writing to both cues can produce a sentence that claims lineage identity the conditional rule denies, and the engine's "An editor reads only its own architect's buffer" reads differently under each. Pin one: the editor was spawned by an architect whose buffer did not reach you; you are a new architect, and the re-pointing is precisely what makes that editor your hand — holding your buffer, not the one that spawned it. The plan's own resolution already implies this; the instruction should say it once.

### Positive Notes

- Anchors are all names — paragraph openers and headings — and every one resolves; nothing addresses by position.
- The plan correctly separates the two halves of one act across the two files (sending side in the lens, receiving side in the engine) and forbids restating either in the other — the exact engine/lens discipline ARCHITECTURE requires.
- The "why not the alternatives" requirement is carried faithfully from the spec with both alternatives and their reasons named, and it references "Losing the editor is never fatal; losing it silently is the defect" by pointing at it rather than editing the paragraph that holds it.
- Ordering with 40.4 and 40.6 is explicit and respected; the frontmatter `description:` assumption is sound — the rule keeps its name, only its coverage widens.

## Deferred observations

- Affects: `docs/paired-loop.md` § "What the memory holds, and who holds it" / the final `aif-docs` verification pass — after this task the engine's re-read sentence states more than the governing spec's own sentence at the same place ("The editor re-reads the settled zone when it changes, not once at birth"). The doc carries the meaning elsewhere (§ "How the memory begins": "the head names the moment that memory moves"; § "What crosses the channel": "naming that the shared memory has moved"), so no contradiction, but the doc's own re-read sentence is now the narrower of the two homes. Spec 129 keeps the doc unedited, so this is not a finding here; docs → code direction suggests the doc's sentence should widen when the doc is next touched.
- Affects: task 40.3 / `src/agents/editor.md` — "the spawn prompt gives you the buffer's own path — held from birth" describes the spawn moment only; once the engine's widened rule lands, the path the editor holds can be replaced by a naming inside a later message. Not false, since the engine is loaded at birth and governs, but the sentence reads as if the path were fixed. 40.3 edits the paragraph directly below it and could bring this clause level in passing, or leave it.
- Affects: governing spec `docs/paired-loop.md` § "How the memory begins, and how it survives" / phase 40 follow-up — the conditional rule closes "Either way the buffer exists before any editor does", and the doc says the same ("creates its own buffer first, and only then takes on a hand"). On the recovery path this task pins, an editor exists before the new buffer does; what stays true is that the buffer exists before the architect *addresses* a hand. Spec 129 keeps the conditional rule byte-identical, so nothing to do here; the wording is a candidate for the doc when it is next revised.
