# Plan Review: agent-architect — the architect's own state survives the compact

**Plan reviewed:** `.ai-factory/plans/trickster77777/13-26-1-agent-architect-the-architect-s-own-state-survives-the-compact.md`
**Governing spec:** `.ai-factory/specs/trickster77777/93-architect-state-survives-the-compact.md` (Phase 26 header carries no `Governing spec:`)
**Target file:** `src/skills/agent-architect/SKILL.md` — two regions only
**Risk Level:** 🟡 Medium
**Round:** 1

## Context Gates

- **Architecture** (`.ai-factory/ARCHITECTURE.md`, present): § "Composition: mechanism vs policy" (`:32-39`) governs when content becomes its own skill. This task extracts nothing and adds no `loads:` edge — it rewrites two regions of one philosophy skill and explicitly guards the frontmatter. `:22` already places `agent-architect` in `src/skills/` opposite the `editor` agent definition; no boundary is crossed. **OK**
- **Rules** (`.ai-factory/RULES.md`): not present — gate skipped (optional file). No `.ai-factory/skill-context/aif-review/SKILL.md` either.
- **Roadmap** (`.ai-factory/roadmaps/trickster77777.md:88`): 26.1 is a live `[ ]` contract line under Phase 26 (owner `trickster77777@gmail.com`); its `Spec:` tag resolves to `93-architect-state-survives-the-compact.md`, which exists. The phase intro pins the order 26.4 → 26.1 → 26.3, and 26.4 is `[x]` at `27ab9cb`, so the pairing role this task records already exists as a concept (`src/skills/architect-pairing-engine/SKILL.md:30`, `:48` — "deciding" / "applying", the exact names the plan uses). Linkage intact. **OK**

## Ground truth re-checked

Every anchor and value the plan asserts was re-read fresh, not taken from its prose:

- `src/skills/agent-architect/SKILL.md:47-58` and `:161-169` match the spec's quoted text; both anchors are valid, and both are reachable by the plan's stated fallback anchors (the opening sentence "Before a compact, …" and the `## Your buffer is yours alone` heading). The paragraph does sit between the engine-load paragraph (`:42-45`) and `## Relay on the marker…` (`:60`).
- Frontmatter `:13` grants `Read Grep Glob Bash Write Edit AskUserQuestion Agent SendMessage Skill` — the meta.json fallback and the buffer write are already covered, and `ListAgents` is absent, exactly as the plan's guard states. `:14` already names both engines.
- The meta.json shape is real: `~/.claude/projects/-Users-max-projects-sakshi-orchestrator/<session-id>/subagents/agent-<id>.meta.json` exists and contains `{"agentType":"editor",…}`; the `<project-key>` derivation (working directory path, separators → hyphens, leading slash included) reproduces the directory name exactly.
- The `Agent` tool schema in this build exposes no `name:` parameter — the plan's conditional phrasing ("wherever the running build exposes it", never the carrier) is the correct handling, and matches the spec's Prevention section.
- Verification commands run against the live tree: `git status --porcelain -- ':!.ai-factory'` is accepted by the installed git (2.50.1) and returns **empty** today, so " M src/skills/agent-architect/SKILL.md" really will be the whole delta under that pathspec; `git diff --stat` is likewise empty, so "exactly one file changed" holds. The `grep -n "name:"` caveat is right — `:2` (`name: agent-architect`) is the only other hit.
- The plan's two interpretive calls are sound. The digest clause is not among the spec's "three recorded things", so nothing retires it, and reading "alone" as scoped to buffer-held state is the only reading that leaves the spec self-consistent. Buffer-creation-at-spawn is a consequence of the at-spawn write, not new machinery, and the guarded path form is untouched by it.

## Critical Issues

**1. The fallback's trigger is pinned to history ("never recorded") while the state it must cover is "you don't hold it" — and the diff creates a second way to not hold a recorded handle.**

Task 1 item 2 writes the handle into the buffer at spawn. Item 1 makes the handoff carry *only* the buffer's path. Item 3 then names the meta.json fallback "For a handle that was **never recorded**." That leaves one state stated nowhere: the handle **was** recorded, into a buffer whose path did not reach the recovering architect — an auto-compact that fired before any handoff was written, or a handoff written for someone else. The file itself already admits this case exists: `:182-183` says "if one exists, the pre-compact handoff", so a compact with no handoff is a state the skill acknowledges today. In it, the fallback's antecedent is literally false, the spec's guard forbids a directory scan to locate the buffer, and the architect is left with no stated route — so it re-spawns and silently orphans a live editor and its buffer, which is exactly what the paragraph's own closing sentence names as the defect.

This is the failure class the task exists to close, and this is where it recurs: the last time this file named an outcome without naming the route, the architect filled the gap with `ListAgents` and reported a live editor dead (spec, Defect C). Closing it costs one clause inside the region already being rewritten — state the trigger as the recovery-time state rather than the recording history, e.g. "a handle you do not hold at recovery — never recorded, or recorded in a buffer whose path did not reach you." That satisfies the spec's rule *a fortiori* (a never-recorded handle is one you do not hold), keeps the `grep -n "subagents/agent-"` verification intact, adds no machinery, and reopens nothing the guards retired.

**2. `:183` is falsified by this diff and left stale inside the file the diff changes.**

`:183` — "the pre-compact handoff that recorded your editor's handle" — is, after this change, wrong: the handoff records the buffer's path, and the handle lives in the buffer. The plan sees this and books it as "known residue, deliberately out of scope" on the strength of the spec's `Files & types` bound. That bound reads "no restructuring beyond them", and correcting one noun phrase this diff itself falsifies is not restructuring — it is the same file, one clause, no new file in the diff, and every verification assertion (`git diff --stat` = one file; `git status --porcelain -- ':!.ai-factory'` = one entry) still passes unchanged.

The placement is what makes it more than cosmetic: `:180-183` is `## On every invocation` — the recovery entry point, the first thing a post-compact architect reads. Shipping a recovery instruction that names the wrong carrier, in the very task whose purpose is that the carrier survives a compact, reintroduces at `:183` the defect being removed at `:47-58`. Fold the one-clause correction ("…that recorded your buffer's path") into task 1 and say so in the guards; if the planner reads the spec's region bound as absolute instead, that is a decision above the plan and belongs in an escalation, not in a residue note.

**3. The pairing role is given a home but no recording moment.**

The contract line asks to "record the editor's handle and any assigned pairing role in the buffer". Task 1 item 2 gives the handle a precise moment ("at the moment the editor is spawned") but gives the role only a home ("the buffer, not the handoff, is where the handle and any assigned pairing role live"). That is the outcome-without-the-mechanism shape the whole phase is correcting — an architect assigned a role mid-session is told where it lives, never when to write it. One clause on the same sentence closes it: the role is written there when the user assigns it. No new content beyond what the contract line already asks for.

## Positive Notes

- The plan does the grounding work rather than trusting the spec: it re-read both regions byte-for-byte, confirmed the meta.json shape on disk, and confirmed the `Agent` schema has no `name:` — which is what turns the spec's "wherever the build exposes it" from a hedge into a checked fact.
- Both interpretive calls are stated up front with their reasoning and their scope, so the implementer inherits decisions instead of guessing them. The digest-stays call in particular resolves a real ambiguity in the roadmap line's "alone" without widening the diff.
- The retired-machinery guard is restated as a hard boundary in the task that could reintroduce it, naming the prior attempt explicitly — the right place for it, and stronger than the spec's own phrasing because it also forbids offering it as an option.
- The one-home discipline between the two tasks is clean: the buffer section points at the paragraph's mechanism instead of restating the liveness test, the `name:` convenience, or the fallback.
- The verification step is executable as written — the pathspec form, the porcelain codes, and the `grep -n "name:"` false-positive caveat all match what this tree and this git actually produce — and it correctly forbids reverting anything under `.ai-factory/`.

## Deferred observations

- Affects: Phase 26 / `.ai-factory/specs/trickster77777/93-architect-state-survives-the-compact.md` — the fallback path pins `<project-key>`'s derivation ("the working directory's path with separators replaced by hyphens") but leaves `<session-id>` as "the running session's own id" with no derivation, while the guard "no line rests on undocumented harness behavior" applies to the same sentence. It is resolvable in practice (the environment carries `CLAUDE_CODE_SESSION_ID`, and "newest first by file mtime" degrades gracefully to a glob across session directories), so it blocks nothing here; but it is the one placeholder in the rewritten paragraph a recovering architect must resolve without being told how, and closing it belongs to whoever next opens that sentence's spec.
- Affects: Phase 26 / `.ai-factory/specs/trickster77777/95-architect-pairing-roles.md` — this task makes `agent-architect/SKILL.md` the second skill body to name "the deciding half" and "the applying half", and `docs/reserved-words.md` § "Paired loop" still registers only *architect* and *editor*. Carried forward from the 26.4 plan-review, now with its second naming site concrete: two skill bodies using an unregistered pair of concepts is precisely the drift the one-word-one-meaning contract exists to catch. One registry entry from whoever closes Phase 26.
