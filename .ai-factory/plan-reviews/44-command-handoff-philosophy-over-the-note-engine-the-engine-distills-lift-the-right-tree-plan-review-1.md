## Code Review Summary

**Files Reviewed:** 1 plan (`44-command-handoff-philosophy-over-the-note-engine...md`) against 4 target/context files (`src/skills/note/SKILL.md`, `src/commands/command-handoff.md`, `src/skills/roadmap-engine/SKILL.md`, spec note `55-handoff-philosophy-over-note.md`)
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture (`.ai-factory/ARCHITECTURE.md`)** — PASS. The plan is a textbook application of the "Composition: mechanism vs policy" section: `note` stays the engine (mechanism — mining, distillation, numbering, placement), `command-handoff` becomes the philosophy (policy — the handoff lens/skeleton, proportionality, semantic slug, pointer). Control stays with the caller; the verbosity hook is generic engine content shared by ≥2 potential callers. No boundary violation. ARCHITECTURE already registers `src/commands/` as a hosted artifact type (line 22), so no doc edit is owed there.
- **Rules (`.ai-factory/RULES.md`)** — WARN (file absent). No project RULES.md exists; nothing to enforce. The relevant conventions live in CLAUDE.md and are honored (see below).
- **Roadmap (`.ai-factory/ROADMAP.md`)** — PASS. The plan's title matches the open milestone on line 99 verbatim, whose `Spec:` tag points at `.ai-factory/notes/55-handoff-philosophy-over-note.md` (confirmed present). The plan's three tasks map cleanly onto the spec's three edits (Task 1 = Edit 1 verbosity hook; Task 2 = Edit 3 map scoping; Task 3 = Edit 2 delegation + frontmatter). The `Depends on note 53` prerequisite from the spec is satisfied — note 53 (destination/template hooks) is `[x]` on line 95, and both hooks are present in the current `note/SKILL.md`.
- **CLAUDE.md conventions** — PASS. `loads: note` is declared in the depending file's own frontmatter (correct per "Dependencies and the skill graph"); no central map to update (correct — the declarations *are* the map). Task 1 includes the mandated reverse-graph grep before touching the engine.

### Critical Issues

None. The plan is implementation-ready. Codebase assumptions verified:
- **Reverse-graph claim is accurate.** `grep "loads:"` confirms `roadmap-engine` is the *only* skill with `loads: note`, and `roadmap-engine/SKILL.md` (lines 30–33) passes only the destination hook, no verbosity — so Task 1's "unaffected by construction" holds. (`command-pin-gaps` merely mentions the word "note" as a target genre; it does not load the engine.)
- **allowed-tools union is correct.** Current command: `Write Bash(ls *)`. `note`'s grants: `Read Write Bash(ls *) Bash(mkdir *) Glob`. Plan's union `Read Write Bash(ls *) Bash(mkdir *) Glob Skill` is the exact superset plus `Skill` — no partial copy.
- **File paths are correct.** `src/skills/note/SKILL.md` and `src/commands/command-handoff.md` both exist and are symlinked into `active/`.

### Non-blocking Observations (WARN)

1. **Slug pass-through trap (Task 3).** `note`'s Step 2 uses `$1` if provided, else derives semantically. When the command loads `note` via the Skill tool in note mode, the implementer must **not** forward `command-handoff`'s `$ARGUMENTS` (the trigger word `note`/`ноут`) into `note`'s `$1`, or the slug becomes the literal `note` — the exact failure the semantic-slug rule forbids. The plan's "slug = derived semantically … never the literal word `handoff`" covers the intent, but neither plan nor spec explicitly flags the arg-forwarding mechanics. Consider one sentence telling the implementer to invoke `note` with no positional arg so its semantic-slug derivation runs. Not a blocker — the semantic-slug instruction implies it.

2. **"slug" is described as a hook but isn't a formal `note` input.** `note` exposes three formal hooks (destination, template, verbosity after Task 1); slug is a `$1` arg / Step 2 derivation, not a hook. The plan lists "slug = derived semantically" among the hooks. This is harmless because `note`'s default behavior already derives a semantic slug — the command just relies on that default rather than a distinct hook. Purely descriptive; no code impact.

3. **Self-check gate folded into the free-text verbosity directive (Task 3).** The plan routes the proportionality policy *and* the self-check gate through the single free-text verbosity directive, "applied to the note-file content before the Write." `note` has no explicit pre-Write gate step, so this relies on the agent honoring the free-text directive during distillation. Acceptable given the directive is deliberately free-text policy — just noting the gate is advisory-by-prose, not a structural step in the engine.

4. **First command to carry a `loads:` field.** No existing command declares `loads:` (only skills do). This is consistent with the convention ("every skill that loads another declares it") extended to commands, and the runtime mechanism is the `Skill` tool (now in allowed-tools), not the frontmatter field. Fine — just the first of its kind, so nothing else keys off it.

### Positive Notes

- The plan preserves every "do not shrink / do not restate" constraint from the spec: it explicitly forbids shrinking the error log and working-discipline sections, keeps skeleton/proportionality/self-check/semantic-slug/pointer text living once in the command, and rejects the pre-filled-template anti-pattern by name — matching the spec's "What NOT to do" list.
- Task 1's instruction to keep the verbosity-hook phrasing generic ("no mention of `command-handoff` or handoffs; standalone `/note` with no hooks stays behavior-identical") correctly protects the engine's caller-agnostic contract and the lazy-migration guarantee.
- Dependency ordering (Task 3 after Task 1) is genuinely required — the verbosity hook must exist before note mode can reference it. Task 3-after-Task 2 is a conservative same-file sequencing choice (both edit `command-handoff.md`); harmless.
- Settings (testing: no, logging: minimal, docs: no) are appropriate for a prompt-only skill/command reshaping with no runtime code surface.

PLAN_REVIEW_PASS
