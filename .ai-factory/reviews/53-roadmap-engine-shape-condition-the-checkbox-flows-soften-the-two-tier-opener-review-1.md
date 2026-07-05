# Review 1 — roadmap-engine: shape-condition the checkbox flows; soften the two-tier opener

**Scope:** `src/skills/roadmap-engine/SKILL.md` (only code file changed; other staged files are prior-milestone artifacts and this milestone's plan/spec/plan-review, not in scope).

## What was verified

The diff contains exactly the three intended hunks — no collateral edits.

1. **Opener (`:27-32`)** — the categorical "Each milestone is a two-tier entry" is gone; replaced with "A task-tier entry with a contract line is a two-tier entry …" plus the shape carve-out ("A caller's hook (a) may define entries with no contract line (e.g. a phase header) — the note and tag machinery here applies only where a contract line exists."). The `<NN>`/`<slug>` note-path detail and the exact `` Spec: `.ai-factory/specs/<NN>-<slug>.md`. `` tag text are preserved. Matches spec §The change/3.

2. **Review progress (`:203-208`)** — marking is scoped to "each unchecked **checkbox entry**"; phase-shaped entries "are never marked," and derived phase progress "may be **reported** as complete, report-only." Scan/propose/apply-on-confirmation/leave-the-rest mechanics intact. Matches spec §The change/1.

3. **Check mode (`:232-234`)** — one sentence added at the top: operates on "**checkbox entries only**"; a checkbox-less caller "registers no check mode (its argument routing should not advertise one)." Scan/evidence/scoring/report mechanics for checkbox callers unchanged. Matches spec §The change/2.

## Guards — all pass

- `grep -n "Each milestone is a two-tier entry"` → no match (categorical claim removed).
- `grep -n "roadmap-outline\|roadmap-decompose\|skeleton"` → zero matches (engine stays caller-agnostic).
- Draft (`:156-162`), finalize (`:176-182`), and update-mode Add (`:209-213`) wording, the "Roadmap File Format" section, the numbering rules, and the contract-line rules are byte-identical to HEAD (diff touches none of them).
- File is 283 lines (≤500).
- Mode-determination routing at `:118` is untouched, as the spec required.

## Correctness note (not a finding)

The new Check-mode sentence states a checkbox-less caller "registers no check mode," while Mode determination at `:118` still routes a literal `check` argument to Check mode for any caller. This is intentional and consistent with the spec: the routing at `:116` was explicitly guarded ("do not touch"), and the remedy is caller-side (the checkbox-less caller drops `check` from its `argument-hint`). The engine merely states the constraint and stays caller-agnostic; the residual — a user typing `check` at a checkbox-less caller still landing in Check mode — is acknowledged in the spec's problem statement and deliberately left to the caller. The scan body still reads "For every open `- [ ]` entry," which is already checkbox-scoped and does not contradict the new sentence.

This is a prose-only change to a skill instruction file — no runtime surface, no migrations, no types, no concurrency. Nothing to break at execution time.

REVIEW_PASS
