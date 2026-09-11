# Plan review — 36.2 — the buffer's creation is conditional, and it moves to the architect's own start

## Code Review Summary

**Files Reviewed:** 1 plan + 7 ground-truth files (`src/skills/agent-architect/SKILL.md`, `src/skills/architect-editor-engine/SKILL.md`, `docs/paired-loop.md`, specs 114/117/122/123, the 36.1 review)
**Risk Level:** 🟡 Medium — a single-file prose edit, but the new opening paragraph names the recovery artifact by a word the rest of the file never uses.

### Context Gates

- **Architecture — OK.** `.ai-factory/ARCHITECTURE.md` § "Composition: mechanism vs policy": the plan adds no `loads:` edge, restates none of the engine's content (path, numbering, zones), and keeps the engine-load as a pointer ("where your buffer's path, zones, and rules are defined"). The engine's own "Load this skill once at birth — the architect per the instruction in its own body" still resolves: the instruction stays in the body, only its position and timing move.
- **Rules — WARN (missing optional file).** `.ai-factory/RULES.md` does not exist; `.ai-factory/skill-context/aif-review/SKILL.md` does not exist. Nothing to apply.
- **Roadmap — OK.** Plan title matches `.ai-factory/roadmaps/trickster77777.md` line `- [ ] **36.2 …**`; the contract line's four requirements (conditional rule, engine resident as part of the start ahead of the buffer, handle write stays where it is, spec 117) are all carried by the plan's tasks. The phase note (spec 114) and the governing spec `docs/paired-loop.md` § "How the memory begins, and how it survives" were read; the plan's account of both is accurate ("The memory exists before the hands do", snapshot → resume, no pointer → new head creates first).
- **Neighbour-task collision — OK.** Spec 122 (36.4) anchors to `write its handle into the buffer` and widens "its content *is* the spawn prompt"; the plan keeps both verbatim. Spec 123 (36.5) edits the opening of the handoff sentence and § "On every invocation"; the plan leaves both byte-identical.

### Verified ground truth

Every claim in the plan's "Ground truth read for this plan" section checks out against the working tree at HEAD `4eb7b0c`: the six-paragraph order of § "Spawn once, message thereafter" (lines 32–95), the 253-line length and ~76-column wrap, the three by-name references to the section heading (lines 23, 110, 228), the engine as the sole home of `.ai-factory/notes/<NN>-architect-buffer.md`, the absence of the three quoted phrases anywhere outside `agent-architect`, the `active/skills/agent-architect` symlink into `src/`, the clean tree (only the plan's own two files are untracked), the 36.1 review ending in `REVIEW_PASS` with no deferred observations, and `Skill` already present in `allowed-tools`.

### Critical Issues

None.

### Findings

**1. The new start paragraph names the pointer "memory snapshot"; the file it lands in calls that artifact "handoff" everywhere else, and nothing bridges the two.**
File: plan task "Open § "Spawn once, message thereafter" with the architect's start" — the worked draft and the guard "refers to the pointer generically — 'a memory snapshot naming a buffer'".
`grep -n "handoff\|snapshot" src/skills/agent-architect/SKILL.md` today: six hits for `handoff` (lines 49, 50, 80, 81, 226, 253), zero for `snapshot`. After this plan lands, the architect rehydrating reads § "On every invocation" — "the pre-compact handoff that recorded your buffer's path" — then the new opening paragraph — "a memory snapshot naming a buffer means you work in that buffer; no such pointer means you are a new architect and create your own buffer". The file never says these are the same artifact. Failure scenario: an architect handed a pre-compact handoff that names a buffer does not recognise it as "a memory snapshot", concludes it holds "no such pointer", and creates a second buffer under a new number — exactly the "new one under an old name" the governing spec forbids, and a silent failure (nothing crashes; the memory forks). The skill-body vocabulary rule also bites: within one skill body, one artifact now goes by two names. The plan's fence against 36.5 is right that the paragraph must not tie the pointer to a *compact*; but tying it to the *artifact the file already describes* survives 36.5 unchanged (36.5 widens the occasions the handoff is written on and reworks § "On every invocation" to name the artifact rather than the occasion — it does not stop the handoff being the carrier of the buffer's path). Pin one bridging appositive in the start paragraph, e.g.: "a memory snapshot naming a buffer — the handoff below that carries your buffer's path — means you work in that buffer …". Add to the verification task a grep that `snapshot` and `handoff` are linked in that sentence, or that the paragraph names `handoff` at least once.

**2. The "work alone" reword introduces "head" as a second name for the architect inside a skill body.**
File: plan task "Reword the "work alone" opening" — draft "you work alone — head and buffer, no hand yet — on the unit named".
`grep -n "head\b" src/skills/agent-architect/SKILL.md` → 0 today. "hand" is already the file's own figure for the editor's role (lines 22, 26), so "no hand yet" is in register; "head" is not — `docs/paired-loop.md` uses head/hand as its narrative frame, but `reserved-words.md` fixes `architect` as the registry name, and a skill body calls the concept by that name. The 36.1 review's allowance for "buffer / settled / live / working memory" covered concepts the registry does *not* name; `architect` is one it does. The meaning the plan pins (alone means without a hand, not without state) is right; only the wording drifts. A form that keeps the pinned meaning without the new name: "you work alone — holding your buffer, no editor's hand yet — on the unit named". Wording is the implementer's per the plan; the plan should just remove "head" from the draft so it is not copied verbatim.

**3. (low) "whichever of the two starts above produced it" is inexact for the resumed start.**
File: plan task "Shorten the spawn-moment sentence to the handle write alone" — the draft's closing clause.
A resumed architect does not *produce* the buffer; it finds one the snapshot names. Since the sentence's point is only that the file exists by the spawn moment, a neutral verb avoids the misread — e.g. "a write into a file that exists by then, whichever of the two starts above you came through." Cosmetic, inside the changed sentence, fixable in place.

### Positive Notes

- The scope fences are precise and grounded: each neighbouring task's anchor (36.4's `write its handle into the buffer` and "its content *is* the spawn prompt"; 36.5's handoff-sentence opening and § "On every invocation") is quoted, and the plan verifies against the specs rather than the roadmap line alone.
- The plan correctly refuses to link `docs/paired-loop.md` from the skill (the skill loads in projects that do not carry the doc) and correctly leaves the governing spec unedited — docs → roadmap → code, the doc is already ahead.
- Deleting the old engine-load paragraph rather than keeping both is the right call: two load moments with two timings would be exactly the drift the vocabulary contract exists to prevent.
- The verification task's greps are the right ones (`if it does not exist yet` → 0, `Before that first channel-message` → 0, `write its handle into the buffer` → 1, path absent from `agent-architect`, `git diff --stat` touching one file, frontmatter byte-identical).
