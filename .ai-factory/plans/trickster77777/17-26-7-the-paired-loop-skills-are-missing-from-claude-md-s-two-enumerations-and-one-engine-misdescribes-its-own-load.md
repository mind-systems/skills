# Plan: 26.7 — the paired-loop skills are missing from CLAUDE.md's two enumerations, and one engine misdescribes its own load

## Context
Three descriptions in this repo have drifted from what the tree actually holds: `CLAUDE.md`'s active-set list omits `architect-editor-engine`, its ownership list ("everything else in `src/skills/` is ours") omits both paired-loop engines, and `architect-editor-engine/SKILL.md` attributes the architect's load to its own `loads:` frontmatter edge rather than to the instruction in the architect's body. This task corrects all three, nothing else.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### CLAUDE.md enumerations

- [x] **Add `architect-editor-engine` to the active-set list**
  Files: `CLAUDE.md`
  Line 74 (the paragraph opening `**The active set** (what \`~/.claude\` actually loads): our skills — …`) currently ends its list of ours with `` `orchestrator-artifacts`, `agent-architect`, `architect-pairing-engine` — plus one upstream original we use as-is: `aif-skill-generator`. ``. Insert `` `architect-editor-engine`, `` immediately before `` `architect-pairing-engine` ``, matching the existing comma-plus-backtick punctuation of the list. Ground truth for the addition: `ls active/skills/` holds symlinks for all three paired-loop skills (`agent-architect`, `architect-editor-engine`, `architect-pairing-engine`). Everything else on the line — the leading prose, the `— plus one upstream original …` clause, the "Everything else … stored but **not** symlinked" sentence, and the final "Adding a skill to the working set …" sentence — stays byte-identical.

- [x] **Add both engines to the ownership list** (depends on the previous task — same file, adjacent concern; do them in one pass)
  Files: `CLAUDE.md`
  Line 189 (the paragraph opening `**Everything else in \`src/skills/\` is ours** — no upstream counterpart to reconcile, sync never touches it: …`) currently ends its list with `` `observe-logs`, `ui-ux-pro-max`, `agent-architect`. ``. Append `` `architect-editor-engine`, `architect-pairing-engine` `` after `` `agent-architect` ``, keeping the list's comma separation and the sentence-final period. The trailing sentence "The same holds for `src/agents/` — the `editor` agent definition has no upstream counterpart; a re-sync must never overwrite it." stays exactly as it is. The two lists remain two separate lists answering two different questions (what is loaded vs. what is ours) — do not merge them, cross-reference them, or reduce one to a pointer at the other.

### Engine self-description

- [x] **Correct the load clause in `architect-editor-engine`**
  Files: `src/skills/architect-editor-engine/SKILL.md`
  Line 17 currently reads: "Load this skill once at birth — the architect via its own `loads:` frontmatter edge, the editor as the first action on spawn — so the contract is resident before any channel-message arrives. This is a load-once engine; its callers depend on its exact behavior, and the reverse graph resolves via `` grep -l "architect-editor-engine" src/skills/*/SKILL.md src/commands/*.md src/agents/*.md ``." Replace only the clause "the architect via its own `loads:` frontmatter edge" so it attributes the architect's load to the instruction in the architect's own body — the ground truth is `src/skills/agent-architect/SKILL.md:42-44`, which tells the architect to load this engine via the `Skill` tool before the first channel-message. `loads:` declares the forward graph; per this repo's own rule (CLAUDE.md § "Dependencies and the skill graph") the declarations *are* the map — a declaration, not a loading mechanism. The replacement clause names no caller: the reverse-graph `grep -l` command later in the same sentence is how a reader finds callers, and it stays byte-identical. Keep the sentence's em-dash structure, the "the editor as the first action on spawn" clause, and the "so the contract is resident before any channel-message arrives" tail. No frontmatter change: the `description:` field already names both callers and is outside this task's scope; no `loads:` edge is added, removed, or reordered anywhere.

### Verification

- [x] **Verify the three edits and the untouched surface** (depends on all three edits)
  Files: `CLAUDE.md`, `src/skills/architect-editor-engine/SKILL.md`
  Run, from the repo root:
  - `git diff CLAUDE.md` → exactly two changed lines (74 and 189), each differing only by the added skill names.
  - `grep -n "architect-editor-engine" CLAUDE.md` → hits on 74 and 189; `grep -n "architect-pairing-engine" CLAUDE.md` → hits on 74 and 189.
  - `git diff src/skills/architect-editor-engine/SKILL.md` → exactly one changed line (17), with the reverse-graph `grep -l` command inside it unchanged and no frontmatter line touched.
  - `sed -n '14,$p' src/skills/architect-editor-engine/SKILL.md | grep -c "agent-architect"` → `0` (the body still names no caller; the scope deliberately starts past the frontmatter, since `description:` names both callers and is untouched).
  - `git status` → no other file modified: `src/skills/agent-architect/SKILL.md`, `src/skills/architect-pairing-engine/SKILL.md`, `src/agents/editor.md`, and `active/skills/` are all untouched.
