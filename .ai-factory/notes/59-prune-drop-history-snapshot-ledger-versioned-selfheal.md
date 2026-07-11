# roadmap-prune: drop-history is a prune-snapshot ledger — versioned Features header + legacy self-heal

**Date:** 2026-07-11
**Source:** conversation context (live prune on `tradeoxy_core` — drop-history ended up polluted with internal-task hashes; user clarified the intended semantics and the migration strategy)

## Key Findings

- **Drop-history is a prune ledger, not a bin for every dropped hash.** Its one job: hold the **snapshot hash of each prune** — the commit *before which* that prune deleted roadmap lines (the last commit where the pruned tasks still existed). Walking those snapshots reconstructs a flat roadmap across the whole project history (`git show <snapshot>:.ai-factory/ROADMAP.md`, one per prune). That reconstruction is the sole reason the row exists.
- **The row's semantics, stated once in the skill (user's wording):** each hash is **the last known intact roadmap** — the roadmap as it last stood whole before a prune cut it. Not a record of prune events; the "off-by-one" against the prune commit is by construction correct: the skill never commits (commit is on-request, later), so at write time the prune commit's hash does not exist — the snapshot (current HEAD) is the only hash there is, and it is the one `git show` needs directly.
- **The bug:** Step 2.1's rule *"Internal only → hash goes to drop history only"* pollutes the ledger. Internal-only tasks (refactors, proto-locks, cleanups, tests that earn no feature row) get their own hash dumped into drop-history, mixed in with the real prune snapshots. In the live `tradeoxy_core` run the row became **2 prune-related hashes + 9 internal-task hashes** — unreadable as a prune history, and the user reasonably miscounted "11 prunes." Ground-truth check of that row found the mix is actually three-way: `0bee791` is a correct snapshot (parent of prune `0be0279`), but `20d2a0e` is a **prune commit itself**, not its parent — confirming the self-heal must rebuild the row wholesale from git, never repair existing hashes in place. Internal-only tasks need **no** hash: they already sit inside the nearest prune snapshot's roadmap and are recoverable there; a per-task hash is redundant and actively misleading.
- **Correct rule:** the only thing that ever enters drop-history is the Step-4.1 prune snapshot — exactly **one hash per prune run**. Internal-only classification affects the Features table (no named row); it writes a hash nowhere.
- **Legacy pollution is already in the wild** (`tradeoxy_core`, and likely every repo pruned by the old skill). The user will not hand-fix each repo. So the skill must **self-heal on invocation**: detect the old format and rebuild the ledger from git ground truth, gated by a version marker so it runs once per repo and can eventually be retired.
- **The version marker doubles as the "already migrated" flag.** Stamp the skill version that last built the Features table directly in the header — `## Features (roadmap-prune v2)`. Absent/older marker → run self-heal, then stamp current. Current marker → skip. Once every consuming repo carries the current marker, the self-heal block is dead code and can be deleted.

## Details

### Edit 1 — drop-history takes only prune snapshots

Delete the *"Internal only → hash goes to drop history"* routing (Step 2.1 / Step 4.2). Internal-only tasks get **no** hash recorded anywhere — they are captured by the nearest prune snapshot. The drop-history row is extended with exactly one hash per prune: the **snapshot** = the last commit where the pruned tasks still lived in ROADMAP.md (the Step-4.1 HEAD; equivalently `<prune-commit>^` after the fact) — **not** the prune/deletion commit itself. Storing the snapshot is what makes `git show <hash>:.ai-factory/ROADMAP.md` reconstruct the pre-prune state directly. One prune = one hash, appended chronologically.

### Edit 2 — versioned Features header

The skill declares its own **Features-table format version** — **one line in the skill body, above the steps** (not frontmatter: a custom frontmatter field is inert metadata far from the executing steps). Both use sites reference that single line: the self-heal pre-pass check and the Step-4.2 header write. Step 4.2 writes the header as:

```
## Features (roadmap-prune v2)
```

Every run (re)stamps the current version — the header always names the version that last maintained the table. Suggested numbering: this fix is **v2**; treat any unmarked/legacy `## Features` header as v1. Bump the number only when the table's format/semantics change again; repos on an older number then self-heal forward.

### Edit 3 — legacy self-heal (pre-pass, every invocation) — "handle the legacy bug when invoked"

Before Step 4.2 writes features, read the `## Features (...)` header marker:

- **Marker == current version** → nothing to migrate; proceed normally.
- **Marker absent or < current** → rebuild the drop-history row from git ground truth, then stamp the current version:
  1. Enumerate the repo's real prune commits on the **current branch only** (never `--all` — a prune on an abandoned branch would inject a foreign timeline's snapshot into this branch's ledger): `git log --format='%h %s' -- .ai-factory/ROADMAP.md` filtered to the prune-message set — `Roadmap prune`, `Remove complete plans`, `Rmove complete plans` (the historic manual wording). The first entry is the exact message the skill's own "Commit (on request only)" section already mandates (landed with milestone 56) — every post-56 prune is message-matched by construction; this task relies on that section and must not alter it. **Verify each candidate by content:** its diff must actually delete `[x]` lines from `.ai-factory/ROADMAP.md` — early history used a two-commit pattern whose same-named twin swept only `plans/`/`reviews/` artifacts and touched no roadmap line; a twin is skipped and reported, never ledgered.
  2. For each, the ledger entry = its **parent** (`<prune>^`) — the snapshot.
  3. **Replace** the drop-history hashes with exactly this reconstructed, de-duplicated, chronological set. The old polluting internal-task hashes are discarded — they hold no navigational value the snapshots don't already carry (user ruling: orphan hashes are unwanted).
  4. **Zero prune commits found** (e.g. a fresh repo whose empty `## Features` section was just generated by `aif-architecture`) → nothing to rebuild; stamp only.
  5. Stamp the header `## Features (roadmap-prune v2)`.

Deterministic and idempotent: re-running yields the same ledger. This is the self-contained migration the skill performs for any repo it touches, so no project needs a manual fix.

**Guard:** the rebuild is authoritative from git — do not try to preserve unclassifiable existing hashes. Self-heal edits **only** the drop-history row and the header marker — never feature rows, never ROADMAP.md, never specs.

### Validation — detection dry-run on the other two legacy repos (2026-07-11)

Detection was exercised against `mind_mobile` and `mind_api` ground truth:

- **Content-verify is required — message-matched non-prunes exist.** Early history used a two-commit pattern: one "Remove complete plans" deletes roadmap lines, a sibling "Remove complete plans" sweeps only `plans/`/`reviews/` artifacts and touches no roadmap line (`mind_mobile` `e7e7d84`, `mind_api` `607995b`). The artifact-sweep twins must be skipped — their snapshots add nothing.
- **Known, accepted loss — hand-edits are not ledgered.** `mind_mobile` `f74ffa4` ("Fix suggestions endpoint path", 03-20) deleted three `[x]` tasks by hand inside an unrelated fix commit; message-only discovery misses it, so those three March-era tasks are absent from the flat reconstruction. User ruling: acceptable — the ledger records the ritual prunes (top-of-file, big batch, uniformly named); a broader discovery signal (net-`[x]`-deletion scan over all commits) was considered and **rejected as over-resolution**.
- **Scope pin:** the content verify counts `[x]` deletions in `.ai-factory/ROADMAP.md` only (the ledger reconstructs the main roadmap; both repos' roadmaps lived at that path their whole history — no path migration to handle).
- **Expected self-heal outcomes:** `mind_api` row `a5959dc, 0656ef1` — both already correct snapshots (`70b965d^`, `575c317^`), zero pollution; heal extends 2 → 5 (three March prunes missing). `mind_mobile` row of 6 = 3 correct snapshots (`d73bd27`, `ece2859`, `1cb7df7`) + 3 internal-task hashes to discard; heal yields 6 entries (the three March prunes join). Together with `tradeoxy_core` these are three ready integration cases: pure-extension, mixed-pollution, and (tradeoxy) prune-commit-instead-of-parent.

### Edit 4 — retirement path

Mark the Edit-3 self-heal block **legacy-removable**: once every consuming repo's Features header shows the current version, the block is dead and can be deleted (the version constant and the per-run stamping stay). Track as a follow-up.

### Edit 5 — header-string coupling with temporal-tree

The versioned header changes the exact `## Features` string that `temporal-tree` locates and `aif-architecture` generates. Per the cross-file-invariant rule (repo CLAUDE.md), one sentence at each coupling point: in `roadmap-prune`, next to the header write — `temporal-tree` matches this header by prefix; in `src/skills/temporal-tree/SKILL.md`, at its locate step — the header may carry a version suffix (`## Features (roadmap-prune vN)`), match by prefix. `aif-architecture`'s template stays unmarked — an unmarked header *is* v1; the first prune's self-heal stamps it (the zero-prune edge above).

### Documented assumption — rewritten history is out of scope

A force-push / shared-history rewrite invalidates every hash in the Features table — feature rows and the ledger alike; defending against it is impossible by construction and out of the skill's scope (repo policy: shared history is not rewritten). One sentence in the skill documents the assumption. Recovery, should it ever happen, already exists: delete the version marker from the `## Features` header and re-run the prune — self-heal rebuilds the ledger from the rewritten history. No mechanism beyond that sentence.

## What NOT to do

- Do not write internal-only task hashes anywhere — they belong to no feature row and to no ledger entry.
- Do not store the prune/deletion commit in drop-history — store its parent (the snapshot), so `git show <hash>:ROADMAP.md` yields the pre-prune roadmap.
- Do not run the self-heal when the header already shows the current version — one-shot per repo.
- Do not let self-heal touch feature rows, ROADMAP.md, or specs — drop-history row + header marker only.
- Do not enumerate prune commits with `--all` — current branch only; the ledger reconstructs this branch's roadmap timeline.
- Do not try to repair existing drop-history hashes in place — the rebuild is wholesale from git (the legacy row mixes snapshots, prune commits themselves, and internal hashes).
