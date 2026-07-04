---
name: milestone-rescue-audit
description: >-
  Outside-view audit of a milestone that looped (2–3 rounds at plan-review or
  implement-review) or is a wall-clock outlier — even if it ultimately passed.
  Diagnoses whether convergence came from genuine understanding or from band-aid
  accretion around one structural/spec gap the implementation routed around. Two
  modes: `rescue` (default) emits a diagnosis plus one upstream recommendation to
  chat, appending only status marks on evaluated deferred observations — no content
  rewrites, no ROADMAP edits; `prune` runs when `roadmap-prune`'s gate refused,
  pinning every unpinned observation via the same marks plus promotion appends into
  existing files. Run `rescue` right after `milestone-rescue` while artifacts are
  warm, or cold on any looped/outlier task; run `prune` when a roadmap prune is
  blocked on unpinned observations. Trigger phrases: "audit", "convergence audit",
  "did it converge or band-aid", "band-aid check", "outside-view audit", "prune gate
  blocked", "pin deferred observations".
argument-hint: "[rescue|prune]"
allowed-tools: Read Edit Glob Grep Bash(git *)
loads: orchestrator-artifacts
---

# Milestone Rescue Audit

Asks the question the green check doesn't: **Convergence by Understanding, or by
Attrition?** A milestone can pass after 2–3 rounds by genuinely solving each
independent finding, or by layering local workarounds over one structural gap that
was never named. This audit tells the difference.

---

## Run mode

`$1` selects the mode. The dispatch is total: `$1 == "prune"` selects prune mode;
everything else — absent, `rescue`, or any other token (including a bare task slug
from the historic invocation form) — selects rescue mode. When `$1` selects rescue
mode but is neither absent nor `rescue`, treat it as the cold-rescue slug (the `$2`
role in `## Inputs` below) rather than an error.

- **`rescue`** — the historic behavior. Runs on one failed/looped task's artifacts,
  warm (right after `milestone-rescue`) or cold, hunting for band-aid accretion.
- **`prune`** — runs when `roadmap-prune`'s deferred-observations gate refused to
  proceed. Evaluates and pins every unpinned `## Deferred observations` entry across
  the target repo's review artifacts so the gate can pass on the next `roadmap-prune`
  run.

Ensure `orchestrator-artifacts` is loaded once this chat (via the Skill tool, only if
not already loaded) — it defines the artifact layout, naming, rounds, signals, and the
status-marker grammar both modes rely on below.

---

## Inputs

**`rescue` mode:** the orchestrator artifacts for **one task** — the plan, all
plan-reviews (every round), implementation diffs or patches, code-reviews (every
round), and any final state files. When run right after `milestone-rescue` these are
already in context. If run cold, locate and read them before Step 1: cold rescue takes
an optional slug naming the task, as `$2` when `$1` is `rescue`, or as `$1` itself per
the `## Run mode` dispatch rule (the historic bare-slug invocation); when no slug
arrives either way, identify the target from the user's prose plus a `Glob` over
`plan-reviews/`/`reviews/` for the matching `<seq>-<slug>-*` artifacts.

**`prune` mode:** the target repo's `.ai-factory/plan-reviews/` and
`.ai-factory/reviews/` directories **in full** — every file in both, not one task's
slice.

For the artifact layout, naming convention, round numbering, and PASS signals, see the
loaded `orchestrator-artifacts` engine.

---

## Step 1 — Reconstruct the finding→fix chain

Read every plan-review and code-review for this task, in round order. For each
round, capture: the finding(s) + severity, the fix applied, and whether that fix
introduced or revealed the next round's finding.

This reconstruction is **internal working material, not the deliverable** — organize
it however is convenient while analyzing (a scratch table, one row per round, is a
fine way to keep it straight). The capture list above is a checklist of what to note
per round, nothing more. The **user-facing form is produced in Step 6**, as a
narrative — not this scratch structure.

Note the total round count, whether severity trended up, down, or flat across
rounds, and the final outcome (pass or fail).

Do not interpret yet — just reconstruct. The full chain is the evidence.

**Deferred observations are captured separately, not as findings.** Entries under a
review's `## Deferred observations` section are **excluded** from the finding→fix
chain, the round count, and the severity trend — per `orchestrator-artifacts` they are
non-findings. Capture each one as separate working material: round, `Affects:` target,
and a one-line gist. Skip any entry that already carries an `audit-*` marker (per the
engine's grammar) — it has already been evaluated by a prior audit; its existing
verdict may still be cited as-is, it just does not need re-evaluating. This capture is
internal scratch, same as the finding→fix chain above — see `orchestrator-artifacts`
for the section format and marker grammar; do not redefine either here.

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

Mark only the observations the audit actually evaluated against the chain/code —
append `[audit-corroborated]` (it matches the root-cause gap) or `[audit-dismissed]`
(evaluated and found unrelated or stale) to the entry line via `Edit`, per the engine's
append-only status-marker grammar. Observations merely captured in Step 1 but never
weighed against a verdict stay unmarked — never mark an entry you did not actually
judge. When marking, mark every sibling occurrence of the same entry across the
milestone's review files (dedup by `Affects:` target + gist, per the engine's rule).

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

Emit the diagnosis to chat. Beyond the status-suffix marks in the Write contract
below, no files are written and the ROADMAP is never edited.

**Form: a chronological narrative in plain prose** — the same register as
`milestone-rescue`'s Diagnosis Report. Tell the milestone's story round by round, in
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
  - *Amend the spec note* — if the gap fits cleanly in one sentence
  - *Decompose the milestone* — if the structural reframe spans multiple concerns
  - *Re-architect before retrying* — if the gap is foundational
  - *Accept as-is* — if the cost of the structural change outweighs the benefit
    (mixed verdict, low round count, low severity)

**Always end with:**
- Cost note as a single line: round count, wall-clock if known

---

## Prune mode — pin every deferred observation

This section runs only when `$1` is `prune`. It does not touch Steps 1–6 above —
those remain the rescue pipeline, unchanged, for `rescue` mode.

Prune mode exists because `roadmap-prune`'s deferred-observations gate refuses to
proceed while any unpinned entry remains. This mode evaluates and pins every one of
them so the next `roadmap-prune` run can pass the gate.

1. **Discover.** Scan every `.md` file under `<target repo root>/.ai-factory/plan-reviews/`
   and `<target repo root>/.ai-factory/reviews/` for a `## Deferred observations`
   section (same scan `roadmap-prune`'s gate performs). Collect every entry line that
   is **not pinned** per the engine's grammar (pinned = the entry line carries ≥1
   bracketed status marker — do not redefine, cite the engine).

2. **Dedup.** Group the collected entries by `Affects:` target + gist, per the
   engine's dedup rule — a real-world gap reported in more than one review file is one
   observation with several sibling occurrences, not several observations.

3. **Evaluate each distinct observation** against the current code and roadmap: does
   the gap it describes still hold, or has it since been resolved or obsoleted by
   later work?

4. **Pin per the engine's markers**, then apply the same marker to **every** sibling
   occurrence across the milestone's review files (dedup rule from step 2):
   - Stale, wrong, or already resolved by later work → `[audit-dismissed]`
   - Real, and `Affects:` resolves to an existing file under the target repo root →
     append the entry verbatim (plus the source `<seq>-<slug>` slug) under a
     `## Deferred observations` heading in that target file — create the heading at
     the end of the file if it is absent — then mark the source entry/entries
     `[promoted → <path>]`
   - Real but unroutable (`Affects:` names a phase, `unknown`, or a path that does not
     resolve to an existing file) → report the observation verbatim in this mode's
     output and mark it `[unrouted-reported]`

   **No route-guessing**: no phase-name resolution, no fuzzy matching. Only an
   `Affects:` value that resolves to an existing file under the target repo root
   promotes — anything else is unrouted, never guessed.

5. **Exit criterion.** Continue until zero unpinned entries remain across both dirs.

6. **Summary.** End with counts per marker (`audit-dismissed`, `promoted`,
   `unrouted-reported`) and the full unrouted list, so the user can route those by
   hand.

---

## Write contract

Both modes are chat-first; the only writes either one ever performs are these two,
both append-only:

- **Status-suffix marks** on a deferred-observation entry line in a review file —
  `[audit-corroborated]` or `[audit-dismissed]` from rescue mode's Step 3 corroboration
  pass; `[audit-dismissed]`, `[promoted → <path>]`, or `[unrouted-reported]` from prune
  mode's evaluation of each entry — appended per the engine's grammar. The entry text
  and its `Affects:` value are never rewritten.
- **Promotion appends**, prune mode only: the entry, verbatim, plus its source
  `<seq>-<slug>` slug, appended under a `## Deferred observations` heading in the
  `Affects:`-target file — creating that heading at end-of-file only if it is absent.

No other file is ever written or edited, in either mode. Step 6's diagnosis is chat
output only — it is never written to a patch, a spec note, a plan, or the ROADMAP.

---

## What NOT to do

- Do not rewrite the plan or implement anything — produce only a chat diagnosis
- Do not write any file beyond the Write contract above — no patches, no spec-note
  edits, no ROADMAP changes, no rewriting plan or review file content
- Do not declare band-aid accretion without the single-sentence test in Step 3
- Do not judge any individual fix in isolation — judge the **sequence**
- Do not treat a passing milestone as automatically healthy; loops on cosmetic
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
- Do not guess routes in prune mode — no phase-name resolution, no fuzzy matching;
  only an `Affects:` value that resolves to an existing file promotes
- Do not redefine the marker grammar, rewrite entry text, rewrite `Affects:` values, or
  rewrite existing markers — status suffixes only ever accumulate
- Do not mark an observation `[audit-corroborated]`, `[audit-dismissed]`, or
  `[unrouted-reported]` unless it was actually evaluated against the chain/code
- Do not sweep, delete, or touch the roadmap in either mode — that is `roadmap-prune`'s
  job, not this skill's
