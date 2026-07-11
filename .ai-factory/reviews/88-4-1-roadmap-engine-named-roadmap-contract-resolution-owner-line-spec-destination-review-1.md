# Code Review — 4.1 roadmap-engine named-roadmap contract

**Change reviewed:** `src/skills/roadmap-engine/SKILL.md` (the only source edit; the other staged files are plan/plan-review/sidecar artifacts). +34/−3, one new `## Named roadmaps` section plus two in-place clause edits in `## The two-tier artifact`.
**Nature:** instructional prose consumed by the calling agent — no executable code, no security surface. "Correctness" here = fidelity to spec 43 / `docs/multiuser-roadmaps.md` and the byte-stability guard, and absence of ambiguity that would drive wrong agent behavior.
**Risk:** 🟢 Low — no findings.

## Verification against ground truth

**Spec 43 five-item Change list — all present and faithful:**
1. Resolution order (SKILL.md:51–54) — explicit arg → "my roadmap" (`.ai-factory/roadmaps/<slug>.md`, only when asked/named, engine never infers) → default `.ai-factory/ROADMAP.md`. ✓
2. Slug derivation (:56–58) — local-part of `git config user.email`, lowercased, non-alphanumeric runs → single hyphen, worked example `kg.wmservice@gmail.com` → `kg-wmservice`, fallback slugified `user.name`. Worked example is arithmetically correct. ✓
3. Owner line (:60–63) — `> Owner: <full email>` first line, written at creation, verified against current git identity, mismatch → hard stop naming owner + two exits, no silent fallback. ✓
4. Test sibling (:65–67) — `.ai-factory/roadmaps/<slug>-tests.md`, derived from the roadmap in play never from identity, same owner line, same single-writer. ✓
5. Spec destination (:69–75) — `.ai-factory/specs/<slug>/` via `note`'s existing hook, per-directory numbering, default keeps flat `.ai-factory/specs/`, plus the `Spec:` tag carries `<slug>/` reflecting `note`'s returned path. ✓

**Byte-stability guard — honored.** Diffed the pre-edit two-tier section against `HEAD`: the only content changes are the two destination clauses gaining the named variant. All other text in the section (the hook-(a) sentence, the exact-tag sentence at :34, "why two tiers", "never write a full spec inline") is word-for-word identical; only line-wrapping shifted. The maintenance-flow steps below are untouched.

**Default case byte-stable behaviorally.** This repo has no `.ai-factory/roadmaps/` dir (confirmed live), so the default path is the running state. With no argument and no "my roadmap" request, resolution yields `.ai-factory/ROADMAP.md`; the two-tier destination resolves to `.ai-factory/specs/` and `<NN>` scans against `.ai-factory/specs/` — identical to pre-edit behavior. Zero regression.

**`note` untouched.** `git diff --stat` under `src/` shows only `roadmap-engine/SKILL.md` changed. The `<slug>/` destination is a plain hook value; `note`'s per-directory numbering already covers it. ✓

**Caller-agnostic.** The new section names no roadmap-family caller (outline/decompose/skeleton/rescue/pin-gaps/test-coverage). Its only skill reference is `note`, which the engine already loads (`loads: note`, frontmatter unchanged). No orchestrator-path wording added. ✓

## Notes (no action required)

- **Disclosed two-clause edit.** Spec 43's guard literally names only "the `<NN>`-scan sentence," but the implementation also varied the `note`-destination clause (:37–40). This is correct and necessary: leaving that clause unconditional (`pass destination .ai-factory/specs/`) would route a named roadmap's specs to the flat dir, contradicting item 5. The deviation was raised and accepted across plan-reviews 2 and 3; the implementation matches exactly.
- **Tag template tension is the accepted design.** The general template at :34 still states the flat `` Spec: `.ai-factory/specs/<NN>-<slug>.md` `` as "the exact tag", with item 5 supplying the named `<slug>/` override. This general-plus-override shape is the byte-stability-preserving choice ratified in review; not a defect. An agent applies it correctly by reading the engine section it is in.

## Deferred observation (out of 4.1 scope)

The new `## Named roadmaps` section and maintenance-flow hook (c) "Target-file routing" (:105–106, :124–126) both describe target-file routing without a cross-link. They are compatible layers and the byte-stability guard forbids editing hook (c) here — a one-clause forward pointer is a Phase-4-coherence follow-up, not this milestone's work.

REVIEW_PASS
