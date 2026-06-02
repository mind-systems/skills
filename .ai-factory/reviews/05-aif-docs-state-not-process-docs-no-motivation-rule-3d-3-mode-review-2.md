# Code Review (pass 2): aif-docs state-not-process docs (no-motivation rule + `3d`/`3д` mode)

**Reviewed:** `git diff HEAD` on branch `master`
**Files changed:** `.claude/skills/aif-docs/SKILL.md`, `.claude/skills/aif-docs/references/REVIEW-CHECKLISTS.md`, `CLAUDE.md` (plus plan/sidecar/review artifacts under `.ai-factory/`)
**Risk Level:** 🟢 Low

## Summary

Text-only change to one skill plus a one-line `CLAUDE.md` registration. No executable code, migrations, types, schemas, or security surface — the only "runtime" is how a model reads the instructions, so this pass checks internal consistency, contradictory directives, and faithfulness to the plan.

All nine plan tasks are implemented faithfully, and the three non-blocking nits from review-1 have been resolved:

- **`argument-hint`** now reads `"[--web] [3d|3д]"` — the Cyrillic variant is surfaced (was the NIT-1 gap).
- **Phrase lists are now aligned** — the REVIEW-CHECKLISTS.md no-motivation item lists the full set (`we changed / was added / was replaced / this replaces / previously / because we / this milestone / was introduced / has been`), matching the Step 4 pass in SKILL.md (was the NIT-2 drift).
- **The 3D Step 1 ROADMAP reference is softened** to "from the stated user intent, spec note, or ROADMAP milestone if one is provided or discoverable in the project" — no longer a dangling instruction to consult a file the skill never resolves (was NIT-3).

Markdown structure is intact: Core Principle 7 sits cleanly in the numbered list; the 3D explanation block and `---` separator are well-formed; the `MODE = normal` branch correctly precedes the State A/B/C fenced block; the Step 4 no-motivation pass and 3D carve-out are coherent. `CLAUDE.md` has exactly one `aif-docs` entry, placed in the "Intentionally diverged" list above the "All other skills — safe to overwrite" line, so a future sync will not treat it as overwrite-safe.

## Findings

No blocking findings. No new nits introduced; the prior pass's nits are resolved.

## Pre-existing observations (not introduced by this change, no action required)

- **Checklist name mismatch.** Step 4 prose calls the two checklists "Technical Accuracy" and "Readability & Completeness", while the reference-file headers are `## Technical Checklist` and `## Readability Checklist — "New User Eyes"`. The new 3D carve-out targets the actual checklist *item text*, so it lands correctly regardless. This naming gap predates the change.
- **Internal-link checks correctly preserved in 3D.** The Step 4 carve-out skips only code-example, install-instruction, and broken-reference-against-the-codebase checks; the "All internal links work" item is not annotated as skipped, so doc-to-doc links are still verified in 3D. Correct distinction, handled deliberately.

## Verification performed

- Read the changed regions of SKILL.md in full; confirmed no malformed markdown, no orphaned fences, correct branch ordering into the State block.
- Confirmed the two no-motivation phrase lists (SKILL.md Step 4 and REVIEW-CHECKLISTS.md) now match.
- Confirmed `argument-hint` advertises both tokens and `CLAUDE.md` has a single, correctly-placed divergence entry.
- Confirmed Change A (Principle 7 + no-motivation pass) is unconditional across modes and the 3D carve-outs explicitly retain the no-history rule — matching the spec's "drops current-state and verify, keeps no-history" constraint.
- No secrets, no shell/exec changes, no `allowed-tools` or dependency changes.

REVIEW_PASS
