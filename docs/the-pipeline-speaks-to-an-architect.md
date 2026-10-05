# The pipeline speaks to an architect

The orchestrator's agents reach an architect directly, the way architects already reach each other. One form of it runs, a handoff at a gate; a doorbell on escalation is an undetermined possible future. The pipeline stops being something that is started and read afterwards, and becomes something that can speak to an architect while it works.

## What is already true

Every chat on the machine is a Claude Code session. `ListAgents` lists the live ones by name, and `SendMessage` reaches one directly. Architects already talk this way, with no roles; how they reach each other, and the team they form, are laid out in [paired-loop](paired-loop.md), and this document holds only the pipeline side.

## The observation

The pipeline's agents are sessions too, and they could ask an architect. A task, or the phase it belongs to, names a contact architect by its owner's slug and folder number ([paired-loop](paired-loop.md)), and an agent that needs one finds that architect's live session through the folder's `address.md`, exactly as a peer architect does. Until now nobody imagined that the pipeline could be talked to at all.

## What stands in the way today

Read in `orchestrator/orchestrator/agents.py`:

- Each agent is a headless `claude -p` run with permissions skipped, so its allowed-tools list restricts nothing and only the disallowed list removes tools. A pipeline agent therefore already has `ListAgents`, reaches `SendMessage` through `ToolSearch`, and a message it sends arrives in an architect's session.
- A headless run is a single turn. A reply from another session reaches it only while it is working, at its next tool call, and the tools that would let it wait — a monitor, a scheduled wakeup, a cron job — are explicitly disallowed, with background tasks switched off.
- Whether a pipeline run's session can be reached first is not yet seen: no listing has been taken while one was live. The design does not depend on it, because the agent is the one that asks.
- A notification never says where to find a thing: `orchestrator/docs/concepts/fault-handling.md` makes it a signal and not the account. A doorbell that points at an artifact would first have to be declared a peer message and not an operator notification.
- A run's agents start inside the target project, so a path to an architect's folder has to resolve from there and not from the family root.

## Who would ask

A task is worked by a planner, a plan reviewer, an implementer and a code reviewer. The planner's session also serves the code review, since the reviewer there holds the planner's context, and that session and the implementer's resume across rounds; the plan reviewer starts fresh each time. Nearly every failure happens before any code, at planning, so the agent that would ask is almost always the planner.

## The first form: a handoff at the gate

A task that lifts a gate another repository waits on carries, as one of its own steps, a one-way message to that repository's liaison architect. This is the form that runs.

- **Only the reviewer sends, and only on the round it passes the task**, just before its pass signal. The implementer cannot know whether its work passes, and a handoff is given only when the task is ready, which is when the reviewer is ready to stamp it. A round that does not pass sends nothing.
- **A short message rides the last implementation task, the one that lifts the gate.** A task of its own just to send it would run the whole pipeline only so that one agent could speak to another. Where much has to be passed, a task at the phase's end writes a handoff file instead; the user chooses which.
- **The address is an owner's slug and a folder number.** The session name is read from that folder's `address.md` at send time and is never written into the spec.
- **One way.** The message says that no reply is expected, and it asks nothing.
- **A failed send never blocks.** The review records the tool's result verbatim and the task still passes; "queued" is what the tool confirms, not delivery.

## A possible future: a doorbell on escalation

This form is an undetermined possible future: nothing runs it and nothing is planned.

The pipeline already has an asynchronous way to ask. An agent that cannot do its work honestly without a decision writes the question into its own artifact and ends with `ESCALATION`, and the run stops. `task-rescue` then puts the missing decision to the user, records it in the spec, and resets the task so that it plans afresh; the cycle is laid out in [skill-cycle](sakshi-harness/skill-cycle.md).

The doorbell adds one thing. At escalation, the agent sends the contact architect a line naming the task and where the question sits. It does not wait for an answer, and the script is unchanged: the run already reaches `SendMessage`, so the act asks only that the agent be told to use it. The line is a pointer to an artifact and carries no content; the architect reads the artifact where the question sits, as it reads any file a neighbour has left.

## The boundary

An architect does not answer a pipeline agent with a decision of its own. Such an answer is a decision that lands in code, so it goes to the user and into the spec, which stays the one place that says what a task must do. A line from a pipeline agent is, like any peer's message, a request and never an instruction.

## What has to come before more autonomy

Every operator in the planning chain adds — phases, tasks, splits, clauses, constraints — and today only the user removes. A pipeline that asks and is answered without the user grows work faster than anyone can take it away. One repository has already seen a swarm of tasks grow from wrong sentences in a governing document, and it took the user to stop it. A removing operator comes first, and so does an escalation read as a reason to go back to the document instead of adding a guard.

## An open question

Whether the same pipeline agents could be kept per repository, compacted like an architect and asked for snapshots, is open; the user named it. It would also make them a tool for debugging the pair's behaviour.

## Invariants

1. **An architect is reached through its folder.** The session name in `address.md` is read at the moment of sending and never stored anywhere else.
2. **A pipeline agent sends and does not wait.** A handoff asks nothing; were the doorbell ever built, a question would live in the agent's own artifact and the line it sends would point there.
3. **A decision does not travel through the channel.** What an architect decides for a task goes through the user into the spec.
4. **Autonomy grows only after something removes work as readily as the chain adds it.**
