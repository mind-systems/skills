# roadmap-prune: deferred-observations gate — no prune while unpinned entries exist

**Date:** 2026-07-04
**Source:** conversation context (deferred-observations channel design; orchestrator spec `.ai-factory/specs/03-deferred-observations-section.md` defines the source format)

## Key Findings

- Reviewers write a `## Deferred observations` section (entry: `- Affects: <phase / spec-note path / "unknown"> — <observation>`) into both `plan-reviews/` and `reviews/` files; prune's sweep `rm -rf`s exactly those dirs. Resolving what stands behind an observation — tracing its connections, routing it, verdicting it — is **not prune's job**: that is `milestone-rescue-audit`'s work (its prune mode, spec `04-audit-reads-deferred-observations.md`). Prune's job is to **refuse to destroy unprocessed observations**.
- Therefore prune gains a **gate at the very top of the skill**, before any other step runs: scan both review dirs for deferred-observation entries carrying no status marker; if any exist, the run **aborts with feedback** — the file, line, and text of every unpinned entry, and the instruction that they must be processed (by `milestone-rescue-audit prune`) before the roadmap can be cleaned. No partial prune, no changes of any kind on a failed gate. The user routes from there.
- Prune itself never promotes, evaluates, or marks entries. Its only relationship to the protocol is the gate: read-only scan, refuse on unpinned. The section format, the marker grammar, and the **pinned** definition (entry line carries ≥1 marker) live in the `orchestrator-artifacts` engine (spec `05-orchestrator-artifacts-engine.md`) — this task adds `loads: orchestrator-artifacts` to prune's frontmatter and references the engine, never redefines the grammar. Depends on the engine task landing first.

## Details

### Edit 1 — the gate, first step of the skill

In `src/skills/roadmap-prune/SKILL.md`: add `loads: orchestrator-artifacts` to frontmatter (ensure loaded once per chat), then add the gate **above Step 1** (the "Before you start" tier):

1. Scan every `.md` file in `<target repo root>/.ai-factory/plan-reviews/` and `.ai-factory/reviews/` for `## Deferred observations` sections (absent section → nothing to check in that file).
2. Collect every entry that is not pinned per the engine's grammar (no status marker).
3. If any exist → **stop the skill entirely**: print each as `<file>:<line> — <entry text>`, state that pruning is blocked until every entry is pinned, and name the resolution — run `milestone-rescue-audit` in prune mode. Make no edits, no sweep, no ARCHITECTURE/ROADMAP changes.
4. If none → proceed with the normal prune flow, unchanged.

### Edit 2 — the summary report

The existing summary-report step additionally quotes, for files that have **no** `## Deferred observations` section but contain pre-standardization marker phrases ("latent", "forward risk", "no action needed", "out of scope for this milestone", "flagging so Phase", "Surface this to the orchestrator"), the matching paragraphs under "possible unharvested margins" — **report-only**: free-form prose has no entry line to pin and never gates.

### Constraints

- The sweep, spec deletion, commit policy, and existing report content are untouched; the gate adds a read-only scan and an abort path only.
- Instructions only in the skill body, no rationale prose (house rule from the sweep task).
- `ROADMAP_TESTS.md` parity: the gate covers the shared `plan-reviews/`/`reviews/` dirs identically; `test-runs/` files carry no review sections and are not scanned.

## What NOT to do

- Do not process, promote, evaluate, or mark entries in prune — the gate reads and refuses, nothing more; pinning is `milestone-rescue-audit`'s work.
- Do not proceed partially on a failed gate — no "prune the rest and skip these files".
- Do not gate on pre-standardization free-form margins — only structured `## Deferred observations` entries pin; prose is report-only.
- Do not rewrite or delete entry text, `Affects:` values, or existing markers anywhere.
