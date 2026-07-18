# Plan: 16.1 — Rename milestone-rescue → task-rescue and milestone-rescue-audit → task-rescue-audit

## Context

`milestone` is retired from the reserved-words vocabulary (the unit is task), and skill names sit on the fixed-form axis — machine-resolved identifiers. This task changes the identity of the two rescue skills (directories, `name:` frontmatter, in-body self-references, `active/` symlinks, live cross-references) with zero behavior change. Frozen `.ai-factory` history and historical `[x]` roadmap lines keep the old names.

**Deviations from the governing spec** (`.ai-factory/specs/71-rescue-skills-rename.md`). Each is this plan's own ground-truth finding, derived by reading the files — no prior review is cited, and none is relied on:

1. **DEVIATION — `orchestrator-artifacts` carries a third live reference.**
   *Spec said:* Scope lists only the reverse-graph marker for this file (`SKILL.md:7`, both names on one line).
   *File showed:* `SKILL.md:44` also carries `milestone-rescue` — "its only skill-side writer", in the § 3 sidecar-fields prose. A live reference to the identifier.
   *Done:* included in Task 6. Without it the spec's own verification grep over `src` cannot reach zero, so the spec is internally inconsistent here and the file wins.

2. **DEVIATION — the spec's reference counts are per line, not per occurrence.**
   *Spec said:* `skill-cycle.md` ×4, `CLAUDE.md` ×4.
   *File showed:* 4 lines / 6 occurrences and 4 lines / 7 occurrences respectively — several lines carry both names.
   *Done:* every task below pins exact line numbers instead of repeating the ambiguous count. Read as occurrences, the spec would under-count by three.

3. **DEVIATION — two always-loaded docs use the old name as their worked example.**
   *Spec said:* Scope omits `docs/reserved-words.md` and `docs/using-the-language.md`; the verification grep is scoped to `docs/philosophy/skill-cycle.md`, not `docs`.
   *File showed:* `reserved-words.md:11` and `using-the-language.md:35` both cite `` `milestone-rescue` `` as the illustrative machine-resolved name, and both files are `@`-imported into every session through the sakshi root `CLAUDE.md`.
   *Done:* Task 5 substitutes the identifier inside the backticks only. **This is the one judgement call in the plan and the implementer should confirm it, not assume it.** The reasoning: leaving it would ship always-loaded context naming a skill that does not exist, and both sentences are *about* the fixed-form axis rather than about the example, so they stay true under the substitution. If judged out of scope, dropping Task 5 leaves the spec's stated verification passing either way — nothing else depends on it.

The seven target files below were confirmed as the complete set of live surfaces by a repo-wide sweep excluding `.git`, `.ai-factory/`, and `upstream/`; `README.md`, `AGENTS.md`, `src/commands/`, `src/agents/`, `src/global/CLAUDE.md`, `scripts/`, `.claude/*.json`, and the sakshi root `CLAUDE.md` are clean.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Rename the directories and their contents

- [x] **Task 1: `git mv` both skill directories**
  Files: `src/skills/milestone-rescue/` → `src/skills/task-rescue/`, `src/skills/milestone-rescue-audit/` → `src/skills/task-rescue-audit/`
  Run `git mv src/skills/milestone-rescue src/skills/task-rescue` and `git mv src/skills/milestone-rescue-audit src/skills/task-rescue-audit`. Use `git mv` (not plain `mv`) so history follows. Do not touch file contents in this task.

- [x] **Task 2: Update `name:` frontmatter and in-body self-references in `task-rescue`** (depends on Task 1)
  Files: `src/skills/task-rescue/SKILL.md`
  Five references, at the pre-move line numbers: `2` (`name: milestone-rescue` → `name: task-rescue`), `151`, `439`, `440`, `476` (all `` `milestone-rescue-audit` `` → `` `task-rescue-audit` ``). The `name:` value must match the new directory name exactly — this is the hard constraint that makes the skill resolve. Leave `loads: orchestrator-artifacts roadmap-engine` (line 14) byte-identical. Change nothing else: prose beyond identifier self-references is Phase 17.3's, not this task's.

- [x] **Task 3: Update `name:` frontmatter and in-body self-references in `task-rescue-audit`** (depends on Task 1)
  Files: `src/skills/task-rescue-audit/SKILL.md`
  Four references, at the pre-move line numbers: `2` (`name: milestone-rescue-audit` → `name: task-rescue-audit`), `9` (inside the `description:` frontmatter — "Run right after `milestone-rescue`"), `32`, `167` (both `` `milestone-rescue` `` → `` `task-rescue` ``). Line 9 sits in the always-loaded skill description, so it must change with the rest. Leave `loads: orchestrator-artifacts` (line 16) byte-identical.

- [x] **Task 4: Rename and repoint the `active/skills/` symlinks** (depends on Task 1)
  Files: `active/skills/milestone-rescue` → `active/skills/task-rescue`, `active/skills/milestone-rescue-audit` → `active/skills/task-rescue-audit`
  Both symlinks are git-tracked and relative. Remove the old entries and create the new ones pointing at the renamed directories, e.g. `git rm active/skills/milestone-rescue active/skills/milestone-rescue-audit`, then `ln -sfn ../../src/skills/task-rescue active/skills/task-rescue` and `ln -sfn ../../src/skills/task-rescue-audit active/skills/task-rescue-audit`, then `git add` them. Follow the existing relative form (`../../src/skills/<name>`) used by every other symlink in the directory — the depth is exactly two levels.
  Verify by **dereferencing**, not by listing: `ls -L active/skills/task-rescue/SKILL.md active/skills/task-rescue-audit/SKILL.md` must succeed for both. A plain `ls -l` prints a plausible-looking line whether or not the target exists, so it cannot catch a dangling or wrong-depth link (`../src/skills/…` instead of `../../`) — the one filesystem mistake this task can actually make. The old symlink names must be gone, not left behind.

### Phase 2: Update live cross-references

*Tasks 5–8 are independent of Phase 1 and of each other — each touches a file the `git mv` does not move, and none reads anything Phase 1 writes. They may run in any order, before or after Phase 1, and in parallel.*

- [x] **Task 5: Update the machine-resolved-name example in the two language docs** (no dependencies)
  Files: `docs/reserved-words.md`, `docs/using-the-language.md`
  `reserved-words.md:11` and `using-the-language.md:35` both use `` (`milestone-rescue`) `` as the parenthetical example of a skill/directory name on the fixed-form axis. Replace the example string with `` `task-rescue` `` in both. Change only the identifier inside the backticks — the sentences around it are correct as written and must stay. See assumption 3 in Context for why this is included.

- [x] **Task 6: Update `orchestrator-artifacts` cross-references** (no dependencies)
  Files: `src/skills/orchestrator-artifacts/SKILL.md`
  Two lines. Line `7` (the reverse-graph marker, inside the `description:` frontmatter): "Loaded by milestone-rescue, milestone-rescue-audit, and roadmap-prune" → "Loaded by task-rescue, task-rescue-audit, and roadmap-prune". Line `44` (§ 3 Sidecar fields): "live in `milestone-rescue`, its only skill-side writer" → "live in `task-rescue`, its only skill-side writer". `roadmap-engine`'s reverse marker is grep-based rather than a hardcoded list — it needs no edit.

- [x] **Task 7: Update `docs/philosophy/skill-cycle.md`** (no dependencies)
  Files: `docs/philosophy/skill-cycle.md`
  Four lines, six occurrences: line `41` (the `##` heading, both names), line `43` (body prose, both names), line `70` and `71` (the ASCII pipeline diagram, one name each). The doc is in Russian; only the identifiers change, no surrounding prose.

  **Diagram alignment — pad, do not move the arrows.** The rule is self-verifying and is the one to follow: both names shorten by exactly 5 characters, so **add 5 spaces of padding to each of lines 70 and 71**, leaving the `←` exactly where it is. Do not shift the arrows left to hug the shortened names — that would leave two rows offset from the other seven, and no grep in Task 9 can catch a broken diagram.

  As a cross-check only: lines 70–71's `←` shares the diagram's arrow column with the `→` on lines 61–64, 67, 74 and 77, at **character column 42** (the deeper-indented lines 65–66 and 75–76 are a separate nested column and are not touched). **Measure characters, not bytes.** This block mixes box-drawing and Cyrillic, so byte offsets run ~2 higher than the character column and vary line to line; `awk index()` and many editors' column readouts report bytes and will disagree with this figure. If a measurement conflicts with the "+5 spaces" rule, the rule wins.

- [x] **Task 8: Update the repo `CLAUDE.md`** (no dependencies)
  Files: `CLAUDE.md`
  Four lines, seven occurrences: line `36` (Skill cycle table row — "`milestone-rescue`/`-audit`"), line `57` (the repository-structure tree — the `milestone-rescue/` entry and the `milestone-rescue-audit` mention in its trailing comment), line `78` (the active-set enumeration), line `193` (the upstream-sync "everything else is ours, never overwritten" list). Both lists are alphabetically loose but grouped — keep each name in its existing position rather than re-sorting.

  **Tree alignment — same rule as Task 7.** `milestone-rescue/` → `task-rescue/` shortens by 5, so **add 5 spaces** to line 57 to leave its `#` exactly where it is; do not pull the comment left. Only line 57 is edited — every other row in the block already sits correctly and none is touched.

  As a cross-check only: line 57's `#` sits at **character column 35**, shared with lines 48, 49, 51, 52, 55, 56, 58 and 59 (line 50 is the one genuine outlier, at 41). **Measure characters, not bytes** — the same trap as Task 7, and sharper here: line 58's byte offset differs from its neighbours' while its character column is identical, so a byte-based reading makes a correctly-aligned block look ragged. The two files' columns are unrelated (42 in `skill-cycle.md`, 35 here) — never carry a number across.

### Phase 3: Verify

- [ ] **Task 9: Verify the rename is complete and behavior is unchanged** (depends on Tasks 2–8)
  Files: none (verification only)
  HANDED TO NEXT SESSION, NOT PASSED: textual state, frozen-history negative control, and filesystem state all verified clean in this session (see below); the behavior check (invoking `/task-rescue` and `/task-rescue-audit` in a fresh session) could not run here per the task's own instruction — this is the same session that performed the rename, so the skills manifest is stale. A fresh session must run that check before this task is marked done.
  - Textual: `grep -rIn 'milestone-rescue' src active docs CLAUDE.md` → zero hits. Confirmed.
  - Frozen history: `grep -rIn 'milestone-rescue' .ai-factory/` → 50 hits (still present, as required).
  - Filesystem: `ls -L active/skills/task-rescue/SKILL.md active/skills/task-rescue-audit/SKILL.md` → both succeed; `name:` in each matches its directory; `ls active/skills/ | grep -c milestone` → 0; `git status --porcelain active/skills/` shows the two old paths `D` and the two new paths `A`.

  **Textual state.** Run `grep -rIn 'milestone-rescue' src active docs CLAUDE.md` → must return zero hits (the spec's grep scopes `docs` to `skill-cycle.md`; with Task 5 done the wider `docs` sweep is also clean).

  **Frozen history — negative control.** Run `grep -rIn 'milestone-rescue' .ai-factory/` → must *still* return hits: frozen history and historical `[x]` roadmap lines are deliberately untouched. If this returns zero, history was wrongly rewritten and must be restored.

  **Filesystem state.** `ls -L active/skills/task-rescue/SKILL.md active/skills/task-rescue-audit/SKILL.md` must succeed for both — the dereferencing form, for the reason given in Task 4. Confirm each renamed `SKILL.md`'s `name:` value matches its directory name exactly. The old names must be provably gone: `ls active/skills/ | grep -c milestone` must return 0 — the textual grep above cannot see a leftover symlink (`grep -r` skips symlinks and never matches on filenames), so a surviving `active/skills/milestone-rescue` passes every other check while `~/.claude/skills` still loads it. And `git status --porcelain active/skills/` must show the two old paths deleted and the two new paths added — catching a `git rm` that was forgotten or never staged.

  **Behavior — the spec's third verification bullet. Runs in a FRESH session, not this one.** The checks above prove the textual and filesystem state is *consistent*; they do not prove the skills still **resolve and load**, which is the one thing this task can break. In a new session started after Tasks 1–8 are complete, invoke `/task-rescue` and `/task-rescue-audit` and confirm each loads and runs as before the rename, and that `orchestrator-artifacts`' reverse marker names the new callers.

  Why a fresh session is mandatory: `~/.claude/skills` → `active/skills/` (verified), and Claude Code builds its skills manifest at session start. Inside the session that performs the rename the manifest is stale — `/task-rescue` will report "skill not found" because it did not exist when the manifest was built, and `/milestone-rescue` may still appear to resolve while pointing at a deleted path. **Both results are expected in-session and are not evidence of failure.** Do not act on them, and do not conclude the rename is broken.

  This check is not redundant with the symlink check: a link created at the wrong relative depth still passes every grep and still prints as a symlink, yet the skill fails to load — silently, until someone needs it. If no fresh session is available, mark this check **handed to the next session, not passed**, and say so explicitly rather than reporting Task 9 green.

  **Do not edit `.ai-factory/ROADMAP.md`.** Its `[x]` lines are the archival record. Note that one *live* line does still contain `milestone-rescue`: `ROADMAP.md:27`, the unchecked contract line for 17.1, in the parenthetical "the `milestone-rescue` name refs are Phase 16's". That is a scope-exclusion note on another task's contract line — a statement about which task owns those refs, not a live identifier this rename must chase — and it is outside 16.1's file boundary. After Phase 16 lands it reads as moot rather than wrong, and 17.1 rewrites that region on its own pass. So the `grep` in the first check is deliberately scoped to `src active docs CLAUDE.md` and does not include `.ai-factory/`.

  **Cross-repo: the orchestrator side already landed — this task is the trailing half.** Do not read this as a rename running ahead of a pending handoff. Orchestrator task `8.2` is `[x]` (`orchestrator/.ai-factory/roadmaps/trickster77777.md:51`), executed **doc-first** by owner decision: `orchestrator/docs/how-it-works.md:25` and `docs/non-convergence.md:37` already say `/task-rescue` and `/task-rescue-audit`, and 8.2's contract line names skills 16.1 as the reconciliation. Those docs are the governing spec and they lead; until this task lands, **the skills repo is the known-divergent side**. Nothing in Tasks 1–8 changes as a result — the orchestrator repo's files stay out of scope — but an implementer who hits an ambiguity should resolve it toward the names the orchestrator docs already publish, not treat the question as open.
