# Plan: command-handoff: boundary-neutral framing + first-class narrative register

## Context
Reframe `command-handoff` so it no longer asserts a `/compact` happened (boundary-neutral) and gains a second, orthogonal **register** axis (skeleton vs narrative) on top of the existing note/chat destination axis. Single file: `src/commands/command-handoff.md`.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Facet A — boundary-neutral framing

- [x] **Task 1: Reword the frontmatter description to trigger by the act, not by `/compact`**
  Files: `src/commands/command-handoff.md`
  Rewrite the `description` block (`:3-7`). Remove the compact-exclusivity phrasing ("the next agent (or yourself after /compact)", "Run this BEFORE /compact", "After compact there is nothing left to mine"). State the trigger by the *act* — transferring context to a future agent/session — and keep the one true timing constraint: mine while the originating session's context is still live, because that is the only moment there is something to mine. Do **not** enumerate boundary kinds (no compact/cross-project/new-session taxonomy) — a taxonomy re-introduces the same over-fit in longer form. Keep the existing note-argument sentence (`"note"`/`"ноут"`/`"давай ноут"`/`"с ноутом"`) intact. While in the frontmatter, also update `argument-hint: "[note]"` to advertise the narrative cue (e.g. `"[note] [narrative]"`) — the register axis (Task 3) introduces explicit cues and this file's frontmatter surface is already being touched. Per spec `.ai-factory/specs/14-handoff-narrative-register-boundary-neutral.md` Facet A.

- [x] **Task 2: Strip compact claims from the Frame skeleton line and the example pointer**
  Files: `src/commands/command-handoff.md`
  Replace the Frame skeleton line (`:54-55`) — "the chat is compacted but the knowledge is durable in files; rehydrate from them, don't trust memory" — with a boundary-neutral line that asserts no compact, e.g. "the originating session's context isn't available here — trust these files, not memory." Replace the example-pointer wording at `:136` ("chat compacted, knowledge is in files") with a boundary-neutral equivalent. After this task, no compact-specific claim survives anywhere in emitted-handoff text or its examples, and no replacement boundary taxonomy is introduced. Verify with `grep -ni "compact" src/commands/command-handoff.md`: `/compact` must not be singled out as the trigger, and it must be absent from the Frame skeleton and example pointer.

### Phase 2: Facet B — first-class narrative register

- [x] **Task 3: Introduce the register axis and its selection heuristic** (depends on Task 2)
  Files: `src/commands/command-handoff.md`
  In the mode-determination block (`:13-18`), add a **register** axis explicitly described as *orthogonal* to the existing note/chat **destination** axis — do not collapse the two into one four-way enum. Define two registers: **skeleton** (state-transfer: many mechanical work-units mid-flight; the existing 11-section skeleton) and **narrative** (understanding-transfer: flowing prose carrying the causal thread to one or two decisions). Selection heuristic: an explicit user cue wins (*narrative / повествование / story*, or a rejection of the numbered form such as "not the numbered skeleton"); otherwise infer from session shape (many mechanical units → skeleton; a reasoning journey → narrative); when genuinely ambiguous, default to skeleton and name the choice. Keep the existing note/chat destination determination unchanged — this task adds a second axis beside it.
  **Reconcile the mining-responsibility paragraph (`:18`).** That paragraph currently states, in destination-only terms, that "in note mode … the agent does not mine the session or populate the skeleton itself here" — true only for skeleton+note. Rewrite it to be register-aware so it does not contradict Task 5: the agent mines and composes **itself** for chat destination (either register) *and* for narrative+note; **only skeleton+note** delegates the mining and population to `note`. This paragraph is inside Task 3's edit block (`:13-18`), so the reconciliation lands here, not deferred. Per spec Facet B, "Selection".

- [x] **Task 4: Add the narrative-register composition guidance to Step 2** (depends on Task 3)
  Files: `src/commands/command-handoff.md`
  In Step 2, add a narrative-register composition path alongside the skeleton one. Narrative = flowing prose (in English) carrying the causal thread: the path walked, the false turns, the decision and its rationale; references to files/specs/notes appear **inline at the moment they are load-bearing**, not catalogued in a separate read-map. It still ends by making the durable next step and the working discipline explicit — woven into the prose, not sectioned away. State that the proportionality principle applies to both registers: a small session yields a short narrative; padding a trivial session to migration-guide length is still a failure. **Guard — skeleton register byte-identical:** do not touch the skeleton's section names/order, the proportionality guard (`:46`), the read-first-map-scoped-to-next-step rule (`:48`), or the self-check gate (`:110`). Add the narrative path around the skeleton, don't rewrite it.
  **Reconcile the second note-mode paragraph (`:108`).** Line 108 ("**Note mode:** do not populate the skeleton here — pass it blank to `note` in Step 3; `note` performs the mining and population itself") is the twin of the `:18` paragraph Task 3 reconciles, keyed on the old destination-only binary — and under narrative+note it is false (the agent composes/populates the prose itself and Writes directly, passing nothing blank to `note`). Rewrite it register-aware, mirroring the `:18` fix: the agent composes/populates itself for chat destination (either register) *and* for narrative+note; **only skeleton+note** passes the blank skeleton to `note` for mining. This paragraph sits inside Task 4's Step-2 edit block, so the reconciliation lands here — it is not one of the byte-identical guards (`:46`/`:48`/`:110`).

- [x] **Task 5: Route narrative output in Step 3 — direct `Write`, not `note`** (depends on Task 4)
  Files: `src/commands/command-handoff.md`
  Extend Step 3 to handle the register × destination combinations. **Narrative + note destination:** the agent composes the prose itself and `Write`s it directly to `.ai-factory/handoffs/<NN>-<slug>.md`, **explicitly not** via `note` — state why: `note` distils, and distillation flattens the exact causal thread the narrative exists to carry. Because there is no `note` call on this path, the numbering mechanic `note` normally owns must be spelled out in the emitted skill text: the agent computes `<NN>` by scanning `.ai-factory/handoffs/` (via the granted `Bash(ls *)`/`Glob`), taking the current max numeric prefix + 1, zero-padded to match existing files; the `<slug>` is derived semantically from the session subject, lowercase hyphen-joined, and ≠ the literal word "handoff". After the direct Write, narrative+note ends with the **same minimal paste-back pointer** the skeleton+note path emits (`:125-139`: path + one-line frame + next step, optionally the work-unit count) — one chat block, not the full prose re-emitted; this stays consistent with the self-check gate at `:110` ("the chat pointer is intentionally minimal … exempt from the proportionality gate"). **Skeleton + note destination:** unchanged — still delegates to `note` with the blank skeleton as the mining lens (and `note` keeps owning numbering there). Both registers may also emit to chat (chat destination) instead of a file. No `allowed-tools` frontmatter change is needed — `Write`, `Skill`, `Bash(ls *)`, `Glob`, and the `note` loader are already present. Per spec Facet B, "Narrative × destination".

## Commit Plan
- **Commit 1** (after tasks 1-2): "Make command-handoff boundary-neutral — drop the hard-coded compact trigger"
- **Commit 2** (after tasks 3-5): "Add the narrative register axis to command-handoff"
