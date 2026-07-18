---
name: task-rescue-audit
description: >-
  Outside-view audit of a task that looped (2–3 rounds at plan-review or
  implement-review) or is a wall-clock outlier — even if it ultimately passed.
  Diagnoses whether convergence came from genuine understanding or from band-aid
  accretion around one structural/spec gap the implementation routed around. Emits
  a diagnosis plus one upstream recommendation to chat only — no files written, no
  ROADMAP edits. Run right after `task-rescue` while artifacts are warm, or
  cold on any looped/outlier task — or in any session, on smell, when you suspect
  the orchestrator stuck crutches around crooked architecture or spaghetti code.
  Trigger phrases: "audit", "convergence audit", "did it converge or band-aid",
  "band-aid check", "outside-view audit".
argument-hint: "[task-slug]"
allowed-tools: Read Glob Grep Bash(git *) Skill
loads: orchestrator-artifacts
---

# Task Rescue Audit

Asks the question the green check doesn't: **Convergence by Understanding, or by
Attrition?** A task can pass after 2–3 rounds by genuinely solving each
independent finding, or by layering local workarounds over one structural gap that
was never named. This audit tells the difference.

---

## Inputs

The orchestrator artifacts for **one task** — the plan, all plan-reviews (every
round), implementation diffs or patches, code-reviews (every round), and any final
state files. When run right after `task-rescue` these are already in context.
If run cold, locate and read them before Step 1: cold rescue takes an optional slug
naming the task as `$1`; when no slug arrives, identify the target from the user's
prose plus a `Glob` over `plan-reviews/`/`reviews/` for the matching
`<seq>-<slug>-*` artifacts.

Ensure `orchestrator-artifacts` is loaded once this chat (via the Skill tool, only
if not already loaded) — see it for the artifact layout, naming, round numbering,
PASS signals, and the deferred-observations section format this audit relies on
below.

---

## Step 1 — Reconstruct the finding→fix chain

Read every plan-review and code-review for this task, in round order. For each
round, capture: the finding(s) + severity, the fix applied, and whether that fix
introduced or revealed the next round's finding. Note the total round count,
whether severity trended up, down, or flat across rounds, and the final outcome
(pass or fail).

This is **internal working material, not the deliverable** — organize it however
is convenient (a scratch table, one row per round, works). The **user-facing form
is produced in Step 6**, as a narrative, not this scratch structure.

**Deferred observations are captured separately, not as findings.** Entries under a
review's `## Deferred observations` section are **excluded** from the finding→fix
chain, the round count, and the severity trend — per `orchestrator-artifacts` they are
non-findings. Capture each one as separate working material: round, `Affects:` target,
and a one-line gist — see `orchestrator-artifacts` for the section format; do not
redefine it here.

---

## Step 2 — Central question

State plainly which of these best describes the chain:

**A.** N independent local corrections — each finding is a distinct problem in a
distinct area; the fix closes it and nothing downstream opens.

**B.** N symptoms of ONE structural or spec gap — each fix patches the surface
manifestation while the gap remains, causing the next round's finding to be a
sibling of the same root.

Neither answer is final here. Step 3 provides the decisive test.

---

## Step 3 — The one-sentence root-cause test (decisive)

Attempt to write **one sentence** — a spec clause or design constraint — such that,
had it been present from the start, ALL N findings would not have occurred.

- **If that sentence exists and is structural** (names a data-model invariant,
  a state-machine constraint, a derivation rule, an API contract — not a mechanical
  "don't forget X"): this is **band-aid accretion**. Name the sentence. Then state
  the structural reframe — the data-model / derived-state / invariant change at the
  *what* level that dissolves the findings by construction rather than patching each.
  Proceed to Step 4 to corroborate.

- **If no single sentence covers all N findings**: the findings are independent.
  Declare **healthy convergence** and stop at Step 5 — skip Step 4's discriminators.

**Default is NOT band-aid.** Over-flagging independent legitimate fixes as band-aid
accretion is itself a failure mode. Require the single-sentence test to succeed
before claiming accretion. If uncertain, declare "Mixed" with low confidence.

**Corroboration from captured deferred observations.** Check the observations
captured in Step 1 against the root-cause sentence above. When one describes the same
gap the finding→fix chain circles around, name it in the narrative (Step 6) as
corroboration — quoting the observation and its round — that the gap was visible early
and routed around instead of fixed. This is **corroborative only**: it never replaces
the one-sentence test above, and the absence of a matching observation carries no
weight either way — do not treat "no matching observation" as evidence against
band-aid accretion.

---

## Step 4 — Discriminators (corroborate, don't replace Step 3)

Run these only when Step 3 found a candidate root-cause sentence. They
corroborate or weaken the claim — they do not substitute for Step 3.

**Band-aid accretion signals:**
- One common root clause explains multiple findings across rounds
- Fixes are local and additive — a flag, guard, special-case, or nil-check bolted
  onto existing logic rather than changing the shape
- Next round's finding is a same-class sibling of the prior (whack-a-mole pattern)
- Boolean complexity grows round-over-round without a corresponding domain concept
- State variables carry workaround names: `sessionHasData`, `isBridging`,
  `skipOnFirst`, `wasAlreadySet`
- A fix works against stated design intent (e.g. caching something the design says
  must be fresh)
- Reviewer language signals resignation: "carried over", "still present", "transient,
  self-heals", "accepted behavior"

**Legitimate fix signals:**
- Findings are independent — different files, different subsystems, different
  failure modes
- Genuinely local problems: a missing guard, a wrong default, a typo — each closed
  by its own fix with no siblings
- Severity trends downward and the surface is diverse (not the same subsystem re-failing)
- Fixes map to recognizable domain concepts and hold or reduce complexity across
  rounds

Use the discriminators to raise or lower confidence in the Step 3 verdict, not to
override it.

---

## Step 5 — Verdict

State the verdict on this spectrum:

```
[Independent legitimate fixes] — [Mixed] — [Band-aid accretion]
```

Include:
- **Confidence:** low / medium / high
- **Evidence:** the narrative is the evidence; the verdict sentence names the 1–2
  strongest signals from it

"Mixed" is a valid verdict when some findings are independent and some are symptoms
of a common gap. Default to the left (legitimate) end of the spectrum in the
absence of strong common-root-cause evidence.

---

## Step 6 — Output (to chat only)

Emit the diagnosis to chat. No files are written and the ROADMAP is never edited.

**Form: a chronological narrative in plain prose** — the same register as
`task-rescue`'s Diagnosis Report. Tell the task's story round by round, in
complete sentences: what the implementation did, what the review found, what the fix
changed, and what that fix introduced or revealed next. One short paragraph per round
is the natural shape; a single-round audit may be a single paragraph. Weave reviewer
findings in as quotes or paraphrases rather than listing them. **No tables, no
fragment-style bullet lists** — the deliverable is a story the user reads once, top
to bottom, not a grid to reconstruct. Round counts and severity trends are legitimate
vocabulary within the prose — convergence across rounds is the audit's subject; the
ban is on tabular/fragment *form*, not on mentioning rounds. **Length scales with the
number of rounds** — never compress a multi-round chain to fit a size budget.

**The narrative ends with the verdict**: spectrum position (independent legitimate
fixes / mixed / band-aid accretion) + confidence, in one or two sentences whose
support the narrative has already told through the rounds above it.

**When verdict is Band-aid accretion or Mixed, continue past the verdict with:**
- The root-cause sentence from Step 3 (the missing spec/design clause) as the payoff
  line, placed immediately after the verdict and visually set off as a block quote.
- The structural reframe — the *what*-level change (data-model / derived-state /
  invariant) that dissolves all N findings by construction rather than patching each
  symptom — as a short prose paragraph; do not prescribe implementation (no *how*).
  Weave the per-fix mapping into this same paragraph: for each band-aid fix, one or
  two sentences on what the structural change replaces it with — not a mapping table
  or arrow list.
- One upstream recommendation, stated plainly as the closing sentence:
  - *Amend the task spec* — if the gap fits cleanly in one sentence
  - *Decompose the task* — if the structural reframe spans multiple concerns
  - *Re-architect before retrying* — if the gap is foundational
  - *Accept as-is* — if the cost of the structural change outweighs the benefit
    (mixed verdict, low round count, low severity)

**Always end with:**
- Cost note as a single line: round count, wall-clock if known

---

## What NOT to do

- Do not rewrite the plan or implement anything — produce only a chat diagnosis
- Write no file, ever — no patches, no task-spec edits, no ROADMAP changes, no
  rewriting plan or review file content
- Do not declare band-aid accretion without the single-sentence test in Step 3
- Do not judge any individual fix in isolation — judge the **sequence**
- Do not treat a passing task as automatically healthy; loops on cosmetic
  findings are a weak signal, but one structural-root signal outweighs them
- Do not present the finding→fix chain as a table or as compressed fragments in the
  output — tables are permitted only as internal scratch during Step 1; the
  deliverable is a story the user reads once, top to bottom
- Both outcomes are valid — healthy convergence is the expected result; band-aid
  accretion is the exception worth naming
- Do not count deferred observations as findings — they never contribute to the round
  count, the severity trend, or the whack-a-mole discriminator in Step 4
- Do not let a matching deferred observation replace the one-sentence root-cause test
  in Step 3 — it corroborates a verdict already reached, never substitutes for reaching it
- Sweeping or deleting the roadmap is not this skill's job — do not touch it
