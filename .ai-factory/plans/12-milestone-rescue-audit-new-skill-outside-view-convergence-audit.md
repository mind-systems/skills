# Plan: milestone-rescue-audit — new skill — outside-view convergence audit

## Context
Add a downstream-only, read-only sibling skill to `milestone-rescue` that audits a milestone which *passed but looped* (2–3 rounds at plan-review/implement-review, or a wall-clock outlier) to diagnose whether it converged by understanding or by band-aid attrition — emitting a diagnosis plus one upstream recommendation to chat, with no file or ROADMAP edits.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Author the skill

- [x] **Task 1: Create `milestone-rescue-audit/SKILL.md` — frontmatter + Inputs block**
  Files: `src/skills/milestone-rescue-audit/SKILL.md`
  Create the new skill directory and file (no `references/`, `scripts/`, or `templates/`). Write the YAML frontmatter exactly per repo authoring rules:
  - `name: milestone-rescue-audit` (must match the directory name)
  - `description: >-` — what it does + when to use it: outside-view audit of a looped/outlier task (even one that passed) to distinguish band-aid accretion from healthy convergence; run after `milestone-rescue` while artifacts are warm. Include trigger phrases (e.g. "audit", "convergence audit", "did it converge or band-aid").
  - `argument-hint:` — quoted; e.g. `"[milestone slug | leave empty if artifacts in context]"`.
  - `allowed-tools: Read` — read-only; the skill diagnoses, never edits or implements.
  Then a short H1 title and 1–2 sentence intro framing the question as "Convergence by Understanding or by Attrition?", and a thin **Inputs** block (~3–4 lines) right after the intro: it expects the orchestrator artifacts for ONE task — the plan, all plan-reviews, implementation diffs/patches, code-reviews, and final state; usually already in context because it runs right after `milestone-rescue`; if run cold, locate them and **see `milestone-rescue` for the artifact layout** rather than re-documenting it here. Follow the structural/style conventions of `src/skills/milestone-rescue/SKILL.md`.

- [x] **Task 2: Write the audit procedure body (Steps 1–6 + Guardrails)** (depends on Task 1)
  Files: `src/skills/milestone-rescue-audit/SKILL.md`
  Append the "Outside-View Audit" procedure, keeping the user's wording from the spec note almost verbatim:
  - **Step 1 — Reconstruct the finding→fix chain.** Ordered per round: round → finding(s) + severity → fix applied → did that fix introduce/reveal the next round's finding. Note round count, severity trend, and final pass/fail.
  - **Step 2 — Central question.** N independent local corrections, or N symptoms of ONE structural/spec gap the implementation routes around?
  - **Step 3 — The one-sentence root-cause test (decisive).** Can you write the SINGLE spec/design sentence that, had it been present, would have prevented ALL N findings at once? If structural and it exists → band-aid accretion (name it, give the structural reframe). If no single sentence → independent legitimate fixes → healthy convergence, stop. State plainly that the default is NOT band-aid and that over-flagging legitimate fixes is itself a failure mode.
  - **Step 4 — Discriminators (corroborate, don't replace the test).** BAND-AID ACCRETION signals (one common root; local/additive fixes — flag/guard/special-case; whack-a-mole same-class finding next round; growing boolean complexity; workaround-named state like `sessionHasData`/`isBridging`; a fix fighting stated design intent; reviewer language "carried over"/"still"/"transient, self-heals"/"accepted behavior") vs LEGITIMATE FIXES (independent findings; genuinely local problems; severity trending down across a diverse surface; fixes map to domain concepts and hold/reduce complexity).
  - **Step 5 — Verdict on the spectrum.** `[Independent legitimate fixes] — [Mixed] — [Band-aid accretion]` + confidence + evidence. "Mixed" is allowed. Require common-root-cause evidence before claiming accretion; default is NOT band-aid.
  - **Step 6 — Output (to chat only).** Verdict + confidence + one-line justification; the finding→fix chain as the evidence table; if accretion/mixed — the root-cause sentence, the structural reframe that dissolves the findings by construction (data-model / derived-state / invariant change at the *what* level, not a full redesign), and a band-aid → replacement mapping; one upstream recommendation said plainly (amend spec / decompose milestone / re-architect — vs accept as-is); a cost note (round count + wall-clock).
  - **Guardrails / What NOT to do.** Both outcomes are valid; judge the SEQUENCE, not any single fix; do not rewrite the plan, implement, write a file, or edit ROADMAP — produce only a chat diagnosis with one upstream recommendation.

### Phase 2: Survive upstream sync

- [x] **Task 3: Register the skill in `CLAUDE.md`** (depends on Task 2)
  Files: `CLAUDE.md`
  In the Upstream Sync section, under **"Custom skills — never overwrite from upstream:"**, add `milestone-rescue-audit` to the bullet list (next to `milestone-rescue` and the other custom skills) so the next upstream sync does not wipe it. Do not alter other Upstream Sync entries.
