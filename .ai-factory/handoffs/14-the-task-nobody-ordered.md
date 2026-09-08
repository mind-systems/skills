# Handoff — the task nobody ordered, and the provenance field that never asked

## 1. Frame

A week of deleting roadmap tasks for behaviour nobody requested traced to its cause this session: every quality gate the family owns checks a task's *form*, none checks whether it was *commissioned* — and the one field that looks like it records commissioning turns out to be a template constant. The originating session's context isn't available here; trust these files, not memory.

## 2. Read-first map

The session produced two independent work-units. Unit A (this repository) is the live one and its must-read set is below. Unit B lives in the sibling `orchestrator` repository and is cross-linked at the end of each subsection; nothing in B blocks A.

### Unit A — the commission gate (this repository)

#### Must-read now (minimal rehydration set)

- `src/skills/note/SKILL.md:69-92` — the note template ← **lead here.** Line 74 reads `**Source:** conversation context` as a **hardcoded literal**, not a placeholder: every other varying element in that template carries angle brackets (`<Topic Title>`, `<YYYY-MM-DD>`) and this one does not. This single line is the whole finding.
- `src/skills/roadmap-engine/SKILL.md:25-47` — the two-tier artifact. Line 36 delegates the task-spec format to `note` ("The task spec follows `note`'s format — load `note` once per chat"), which is how the constant reaches every task spec in every project.
- `src/skills/roadmap-decompose/SKILL.md:59-70` — hook (b), the Atomicity Gate. The only existing per-entry gate, and it asks one question: "Can the first half be deployed without the second half and still make sense?" That is a question about *size*. A commission gate would be its sibling, at the same moment, asking a different question.
- `src/commands/command-pin-gaps.md:30,42` — read to understand why pin-gaps is **not** the owner. Its docs-branch exists ("**Toward the docs:** behavior the task assumes that no document states … the hole is then in the governing spec, not in the task") but is scoped to a task's *content*, and it disclaims the tier where commissioning would be visible ("The pass does not locate the phase, does not read the pointers on its header").

#### Read on demand

- `src/skills/roadmap-decompose/SKILL.md:24-58,72-102` — hooks (a), (c), (d), the rest of decompose's surface.
- `src/skills/roadmap-engine/SKILL.md:77-121` — the roadmap file format, if the contract-line tier turns out to need anything.
- `.ai-factory/roadmaps/trickster77777.md` — this repo's roadmap; the seam is the `---STOP---` at line 146, with directions through Phase 30 above it.

### Unit B — a run that edits its own governing spec (sibling `orchestrator` repository)

#### Must-read now, if and when B is picked up

- `orchestrator/orchestrator/prompts/implementer.md:126` — Critical Rule 6: "**Ground truth wins over the plan** — implement a stale/wrong plan detail per the file and flag it with `DEVIATION`". This is the habit that generalises wrongly onto documents.
- `orchestrator/orchestrator/prompts/escalation.md` — 4 lines of substance; names "the ratified spec above the current task" as outside an agent's authority, but only for a fork the spec leaves open, never for a spec that is wrong or silent.
- `orchestrator/docs/concepts/context-model.md:35` — "The contract line is the only guaranteed entry point. Everything material to a task must be reachable from it by links."

Paths in this subsection are root-relative from the family root `/Users/max/projects/sakshi`, per the root CLAUDE.md's cross-repo convention.

## 3. Current state

**Done:**

- **Orchestrator task 24.1, its spec 57, and handoff 11 are deleted.** The task ("the prompts read the phase note beside the governing spec") was to extend three prompt clauses to name `Phase note:` beside `Governing spec:`. The user judged it behaviour nobody ordered and had it removed. The roadmap file was restored to `HEAD` with `git checkout --` (the whole block was that file's entire uncommitted change: 10 insertions, 0 deletions), and the two untracked files were deleted outright. Verified after the fact: roadmap diff empty, both files gone, both `---STOP---` markers intact, `orchestrator/prompts/` untouched. Nothing was committed. The orchestrator's spec numbering now has a permanent gap at 57 — leave it.
- **The cause of the week's deletions is diagnosed** (see § 8).

**In-flight — proposals only, none ratified:**

- **A commission gate** (unit A, this repository). Two candidate landing points, both unwritten: make the spec tier's provenance a real answered question rather than `note`'s constant, and give `roadmap-decompose` a per-entry gate beside the Atomicity Gate that refuses a task whose commissioning cannot be named. **The user has not approved either. Do not write them as tasks without asking.**
- **An escalation pair** (unit B, sibling repository). Two prompt-side clauses: extend `escalation.md`'s "ratified spec" clause to cover a governing spec that contradicts the task's target behaviour or fails to cover it; and add a counterpart to `implementer.md`'s Rule 6 stating that where a plan disagrees with the code the code wins, but where a governing spec disagrees with the code the spec wins and the run stops. Also unratified, and lower priority than A by the user's own symptom.
- A third, more aggressive option was raised and **not** adopted: forbid a plan from listing any `docs/` path the task spec does not name. Rejected as too blunt — it would have blocked orchestrator task 8.1, whose spec names `docs/*.md` by glob.

**Uncommitted working-tree state:**

- In this repository: clean at the time of writing. Note that it was **dirty earlier in the same session** (`.ai-factory/notes/06-architect-buffer.md`, `.ai-factory/roadmaps/trickster77777.md`, `.ai-factory/specs/trickster77777/105-rescue-report-persisted.md`, plus an untracked rescue report) and became clean without this session touching anything — another architect is working this repository concurrently. Do not assume exclusive access.
- In the sibling orchestrator repository: only `.ai-factory/notes/01-architect-buffer.md` is modified, which is that session's private architect buffer.

## 4. Next step

Ask the user whether to write unit A as roadmap tasks in this repository, and at which of the two landing points — `note`'s template, `roadmap-decompose`'s gate, or both. Do not draft the tasks first. The user ended this session by choosing a handoff over task-writing, which is a deliberate pause, not an oversight.

If the answer is yes, the decomposition question to settle before anything is written: `note` is a general-purpose distiller loaded by several callers (`roadmap-engine:36` for task specs, `command-handoff` for handoffs, and others), so changing its template changes every artefact it produces, not only task specs. Whether the provenance requirement belongs in `note` at all, or only in the roadmap tier that consumes it, is the fork — and it is a real one, not a formality.

## 5. Working discipline

- **Findings are discussed before anything is applied.** Nothing is written or committed without the user saying so explicitly.
- **Never commit without explicit permission**, and never push.
- **The user rules the forks.** Surface a genuinely marginal call rather than burying it in a task.
- **Chat plans; the orchestrator implements.** In a planning session, only planning artifacts are written — roadmaps, task specs, docs. No application code.
- **Verify every claim against the file, including the claims in this handoff.** A description drifts; the file does not.
- **Test a path by opening it, not by reading about it.** An empty grep against a path that does not exist looks exactly like an empty grep against a path that does.
- All artefacts in English regardless of the conversation's language.

## 6. Error log

- **A grep was run against `src/commands/roadmap-decompose.md`, which does not exist** — the skills live at `src/skills/<name>/SKILL.md`; `src/commands/` holds only three files. The empty result was briefly read as "the field is absent from decompose", which happened to be the correct conclusion reached by an invalid route. **Corrected:** re-ran against `src/skills/roadmap-engine/`, `src/skills/roadmap-decompose/`, `src/skills/roadmap-outline-deep/`; the answer held. A grep whose path is wrong returns the same silence as a grep whose answer is no.
- **Deleted tasks were counted from git history with `git log -p | grep "^-- \[ \]"` and the nine hits on this repository's roadmap were read as deletions.** They are almost all `- [ ]` → `- [x]` transitions and retitles (29.1 appears twice under different titles). **Corrected:** the measurement is impossible in principle — a task deleted before it is ever committed leaves no trace at all, which is exactly what happened to orchestrator 24.1. The cost of the week is invisible to both repositories.
- **An `APPLY-EDIT` work-order was authored whose self-verify step 5 ("`git diff --stat` must show no changed tracked files at all") contradicted its own step 2 and its own guardrail** forbidding any touch of the architect buffer. The editor flagged the contradiction instead of touching the guarded file to force the check green. **Correction for the future:** re-derive an inherited or hastily-written check against the tree it will actually run in.
- **The session's first substantive proposal was a repair to task 24.1** — fixing a `header` / `header or preamble` mismatch in four places of the planning layer. It was a well-grounded repair to a task that should not have existed. The user's question ("what is this task even for?") was the correction, and it arrived only because a person asked it. No gate in the family would have.

## 7. Orientation

- **`**Source:** conversation context` is a constant, not a record.** It appears in 25 of the orchestrator's 26 surviving task specs, which reads like a well-kept provenance discipline and is nothing of the kind — it is copied from `note`'s template, where it is a fixed literal. This is worse than the field being absent: an absent field prompts a question, a pre-filled one silences it. The deleted spec 57 was one of the only two without it, and it lacked it because there was genuinely nothing to name.
- **"The task assumes undocumented behaviour" and "the task was never commissioned" are not the same hole.** pin-gaps owns the first. Nothing owns the second. The wording is close enough that the second keeps looking like it is already covered.
- **`DEVIATION` and `ESCALATION` are not two strengths of one signal.** For a *plan*, ground truth outranks the artefact and the agent implements per the file (`implementer.md:126`). For a *governing spec*, the artefact outranks the code and the run must stop instead. Reaching for the first mechanism where the second applies is how a run ends up editing its own specification.
- **Every gate the family owns is a gate on form.** Two-tier shape, the 400–1000 character contract line, pinned values, a `Verify` section, the Atomicity Gate's split question. All of them make an unordered task *better*. None of them makes it *not exist* — pin-gaps would have sharpened 24.1 by closing its unreachable path, producing a more implementable task that still should not have been written.
- **This repository is worked by more than one architect at a time.** `.ai-factory/notes/06-architect-buffer.md` belongs to another session. Its working tree changed underneath this session without this session touching it.

## 8. Domain model spine

- **Change moves one way: docs → roadmap → code.** The documentation states desired behaviour, the code states implemented behaviour, and the roadmap carries the difference between them. The corollary is the whole finding: **if no document ever promised the behaviour, there is no difference to carry, and the task has no source.** Deleted task 24.1 is the specimen — its commissioning source was an asymmetry noticed in a sibling repository ("that side grew a token, this side does not read it"), which is a true observation and not a commission. Its spec could name no document of its own repository, which is precisely why it reached across the repository boundary instead. Don't re-litigate; the evidence is `orchestrator/docs/concepts/context-model.md`, which says nothing about a phase note.
- **A discovered asymmetry is auto-promoted to a task, and nothing intervenes.** The step from "here is a gap" to "therefore it must be closed" is taken silently, at decomposition time, by the planning side — not by the orchestrator run. A ban on the run writing documentation would not have prevented a single one of the week's deletions.
- **A task spec's paths must resolve from the run's own working directory.** Every orchestrator agent is launched with `cwd = project_dir` (`orchestrator/orchestrator/agents.py:427,472,524,576`), so a cross-repo path written root-relative from the family root — `skills/src/...` — resolves to nothing during a run. This is a live rule with no home; it was found via spec 57 and outlived it. The family root convention in the root `CLAUDE.md` is for a reader standing at that root, which a run never is.
- **A task spec that copies a paragraph from a document instead of linking to it is not a defect** at this tier — the roadmap is the perishable seam between documentation and code, and the copy earns its place because an agent does not reliably walk to a leaf. This is stated in `src/commands/command-pin-gaps.md` and matters directly to any commission gate: the gate must ask for a *source*, never forbid the restatement.

## 9. Hard rules

- Never commit without explicit permission; never push.
- All files in English regardless of the conversation's language.
- Never write to agent memory unless the user uses an explicit trigger phrase.
- Tasks route by ownership: skills/commands/agent-definitions/planning-discipline → this repository's `.ai-factory/`; pipeline/prompts/sidecars/orchestrator code → the sibling's. The family root never hosts tasks.
- A planning artefact that names a new abstraction carries the language's own interface marker in the name.

## 10. Cross-cutting contracts / invariants checklist

- **`**Source:** conversation context`** — today a byte-exact literal at `src/skills/note/SKILL.md:74`. Anything that makes it load-bearing changes `note`, and `note` is a shared load-once engine with several callers (`roadmap-engine:36` for the task-spec format, `command-handoff` for handoffs). Its blast radius is every artefact `note` produces, not only task specs. Enumerate the callers before touching it: `grep -rl "note" src/skills/*/SKILL.md src/commands/*.md`.
- **The Atomicity Gate's question stays a question about size.** If a commission gate is added at hook (b), it is a second gate beside the first, not a widening of it — "can this be split" and "was this asked for" fail differently and must be answerable separately.
- **pin-gaps stays code-side.** Its remit is a task's landing on the code that exists; the commission question belongs upstream at decomposition. Do not push it into pin-gaps because its docs-branch superficially resembles it.
- **The orchestrator's spec numbering has a permanent gap at 57.** Do not renumber, do not reuse.
- **The orchestrator roadmap has two `---STOP---` markers.** The first is the seam.

## 11. Per-unit map with watch-points

- **`src/skills/note/SKILL.md`** — untouched this session. *Became:* identified as the true origin of the false provenance field, at line 74. *Watch:* it is a general distiller, not a roadmap skill; a requirement written into it lands on handoffs and research notes too, which may not be wanted. Decide the tier before editing.
- **`src/skills/roadmap-decompose/SKILL.md`** — untouched. *Became:* identified as the moment a commission gate would fire, beside hook (b). *Watch:* hook (b) fires *after* an entry's full spec is drafted and before its contract line is written. A commission gate that fires there has already paid for the spec; whether it belongs earlier, at hook (a), was not settled this session.
- **`src/commands/command-pin-gaps.md`** — untouched. *Became:* ruled out as owner, on its own text. *Watch:* it genuinely does carry a docs-branch routing to `aif-docs`; a future reader will find it and conclude the case is covered. It is not — the branch audits a task's content, never its existence.
- **Orchestrator task 24.1 / spec 57 / handoff 11** — deleted, verified. *Watch:* the sibling repository's own handoffs 12 and 13 and its architect buffers 05 and 06 still reference 24.1 and spec 57 as live work. Those are that repository's historical session records and were deliberately left alone; a reader meeting them should know the task is gone, not resurrect it.
- **Orchestrator commit `8bef0c5` (task 21.3)** — not modified, cited as evidence. *Became:* the proof that a run will edit its own governing spec. It rewrote invariant 5 of `orchestrator/docs/concepts/fault-handling.md` and a paragraph above it, changing a notification's contract from "names where the account is" to "never where to find it". *Watch:* its own spec 54 names that document only in a `**Source:**` line and mandates no edit to it in `## The change`, `## Guards`, or `## Verify` — so the run authored that change unprompted. Anyone re-examining unit B should start here rather than re-deriving it.
