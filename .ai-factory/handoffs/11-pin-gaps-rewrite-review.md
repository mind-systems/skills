# Handoff — review the pin-gaps rewrite: task 29.1 and the skill it rewrites

## 1. Frame

We are rewriting one file, `src/commands/command-pin-gaps.md`, so that it walks the transformation a task claims — this governing spec, through this task, into that code — and reports every point where the three fail to join; the task that does it is still uncommitted and still movable — the originating session's context isn't available here; trust these files, not memory.

## 2. Read-first map

### Must-read now (minimal rehydration set)

- `src/commands/command-pin-gaps.md` — the 26-line file being rewritten, and the only thing the task touches ← lead here. Frontmatter `:1-12`; target resolution `:17`; the premise `:19`; value holes `:21`; meaning holes `:23`; scan-mode line format `:25`; default-mode report `:26`.
- `.ai-factory/specs/trickster77777/103-pin-gaps-blast-radius-class.md` — the task spec: what the rewrite must produce, what it must not, and how it is verified.
- `.ai-factory/roadmaps/trickster77777.md` — task `29.1` under `### Phase 29`, state `- [ ]`; the contract line is the spec's header.
- `src/global/CLAUDE.md` § "Grounding claims" — the direction change moves in, docs → roadmap → code, and the walk down named references to the leaf. This is everything the command needs in order to know what a joined task looks like, and it is resident in every session of every project.

### Read on demand

- `src/skills/roadmap-decompose/SKILL.md` and `src/skills/roadmap-decompose-skeleton/SKILL.md` — the two skills that build tasks. The first carries no instruction to read code at all; the second reads it only through three testability lenses. Between them the integration side is unowned, which is the gap this task claims.
- `.ai-factory/handoffs/09-pin-gaps-blast-radius-class.md` — the first request: add a blast-radius finding class. Absorbed into 29.1; read it for what the class is and the downstream incident that produced it.
- `.ai-factory/handoffs/10-pin-gaps-must-be-the-final-readiness-gate.md` — the second request, from another session: the command should be the final line under a task. Substantially absorbed, and the framing it proposed has since been withdrawn; read it only to argue the absorption was wrong.

## 3. Current state

**Done:**
- The global CLAUDE.md now states the direction change moves in — docs → roadmap → code — names the project's `docs/` as the governing spec rather than a description, separates that direction from the order the surfaces appear in, and records that tasks execute in file order, one at a time, top to bottom. Committed as `13b677a`.
- Phase 28 / task 28.1 with spec `102-roadmap-outline-deep.md`: a second pass that gives a drafted phase a note and a short contract-line preamble. Committed as `aa16bbd`.

**In-flight:**
- Phase 29 / task 29.1 with spec 103. It has carried three framings. It began as "add a blast-radius finding class"; that was absorbed when the class proved a real capability but not the answer. It then became "rehearse the orchestrator's plan and plan-review", and that framing was withdrawn: it aimed the command at producing a plan rather than checking a task, and it put paths into a sibling repository inside a command that ships everywhere. The current framing is the transformation walk. Read the files, not this description of them.

**Uncommitted working-tree state:**
- ` M .ai-factory/roadmaps/trickster77777.md` — the Phase 29 block
- ` M .ai-factory/notes/05-architect-buffer.md` — a private buffer, never edited from outside
- `?? .ai-factory/specs/trickster77777/103-pin-gaps-blast-radius-class.md`
- `?? .ai-factory/handoffs/10-...md` and `?? .ai-factory/handoffs/11-...md`

Nothing under `src/` has been touched. The task is unimplemented by design; the orchestrator builds it in a separate run.

## 4. Next step

Review two things together and report findings; change nothing, write nothing.

**The task.** Is 29.1 answerable as written? Would a planner holding only its contract line and spec have to invent anything? Does its Verification section contain a check that cannot fail, or one that must fail on correct work? Do its Guards contradict its change items — this thread produced that exact defect three times, always by replacing an item and leaving the references to it further down the file untouched. And does anything survive from either withdrawn framing?

**The skill.** Take the rewrite the spec describes and ask whether the file it produces would do the job: a command that reads a task, reads the documents the task and its phase name, reads the code the task will land in, and reports every point where the three fail to join — desired behavior that lands nowhere in the code, and behavior the task assumes that no document states. It holds no power to fix what it finds beyond what it can pin into the artifact in place, and it carries no path into a sibling repository, because it runs in projects that have none.

## 5. Working discipline

- Verify every claim against the file, including the claims in this handoff. A description drifts; the file does not.
- Count phrases against a whitespace-normalized read, and normalize `**` out of both sides before comparing a quoted span. A line-oriented `grep` returns 0 for any phrase spanning a hard wrap, and an exact-match check over markdown fails on emphasis inside the quoted span. Both produced false results in this thread.
- Never state a line number or a count without reading it off disk in the same breath. Predicted counts were wrong five times; measured ones never were.
- Findings are discussed before anything is applied. Nothing is written or committed without the user saying so.

## 6. Error log

- Three rounds shipped a spec that contradicted itself: an item was replaced and the bullets referring to it were not swept. The prophylaxis that works: before changing anything's role, grep the file for its name and read every hit.
- A whole obligation was invented and then defended against: `roadmap-prune` was said to orphan phase notes in `.ai-factory/notes/`, but that skill does not mention that directory at all. The branch was deleted, and returned later — correctly and much smaller — only once the note's destination moved into a directory prune actually owns.
- `roadmap-outline` was said to forbid the pointer form the task uses. It does not: `:40-41` already permits plain markdown links in preamble prose.
- A quotation was assembled from real and invented fragments; another round asserted the contents of a file that had not been opened. Both were caught by counting, not by reading.
- A contract line shipped at 1021 characters against a 400–1000 band because its length was predicted instead of measured.
- Three sibling-repository paths shipped in the spec that resolved to nothing — each dropped the package directory. Found by extracting every path a file names and testing each for existence, not by reading them.
- A batch of string replacements in this very handoff silently matched nothing and left the withdrawn framing in place. Caught by counting residue afterwards; fixed by rewriting the file whole.

## 7. Orientation

- **The command's question is its identity; the verdict is not.** It asks one thing — where would the implementing agent have to invent? Everything the rewrite adds exists to make that question answerable. A pass/fail verdict must not displace the finding list.
- **It walks a transformation; it does not produce a plan.** The command is not a planner and not a reviewer of plans. Any wording that has it emit a plan, or hold to another agent's pass bar, is drift from a framing that was withdrawn.
- **A hole has two ends and either may be reported.** Toward the code: desired behavior that lands nowhere. Toward the docs: behavior the task assumes that no document states, because it surfaced during decomposition rather than specification — that one is not the task's defect, and the governing spec is where it is repaired.
- **It names owners and wields none.** A task that cannot be planned coherently belongs to `roadmap-decompose` or `roadmap-decompose-skeleton`; behavior no document describes belongs to `aif-docs`; a silently-failing surface owes a test by `test-philosophy`'s discriminator. Naming an owner requires no `loads:` edge.
- **A blast-radius hole is not a scope boundary.** A scope boundary says what the task must not touch; a blast radius says what the change breaks whether the task touches it or not.

## 8. Domain model spine

- **Change moves one way: docs → roadmap → code.** Docs state desired behavior, code states implemented behavior, the roadmap carries the difference between them. Ratified into `src/global/CLAUDE.md` § "Grounding claims". Don't re-litigate.
- **The roadmap is the perishable surface.** It goes stale and is pruned; the other two persist. That is why a task spec may copy a paragraph out of a document instead of linking to it — the copy has a bounded lifetime, and an agent that would not have walked to the leaf reads it anyway. `command-pin-gaps` already works this way: `:21` pins the exact value with a `file:line` citation, `:23` writes the constraint as a spec clause citing its code. Neither links.
- **The global CLAUDE.md's § "Documentation style" still says a fact's second home is always a link, never a copy**, with no exception stated for the roadmap tier. Known conflict with the point above; raised, deliberately not fixed.
- **Nothing in the family checks the integration side.** `roadmap-decompose` carries no instruction to read code; `roadmap-decompose-skeleton`'s three lenses — skeleton, tests-first, concurrency contract — all judge whether behavior can be verified, never where new code meets old. That unowned side is what this task claims.
- **The command ships everywhere.** It is symlinked into `~/.claude/commands` and invoked in projects that have no sibling repository beside them. A path into one resolves inside this coordination root and nowhere else.

## 9. Hard rules

- The frontmatter gains nothing: no `Write`, no `AskUserQuestion`, no `Agent`; `loads:` stays `roadmap-engine`. If a capability appears to need one of them, it has been written as an action instead of a finding.
- No path into a sibling repository appears in a shipped skill or command, and no rule in one may depend on that repository existing.
- The file stays a command in `src/commands/`; it is not promoted to a skill.
- The repair verb is `Grep` or `rg`, never bare `grep` — `:10` grants no `Bash(grep *)`.
- Chat plans; the orchestrator implements. No task's own code is written here.
- All files in English regardless of the conversation's language.
- Never commit without explicit permission; never push.

## 10. Cross-cutting contracts / invariants checklist

- **Every finding class must reach both mode branches**: it exists in the body, appears in the scan-mode line format at `:25`, and is countable by the default-mode report at `:26`.
- **The frontmatter `description:` is contract, not summary** — always loaded, so a capability absent from it is one the invoking agent may never learn exists. The walk belongs in it, not only in the body.
- **Every class's paragraph has the same shape**: a bold name, the definition of what it looks for, then `Repair:`.
- **The four named owners are `roadmap-decompose`, `roadmap-decompose-skeleton`, `aif-docs`, `test-philosophy`** — each named in the body, each checked in Verification, none loaded and none invoked.
- **Comparative judgments are seat-bound.** Judging a task too large, and judging a behavior undocumented, need the neighbouring tasks' costs and knowledge of what other phases' documents cover; from inside one task every task looks normal-sized.
- **Phase and spec numbering are file-wide and historic.** Phase numbers never restart and gaps are legal; a spec number is the highest in its directory plus one.

## 11. Per-unit map with watch-points

- **`src/commands/command-pin-gaps.md`** — it stays a 26-line command that gains the transformation walk and a third finding class, and gains no powers. *Watch:* every line of it is load-bearing; `:19`'s premise and `:26`'s report are the two most likely to be left silently inconsistent with a new capability; `:10` and `:11` must come out byte-unchanged; and the string `orchestrator/` must not appear in it at all.
- **Task 29.1 and spec 103** — *watch:* the spec has carried three framings. Look for sentences surviving from either withdrawn one, for any reference to a plan, a pass bar, or a sibling repository, and for Verification bullets whose expected counts no longer match the body they check.
- **Phase 28 / spec 102, committed** — `roadmap-outline-deep`, a second pass over drafted phases. *Watch:* not part of this review; touch neither.
