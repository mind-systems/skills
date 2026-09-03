## Code Review Summary

**Files Reviewed:** plan + 2 target files (`src/skills/architect-pairing-engine/SKILL.md`, `src/skills/agent-architect/SKILL.md`), spec 99, contract line 26.8, handoff 08
**Risk Level:** 🟡 Medium

### Context Gates

- **Architecture** (`.ai-factory/ARCHITECTURE.md` § "Composition: mechanism vs policy") — PASS. The one-block relay rule stays in `architect-pairing-engine` and is explicitly kept out of `architect-editor-engine`, which remains the delivery-agnostic format engine — one home per fact, engine holds mechanism only. The added load instruction lives in the caller's body while `loads:` keeps declaring the graph alone, matching the correction 26.7 made to the sibling engine.
- **Rules** — `.ai-factory/RULES.md` absent; no `.ai-factory/skill-context/aif-review/SKILL.md`. WARN (optional files, nothing to enforce).
- **Roadmap** — PASS. Contract line 26.8 is `[ ]` at `.ai-factory/roadmaps/trickster77777.md:98`, its `Spec:` tag resolves to `.ai-factory/specs/trickster77777/99-pairing-wiring-left-half-finished.md`, and all seven plan edits map 1:1 onto the spec's seven pinned changes. Handoff 08 § 4/§ 8/§ 10 confirms the same scope, including the `loads:`-without-load gap the plan folds in.

### Verified against ground truth

I re-derived the plan's own claims rather than trusting them:

- All six pinned blocks measure ≤76 under `python3 len()` (the `description:` block ≤74) — the plan's "already wrapped to that width" holds.
- The three re-wrapped paragraphs (check paragraph, `description:` tail, `agent-architect:184-188`) are word-preserving: normalizing whitespace and applying only the pinned substitution to the `HEAD` text reproduces the pinned block byte-for-byte in all three cases.
- The § Assumption inventory of pre-existing over-76 lines in `agent-architect` (`4-8, 13, 19-21, 23, 79, 81, 118, 186, 192, 210-211`) matches the file exactly — the deviation from the spec's whole-file width check is correctly grounded.
- Current occurrence counts confirm the expected post-state: `architect-pairing-engine` in `agent-architect` = 2 → 3; `paired architect` = 0 → 1; `single code block` = 0 → 1; `applies through its own editor` lands once (the body's new paragraph says "message to its own editor", not the counted phrase).
- Paragraph boundaries are right: blanks at `:51` and `:57`, `:65`, and the first deciding-half paragraph ends at `:41`. `agent-architect:25-26` does carry the generic fallback the plan relies on after deleting the supersession paragraph.

### Critical Issues

**1. § Assumption and the last edit task contradict each other about `agent-architect:186` — the Verify list encodes a check that fails on a correct implementation.**

§ Assumption pins the width check as "every added line in `git diff` is ≤76 … and **every pre-existing over-width line stays exactly as it is**", and lists `:186` among those lines (it is 77 characters: `round is settled is what counts, not who reads it. A relay and its work-order`). But the task **Name the paired architect as a possible work-order addressee** re-wraps the whole paragraph `:184-188`, which necessarily rewrites `:186`. The Verify task then restates the impossible condition verbatim: "Pre-existing over-width lines listed in § Assumption must be unchanged."

Failure mode: the implementer applies the pinned re-wrap correctly, runs the Verify list literally, sees `:186` changed, and either reports a false failure (burning an iteration) or "repairs" it by restoring the old wrap — which would drop the pinned addressee text or leave the paragraph mis-wrapped.

Fix: exclude `:186` from the Assumption's must-stay list (it is inside a paragraph this task re-wraps), or restate the invariant as "no pre-existing over-width line outside the two re-wrapped paragraphs changes."

**2. Every line reference is stated against `HEAD`, but the plan's own edit order shifts them — and one task carries no ordering edge at all.**

The plan sequences edits with `depends on` but never says its line numbers are pre-task coordinates. Three of them are already stale by the time their task runs:

- Within the applying-half chain, **Replace the originates-no-edit paragraph** turns 5 lines into 6. The check paragraph is then at `:59-65`, not the `:58-64` the next task names; after that, the blank line is at `:66` and the supersession paragraph at `:67-70`, not the `:65` / `:66-69` the delete task names.
- **Name the editor as the hand in `description:`** turns lines `9-13` into 6 lines (+1), shifting the entire body down by one. **Insert the single-code-block rule** has *no* `depends on` edge, so if it runs after the `description:` task its anchors `:41` and `:43` are both off by one; if it runs before the applying-half chain, that chain's `:52-56` are off by six.
- In `agent-architect`, **Instruct the load where the pairing role is recorded** replaces 3 lines with 4 (+1). There is no dependency edge between the two `agent-architect` tasks, so if it runs first the next task's `:184-186` / `:184-188` are off by one.

Each task does carry a text anchor ("the paragraph between the blank lines", the quoted opening words, "immediately after the first paragraph — the one ending …"), so a careful implementer recovers. But the numbers as written are wrong at execution time, and a plan that pins line numbers this precisely invites them to be trusted. Fix: add the missing `depends on` edges to fix a total order (in particular, make the insert task depend on the `description:` task, and the `:184-188` task depend on the `:61-65` task), and state once that all line numbers are relative to `HEAD` — anchors, not addresses.

### Minor Issues

**3. Nothing in the Verify list asserts that "every change *it makes* to a shared artifact" is gone.**

The plan's Context names that clause as one of the three carriers of the wrong model ("What disappears with it"), and the pinned replacement drops "it makes". The Verify list checks `does not route it onward…` → 0 and `the way an editor would` → 0, but no check covers the "it makes" clause; the word-preservation check only applies to re-wrapped paragraphs, and this paragraph is a wholesale replacement. A one-line addition — `every change it makes` → 0 in `src/skills/architect-pairing-engine/SKILL.md` — closes it at zero cost.

### Positive Notes

- The § Assumption is exactly the right shape for a `DEVIATION`: it names the spec's check, names the ground truth that disagrees, and re-scopes the check to what the task actually writes — with the pre-existing over-width lines enumerated so the narrowing is auditable rather than an excuse.
- The verification method inherited from the spec is genuinely load-bearing: whitespace-normalized counting instead of line-oriented `grep` on a 76-wrapped file, `python3 len()` instead of byte counters for em-dashes, and word-sequence comparison against `git show HEAD:<path>` to catch a word dropped in a re-wrap. Each of those corresponds to a recorded past failure (handoff 08 § 6.6, § 6.7) — the plan carries the lesson, not just the rule.
- The scope check is correctly path-scoped (`-- src/ .ai-factory/roadmaps/`), so it is invariant to the spec file's own uncommitted tracking state — which is genuinely dirty in this tree right now and would have defeated a whole-tree `--stat`.
- Guards are stated as guards, not hopes: the check paragraph 26.6 settled is protected by an explicit "no correction licence, no round-closing clause, no third mode may return with this re-wrap", which is precisely the failure 26.5 → 26.6 exists to undo.

## Deferred observations

- Affects: `src/skills/architect-pairing-engine/SKILL.md:40-41` (§ "The deciding half") / a follow-up task in phase 26 — The plan states it removes the own-hands model "from all three places it lives", but a fourth carrier survives one section above the ones it edits: "The applying architect is the one that acts on shared artifacts, not this half's own editor." After this task, the applying architect does not act on shared artifacts — its editor does; the sentence's contrast is about which *side* the change lands on, but it does so in the exact vocabulary the task is purging, and a deciding-half architect reading only its own section would reconstruct the rejected model. Fixing it is out of this task's reach in three independent ways: spec 99 pins exactly seven edits, the plan's own guard freezes both deciding-half paragraphs word-for-word, and handoff 08 § 11 records the user's ruling that the deciding half "is correct and must not be touched". It wants a ruling and a task of its own, not a silent widening of this one.
