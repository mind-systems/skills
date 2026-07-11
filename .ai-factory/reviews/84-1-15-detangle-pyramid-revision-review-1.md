# Code Review — 84-1-15 detangle: pyramid revision

**Scope:** `git diff HEAD` / `git status`. The only product-code change is `src/skills/detangle/SKILL.md` (the "Before you start — load project context" section, lines 28–33). The other staged files are planning/review artifacts (`.ai-factory/plans/*`, `.ai-factory/plan-reviews/*`, the `.json` sidecar) — protocol records, not runtime code; no review surface.

**Spec/plan mandate checked against:** spec 35 and the plan both require **behavior-identical**, frontmatter unchanged, no `docs/…` path link in the shipped body, the multi-tree raise never reduced to a link.

## What the change does (correct parts)

- **Frontmatter untouched** — `name` / `description` / `argument-hint` only; no `loads:` / `allowed-tools` added. ✅ matches guard.
- **No `docs/…` path link landed in the body.** The relink points at **global § "Grounding claims" by name**, exactly as the plan requires for a globally-shipped skill. ✅
- **Reference target verified accurate.** `src/global/CLAUDE.md` § "Grounding claims" (line 15) genuinely owns the two-entry-maps content ("`ROADMAP.md` … entry map of **time** … its counterpart `.ai-factory/ARCHITECTURE.md` is the entry map of **space** … the two maps together orient a cold session before any skill is invoked") and the decay rule (line 13, "re-read its leaf fresh"). The by-name pointer is not dangling and is loaded in every session. ✅
- **Protected content untouched** — the fractal model (14–24), Step 2 climb (45–64), Step 3 forest raise (66–78), depth rules (111–116), synthesis/intent block (80–107) are all byte-identical in the diff. The multi-tree shared-contract raise is not reduced to a link. ✅
- **Imperative-safety precondition holds** — the block still commands a read ("re-read them fresh here"), so the executor is not left with an inert pointer; and the always-loaded global rule does independently command raising each map. ✅

## Finding 1 (Low–Medium) — the `and` conjunction narrows the trigger; not behavior-identical for single-map projects

`src/skills/detangle/SKILL.md:30`

```
If `.ai-factory/ARCHITECTURE.md` and `.ai-factory/ROADMAP.md` exist, both are already
raised as the project's entry maps per global § "Grounding claims" — re-read them fresh
here for detangle's own angle: is the element you're looking at part of an in-progress or
planned roadmap milestone? That changes the impact analysis in Step 4.
```

The original used **two independent conditionals** — "If `ARCHITECTURE.md` exists — read it." and separately "If `ROADMAP.md` exists — read it." — so the executor read *whichever* file was present. The rewrite fuses them into a single **conjunction**: the block fires only when **both** files exist.

**Failure scenario:** a project that has `.ai-factory/ROADMAP.md` but no `.ai-factory/ARCHITECTURE.md` (or the reverse — common in early-stage projects, and detangle ships globally into many foreign roots). Under the original, detangle read the file that existed and applied its milestone-impact angle. Under the rewrite, `A and B` is false, so the entire block is skipped: the executor is given **no** detangle-specific instruction, and in particular the roadmap-milestone → Step-4-impact nudge (which is detangle's *own* contribution, not carried by the global rule) is silently dropped for the ROADMAP-only case.

This is a real, if narrow, violation of the plan's and spec's **behavior-identical** guard — the trigger condition changed from "either present" to "both present." The global grounding rule still raises whichever map exists at session entry, so nothing crashes, but detangle's own impact-analysis prompt no longer runs in the single-map case.

**Suggested fix:** restore independence of the guard, e.g. "If `.ai-factory/ARCHITECTURE.md` and/or `.ai-factory/ROADMAP.md` exist …" or "Whichever of `.ai-factory/ARCHITECTURE.md` / `.ai-factory/ROADMAP.md` exists is already raised …". Keeps the slim-in-place rewrite intact while preserving the original's per-file trigger.

## Note (non-blocking)

The rewrite drops the original's ARCHITECTURE-specific rationale ("module communication patterns and where boundaries are intentionally drawn") and keeps only the ROADMAP angle. This is intended by the plan — that meaning is now owned by the global rule's "entry map of space — module boundaries, the chosen pattern" — and the executor is still told to re-read `ARCHITECTURE.md`. No loss beyond Finding 1's conjunction issue. No action required.

---

Finding 1 should be corrected before merge (one-word guard fix). Everything else conforms to the spec and plan.
