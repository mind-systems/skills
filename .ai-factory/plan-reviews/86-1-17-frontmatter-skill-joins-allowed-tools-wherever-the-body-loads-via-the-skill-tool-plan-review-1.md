## Plan Review Summary

**Plan:** 1.17 — frontmatter: `Skill` joins `allowed-tools` wherever the body loads via the Skill tool
**Files Reviewed:** plan + governing spec (`.ai-factory/specs/42-skill-tool-grant-alignment.md`) + ROADMAP line 191 + all `loads:` declarers and their `allowed-tools` lines
**Risk Level:** 🟢 Low

### Context Gates

- **Roadmap (WARN→OK):** Plan `# Plan:` heading resolves to ROADMAP line 191 (`1.17`), which names `Spec: .ai-factory/specs/42-skill-tool-grant-alignment.md`. Spec read; plan is faithful to it — grep-driven inventory, plain unscoped `Skill`, frontmatter-only, byte-identical bodies, `after 1.8.3` ordering, never-touch-upstream. No linkage gap.
- **Ordering guard (OK):** Spec/plan require running after 1.8.3 to avoid a same-file collision with prune's pyramid pass. ROADMAP line 171 shows `1.8.3` is `[x]` and `roadmap-prune`'s `allowed-tools` is currently stable at `Read Write Edit Bash(git *) Bash(rm *) Glob Grep` — the collision window is closed. Satisfied.
- **Architecture/Rules:** `.ai-factory/ARCHITECTURE.md` "Dependencies and the skill graph" convention holds — the plan reads `loads:` as a *declaration* only and correctly treats the Skill tool as the sole runtime injection mechanism, matching the spec's framing and CLAUDE.md.

### Critical Issues

None. Independent verification against the live tree confirms every factual claim:

- **Inventory exact.** The four current `allowed-tools` lines match the plan's table byte-for-byte:
  - `roadmap-prune`: `Read Write Edit Bash(git *) Bash(rm *) Glob Grep` (no `Skill`) ✓
  - `milestone-rescue`: `Read Write Edit Glob Grep Bash(git *) AskUserQuestion` (no `Skill`) ✓
  - `milestone-rescue-audit`: `Read Glob Grep Bash(git *)` (no `Skill`) ✓
  - `roadmap-engine`: `Read` (no `Skill`) ✓
- **Expected results exact.** Each Task 2 target is the current line + a single trailing ` Skill`. Verified against actual content.
- **"Already carry `Skill`" set accurate.** `roadmap-outline`, `roadmap-decompose`, `roadmap-decompose-skeleton`, `roadmap-test-coverage`, `command-handoff` all already list `Skill` — no edit needed. Confirmed.
- **Gaps are genuine (not false positives).** `roadmap-engine:34` loads `note` "via the Skill\ntool" (line-wrapped prose); `roadmap-prune:20` loads `orchestrator-artifacts` via the Skill tool. Both bodies truly invoke the tool.
- **Audit method is complete.** Starting from `loads:` declarers is the safe superset: a multiline sweep for `the Skill\s+tool` surfaces exactly `{roadmap-prune, milestone-rescue-audit, milestone-rescue, roadmap-engine, roadmap-decompose, roadmap-outline}` + `editor.md` — no file outside the plan's reasoning. The three `loads:` declarers whose bodies don't literally say "the Skill tool" (`roadmap-decompose-skeleton`, `roadmap-test-coverage`, `command-handoff`) already carry the grant, so they need no edit regardless.
- **Out-of-scope exclusion correct.** `src/agents/editor.md` uses agent `tools:` syntax (`Read, Grep, Glob, Bash, Write, Edit, Skill`) and already grants `Skill`; it is neither `src/skills/*` nor `src/commands/*`. Correctly excluded.

### Positive Notes

- Task 1 rightly refuses to trust the static table ("files are in flux") and re-derives the gap set from `loads:` + prose grep + a multiline sweep for the wrapped form — the one real trap here (roadmap-engine's `via the Skill\ntool` line break) is explicitly anticipated.
- Guards are tight and testable: exactly one edited line per file, `name`/`description`/`argument-hint`/`loads:` untouched, `git diff` must show four lines in four files. Task 3's pairing invariant ("zero files with the instruction and without the grant") is the correct closure check.
- Plain unscoped `Skill` (not `Skill(<name>)`) is the right call — scoped frontmatter syntax is unverified.

## Deferred observations

- Affects: `roadmap-engine` frontmatter (a separate grant class, outside this milestone's Skill-only scope) — `roadmap-engine`'s body instructs writing files (e.g. `:181` "Then write `$TARGET_FILE`", plus the spec-note write it drives through `note`), yet its `allowed-tools` is `Read` and this plan leaves it at `Read Skill`. The milestone-41 creation line specified `Read Write Edit Glob Grep Skill`, so the current `Read` is a later reduction whose intent is unclear — it may be deliberate (the engine is `user-invocable: false` and normally loaded into a caller's context, where the caller's grants perform the writes), or it may be a stray body-vs-grant gap of the *same class* as this milestone but a *different tool*. This plan neither creates nor worsens it, and fixing it would exceed the explicit "append `Skill` only" scope, so it is not a finding here — flagging it for whoever next audits `roadmap-engine`'s frontmatter to confirm the `Read`-only grant is intentional for model-direct invocation. [routed → .ai-factory/specs/54-engine-grants-restored.md]

PLAN_REVIEW_PASS
