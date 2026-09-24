# Plan: 57.2 — the philosophy unit is built in test-philosophy's shape

## Context
Create `src/skills/polymorphism-philosophy/` — one SKILL.md holding the phase-57 unit (question, two entries, trigger, exemption, vocabulary), built in `test-philosophy`'s shape — symlink it into the active working set, and name it in CLAUDE.md's two exhaustive skill rosters so neither goes stale.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## The input contract, decided
The unit is user-invocable and its space entry needs a region, so what carries that region has to be settled before the frontmatter block reads as final. It is settled, and it is not settled by the precedent merely carrying no `argument-hint`:

**The region arrives in the invoking conversation, not as `$ARGUMENTS`.** The ground is the user's own standing ruling, quoted in phase note 151 — he invokes the philosophy and names the region and what raises his suspicion in the same message ("укажу область в коде и скажу что вызывает у меня подозрения"), and the note calls this "the same arrangement `test-philosophy` already has". The ruling is drawn from invoking `test-philosophy` exactly this way; it describes a conversational input, not a parsed argument. So the spec's pinned frontmatter block stands unchanged, and it stands on the ruling rather than on precedent-by-shape.

Two consequences follow, and neither reopens the block:
- **No `argument-hint`.** CLAUDE.md § "SKILL.md frontmatter (required fields)" lists the field, and the repository's practice does not settle its absence either way: of the 17 skills in `src/skills/` carrying the hint, only 6 contain the token `ARGUMENTS` at all — the other 11 take a named target and refer to it in prose, and `test-philosophy` and the unsymlinked `ui-ux-pro-max` carry no hint. Read as *does an invocation expect a named target*, that practice would put this unit on the carrier side. What decides it is narrower and checkable: **nothing in the spec's pinned body interpolates `$ARGUMENTS`.** A region typed after the slash command and a region named in the next sentence reach the agent's context identically, so here the field is a UI hint and nothing else — its absence breaks no path, and adding it would mean deviating from a pinned block to change a hint.
- **`allowed-tools: Read` stands.** The body's own claim is that the skill "has no I/O of its own": walking a named region belongs to the invoking session or to the calling skill, which hold their own tools, not to this unit. It is not a tool set that has to enumerate a directory.

If a live direct invocation ever shows the space entry actually blocked from reaching a named region, that is a defect against the task spec's pinned block and routes back there — the implementer does not patch the frontmatter in passing.

## Tasks

### The unit

- [x] **Create the skill directory and its SKILL.md**
  Files: `src/skills/polymorphism-philosophy/SKILL.md`
  Write the file with the body the task spec pins in full (`.ai-factory/specs/trickster77777/157-the-philosophy-unit-is-built-in-test-philosophys-shape.md` § "The change") — copy that fenced block verbatim, it is the deliverable, not a sketch to re-derive. Its content (question, two entries, trigger, exemption, vocabulary) is settled in the phase note and is not re-derived, extended, or trimmed here; in particular do not add a single-responsibility clause — the note rules it out for a structural reason.
  Confirmed ground truth to hold to:
  - Frontmatter mirrors `src/skills/test-philosophy/SKILL.md` exactly in shape: `name`, `description` (`>-` folded), `user-invocable: true`, `disable-model-invocation: false`, `allowed-tools: Read`. No `argument-hint` and no `loads:` — per § "The input contract, decided" above; the unit parses no argument and loads nothing.
  - `name: polymorphism-philosophy` must match the directory name byte-for-byte; both are machine-resolved identifiers (CLAUDE.md § "Key constraints").
  - The body keeps the load-once engine sentence and the reverse-graph grep line in `test-philosophy`'s own form, per CLAUDE.md § "Dependencies and the skill graph". The body names `roadmap-decompose-skeleton` as the calling skill before that `loads:` edge exists — task 57.3 adds the edge; this is the spec's pinned wording, leave it.
  - Body well under the 500-line limit; no `references/`, `scripts/`, or `templates/` subdirectories — the precedent is a single-file skill.
  Verify (spec's first blast-radius invariant, half one): `ls src/skills/ active/skills/ 2>/dev/null | grep -i "polymorphism-philosophy"` returned nothing before this task and must return the real directory after it.

### The working set

- [x] **Symlink the skill into `active/skills/`** (depends on Create the skill directory and its SKILL.md)
  Files: `active/skills/polymorphism-philosophy`
  Run `ln -sfn ../../src/skills/polymorphism-philosophy active/skills/polymorphism-philosophy` — a relative `../../src/skills/<name>` target, matching every existing our-skill symlink in that directory (`test-philosophy`, `roadmap-engine`, and the rest, confirmed by `ls -la active/skills/`). Do not copy the directory; `active/` holds per-item symlinks only.
  Verify, both halves — the name sweep alone is not enough here:
  - Name: the sweep above now returns exactly two entries, and no third, colliding entry.
  - Resolution: `head -1 active/skills/polymorphism-philosophy/SKILL.md` prints `---`. This is the check that catches the failure the sweep cannot see — a wrong relative depth (`../src/skills/…`) or a typo in the target leaves a dangling link whose *name* still prints in `ls`, so the sweep reads satisfied while `~/.claude/skills` gains an entry Claude Code silently never loads. The spec's rule that "the symlink target must resolve" is only answered by dereferencing it.

### The rosters

- [x] **Name the skill in CLAUDE.md's two exhaustive rosters** (depends on Symlink the skill into `active/skills/`)
  Files: `CLAUDE.md`
  Both rosters assert completeness (neither carries an ellipsis), so both go stale the moment the skill exists unnamed in them. Insert `polymorphism-philosophy` immediately after `test-philosophy` in each — the sibling it is built beside:
  - **"The active set"** paragraph: `…aif-docs`, `test-philosophy`, `polymorphism-philosophy`, `roadmap-outline`…`
  - **"Everything else in `src/skills/` is ours"** paragraph: `…note`, `test-philosophy`, `polymorphism-philosophy`, `observe-logs`…`
  Change no other word in either paragraph. The "Repository Structure" tree is explicitly out of scope — its skill sample ends in `└── …` and makes no completeness claim (confirmed in the file); leave it byte-identical, and likewise the § "Dependencies and the skill graph" engine example, which names `test-philosophy` illustratively rather than as a roster.
  `AGENTS.md` is a symlink to `CLAUDE.md`, so this one edit serves both entry points — do not edit it separately.
  Verify (spec's second blast-radius invariant): `grep -c "polymorphism-philosophy" CLAUDE.md` returns `2`, one occurrence in each roster and nowhere else in the file.
