# Code review — 17.1 Engines: one dictionary in note, roadmap-engine, test-philosophy, orchestrator-artifacts

## Summary

**Files reviewed:** `git diff HEAD` in full (12 files) + both changed `SKILL.md` files read in full around every changed region + the two no-edit certification targets + `orchestrator/orchestrator/roadmap.py` (cross-repo, for the `---STOP---` semantics) + all eleven callers of the two edited engines.
**Risk level:** 🟢 Low
**Findings:** none.

The product of this task is two files — `src/skills/roadmap-engine/SKILL.md` (19 insertions / 19 deletions) and `src/skills/orchestrator-artifacts/SKILL.md` (6 / 6). Both are naming-only prose edits with no executable surface. The remaining ten changed files are planning artifacts (ROADMAP, five specs, the plan, two plan-reviews, the sidecar).

## Verification — every gate in the plan's Task 6, run

| Gate | Expected | Actual |
|---|---|---|
| `rg -U -in 'spec\s+notes?'` over all four engines | zero | **zero** ✓ |
| `rg -U -in 'milestones?'` over all four | zero | **zero** ✓ |
| `rg -U -in 'roadmap\s+lines?'` (two engine files) | zero | **zero** ✓ |
| `rg -U -in 'the\s+note\b'` (roadmap-engine) | zero | **zero** ✓ |
| `rg -U -in '\bnotes?\b'` residue | 9 lines, 4 legal classes, no artifact noun | **exactly 5, 11, 36(×2), 37, 39, 70, 73, 190, 210** ✓ |
| old email/slug | zero | **zero** ✓ |
| new value read back | `john.doe@example.com`:57, `john-doe`:58, oa 28/29 | **all four present** ✓ |
| `<note pending>` | 2 | **2** ✓ |
| `` Spec: ` `` | 7 | **7** ✓ |
| `## Deferred observations` | 2 | **2** ✓ |
| `note` + `test-philosophy` diff | empty | **empty** ✓ |
| `Silent-Failure\|Loud-failure` | 3, all exonerated | **3** at 14 (H1), 25 (H2), 41 (sentence-initial attributive) ✓ |
| frontmatter: only `description:` changed | `name:`/`loads:`/`allowed-tools` untouched | **zero hits on those** ✓ |
| reverse-graph markers | byte-identical | **unchanged in both engines** ✓ |
| line count / numbering | identical pre/post | **315→315, 84→84; numstat 19/19 and 6/6** ✓ |
| spec-path templates | literals survive | **6 occurrences intact; only surrounding prose changed** ✓ |

The no-reflow constraint held exactly as predicted: line 43 measures 90, line 213 measures 89, `orchestrator-artifacts:68` measures 86 — the plan forecast 90/89/86. The 16–17 two-line reflow landed byte-length-preserving (87/83 before and after), so no downstream line number moved.

## Correctness checks beyond the plan's gates

- **Caller coupling.** All eleven callers of the two engines were grepped for verbatim quotes of the rewritten prose (`the note is the implementation`, `note holds the full implementation`, `make two milestones`, `not the roadmap line`, `milestone's artifacts`, `The note follows`). Zero hits — no caller can desync.
- **No runtime scanner depends on the changed words.** Nothing in the orchestrator or `skills/scripts/` greps for `spec note`/`milestone`. `orchestrator/roadmap.py` parses roadmap lines through `CHECKBOX_RE` only (`^- \[([ x])\] \*\*(.+?)\*\*…`) — it reads checkbox, title and description as opaque text, never the vocabulary inside.
- **Semantic reads, not just greps.** Every changed region was read in full. Two spots deserved the check and both are right: `orchestrator-artifacts:31` ("`<seq>` … not recoverable from a contract line") correctly names the roadmap's task line, not the roadmap file; and the finalize paragraph at 209–214 is now internally consistent ("write its task spec … need neither a task spec … only the confirmed set gets task specs"), which was the specific drift the plan's Assumption 2 existed to prevent.
- **Scope boundary held.** `spec note` still survives in exactly six files — `roadmap-decompose`, `roadmap-decompose-skeleton`, `roadmap-outline`, `aif-docs` (17.2's set) and `task-rescue`, `task-rescue-audit` (17.3's). No reach into `roadmap-prune`.
- **The 17.5 hold-out is intact.** `orchestrator-artifacts:55` still reads `spec-note path`, correctly frozen; the conformance grep's `\s+` does not match the hyphenated form, so the check and the deliberate hold-out do not fight.

## Two things I checked hard and cleared

Recording these because both looked like defects on first pass and neither is.

**1. Two `---STOP---` markers were removed from ROADMAP.md.** These are orchestrator control markers (`roadmap.py:58` — parsing halts at the first one), so removing them is a control-flow change, and it sits outside this task's stated four-file scope. Traced through:

- The marker after 17.4 was replaced by the new 17.5 contract line. The next marker sits after `13.1`, which is `[x]`. Net effect on the undone queue: `{17.1–17.4}` → `{17.1–17.5}` — exactly the intended addition of 17.5.
- The marker after 15.1 (HEAD:60) was redundant: HEAD carried another at :70 with **no tasks between them**. Batching is unchanged — the boundary after 15.1 is still enforced by the marker now at :67, before 2.1.

Only the *first* marker is ever operative in a given parse, so neither removal alters what runs. Cleared.

**2. The changeset bundles planning artifacts with the implementation.** ROADMAP.md and five specs changed alongside the two engine files. This is coherent rather than scope creep: the 17.1 contract line was corrected to match what actually landed (7 `spec note` sites not 6, plus the 8 bare-`note` sites and the two `roadmap line` sites the original line never mentioned), spec 62's stale Phase-16 carve-out was replaced with the correct post-16.1 expectation, and spec 72 was narrowed to `roadmap-prune` 231/276 — dropping the over-included line 155, which describes lines deleted from the roadmap *file* at a git snapshot boundary and would have been corrupted by the substitution. The contract line stays `[ ]`; nothing claims completion prematurely.

## Notes

- `test-philosophy` and `note` correctly landed **zero** edits. This is the right outcome, not an omission: all three `Silent-Failure`/`Loud-failure` sites sit in exonerating grammatical positions (two headings, one sentence-initial attributive) under the spec's own casing rule, and `note` carries no synonym tokens. The empty `git diff --stat` is the assertion that proves it rather than assuming it.
- The `description:` field edit (`roadmap-engine:5`) is in scope and correct — it is the always-loaded skill description field, the surface the reserved-words contract binds hardest. No doc or index copies that string, so there is no second home to keep in sync.

REVIEW_PASS
