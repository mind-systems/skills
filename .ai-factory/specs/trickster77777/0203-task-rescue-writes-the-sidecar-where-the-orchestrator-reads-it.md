# 51.1 — task-rescue writes the sidecar where the orchestrator reads it

## What is true now

`src/skills/task-rescue/SKILL.md` Step 1, in the bullet "Where the sidecar lives", locates the sidecar "per `orchestrator-artifacts` § 1": the flat `plans/<seq>-<slug>.json` for the default pair, and for a named roadmap a subdirectory keyed by its roadmap file stem, `roadmaps/john-doe.md` → `plans/john-doe/<seq>-<slug>.json`, with "`$TARGET_FILE` is already resolved above, so the stem is known here".

Step 5 has two write sites that name the flat path. Under "Depth: spec + plan" step 4 reads: "Locate the sidecar at `.ai-factory/plans/{seq}-{slug}.json`. Read it if present; start from `{}` if absent. Set the `step` key to `"planned:1"` and **delete** the `implementer` key …". Under "Depth: plan ratified, implementation absent" step 3 begins with the same sentence, "Locate the sidecar at `.ai-factory/plans/{seq}-{slug}.json`. Read it if present; start from `{}` if absent. Set the `step` key to `"plan_reviewed"` …". Under "Depth: spec + plan + code" step 5 says "same read/update/write procedure as the spec+plan depth above". The text wraps in the file at a fixed column.

The orchestrator reads a named roadmap's sidecar under `plans/<stem>/`: `orchestrator/orchestrator/main.py` roots `plans_dir` under `artifact_subdir`, and `agents.py` reads the sidecar as the plan file's `.json` sibling. In a repository on a named roadmap the rollback lands where the orchestrator does not read it, and the run resumes from the old step, silently.

## What must be true after

In both write sites the first sentence reads: "Locate the sidecar where Step 1 does — `.ai-factory/plans/{seq}-{slug}.json` for the default roadmap pair, `.ai-factory/plans/<stem>/{seq}-{slug}.json` for a named roadmap, `<stem>` being the stem of `$TARGET_FILE`." The sentences after it in each step are as they stand.

## What breaks on contact

**Rule:** a text breaks on this change if it names a sidecar path, or follows the write sites' procedure.

**Sweep:**
```
grep -rn "seq}-{slug}.json" src/ docs/ CLAUDE.md
grep -n "sidecar" src/skills/task-rescue/SKILL.md
grep -rn "plans/" src/skills/task-rescue/ src/skills/orchestrator-artifacts/
```

**Finding.** The first search reaches the two write sites alone, the task's target; no other skill, doc or `CLAUDE.md` names the flat sidecar path with that placeholder. The second reaches the places in the skill that speak of the sidecar. The Step 1 bullet already locates it by the layout and stays. The spec depth deletes the sidecar and names no path, acting on the file Step 1 located. The depth "spec + plan + code" takes the write-site procedure by reference, so it reads the new locator through the spec-plus-plan site. The escalation and no-repair branches leave the sidecar untouched and name no path, and the table of valid `step` states names none. The third reaches the artifact directories in Step 1's filter and `orchestrator-artifacts` § 1, which defines the layout the new sentence cites. The skill has no references directory. The default roadmap's flat layout keeps working: the new sentence names the flat path first, for the default pair, so a repository on `ROADMAP.md` locates the same file as before. `docs/sakshi-harness/skill-cycle.md` describes the rollback of the sidecar without a path, and the orchestrator reads the sidecar where the new sentence points.
