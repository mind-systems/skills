# Plan: 17.2 — The "new work" coupling: one dictionary in the authoring skills

## Context

Retire the two remaining synonyms for registry concepts across the "new work" authoring flow: `milestone` → **phase** (outline, whose product is `### Phase N`) or **task** (decompose/skeleton, whose product is `N.M`), and `spec note` / bare artifact-`note` → **task spec**. Naming-only conformance per the governing spec [reserved-words](../../docs/reserved-words.md); zero behavior change. Three files in the task's set (`agent-architect`, `editor.md`, `command-pin-gaps`) are certifications — they land no edit.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Assumptions & pinned decisions

Grounded by a fresh grep of all seven files (2026-07-18); line numbers and line lengths below are measured against the live files, not the spec's 2026-07-13 inventory.

1. **Line counts frozen; no rewrapping anywhere, and some lines end up long.** `roadmap-outline`, `roadmap-decompose`, `roadmap-decompose-skeleton` are hard-wrapped ~85–88 cols; `aif-docs` uses long unwrapped lines. Every file's line count must be identical pre/post — 17.1's landed discipline (its review confirmed 315→315 / 84→84).
   The substitutions are **not** uniformly length-preserving, and the plan accepts the resulting raggedness deliberately:
   - Length-neutral: contiguous `spec note` → `task spec` (9→9), and the split-across-lines variant where `spec`→`task` and `note`→`spec` are both 4 chars (`roadmap-decompose:29–30`).
   - Shortening: `milestone` → `task` (−5 per site) — leave the line short.
   - **Lengthening**: bare `note` → `task spec` (+5 per site) and Task 3's line-6 rewrite (+7). Measured post-edit widths: `roadmap-decompose:6` ~100, `:79` 90, `:81` 92; `roadmap-decompose-skeleton:122` ~96, `:123` 94, `:126` 95.
   These six lines are **left long and unwrapped**. Rewrapping them would push text across line boundaries, move every downstream line number, and defeat the frozen-count gate — a cosmetic wrap column is not worth that. `roadmap-decompose:6` is already a 93-char outlier in its own block, so it is not even a new anomaly.

   **Scope of the directive:** no task rewraps a folded frontmatter block, and no task reflows a multi-line paragraph in a way that shifts its line count or moves downstream line numbers. It is not a ban on any word ever crossing a line break: Task 2 is the one **pinned, count-preserving exception**, where both replacement lines are given byte-for-byte and the pair stays two lines (78 and ~69 chars, both inside the file's ~85 wrap). Apply Task 2's pinned bytes exactly — do not "restore" the original wrap point.
2. **`Spec:` is a tag, not a noun.** The on-disk tag `` `Spec:` `` stays byte-identical everywhere. Where prose reads "a `Spec:` note" meaning *the artifact*, the noun becomes `task spec`; where it means *the tag itself*, the noun is dropped. Both forms occur — the exact rewrite for each site is pinned in the tasks below rather than left to judgment.
3. **Bare-note sweep is scoped to edited files** (spec 63 § Guards). `command-pin-gaps` is certified no-change by the spec, so its `` `Spec:` note file `` (line 17) is **not** touched by this task. Recorded as an observation for the reviewer, not silently expanded.
4. **`**Note:**` at `aif-docs:41` is the ordinary English word**, not the artifact — leave byte-identical. It is the *only* legitimate `\bnotes?\b` survivor across the four edited files (verified: none of the four contains a backticked `` `note` `` skill reference, and all three roadmap skills declare `loads: roadmap-engine` / `roadmap-engine test-philosophy` — `note` appears in no `loads:` value here).
5. **Word choice only.** Grain and register of `description:` fields belong to Phase 14 (task 14.1), which explicitly re-verifies against these post-17.2 descriptions. Do not level altitude here.
6. **Two tasks may touch one line.** Where a later task's quoted pre-edit text overlaps a line an earlier task already changed, the tasks are marked "apply both" on that line. An implementer must match against the *current* state of the line, not the quoted original.

## Tasks

### Phase 1: The flagship — `roadmap-outline`

- [x] **Task 1: outline `description:` — product is phases, trigger stays**
  Files: `src/skills/roadmap-outline/SKILL.md`
  Line 3: `Create or update a project roadmap with major milestones.` → `...with major phases.` The word `"milestones"` inside the same line's `Use when user says "roadmap", "project plan", "milestones", or "what to build next".` trigger list **stays byte-identical** — the contract binds output naming, never user input, and this is the only such trigger in the task's file set. Frontmatter `name:` / `argument-hint:` / `allowed-tools:` / `loads:` / `disable-model-invocation:` untouched.

- [x] **Task 2: outline body — `spec notes` → task specs** (depends on Task 1)
  Files: `src/skills/roadmap-outline/SKILL.md`
  Lines 40–41 currently read: `Links to handoff/spec notes are allowed as plain markdown links inside the intro/` / `preamble prose — no formal `Spec:` tag, no invented notes.` Rewrite to name the two genres plainly: `Links to handoffs and task specs are allowed as plain markdown links inside the` / `intro/preamble prose — no formal `Spec:` tag, no invented task specs.` The `` `Spec:` `` tag stays byte-identical. Keep two lines; the wrap point moves within the pair (`intro/` shifts from the end of 40 to the start of 41) but the line count does not change. This is the pinned exception named in Assumption 1 — apply the two replacement lines exactly as given; neither is long (78 and ~69 chars).

### Phase 2: The unit-producers — `roadmap-decompose`

- [x] **Task 3: decompose `description:` — the unit is the task** (depends on Task 2)
  Files: `src/skills/roadmap-decompose/SKILL.md`
  Three substitutions inside the folded `>-` block (lines 4–8). Note the block's live wrap: `with` is the **last word of line 5**, and line 6 begins `the full spec…` — quote each edit against its own line only.
  - Line 4: `Create or update a project roadmap with atomic, granular milestones. Each roadmap` → `...with atomic, granular tasks. Each roadmap` (−5).
  - Line 6, matching the line-6 text alone (`  the full spec persisted as a note, rendered per roadmap-engine's format. Use when user says`): `the full spec persisted as a note` → `the full detail persisted as a task spec`. This mirrors the engine's own landed description (`roadmap-engine:5` — "contract line plus a full task spec written via note") and avoids the redundant "spec persisted as a task spec".
  - Line 8: `milestones that need to be implementation-ready.` → `tasks that need to be implementation-ready.` (−5).

  **Pinned, overriding nothing — this is the one site where the question arises:** line 6 goes 93 → ~100 chars and is **left long and unwrapped.** Do not rewrap the folded block, do not redistribute words across lines 4–8. The block stays 5 lines and every other line keeps its current break. (Per Assumption 1; line 6 is already the block's 93-char outlier.)
  The `Use when` list already says "break down tasks / spec tasks / create tasks" — no trigger word changes.

- [x] **Task 4: decompose body — `milestone` → `task`** (depends on Task 3)
  Files: `src/skills/roadmap-decompose/SKILL.md`
  Five sites: line 17 `every milestone is a two-tier entry` → `every task is a two-tier entry`; line 41 `mark already-completed milestones as `[x]`` → `already-completed tasks`; line 75 `expand a vague milestone into a full spec` → `a vague task`; line 83 `If the milestone bundles 2+ independent concerns` → `If the task bundles`; line 92 Critical-Rule heading `1. **Milestones are atomic and specific**` → `1. **Tasks are atomic and specific**`. All five shorten by 5 — do not rewrap. **Line 83 is also edited by Task 5 — apply both.**

- [x] **Task 5: decompose body — `spec note` and the bare artifact-`note` sweep** (depends on Task 4)
  Files: `src/skills/roadmap-decompose/SKILL.md`
  The `spec note` sites (all length-neutral): line 18 `a full spec note, rendered per` → `a full task spec, rendered per`; the **wrapped** site at 29–30 (`...plus a full spec` / `note per `roadmap-engine`'s format...`) → line 29 ends `...plus a full task`, line 30 begins `spec per` — 4→4 chars on both lines, so no downstream line number moves; line 93 `a contract line in the roadmap plus a spec note,` → `plus a task spec,`.
  Then the bare-note sweep (spec 63 § Guards) over the same file — each of these names the task-spec artifact:
  - Line 78 heading `Note-handling rule:` → `Task-spec-handling rule:`.
  - Line 79 `update the named note in place with `Write`` → `update the named task spec in place with `Write`` (85 → 90 chars, left long).
  - Line 81 `write a new note per `roadmap-engine`'s format` → `write a new task spec per ...` (87 → 92 chars, left long).
  - Line 83 `(a split → two notes` → `(a split → two task specs`. **Task 4 also edits this line (`If the milestone bundles` → `If the task bundles`) — apply both.**

  Leave byte-identical: the `` `Spec:` `` tag (79, 82) and every backticked `` `roadmap-engine` `` reference.

### Phase 3: The splitter — `roadmap-decompose-skeleton`

- [x] **Task 6: skeleton — `milestone` → `task`** (depends on Task 5)
  Files: `src/skills/roadmap-decompose-skeleton/SKILL.md`
  Seven sites, each −5: 96 `one "contract" milestone` → `one "contract" task`; 98 `the impl milestone turns them green` → `the impl task turns them green`; 102 `own standalone shared-scaffold milestone` → `...shared-scaffold task`; 122 `it becomes the **impl** milestone` → `the **impl** task`; 124 `are now separate milestones` → `are now separate tasks`; 125 `Insert** the new skeleton/TDD/contract milestones` → `...contract tasks`; 130 `to number the inserted milestones` → `the inserted tasks`. Do not rewrap.
  **Lines 122 and 124 are also edited by Task 7 — apply both.** On line 124 the two edits are net length-neutral (−5 here, +5 there).

- [x] **Task 7: skeleton — `spec note`, `Spec:` note, and the bare-note sweep** (depends on Task 6)
  Files: `src/skills/roadmap-decompose-skeleton/SKILL.md`
  `spec note` sites (length-neutral): 35 `(contract line + spec note)` → `(contract line + task spec)`; 117 `(contract line + spec note) for each resulting task` → same substitution; 127 `orphaning its spec note.` → `orphaning its task spec.`
  Bare-note sweep, applying Assumption 2 per site. **Match against the post-Task-6 state of lines 122 and 124, not the text quoted here** — Task 6 has already replaced `milestone(s)` with `task(s)` on both:
  - 122 `contract line and a `Spec:` note` → `contract line and a `Spec:`-tagged task spec` (the artifact; 89 → ~96, left long). **Apply on top of Task 6's `**impl** milestone` → `**impl** task` on this line.**
  - 123 `line and note **in place** (update the note's content to reflect...)` → `line and task spec **in place** (update the task spec's content to reflect...)` (the artifact, twice; 84 → 94, left long).
  - 124 `do not render a second contract line or a new note for` → `...or a new task spec for` (the artifact). **Apply on top of Task 6's `are now separate milestones` → `tasks` on this line.**
  - 126 `mirrors `roadmap-decompose`'s in-place note-update discipline` → `in-place task-spec-update discipline` (90 → 95, left long; attributive hyphenation is ordinary English and stays). This is the paired half of Task 5's rename of the same discipline in `roadmap-decompose` — the two sides move in lockstep.
  - 132 `its contract-line text and `Spec:` note tag stay unchanged` → `its contract-line text and `Spec:` tag stay unchanged` — here `note tag` means the **tag**, so the noun is dropped rather than substituted.

  Every `` `Spec:` `` literal stays byte-identical. Line count 148 → 148.

### Phase 4: `aif-docs`

- [x] **Task 8: aif-docs line 70 — the two tokens, nothing else** (depends on Task 7)
  Files: `src/skills/aif-docs/SKILL.md`
  Single line, two substitutions: `gather the target behavior from the stated user intent, spec note, or ROADMAP milestone if one is discoverable` → `...from the stated user intent, task spec, or ROADMAP phase if one is discoverable`. `milestone` → **phase** here (not task): aif-docs' governing spec is phase-scoped, named on the phase header. The file is unwrapped, so length is a non-issue.
  Leave byte-identical, deliberately: lines 26 and 182 — `"this milestone"` inside the no-history forbidden-phrase detection lists (`"we changed"`, `"was added"`, `"this milestone"`). These are **mentions** — a phrase the skill scrubs from generated docs — not a naming of a roadmap unit; rewriting them would change behavior by making the detector miss the phrase it exists to catch. Line 41's `**Note:**` is the ordinary English word (Assumption 4). The existing `governing spec` spellings are already conformant. The two-doc-mode doctrine (Phase 13) is out of scope — do not touch aif-docs' semantics.

### Phase 5: Certification and verification

- [x] **Task 9: certify the three audit-clean files land zero edits** (depends on Task 8)
  Files: `src/skills/agent-architect/SKILL.md`, `src/agents/editor.md`, `src/commands/command-pin-gaps.md`
  Assert, do not assume — these files are in the task's set as a certification. Run `rg -U -in 'spec\s+notes?|milestones?' src/skills/agent-architect/SKILL.md src/agents/editor.md` → expect **zero** (rg exit 1). For `command-pin-gaps.md`, confirm `contract line` (17) is already conformant, `"Named roadmaps"` (17) is a quoted section-title reference to `roadmap-engine`, and `field types` (21) is generic. Expected outcome: `git diff --stat` shows these three files **unchanged**. Note for the reviewer: `command-pin-gaps:17` carries `` its `Spec:` note file `` — a bare artifact-`note`, but the file is not edited by this task, and spec 63 scopes the bare-note sweep to edited files. Out of scope here; surface it rather than expanding.

- [x] **Task 10: run the spec's verification gates** (depends on Task 9)
  Files: (no edits — verification only)
  Run each gate from spec 63 § Verification and record the result:
  - `rg -U -in 'spec\s+notes?' src/skills/{roadmap-outline,aif-docs,roadmap-decompose,roadmap-decompose-skeleton}/SKILL.md src/commands/command-pin-gaps.md` → **zero**. Multiline-tolerant (`-U`) on purpose: the single-line form returns a false zero over the live wrap at `roadmap-decompose:29–30`.
  - `rg -U -in '[^-]milestones?' src/skills/{roadmap-outline,roadmap-decompose,roadmap-decompose-skeleton,aif-docs}/SKILL.md` → **exactly 3 matching lines**, falling into 2 exempt categories: `roadmap-outline:3` (the user-trigger word) and `aif-docs:26` + `aif-docs:182` (the detection-list `"this milestone"`, one line each — `rg` reports per line, so the two categories yield three hits). Baseline before the edits is 18 matching lines. Three hits is a **pass**, not a failure; anything else is a real finding.
  - `rg -U -in '\bnotes?\b' src/skills/{roadmap-outline,roadmap-decompose,roadmap-decompose-skeleton,aif-docs}/SKILL.md` → **exactly one matching line: `aif-docs:41`** (`**Note:**`, the ordinary English word). No other survivor is legitimate: none of the four files contains a backticked `` `note` `` skill reference and none names `note` in a `loads:` value (Assumption 4). Any second hit is residue to fix, not a category to wave through.
  - Byte-stability gates: `git diff` shows **no** change to any `name:` / `loads:` / `allowed-tools:` / `argument-hint:` frontmatter value, no change to any `` `Spec:` `` or `Governing spec:` tag, no change to any `.ai-factory/specs/` path literal, and no reverse-graph marker touched.
  - `wc -l` per file identical to the pre-edit baseline: outline 75, aif-docs 271, decompose 97, skeleton 148, and the three certified files unchanged.
  - Behavior gate (static, per 17.1's precedent — a headless live render is impossible): confirm by reading that `roadmap-outline` still instructs `### Phase N` headers, `roadmap-decompose` still renders `**N.M — Name**`, and `aif-docs`' governing-spec genre instructions are untouched. A rename that changes an artifact's shape is a bug.
