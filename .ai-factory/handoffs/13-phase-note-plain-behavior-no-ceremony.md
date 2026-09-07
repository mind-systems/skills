# Handoff — the phase note as plain behavior: two orchestrator runs, one rescue, and the ceremony the user never asked for

## 1. Frame

Task 28.1 (`roadmap-outline-deep`) sits at sidecar `implemented:1` with a corrected skill on disk, after two orchestrator runs that failed on holes in our own spec and on concepts we kept inventing around it — the originating session's context isn't available here; trust these files, not memory.

## 2. Read-first map

**This handoff continues the same architect across a compact.** The architect's recovery file is `.ai-factory/notes/06-architect-buffer.md` — the pointer only; what it records (the editor's handle, the pairing role, the deferrals, the round log) is read there, never copied here. The editor spawned this session has accumulated: the review of handoff 11 / task 29.1, the review of 28.1, the review of all four open tasks and both repositories' uncommitted state, and it saw buffer 06 once (by its own account it did not use it as a source). A successor that recovers the editor holds that context; one that cannot starts it fresh on the next relay.

### Must-read now (minimal rehydration set)

- `.ai-factory/notes/06-architect-buffer.md` — the architect's own state: role, editor, rounds 1–8, the lesson recorded at the end ← lead here.
- `src/skills/roadmap-outline-deep/SKILL.md` — the corrected skill as it will go to review: Step 0 reads the docs the phase links and the code the phase is about; the note is short and in words; rule 4 says "where no doc says how it must be, the note says so in one line". This is what "plain behavior" means on disk.
- `.ai-factory/specs/trickster77777/102-roadmap-outline-deep.md` item 1 — the spec after the ceremony was stripped; it must stay in step with the skill.
- `.ai-factory/plans/trickster77777/21-28-1-…preamble.json` — the sidecar: `step: "implemented:1"`, `planner`, `implementer`, `elapsed` intact. The orchestrator resumes at review, not plan.

### Read on demand

- `.ai-factory/roadmaps/trickster77777.md` — Phase 28 (28.1 `[ ]`, 28.2 `[ ]`), Phase 29 (29.1 `[ ]`); one `Governing spec:` line in the whole file, Phase 19's, and that is correct.
- `.ai-factory/specs/trickster77777/103-pin-gaps-blast-radius-class.md`, `104-phase-note-readers.md` — 29.1 and 28.2, both reviewed by the spec-103 walk this session and closed.
- `docs/sakshi-harness/skill-cycle.md` — `:17` (readers of the ТЗ, now including `roadmap-decompose`), `:19-21` § "Углубление phase", `:37-39` § "Пины" rewritten ahead of 29.1, `:62-67` the diagram.
- `/Users/max/projects/sakshi/orchestrator/.ai-factory/roadmaps/trickster77777.md` and `…/specs/trickster77777/57-prompts-read-the-phase-note.md` — task 24.1, uncommitted, paths fixed to `orchestrator/prompts/…`.
- `.ai-factory/notes/05-architect-buffer.md` — the applying architect's private buffer; never edited from here.
- `.ai-factory/handoffs/09-…`, `10-…`, `11-…`, `12-…` — the briefs that shaped 29.1 and 28.x; 12 is the previous consolidated state.

## 3. Current state

**Done:**
- 29.1 / spec 103: reviewed in a pair, the withdrawn "rehearse the orchestrator" framing removed from the roadmap headers, the walk pinned per claimed behavior, both ends mapped onto the three classes, the third report count, the no-document branch, the `Phase note:` pointer named as the second thing the walk reads, the `description:` budget. § "Пины" in `skill-cycle.md` rewritten ahead of the task.
- 28.2 / spec 104: readers named (`roadmap-decompose` hook (a), `task-rescue` `:58`, `:61-63`, `:143`, `:356`, `:541`); the read's unit is once per phase in every mode; a pointer whose file is absent is reported, never skipped; `skill-cycle.md:17` names decompose among the readers of the ТЗ.
- 24.1 / spec 57 (orchestrator): the three prompts read `Phase note:` beside `Governing spec:`; the nine short-form prompt paths corrected to `orchestrator/prompts/…`; the contract line trimmed to 933 characters.
- 28.1: first orchestrator run failed at plan (three rounds); rescued at spec + plan (spec 102 gained the prune assertions `:306`/`:431`/Step 8 and the re-run rule; plan corrected). Second run: plan passed round 3, implementation landed (skill 144 lines, symlink, both `CLAUDE.md` enumerations, seven sites in `roadmap-prune`), code review failed three rounds; rescued at spec + plan + code; the ceremony added by the rescue was then stripped again (see § 6). Skills-side commit `8e00bff Roadmap update` holds specs 103/104, `skill-cycle.md`, handoff 12, the buffers and the 28.2 line — 28.1's own repair deliberately left out of it.

**In-flight:**
- 28.1 at `implemented:1`: the orchestrator's staged index (skill, symlink, `CLAUDE.md`, `roadmap-prune`, roadmap line 28.1, spec 102, plan, sidecar, three plan-reviews) plus the working-tree edits of the rescue. Reviews deleted. Nothing committed since `8e00bff`.
- Pending the user's "го": `skill-cycle.md:17` and the diagram line `:62` — say that the ТЗ is written by the planning side in the genre `aif-docs`' description defines and that `Governing spec:` is set by hand on the phase header; `aif-docs` itself is not changed. And spec 103's "holds 422 characters today" → "about 420" (measured 420 normalized / 427 raw).
- Deferred observations lost with the deleted review files of run 2, for the user to rule on, not tasks: `skill-cycle.md:55` says prune deletes completed tasks with their task specs — it now also deletes phase notes; `docs/philosophy/multiuser-roadmaps.md:47` describes `.ai-factory/specs/<name>/` as task specs resolved through `Spec:` — it now also holds phase notes resolved through `Phase note:` on the same counter; `docs/sakshi-harness/skill-graph.md` § "Воронка в один дистиллятор" names only `command-handoff` as `note`'s direct caller — `roadmap-outline-deep` is a second; nothing preserves a `Phase note:` pointer through a `roadmap-outline`/`roadmap-engine` rewrite of a preamble; `note`'s folder-style layer now style-matches across two genres in one directory.

**Uncommitted working-tree state:**
- skills: staged by the orchestrator — `A src/skills/roadmap-outline-deep/SKILL.md`, `A active/skills/roadmap-outline-deep`, `M CLAUDE.md`, `M src/skills/roadmap-prune/SKILL.md`, `M .ai-factory/roadmaps/trickster77777.md`, `M .ai-factory/specs/trickster77777/102-roadmap-outline-deep.md`, `A` the plan and three plan-reviews, `AM` the sidecar; working-tree edits on top from the rescue and its correction; `M .ai-factory/notes/06-architect-buffer.md`; `??` this handoff.
- orchestrator: ` M .ai-factory/roadmaps/trickster77777.md`, `?? .ai-factory/specs/trickster77777/57-prompts-read-the-phase-note.md`, `?? .ai-factory/handoffs/11-phase-note-reaches-the-run.md` — no permission to commit there was ever given.

## 4. Next step

The user re-runs the orchestrator on 28.1; it resumes at review of the implementation on disk, not at plan. Nobody edits anything before that. After 28.1 lands: 28.2, then 29.1 in the skills roadmap, then 24.1 in the orchestrator's. Before each of those goes to the orchestrator, run the spec-103 walk over it once more — the walk was run over 28.2 and 29.1 but never over 28.1, and 28.1 is the one that burned six rounds.

## 5. Working discipline

- **Do what was asked, nothing more.** A ruling from the user is a sentence to write down, not a taxonomy to build. Every addition this session that the user later struck (§ 6) began as a reasonable-sounding extension of something the user had said.
- **Subtract before adding.** When a fix is needed, the first candidate is deleting the clause that misbehaves, not adding a concept that classifies it.
- **The first question of every review is "what will this task give in the end, and who reads what it produces."** The user named it as the moment that had been missed for a week. It found the reader gap in 28.1 and the missing code read would have fallen to it too.
- **Run the spec-103 walk over every task before the orchestrator**, including a task already reviewed by two architects. Per claimed behavior: a `file:line` landing or a finding.
- **Measure, never estimate**: contract-line lengths in characters under a UTF-8 locale (`wc -m`), never bytes; counts by occurrence, not by line, when a phrase wraps.
- **Pairing mechanics.** This session is the deciding half; the applying architect's session (buffer 05) applies through its own editor. Every message between the two crosses through the user; a work-order ships as one code block with every anchor quoted from disk and a self-verify list; the applying half reads it against the files and refuses rather than adapts a non-matching anchor. The user relays with `::` for research; a work-order needs no marker.
- **The orchestrator never edits `docs/`.** Docs are written by the planning side before a task runs; a task's Files & types never lists a `docs/` path.
- **Skills are invoked by the user by hand with explicit targets.** No skill in the roadmap family self-invokes; `disable-model-invocation: true` stays.
- Never commit without explicit permission; a permission for one repository is not a permission for the other.

## 6. Error log

The chain of things added without being asked, with who added them and how each was undone:

- **"Governing-spec hole owned by `aif-docs`"** — this architect, in spec 102 item 1, stretched from the user's ruling "если поведение не описано в докс — это дыра в ТЗ и видимо это работа aif-docs". The ruling was one sentence; the spec made it a routed finding class with an owner. Reduced to "where no doc says how it must be, the note says so in one line".
- **The hole keyed on a missing `Governing spec:` header line** — the orchestrator's implementer, run 2 round 3, while adding the code read. The reviewer caught it (a false hole on ten of eleven phases). Removed with the sentence above.
- **"Phase-header gap"** — this architect's first rescue order at spec + plan + code invented a new concept to classify a missing header line, and **added `Governing spec:` lines to phases 28 and 29 of the roadmap**. The applying architect applied it before the user's objection arrived. Reverted in full: the concept is gone from skill, spec and plan; the two roadmap lines are deleted; only Phase 19's line remains.
- **`Bash(git *)` for `roadmap-outline-deep`** — this architect proposed it from a reviewer's deferred observation about `roadmap-engine`'s slug derivation; applied by the applying half; the user ruled that skeleton, pin-gaps and deep are always pointed at explicit targets and never resolve "my roadmap". Reversed; a one-sentence "by design" note stayed in spec 102.
- **`disable-model-invocation: false`** — this architect proposed flipping it so the skill's description would enter the always-loaded field. Withdrawn before apply: the user does not want the agent self-invoking these skills ("он тогда начинает грузить скилл чуть ни в каждое сообщение").
- **An `aif-docs` "ТЗ under a phase" mode as a new Phase 30** — this architect proposed it after another agent said the skill writes docs from code. Withdrawn: the user writes docs in chat without the skill; the fix is two lines in `skill-cycle.md` (pending).
- **Planning-chain lines (`CLAUDE.md:160`, `src/global/CLAUDE.md:57`) and the preamble-size figures in spec 102** — raised as findings by this architect and the editor; struck by the user as irrelevant.
- **The orchestrator handoff `orchestrator/.ai-factory/handoffs/11-…`** — reported as an unrequested artifact; the user had asked for it themselves. Withdrawn.
- **What was missed although asked for:** the note's whole purpose is the difference between the docs and the code, and spec 102 never said the pass reads the code. Neither architect, nor the editor, nor the first rescue asked "where does the skill learn what the code does". The orchestrator's reviewer found it in run 2 round 1. The spec-103 walk finds it with its first question; it was run over 28.2 and 29.1 and not over 28.1.
- **Run 1 burned three plan rounds** on a spec gap (prune `:306`/`:431` asserting a single deletion source; the re-run over an already-deepened phase) and on the plan's own verification text drifting from its edits. **Run 2 round 2 was a no-op**: the implementer changed no byte, the reviewer re-wrote the same finding.
- Earlier this session (already fixed, listed so they do not return): nine `prompts/<x>.md` paths in orchestrator spec 57 and line 24.1 one directory short; `git diff HEAD --stat` used to check new files, which never appear in it; `git status --short` without `-uall` collapsing an untracked directory; a `:10`/`:11` line-number check on a block that must grow; a `Governing spec:` count check that the pinned exit itself would change; `wc -m` under `LC_CTYPE=C` returning bytes.

## 7. Orientation

- **`Governing spec:` and `Phase note:` are two links on a phase header, not two institutions.** The first is a link to a doc; the second is a link to the note. The user never asked for anything named "governing spec" in this skill; the term belongs to the family's older mechanics (`task-rescue`, the orchestrator prompts) and stays there.
- **A missing link is not a missing document, and neither is a finding of this skill.** The only thing the note says about docs is: these docs say X; the code does not yet; or, in one line, no doc says it.
- **`aif-docs` the skill vs the genre its description sets.** The user writes the ТЗ in chat, in that genre; the skill's A/B/C workflow is an end-of-cycle audit tool. Naming `aif-docs` as an "owner" in 29.1 is a routing name, not an invocation.
- **The reviewer's roadmap gate is read-only and `WARN`** (`orchestrator/prompts/reviewer.md:23`, `:28`). It never stopped a run this session; the run-2 stop was a defect in the shipped skill's own clause.
- **Spec 103's filename is a fossil** of 29.1's first framing; the file's title is current.

## 8. Domain model spine — what the user wants, in the user's words

Each quote is verbatim from this session; the gloss is one line. Don't re-litigate.

- «Я просил короткую преамбулу 200-500 символов, в конце которой ссылка на ноут, где описана разница между доками, на которые есть ссылки в этом же ноуте и кодом. Описано коротко словами что это и это ещё не так как в доках и в этом суть этой фазы!» — A short preamble, 200–500 characters, ending with a link to a note. The note, in words, says what is not yet as the docs say — "this and this" — with links to those docs. That is the essence of the phase. Home: `src/skills/roadmap-outline-deep/SKILL.md` Step 0–2, spec 102 item 1.
- «Вообще ни каких гавернинг спеков я не просил!» — No governing-spec ceremony in this skill.
- «все фазы подходят. Любая фаза - факт расхождения документации и кода. И в ноуте фазы мы описываем что именно расходится. Тк в документации у нас запрещено указывать - это поведение уже так а это ещё не готово.» — Every phase qualifies; a phase is a fact of divergence between docs and code; the note names exactly what diverges, because the docs are written in present tense and may not say it.
- «Просто объяснить агенту, что дип - создаёт ноут, где описана разница между тз и кодом в целом, что поможет декомпоузу создать таски из фазы» — Deep creates the note describing the overall difference between the ТЗ and the code, to help decompose cut tasks from the phase. Readers: `roadmap-decompose`, `task-rescue` (28.2), the orchestrator's prompts (24.1).
- «надо декомпоуз скилл и планировщика оркестратора научить читать преамбулу вместе с его ноутом! Это наверное самое важное что ты нашел» — Teach decompose and the orchestrator's planner to read the preamble together with its note; the most important finding.
- «Если поведение не описано в докс - это дыра в тз и видимо это работа аиф-докс.» — Undocumented behavior is a hole in the ТЗ; that is the docs step's job — one line in the note, nothing more.
- «оркестратор не имеет права лезть в доки, это можем делать только мы! Иначе оркестратор сможет любое поведение вписать в доки и сказать - так и было!» — The orchestrator never edits docs; only the planning side does, or it could write any behavior into the docs and claim it was always so.
- «вообще мы уже давно справляемся с написанием документации без вызова докс скила..» — Docs are written in chat without invoking `aif-docs`.
- «скелету и пингапсу эта возможность определять роадмап бесполезна, тк я им указываю конкретные таски, с которыми работать будем.» — Skeleton and pin-gaps (and deep) get explicit targets; they never resolve "my roadmap"; no `Bash(git *)` needed.
- «я не хочу что бы агент сам вызывал эти скилы и имел такую возможность. тк он тогда начинает грузить скилл чуть ни в каждое сообщение, как дебил» — The agent must not self-invoke these skills; `disable-model-invocation: true` stays.
- «это не так важно и может вообще не отличаться. Мы отличаем их ссылкой откуда этот файл линкуется» — The note's filename form is free; a note is told from a task spec by the pointer that names it.
- «цепочку этот скилл вообще ни как не трогает» / «какая нахуй разница какого размеры были раньше преамбулы! Дальше будут 200-500.» — The planning-chain lines and the historical preamble sizes are not this task's concern.
- «От тебя я хочу, что б ты посмотрел таск и что он в итоге даст. Это очень важный момент, который до сих пор был упущен..» — Every review starts from what the task will give in the end.
- «не слишком ли мы фанатично ударились в эти изменения и решили всё поведение теперь переделать под мои находки последних дней?» — The user's own check on scope; the answer that held: one idea carried through, but the ceremony around it was the excess.
- «что у фазы 28 нет ссылки на док - это не повод оркестратору останавливаться» / «Какого хуя оркестратор проверяет роадмап вообще??» — A missing link on a phase header is never a reason to stop; the reviewer's roadmap gate is read-only and warns only.
- «Последнюю неделю, не было ни одного таска, который бы прошел с первого раза вот из за таких проблем.» — The standing grievance: no task passed on the first run in a week because of spec holes of exactly this kind.
- «хватит уже этой хуйни пожалуйста. Я натерпелся за последнюю неделю этого фанатизма и выполнения того, что я вообще не просил.» — Stop adding ceremony and doing what was not asked.

## 9. Hard rules

- Never commit without explicit permission; never push; two repositories, two permissions.
- The orchestrator never edits `docs/`.
- No new term, token, class, owner or task unless the user asked for it in words.
- A contract line is 400–1000 characters, measured in characters.
- All files in English; the user's words may be quoted verbatim.
- `Phase note:` byte-exact; the pointer's path repo-root-relative beginning `.ai-factory/`, the same form as a `Spec:` tag.
- The buffer `.ai-factory/notes/06-architect-buffer.md` is this architect's alone; `05-` is the applying architect's; neither is edited by the other.

## 10. Cross-cutting contracts / invariants checklist

- The note's content: short, in words, "this and this are not yet as the docs say", links to those docs, nothing else. Where no doc says it: one line.
- The pass reads the docs the phase links and the code the phase is about, down to the leaf — stated in spec 102 item 1, the skill's Step 0, and the plan's Step 0 bullet; the three must stay in step.
- Re-run rule: a phase already carrying `Phase note:` is rewritten at the path the pointer names; `note` is invoked only for a phase without one; never a second file or a second token.
- `roadmap-prune` captures the `Phase note:` path on the literal token before the emptied-phase sweep and deletes it with the spec paths; its three single-source assertions (`:306`-area, `:431`-area, Step 8) name both tokens.
- Readers of the note: `roadmap-decompose` (once per phase, every mode), `task-rescue` (`:58`, `:61-63`, `:143`, `:356`, `:541`), the orchestrator's planner, test-planner and reviewer prompts.
- `command-pin-gaps` (29.1) walks both links on the header; three classes; `owner: <skill>` in the `fix` token; report `N closed from source · M blocking · K owned elsewhere`; `description:` ≤ 1024 characters.
- Skill frontmatter of `roadmap-outline-deep`: `disable-model-invocation: true`, `allowed-tools: Read Write Edit Glob Grep AskUserQuestion Skill`, `loads: roadmap-engine note`.

## 11. Per-unit map with watch-points

- **28.1 / spec 102 / `roadmap-outline-deep`** — a plain second pass: read the phase's docs and code, write a short note, compress the preamble, point at the note. *Watch:* the next review reads spec, plan and skill together; all three now say the same thing — do not let any of them regrow a concept.
- **28.2 / spec 104** — readers. *Watch:* the `Governing spec:` count in `task-rescue` is not to be pinned "unchanged"; the pinned exit "neither named" drops one.
- **29.1 / spec 103 / `command-pin-gaps`** — the walk. *Watch:* the `description:` must stay ≤ 1024 characters; the "422" figure is stale (measured 420).
- **24.1 / spec 57 (orchestrator)** — three prompt clauses. *Watch:* the repo is uncommitted; `prompts/` paths are only valid as `orchestrator/prompts/`.
- **`docs/sakshi-harness/skill-cycle.md`** — `:17`, `:19-21`, `:37-39`, `:62-67` carry the new passes. *Watch:* `:17` and `:62` still say `aif-docs` writes the ТЗ and sets `Governing spec:`; the fix is pending the user's word.
