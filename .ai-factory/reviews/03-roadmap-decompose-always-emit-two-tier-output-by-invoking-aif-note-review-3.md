# Code Review 3: roadmap-decompose — always emit two-tier output by invoking aif-note

**Reviewed change:** `.claude/skills/roadmap-decompose/SKILL.md` (only functional change; `ROADMAP.md`, `notes/15-…`, `plan-reviews/*`, `plans/03-*`, `reviews/review-1`, `reviews/review-2` are process artifacts).

**Verdict:** All findings from reviews 1 and 2 are resolved. The skill is internally consistent and the runtime behavior it specifies is sound. No outstanding correctness, security, or robustness issues.

---

## Prior findings — all resolved

- **Review-1 #1 (Mode 1 eager note-writing, Medium)** — resolved. Step 1.3 drafts the roadmap **in memory** with `` Spec: `<note pending>`. `` placeholders and explicitly defers `aif-note` to the Step 1.4 finalization, which runs only for the confirmed set ("Milestones removed or rewritten during options 2–4 receive no note invocation"). No orphaned notes, no burned `<NN>`.
- **Review-1 #2 / Review-2 #1 (Step 1.3 "draft" could be misread as a disk write, Low)** — resolved. Line 90 now reads *"Draft the roadmap **in memory (do not write `$TARGET_FILE` yet)**"*; the only write is the 1.4 finalization (line 136). Placeholders can no longer leak to disk.
- **Review-1 #2 / Mode 2.5 update path (Medium)** — resolved. Lines 208–210 split the rule explicitly: existing `Spec:` tag → instruct `aif-note` to update the named note in place; no tag → create new and add the tag. Consistent with `aif-note`'s Important Rule 5; no duplicate-note risk.
- **Review-1 #3 (malformed `Spec:` tag example)** — resolved. Line 292 renders the canonical `` Spec: `.ai-factory/notes/<NN>-<slug>.md`. `` form.
- **Review-1 #4 (wording drops)** — resolved (lines 290, 296).

## Verified correct

- `Skill` present in `allowed-tools` (line 10); `aif-note` is model-invocable (`disable-model-invocation: false`); `roadmap-decompose`'s own `disable-model-invocation: true` correctly left unchanged (it is the user-invoked entry point).
- `description` (lines 3–8) reflects the contract-line + spec-note shape, preserves all trigger keywords, and is well under 1024 chars.
- Mode 1: draft-in-memory → confirm → sequential `aif-note` finalization → single file write. The `<note pending>` placeholder is replaced with the real captured path before the only disk write — no collisions, no leaked placeholders.
- Mode 2.4 writes notes for user-described (non-speculative) tasks — eager write is appropriate there; no confirmation-gate concern.
- Two-Tier Output block (lines 284–298) is coherent and DRY; Mode 1's Step 1.4 correctly invokes only "steps 3–5" since draft + gate already ran in 1.3/1.3.1; Mode 2 invokes the full procedure.
- Sequential-invocation rule (line 296) plus the placeholder/finalization design make `<NN>` collisions structurally impossible.
- Atomicity Gate logic preserved and consistently re-scoped to run on the full spec before note/contract-line emission in both modes.
- Format section + Critical Rule 6 consistently encode the two-tier model; per-task scoping (task name as `$1`, delimited spec text) present (line 290).
- Mode 3 (`check`) logic unchanged — still only flips `[ ]`→`[x]`.

## Non-blocking observations (not findings)

- The Mode 2.5 update path's fidelity ultimately rests on `aif-note` honoring an explicit "update note `<path>`" instruction at runtime; this is the correct delegation given the "do not alter aif-note" constraint and is not a defect in this change.
- The Mode 3 status emoji (✅/🔨/⏳) were dropped as incidental cosmetic drift; harmless and not a correctness issue.

No actionable findings.

REVIEW_PASS
