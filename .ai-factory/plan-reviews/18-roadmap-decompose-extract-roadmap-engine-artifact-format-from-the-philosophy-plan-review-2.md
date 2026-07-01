# Plan Review (round 2): roadmap-decompose — extract `roadmap-engine` (artifact format)

**Plan:** `18-roadmap-decompose-extract-roadmap-engine-artifact-format-from-the-philosophy.md`
**Files reviewed:** `roadmap-engine/SKILL.md`, `roadmap-decompose/SKILL.md`, `aif-roadmap/SKILL.md`, `roadmap-test-coverage/SKILL.md`, full `src/skills` listing, round-1 review
**Risk Level:** 🟡 Medium

## Verdict

The revision resolves every round-1 concern cleanly. The one thing left is a **new dangling-reference gap** the tighter carve-out introduced: the plan repoints the `Two-Tier Output` references at Steps 1.4 / 2.4 / 2.5 and simultaneously marks Step **2.4.1** byte-identical — but 2.4.1 itself contains a `Two-Tier Output` reference (decompose line 198) that will dangle once that section is deleted. Fix that one carve-out and the plan is ready.

---

## Round-1 items — all addressed

- **3-caller premise (WARN):** Fixed. New "Caller reality" section (plan lines 6–12) states decompose is the only real caller, `aif-roadmap` is untouched (verified: its `allowed-tools` lacks `Skill` and it holds zero engine references), and `roadmap-decompose-skeleton` does not exist (verified: no such directory). Task 2 now forbids asserting three callers and frames the engine as forward-looking shared-format infra. ✔
- **Task 3 byte-identical contradiction (Medium):** Fixed via the explicit carve-out at plan line 47 — the guard protects mode wording *except* the Two-Tier Output references being repointed. ✔ (but see the residual gap below)
- **Task 1 guard vs. reframe (Minor):** Fixed — now "same content, reflowed from numbered steps into prose" (plan lines 25, 31). ✔
- **Dangling `---` separators (Minor):** Fixed — Task 3 bullet 2 and Task 4(b) call for collapsing orphaned rules. ✔
- **Atomicity Gate coupling (Minor):** Fixed — Task 1 now explicitly says "Do NOT carry over the Atomicity Gate" and keeps it in decompose (plan line 29). ✔

## Line-number & fact re-verification (current file state)

- decompose "Roadmap File Format" heading **302**, block **304–314**, contract-line rules **316–323** ✔
- decompose "Two-Tier Output (per task)" procedure **284–298**; Atomicity Gate embedded as step 2 at **289** ✔
- decompose intro **line 16**, Critical Rule 6 **line 332** ✔
- engine sections to remove — "Input Contract" (23), "Per-Task Render Procedure" (42), "What This Engine Does NOT Own" (94) ✔
- `roadmap-engine` has exactly one referrer today (itself); no external skill loads it — confirms the single-caller reality ✔

---

## Medium — residual dangling reference inside Step 2.4.1 (line 198)

The plan enumerates the spans to repoint as **Steps 1.4 / 2.4 / 2.5** (plan lines 43, 47) and, in the same breath, protects the Atomicity-Gate blocks **1.3.1 and 2.4.1** as byte-identical/verbatim.

But decompose **line 198**, which lives *inside* Step 2.4.1, reads:

> If **no** → the task is atomic, proceed with the **Two-Tier Output procedure**.

That "Two-Tier Output procedure" is precisely the section Task 3 deletes (lines 284–298). So the plan's own guard, taken literally, preserves a reference to a section that will no longer exist — a dangling internal pointer, and a self-contradiction with Task 4(c) ("Atomicity Gate wording … unchanged apart from the repointed Two-Tier Output references").

The five `Two-Tier Output` references in decompose are lines **136** (1.4), **187** (2.4), **198** (2.4.1), **208** and **210** (2.5). The plan's repoint list covers 1.4 / 2.4 / 2.5 — i.e. 136, 187, 208, 210 — but **omits 198**, the one embedded in the gate block it marks verbatim.

**Fix (small edit to plan Task 3):** extend the carve-out to name line 198 as well — repoint it to the engine's format (e.g. "→ the task is atomic; produce the two-tier artifacts per the engine's format") while keeping the gate's actual decision logic verbatim. Equivalently: the byte-identical guard on 2.4.1 protects the *gate wording*, but its trailing `Two-Tier Output` reference is repointed like the others so no pointer to the deleted section survives. (Mode 1's gate, Step 1.3.1, has no such reference — its closing lines point at "Step 1.4", which stays — so only 2.4.1 needs this.)

**Severity: Medium** — does not break the refactor's intent, but leaves a broken internal reference and contradicts the plan's stated guard; worth a one-line plan edit before implementing.

---

## Accepted WARN (carried, not a blocker) — single real caller

The composition rule in `CLAUDE.md` ("factor into its own skill only when it carries shared content used by ≥2 callers") is in tension with the post-plan reality of one caller. The plan now handles this honestly: it declares the engine forward-looking shared-format infra and states (line 12) it "does not fix [the pre-existing condition] beyond making the wording honest." That is a legitimate, transparent scoping decision, not a defect the plan introduces. No action required here beyond keeping the later `aif-roadmap` / `roadmap-decompose-skeleton` wiring on the roadmap so the engine doesn't remain a single-caller loader indefinitely.

---

## Positive Notes

- The "Caller reality" section is exactly the right response to round-1: it corrects the premise in prose, cites the concrete evidence (missing `Skill` tool, absent directory), and scopes the wiring out explicitly rather than silently.
- The byte-identical carve-out (plan line 47) is precisely worded and directly dissolves the round-1 contradiction — it just needs to reach one line further into 2.4.1.
- Task 1's "same content, reflowed from steps to prose" framing correctly separates content-preservation from form-change, and the explicit "do not carry the Atomicity Gate / Input Contract / does-NOT-own list into the engine" instructions keep philosophy and format cleanly separated.
- Removing the "Input Contract" scope caveat (note-creation-only) is coherent with the reframe: once the engine is format knowledge rather than a procedure, Mode 2.5's in-place note edit is just decompose applying that format, so no scope limitation is needed.
- Task 4's checklist remains concrete and testable and correctly scopes out the untouched callers.

---

## Recommendation

One small edit: extend Task 3's carve-out to repoint the `Two-Tier Output` reference at decompose **line 198** (inside Step 2.4.1), so the deletion leaves no dangling pointer. Everything else is solid and verified. Because this leaves a concrete unresolved gap in the plan text, this review does not pass yet.
