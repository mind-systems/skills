# 80.5 — the rescue report drops the finder section

## What is true now

The skill is as 80.4 leaves it, which touches § 5.6 only.

`src/skills/task-rescue/SKILL.md`, § "Step 5.7 — Write the durable report", gives the report's template literally: a title line, the `**Project:**`, `**Date:**`, `**Stopped at:**`, `**Elapsed before the rescue:**` and `**Sessions:**` lines, the diagnosis exactly as Step 3 wrote it, a `## Who found what` section holding a `**Root cause found by:**` line and one bullet per finding with its finder and moment, and a `## Intended repair` section. The paragraph after the template says the diagnosis keeps its prose form and the finders live only in `## Who found what`; defines *who* (the user; head N by its number; the editor; the plan-reviewer or the reviewer at round R; the implementer or the planner; the rescue itself) and *when* (before the run; in the run; in the rescue; after the rescue, for a defect in the repair itself); says the role and round come from the sidecar's session keys and the number each plan-review and review file carries, and the user and the heads from the conversation; says a finder no artifact and no conversation states is written as "not stated"; and says the section holds one bullet per finding the diagnosis names. The `**Stopped at:**` line holds the step fact and what stopped the run, the review cycle spent at its round R or the role that escalated.

Step 3's paragraph "First write of the report" says that write "holds the diagnosis, the section on who found what, and the intended repair and rollback".

The user: «У нас есть летопись кто что поймал и где вектор развернул, пусть там собираются все случаи и рескью тоже. Там может быть ссылка на отчёт… А рескью эта возможность вообще никчему. Его дело таски спасать. И отчёт о спасении.»

## What must be true after

The template has no finder section. `## Who found what` goes with its `**Root cause found by:**` line and its bullet, and the template runs from the diagnosis to `## Intended repair`. The paragraph after the template that defines *who* and *when*, says where each comes from, writes "not stated" and fixes one bullet per finding goes whole; the diagnosis's prose form is Step 3's and stays there. `**Stopped at:**` keeps the step fact and what stopped the run.

Step 3's sentence on the first write says it holds the diagnosis and the intended repair and rollback, and names no section on who found what.

Who caught what is recorded in the family's chronicle of catches, `.ai-factory/chronicle/skills.md`, where a rescue's catches are linked to its report; the skill carries nothing of it. The rest of § 5.7 stays as it stands: the extension by dated sections, the destination, the hooks, the title phrase and "When the write cannot happen".

## What breaks on contact

**Rule:** a text breaks on this change if it names the finder section, a finder, or who or when a finding was caught.

**Sweep:**
```
grep -n -i -E "who found|finder|not stated" src/skills/task-rescue/SKILL.md
```

**Finding.** The search returns Step 3's first-write sentence, the template heading, and the paragraph after the template; each is a target above. No doc, skill or orchestrator text reads the section. The phase note `0226` records the finder line and its move to the chronicle, and the earlier rescue reports and the landed spec of the task that added the section keep the section as written, as history.
