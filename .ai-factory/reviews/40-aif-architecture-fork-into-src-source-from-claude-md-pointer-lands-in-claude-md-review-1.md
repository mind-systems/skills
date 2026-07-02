# Review 1: aif-architecture fork into `src/`

## Scope
Reviewed `git diff HEAD` / `git status`. Code changes under review:
- `src/skills/aif-architecture/SKILL.md` (new, 236 lines)
- `src/skills/aif-architecture/references/architecture.md` (new, copied verbatim)
- `active/skills/aif-architecture` (symlink repointed)
- `CLAUDE.md` (repo bookkeeping)

(Plan/plan-review/`.json` artifacts are process files, not code — not reviewed for behavior.)

## Verification performed

**Task 1 — copy + symlink.** `active/skills/aif-architecture` now resolves to `../../src/skills/aif-architecture` (was `../../upstream/...`). `references/architecture.md` is **byte-identical** to the upstream copy (`diff -q` clean) — the "keep `references/` as-is" contract is honored. `SKILL.md` differs from upstream as intended. Upstream mirror untouched.

**Task 2 — Step 0.** DESCRIPTION.md read replaced with project `CLAUDE.md` read + light codebase scan (package-manager files, `src/` layout). Config read keeps `paths.architecture` + language; the `DESCRIPTION.md:` default line is dropped; ARCHITECTURE.md + language defaults retained. Manual-input fallback rewritten to no longer route the user to `/aif` for a DESCRIPTION.md. The entire `skill-context` / aif-evolve block is deleted.

**Task 3 — Steps 1/1.5/2 preserved + `## Features`.** Step 1 recommendation flow (arg mapping incl. legacy aliases, decision matrix, AskUserQuestion, CRITICAL `references/architecture.md` read), Step 1.5 Codebase Alignment Check, and the Step 2 template with **both** policy branches are intact. Template gains the reserved empty `## Features` section with the roadmap-prune/temporal-tree anchor comment. `## Decision Rationale` project-type source changed to `[from CLAUDE.md / codebase]`.

**Task 4 — Step 3/4, frontmatter, ownership.** Step 3 now writes an add-if-absent `## Architecture` pointer into the project CLAUDE.md, using the resolved path (not the literal), and explicitly skips when CLAUDE.md is absent. Step 4 (AGENTS.md) deleted; Confirm renumbered Step 5→Step 4 with content preserved. Artifact Ownership companion-update line now names only the CLAUDE.md pointer. Frontmatter `description` no longer references DESCRIPTION.md; unused `Questions` removed from `allowed-tools`; `Bash(mkdir *)` correctly retained (Step 2 still creates the parent dir). No stale `DESCRIPTION|AGENTS|skill-context|aif-evolve|Step 5|Questions|Localized heading` refs remain (grep clean).

**Task 5 — repo CLAUDE.md.** Active-set line: "two upstream originals" → "one … `aif-skill-generator`", with `aif-architecture` moved into the "our skills" enumeration. Reconcile list + `diff -rq` example block gain the `aif-architecture` entries. The "Everything else … is ours" list is untouched (correct — reworked-from-upstream belongs on the reconcile list).

## Correctness notes
- Step numbering is sequential (0, 1, 1.5, 2, 3, 4) with no dangling references.
- Body is 236 lines — well under the ≤500 limit.
- Ordering dependency (aif creates CLAUDE.md before invoking aif-architecture, per task 89) means Step 3's target exists during a normal `/aif` run; standalone use is guarded by the "skip if CLAUDE.md doesn't exist" branch. No runtime gap.
- No security-relevant content; no executable scripts added.

All plan tasks and spec-note (`51-aif-architecture-fork.md`) requirements are satisfied. No bugs, security issues, or correctness problems found.

REVIEW_PASS
