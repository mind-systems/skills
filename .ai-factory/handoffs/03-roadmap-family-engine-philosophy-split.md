# Handoff — the roadmap-family engine/philosophy split (full context)

*This is written as context, not a checklist. The chat that produced all this reasoning is being compacted; after that you will have amnesia about everything below, so read it as the story of what we decided and — more importantly — what we got **wrong** and how we fixed it. The mistakes are the expensive part to re-learn.*

---

## Where we are, and how this repo works

`~/projects/skills` is the source-of-truth repo for generic AI-Factory skills (Claude Code slash-command packages, living under `src/skills/`, symlinked to `~/.claude/skills`). Its *product* is skills, not application code.

Crucially: milestones in `.ai-factory/ROADMAP.md` are executed by **the orchestrator** — a separate Python project at `~/projects/orchestrator` that autonomously plans → plan-reviews → implements → reviews → commits each milestone, using its own prompts (`orchestrator/prompts/planner.md`, `reviewer.md`, `implementer.md`), NOT the `aif-*` skills. Our job in *this* chat is upstream of that: we **spec** milestones (a ~600-char roadmap contract line + a full spec note in `.ai-factory/notes/`), then **review** what the orchestrator produced and **rescue** failures. We do not write skill code ourselves in chat — that is the orchestrator's job. (This is now hard-coded in global `~/.claude/CLAUDE.md`: "Chat plans; the orchestrator implements.")

The whole session was one epic: **break the roadmap skill-family into a shared "format engine" plus thin "philosophy" skills.** Behind that sits a mental model we developed and wrote down (see "The model" below), because getting the model wrong is exactly what cost us a full milestone.

---

## What we're building (the epic)

The roadmap family currently duplicates output machinery. `roadmap-decompose` held, inline, both the *decomposition philosophy* (the Atomicity Gate, the create/update/check modes) **and** the *artifact format* (what a contract line looks like, the two-tier contract-line-plus-spec-note structure, the roadmap file layout). The plan: pull the format out into a shared skill the philosophy skills load, so:

- **`roadmap-engine`** = the shared *artifact format* (mechanism). Just an explanation of what the two-tier artifacts look like.
- **`roadmap-decompose`** = the *decomposition philosophy* (policy): atomicity, modes, exploration, confirmation. Loads the engine for the format.
- **`roadmap-decompose-skeleton`** (note 27, new skill) = a second-pass decomposition along the spec-before-code axis — three lenses (skeleton-first / TDD / concurrency-contract). Loads `roadmap-engine` + `test-philosophy`.
- **`test-philosophy`** (note 31, renamed from `test-engine`) = the shared testing *philosophy*: "test only what fails silently, skip what fails loudly."
- **`roadmap-test-coverage`** sources that philosophy from `test-philosophy` instead of inlining it.
- **`aif-roadmap`** (note 32) = strategic (coarse) roadmap creation; refactored to load `roadmap-engine` for the format while keeping only its *granularity* philosophy.

The roadmap order (above the `---STOP---` Max placed at L47 to pause for review): `[x] 30 extract-engine` done → `[ ] 27 skeleton` → `[ ] 31 test-philosophy` → `[ ] 32 aif-roadmap`. (`observe-logs`, below the *second* STOP at L55, is backlog, not epic.)

---

## The problems we hit — in detail

### 1. The rigid-engine phantom (the central, most-expensive mistake)

This is the one to internalize. When `roadmap-engine` was first built (milestone 28), it was written as a **rigid procedure**: an "Input Contract" (`{task name, full spec, target roadmap file}`) and a numbered "Per-Task Render Procedure" (load aif-note → write a *fresh* note → append a *fresh* contract line → **save**), plus a "What This Engine Does NOT Own" list. It read like an API — for a skill that has no programmatic call surface at all.

Then milestone 30 was originally specced as *"roadmap-decompose: render via roadmap-engine"* — refactor decompose to delegate its output to that engine. The orchestrator implemented it and **looped at code-review three times on byte-identical code**. The reviewer's finding, stable across all three rounds, was correct and devastating: the engine's contract is "append a fresh line and save," but decompose needs *three different output shapes* — Mode 1 builds the whole roadmap file at once, Mode 2.4 appends a new task, Mode 2.5 edits an *existing* milestone line to add a `Spec:` tag. Only Mode 2.4 fits "append." Mode 1 would need the engine to *return content without saving* (it can't); Mode 2.5 routed through the engine would **append a duplicate line** (it can't edit in place). So the plan asked the engine for behaviors it did not have. The implementer had faithfully implemented a wrong plan and literally could not fix it, because any fix contradicted its own plan.

**My response was wrong, twice.** First I ran milestone-rescue at depth-3 and hand-fixed decompose to work *around* the rigid engine — Mode 1 became "write a scaffold, then append per milestone in order," Mode 2.4 "append then reorder via Reprioritize," Mode 2.5 "stay local, the engine can't edit lines" — and I propagated an "engine is append-and-save-only" constraint clause into notes 27 and 32. It was a lot of careful, correct-looking work that treated the *symptom*. Then I escalated: I proposed an "engine v2 — decouple render from write" (the engine *returns* content, callers place it), a whole new contract with more modes.

**Max cut through all of it.** The insight: *skills are not executable programs — they are reusable instructions for one agent.* There is no separate process, no fixed function signature. `roadmap-engine` is simply the shared **explanation of the artifact format**; the one agent, knowing the format, writes / appends / edits contextually as each situation needs. The entire "append-only / can't-do-in-place / needs-content-return" limitation was a **phantom** I had manufactured by taking the engine's self-described *procedure* as gospel. The proof: the format had worked *perfectly* inside decompose for ages (as a "Roadmap File Format" section) — nobody ever hit an "append-only" problem — because there it was format, not a procedure. Extracting it *as a procedure* is what broke it.

The fix was a **full reset**, not more workarounds: revert decompose to HEAD, delete the plan/plan-reviews/reviews/sidecar, undo my workaround edits to notes 27/32, and **re-spec milestone 30** as *"extract `roadmap-engine` as the artifact FORMAT — verbatim from decompose's 'Roadmap File Format' section + the two-tier-note explanation — dropping the Input Contract / Per-Task Procedure / 'does NOT own' framing."* The orchestrator re-ran it, it passed first review, committed `1c3fbc3`. And because the engine is now *format*, the modes just work: Mode 1 writes notes and the file, Mode 2.5 adds a `Spec:` tag to the existing line — all contextual, no scaffold/append/content-return machinery anywhere. The phantom is gone by construction.

**The durable lesson:** if a skill is written like an API with a rigid contract, that rigidity is itself the bug. Model shared skills as format/knowledge the agent applies, never as callables with signatures. The moment you start building "modes / content-return / insertion-point" to work around a skill's "contract," stop — the skill is over-specified. And note the meta-pattern: my instinct was repeatedly to *add* machinery; Max's correction was always to *remove* it. He said it plainly more than once: "ты вечно пытаешься усложнить скил." Believe it.

### 2. The `test-engine` misnomer → `test-philosophy`

We'd extracted the silent-failure testing rule into a skill we called `test-engine`. Max caught that this is a **philosophy** ("test only what fails silently"), not an engine. The distinction matters: the *roadmap* family really does have a shared mechanism (the artifact format = a genuine engine), but the *test* family does **not** — `roadmap-test-coverage` has its own 8-layer pipeline that nothing else shares. There is only a shared *rule*, no shared *algorithm*. Calling it "engine" was forcing the analogy. Milestone 31 was re-spec'd to **rename `test-engine` → `test-philosophy`** (dir, frontmatter `name`, H1 heading, body wording, and every reference). And a consequence Max spotted: `roadmap-engine` is correctly `user-invocable: false` (it's meaningless standalone — no point a human invoking a bare format), but a *philosophy* is usable standalone (a user might invoke `/test-philosophy` to consult or apply the rule), so `test-philosophy` must flip to `user-invocable: true`.

### 3. The `/aif-implement` fabrication

I kept ending messages with "ready for `/aif-implement`." Max asked where I was getting that. It was pattern-matched from the generic AI-Factory lifecycle, but wrong here: these milestones are run by the **orchestrator**, not by that skill. I retracted it, and we rewrote the global `~/.claude/CLAUDE.md` "Planning workflow" section accordingly: *chat plans, the orchestrator implements; never modify application code on your own initiative — only planning artifacts; do not drift into coding.* With one narrow exception (explicit, unambiguous user request for a specific change) worded to avoid becoming a loophole — modelled on how the same file's Memory section handles exact triggers.

### 4. Why milestone 30 took three plan-review rounds (and how we pre-empted it for 31/32)

Two classes of stumble:

**(a) A false "3-caller" premise.** The plan justified the engine by claiming three callers (decompose, skeleton, aif-roadmap). Reality after the split: *one* real caller. Decompose loads it; `roadmap-decompose-skeleton` doesn't exist yet; `aif-roadmap` *can't* invoke it (its `allowed-tools` lack the `Skill` tool). This collides with our own composition rule ("factor into a skill only when it carries shared content used by ≥2 callers; a single-caller loader is negative value"). The plan resolved it honestly by declaring the engine forward-looking infra — but note this is a **deferred bet**: the engine only earns its keep once skeleton (27) and aif-roadmap (32) actually wire in. If those slip, the engine is temporarily dead weight and decompose should re-inline the format. Watch it.

**(b) Reference-hygiene during a text-move.** Extracting the format meant repointing five "Two-Tier Output" references in decompose; one of them was **hidden inside an Atomicity-Gate block (line 198)** and the repoint list kept omitting it — the reviewer surfaced it only in round 2. Plus a "keep the modes byte-identical" instruction that collided with "edit these mode sub-steps," and orphaned `---` separators left after the deletion.

Milestones **31 and 32 are the same *kind* of task** (a rename and an extraction — both text-moves), so they will hit class (b) unless the spec pre-empts it. I therefore baked a **"Refactor hygiene"** section into notes 31 and 32: *enumerate every reference exhaustively (grep the whole repo — never work from a partial list, because 30 kept discovering a missed one); state the byte-identical carve-out explicitly ("verbatim EXCEPT the named sites being changed"); collapse orphaned separators.* Milestone 27 is a *new* skill, not a text-move, so it's exposed to design-complexity review (three lenses, fusion rules, ordering) instead — that class can't be pre-empted the same mechanical way.

### 5. Load-once verbosity, and making it crisp again

Before the split, decompose had a crisp rule that made `aif-note` "load once per session, perfectly." After the extraction, that got replaced by a whole verbose paragraph inside the engine, and the decompose call-sites just said "load roadmap-engine once for the artifact format" without the crisp "don't re-invoke if already loaded" discipline. Max wanted the *same* crispness restored. We fixed it: the engine's own load-once and its aif-note load-once are now single bolded one-liners; decompose's three call-sites say **"ensure `roadmap-engine` is loaded once this chat (don't re-invoke if already loaded)."** And — the durable guard against re-introducing the verbosity — the consumer specs (27, 32) now say callers only *load-once* + "produce per the engine's format," and must **not** restate the note format / aif-note load-once / `<NN>`+slug details, because the engine owns those. Any spec or impl that re-inlines the engine's internals is the mistake returning.

### 6. A git gotcha worth remembering

During the milestone-30 full-reset, `git checkout -- src/skills/roadmap-decompose/SKILL.md` restored the **staged** (orchestrator's buggy, uncommitted) version, not the committed one. To get the true pre-milestone state you need `git checkout HEAD -- <file>`.

---

## Two things we did alongside the epic

**Upstream sync.** We pulled from `lee-to/ai-factory` and synced 18 `aif-*` skills (committed). Method: temp-clone + per-skill diff, with one agent per skill judging PULL / MERGE / SKIP. All 18 were clean pulls except `aif-qa` (upstream had *relaxed* a determinism rule ours states more strictly — Max chose to sync anyway since it's fully theirs). `aif-docs` and `aif-plan` are ours/diverged — cherry-pick review found no upstream bug-fixes worth porting; we kept ours. We also fixed an internal staleness in our own `aif-plan/references/EXAMPLES.md` (it still described fast/full/parallel modes our rewritten SKILL.md dropped). Separately, while syncing we noticed the **orchestrator's `planner.md`** tells the planning agent to spawn Explore sub-agents via a `Task` tool it isn't granted (`agents.py:249` gives it only Read/Write/Glob/Grep/Bash) — a report-only handoff for that is parked at `~/projects/orchestrator/.ai-factory/handoffs/02-planner-prompt-explore-tool-mismatch.md`.

**The composition model (written down so it survives).** The engine-vs-philosophy idea generalized into a principle we documented: `docs/skill-composition-model.md` (a Russian narrative essay) and `.ai-factory/ARCHITECTURE.md` → "Composition: mechanism vs policy," with a pointer in the project `CLAUDE.md`. The web-search we did confirmed our metaphors map onto real conventions: **separation of mechanism and policy** (microkernel design), the **Strategy/policy pattern**, and Anthropic's own **Composability** principle for Agent Skills — with our own twist that in skill-space *abstraction is paid in context tokens* (unlike compiled code where a delegating layer is free), so you extract only for shared *content*, never for pure routing.

---

## The model we settled on (do not re-litigate)

- **Skills are loadable instruction units for one agent — not compiled objects or APIs.** Composition = loading another skill's content into the current context (like `#include`), not a service call. There is no runtime call-stack, no typed interface; `$VARIABLES` are textual substitution, not bindings.
- **Mechanism vs policy.** Extract a skill only when it carries shared *content* (a format, rule, or procedure) used by ≥2 callers. A skill that only routes to other skills, with no content of its own, is negative value — every loaded line is a recurring context cost.
- **`roadmap-engine` is a FORMAT explanation**, applied contextually. No input contract, no per-task procedure, no modes, no save-ownership. This is what dissolved the phantom.
- **`test-philosophy` is a rule only** — the test family has no engine.
- **There is no automated way to test skills' behavior** (LLM-generated, non-deterministic). The regression guard for refactors is discipline: a *move, not a rewrite* — preserved text stays byte-identical, verified by a static diff. Upstream `lee-to/ai-tester` (a separate Rust harness with yaml fixtures) is the real skill-test tool if we ever adopt it; we haven't.

---

## How Max works (so you don't misread him)

Short, dense, often single-word instructions, in Russian; generated files in English. He authorizes with "делай / правь / чини / давай"; he wants a recommendation, not a survey of options. He reviews critically and catches paraphrase and scope-creep instantly — "copy" means byte-for-byte. He rolls back anything that oversteps. **His strongest and most repeated correction this session was against over-engineering** — prefer the smallest, simplest skill; don't add modes/APIs/machinery where plain instructions suffice. No commit without explicit permission. He delegates parallel work aggressively (we ran 18 sync agents at once). He put the `---STOP---` at ROADMAP L47 himself, deliberately, to pause the epic for this review — it is not a bug; don't "fix" it.

---

## Current state and the next step

**Done:** the epic is fully specced (notes 27–32, above the STOP); milestone 30 (extract-engine) is committed (`1c3fbc3`) and reviewed-correct; post-review fixes are applied but **uncommitted** on master (engine `allowed-tools` → `Read`; crisp load-once in engine + decompose; refactor-hygiene baked into notes 31/32). The composition model and the global CLAUDE.md rewrite are done. The upstream sync is committed.

**Uncommitted on master right now:** `ROADMAP.md`, `notes/27`, `notes/31`, `notes/32`, `src/skills/roadmap-decompose/SKILL.md`, `src/skills/roadmap-engine/SKILL.md` (all review fixes); plus untracked `plans/19-…skeleton.{md,json}` — the orchestrator has already begun planning milestone 27 (skeleton).

**Next:** drive the epic to completion. Let the orchestrator run 27 → 31 → 32 (Max lifts/moves the L47 STOP). As each finishes, **we review it** the way we reviewed 30 — read the plan-reviews to see where the planner stumbled, then read the two/three changed files independently, don't just trust the REVIEW_PASS. If a milestone **fails or loops**, diagnose and rescue (milestone-rescue), and remember the lesson from problem #1: check whether the failure is a real defect or a phantom created by over-specification before you start building workarounds.

**After the whole epic lands**, Max wants to return to a **repo re-decomposition** we designed earlier this session: upstream `ai-factory` becomes its own folder of original skills (as a git *remote*/worktree, not a hand-copied dump — so syncing is `git fetch`, no temp clones); our custom skills sit separately; and the active `~/.claude/skills` set stops being "every possible skill" and becomes **only the skills Max actually uses** (delete the unused; the text sync-ledger in CLAUDE.md gets retired in favor of `git diff upstream`, which classifies each skill as ours / pristine / diverged automatically).

---

## Where this note lives

This handoff is intentionally on a separate git worktree/branch (`handoff-notes`, checked out at `../skills-handoff-notes`) so it does **not** appear in the orchestrator's `master` working tree while it runs the epic. It is uncommitted there unless Max commits it on that branch.
