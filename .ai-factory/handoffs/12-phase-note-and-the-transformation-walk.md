# Handoff — the phase note and the transformation walk: four tasks open across two repositories

## 1. Frame

Four planning tasks are written and none is implemented: three in `skills` that give a phase a second tier and rebuild `command-pin-gaps` around it, one in `orchestrator` that lets a run read it — the originating session's context isn't available here; trust these files, not memory.

## 2. Read-first map

**Memory map — read in this order, and read the first one before anything else.**

The architect that wrote these tasks kept a private buffer. It is the recovery file: everything decided this session, why, and what is deliberately left open lives there, along with the state a paired loop needs to resume. This handoff carries the pointer to it and nothing that the buffer holds — the two are not copies of each other.

### Must-read now (minimal rehydration set)

- `.ai-factory/notes/05-architect-buffer.md` — **lead here, start at the section headed `PRE-COMPACT CONSOLIDATION` near the end.** It holds the decisions register (every ruling and its reason), the standing method rules, the open deferrals with their triggers, and the paired-loop state. Everything else in this handoff is orientation around it.
- `.ai-factory/roadmaps/trickster77777.md` — tasks `28.1`, `28.2`, `29.1`, all `- [ ]`, under `### Phase 28` and `### Phase 29`.
- `.ai-factory/specs/trickster77777/102-roadmap-outline-deep.md` — 28.1's spec: the new skill, its format, its guards.
- `.ai-factory/specs/trickster77777/103-pin-gaps-blast-radius-class.md` — 29.1's spec: the transformation walk. Its filename is a fossil of the task's first framing; the file's own title is current.
- `.ai-factory/specs/trickster77777/104-phase-note-readers.md` — 28.2's spec: who reads the phase note.
- `src/global/CLAUDE.md` § "Grounding claims" — the model everything else rests on, and the one surface loaded in every session of every project.

### Read on demand

- `../orchestrator/.ai-factory/handoffs/11-phase-note-reaches-the-run.md` — the brief for the orchestrator-side conversation about task 24.1, including one open question that side must rule on.
- `../orchestrator/.ai-factory/specs/trickster77777/57-prompts-read-the-phase-note.md` and `../orchestrator/.ai-factory/roadmaps/trickster77777.md` — task 24.1 itself.
- `.ai-factory/handoffs/09-...md`, `10-...md`, `11-...md` — the three briefs that shaped `command-pin-gaps`. 09 and 10 are absorbed; 11 is the review brief for 29.1 and is current.
- `docs/sakshi-harness/skill-cycle.md` — the pipeline order, now carrying the new pass between `aif-docs` and `roadmap-decompose`.

## 3. Current state

**Done:**
- `src/global/CLAUDE.md` § "Grounding claims" states the direction change moves in, names the project's `docs/` as the governing spec, separates direction from the order surfaces appear in, and records that tasks execute in file order, one at a time, top to bottom. Committed `13b677a`.
- Four planning tasks written, verified and committed on the skills side as `9bd9426`.
- `docs/sakshi-harness/skill-cycle.md` carries the new pass and its diagram line, written by the planning side before the task that needs it — committed in the same commit.

**In-flight:**
- Nothing is implemented. All four tasks are `- [ ]` and the orchestrator has not run.
- The orchestrator repository is **uncommitted**: its roadmap is modified and spec 57 and handoff 11 are untracked. No permission to commit there was given.

**Uncommitted working-tree state:**
- `skills` — clean at `9bd9426`.
- `orchestrator` — ` M .ai-factory/roadmaps/trickster77777.md`, `?? .ai-factory/specs/trickster77777/57-prompts-read-the-phase-note.md`, `?? .ai-factory/handoffs/11-phase-note-reaches-the-run.md`.

## 4. Next step

Read the buffer's consolidation section first; it answers most of what a fresh reader would otherwise ask.

Then the one concrete thing: **the orchestrator repository has never been committed this session** and holds a modified roadmap plus two untracked files. Ask the user for permission and commit it, or hand it to the applying architect to commit — nothing else is pending on that side. After that, the four tasks are the orchestrator's to implement, in order: 28.1 first, because it defines the `Phase note:` token that 28.2 and 24.1 both consume.

One sequencing constraint that will otherwise bite: 28.1's verification asserts `git diff HEAD -- docs/` is empty. The skill-cycle change is already committed, so that check now passes — but it fails on correct work if that commit is ever unwound.

## 5. Working discipline

- The user rules the forks; the architect decides the clear calls and surfaces the marginal ones crisply. Nothing is applied before findings are discussed.
- Never commit without explicit permission; never push. Two repositories here, and permission for one is not permission for the other.
- Every claim is verified against the file before it is acted on, including claims made by this handoff. Report evidence rather than adapting an order that does not match.
- The full method rules — how to count, how to measure, when to sweep, when to replace a file whole — are in the buffer under "Standing method rules". They were earned by failures listed in § 6 and are not optional.

## 6. Error log

- Three rounds shipped a spec that contradicted itself, each time by replacing an item and leaving the references to it further down the file untouched. A fourth was caught by the paired architect before it landed. The prophylaxis: before changing anything's role, grep the file for its name and read every hit.
- A whole obligation was invented and then defended against — `roadmap-prune` was said to orphan phase notes in `.ai-factory/notes/`, but that skill does not mention that directory at all. The branch was deleted; it returned later, correctly and much smaller, only once the note's destination moved into a directory prune actually owns.
- `roadmap-outline` was said to forbid the pointer form the task uses. It does not: `:40-41` already permits plain markdown links in preamble prose.
- An apply work-order was handed over in the same turn as the relay before it, before the independent second read returned. The order was defective in exactly the way that read would have caught.
- Contract lines shipped at 1021 and 1022 characters against a 400–1000 band because their lengths were estimated rather than measured.
- Six prompt paths and three more in a contract line resolved to nothing — each dropped a package directory. Found by extracting every path and testing it for existence; reading them would not have found it.
- A verification bullet ran `git diff HEAD --stat` unscoped and would have failed on correct work; another checked `git status --short` without `-uall` and could never have passed.
- A batch of string replacements silently matched nothing and left withdrawn text standing. Caught by counting residue afterwards.

## 7. Orientation

- **`103-pin-gaps-blast-radius-class.md` is 29.1's spec, and its filename is stale.** The blast-radius class was the task's first framing; the file's title and body are the transformation walk. Do not infer the task from the filename.
- **Two pointers on a phase header, not interchangeable.** `Governing spec:` states how the phase must become; `Phase note:` states what diverges now.
- **`DEVIATION` and `ESCALATION` are mirror mechanisms, not two strengths of one.** A stale *plan* detail is implemented per the code and flagged, because ground truth outranks a plan. A deficient *governing spec* is the opposite: the spec outranks the code, so the run stops instead.
- **"Unconditional" means "never suspicion-gated", not "must exist".** Where a phase names neither pointer, every prompt behaves exactly as it does today.
- **The orchestrator roadmap has 22.1–22.4 open above our Phase 24.** Pre-existing work, executed first, unrelated to this thread.

## 8. Domain model spine

- **Change moves one way: docs → roadmap → code.** Docs state desired behavior, code states implemented behavior, the roadmap carries the difference. `src/global/CLAUDE.md` § "Grounding claims". Don't re-litigate.
- **The roadmap is the perishable surface** — it goes stale and is pruned, so a task spec may copy a paragraph from a document rather than link to it. The conflicting unqualified rule in § "Documentation style" is a known, deliberately unfixed inconsistency; the buffer records why.
- **The orchestrator never edits `docs/`.** Documentation is written by the planning side before a task runs; a task's file list never carries a `docs/` path.
- **Nothing in the family checks the integration side.** `roadmap-decompose` carries no instruction to read code; `roadmap-decompose-skeleton`'s three lenses all judge testability. That unowned side is what 29.1 claims.
- **No shipped skill or command carries a path into a sibling repository** or depends on one existing.

## 9. Hard rules

- Chat plans; the orchestrator implements. No task's own code is written in a planning session.
- Never commit without explicit permission; never push.
- All files in English regardless of the conversation's language.
- A contract line is 400–1000 characters, measured, never estimated.
- Cross-repo references are written root-relative from the family root — `skills/…`, `orchestrator/…` — and every reader resolves them against that root. Inside the orchestrator repository its own package is `orchestrator/prompts/<name>.md`; the bare `prompts/<name>.md` resolves to nothing.

## 10. Cross-cutting contracts / invariants checklist

- **`Phase note:`** — byte-exact everywhere, capital P, lowercase n, colon. Emitted by `roadmap-outline-deep` in `skills`, read by `roadmap-decompose`, `task-rescue`, and the orchestrator's three prompts. The two sides change in lockstep or not at all.
- **The pointer's path** is repo-root-relative beginning `.ai-factory/`, the same form a `Spec:` tag uses, so `roadmap-prune` joins it onto the target repo root unchanged.
- **The four named owners of a routed hole** are `roadmap-decompose`, `roadmap-decompose-skeleton`, `aif-docs`, `test-philosophy` — each named, none loaded, none invoked.
- **`roadmap-prune` keys its capture on the literal token, never on a link's position**, and never sweeps a `Governing spec:` target.
- **Task order across repositories:** 28.1 defines the token; 28.2 and 24.1 both follow it and are independent of each other.
- **Every finding class reaches both mode branches** of `command-pin-gaps`: the body, the scan-mode line format, and the default-mode report.

## 11. Per-unit map with watch-points

- **28.1 / spec 102 — `roadmap-outline-deep`.** Five paths: the new skill, its `active/` symlink, both `CLAUDE.md` enumerations, one capture in `roadmap-prune`. *Watch:* the two enumerations are the omission task 26.7 already had to repair once; and the spec's status check needs `-uall` or an untracked directory prints collapsed.
- **28.2 / spec 104 — the phase note's readers.** Two files, `roadmap-decompose` hook (a) and `task-rescue`. *Watch:* `task-rescue` carries `Governing spec:` twice in `:61-63`, so any check phrased as "unchanged in count" fails on correct work.
- **29.1 / spec 103 — the transformation walk.** One file, rewritten in place, frontmatter untouched. *Watch:* the spec has carried three framings; look for survivals of the two withdrawn ones — any reference to producing a plan, to a pass bar, or to a sibling repository.
- **24.1 / spec 57 (orchestrator) — the prompts read both pointers.** Three clauses, of which two are byte-identical and the third sits inside a longer sentence. *Watch:* apply the same wording to both identical ones, and do not duplicate what the third already says.
