# Plan Review: roadmap-decompose — extract `roadmap-engine` (artifact format)

**Plan:** `18-roadmap-decompose-extract-roadmap-engine-artifact-format-from-the-philosophy.md`
**Files reviewed:** `roadmap-engine/SKILL.md`, `roadmap-decompose/SKILL.md`, `aif-roadmap/SKILL.md`, full skills listing
**Risk Level:** 🟡 Medium

## Verdict

The plan is mechanically sound: the cited line numbers are accurate, the content-move is well-scoped, and — critically — nothing outside the two edited files references the strings being removed (`Input Contract`, `Per-Task Render Procedure`, "does NOT own"), so the deletion breaks no dangling references. The refactor's *framing goal* (engine = format explanation, not a render procedure) is coherent and improves the split.

However, the plan's stated **premise** — that the engine is "the shared explanation … invoked by `roadmap-decompose`, `roadmap-decompose-skeleton`, and `aif-roadmap`" — does not hold against the actual codebase. This is the main thing to resolve before/while implementing.

---

## Line-number & content verification (all accurate)

- decompose "Roadmap File Format" block **302–314** + contract-line rules **316–323** ✔
- decompose "Two-Tier Output (per task)" procedure **284–298** ✔
- decompose intro **line 16** (the "written manually following aif-note's note format" clause) ✔
- decompose Critical Rule 6 **line 332** ✔
- engine sections to delete — "Input Contract" (23), "Per-Task Render Procedure" (42), "What This Engine Does NOT Own" (94) — all present ✔
- grep confirms these removed strings live **only** inside `roadmap-engine/SKILL.md` — no external caller depends on them ✔

---

## Critical Issues

None that block correctness (no runtime, no broken references). The items below are architectural / spec-clarity concerns.

---

## Architectural Concern (primary) — the 3-caller premise is false

The plan (Context, Task 2) rests the engine's justification on three callers. Reality:

1. **`roadmap-decompose` does NOT currently load `roadmap-engine`.** It carries its *own* inline "Two-Tier Output" procedure (lines 284–298) and format block. Task 3 is what first wires decompose to the engine — so *after* this plan there is exactly **one** real caller.
2. **`aif-roadmap` does NOT invoke `roadmap-engine`** — grep finds zero references, and its `allowed-tools` (`Read Write Edit Glob Grep Bash(git *) AskUserQuestion Questions`) doesn't even include `Skill`, so it *cannot* invoke it as written. It is a separate strategic-planning skill with its own format.
3. **`roadmap-decompose-skeleton` does not exist** as a skill directory (it's named in the repo's "custom skills" list as a planned skill, but there is no `src/skills/roadmap-decompose-skeleton/`).

**Why this matters:** the repo's own composition rule (`CLAUDE.md` → "mechanism vs policy": *"Factor a capability into its own skill only when it carries shared content used by ≥2 callers — a pure router with no content of its own is negative value. Every loaded line is a recurring context cost"*) is exactly the test this refactor should be measured against. With a single real caller, having `roadmap-decompose` load a *separate* skill to read a format block it used to hold inline **increases** context cost (Skill invocation + full engine body vs. ~40 inline lines) rather than amortizing it.

This is a **pre-existing** condition (the engine already shipped with this framing) that the plan does not introduce — but the plan also does not address it, and **Task 2 perpetuates the inaccurate 3-caller description**. Recommended resolution, pick one:
- **(a)** State explicitly in the plan that the engine is forward-looking infrastructure for `roadmap-decompose-skeleton`/`aif-roadmap` wiring that lands in later milestones, and keep the description as aspirational — *and* file/track those wiring milestones so the engine isn't left as a single-caller router indefinitely; **or**
- **(b)** Trim the Task 2 description to name only the caller that actually wires in (`roadmap-decompose`) until the others exist.

Either is fine, but the plan should not silently assert three callers when two are phantom. **Severity: WARN** (does not break; undercuts the stated rationale).

---

## Medium — Task 3 internal contradiction (byte-identical vs. required edits)

Task 3 bullet 2 requires editing the Two-Tier Output references **inside** Mode 1 Step 1.4, Mode 2.4, and Mode 2.5 (repoint them at the engine's format). But Task 3's "**Keep byte-identical**" list says to leave *"all mode descriptions (create / update / decompose-existing / reprioritize / check)"* untouched. Steps 1.4 / 2.4 / 2.5 **are** part of those mode descriptions, so the two instructions collide.

An implementing agent following the byte-identical guard literally would fail to make the repoint edits (or vice-versa). **Fix:** add an explicit carve-out — the byte-identical guard covers mode descriptions *except* their `Two-Tier Output` references, which are the only spans being repointed; the Atomicity-Gate wording (1.3.1 / 2.4.1) and `AskUserQuestion` blocks stay verbatim.

---

## Minor

- **Task 1 guard vs. reframe.** The guard says diffing the engine body against decompose's removed text should show *"the same content — not a rewrite."* Yet the same task instructs reframing the two-tier note from **numbered steps** into **descriptive knowledge**. These are reconcilable (content preserved, form changed) but literally worded they conflict. Suggest: "same *content*, reflowed from numbered steps to prose — no invented modes/procedure/contract."
- **Dangling `---` separators.** Removing decompose lines 284–298 and 302–323 leaves the surrounding horizontal rules adjacent (line 282 `---` … line 300 `---`). Note in Task 3 that the implementer should collapse the now-orphaned `---` separators so the philosophy body reads cleanly.
- **Atomicity Gate coupling.** The inline Two-Tier Output procedure currently embeds the Atomicity Gate as step 2 (line 289). Task 1 correctly keeps the gate *out* of the engine (philosophy stays in decompose, which already has standalone 1.3.1/2.4.1 gate blocks). This is consistent — just confirming the implementer must not carry that step into the engine.

---

## Positive Notes

- Line references are precise and verified against current file state — rare and valuable for a text-move plan.
- The safety-critical check passes: removed engine sections have no external consumers, so the deletion is non-breaking.
- The framing shift (render procedure → contextual format explanation) genuinely fits the mechanism-vs-policy model and removes the awkward "Input Contract / does NOT own" scaffolding that read like an API for a skill that has no programmatic call surface.
- Task 4's verification checklist is concrete and testable, and correctly scopes out the untouched callers.

---

## Recommendation

Resolve the **Medium** contradiction (Task 3 carve-out) and **address the caller premise** (WARN) — at minimum by correcting the Task 2 description or explicitly marking the engine as forward-looking infra with tracked wiring milestones. The two Minor items are cleanup nudges for the implementer. None of these require re-architecting the plan; they are edits to the plan text.
