# Plan: 80.4 — § 5.6 states one moment for a pin

## Context
In `src/skills/task-rescue/SKILL.md`, § "Step 5.6 — Pin disposed observations" gives two moments for one pin. Its opening sentence pins each disposed entry "at the moment it disposes of it". The last sentence of its second paragraph says the pin is written when the repair is applied, on the user's word, and not at the moment of a judgment made before it. Since 80.3 the rescue makes its judgment in Step 3, then pauses for the user's word, so these two moments are different. This task makes § 5.6 state one moment, the second paragraph's. The opening sentence carries it, and the second paragraph's last sentence goes.

The task spec `.ai-factory/specs/trickster77777/0256-section-5-6-states-one-moment-for-a-pin.md` is authoritative. The phase's governing spec is `docs/names-and-reasons-not-laws.md`.

Assumptions:
- The spec does not pin the after-text word for word. The draft below keeps the skill's register and the file's hard wrap of about 86 columns.
- The spec's sweep (`grep -n -i "moment" src/skills/task-rescue/SKILL.md`) also returns a phrase in § "Step 5.7 — Write the durable report" about the moment of the report's first write. It also finds the resolution session's "at the moment it disposes of an observation" in `orchestrator-artifacts` § "6. Status-marker grammar". The spec leaves both as they are, so this plan does not touch them.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Edit `src/skills/task-rescue/SKILL.md`

- [x] **§ 5.6 opening carries the moment of the repair, and the repeat goes**
  Files: `src/skills/task-rescue/SKILL.md`
  In § "Step 5.6 — Pin disposed observations":
  1. Rewrite the opening paragraph's first sentence so the pin's moment is the moment the repair is applied, on the user's word, and not the moment of a judgment made before it. Keep "together with every sibling occurrence across that task's review files". Keep the second sentence unchanged: the pointer to `orchestrator-artifacts` § "6. Status-marker grammar", "by that pointer, never redefined here". Draft:
     > A rescue pins each deferred-observation entry it disposes of this session, together
     > with every sibling occurrence across that task's review files, when the repair is
     > applied, on the user's word, and not at the moment of a judgment made before it. The
     > pin follows the grammar and dedup rule of `orchestrator-artifacts`
     > § "6. Status-marker grammar" — by that pointer, never redefined here.
  2. In the second paragraph, delete only the last sentence, "A pin is written when the repair is applied, on the user's word, and not at the moment of a judgment made before it." Keep the rest of the paragraph word for word: the scope to review files still present on disk at pin time, the note that Step 5 may already have deleted the slug's review files, and the `roadmap-prune` gate clause. Re-wrap the paragraph's last line if needed.
  3. Leave the closing paragraph ("Rescue disposes only of what it evaluates this session …") unchanged. Nothing outside § 5.6 changes.
  4. Verify with `grep -n -i "moment" src/skills/task-rescue/SKILL.md`. It must return exactly two lines: the one § 5.6 line that names the judgment's moment as the moment the pin is not written, and the § 5.7 line about the report's first write. Run `grep -n "on the user's word" src/skills/task-rescue/SKILL.md` and check that § 5.6 contains it exactly once.
