# Plan: 28.2 — the phase header's two pointers get their readers: `roadmap-decompose` and `task-rescue`

## Context
Task 28.1 minted the `Phase note:` pointer on the phase header and nothing reads it; `task-rescue` reads only `Governing spec:`, and `roadmap-decompose` reads no phase preamble at all. This task gives both pointers their readers in those two skills, in one unconditional shape.

Both tokens are protocol tokens under the root CLAUDE.md § "Protocol tokens are a different axis" — matched literally, byte-identical wherever produced or consumed. `Phase note:`'s form is pinned in `src/skills/roadmap-outline-deep/SKILL.md:104-108` (capital P, lowercase n, colon); `Governing spec:` has no format home in `src/` and is matched as the literal it already is at `task-rescue/SKILL.md:61`, `:541` and `roadmap-outline-deep/SKILL.md:114`.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### `roadmap-decompose` — the phase-preamble read

- [x] **Add the phase-preamble read to hook (a) Granularity**
  Files: `src/skills/roadmap-decompose/SKILL.md`
  In hook (a) Granularity (`:26-44`), add a paragraph — placed after the numbering/flat-fallback text (ending `:38`), before the "Two parity carry-overs" list (`:40`) — instructing: before the phase's first entry is drafted, read the phase preamble; where the header or preamble names `Governing spec:` documents or a `Phase note:`, read those files in full first. State it as unconditional, never suspicion-gated, in the same register `task-rescue/SKILL.md:61-63` already uses. Keep the two pointers apart in the wording, per the spec: the governing spec states how the phase must become, the phase note what diverges now. Match both tokens literally, byte-exact.

- [x] **State the read's unit and where a preamble can be present** (depends on Add the phase-preamble read to hook (a) Granularity)
  Files: `src/skills/roadmap-decompose/SKILL.md`
  The same paragraph must state its own unit, because `roadmap-engine` applies hook (a) per entry (`roadmap-engine/SKILL.md:189` the create-mode draft, `:242` inside the **Add** action): the read runs **once per phase**, at the moment that phase's first entry is drafted, **in whatever mode the draft runs** — never once per entry, and never re-run for later entries of a phase already read. State the unit mode-independently, as the contract line does ("in every mode"), and let the enumeration name the sites where a preamble can actually be present: the create-mode draft cycle as re-run by the update menu's **Rewrite** over an existing `$TARGET_FILE` (`roadmap-engine/SKILL.md:248-250`), the **Add** action (`:241-242`), and hook (d) "Decompose existing" (`:73`) for the target task's phase. Do **not** name first-run create mode as a site: `roadmap-engine/SKILL.md:152-154` enters it only when `$TARGET_FILE` does not exist, and `:35-38` forbids inventing a phase header, so no preamble can exist there — the flat-fallback exit covers it. State the exits: under the flat fallback (no phase headers, `:35-38`) there is no preamble to read; where the preamble names neither pointer, proceed as today. State that a named file that is absent is reported to the user as a finding, never skipped silently. Do not add a `loads:` edge and do not touch the frontmatter — reading a file named on a phase header is a read, not a skill invocation.

### `task-rescue` — both pointers at all five sites

- [x] **Widen the Step 1 read and its title** (depends on State the read's unit and where a preamble can be present)
  Files: `src/skills/task-rescue/SKILL.md`
  `:58` — the bolded step title "**Read the phase's governing spec.**" names both pointers (e.g. the phase's governing spec and phase note). `:61-63` — the check extends from a `Governing spec:` reference alone to `Governing spec:` documents and a `Phase note:`, keeping the shape word-for-word in substance: read every named file in full before proceeding to Step 2, unconditional and not suspicion-based; and the existing exit stays — if the task is under no phase, or neither pointer is named, proceed as today. The trailing sentence about the read being additive to Step 4's `$TARGET_FILE` resolution stays. `Governing spec:` stays at this site — the second pointer joins it, never replaces it.
  **Absent-file landing, decided here:** a named file that does not exist is told to the user at Step 1 *and* carried into the Diagnosis Report as a finding — never skipped silently. Both destinations are stated in the edit, so the finding survives the gap between Step 1 and the report `:150-151` makes a first-class deliverable.

- [x] **Extend the Step 3 judgment to the note, with its consequence** (depends on Widen the Step 1 read and its title)
  Files: `src/skills/task-rescue/SKILL.md`
  At `:143-148` ("When a governing spec was read in Step 1, judge the recurring findings against it…"), let the phase note stand beside the governing spec as a baseline a finding is judged against — the governing spec says how the phase must become, the note what diverges now.
  **The consequence, decided here rather than left to the implementer:** the note's participation is observable in the output. Extend the Diagnosis Report duty at `:147-148` with one clause — where a finding matches a divergence the phase note already records, the report says so and names it as already-recorded divergence. And pin the routing effect explicitly: such a finding is *not* by itself a "specification gap" (the divergence is known and ratified at the phase tier), so it does not on its own drive the Step 4 depth choice (`:150-151`) toward inventing a new decision — the repair target is the task spec failing to carry what the note already stated, mirroring the root-cause/repair-target distinction already at `:145-146`. The existing governing-spec duty is unchanged: the report still states whether the failure violates the governing spec and quotes the relevant clause.

- [x] **Extend the Step 5 no-wholesale-copy rule** (depends on Extend the Step 3 judgment to the note, with its consequence)
  Files: `src/skills/task-rescue/SKILL.md`
  At `:355-357` (depth: spec, item 1 — "If a governing spec was read in Step 1, do not copy its content into the task spec wholesale — quote/restate only the clauses implicated by the findings"), widen the subject to cover both files read in Step 1, governing spec and phase note alike, with the quote/restate-only constraint unchanged.

- [x] **Extend the `## What NOT to do` rule** (depends on Extend the Step 5 no-wholesale-copy rule)
  Files: `src/skills/task-rescue/SKILL.md`
  At `:539-543` ("Do not issue a semantic diagnosis, blocker, or spec repair without having read the phase's `Governing spec:` documents when the phase names them…"), extend to both pointers in the same unconditional shape — never suspicion-gated — keeping the stated reason (otherwise the ratified spec tier does not participate in the rescue at all) and adding the note's own stake: without it the rescue never sees what the phase already recorded as diverging.

- [x] **Leave `:227` alone, deliberately** (depends on Extend the `## What NOT to do` rule)
  Files: `src/skills/task-rescue/SKILL.md`
  The escalation option menu at `:227` ("Decision belongs elsewhere (a neighboring task / the governing spec) — point there and reset") is the one remaining `governing`-mention in the file and stays byte-identical. It names the governing spec as the *authority an unmade decision belongs to*, not as a file the Step 1 read fetched, and a phase note — which records what diverges now — is never where an unmade decision lands. This reasoning is recorded here in the plan, which is where a run's reasoning belongs; the step produces no edit to any file — not to `task-rescue/SKILL.md`, and not to the task spec or any other artifact under `.ai-factory/`. It exists so a later sweep of this file (26.9/26.10 each landed one instance short) finds the exclusion already reasoned.

### Verification

- [x] **Verify against the spec's checks** (depends on Leave `:227` alone, deliberately)
  Files: `src/skills/roadmap-decompose/SKILL.md`, `src/skills/task-rescue/SKILL.md`
  Take every count on a whitespace-normalized read of the named file, never a line-oriented `grep`: `Phase note:` appears at least once in `roadmap-decompose/SKILL.md` and at least twice in `task-rescue/SKILL.md`, byte-exact; `Governing spec:` still appears at both `task-rescue` sites (the Step 1 read and the `## What NOT to do` rule). By reading, not by count: decompose states the read's unit mode-independently, names Rewrite, Add and "Decompose existing", and names no first-run create site; rescue's Step 1 title names both pointers, the Step 3 judgment carries the note into the Diagnosis Report, the Step 5 copy rule names the phase note, the absent-file branch is stated in both skills with its destination, and `:227` is unchanged. Finally `git diff HEAD --stat -- src/ active/ docs/ CLAUDE.md` lists exactly the two `SKILL.md` files and nothing else — no `active/` symlink change, no doc edit, no other skill (`roadmap-outline-deep`, `note`, `roadmap-engine`, `roadmap-outline`, `roadmap-prune` all stay untouched).
