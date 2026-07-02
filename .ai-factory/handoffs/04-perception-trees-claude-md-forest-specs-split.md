# Handoff — perception trees, CLAUDE.md forest sweep, notes→specs genre split

## 1. Frame
Two-day session (2026-07-02/03) that reframed the whole skills ecosystem around one model — agents lift lazy perception trees by following mentions from their contract line — and applied it everywhere: skill output registers, the orchestrator's prompts, every project's CLAUDE.md, artifact retirement (DESCRIPTION.md), and the notes→specs genre split. The chat is compacted but the knowledge is durable in files; rehydrate from them, don't trust memory.

## 2. Read-first map

### Must-read now (minimal rehydration set)
- `~/projects/skills/.ai-factory/ROADMAP.md` — the live queue: open tasks 53–56 above `---STOP---` (note hooks → specs split → handoff-over-note → prune artifact trail); everything before is done with timings
- `~/projects/skills/.ai-factory/notes/53-…` `54-…` `55-…` `56-…` — the four open specs; they encode every design decision of the final arc
- `~/projects/skills/CLAUDE.md` — repo model (src/upstream/active zones, `loads:` convention, editing rules, global-CLAUDE.md symlink chain)
- `~/projects/skills/src/global/CLAUDE.md` — the user's global instructions, now version-controlled here; contains the new "Project CLAUDE.md authoring" + "Planning workflow" rules that govern all cross-project work

### Read on demand
- `~/projects/skills/docs/skill-composition-model.md` — semantics of the skill language (3 new sections: refactoring works, no compiler, runtime is attention)
- `~/projects/orchestrator/docs/context-model.md` — the perception-tree model (what agents get literally, edges, eager vs lazy)
- `~/projects/orchestrator/docs/non-convergence.md` — two terminal-stop patterns (attrition-pass vs escalating blocker)
- `~/projects/orchestrator/.ai-factory/ROADMAP.md` — orchestrator queue: open task 05 (drop sweep-guard + specs naming) above STOP
- `~/projects/orchestrator/orchestrator/prompts/planner.md`, `reviewer.md` — where follow-mentions landed (tasks 03–04 done)
- `~/projects/skills/src/skills/milestone-rescue/SKILL.md` + `milestone-rescue-audit/SKILL.md` — the narrative Diagnosis Report register (shared both-ends contract)

## 3. Current state

**Done (skills repo, all orchestrator-executed, `[x]` with timings):**
- 33–34: rescue + audit reframed to narrative prose output (verified live on tradeoxy Phase 7 — dramatic improvement)
- 35–47: pipeline fix wave — test-coverage handoff-to-decompose + Class-A patch legalized; stale `/aif-plan`//`aif-roadmap`//`decompose` refs removed; pin-gaps default target + value-vs-meaning holes + scope-boundary hole type; engine caller-agnostic; workflow.md audit reframe; audit cold-run tools; `Questions` pseudo-tool dropped; governing-spec read in rescue; roadmap-engine absorbed the maintenance flow; decompose+outline slimmed to philosophies; `loads:` convention (ran FIRST as live semantics test — reviewer immediately used graph awareness)
- 48–49: aif-docs — doc index moved to CLAUDE.md (no README tables), diet to ~450 lines via references/
- 50–52: `aif` forked to src/ (CLAUDE.md-first bootstrap, marketplace kept, DESCRIPTION generation cut, AGENTS.md → one-line pointer); `aif-architecture` forked (sources from CLAUDE.md, pointer lands in CLAUDE.md `## Architecture`, `## Features` reserved section); DESCRIPTION reads retired from all our skills
- Orchestrator repo: 01–04 done (caffeinate, stderr deadlock, planner Step 3, follow-mentions with plan-review root recovery, DESCRIPTION reads dropped)

**Done (cross-project, all committed):**
- DESCRIPTION.md deleted in all 19 locations; 6 salvages into CLAUDE.mds (tradeoxy shared-Redis auth invariant; core tick pipeline; gui branded-UUID; mind web ownership-checks rule; mcp env vars + stderr-only rule; observe-js build/verification + contract content-inlined v0.1.2)
- CLAUDE.md forest swept: tradeoxy (routing tables only, dead-skill routing gone), mind (camera_ppg_kit registered, ECharts fix, gRPC facts fixed, api module graph → pointer, mcp gRPC deps), observability (phantom `tools/` → `observe-logs` skill, 5-repo routing, contract edges both ends, herald status/commands/eval), orchestrator (config + target-project sections → doc pointers)
- Global CLAUDE.md: new sections (no skill names in project files; one home per fact; monorepo routing protocol; planning chain; deferred-questions rule) and moved under version control: `~/.claude/CLAUDE.md` → `~/projects/skills/active/CLAUDE.md` → `../src/global/CLAUDE.md`
- Orchestrator docs: context-model.md + non-convergence.md written; doc index in CLAUDE.md (English labels); README table removed

**In-flight (open queues, specs written, not yet run):**
- Skills 53: `note` gets destination+template hooks (defaults unchanged — standalone byte-identical; lazy migration depends on default staying `notes/`)
- Skills 54: roadmap family writes to `.ai-factory/specs/`; readers (rescue, pin-gaps, temporal-tree) resolve **via `Spec:` tag only**, never a directory; NO project migration — lazy
- Skills 55: command-handoff becomes philosophy over `note` (loads: note, destination `handoffs/`, skeleton as template, verbatim); map fix — lift the tree scoped to the *next step*; several small cross-linked trees for multi-unit sessions
- Skills 56: prune deletes the pruned tasks' whole artifact trail (spec via tag; plans incl. sidecar, plan-reviews, reviews, patches via `<seq>-<slug>` match); orphan report (report-only); **no auto-commit** — on user's word, exactly one commit, message exactly `Roadmap prune`; `notes/` never mentioned by the skill
- Orchestrator 05: DELETE the sweep-guard clause (replace with nothing — positive follow-mentions rule is the whole protection); docs phrase-sweep for `specs/` current / `notes/` legacy-via-tags

**Uncommitted working-tree state:**
- skills repo: this handoff file (04-…) once written; everything else committed (`2790329` Roadmap update)
- `~/.claude/CLAUDE.md.bak` — backup of the pre-symlink global file, pending fresh-session verification

## 4. Next step
Run the orchestrator on the skills queue (53→54→55→56 — order is the dependency) and on the orchestrator repo (05). When results come back, verify each against its spec note — especially 53's "standalone /note byte-identical" and 55's "engine must not reshape the caller's template". Separately: user verifies a fresh session loads global instructions through the symlink chain, then deletes `~/.claude/CLAUDE.md.bak`.

## 5. Working discipline
- Chat plans; the orchestrator implements. This session writes specs/roadmaps/docs — never edits skill bodies directly (the one exception all session: docs and CLAUDE.mds, which the user asked for explicitly).
- Assessment first: when the user asks a question or shows a problem, deliver the diagnosis and stop; edits happen after his explicit go ("вноси", "давай таск").
- He corrects mid-design — treat pushback as design input, revise the note, don't defend. His corrections this session were always structural improvements.
- NEVER commit without his word; when he says commit, batch per repo, message style: short sentence-case imperative/noun phrase, no prefixes, no body.
- Tasks are two-tier: ~600-char contract line + spec note; atomicity gate ("can the first half deploy without the second?"); new tasks go above `---STOP---`.

## 6. Error log
- **Orchestrator note 03 (follow-mentions):** I drifted onto two foreign axes — mandatory-read pressure ("read in full, first") and tier authority ("ratified, do-not-re-litigate"). Correction: one rule — follow mentions from the contract line; depth self-limits by construction. Both axes are now explicit What-NOT-to-do bans in that note.
- **Same note, Edit 2:** I assumed the plan-reviewer knows its milestone — it doesn't (`agents.py:327`: fresh session, plan path only). The orchestrator itself amended: recover the root by matching the plan's `# Plan: <title>` against ROADMAP(_TESTS).md, skip the gate if no match.
- **tradeoxy root routing:** I deleted the routing tables wholesale as "dead skill routing". Wrong — the *function* (targeting from monorepo root; awareness of siblings) is live; only the skill names were dead. Restored skill-agnostically ("tasks go to the project they belong to" + tables).
- **note absorption:** I proposed folding `note` into roadmap-engine (1 caller). User: definitively no — note is the *generic distiller* (chat/spec/handoff genres); the second caller is command-handoff, which should shed its hand-rolled file machinery. Counting callers by current wiring instead of genre space was the mistake.
- **herald Status:** I proposed pointing CLAUDE.md at the roadmap. User: never mention the roadmap in CLAUDE.md — not every agent needs it; he routes it per-task himself (user-as-router, lazy tree).
- **observe-js contract edge:** I wrote "pinned as dev-time dependency by git tag" — actually the contract is content-inlined at `contract/` (v0.1.2, not a submodule). Fixed during the DESCRIPTION salvage.
- **Ollama tunnel (herald):** I framed the SSH tunnel as an architectural fact — it's dev-only; deployed service sits next to Ollama on the server.
- **Static skill-graph map:** I nearly added a hand-maintained dependency map to CLAUDE.md — rejected as cache-without-invalidation; replaced by the colocated `loads:` frontmatter convention + grep-derived reverse graph.
- **Edit-tool traps:** ROADMAP.md is modified concurrently by the running orchestrator — re-read before every edit (hit "file modified" twice); the literal string `---STOP---` also appears *inside* task 37's contract line — anchor edits on longer unique context.

## 7. Orientation
- **Two roadmaps, two note-numbering spaces:** skills repo (notes 01–56) vs orchestrator repo (notes 01–05). Don't cross-reference numbers without naming the repo.
- **Three directories, three genres:** `specs/` (new home, roadmap-family task specs), `notes/` (legacy specs, served via literal `Spec:` tag paths — user cleans by hand, skills never mention it after 54/56), `handoffs/` (session handoffs — this file's genre).
- **`roadmap-engine` changed meaning mid-session:** it now holds BOTH the two-tier format AND the create/update/check maintenance flow (task 43); outline/decompose are thin philosophies over it.
- **`aif` and `aif-architecture` are OURS now** (src/, reworked forks); only `aif-skill-generator` remains an upstream original in active/.
- **tradeoxy_gui vs mind_web** — two similar dashboards with layout systems; ECharts is mind_web, lightweight-charts is tradeoxy_gui.
- **Fable memory dir is project-scoped** (`~/.claude/projects/-Users-max-projects-skills/memory/`) — rules that must act across projects go into the global CLAUDE.md, not memory.

## 8. Domain model spine
- **Perception tree / lazy lifting** (don't re-litigate): agents get one contract line; context is lifted by following mentions; eager whole-graph loading burns out (measured — `enable_phase_sessions: false` is ~2× cheaper, no quality gain). Files: `orchestrator/docs/context-model.md`, `docs/phase-sessions.md`.
- **Skill language semantics**: skills are executable code with no compiler; contracts live in words ("behavior-identical", "word-for-word"); output register IS behavior; salience is the runtime resource. File: `skills/docs/skill-composition-model.md`.
- **Mechanism vs policy**: engines hold shared *how* (≥2 callers by genre space, not current wiring); philosophies keep control. File: repo CLAUDE.md + ARCHITECTURE.md.
- **One home per fact**: AGENTS.md = one-line pointer; doc index in CLAUDE.md, never README; module maps live in code/ARCHITECTURE.md; DESCRIPTION.md is dead. File: `src/global/CLAUDE.md`.
- **Non-convergence taxonomy**: severity falling + diverse findings = commit-as-is; one recurring blocker + rising severity (often "spec-owner decision" in round 1) = respec above, iterations won't help. File: `orchestrator/docs/non-convergence.md`.

## 9. Hard rules
- NEVER commit without explicit permission; exceptions are the fixed-message commands: `command-commit-roadmap-update` → `Roadmap update` (amend-if-unpushed pattern), and (after task 56) prune's on-request commit → exactly `Roadmap prune`.
- Artifacts/plans/specs in English; docs match neighboring docs' language (mostly Russian in orchestrator/skills docs).
- No skill/command names in project CLAUDE.mds (global rule; names rot → dead routing).
- Memory writes only on explicit trigger phrases ("запомни", "remember this", …).
- Upstream mirror (`upstream/ai-factory/`) is never hand-edited.

## 10. Cross-cutting contracts / invariants checklist
- `Spec:` tag carries a **literal path** and is the ONLY spec-resolution mechanism for readers (rescue/pin-gaps/temporal-tree/prune) — never directory scans. This is what makes the notes→specs migration lazy and invisible.
- `loads:` frontmatter: one-way (callers declare engines; engines never list callers); reverse graph = `grep -l`. Current edges: outline/decompose→roadmap-engine; skeleton→roadmap-engine test-philosophy; test-coverage→test-philosophy; roadmap-engine→note; (after 55) command-handoff→note.
- `note` hooks (after 53): destination dir + template are caller-supplied; unset = `.ai-factory/notes/` + Key Findings/Details/Open Questions, byte-identical.
- Rescue↔audit shared Diagnosis-Report register (chronological prose, no tables, root-cause payoff line) — declared in BOTH files; change both or neither.
- Rescue's sidecar `step` table mirrors `_validate_sidecar_step()` in orchestrator — never diverge.
- Global CLAUDE.md symlink chain: `~/.claude/CLAUDE.md` → `skills/active/CLAUDE.md` → `../src/global/CLAUDE.md` (git stores the symlink, mode 120000).
- Two-tier task format: contract line ~600 chars ending with `` Spec: `path`. `` + spec note; milestones `- [ ] **Title** — description` (orchestrator regex `roadmap.py`).
- PASS signals: `PLAN_REVIEW_PASS` / `REVIEW_PASS` as last line of the respective artifact file.

## 11. Per-unit map with watch-points
- **milestone-rescue / -audit** — narrative Diagnosis Report register, governing-spec read (42), cold-run tools (40). Watch: any future edit must preserve the both-ends register sentences and the `step` table mirror.
- **roadmap-engine** — format + maintenance flow + caller-agnostic. Watch: no philosophy content may creep in ("entry", not "task"); after 54 it passes destination `specs/` to note.
- **roadmap-outline / -decompose** — slim philosophies (outline: spec note OPTIONAL at strategic tier — no `Spec:` tag rather than invented content; decompose: atomicity gate as the flow's per-entry hook). Watch: behavior-identical claims were verified only by review, not yet by a full live create-mode run.
- **roadmap-test-coverage** — no roadmap writes; findings hand off to decompose via Layer 8 printout; Class-A patching is the one legal write. Watch: Layer 7 table stays (user likes tables about code — the anti-table rule is for diagnosis registers about process).
- **command-pin-gaps** — value holes (pin `file:line`) vs meaning holes (spec clause from observed behavior); scope-boundary hole type; default target = open tasks above STOP. Watch: 54 must keep its tag-based resolution.
- **aif** — CLAUDE.md-first bootstrap; config.yaml machinery KEPT verbatim (user likes it); marketplace/scanner KEPT (logic unchanged); AGENTS.md one-liner. Watch: recognizable-vs-upstream diff was the constraint; future edits shouldn't restructure.
- **aif-docs** — index in CLAUDE.md; ~450 lines; references/ split. Watch: verify a live State C run someday (spec said so; not yet done).
- **CLAUDE.md forest** — every root now: structure table + routing tables only (protocol lives in global) + invariants. Watch: broker signal-flow headline ("TradingView webhook →") — user never confirmed whether it's stale; open question.
- **repo-stats-herald** — Status boundary (target contract vs built: CLI summarizer + eval harness), Commands, eval-harness section. Watch: 3D-style CLAUDE.md is intentional there; don't "fix" present tense.
