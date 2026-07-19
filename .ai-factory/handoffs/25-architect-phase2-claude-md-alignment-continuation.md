# Architect handoff — Phase 2 CLAUDE.md-tree alignment, continuation

Rehydration note written by the architect, for the architect. On the next session
the user re-invokes `/agent-architect`; load this first. It is a private recovery
note — never sent to the editor.

## Who you are, who the editor is

You are the **architect** of the paired loop (`agent-architect` skill): you plan,
review, and decide; the **editor** applies every file change and reports back. You
verify the editor's reports against the real files, never against the note.

- **Live editor handle: `a80edd7e0a428f87e`** (model: sonnet). This is the *second*
  editor — the first (`a78fbc0eca13a17da`, also sonnet) was stopped by the user
  mid-session and is cancelled/non-resumable. Continue `a80edd7e...` via
  `SendMessage`. On rehydration, test it's alive with a trivial send or by watching
  for a stale-handle error; **if the send fails, it's dead — report to the user
  before sending anything onward, then spawn a fresh `editor` subagent** and re-issue
  the work-order (apply work-orders are self-contained and resend as-is).

## The work: Phase 2 = CLAUDE.md-tree alignment across project families

`skills/.ai-factory/ROADMAP.md` → `## Experiments` / `### Phase 2`. Each task aligns
one project's CLAUDE.md tree to the context-tree philosophy (dedupe, hoist, resolve
root↔leaf conflicts by ground truth, rules hygiene). Orchestrator can't run these —
they're cross-repo — so each is a **guided manual pass**, not an orchestrator job.

- **2.1 mind** — DONE, committed, pushed. Spec 24.
- **2.2 tradeoxy** — DONE, committed, pushed. Spec 39.
- **2.3 repo-stats-herald** — spec 75 written, NOT executed.
- **2.4 observability** — spec 76 written, NOT executed.
- **2.5 digital_ocean** — spec 77 written, NOT executed.

**Next up: execute 2.3, 2.4, 2.5** as guided passes, same flow as mind/tradeoxy.

### The per-project execution flow (proven on mind + tradeoxy)

1. Author an apply work-order → editor executes the pass (do-not-commit), grounding
   in the spec + the four philosophy docs (`context-tree.md`, `skill-pyramid.md`,
   `skill-composition-model.md` under `skills/docs/philosophy/`, and
   `skills/src/global/CLAUDE.md` §§ Grounding claims / Documentation style / Project
   CLAUDE.md authoring).
2. Your own bird's-eye review by fact (dedup vs the global CLAUDE.md; smooth
   through-read; every repo named where it belongs) — this fact-review plus grounding
   every editor call against the real files IS the verification.
3. Mark the task `[x]`, commit + push per repo.

**No cold-agent probe.** It was a one-time mechanism-validation on the first project
(confirmed a leaf session gets the hoisted facts; surfaced the mind_api ARCHITECTURE.md
drift → handoff → `b477bea`). The mechanism is proven — do not spawn a probe per pass;
it is pure overhead now. Direct fact-review covers verification.

Do the user's forks first each time — they may pre-rule; surface genuinely marginal
choices, don't bury them.

## Standing conventions — baked into how every pass runs

- **AGENTS.md → a symlink to its sibling CLAUDE.md.** Existing content dropped, NO
  salvage; created where missing. (The "one-line pointer" doctrine was retired
  session-wide — global CLAUDE.md, `aif`, `aif-docs`, specs 24/39 — as roadmap task
  18.1, committed.)
- **DESCRIPTION.md → retired genre, dropped.** Exception: genuinely unique facts get
  salvaged. Per-server hardware facts (CPU/RAM/GPU/disk/OS) → a doc under `docs/`
  (NOT CLAUDE.md — not needed in every always-loaded context; structure for multiple
  servers). Always-relevant behavioral rules → CLAUDE.md. (digital_ocean is the only
  DESCRIPTION.md with real unique content so far.)
- **CLAUDE.md top block is contentless noise → strip it.** Both the `# CLAUDE.md` H1
  title AND the `This file provides guidance to Claude Code…` boilerplate (standard
  or paraphrased) + their blanks; file starts at its first real `## section`.
  Already applied + pushed to mind (8), tradeoxy (5), sakshi-family (3: root,
  skills, orchestrator). Baked into specs 75/76/77 for the pending passes. NOT done
  in the 3 pending projects (their own passes strip it). NEVER touch
  `skills/src/global/CLAUDE.md` (title `# Global Instructions`, no boilerplate) or
  `skills/active/CLAUDE.md` (symlink).
- **Grove vs single repo.** A grove (separate git repos under a root) gets the full
  pass + grove entry checks (harness parent-load premise, README § Setup layout
  guarantee incl. freshest-branch, no upward-edge lines in leaves, re-measure sizes
  on entry). A single repo (repo-stats-herald, digital_ocean) → grove checks and
  hoist are **void-with-reason**; only intra-file cleanup + AGENTS.md/DESCRIPTION.md.
- **Same-name / submodule hazards.** Multiple same-named files resolve by explicit
  relative paths (tradeoxy's three `docs/architecture.md`); git submodules are
  EXCLUDED from edit scope (observability's `observe-dart/contract` &
  `observe-swift/contract` are submodules of `observe-contract`).
- **Commits: NO `Co-Authored-By` trailer.** The harness default "Claude Fable 5" is
  inaccurate (editor is Sonnet; you run as Opus 4.8 after the user's `/model opus`).
  User rejected it. Messages: noun phrase, sentence case, no type prefix, no body
  (body only for multi-concern commits).

## The three pending specs — grounded facts (verify fresh before acting)

- **Spec 75 / repo-stats-herald** — SINGLE repo, one CLAUDE.md (~91 lines), rules
  `base.md`. Grove/hoist void. Real conflict: rules file names `src/routes,services,
  models` that don't exist (actual: `src/core,llm,commits,summarization`). AGENTS.md
  1-line → symlink. **Boilerplate is NON-standalone** — shares its line with a real
  `docs/spec-overview.md` pointer; strip only the boilerplate clause, keep the pointer.
- **Spec 76 / observability** — nested grove: root + 5 subrepos (observe-write-proxy,
  observe-dart, observe-js, observe-swift, observe-contract), 6 in-scope CLAUDE.md
  (~402 lines). `observe-dart/contract` + `observe-swift/contract` are SUBMODULES of
  observe-contract → excluded. `observe-js/AGENTS.md` is 35-line → discard. README
  omits `observe-contract` (camera_ppg_kit-class gap → add to § Setup). Root's Naming
  Conventions is SUBSTANTIVE (cross-SDK API + OTel), keep it — unlike observe-js's
  casing noise.
- **Spec 77 / digital_ocean** — SINGLE repo, one CLAUDE.md (~131 lines), NO rules
  files (rules-hygiene void). AGENTS.md 69-line stale → discard. DESCRIPTION.md
  (85 lines) → salvage the hardware quintet (CPU i5-4460 / RAM 15GB / GPU RTX 3090
  24GB CUDA / disk 228GB / OS Ubuntu 24.04) into a NEW `docs/` file, destructive-op
  rule → CLAUDE.md's "Working with the Server"; then delete DESCRIPTION.md. Nginx
  vhost-table 3-way drift resolved by `configs/nginx/*.conf` (CLAUDE.md's 12-row
  table is already correct). README carve-out: kill the dead DESCRIPTION.md ref.

## State on disk (re-verify — held context decays)

- 2.1/2.2 alignment + top-block strips: committed & pushed across mind (8 repos),
  tradeoxy (5), sakshi-family (3).
- Planning for 2.3/2.4/2.5 lives in the **skills working tree**: `ROADMAP.md` (the
  three `[ ]` contract lines, condensed) + untracked specs `75/76/77`. The user
  manages when to commit this — **do not raise commit status unless asked** (they
  told you twice to stop). A `---STOP---`-fence removal around 2.1/2.2 also sits in
  the tree (an external edit, likely the user's) — leave it.

## Open threads the user has not closed

- The inaccurate `Co-Authored-By: Claude Fable 5` trailer sits on ~15 earlier commits
  (mind ×8, tradeoxy ×5, skills ×2). Cleaning them = rebase + force-push per repo.
  User hasn't ruled. New commits already omit it.
- Whether/when to commit the 2.3–2.5 planning pile — user's call, don't ask.

## Working with this user

Terse, decisive, wants execution not deliberation. Gets annoyed by over-asking
(especially commit-permission) and by defensive/hedged choices (kept the `# CLAUDE.md`
header "to be safe" → got pushback that it's useless). Relays to the editor end with
`::`; no marker = talk to you, never forwarded. Lead every report with the outcome,
grounded by fact.
