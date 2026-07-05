# Roadmap family: two-level phase grammar — outline owns phase headers, decompose/skeleton own N.M tasks

**Date:** 2026-07-05
**Source:** conversation context (design session over `.ai-factory/notes/57-task-roadmap-outline-phase-headers-decompose-task-numbers.md`; grammar converged live in the tradeoxy planning sessions against `tradeoxy_broker` and `tradeoxy_gui` roadmaps)

## Problem today

The roadmap family (`roadmap-outline`, `roadmap-decompose`, `roadmap-decompose-skeleton`) shares one output shape: all three write checkbox task bullets. The tradeoxy sessions settled a two-level grammar — outline owns `### Phase N` headers and the numbering spine, decompose/skeleton own the `N.M` tasks under them — but the skills don't know it, so the user re-teaches it by hand every session ("давай пронумеруем фазы 9, 10..", "каждому таску дай заголовок Phase 1.. Пронумеруй", "пронумеруем phase 8.., чтоб без конфликтов", "заполним тасками, пронумеруем их 9.1 10.1 10.2"). Two live failures the split must prevent (note 57 error log):

- Outline's current hook (a) ("each entry is a high-level goal" rendered as a contract line) makes phases themselves checkbox milestone bullets with tasks nested under them by indentation — corrected by the user against the broker roadmap.
- Phase numbering restarted at 1 inside a new direction section, colliding with an existing Phase 1–8 in the same file; renumbered to 9–12 by hand, chasing cross-references ("blocked on Phases 9 and 10") manually.

Additionally, `roadmap-engine`'s "Roadmap File Format" section still shows a flat `## Milestones` list that matches no live roadmap below `---STOP---` — the shared format description is stale.

## The settled grammar (canonical form)

```markdown
## <Direction name>                          ← direction section (## header)

<direction preamble: source handoff/spec links, hard rules, gating>

### Phase N — <Phase title>                  ← outline writes THESE

<phase intro as prose, no checkbox: gate ("blocked on X"), the problem today,
key contracts / pinned decisions the phase rests on>

- [ ] **N.1 — <Task name>** — <contract line per the two-tier
  format>. Spec: `.ai-factory/specs/<NN>-<slug>.md`.   ← decompose/skeleton write THESE
- [ ] **N.2 — <Task name>** — … Spec: …
```

Reference implementations: `tradeoxy_broker/.ai-factory/ROADMAP.md` (section below `---STOP---`: `## Limit Order Intents` → `### Phase 1 - Intent Store` → `- [ ] **1.1 …**`) and `tradeoxy_gui/.ai-factory/ROADMAP.md` (`## Limit Order Intents — GUI surfaces` → `### Phase 9` … `### Phase 12`, continuing after an earlier section's Phase 8).

## Design decisions (settled this session)

1. **The grammar lives in `roadmap-engine`'s "Roadmap File Format" section; division of labor lives in the callers' hooks.** Rationale per the composition rule (shared content, ≥2 callers): outline must know the header shape, decompose AND skeleton must both know the `N.M` shape — three callers reading one render format. The engine/policy boundary is preserved: the *shape* (what markdown) is mechanism → engine; *who emits which level and when* (outline — headers, never checkboxes; decompose/skeleton — `N.M` tasks) is policy → hooks (a). The engine stays caller-agnostic — it describes levels of the format, never names which skill writes which.
2. **Phase numbers are globally sequential integers across the whole roadmap file.** A new direction section continues from the highest existing phase number in ANY section, never restarts at 1. Uniqueness across the file is the point: the orchestrator (and cross-references in contract lines) can address a phase without naming its section. Gaps in the sequence are legal and expected (prune leaves holes; see decision 5). This is a file-level invariant → engine format section; outline merely applies it when creating phases.
3. **Sub-numbering `N.M.x` for splits of an already-numbered task — never cascade renumbering.** When a numbered task `N.M` is split (skeleton's insertion, or decompose's "Decompose existing" offering a split), the children are numbered `N.M.1 … N.M.k` in chain order and the **original impl line is renumbered to the last child `N.M.k`** — the number `N.M` ceases to exist as a task number and becomes the family prefix. External references ("blocked on 9.1") stay valid: the family completes exactly when its impl tail completes, so the reference semantics are unchanged with zero lines rewritten outside the family. Rejected alternative: shifting the tail of the phase (`9.2` → `9.4`) — one insertion cascades through cross-references file-wide, the exact manual chase from the error log. Two callers need this rule (skeleton + decompose's split) → it lives in the engine format section.
4. **Flat fallback.** When the target roadmap has no phase headers (legacy flat roadmap, `ROADMAP_TESTS.md`, this repo's own ROADMAP.md), tasks are emitted unnumbered as flat checkbox bullets — exactly today's behavior. Decompose must never invent a phase header to hang a number on; no header → no number. This keeps the migration lazy: no existing project roadmap is touched.
5. **Prune deletes emptied phase headers, never renumbers.** When all tasks under a `### Phase N` header are pruned, the header and its intro prose go too; remaining phase numbers are NOT shifted — the numbering is historic and gaps are normal (they may still be referenced from specs, commits, and ARCHITECTURE.md features).
6. **A phase has no `Spec:` tag and no spec-note category.** The prose intro absorbs what used to be the milestone contract line (gate, problem, key contracts). Links to handoff/spec notes are allowed as plain markdown links inside the intro/preamble prose — no formal tag, no invented notes. Outline's whole "spec note optional at this tier" clause dies with the category.
7. **Outline drops check mode.** With no checkboxes at the phase tier there is nothing for check mode to scan or mark; phase progress is a derivative of its tasks (`N.M` checkboxes — decompose/prune territory). Outline keeps the rest of the engine's maintenance flow (create/update, draft→confirm, routing) — the overlap with the engine shifts entirely from the artifact format to the flow.
8. **Engine's create-mode wording loosens from hard-coded two-tier to hook-shaped.** Today it mandates "produce each entry as a two-tier artifact … with a placeholder `Spec: <note pending>`" — which would force checkbox mechanics on outline no matter what hook (a) says. Reword: produce each entry per hook (a)'s shape; the two-tier `Spec: <note pending>` placeholder mechanics apply when that shape is two-tier.

## The change, file by file

### 1. `src/skills/roadmap-engine/SKILL.md`

- **"Roadmap File Format" section — rewrite** to the two-level grammar (canonical block above). Show: direction `##` section with prose preamble; `### Phase N — Title` headers each followed by a prose intro paragraph (no checkbox, no `Spec:` tag); tasks as flat `- [ ] **N.M — Name** — <contract line>. Spec: …` bullets directly under their phase header (flat, never indented/nested). Keep the existing contract-line rules block unchanged (files/types named, problem-first, ~600 chars, `Spec:` tag, one reason to revert) — it now describes the task tier.
- **Numbering rules** (new, in the format section): (a) phase numbers globally sequential across the file, new sections continue from the file-wide maximum, never restart, gaps legal; (b) task numbers `N.M`, `N` from the parent phase header, `M` a 1-based ordinal within the phase; (c) split sub-numbering: splitting numbered task `N.M` yields children `N.M.1 … N.M.k` in chain order, original line becomes the last child; outside references to `N.M` remain valid as family references; (d) flat fallback: a file (or file region) without phase headers keeps the flat unnumbered bullet format — never invent headers to number against.
- **Create-mode loosening** (maintenance-flow section): reword the draft step per decision 8. Touch only the two-tier/placeholder sentences; the rest of the flow (draft in memory, confirm menu, notes-after-confirmation) unchanged.
- Engine stays caller-agnostic: no skill names in the format section (note 38's rule). The reverse-graph marker and load-once framing unchanged.

### 2. `src/skills/roadmap-outline/SKILL.md`

- **Hook (a) — full rewrite.** An entry is a **phase**: `### Phase N — <Title>` header plus a prose intro paragraph (the gate/"blocked on X", the problem today, key contracts and pinned decisions the phase rests on) — **never a checkbox bullet, no contract line, no `Spec:` tag**. Numbering: continue from the highest phase number anywhere in the file (per the engine's file-level invariant); when creating the first phases of a new direction section, also emit the `##` direction header and preamble prose. 5–15 phases stays as the granularity sweet spot; dependencies-first ordering stays; "phases are what `/roadmap-decompose` fills with tasks" replaces "milestones later serve as phase names".
- **Parity carry-overs:** the `[x]`-on-first-run carry-over dies (no checkboxes to mark); the gather-input question stays.
- **Check mode:** explicitly opt out — outline registers no check mode (nothing to scan at this tier; progress is derived from `N.M` tasks). Create/update modes and the confirm cycle stay on the engine's flow.
- **Spec-note clause:** delete the "optional at this tier" paragraph entirely (decision 6); links in prose are permitted, stated in one sentence.
- **Critical Rules:** update to match (phases not milestones; two-tier rule replaced by "phases render as headers + prose per the engine's format; tasks are decompose's tier"; NO-implementation rule unchanged).

### 3. `src/skills/roadmap-decompose/SKILL.md`

- **Hook (a) — add the numbering rule.** Tasks are emitted as flat checkbox bullets directly under their parent `### Phase N` header, numbered `**N.M — Name**` (`N` from the header, `M` 1-based ordinal continuing after the highest existing `M` in that phase). Everything else about a task is unchanged: two-tier per the engine (contract line + spec note + `Spec:` tag), atomicity gate, dependencies-first ordering. **Fallback:** target file/region has no phase headers → emit unnumbered bullets exactly as today; never invent a phase header.
- **"Decompose existing" (hook d):** when a split of an already-numbered task `N.M` is offered and accepted, number per the engine's sub-numbering rule — children `N.M.1 … N.M.k`, original line becomes the last child; note-handling rules unchanged.

### 4. `src/skills/roadmap-decompose-skeleton/SKILL.md`

- **Disposition section:** inserted skeleton/TDD/contract milestones for target task `N.M` are numbered `N.M.1 … N.M.(k-1)` in chain order (skeleton → TDD/contract → …), and the original impl line — kept in place per the existing rule — is **renumbered to `N.M.k`** (last child); its contract line text and `Spec:` note tag stay. Unnumbered target task (flat roadmap) → insertions stay unnumbered, today's behavior. No renumbering outside the family.

### 5. `src/skills/roadmap-prune/SKILL.md`

- **One rule in the sweep:** after deleting a phase's last task, delete the now-empty `### Phase N` header and its intro prose; never renumber surviving phases — gaps are historic. (The existing "Never copy a phase or section header as a feature name" rule is untouched and unrelated.)

## Guards

- **Engine callers are the contract:** exactly three skills load `roadmap-engine` (outline, decompose, skeleton — verified by grep this session); every engine edit must keep all three hooks coherent. No caller names enter the engine.
- **`ROADMAP_TESTS.md` stays flat** — decompose's test routing is untouched; the fallback covers it.
- **Lazy migration:** no project roadmap is edited by this task; old flat roadmaps keep working via the fallback. The grammar applies as roadmaps live.
- **Direction preamble and phase intro are prose, not bullets** — output register is behavior (CLAUDE.md rule); do not compress them into bullet lists in the format example.
- **≤500 lines** per file; the engine gains a format block but the flat example it replaces is similar size.
- **Live-run verification:** the refactor is unverified until a live run — outline creating a new direction section in a file with existing phases (numbering must continue, not restart), decompose filling a phase with `N.M` tasks, skeleton splitting a numbered task into `N.M.x` — compares against the tradeoxy reference roadmaps.

## How to verify

1. `grep -n "Phase N" src/skills/roadmap-engine/SKILL.md` — format section shows the two-level grammar; `grep -n "## Milestones" src/skills/roadmap-engine/SKILL.md` — the stale flat example is gone.
2. `grep -n "checkbox\|Spec:" src/skills/roadmap-outline/SKILL.md` — hook (a) forbids checkboxes/`Spec:` at the phase tier; no "optional at this tier" clause remains.
3. `grep -n "N.M" src/skills/roadmap-decompose/SKILL.md src/skills/roadmap-decompose-skeleton/SKILL.md` — numbering + sub-numbering rules present, with the flat fallback stated in decompose.
4. `grep -n "empty\|header" src/skills/roadmap-prune/SKILL.md` — emptied-phase sweep rule present.
5. Live run per Guards.
