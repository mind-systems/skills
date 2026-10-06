# Plan: 74.1 — task-rescue-audit is deleted and every live statement of it follows

## Context
Retire the `task-rescue-audit` skill: delete its source directory and its `active/` symlink, and edit every live text in this repository that names it so that each one matches the after-text pinned in the task spec `.ai-factory/specs/trickster77777/0207-task-rescue-audit-is-deleted-and-every-live-statement-of-it-follows.md` (§ "What must be true after"). Edit only the files listed below. The spec's § "What breaks on contact" lists what stays as it is: `docs/reserved-words.md` (declared final), `docs/self-analysis.md`, the `[audit-corroborated]`/`[audit-dismissed]` legacy markers in `src/skills/orchestrator-artifacts/SKILL.md`, the orchestrator repository (its own head changes `docs/concepts/non-convergence.md`), and all `.ai-factory/` history. None of these is touched.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Remove the skill

- [x] **Delete the skill directory and its active symlink**
  Files: `src/skills/task-rescue-audit/` (contains only `SKILL.md`), `active/skills/task-rescue-audit` (symlink → `../../src/skills/task-rescue-audit`)
  Run `git rm -r src/skills/task-rescue-audit` and `git rm active/skills/task-rescue-audit`, or delete them with `rm`. Do not commit. Afterwards neither path exists. Delete only the symlink at `active/skills/task-rescue-audit`, never its target through the link. `~/.claude/skills` resolves through `active/skills`, so the skill drops out of the global scope automatically, and no other step is needed.

### Live text drops the name

- [x] **task-rescue Step 3: delete the shared-register sentence pair**
  Files: `src/skills/task-rescue/SKILL.md`
  In Step 3, under "**Write the Diagnosis Report**", the paragraph that begins "Form: a chronological narrative in plain prose." currently ends with the wrapped text:
  ```
  findings from the recurring rounds (2+) into the narrative as quotes or paraphrases, as
  evidence. This narrative register is shared with `task-rescue-audit`'s output —
  change it in both files or neither.
  ```
  Delete the two sentences after "evidence.", from "This narrative register is shared…" through "…change it in both files or neither.". The paragraph must end at "…as quotes or paraphrases, as evidence.", so the line becomes just `evidence.` and the line `change it in both files or neither.` goes completely. Leave the blank line and the following paragraph ("No tables, no fragment-style bullet lists…") exactly as they are. Make no other change to the file.

- [x] **skill-cycle.md: heading, paragraph, and scheme line**
  Files: `docs/sakshi-harness/skill-cycle.md` (Russian; keep it Russian)
  1. Heading: `## Когда task не сходится — \`task-rescue\`, \`task-rescue-audit\`` → `## Когда task не сходится — \`task-rescue\``.
  2. Replace the paragraph under that heading with exactly this, verbatim from the spec:
     `Остановка на лимите итераций оставляет артефакты на диске. \`task-rescue\` диагностирует глубину корня (task-spec? план? код?), чинит на эту глубину и откатывает sidecar с артефактами в отремонтированное состояние.`
     That is, delete everything from "`task-rescue-audit` — взгляд снаружи…" through "…ни во что не пишет.".
  3. In the scheme code block, delete the whole line `          │   task-rescue-audit          ← взгляд снаружи на зациклившуюся task`. The line above it, `          │   task-rescue                ← task не сходится (чинит по глубине)`, stays byte-identical, and so does the `          ▼` line below it.

- [x] **CLAUDE.md: four places drop the name**
  Files: `CLAUDE.md` (`AGENTS.md` is a symlink to it and must not be edited separately)
  1. The "Skill cycle" row of the Guides table: `→ orchestrator → \`task-rescue\`/\`-audit\` → \`roadmap-test-coverage\`` → `→ orchestrator → \`task-rescue\` → \`roadmap-test-coverage\``. The rest of the row is unchanged.
  2. The Repository Structure tree comment: `│   │   ├── task-rescue/          #     … and task-rescue-audit, detangle,` → `│   │   ├── task-rescue/          #     … and detangle,`. Keep the column of `#` unchanged, and leave the next line (`│   │   └── …                     #     temporal-tree, …`) as it is.
  3. The active-set list ("**The active set** … our skills — …"): remove `` `task-rescue-audit`, `` so it reads "our skills — `detangle`, `task-rescue`, `roadmap-decompose`, …". The rest of the list and the sentence are unchanged.
  4. The list opening "**Everything else in `src/skills/` is ours**": remove `` `task-rescue-audit`, `` so it reads "`detangle`, `task-rescue`, `roadmap-outline`, …". The rest is unchanged.

### Confirm the sweep

- [x] **Re-run the spec's sweep** (depends on all tasks above)
  Files: none (read-only check)
  From the family root `/Users/max/projects/sakshi`, run the first sweep command from the spec:
  `grep -rnE 'rescue-audit|`-audit`|/-audit' . --exclude-dir=.git --exclude-dir=.venv --exclude-dir=node_modules --exclude-dir=upstream --exclude-dir=.ai-factory`
  It must find nothing in `skills/`. A hit in `orchestrator/` belongs to that repository and stays. Then run the second sweep (`convergence by|attrition|band-aid|outside-view|outside view|взгляд снаружи`). Its only remaining hits in `skills/` must be `docs/reserved-words.md` (the "**prune · rescue · audit**" entry) and `docs/self-analysis.md`, and both stay unedited by spec. Check that `ls active/skills/` no longer lists `task-rescue-audit` and that no dangling symlink is left behind.
