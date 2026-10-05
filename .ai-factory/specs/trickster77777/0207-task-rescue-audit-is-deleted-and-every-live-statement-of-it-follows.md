# 74.1 — task-rescue-audit is deleted and every live statement of it follows

## What is true now

`src/skills/task-rescue-audit/` holds the skill, and `active/skills/task-rescue-audit` is a symlink to it, so its description loads in every session. The user has not invoked it for months. What it gave, an outside view of a task that looped, is now carried by the rescue report's own round-by-round narrative, by peer architects holding memory across repositories, and by names in the architecture maps.

Live text names the skill in these places; each is wrapped in its file at a fixed column where noted.

`src/skills/task-rescue/SKILL.md`, in Step 3 under "**Write the Diagnosis Report**", closes the paragraph on the narrative form: "…into the narrative as quotes or paraphrases, as evidence. This narrative register is shared with `task-rescue-audit`'s output — change it in both files or neither." The text is wrapped, and the two sentences after "evidence." are the ones that name it.

`docs/sakshi-harness/skill-cycle.md` (Russian) has the heading "## Когда task не сходится — `task-rescue`, `task-rescue-audit`"; the paragraph under it, whose first two sentences concern `task-rescue` and whose rest begins "`task-rescue-audit` — взгляд снаружи на любую зациклившуюся или аномально долгую task" and ends "Он только оценивает и рассказывает — ни во что не пишет."; and in the scheme the line "          │   task-rescue-audit          ← взгляд снаружи на зациклившуюся task".

This repository's `CLAUDE.md` (`AGENTS.md` is a symlink to it) names it in four places: the "Skill cycle" row of the guides table, "→ orchestrator → `task-rescue`/`-audit` → `roadmap-test-coverage`"; the repository tree comment "│   │   ├── task-rescue/          #     … and task-rescue-audit, detangle,"; the active-set list "our skills — `detangle`, `task-rescue`, `task-rescue-audit`, `roadmap-decompose`, …"; and the list that opens "**Everything else in `src/skills/` is ours**": "`detangle`, `task-rescue`, `task-rescue-audit`, `roadmap-outline`, …".

## What must be true after

`src/skills/task-rescue-audit/` does not exist, and neither does the symlink `active/skills/task-rescue-audit`.

In `src/skills/task-rescue/SKILL.md` the paragraph ends at "…as quotes or paraphrases, as evidence." and the two sentences that followed are gone; the register is the report's own, and nothing states it is shared.

In `docs/sakshi-harness/skill-cycle.md` the heading reads "## Когда task не сходится — `task-rescue`", and the paragraph under it reads in full: "Остановка на лимите итераций оставляет артефакты на диске. `task-rescue` диагностирует глубину корня (task-spec? план? код?), чинит на эту глубину и откатывает sidecar с артефактами в отремонтированное состояние." The scheme line naming `task-rescue-audit` is deleted, and the line "          │   task-rescue                ← task не сходится (чинит по глубине)" stays as it is.

In `CLAUDE.md`: the row reads "→ orchestrator → `task-rescue` → `roadmap-test-coverage`"; the tree comment reads "│   │   ├── task-rescue/          #     … and detangle,"; the active-set list reads "our skills — `detangle`, `task-rescue`, `roadmap-decompose`, …" and the other list reads "`detangle`, `task-rescue`, `roadmap-outline`, …", each without the name and with the rest of its list unchanged.

## What breaks on contact

**Rule:** a text breaks on this change if it names the skill, its slash command or its `-audit` shorthand, or states the role it had, an outside assessment of a task that converged by understanding or by attrition.

**Sweep:**
```
grep -rnE "rescue-audit|`-audit`|/-audit" . --exclude-dir=.git --exclude-dir=.venv --exclude-dir=node_modules --exclude-dir=upstream --exclude-dir=.ai-factory
grep -rn -i "convergence by\|attrition\|band-aid\|outside-view\|outside view\|взгляд снаружи" . --exclude-dir=.git --exclude-dir=.venv --exclude-dir=upstream --exclude-dir=.ai-factory
```
run from the family root, both repositories.

**Finding.** The first search reaches the skill's own file, every place listed above, and one more, in the orchestrator, recorded below. The second reaches the skill-cycle paragraph and scheme line already listed, the orchestrator sentence recorded below, and two texts that stay: `docs/self-analysis.md`, whose "outside view" is its own subject and not this skill, and `docs/reserved-words.md`, whose entry "**prune · rescue · audit**" registers audit as "an outside-view look at a task that looped". That file declares itself final and not subject to update, so this task leaves it; the registry keeps a name for a skill that is gone until the user rules on the entry. `src/skills/orchestrator-artifacts/SKILL.md` lists `[audit-corroborated]` and `[audit-dismissed]` among its legacy markers; they are protocol tokens still read as pinned in old repositories, not mentions of the skill, and stay byte-identical. The orchestrator's `docs/concepts/non-convergence.md` names the skill in a sentence that is that repository's own to change, and this task does not edit it: "Diagnosis and repair are carried out by chat skills over the remaining artifacts: `/task-rescue` diagnoses how deep the root cause runs (spec / plan / code), repairs to that depth, and rolls the sidecar and artifacts back to the repaired state; `/task-rescue-audit` gives an outside assessment — whether the task converged through genuine understanding or through attrition around an unnamed structural gap." The orchestrator's head removes the clause on `/task-rescue-audit` in its own repository. The `.ai-factory/` history of both repositories, handoffs, closed specs, plans, reviews and rescue reports, names the skill as a record of its time and is not edited.
