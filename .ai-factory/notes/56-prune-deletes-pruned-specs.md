# roadmap-prune: sweep the artifact dirs with plain rm, delete completed tasks' specs by tag

**Date:** 2026-07-03
**Source:** conversation context (notes-are-specs review; second respec — plain rm, no git rm)

## Key Findings

- After a prune, completed work's leftovers at HEAD are dead weight: the four artifact dirs and the specs of `[x]` tasks. Everything stays reachable through history (the completion commits and the Step 4.1 snapshot).
- The mechanism is the user's own manual workflow, encoded: **plain `rm`, then `git add -A` at commit time**. No `git rm` anywhere — its staging split, its two abort modes, and the tracked-file reasoning all disappear with it.
- The skill carries **instructions only, no rationale**. No explanations of counters, git semantics, or safety reasoning — the previous attempt failed review rounds over exactly such prose being imprecise.

## Details

### Edit 1 — the sweep

In the prune execution, after the Step 4.1 snapshot and the ARCHITECTURE.md update, before deleting lines from ROADMAP.md:

1. **Capture first:** collect the `Spec:` tag path of every `[x]` line (pruned and kept). A `[x]` line with no `Spec:` tag contributes nothing — skip it, never synthesize a path.
2. `rm -rf` the four artifact dirs: `plans/`, `plan-reviews/`, `reviews/`, `patches/`. Missing dirs are a non-event (`-f`).
3. `rm -f` each captured spec path.

Anchor every deletion on the **target repo root** — the parent of the `.ai-factory/` the skill reads ROADMAP.md from, derived from the argument. The four dirs sit directly under that `.ai-factory/` (`plans/`, `plan-reviews/`, `reviews/`, `patches/`). The captured `Spec:` tag paths are repo-root-relative — they already begin with `.ai-factory/` — so use them **verbatim** against the target repo root; never re-prefix them with `.ai-factory/` (that would double the segment). Never a fixed top-level path: a sub-repo roadmap at `<subrepo>/.ai-factory/ROADMAP.md` sweeps only `<subrepo>/.ai-factory/*`.

### Edit 2 — replace the old rules

The What-NOT-to-do line "Do not delete the notes/ directory or individual note files…" is replaced by: spec deletion goes only through `[x]` lines' `Spec:` tags — never scan or sweep a spec directory, never touch a path an open `[ ]` line's tag names. `handoffs/` is never touched.

### Edit 3 — the prune commit (on request, never automatic)

The run ends with all changes in the working tree — **no commit**; the user reviews first. When the user says to commit (any wording): `git add -A` scoped to the target repo, then **one commit** with the message exactly:

```
Roadmap prune
```

No body, no prefixes, no co-author line, no per-file commits, never ask about the message. The Step 4.1 snapshot hash is captured **before any changes**.

### Constraints

- The sweep is plain `rm` — it removes uncommitted files in those dirs too. Prune is run deliberately on a settled tree; that is accepted, no guards, no tracked-file filtering.
- The skill states what to do, not why. No counter-reset claims, no git-semantics explanations, no safety rationale in the skill body.
- The summary report lists the swept dirs and deleted spec files — information only; the skill's pre-existing Verify checks stay as they are, nothing added to them.
- `ROADMAP_TESTS.md` parity: same sweep; `test-runs/` joins the swept dirs in that mode only.

## What NOT to do

- Do not use `git rm` — deletion is plain `rm`; staging happens once, at commit time, via `git add -A`.
- Do not scan or sweep any spec directory — specs are deleted only via `[x]` lines' tags; no tag → skip.
- Do not add rationale/explanation prose to the skill — instructions only.
- Do not resolve artifacts per task — no slug derivation, no discovery, no orphan report, no extended verify.
- Do not commit automatically — on request only; exactly one commit, exactly `Roadmap prune`.
