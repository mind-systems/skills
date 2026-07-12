# Handoff — the architect over-specifies the editor and destroys its independence; "convergence" becomes an echo

> Process/design handoff, not a parked task. Surfaced live while running the `agent-architect` paired loop against a real repo (tradeoxy_core). The bug is in how the architect *prompts* the editor, and the fix is a `agent-architect` (and possibly editor) skill-definition change. Trust the reasoning here; the session that produced it isn't attached.

## 1. The problem in one line

When the architect hands the editor an **analysis** task (dry-run: review / decompose / hunt for hazards), pinning the architect's own candidate findings and a preliminary verdict into that prompt **contaminates the editor's reasoning** — its report comes back "fully converged" with the architect, and that convergence is read as confidence when it is actually **manufactured agreement**. The second mind was told the answer, so it stopped being a second mind.

## 2. Two work-order modes the architect must NOT conflate

- **Apply mode** (execute an already-decided change): pinning every value, path, exact `find/replace` string, guardrail is **correct**. The editor should apply deterministically and NOT re-decide. Verbosity here is precision.
- **Analysis / think mode** (judge, review, decompose, adversarially verify): the editor's entire value is **independent reasoning**. Pinning candidate hazards, a stress-test checklist, and a "my preliminary verdict is X" turns the editor into an executor of the architect's frame. Its "independent" review re-derives the architect's conclusion because it was handed it.

The failure is applying **apply-mode precision to an analysis-mode task**. Precision is right for a decided change and poison for an open question.

## 3. Evidence from the session

Four consecutive analysis dry-runs (a code-vs-spec orientation, then skeleton passes over three roadmap phases) each returned a report that "fully converged" with the architect's pre-stated assessment. The architect read four-for-four convergence as strong signal. In fact each dry-run prompt had pre-loaded: the three specific surfaces to stress-test, and a "my preliminary verdict: pass-through / here's the one gap" line. The editor dutifully confirmed exactly those surfaces and that verdict. A genuinely independent editor might have found a *different* gap, or challenged the verdict — but it was never given the room to; it was handed the map and asked to walk it.

Two smaller symptoms rode along:
- **Re-instructing "Read `~/.claude/skills/<name>/SKILL.md`" every work-order**, though the persistent editor loaded that skill once at session start and it is in its context. Wasteful, and it signals distrust that flattens the agent.
- **40–60 line prompts** where, for an analysis task, a single trigger line ("fresh skeleton pass, phase 14") is the whole correct prompt.

## 4. Why the current skill doesn't catch this

`agent-architect` already says, for reviews: *"run your own review in parallel, then reconcile … reach your own verdict independently before you weigh the editor's."* That guards **one half** of the independence — the *architect's* verdict must form before it sees the editor's. It says nothing about the **other half**: the *editor's* verdict must form without being seeded by the architect's. Both halves are required for a real second opinion. The skill protects the architect from anchoring on the editor, but not the editor from anchoring on the architect — and in practice the architect writes the prompt, so it is the editor's independence that is the easier and more damaging one to destroy.

There is a real tension the skill must name, not ignore: a work-order must be **self-contained and unambiguous** (the architect skill stresses this — pin every contract "a reader would not reconstruct identically twice"). For *apply* that means pinning values. For *analysis* the self-contained thing to pin is the **question and the target**, not the answer. The architect currently reads "self-contained" as "pin everything" and over-applies it to analysis.

## 5. The fix (skill-level)

In `agent-architect`, split the work-order guidance by mode:

- **Analysis / dry-run / review → minimal.** Give the editor the target and the question, nothing more. NO candidate findings, NO stress-test checklist, NO preliminary verdict, NO restated method, NO "read the skill" (it's loaded). The architect runs its OWN analysis separately and in parallel; then reconciles **two independently reached** results. If the two agree, that is now real signal; if they diverge, that divergence is the point of the pair.
- **Apply → pin exactly**, as today (values, paths, exact strings, guardrails, self-verify, "do not commit").
- **Persistent-editor hygiene:** skills/files loaded once in the session persist in the editor's context — never re-instruct reading them; reference by name.

A one-line test the architect can apply before sending any editor prompt: *"Am I telling it what to decide, or only what to look at?"* If the former on an analysis task, cut it back to the target + the question.

## 6. Blast radius / where it applies

Anywhere a driving agent fans work out to a reasoning sub-agent and then treats the sub-agent's answer as corroboration: paired-loop analysis, judge panels, adversarial-verify passes, multi-agent review. Seeding the sub-agent with the driver's hypothesis converts "N independent opinions" into "N copies of one opinion." The value of fan-out is diversity of thought; a prescriptive prompt spends the tokens and gets none of it.

## 7. One-line statement

For an analysis task, the correct prompt to an independent agent is the **question**, never the **answer** — pin values only when applying a decided change; pinning your conclusion into an open question buys you an echo and calls it agreement.
