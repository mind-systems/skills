# 84.1 — the capture records the session ids and the report names them

## What is true now

`src/skills/task-rescue/SKILL.md`, § "Step 1 — Discover artifacts", the paragraph that opens "**Capture the report facts.**", reads: "Record four facts now, at discovery, before anything is deleted, and hold them for the report Step 5.7 writes — Step 5 deletes the sidecar at some repair depths, and `step`/`elapsed` are unrecoverable once that happens." Its bullets name the project, the date, "**`step` and `elapsed`** — read from the task's sidecar; the two fields worth keeping, per `orchestrator-artifacts` § 3", where the sidecar lives — "a sidecar missed by reading the wrong path records exactly the same thing as an absent one — both numbers lost, with no signal" — and "**No sidecar on disk** → record both `step` and `elapsed` as **absent**; never guess, never reconstruct a number from anything else. Step 5.7 renders absence as absence." It records no session id.

`orchestrator-artifacts`, § "3. Sidecar fields", names `planner` and `implementer` as "resumable session ids". § "Step 5 — Apply repair and roll back artifacts" deletes the sidecar at spec depth, drops `implementer` at spec+plan depth and at the plan-ratified depth, and a re-run of the orchestrator overwrites keys: `_write_session` in `orchestrator/orchestrator/agents.py` sets `data[key] = value` on the sidecar's JSON.

§ "Step 5.7 — Write the durable report" gives the report a template whose header lines are `**Project:**`, `**Date:**`, `**Stopped at:**` and `**Elapsed before the rescue:**`, each filled from the Step 1 facts, and no line for a session.

## What must be true after

In § "Step 1 — Discover artifacts", the paragraph that opens "**Capture the report facts.**" reads in its lead sentence:

"Record these facts now, at discovery, before anything is deleted, and hold them for the report Step 5.7 writes — Step 5 deletes or rewrites the sidecar at some repair depths and a re-run overwrites its keys, so `step`, `elapsed` and the session ids are unrecoverable once that happens."

The bullet on `step` and `elapsed` reads:

"- **`step` and `elapsed`** — read from the task's sidecar, per `orchestrator-artifacts` § 3."

and a bullet follows the bullet on `step` and `elapsed`:

"- **The session ids** — every session id the sidecar holds, each under its key as the sidecar spells it. They are the sessions whose artifacts this rescue reads, and the report names them so that one can be resumed and asked to quote what it saw. The sidecar is the live state of the attempt and is overwritten; the report is the record of this attempt and its diagnosis."

In the bullet on where the sidecar lives, the clause reads "an absent one — everything it holds lost, with no signal." in place of "an absent one — both numbers lost, with no signal."

The bullet on an absent sidecar reads:

"- **No sidecar on disk** → record `step`, `elapsed` and the session ids as **absent**; never guess, never reconstruct a number from anything else. Step 5.7 renders absence as absence."

In § "Step 5.7 — Write the durable report", the template reads, directly after its `**Elapsed before the rescue:**` line:

"**Sessions:** <every session id the Step 1 capture holds, each as `<key>: <id>`, or "absent">"

## What breaks on contact

**Rule:** a text breaks on this change if it lists the facts the report captures without the session ids, says the ids are lost with the sidecar and the report holds none, or reads the report's header as ending at `elapsed`.

**Sweep:**
```
grep -rn "report facts" src docs CLAUDE.md
grep -rn "unrecoverable" src docs CLAUDE.md
grep -rn "fields worth" src docs CLAUDE.md
grep -rn "both numbers" src docs CLAUDE.md
grep -rn "No sidecar on disk" src docs CLAUDE.md
grep -rn "Elapsed before" src docs CLAUDE.md
grep -rn "Stopped at" src docs CLAUDE.md
grep -rn "elapsed" src docs CLAUDE.md
grep -rn "resumable session" src docs CLAUDE.md
```

**Finding.** The searches for `report facts`, `unrecoverable`, `fields worth`, `both numbers` and `No sidecar on disk` each return `task-rescue`'s Step 1 paragraph, the target. The searches for `Elapsed before` and `Stopped at` each return the Step 5.7 template, the target. The search for `elapsed` also returns: the dropped-key sentence "The loss of `planner`, `implementer`, and `elapsed` is intentional" in § "Step 5 — Apply repair and roll back artifacts", which stays true, since it is the sidecar that loses them and the report now holds the ids; the spec+plan and plan-ratified procedures that preserve `planner` and `elapsed` untouched, which stay true; the "What NOT to do" bullet "Do not overwrite `planner` or `elapsed` in the sidecar", whose sidecar discipline is unchanged, recording an id in the report keeping nothing in the sidecar; and `orchestrator-artifacts`' § "3. Sidecar fields" line naming `elapsed`, which stays true. The search for `resumable session` returns that same section, which already names the ids by key and stays true. A rescue tells an id from `step`, `elapsed` or `escalation` by that section's list, so a key the orchestrator adds reaches the capture when § 3 names it; that is § 3's lockstep with the orchestrator, not this task's change. The Step 3 rule that the diagnosis uses "no sidecar" vocabulary governs the diagnosis narrative; the report's header lines sit outside it, as `Stopped at` and `Elapsed before the rescue` already do, so it stays true. `.ai-factory/rescue-analysis/method.md` takes the `planner` id from a report's rewritten sidecar, which stays true; the report now also names it where the sidecar did not survive. No doc or `CLAUDE.md` text appears in any output. The reverse graph of `task-rescue`, `grep -l "task-rescue" src/skills/*/SKILL.md src/commands/*.md src/agents/*.md`, returns `orchestrator-artifacts` alone, which names the sidecar's fields and states no report fact; the `docs/` and `CLAUDE.md` mentions of the skill name it and state no report fact.
