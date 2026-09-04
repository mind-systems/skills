# Architect buffer

Private state file for this architect↔editor loop. Deferral entries: **what**, **why deferred**, **trigger** — delete an entry once resolved. Non-deferral state (role, editor handle) is recorded at the top and is what a post-compact rehydration reads first.

**Scope of this buffer:** this session only. `01-`–`04-architect-buffer.md` belong to earlier architect sessions of the phase-26 paired-role experiment; not mine, never edited from here. `03-` (deciding half) and `04-` (applying half) are the useful outside reference if this session turns out to touch that thread.

## Role and configuration

- **Unpaired.** No pairing role assigned this session; `architect-pairing-engine` is not loaded. If the user assigns a half mid-session, load the engine at that moment and record the role here.
- **Editor handle:** `ab8b2f1a1b98a601b` — spawned 2026-09-04 on the first `::` relay of the session, which was itself the spawn prompt. Resume with `SendMessage({to: 'ab8b2f1a1b98a601b', ...})`, never a fresh spawn. `architect-editor-engine` loaded via `Skill` immediately before the spawn.
- **Release order:** nothing that closes a round — summary, verdict, or work-order — leaves before the editor's report on that round exists. My own parallel pass runs through the wait; what defers is the announcement.
- **Repo state at entry:** branch `dev`, tree clean, seam past **26.10** (`366d7d1`) in `.ai-factory/roadmaps/trickster77777.md` — no open `[ ]` task. Phase 26 fully implemented and committed.

## Standing rules carried in from buffers 03/04 (learned expensively, do not re-derive)

- Only the orchestrator implements a task. Paired or not, a chat architect writes contract lines, specs and notes — never an edit under `src/`. Flag an arriving order that edits code *before* applying, not after.
- Never state a line number or a count in a work-order without reading it off disk in the same breath. Both prior halves lost rounds to numbers recalled from memory that were right minutes earlier.
- Check what moved on disk between rounds before calling an order's numbers stale — read `git log` first.
- Phrase counts go against a whitespace-normalized read (`re.sub(r'\s+',' ',…).count(…)`); a line-oriented `grep` returns 0 for any phrase spanning a hard wrap, so it is a check that cannot fail.

## Round 1 — the three-layer model, ratified into the artifacts (2026-09-04, open)

**User's payload (relayed as-is, unenriched):** the work has three layers — docs, roadmap, code. Docs state desired behavior, code states implemented behavior, and the roadmap owns the description of the difference between the two — the seam between ТЗ and code. Nothing fundamental changes: the roadmap still carries tasks inside phases. The ask is that this reads more coherently than it does now, and that the model be written down — ratified — including the blocks that describe what a roadmap is and how it works.

**After-mark constraint, mine alone (never relayed):** no metaphors in the roadmap — the seam/foundation imagery is chat-only. The language of our artifacts is strict and laconic.

**Prior finding from the same session, before the relay:** the global CLAUDE.md holds the governing-spec concept at `:5`, `:9`, `:22` (ТЗ ahead of code; code built and verified against it; disagreement is a defect, not a stale doc), but its own metaphor at `:9` runs the other way — "docs are the crown, code the root system". The project fact "our docs under `docs/` *are* the ТЗ, written before any code" is **not** in the global CLAUDE.md; it homes in `docs/sakshi-harness/skill-cycle.md:17` and `aif-docs/SKILL.md:15` + its `description:`. Reserved-words confirms that home.

## Deferrals

_(none open)_

### My own parallel read (held until the editor reports — do not release early)

Surfaces read fresh off disk this round: `src/global/CLAUDE.md` (55 lines, full), `docs/philosophy/context-tree.md` (31 lines, full), `src/skills/roadmap-engine/SKILL.md` (§ head, § Roadmap File Format, section map), `docs/sakshi-harness/skill-cycle.md:1-25`, `docs/reserved-words.md` § Roadmap artifacts / Entry maps, plus a repo-wide sweep for `seam|stratum|time axis`.

**What the model adds that no surface states.** The roadmap is defined today *only temporally* — "карта времени" (`context-tree.md:15,17`), "entry map of **time**" (`global:13`), seam = "где проект живёт сейчас" (`reserved-words:33`). Nowhere is its *subject matter* stated. The user's claim supplies it: the roadmap's content is the difference between desired behavior (docs) and implemented behavior (code).

**Four currently-independent assertions become derivable from that one:**
1. Why `[ ]` exists — a named piece of the delta, not merely "not done yet".
2. Why `[x]` is history and only files verify the present (`global:13`, `context-tree:17`) — a closed delta describes no difference; what remains is the record of having described one.
3. Why `roadmap-prune` folds `[x]` into ARCHITECTURE § Features — today a housekeeping rule; under the model a consequence: a closed delta leaves the time map and becomes part of the description of what the code now is.
4. Why a governing spec disagreeing with its code is a defect, not a stale doc (`global:5`) — such a divergence is an *unnamed* delta, and naming every delta is exactly the roadmap's responsibility. This is what would finally connect `global:5` and `global:13`, which sit in one section today with no link between them.

**Three frictions to put to the user:**

a) **`context-tree.md:3` holds a rival model, and it is the load-bearing line.** "Техзадание — место, где ствол переходит в корни: описание поведения, у которого две стороны — доки, которые его рассказывают, и код, который его исполняет." That is a *two-sided* picture with ТЗ as the junction. The new one is three-layered with the **roadmap** as the junction and ТЗ demoted to being the docs layer itself. Both cannot stand.

b) **Position collision inside the tree metaphor.** trunk = CLAUDE.md, crown = docs, roots = code. The roadmap has *no* position in the tree today — it is bolted on as a separate axis. Placing it between crown and roots puts it where the trunk already is and where `:3` already puts ТЗ: three claimants, one position. This is most likely the actual incoherence the user is feeling.

c) **Vocabulary collision on "layer".** `reserved-words:34` glosses `stratum` as "an `[x]` line is a **layer** of history". Naming the three (docs/roadmap/code) "layers" gives one word two meanings — the bidirectional rule's exact prohibition. Fork for the user: rename the three, or re-gloss `stratum`.

**Bounded surface set for the ratification:** `src/global/CLAUDE.md:5,9,13` (normative home) · `docs/philosophy/context-tree.md:3,15,17` (+ knock-on `:19,:23`) · `docs/reserved-words.md:31,33,34` and § Roadmap artifacts · `src/skills/roadmap-engine/SKILL.md` § "Roadmap File Format" / "Why two tiers" · `docs/sakshi-harness/skill-cycle.md:5,17` · `CLAUDE.md:35` if context-tree's index row changes · possibly `roadmap-outline`/`roadmap-decompose`/`roadmap-prune`/`aif-docs`.

**Constraint from the after-mark half (never relayed):** no metaphor in the roadmap or in artifacts generally — strict, laconic. `context-tree.md` is the one surface where metaphor is the established genre, so the model gets written in two registers.

### Reconcile — editor's report vs my parallel read (round 1 closed)

**Converged independently:** the model is latent in two places that never cross-reference (editor: `global:5` ↔ `context-tree:3`; me: `global:5` ↔ `global:13` — both pairings true); the explicit third term is genuinely absent, not merely under-phrased; `CLAUDE.md`'s index row is a by-design second home and must track.

**Conceded to the editor — sharper than mine:**
1. **The `seam` collision, which I missed entirely.** The user's own word ("роадмап — это шов между тз и кодом") collides with the reserved `seam` = the `[x]`/`[ ]` boundary, load-bearing in the always-loaded global CLAUDE.md and used across five files. Editor's shape argument is right: one sense is a cursor position *inside* one file, the other a file's *role* relative to two other files — different granularity, so widening degrades the existing sentences. This outranks my "layer"/`stratum` collision, which stands but is smaller (a gloss word, live only if we mint "layer" as a term).
2. **Not every task line has a governing-spec counterpart.** `Governing spec:` attaches per phase; tooling, tests, prune and refactor tasks have no docs-side desired behavior. This falsifies a blanket "docs = desired, roadmap = the delta". I did not have it and it is the sharpest substantive catch of the round.
3. **`roadmap-engine` is mechanism-only** and must not host the model — I had listed it as a landing point; that would break the engine/lens split. Same for `reserved-words`: a pointer at most, never new prose.

**Held against the editor:**
1. **`context-tree.md:3` is a *rival* model, not a disconnected one.** The editor read it as supporting ("already states the duality your model rests on"). It assigns the junction position to **ТЗ** ("место, где ствол переходит в корни"), two-sided. The new model gives that position to the **roadmap** and demotes ТЗ to being the docs layer. That sentence must change its claim, not merely gain a link.
2. **Position collision inside the tree metaphor** — untouched by the editor. trunk = CLAUDE.md, crown = docs, roots = code; the roadmap has no position in the tree at all. Three claimants for one position; likely the actual source of the felt incoherence.
3. **The derivation chain.** The editor got one of four (`[x]` region), and read it as a *limit* on the model; I read it as the model's own *consequence*. I keep the other three, especially: an unnamed docs↔code divergence is exactly what the roadmap exists to prevent — the link that ties `global:5` to `global:13`.
4. **Process split** (editor out of remit): `docs/` is chat's to write; `src/global/CLAUDE.md` and any skill body need a roadmap task + spec for the orchestrator.

**Three forks put to the user** (`AskUserQuestion`): the `seam` collision; the scope of the "docs = desired" claim; whether the model reaches the always-loaded global CLAUDE.md.

## Round 2 — scope corrected by the user; reformat § Grounding claims only (2026-09-04, open)

**User's payload (marker trailed the whole message → relayed as-is, unenriched; no after-mark remainder).** Not a rewrite of everything and not the only way forward. Our own repo is special — a skill is its own documentation *and* the executable, so "documentation" means something different here. But the global CLAUDE.md is used in every project, and roadmap and code exist everywhere, including here. No reserved words of ours to be introduced. The text is already well written; the ask is to *reformat* it so it reads more coherently. My three-question fork set was rejected as overwrought — correctly.

**Scope now:** `src/global/CLAUDE.md` § "Grounding claims" alone. Not `docs/`, not `context-tree.md`, not the registry, not the skills. My round-1 findings about `context-tree.md:3` as a rival model and the tree's position collision are **out of scope for this task** — parked, not refuted.

**My own parallel read (held until the editor reports).** Section re-read fresh off disk; five paragraphs at `:5`/`:7`/`:9`/`:11`/`:13`, 401/511/573/204/463 chars.

The section interleaves two subjects with no divider:
- *which artifact is authority for what* — `:5` (docs vs code) and `:13` (ROADMAP, ARCHITECTURE);
- *how you read them* — `:7` (chain to the leaf), `:9` (map, walk), `:11` (decay).

`:5` sets up two of the three layers. `:13` introduces the third — four paragraphs later, behind the entire reading discipline, and characterized only temporally. Nothing joins them. That separation *is* the incoherence the user feels; it is structural, not verbal, which is why "just reformat" is the right diagnosis.

**Minimal move:** lift `:13` whole to sit immediately after `:5`, leaving `:7`/`:9`/`:11` in order behind it. No sentence is rewritten, ARCHITECTURE rides along inside its own paragraph so "The two maps orient a cold session" stays intact, and the section then reads: what the artifacts are → how to walk them.

**One increment above pure reformatting, to be offered separately:** adjacency alone still never says the roadmap holds the *difference* between the other two. One connective clause does. Offer it as an opt-in on top of the move, not folded into it — the user hedged ("наверное просто отформатировать").

**Left alone deliberately:** `:9`'s "docs are the crown, code the root system" — the file's only metaphor, but it serves the *walk*, not the layer model, and the user called the text well written. Also `:9`'s "A governing spec answers what the system *must do*" — an authority claim sitting inside a reading paragraph, but `:9` needs it locally to justify "for unbuilt code it legitimately ends at the doc".

**Vocabulary check:** the move coins nothing. Any bridge clause must reuse only words already in `:5`.

### Reconcile — round 2 closed

**Converged independently:** all the content is already on the page, the defect is arrangement; `:13` arrives with no bridge; and the fork is exactly two sizes — pure reflow vs reflow plus one bridging sentence. Both of us flagged that fork rather than picking it. `seam` stays untouched; moot under the corrected scope.

**Conceded — editor sharper:**
1. **`:5` and `:9` state the same duality twice in two unrelated metaphor sets.** I had assigned `:9` cleanly to the reading-discipline subject and explicitly waved past its duality clauses ("`:9` needs it locally"). The editor is right that the redundancy is itself a source of the incoherence, not just the separation between `:5` and `:13`.
2. **Do not tighten the language toward a two-file assumption.** In this repo a skill is its own doc and its own executable, so the reflow must leave "a description" / "ground truth" as loose as they already are. I did not have this; it comes straight out of the user's own remark.

**Held / added:**
1. **My structural cut survives and absorbs the editor's catch:** the section interleaves *which artifact is authority for what* (`:5`, `:13`) with *how you read them* (`:7`, `:9`, `:11`). `:9`'s duplication is a piece of the first subject stranded inside the second. The two reads compose; together they make the fix mechanical rather than a judgment call.
2. **`:13` moves whole** — ARCHITECTURE rides inside its own paragraph, "The two maps orient a cold session" stays intact, no surgery. This is what keeps the change a reformat.
3. **Correction to the editor's option 1.** It calls merging `:5`/`:9` "zero new claims". Not quite: `:9` leans on the duality to justify "for unbuilt code it legitimately ends at the doc" and "the leaf is code, on both sides of the spec". Strip the duality out of `:9` and that justification loses its antecedent — so even pure reflow has to keep or re-anchor that support.

**Open with the user:** pure reflow vs reflow + one clause (my lean: + one clause, since adjacency alone never states a relation, which is the user's whole goal); and the process fork — `src/global/CLAUDE.md` is under `src/`, so by the standing rule this is a contract line plus spec for the orchestrator, not a chat edit.

## Round 3 — the real defect: the always-loaded layer never assigns docs to a mode (2026-09-04, open)

**User's payload (marker trailed → relayed as-is).** An excerpt from a live chat in another project: an agent argued that a descriptive doc running ahead of code is defective — the mirror image of a stale doc — and the user conceded ("уступаю целиком"), then recognized the concession as wrong. Our documentation *is* the ТЗ the orchestrator leans on when executing a task; it is the foundation for tasks and must be held ahead of them. English has no word for ТЗ, so we call it "documentation" though it is not documentation. "Governing spec" was proposed and rejected — it collides with task specs in the roadmap, and in every project the material already sits in `docs/`; renaming the folder and fixing every link across all projects is out. In the user's understanding docs are *obliged* to describe desired behavior.

**My own parallel read, verified off disk (held until the editor reports).**

The global CLAUDE.md — the only always-loaded surface in every project — states the two doc modes **twice** (`:5`, `:22`) and **never assigns** the project's `docs/` to either. It never names `docs/` at all; the only paths in the whole file are `.ai-factory/*`. Confirmed by grep.

The assignment exists in exactly two places, neither of which is loaded in an ordinary session of another project: `docs/sakshi-harness/skill-cycle.md:17` ("Всё под `docs/` — governing-spec"), a sakshi-repo doc; and `aif-docs/SKILL.md:15` + its `description:`. The `aif-docs` description does sit in the always-loaded skill-description-field via the personal scope — but it is read as *when to invoke aif-docs*, not as a rule for how to treat an existing doc mid-task. Weak counter-signal, not a rule; do not overclaim it.

**Consequence, and it is mechanical, not agent stubbornness.** An agent mid-task in any project has `:5`'s opening "Descriptions drift; code wins" and no rule telling it `docs/` is not a description. It classifies by the default and reaches exactly the verdict in the excerpt. The user has been arguing with a defect in the always-loaded text, repeatedly, across projects.

**Sharper still:** `:5`'s ordering makes description the default and the ТЗ mode the exception ("the other doc mode"). Absent an assignment rule, an agent takes the default. So adding the assignment is necessary but not sufficient — the ordering itself teaches the wrong prior, which is precisely what the round-2 reflow was already going to touch.

**Proposed wording direction (zero coined terms, no rename, threads both objections):** one sentence in the global CLAUDE.md to the effect that the project's `docs/` state desired behavior and are held ahead of the code — they are not descriptions of it. No "governing spec", no "ТЗ", nothing renamed, no link touched anywhere.

**Honest reclassification to put to the user:** this is no longer a formatting job. The current text *causes* the argument the user is tired of having. Say so plainly rather than smuggling the fix in as a reflow.

**Open question, do not resolve alone:** whether rejecting "governing spec" means dropping it from `reserved-words.md` as a term, or only refusing to rename the folder / call the artifacts that in prose. The objections given ("collides with task specs", "already in `docs/`") are both about naming artifacts, and the registry already exists to resolve exactly that collision — so the narrow reading is likelier, but it is the user's call and it changes the wording.

### Reconcile — round 3 closed. Editor fabricated a quote; verified false.

**Verified off disk before accepting anything from the report** (normalized read, `python3`): `'exactly as defective'` → 0, `'mirrored'` → 0, `'stale description'` → 0, `'ahead of tasks'` → 0; `'ahead of code'` → 1, `'not a stale doc'` → 1, `'the other doc mode'` → 1.

**Held, and it is the round's main finding.** The editor wrote, in quotation marks, that `:5` already names the failure — *"a governing spec (ТЗ) that runs ahead of code is exactly as defective as a stale description — the same defect, mirrored."* No such sentence exists. `:5` says the **opposite**: running ahead of code is the mode's *definition* ("it states intended behavior ahead of code"), and disagreement is "a defect to reconcile — **not a stale doc**". The editor attributed to the file the very proposition the file exists to refuse.

**Consequence:** the editor's guardrail "keep the existing two-mode framing — a doc is either description-mode or governing-spec-mode, 'docs' stays the umbrella" would preserve the defect. Rejected. The two-mode split *without an assignment rule*, with description as the default, is what produces the argument the user is tired of.

**Also held:** the editor read the excerpt as field evidence of a failure mode the text covers. It is the inverse — evidence that the always-loaded text hands an agent the argument that defeats the user's model. (The excerpt does contain a real, separate distinction worth preserving: a ТЗ ahead of code is correct; a *descriptive* doc claiming a fix landed when it did not is wrong. The excerpt conflates them; the fix must not.)

**Conceded — editor sharper:**
1. **"Ahead of tasks", not only "ahead of code".** The user's own words: docs are what the orchestrator leans on when executing a task, the foundation *for tasks*, held ahead of them. `'ahead of tasks'` counts 0 in the file — the relation is genuinely absent, and my own proposed wording said only "ahead of the code". The editor's is sharper.
2. **Registry under-attribution** (minor, out of scope): `reserved-words.md:25`'s `governing spec` entry points Home at `skill-cycle` / `aif-docs`, while the term is actually defined at `global CLAUDE.md:5`. On record, not for this task.

**Standing lesson for this session:** the editor's reports now carry a fabricated quotation. Every quoted string from it gets counted off disk before use.

## Round 4 — draft the prescribing paragraph (2026-09-04, open)

**Marker split mid-message; the after-mark half was an explicit enrich instruction** ("не надо это сообщение пересылать как есть, я просто хочу, чтоб ты мои желания передал редактору, чтоб он был на одной волне с нами"). So this is the one licensed enrichment: the named context is *the user's wishes*, and exactly that went over — his scope correction, his model in his own words, his hard constraints, and the ask. None of my findings, counts, the fabricated-quote catch, or my direction-vs-chronology formulation crossed the channel.

**Scope now final:** skill descriptions are OFF the table — the user considers them well written and the skills work. One target only: the gap in the global CLAUDE.md. He also states he had never before formulated the three layers or the direction — this is new articulation, so there is no prior agreement to conform to.

**My own draft (held until the editor reports). 550 chars — inside the file's own range of 401–573.**

> Change moves one way — **docs → roadmap → code** — never the reverse. The docs state desired behavior, held ahead of the tasks and the code; the roadmap names what is not built yet; the code is what is built. A doc ahead of its code is doing its job, not drifting: the description rule above governs handoffs, notes and memory, never the project's own `docs/`. Which surface appears first varies — the direction does not. Discovery runs the other way — a problem met in code rises to the roadmap, sometimes to the docs — and is implemented back down.

**Why each clause is there:**
- *"Change moves one way… never the reverse"* — the invariant, stated first because it is what an arguing agent needs in one line.
- *"held ahead of the tasks and the code"* — carries the editor's round-3 catch; `ahead of tasks` counts 0 in the file today.
- *"the roadmap names what is not built yet"* — the third layer's job, without coining a term for it.
- *"A doc ahead of its code is doing its job, not drifting"* — kills the exact argument from the 38.5 excerpt in one sentence.
- *"the description rule above governs handoffs, notes and memory, never the project's own `docs/`"* — the missing **assignment rule**, the round-3 finding. Scopes `:5`'s first sentence instead of contradicting it, so `:5` needs no rewrite. Names `docs/`, which appears nowhere in the file today.
- *"Which surface appears first varies — the direction does not"* — separates direction from chronology, the collapse that licenses writing docs from code.
- *"Discovery runs the other way… implemented back down"* — dissolves the feedback edges as an apparent counterexample.

**Rejected while drafting:** "Never write a doc from the code it governs" — too absolute, it would forbid `aif-docs`' final verification pass (`skill-cycle.md:55`, сверка ТЗ с построенным). The point is that code never *overrules* the doc, not that code is never read.

**Placement:** immediately after `:5`, because the paragraph scopes `:5`'s description rule. Same landing the round-2 reflow was already heading for.

## Round 5 — APPLY-EDIT sent (2026-09-04, open)

**User's rulings this round (no marker — conversation, never relayed):** insert directly this time, no orchestrator; but a new phase and task go into the roadmap and get marked `[x]` once the insertion is done; stop cramming into ~500 chars, because the old roadmap/docs text can be shortened or dropped after the update; and a new requirement — state that tasks are executed sequentially, one at a time, top to bottom. Then: no task spec for 27.1, the contract line alone is enough with a short description. That overrides `roadmap-engine`'s two-tier rule and the `Spec:` tag; the user rules the forks.

**Round-4 reconcile, condensed.** The editor's citation of `task-rescue:227` ("Decision belongs elsewhere (a neighboring task / the governing spec)") verified accurate — clean round after the round-3 fabrication, and it grounded the model against `skill-cycle` and `task-rescue` before drafting rather than accepting it. Conceded to it: the obligation register ("foundation, not an afterthought"), the concrete manifestation order, the actionable repair guidance, and both of its own flags (keep the ТЗ etymology out; do not pin `task-rescue` into a universally-loaded file). Held against it, decisively: its draft carried **no assignment rule**, so it described the right behavior without fixing the verified cause; it never named `docs/`, having conflated "do not rename `docs/`" with "do not mention it" (`docs/` counts 0 in the file); it never said what the roadmap *is* relative to the other two; and at 725 chars it overran the file's 573 maximum.

**Pinned off disk before the order went out:** next spec number 102 (unused — the user then dropped the spec); new phase 27; last phase 26; insertion after `:102`, before `---STOP---` at `:104`; owner `trickster77777@gmail.com`; named-roadmap spec destination `.ai-factory/specs/trickster77777/`.

**Target section measured:** ¶1 379, ¶2 338, ¶3 371, ¶5 465, ¶7 560 — all inside the file's own 204–573 band. Section grows 2152 → 2828 (+676) while gaining two new rules and shedding `:9`'s duplication.

**Design decision I made and flagged to the user:** dropped "docs are the crown, code the root system" from `:9`. The metaphor's home is `context-tree.md`, and the user's standing rule is that artifact language is strict. Offered to restore it on request.

**Work-order sent:** four changes to `src/global/CLAUDE.md` (replace `:5`, insert two paragraphs after it, replace `:9`, replace `:13`), plus a new direction, Phase 27 header and the `[x]` 27.1 contract line in the roadmap. Guardrails: two files only, no rename, no coined term, no `Spec:` tag, File 1 verified before File 2, do not commit or stage. Self-verify by normalized phrase counts, ten of them pinned.

**Next:** verify by fact on the files myself — counts taken personally, not read off the report.

### Round 5 verified by fact — landed clean

Every number taken personally off the files, not read from the report.

**`src/global/CLAUDE.md`** — 13 normalized phrase counts on target, including three I added beyond the order's ten: `ahead of tasks` → 0 (the old wording is gone, replaced by "ahead of the tasks"), `a doc ahead of its code is doing its job` → 1, `governing spec` → 3. All three retired phrases at 0: `the other doc mode`, `docs are the crown`, `a description doc, CLAUDE.md`. § "Grounding claims" now 7 paragraphs at 379 / 338 / 371 / 511 / 465 / 204 / 560 — the 511 and 204 are the old `:7` and `:11` at their exact original lengths, untouched. No paragraph carries a newline; no hard wraps introduced. Diff content read line by line: exactly three replacements and two insertions, byte-matching the pinned strings; nothing below `## Documentation style` changed.

**`.ai-factory/roadmaps/trickster77777.md`** — `27.1` appears once, marked `[x]`, 557 chars, no `Spec:` tag on the line; `### Phase 27` once; `---STOP---` still the last non-empty line; the 26.10 line intact; **zero deletions** in the diff (the single `^-` match is the `--- a/` header, not a removed line).

**Repo:** `git diff --stat` = 2 files, +17/−3. My earlier arithmetic worry was my own error, not a defect — the stat's `10` column is total changed lines per file, so CLAUDE.md is +7/−3 (three replacements plus two paragraphs with their blank separators) and the roadmap +10/−0. `git status --short` shows ` M` on both (unstaged) plus this buffer as untracked. Nothing staged, nothing committed.

**Editor's own judgment call, correct:** it flagged the untracked `05-architect-buffer.md` against the "touch no file other than these two" guardrail rather than staying silent about a file it had not created. That is the right instinct — it is mine, and it sits outside the diff.

## Deferrals

- **`context-tree.md:3` holds the rival two-sided model** (ТЗ as the junction between trunk and roots), and the tree metaphor gives the roadmap no position at all. *Why deferred:* the user scoped this task to the global CLAUDE.md alone. *Trigger:* any future work on `docs/philosophy/context-tree.md`, or a user ask to make the three layers coherent across the philosophy docs.
- **`reserved-words.md:25` under-attributes `governing spec`** — Home points at `skill-cycle` / `aif-docs` while the term is defined in `global CLAUDE.md:5`. *Why deferred:* out of scope, cosmetic. *Trigger:* next edit to the registry.
- **Pipeline skill descriptions carry neither `docs` nor the direction** — `roadmap-outline`, `roadmap-decompose`, `task-rescue`, `roadmap-prune` say nothing about docs; `roadmap-decompose-skeleton`'s "spec-before-code axis" names a different spec. *Why deferred:* the user considers the descriptions well written and took them off the table. *Trigger:* recurrence of the same argument with an agent after this change ships.

## Round 6 — a new second-pass skill over phases (2026-09-04, open)

**Two `::` in the message**; the first sits inside quoted material from another chat, so the operative line is the last one. Before it — the whole excerpt plus the user's framing — relayed as-is. After it, mine alone: "давай обдумаем это направление". Not an enrich instruction, so the payload went unenriched.

**The ask.** A new skill holding the prompts the user keeps re-typing: a *second pass* over already-drafted phases that gives each phase its own note (what is wrong now + pointers into the docs for how it should become), shortens the preamble to ~200–500 chars in contract-line register, and puts the note link **inline at the end of the preamble line** rather than in a separate paragraph, so an agent reads the whole preamble in one line as it does a task. Explicitly **not** an update to `roadmap-outline` — it works perfectly and the user does not want notes at draft time. Name shape: `outline-<something about deepening>`.

**My own parallel read (held until the editor reports), grounded off disk.**

1. **The sharpest finding: `roadmap-outline` forbids exactly this, in three places.** `:25-26` "never a checkbox bullet, no contract line, no `Spec:` tag"; `:41` "no formal `Spec:` tag, no invented task specs"; Critical Rule 2 at `:72-73` "never a checkbox, never a `Spec:` tag". So the new skill does not merely add a pass — it *relaxes a prohibition its sibling states three times*. Left alone, the two skills contradict each other and an agent reading outline will refuse what the new skill prescribes. The repo's own rule covers this: a cross-file invariant grep cannot derive gets one sentence at the coupling point in **both** files. Minimal fix: scope outline's prohibition to its own moment ("at outline time"), not a rewrite — which preserves "works perfectly".

2. **The precedent is exact and gives the shape.** `roadmap-decompose` → `roadmap-decompose-skeleton` is already a first-pass/second-pass pair over the task tier: 147 lines, `loads: roadmap-engine test-philosophy`, structure Targeting → Workflow Step 0–4 → Critical Rules. The new skill is the same relation over the phase tier. Family stem is `roadmap-`, so the name should be `roadmap-outline-<lens>`, not `outline-<verb>`.

3. **Naming collision to raise.** `roadmap-outline-drift` is semantically exact under the model we just ratified — but `drift` now carries the opposite sense in the always-loaded text we wrote this session ("Descriptions drift; code wins" = decay). One word, two meanings, in authored product text: the registry's exact prohibition. My lean is the user's own word — `roadmap-outline-deepen` — though it names a verb where the sibling names a lens. Naming is the user's call.

4. **This is a skill *plus* an engine extension, and that should be said plainly.** `roadmap-engine` owns "Roadmap File Format" and the contract line's ~600-char budget lives there, not in `roadmap-decompose`. By that precedent the phase preamble's inline pointer and its 200–500 budget are **format** and belong in the engine; the new skill holds only policy — when to deepen, what goes in the note. The user framed it as one skill; honest to flag it is two edits.

5. **Vocabulary consequence.** reserved-words defines `two-tier` as "a contract line plus its task spec: two levels of one task". This makes the phase two-tier too — preamble plus phase note. Either the entry generalizes beyond tasks, or the phase's pair needs its own name.

6. **Clean derivation worth stating:** under the paragraph we just landed in the global CLAUDE.md, the roadmap holds the difference between docs and code. A phase note is exactly *that phase's statement of the difference*. The new skill is downstream of this session's own work, not a separate idea.

7. **Do not import the other project's layout unchecked.** The excerpt's `.ai-factory/notes/NN-phase-N-slug.md` and the `Decomposition context, …: [note NNN](…)` pointer come from a different repo (Limit Order Intents / core). Here `specs/` took over task specs and `notes/` holds research notes — a phase note is a third genre and its home is an open decision, not a given.
