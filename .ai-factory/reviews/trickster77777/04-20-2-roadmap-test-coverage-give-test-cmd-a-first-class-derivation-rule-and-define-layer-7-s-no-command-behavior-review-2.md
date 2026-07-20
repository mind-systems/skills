# Code Review 2 (re-review) — 20.2 `$TEST_CMD` derivation rule + Layer 7 no-command behavior

Re-review after fixes addressing [review-1](04-20-2-roadmap-test-coverage-give-test-cmd-a-first-class-derivation-rule-and-define-layer-7-s-no-command-behavior-review-1.md). All cited lines re-read from disk this pass; no verdict below rests on session memory.

**Files Reviewed:** `src/skills/roadmap-test-coverage/SKILL.md` (read in full), `.ai-factory/specs/trickster77777/82-test-cmd-derivation-rule.md`, plan, review-1
**Risk Level:** 🟢 Low — both prior findings fixed, no new issues.

## Verdicts on review-1 findings

### Finding 1 — `CLAUDE.md` read-list entry was unpinned prose → **Fixed**

Current content, `src/skills/roadmap-test-coverage/SKILL.md` L27–35:

```
Read in order (skip if absent):
- `.ai-factory/ARCHITECTURE.md` — module boundaries, folder structure
- `CLAUDE.md` at the same root as the `.ai-factory/` directory in play (not
  necessarily the ambient auto-loaded one) — the declared test command in its
  `## Commands` section
- The roadmap in play per `roadmap-engine`'s named-roadmap resolution order
  (explicit `$ARGUMENTS` wins, then "my roadmap", then the default
  `.ai-factory/ROADMAP.md`; see the engine's "Named roadmaps" section for the
  slug/owner mechanics) — all tasks
```

The entry now resolves the way its siblings do. Two things make this a real fix rather than a reword:

1. **It names a resolution anchor.** "at the same root as the `.ai-factory/` directory in play" co-resolves with the `ARCHITECTURE.md` read one bullet above, which is itself `.ai-factory/`-relative. The two Layer 1 file reads therefore land in the same repo by construction — the grove split that motivated the finding can no longer separate them.
2. **It closes the specific failure mode by name.** The parenthetical "(not necessarily the ambient auto-loaded one)" states the trap explicitly, so an agent that *has* a `CLAUDE.md` already in context is told not to use it on that basis. Review-1's scenario — a Python sub-repo declaring `| Tests | uv run pytest |` while the grove-root `CLAUDE.md` gets read instead, falling through to empty and skipping the gate on a project with a real suite — is no longer reachable by following the text.

The spec records the same requirement as a guard (§ Guards: "**Layer 1's read list gains `CLAUDE.md`.** The primary `$TEST_CMD` source must be an explicit Layer 1 read, not an assumed ambient auto-load…"), so the constraint survives for the next reader.

Residual, non-blocking and not a finding: the Primary/Fallback clauses at L54 and L58 still say "its `CLAUDE.md`" / "`CLAUDE.md`" without repeating the anchor. That is correct as written — the read list pins the file three lines above in the same layer, and repeating the qualifier at every mention would violate one-home-per-fact. The rule refers back to the file Layer 1 just read.

### Finding 2 — spec guard "exactly one added line" was narrower than the correct implementation → **Fixed**

Current content, `.ai-factory/specs/trickster77777/82-test-cmd-derivation-rule.md` § Guards:

```
- **Layer 8 takes exactly one added counts-block line plus the sentence
  governing when it prints** — the skipped-gate counter, in the counts block,
  and the one-line note that it prints only when Layer 7 skipped the gate
  (needed for correctness: without it the line would read as unconditional and
  print on every run, including ones where the suite executed and passed).
  Everything else in Layer 8 is byte-identical: …
```

The guard now covers what the implementation actually (and correctly) needed, and — better than the minimum — it carries the *reason* the second element exists, so a future reader cannot re-narrow it back into a contradiction with the visibility requirement. The skill text it authorizes is present and correct at L378–379: "The `Existing-test gate` line prints only when Layer 7 skipped the gate for an empty `$TEST_CMD`; omit it entirely when Layer 7 ran the suite."

## Full re-review — new issues

**None found.** What I checked this pass:

**Guard scope re-verified from the current diff.** `git diff HEAD -- src/skills/roadmap-test-coverage/SKILL.md` touches exactly five hunks: Layer 1's read list (+3), the `$TEST_CMD` paragraph (L52–68), Layer 7's guard (L289–295), the re-run gate (L353–355), and Layer 8's counts line plus its conditionality note (L373, L378–379). `$STACK`'s block (L40–50) is byte-identical to post-20.1 — re-read and compared, including the `[language, framework]` placeholder clause. Layers 2–6 produce no diff hunks. Layer 8's `$HANDOFF_LIST` print instruction (L381–382), both category headings (L387, L391), the per-item pointer paragraph, and `Next step:` are byte-identical.

**Control flow through Layer 7 is total.** Three exits, no gap: empty → skip everything and go to Layer 8 (L289–293); non-empty and green → L300; non-empty with failures → classify, patch Class A, hand off Class B, re-run gate (L353–355). The gate's added clause names the empty case as already-departed rather than leaving it implicit, so there is no path on which an empty `<$TEST_CMD>` reaches a shell — the original defect.

**`$TEST_CMD` resolution is exhaustive.** Primary / Fallback / Neither (L54–64) covers every input state, including `aif`'s documented "leave light if no scaffolding exists yet" case via "that section declares no test command". The empty state is declared *defined* and pointed at Layer 7, which is what lets the Layer 7 guard read as a contract rather than defensive coding.

**No downstream consumer of the skip.** Re-read Layers 2–6 in full: none reference `$TEST_CMD`, so skipping Layer 7's run cannot strand a later layer. Layer 8's other counters degrade correctly on a skip (`Existing tests patched: K` and `Class B items handed off: J` are both 0 — the skip path appends nothing).

**No cross-file invariant broken.** Grepped the repo outside `.ai-factory/` for `TEST_CMD` and `roadmap-test-coverage`: the only file containing `$TEST_CMD` or the Layer structure is the skill itself. `test-philosophy`, `roadmap-decompose-skeleton`, `CLAUDE.md`, and `docs/sakshi-harness/skill-cycle.md` reference the skill by name only (pipeline order and reverse-graph markers), none of which the rewritten text affects. `loads:` edges unchanged; `allowed-tools` correctly untouched — the primary rule adds only a `Read`, granted at L10.

**Register preserved.** The `$TEST_CMD` block mirrors the `$STACK` block's numbered Primary/Fallback shape and sentence voice; the Layer 7 and Layer 8 additions read as the same author. This was an explicit guard and it holds.

## Deferred observations

- Affects: phase 20 / `.ai-factory/specs/trickster77777/82-test-cmd-derivation-rule.md` — The spec's Change bullet 1 still describes the primary as "the `## Commands` table `aif` writes into `CLAUDE.md` (the `Tests` row…)", which overstates what `aif/SKILL.md` L37 mandates (no table, no `Tests` row). The skill text is correct — it rules against the section with the row named as a typical shape — so this is spec-description drift only, carried unchanged from plan-review-1 and review-1. Worth a small correction on a future spec pass.
- Affects: phase 20 / `src/skills/roadmap-test-coverage/SKILL.md` — Running the skill against this repo resolves `$TEST_CMD` to empty (neither grove `CLAUDE.md` has a `## Commands` section; no manifest at the `skills/` root), so Layer 7 skips the gate and Layer 8 prints the skip line. Correct behavior for a repo whose product is skill text with no suite, and it exercises the new path end to end. Not a defect.

Both review-1 findings are fixed and nothing new surfaced. The live Python-project run remains the user's out-of-pipeline check per the spec's verification note, and its absence here is expected, not a gap.

REVIEW_PASS
