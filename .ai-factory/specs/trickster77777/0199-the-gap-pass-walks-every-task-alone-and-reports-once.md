# 43.1 — the gap pass has one mode: every task walked alone, one report at the end

## What is true now

`src/commands/command-pin-gaps.md` fixes the unit of its walk in one task and leaves its targeting and its report open to many, and it keeps two modes. The text of each paragraph is one line of the file.

The frontmatter reads: "description: >- Scan a plan, task, phase, or task spec for where the implementing agent would have to guess: read the task, its task spec, and the code it lands in, walking the task's transformation into the code along named references to the leaf, then reason the way the orchestrator would plan and review it. Reports three finding classes: value holes (an unpinned value from the code), meaning holes (an undefined edge, or a constraint no document states, routed to its owner), and blast-radius holes (what the change breaks elsewhere in the repository). Closes what it can in place. Pass "scan" to only list findings without editing." and `argument-hint: "[path | scan]"`.

The targeting paragraph reads: "Target, in priority order: the file(s) in `$ARGUMENTS`, if given — else the scope under discussion in chat (a named task, phase, or task spec) — else all open `- [ ]` tasks of the roadmap in play per `roadmap-engine`'s named-roadmap resolution order (explicit argument → "my roadmap" → default `.ai-factory/ROADMAP.md`; see the engine's "Named roadmaps" section for the slug/owner mechanics) above `---STOP---`, scanning each contract line and its `Spec:`-tagged task spec."

The paragraph on the two ends of a hole says: "The two ends are not classes: every finding carries exactly one of three, and the end shows only in how it closes — in place, or `owner: <skill>` in the scan line's `fix` token." The paragraph on what the pass names and performs ends: "A hole it can close in place it closes, exactly as today; a hole whose repair belongs elsewhere is reported, in both modes." The two closing paragraphs read: "**scan mode** (`$ARGUMENTS` contains `scan`/`report`/`только скан`): list findings as `[file:line|spec-location] → value|meaning|blast-radius → what's missing → fix`, where `fix` reads `owner: <skill>` for a hole whose repair belongs elsewhere, and stop." and "**default:** edit the file in place — replace each vague spot with the concrete value, spec clause, or rule-sweep-invariant — then report `N closed from source · M blocking · K owned elsewhere`."

The command's questions speak of one task: "The unit of the walk is one behavior the task claims", and "would the run, holding this task and nothing else, have to invent". Nothing says what the walk does when the target names many tasks, whether the pass stops between them, or where the blockers of several tasks are gathered. The user ruled it: the pass always works with one task, he asks for each open task one at a time, without stopping, with the report and the blockers at the end, and "Режим один — проходим тот диапазон, который я указал. Других нет."

## What must be true after

The command has one mode and no mode label. The frontmatter reads: "description: >- Scan a task, a phase, or a task spec for where the implementing agent would have to guess: read the task, its task spec, and the code it lands in, walking the task's transformation into the code along named references to the leaf, then reason the way the orchestrator would plan and review it. Reports three finding classes: value holes (an unpinned value from the code), meaning holes (an undefined edge, or a constraint no document states, routed to its owner), and blast-radius holes (what the change breaks elsewhere in the repository). Closes what it can in place." and `argument-hint: "[path]"`.

The targeting paragraph ends: "…above `---STOP---`. Each task the target names is walked alone, in roadmap order: the command reads that task's contract line and its `Spec:`-tagged task spec, holds that task and nothing else, finishes that task's findings before the next is opened, and does not stop between tasks."

The sentence on the two ends reads: "The two ends are not classes: every finding carries exactly one of three, and the end shows only in how it closes — in place, or `owner: <skill>` in the report." The closing sentence of the paragraph on what the pass names and performs reads: "A hole it can close in place it closes, exactly as today; a hole whose repair belongs elsewhere is reported."

The two closing paragraphs are replaced by one: "For each task in turn the command edits its file in place — replacing each vague spot with the concrete value, spec clause, or rule-sweep-invariant — and moves on to the next task. One report comes at the end, `N closed from source · M blocking · K owned elsewhere`, with the blockers of every task gathered under it, each naming its task, and each hole owned elsewhere naming its owner as `owner: <skill>`."

## What breaks on contact

**Rule:** a text breaks on this change if it names the scan mode, its trigger words or the list format, if it reads the report line, if it describes what the pass does with a target that names many tasks, or if it invokes the command.

**Sweep:**
```
grep -rn "spec-location" src/ docs/ CLAUDE.md
grep -rn -i "scan mode\|только скан" src/ docs/ CLAUDE.md
grep -rn "\"scan\"\|`scan`" src/ docs/ CLAUDE.md
grep -rn "closed from source" src/ docs/ CLAUDE.md
grep -rn "pin-gaps" src/
```

**Finding.** The scan mode, its trigger words and the list format are named only inside the command: in the frontmatter description and argument hint, in the sentence on the two ends ("the scan line's `fix` token"), in "in both modes", and in the scan paragraph itself, and each is repinned above. No other skill, command, doc or `CLAUDE.md` names the mode, the words `scan`, `report` or `только скан` as triggers, or the `[file:line|spec-location] → …` list, so nothing outside the command changes when they go. Closed task specs and notes record the list format as chat output, and are records. The report line appears only in the command's own text; the report keeps the same three counts, once at the end, and now carries the owner of each hole that belongs elsewhere, which the scan line used to carry, so no information the mode held is lost. `docs/sakshi-harness/skill-cycle.md` § "Пины — `command-pin-gaps`" describes the pass in the singular, "Команда читает таск, его task-spec и код", states the deciding finding as a place where the orchestrator, "у которого нет ничего кроме этого таска", would have to invent, says "Что команда закрыть не вправе, она адресует владельцу", and ends "Отчёт считает три группы: закрыто из источника, блокеры, отдано владельцу". It names no mode, no phase or batch as a target, and nothing between tasks, so it does not contradict the new text, and it is left as it is. Nothing under `src/` invokes the command, which the user runs, or an architect's round runs by expanding it by reference, and either reads the new text as written. The `docs/` files that mention the command by name, and the `CLAUDE.md` index, describe neither its targeting nor its report.
