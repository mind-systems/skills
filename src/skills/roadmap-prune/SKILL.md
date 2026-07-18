---
name: roadmap-prune
description: >-
  Prunes completed tasks from ROADMAP.md by grouping them into named features,
  anchoring each feature to its commit hash in ARCHITECTURE.md, sweeping the
  completed work's artifact dirs and specs, and deleting the pruned tasks from
  the roadmap. Use when ROADMAP.md has accumulated many [x] tasks and needs to
  be trimmed without losing navigational history.
argument-hint: "[path/to/ROADMAP.md]"
allowed-tools: Read Write Edit Bash(git *) Bash(rm *) Bash(find *) Glob Grep Skill
loads: orchestrator-artifacts
---

# Roadmap Prune

**Features-table format version:** `roadmap-prune v2` — the version stamped into the
`## Features` header; an unmarked/legacy `## Features` header is v1. Every read of the
`## Features` header inside this skill — Step 2's classification read, the self-heal
marker read (4.2a), and Step 4.2's find-or-create — matches the stable base
`## Features` by prefix, tolerating an optional ` (roadmap-prune vN)` suffix, never by
exact `^## Features$`, so both a versioned header and an unmarked legacy header resolve
at every read site.

**Out-of-scope assumption:** a force-push / shared-history rewrite invalidates every
hash in the Features table (feature rows and ledger alike); defending against it is out
of scope (repo policy: shared history is not rewritten) — recovery is to delete the
version marker from the header and re-run the prune so self-heal rebuilds from the
rewritten history.

---

## Step 0 — Deferred-observations gate

Ensure `orchestrator-artifacts` is loaded once this chat (via the Skill tool, only if
not already loaded) — it defines the `## Deferred observations` section format and the
status-marker grammar / **pinned** definition referenced below.

1. Derive the target repo root from the skill argument (parent of the `.ai-factory/`
   holding the target ROADMAP.md) — same anchoring rule Step 5 uses.
2. Scan every `.md` file under `<target repo root>/.ai-factory/plan-reviews/` and
   `<target repo root>/.ai-factory/reviews/`, at any depth (including files nested in
   per-roadmap stem subdirectories), for a `## Deferred observations` section. This
   scan is repo-wide by design — prune is an integration-branch act, so any
   developer's unpinned observation blocks it regardless of author; do not scope the
   scan to the pruned roadmap's stem. A file with no such section contributes nothing
   to this step — but capture it for step 6 below, before moving on, if it falls
   within Step 5's sweep scope for this prune (the flat `plan-reviews/`/`reviews/`
   files for a default-pair prune, or the pruned stem's `plan-reviews/<stem>/` and
   `reviews/<stem>/` files for a named prune) — Step 5 deletes only those files and
   Step 8 runs after the sweep. A file outside that sweep scope is scanned for the
   gate here but not handed off to step 6 (the gate scan stays repo-wide; margin
   capture follows the sweep scope, not the reverse).
3. Collect every entry line that is **not pinned** per the engine's grammar (pinned =
   the entry line carries ≥1 bracketed status marker — do not redefine, cite the
   engine).
4. If any unpinned entry exists → stop the skill entirely: print one line per unpinned
   entry as `<file>:<line> — <entry text>`, state that pruning is blocked until every
   entry is pinned, and name the resolution — the prune is parked, not engineered
   around:
   1. the user runs `/command-handoff` on this session — the handoff carries every
      unpinned observation (gist, original reviewer text, `Affects:`, `file:line` of
      the entry) plus the gate context into `.ai-factory/handoffs/`;
   2. a **dedicated resolution session** works through the findings — fixing, routing
      into an **open** task's spec, or dismissing — and sets pins per
      `orchestrator-artifacts` § 6 (`[fixed]` / `[routed → <path>]` / `[dismissed]`);
   3. `roadmap-prune` is re-run when every entry is pinned; the gate passing is the
      resolution's proof, never manufactured.
   Make no edits, no sweep, no ARCHITECTURE/ROADMAP changes, no partial prune.
5. If none are unpinned → proceed to `## Before you start` and the normal flow,
   unchanged.
6. While scanning, for every file that has **no** `## Deferred observations` section
   **and falls within Step 5's sweep scope for this prune** (per item 2's hand-off
   clause above — at any depth, scoped to the sweep, never repo-wide), also check it
   for any pre-standardization marker phrase — `latent`, `forward risk`, `no action
   needed`, `out of scope for this milestone`, `flagging so Phase`, `Surface this to
   the orchestrator`. Capture the matching paragraph(s) with their source file now,
   before Step 5 deletes the file — Step 8 only echoes what is captured here, it
   never re-reads these dirs.

`ROADMAP_TESTS.md` parity: the gate scans the shared `plan-reviews/`/`reviews/`
trees, at any depth, identically in both modes; `test-runs/` files carry no review
sections and are not scanned. Prune never promotes, evaluates, or marks entries —
this gate is read-and-refuse only.

---

## Before you start

Read the target ROADMAP.md in full — do not start grouping until you have read every `[x]` task.

---

## Step 1 — Identify the pruning slice

Count all `[x]` tasks. The pruning slice is **all `[x]` tasks** — every completed
task is pruned by default.

The only exception is a `[x]` line the user explicitly names for retention at
invocation. Absent such an explicit instruction, prune every `[x]` task; the history
is preserved in git and ARCHITECTURE.md. The run's end — all changes left in the
working tree before the on-request commit (see Commit, below) — is an informal
second chance to catch a task that should have been kept, not a formal gate.

---

## Step 2 — Classify, then group tasks into features

Before grouping, read `.ai-factory/ARCHITECTURE.md` `## Features` table (if the file
exists) to learn what features have already been anchored. If ARCHITECTURE.md does not
exist yet (first-ever prune), skip gracefully and proceed with fresh grouping.

### 2.1 — Classify every task

For every task in the pruning slice, ask one question:

> "Could you write an e2e test for this that didn't exist before?"

If yes — it's a feature. Any verifiable interaction counts: user→system, system→system,
system→external service, or a distinct internal subsystem with its own behaviour
contract (e.g. structured logging with disk persistence and replay). If no — it's
internal.

Based on the answer, assign one of three outcomes:

| Outcome | Signal | Action |
|---------|--------|--------|
| **New feature** | New e2e scenario becomes possible | Create a new feature row |
| **Extended feature** | Existing e2e scenario gains new parameters or coverage | Append hash to existing row |
| **Internal only** | No new e2e behaviour — refactor, cleanup, dep fix, arch change | No feature row and no hash recorded anywhere — captured by the nearest prune snapshot |

Rules:
- Never copy a phase or section header as a feature name. Phase headers organise work; feature names describe what the system can do.
- A refactor that enables a future feature is still internal — it gets no feature row and no hash anywhere.
- When uncertain between new vs. extended: prefer extending an existing row.
- **Internal-only items never get a named row in the Features table.** Refactors, renames, cleanups, doc fixes, migration changes, and dependency updates write no hash anywhere — they are captured by the nearest prune snapshot. The only named row under **Internal** is `Roadmap drop history`.

### 2.2 — Group and name

Group tasks that share the same capability outcome. A group that spans many tasks but
delivers one operator-visible thing is still one feature row.

- Tasks that implement the same capability belong together
  (e.g. "gRPC client" + "gRPC signal stream" + "Remove `/webhooks/core` route" → **gRPC transport**)
- Tasks that are explicitly marked as sub-items of a larger item belong together
- When uncertain: prefer fewer, larger features over many small ones

Name each feature in 2–5 words from the operator's perspective (what it does, not how it's built).

Then sort the features by domain and group them under bold section headers. Features in the same
domain (e.g. all transport-layer work, all persistence work, all UI panels) should be adjacent.
Domain names reflect the product boundaries of this specific project, not generic labels.

Internal/refactor work goes last under an **Internal** header. The only rows under **Internal** are:
- Named rows for significant architectural subsystems established during this prune (e.g. a new layer pattern, a new protocol integration) — only if the subsystem has its own behaviour contract
- `Roadmap drop history` — always the last row; it holds exactly one hash per prune — the Step-4.1 snapshot, the last known intact roadmap before that prune (the commit before which the prune deleted roadmap lines; equivalently `<prune-commit>^`). Storing the snapshot is what makes `git show <hash>:.ai-factory/ROADMAP.md` reconstruct the pre-prune roadmap directly. In a multiuser project (`.ai-factory/roadmaps/` exists), the snapshot commit holds all files, so one repo-wide ledger serves every roadmap — `git show <snapshot>:<roadmap path>` reconstructs any roadmap at that prune; no per-roadmap ledger rows. Maintenance work (refactors, cleanups, dep fixes, renames, doc changes) writes no hash anywhere — it is captured by the nearest prune snapshot, never a named row

Example structure:

```
| Feature | Hashes |
|---------|--------|
| **<Domain A>** | |
| <What a user can do> | abc1234 |
| <What a user can do, extended> | def5678 9a3bc12 |
| **<Domain B>** | |
| <What service A delivers to service B> | c7d4a88 |
| <What the system does end-to-end> | e1f2g3h |
| **Internal** | |
| Roadmap drop history | 5d1284c |
```

Use an empty Hashes cell (`| |`) for section header rows — they are visual separators, not features.

---

## Step 3 — Find the commit hash for each feature

For each feature, find the commit where its last task was closed.

```bash
# Find commits that touched ROADMAP.md
git log --oneline -- .ai-factory/ROADMAP.md

# Show ROADMAP.md as it looked at a given commit
git show <hash>:.ai-factory/ROADMAP.md

# Find the commit where a specific task was first checked off
# Strategy: look at diffs on ROADMAP.md, find the commit where
# the last task of the feature changed from [ ] to [x]
git log -p -- .ai-factory/ROADMAP.md | grep -B5 "\+- \[x\].*<task-keyword>"
```

Pick the commit where the **last task of the feature** was marked `[x]`. That is the
hash to record in ARCHITECTURE.md.

---

## Step 4 — Update ARCHITECTURE.md

**4.1 — Capture the prune snapshot hash**

Before touching any files, record the current HEAD:

```bash
git rev-parse --short HEAD
```

This hash points to the last commit where ROADMAP.md still contains all the tasks being pruned.

**4.2 — Write Features and drop history**

In a multiuser project (`.ai-factory/roadmaps/` exists), prune runs on the integration
branch, one actor, after merges — never per-developer; Features are project features
(authorship lives in commit history, not the table), and single-actor prune keeps both
the drop-history row and the feature rows single-writer.

**4.2a — Legacy self-heal pre-pass.** Before writing anything, open ARCHITECTURE.md and
read the `## Features (...)` header marker (matched by prefix, per the format-version
line above `## Step 0`):

- **Marker == current version** (`roadmap-prune v2`) → nothing to migrate; proceed to
  the write below.
- **Marker absent or older** → rebuild the drop-history row wholesale from git ground
  truth, then stamp the current version:
  1. Enumerate the repo's prune commits **on the current branch only** (never `--all`):
     `git log --format='%h %s' -- .ai-factory/ROADMAP.md` filtered to the prune-message
     set — `Roadmap prune` (the exact message pinned in the "Commit (on request only)"
     section below — do not alter that section, this pre-pass relies on it), plus the
     historic manual wordings `Remove complete plans` and `Rmove complete plans`.
     **Content-verify each candidate:** its diff must actually delete `[x]` lines from
     `.ai-factory/ROADMAP.md` — an artifact-sweep twin that touches no contract line is
     skipped and reported, never ledgered.
  2. For each verified candidate, the ledger entry is its **parent** (`<prune>^`).
  3. **Replace** the drop-history hashes with this reconstructed, de-duplicated,
     chronological set — the old polluting hashes are discarded; do not repair existing
     hashes in place, the rebuild is authoritative from git.
  4. **Zero prune commits found** → nothing to rebuild; stamp only.
  5. Stamp the header `## Features (roadmap-prune v2)`.

**Guard:** self-heal edits only the drop-history row and the header marker — never
feature rows, never ROADMAP.md, never specs.

*Legacy-removable:* once every consuming repo's `## Features` header shows the current
version, this 4.2a block is dead code and can be deleted (the format-version line above
`## Step 0` and the per-run stamping in the write below stay).

Open ARCHITECTURE.md. Find or create the `## Features` section — matched by prefix,
tolerating the optional ` (roadmap-prune vN)` suffix — and write/restamp its header as
`## Features (roadmap-prune v2)` (the version from the format-version line above
`## Step 0`); every run (re)stamps the current version. `temporal-tree` matches this
header **by prefix** (`## Features (roadmap-prune vN)`), so the version suffix must not
break prefix-matching. For each feature:

- If the feature already exists → append the new hash to its Hashes cell (space-separated).
- If the feature does not exist → add a new row with the hash from Step 3.

For the drop history row: find or create it at the bottom of the Features table. Guard before appending: if the row already exists and its **last** hash already equals the current Step-4.1 snapshot hash, skip the append and report it (e.g. "snapshot already ledgered — uncommitted re-run") — compare against the **last** hash only, never a whole-row scan, because two distinct prunes always have a commit between them so their snapshots differ. Otherwise append exactly the Step-4.1 snapshot hash (one per prune run), comma-separated.

Follow the table format and grouping rules from Step 2.2. Additional rules:

- Section headers are bold rows with an empty Hashes cell — pure visual separators.
- Domain names reflect the product boundaries of this specific project, not generic labels.
- Features are named from the operator's perspective (what the system can do), not from the implementation.
- `Roadmap drop history` is always the last row of the **Internal** section. It holds exactly one hash per prune — the Step-4.1 snapshot (the last known intact roadmap before that prune) — never a named row; maintenance work (refactors, arch cleanup, dep fixes, renames, doc changes) writes no hash anywhere.
- Use short (7-char) hashes throughout.

---

## Step 5 — Sweep completed artifacts and specs

Run this after Step 4 and before Step 6. Tags are captured before any ROADMAP.md line is deleted.

Derive the **target repo root**: the parent of the `.ai-factory/` directory the target ROADMAP.md lives in (from the skill argument). Anchor every deletion in this step at that root. For a sub-repo roadmap at `<subrepo>/.ai-factory/ROADMAP.md`, the target repo root is `<subrepo>`, and the sweep touches only `<subrepo>/.ai-factory/*`.

1. **Capture** the `Spec:` tag path of every `[x]` line being pruned. A user-kept `[x]`
   line's `Spec:` tag is not captured — its contract line and its spec file both stay
   untouched. A `[x]` line with no `Spec:` tag contributes nothing — skip it, never
   synthesize a path.
2. Determine the sweep scope from the same skill argument used to anchor this step,
   then delete:
   - **Default pair** — the target is `.ai-factory/ROADMAP.md` or
     `.ai-factory/ROADMAP_TESTS.md`. Check whether
     `<target repo root>/.ai-factory/roadmaps/` exists:
     - **`roadmaps/` absent (solo repo)** — `rm -rf` the three flat dirs directly
       under `<target repo root>/.ai-factory/`: `plans/`, `plan-reviews/`,
       `reviews/`.
     - **`roadmaps/` present** — delete only the regular files directly under each
       of those three flat dirs (`[ -d <dir> ] && find <dir> -maxdepth 1 -type f
       -delete`, guarding the way `rm -rf` tolerates a dir that was never
       created), preserving every developer's per-roadmap stem subdirectories
       (`plans/<stem>/`, `plan-reviews/<stem>/`, `reviews/<stem>/`) — the same
       per-stem protection the Named-roadmap branch below already gives, now
       protected from both sides: never a sibling stem's subdirectory, whichever
       side the prune runs from.
   - **Named roadmap** — the target is under `.ai-factory/roadmaps/…` — derive
     `<stem>`: a named main roadmap `roadmaps/<name>.md` gives `<stem> = <name>`; its
     test sibling `roadmaps/<name>-tests.md` also gives `<stem> = <name>` (the
     `-tests` suffix stripped — never the raw basename `<name>-tests`). `rm -rf` only
     `plans/<stem>/`, `plan-reviews/<stem>/`, `reviews/<stem>/` under
     `<target repo root>/.ai-factory/` — never the flat dirs, never a sibling stem's
     subdirectories (another developer's completed artifacts are not this prune's to
     delete).
3. `rm -f` each captured spec path — the captured paths are repo-root-relative and already begin with `.ai-factory/`; join them onto the target repo root, not onto `.ai-factory/`.

Spec deletion goes only through the **pruned** `[x]` lines' `Spec:` tags — no spec
directory is ever scanned or swept, so a user-kept `[x]` line's spec and open `[ ]`
tasks' specs are never touched.

`test-runs/` is swept only when the pruned target is the **test** roadmap —
`ROADMAP_TESTS.md` for the default pair, `roadmaps/<name>-tests.md` for a named
pair — never on a main-roadmap prune. In that case the swept dir is flat
`test-runs/` for the default pair and `test-runs/<stem>/` for a named test roadmap,
using the same `-tests`-stripped `<stem>` derived above. For the default pair, the
same `roadmaps/`-presence split from item 2 applies to flat `test-runs/`:
`roadmaps/` absent → today's whole-dir `rm -rf` of flat `test-runs/`, byte-stable;
`roadmaps/` present → delete only the regular files directly under flat
`test-runs/` (`[ -d test-runs ] && find test-runs -maxdepth 1 -type f -delete`),
preserving every `test-runs/<stem>/` subdirectory. The named-test-roadmap case is
unchanged.

---

## Step 6 — Update ROADMAP.md

Delete the pruned `[x]` tasks from the task-holding sections — a flat `## Tasks` (or
legacy `## Milestones`) list, or direction sections (`## <Direction name>` → `### Phase N` → `N.M` tasks) —
only after Step 5's tag capture has run. Do not replace them with a table — the tasks
are gone from the roadmap.

Keep the task-holding sections with all remaining `[ ]` tasks. Additionally, always
retain the last phase header, even when it is emptied of all its tasks.

**Emptied-phase sweep:** after deleting a phase's last task, if the `### Phase N`
header now has no tasks left under it, delete the header and its intro prose too —
never renumber surviving phases; numbering is historic and gaps are normal (a
deleted phase's number may still be referenced from specs, commits, and
ARCHITECTURE.md features). This coexists with the retain rule above: a phase that
still holds a user-kept `[x]` task is not emptied and keeps its header; the last
phase header is kept regardless.

**Emptied-direction sweep:** after the emptied-phase sweep removes a direction
section's last phase header, if the `## <Direction name>` section now has no phases
or tasks left under it, delete the header and its preamble prose too — never
renumber anything; phase numbering is historic and file-global, so a deleted
direction's phase numbers stay as gaps. This coexists with the retain rule above:
the retain-last-phase-header rule keeps the newest direction alive by construction,
so this sweep can only fire on older, fully-pruned directions.

---

## Step 7 — Verify

Before finishing, verify:

- Every pruned task group is represented by a feature row in ARCHITECTURE.md
- Every feature row has a real, resolvable commit hash:
  ```bash
  git cat-file -t <hash>   # should output "commit"
  ```
- ROADMAP.md has no orphaned `[x]` tasks (all checked items are either deleted
  or explicitly kept by the user)
- The task-holding sections still read coherently without the pruned tasks

---

## Step 7.5 — Plan-layer citation scan (report-only)

Report-only — never gates, never edits, never blocks; distinct from the Step 0 gate, which
does. This scan never touches the roadmap, specs, or `## Features`, and its outcome never
affects whether the prune proceeds.

1. Anchor at the target repo root — the same anchor Step 5 derives (the parent of the
   `.ai-factory/` directory the target ROADMAP.md lives in).
2. Scope: the repo tree under that root, excluding `.ai-factory/` and `.git/`.
3. Grep (read-only) for citation shapes: `Phase [0-9]`, `note [0-9]{2}`,
   `\.ai-factory/(specs|notes)`, `ROADMAP`, `Plan [0-9]`. The invocation below is
   guidance, not contract — the pattern set is the contract; flags may be adjusted per
   platform as long as the scan stays read-only, repo-root-anchored, with the two excludes:
   ```bash
   grep -rInE "Phase [0-9]|note [0-9]{2}|\.ai-factory/(specs|notes)|ROADMAP|Plan [0-9]" \
     <target repo root> --exclude-dir=.ai-factory --exclude-dir=.git
   ```
4. Capture each hit as `<file>:<line> — <matched text>` for the Step 8 echo below. False
   positives are acceptable — this is a heads-up at the number-reuse moment, not a proof.

*Legacy-removable:* once every consuming repo reads clean of plan-layer citations, this scan
can be deleted — or kept as a cheap standing regression net; the decision is deliberately
deferred.

---

## Step 8 — Summary report

List the dirs swept in Step 5 — the flat three dirs (plus flat `test-runs/` in tests
mode) for a default-pair prune, or the pruned stem's `plans/<stem>/`,
`plan-reviews/<stem>/`, `reviews/<stem>/` (plus `test-runs/<stem>/` in tests mode) for
a named prune — and the spec files deleted in Step 5.

Report-only, never gates: echo the paragraph(s) captured by Step 0.6 under a "possible
unharvested margins" heading, one entry per source file. Do not re-scan
`plan-reviews/`/`reviews/` here — Step 5 already deleted the swept files; this step
only reports what Step 0 captured before the sweep. Free-form prose has no entry line
to pin; this never affects the Step 0 gate. If Step 0 captured nothing, omit the
heading.

Report-only, never gates: echo the hits captured by Step 7.5 under a "possible plan-layer
citations" heading, one `<file>:<line> — <matched text>` line per hit. This echo never
gates and never affects the Step 0 gate. If Step 7.5 captured nothing, omit the heading.

---

## Commit (on request only, never automatic)

The run ends with all changes in the working tree — no commit is made. When the user says
to commit (any wording): `git add -A` scoped to the target repo root, then one commit with
the message exactly `Roadmap prune` — no body, no prefixes, no co-author line, no per-file
commits, never ask about the message.

---

## What NOT to do

- Do not write internal-only task hashes anywhere — they belong to no feature row and to no ledger entry.
- Do not store the prune/deletion commit in drop-history — store its parent (the snapshot), so `git show <hash>:ROADMAP.md` yields the pre-prune roadmap.
- Do not prune `[ ]` tasks — only `[x]` tasks are candidates
- Do not invent commit hashes — find real ones from `git log`
- Do not merge unrelated features into one row to save space
- Do not update the first hash when a feature only had minor internal changes
- Do not scan or sweep a spec directory — spec deletion goes only through the **pruned**
  `[x]` lines' `Spec:` tags; never touch a path an open `[ ]` line's tag names or a
  user-kept `[x]` line's tag names
- Do not touch `handoffs/` — it is never swept
- Do not use `git rm` — deletion is unstaged (`rm`/`find -delete`), never `git rm`; staging happens once, at commit time, via `git add -A`
- Do not resolve artifacts per task — no slug derivation, no discovery, no orphan report, no extended verify
- Do not add rationale or explanation prose to the skill body — instructions only
- Do not commit automatically — on request only; exactly one commit, exactly `Roadmap prune`
