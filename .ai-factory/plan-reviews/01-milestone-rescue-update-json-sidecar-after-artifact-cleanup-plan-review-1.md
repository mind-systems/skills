# Plan Review: milestone-rescue — update JSON sidecar after artifact cleanup

**Plan file:** `.ai-factory/plans/01-milestone-rescue-update-json-sidecar-after-artifact-cleanup.md`
**Target skill:** `.claude/skills/milestone-rescue/SKILL.md`

## Risk Level
🔴 High — the plan as written instructs the agent to do something the skill's `allowed-tools` frontmatter does not allow. Without a frontmatter change, the new sub-step is not executable.

## Critical Issues

### 1. `allowed-tools` frontmatter is not updated — the new sub-step has no runnable tool path

Current frontmatter (line 11 of `SKILL.md`):

```yaml
allowed-tools: Read Edit Glob Grep Bash(git *) AskUserQuestion
```

The plan (Task 1, instructions 3 and 6) tells the agent to use `json.load` and `json.dump` — i.e. invoke Python via Bash. But Bash is restricted to `Bash(git *)`, so the agent cannot run `python3 -c "..."`. Equally, the mapping table includes a "Sidecar doesn't exist → create it with correct `step`" branch that requires the `Write` tool — also not in `allowed-tools`.

Net effect: every code path in the new sub-step either needs a tool that is not granted, or requires `Edit` to surgically rewrite a JSON file by exact-string match (fragile across formatting differences and impossible when the file does not exist).

**Fix:** Add a Task 0 (or merge into Task 1) that extends `allowed-tools` to include both `Write` and an unrestricted-enough `Bash` permission (e.g. `Bash(python3 *)` alongside `Bash(git *)`). Pick one of:

- Option A — keep the Python wording the note uses:
  `allowed-tools: Read Edit Write Glob Grep Bash(git *) Bash(python3 *) AskUserQuestion`
- Option B — drop the `json.load`/`json.dump` wording and rewrite the sub-step to use only `Read` + `Write` (parse/serialize JSON "in the agent's head"). Then add only `Write` to `allowed-tools`.

Either is acceptable, but the plan must pick one and reflect that choice in both the frontmatter and the prose. As written, it does neither.

### 2. The plan copies the note's `json.load` / `json.dump` wording without deciding whether the skill is a Python-driven skill or a tool-driven skill

The other steps in `SKILL.md` are written in tool-agnostic prose ("use Edit to modify…", "use `git status --short` to identify them") — no Python anywhere. Introducing `json.load`/`json.dump` would be the first place in this skill that prescribes a specific runtime. That is a stylistic departure that should be a deliberate choice, not a side-effect of copying a note verbatim.

Recommendation: rephrase Task 1, instruction 3 and 6 to "parse it as JSON" / "serialize it back as JSON with 2-space indentation", matching the existing prose style. The mapping table still gets copied verbatim (per the note's explicit instruction), but the surrounding sentences should read like the rest of Step 5.

## Medium Issues

### 3. Interaction with Step 5.5 is not specified

Step 5.5 ("Propagate findings to open milestones") currently runs *after* Step 5's deletion block. If the sidecar update is added at the tail of Step 5 (before the "Show the user the list of deleted files…" confirmation), the order becomes: delete artifacts → update sidecar → confirm rescue complete → Step 5.5 propagation question. The plan does not explicitly say where it lands relative to Step 5.5, but the prose ("before the final `Show the user the list of deleted files and confirm the rescue is complete.` line") implies inside Step 5, which is the right call. Worth stating that explicitly so the implementer doesn't accidentally insert it after Step 5.5 or at the top of Step 5.

### 4. "Sidecar doesn't exist" row of the mapping table is ambiguous on the right-hand side

The verbatim row reads:

| Sidecar doesn't exist | create it with correct `step` |

This is recursive: the "correct `step`" must itself be looked up from the rows above. The plan should add one explicit instruction sentence after the table clarifying that when the sidecar does not exist, the agent first determines `step` from the same on-disk rules (the first three rows), then writes a new file containing only `{ "step": "<value>" }`. Otherwise an agent reading the table cold may write `step: "create it with correct step"` literally, or get stuck.

### 5. No guidance for the "reviews exist and pass" case

The mapping table covers three post-cleanup situations, but not "plan-reviews pass and reviews pass". In a normal rescue this should not happen (the rescue would not have been triggered), but if it does occur (e.g. user invokes rescue manually with a still-green pipeline), the plan gives the agent no instruction. Acceptable to leave as-is, but worth a one-line note: "If reviews pass, the orchestrator finished — surface this to the user and skip the sidecar update."

## Minor Issues

### 6. Task 2 wording overlap with Task 1, instruction 7

Task 1 instruction 7 already tells the agent to "Explicitly forbid touching `planner` / `implementer` / `elapsed`." Task 2 then adds the same forbiddance to the "What NOT to do" list. This is fine (defense in depth) but the plan should call out that the duplication is intentional rather than a missed dedup pass.

### 7. Sidecar file existence check — what counts as "exists"

The plan does not say whether the agent should look in the working tree only, or also consider whether the sidecar is staged / tracked. Given that the deletion block uses git-native commands (`git clean -f`, `git rm -f`), it would be consistent to check the working tree via `Glob` or `ls`. A one-liner in the prose would prevent confusion.

## Positive Notes

- Correct file path `.claude/skills/milestone-rescue/SKILL.md` (not the upstream-style `milestone-rescue/SKILL.md` mentioned in the note).
- Correct insertion point — end of Step 5, before the final confirmation line, before Step 5.5.
- Correctly requires the mapping table be copied verbatim, as the source note demands.
- Correctly preserves section numbering — does not bump Step 5 to a new top-level step.
- Task 2 (extending "What NOT to do") is the right place for the preservation invariant.

## Required Changes Before PASS

1. Update `allowed-tools` frontmatter to grant the tools the new sub-step actually uses (either `Write` + `Bash(python3 *)` or just `Write` plus a tool-agnostic rewrite of the prose). Add this as an explicit task.
2. Rewrite Task 1 instructions 3 and 6 to either commit to Python (and reflect it in frontmatter) or commit to Read+Write (and drop the `json.load`/`json.dump` wording).
3. Add a clarification sentence after the mapping table for the "sidecar doesn't exist" branch so the agent knows to pick `step` from the first three rows.
4. Optionally state interaction with Step 5.5 explicitly.

Once the `allowed-tools` and prose-style issues are reconciled, the plan is otherwise sound and well-scoped.
