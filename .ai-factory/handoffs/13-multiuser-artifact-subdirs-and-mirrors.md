# Handoff — multiuser: artifact subdirectories ratified, skills-side protocol mirrors owed

## 1. Frame

The multiuser direction's orchestrator half is now decomposed (tasks 12–14 in the orchestrator repo) and this session amended the governing spec twice — three-state orchestrator setting including `my`, and per-roadmap artifact subdirectories replacing the "artifacts stay flat" carve-out — while the orchestrator is live-running Phase 4 in this very repo; the originating session's context isn't available here — trust these files, not memory.

## 2. Read-first map

### Must-read now (minimal rehydration set)
- `docs/multiuser-roadmaps.md` — the governing spec **as amended** (Russian): § «Разрешение целевого файла» now carries the three-state orchestrator setting (absent → `ROADMAP.md`; `my` → identity derivation + owner check with loud fallback when the file is missing; explicit path → no checks) and the per-roadmap artifact-subdirectory paragraph with its factual rationale. On conflict this file wins.
- `~/projects/orchestrator/.ai-factory/specs/13-artifact-subdirs.md` — the exact layout change the mirrors must describe: subdir key = roadmap file stem (`roadmaps/kg-wmservice.md` → `plans/kg-wmservice/…`), default pair stays flat, numbering per-directory.
- `src/skills/orchestrator-artifacts/SKILL.md` — the protocol mirror to update: still describes a flat-only layout AND the `patches/` bridge retired by orchestrator task 02 (pre-existing drift).
- `.ai-factory/ROADMAP.md` § "Multiuser — named roadmaps" (Phase 4) — where the mirror task lands; 4.1–4.2 done, 4.3 in-flight, 4.4–4.5 pending.

### Read on demand
- `~/projects/orchestrator/.ai-factory/specs/12-roadmap-path-setting.md` — full three-state resolution: slug derivation, owner gate (`HaltError`), lazy-migration fallback, pinned forks.
- `~/projects/orchestrator/.ai-factory/specs/14-resume-adoption-gate.md` — leans on the protocol sentence "tracked artifacts belong to completed tasks, uncommitted ones to failed/in-flight"; any rewording of `orchestrator-artifacts` must preserve that meaning.
- `src/skills/roadmap-prune/SKILL.md` — the artifact sweep must learn per-roadmap subdirectories; pending 4.4 already touches this file.
- `~/projects/orchestrator/.ai-factory/handoffs/03-multiuser-named-roadmaps-orchestrator-side.md` — origin handoff; its "the orchestrator performs no identity derivation" narrowing is superseded (see Error log).

## 3. Current state

**Done:**
- Governing spec amended, two paragraphs: (1) the orchestrator setting carries three explicit states — no null-implies-derivation; (2) the artifact-flatness carve-out is replaced by per-roadmap subdirectories (`plans/<stem>/`, `plan-reviews/<stem>/`, `reviews/<stem>/`, `test-runs/<stem>/`; default pair flat) with the rationale: artifacts are committed with each milestone and spread through merges, so flat dirs union all developers' queues (duplicate numbers, merge conflicts, foreign-plan adoption by the resume detector). `patches/` dropped from the artifact list (retired by orchestrator task 02).
- Both amendments are **already committed** — swept into milestone commit `0763017` (4.2) by the live orchestrator run's `git add -A`. Content correct, attribution rode a foreign commit; nothing uncommitted remains for this doc.
- Orchestrator repo: task 12 rewritten (three-state `roadmap_path`, owner gate, test-sibling derivation, reviewer-prompt widening), tasks 13 (artifact subdirs) and 14 (resume adoption gate) decomposed with specs; queued before `---STOP---`. Uncommitted there.

**In-flight:**
- The orchestrator is live on this repo: 4.3 plan is untracked (`plans/90-4-3-readers-resolve-…`); 4.4–4.5 pending after it.

**Uncommitted working-tree state:**
- only the in-flight 4.3 plan artifacts (the orchestrator's own).

## 4. Next step

Decompose the protocol-mirror task into Phase 4 (as 4.6): `orchestrator-artifacts` gains the per-roadmap artifact-subdirectory layout (default pair flat) and drops the retired `patches/` bridge description; decide during decomposition whether prune's sweep-path awareness folds into pending 4.4 (same file, integration-branch contract) or stands alone; also verify the pending specs 45–47 don't contradict the amended artifact paragraph. Appending a task to Phase 4 while the orchestrator runs is safe (the loop re-scans the roadmap before each milestone) — but do not edit existing task lines mid-run.

## 5. Working discipline

- Design forks settled in dialogue fast: options with one recommendation, confirm before structural decisions; the user reverses freely — the governing spec, not chat memory or handoffs, is the settled state.
- Ground truth (code, git) overrides any description of it — this session revised a ratified pin because its premise failed against `main.py:96`.
- **Never commit without explicit permission.**

## 6. Error log

- **Handoff-03's narrowing contradicted the spec it summarized**: it said "the orchestrator performs no identity derivation", while the governing spec's owner-line section names the orchestrator among the resolvers of "my" («скилл или оркестратор»). Corrected: `my` keyword in `orchestrator.json` with the family derivation. Lesson: a handoff is a description; the spec wins.
- **The "artifacts stay flat — branch-local, transient" pin was factually wrong**: `_git_commit` runs `git add -A` (orchestrator `main.py:96`), artifacts ride milestone commits and spread via merges — flat dirs become the union of all users' queues. Revised to per-roadmap subdirs; the old rationale sentence («накопления одинаковых номеров там не возникает») is gone from the spec.
- **`orchestrator-artifacts` mirror drift found**: it still documents the `patches/` bridge retired by orchestrator task 02 — unfixed, folded into the 4.6 scope.
- **This session's doc edits were silently swept into the running orchestrator's commit `0763017`**: when editing files in a repo where the orchestrator is live, its `git add -A` will absorb them into the next milestone commit — check `git log` before assuming your edits sit uncommitted.

## 8. Domain model spine

- **Three-state `roadmap_path`** — absent → `ROADMAP.md`; literal `my` → derive + owner-check, missing file → loud fallback to default; any other value → explicit relative path, no checks. No state is inferred from null. Don't re-litigate. Spec § «Разрешение целевого файла»; orchestrator spec 12.
- **`my` + named roadmap exists + default has pending leftovers → the named roadmap runs**; draining the shared default is an explicit act (unset the key or point at it). Pinned: auto-picking shared leftovers from N workstations recreates the cross-user collision. Orchestrator spec 12 § Pinned forks.
- **Artifact subdir key = roadmap file stem, never git identity**; default pair flat (byte-stable); numbering per-directory — the same argument that ratified `specs/<slug>/`. Amended spec paragraph; orchestrator spec 13.
- **Resume adoption discriminator = git state**: tracked+clean plan → completed → stale, never adopted; untracked/modified/staged → in-flight → adoptable. Grounded in the protocol sentence in `orchestrator-artifacts`. Orchestrator spec 14.
- Slug rule, `> Owner:` line, single-writer, integration-branch prune — unchanged from the spec.

## 9. Hard rules

- Never commit without explicit permission (and beware the live orchestrator committing *for* you — see Error log).
- Generated artifacts in English regardless of conversation language.
- Lazy migration everywhere: defaults byte-stable; no code creates `roadmaps/` or owner lines on its own.

## 10. Cross-cutting contracts / invariants checklist

- Layout: named roadmap `<stem>` → `plans/<stem>/`, `plan-reviews/<stem>/`, `reviews/<stem>/`, `test-runs/<stem>/`; `ROADMAP.md`/`ROADMAP_TESTS.md` → flat dirs, byte-identical to today.
- `patches/` is retired everywhere — must vanish from `orchestrator-artifacts`.
- Test sibling always derived from the roadmap in play: `ROADMAP.md` → `ROADMAP_TESTS.md` (named special case); else same directory, stem + `-tests.md`. Never a second setting, never from identity.
- Protocol sentence whose meaning must survive any mirror rewording: **"tracked artifacts belong to completed tasks, uncommitted ones to failed/in-flight"** — now load-bearing for the orchestrator's resume gate.
- Slug: `user.email` local-part, lowercase, non-alnum runs → one hyphen (`kg.wmservice@gmail.com` → `kg-wmservice`); fallback slugified `user.name`. Owner line: `> Owner: <full email>`, exact form, first line.
- Resolution order, family-wide, identical wording everywhere: explicit argument → "my" → default `.ai-factory/ROADMAP.md`.
