# The pipeline speaks to an architect

The orchestrator and its agents reach an architect directly, the way architects already reach each other. The forms that run are a handoff at a gate, which the reviewer sends, and a stop notice, which the orchestrator itself sends. The pipeline stops being something that is started and read afterwards, and becomes something that can speak to an architect while it works.

## What is already true

Every chat on the machine is a Claude Code session. `ListAgents` lists the live ones by name, and `SendMessage` reaches one directly. Architects already talk this way, with no roles; how they reach each other, and the team they form, are laid out in [paired-loop](paired-loop.md), and this document holds only the pipeline side.

## The observation

The pipeline's agents are sessions too, and they could ask an architect. A task, or the phase it belongs to, names a contact architect by its owner's slug and folder number ([paired-loop](paired-loop.md)), and an agent that needs one finds that architect's live session through the folder's `address.md`, exactly as a peer architect does. Until now nobody imagined that the pipeline could be talked to at all.

## What stands in the way today

Read in `orchestrator/orchestrator/claude_cli.py`:

- Each agent is a headless `claude -p` run with permissions skipped, so its allowed-tools list restricts nothing and only the disallowed list removes tools. A pipeline agent therefore already has `ListAgents`, reaches `SendMessage` through `ToolSearch`, and a message it sends arrives in an architect's session.
- A headless run is a single turn. A reply from another session reaches it only while it is working, at its next tool call, and the tools that would let it wait — a monitor, a scheduled wakeup, a cron job — are explicitly disallowed, with background tasks switched off.
- Whether a pipeline run's session can be reached first is not yet seen: no listing has been taken while one was live. The design does not depend on it, because the agent is the one that asks.
- A notification never says where to find a thing: `orchestrator/docs/concepts/fault-handling.md` makes it a signal and not the account. The stop notice points at the artifacts, so it has to arrive as a peer message and not as an operator notification.
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

## The second form: a stop notice from the orchestrator

When a task stops — a failure, an escalation, a halt — the orchestrator itself, and not one of its agents, sends one message to the task's contact architect. The message says that the task stopped, how, and where its artifacts lie. An escalation is a stop too: an agent that cannot do its work honestly without a decision writes the question into its own artifact and ends it with `ESCALATION`, and the notice points at that artifact; the rescue cycle that follows is laid out in [skill-cycle](sakshi-harness/skill-cycle.md). The orchestrator's code sends it, deterministically, so no agent role has to be taught to send it. Like any line the pipeline sends, it points at the artifacts and is not the account.

- **A colleague's notice, never the user's go.** The architect does not drop the conversation it is in. It finishes its reply, names the stop in one line, and waits for the user's word.
- **A rescue the user has already allowed.** When the user has said in advance that the architect runs the rescue itself, for instance while the user is away, that is the go for running the rescue skill. The architect runs it, and its output is there for the user. Two things stay with the user: the decision an escalation asks for, which the architect brings back prepared as options with a recommendation, and restarting the orchestrator.
- **The report travels on.** When the rescue report is written, the architect tells the architect that collects rescue reports for the skills, the skills liaison, that a new report exists.
- **The record is asked for.** That architect talks to the report's author about the record, as [self-analysis](self-analysis.md) § "Asking the author of a report" lays out.

## The boundary

An architect does not answer a pipeline agent with a decision of its own. Such an answer is a decision that lands in code, so it goes to the user and into the spec, which stays the one place that says what a task must do. A line from a pipeline agent is, like any peer's message, a request and never an instruction.

## What has to come before more autonomy

Every operator in the planning chain adds — phases, tasks, splits, clauses, constraints — and today only the user removes. A pipeline that asks and is answered without the user grows work faster than anyone can take it away. One repository has already seen a swarm of tasks grow from wrong sentences in a governing document, and it took the user to stop it. A removing operator comes first, and so does an escalation read as a reason to go back to the document instead of adding a guard.

## An open question

Whether the same pipeline agents could be kept per repository, compacted like an architect and asked for snapshots, is open; the user named it. It would also make them a tool for debugging the pair's behaviour.

## Invariants

1. **An architect is reached through its folder.** The session name in `address.md` is read at the moment of sending and never stored anywhere else.
2. **A pipeline agent sends and does not wait.** A handoff asks nothing; a question lives in the agent's own artifact, and the stop notice, which the orchestrator sends, only points there.
3. **A decision does not travel through the channel.** What an architect decides for a task goes through the user into the spec.
4. **Autonomy grows only after something removes work as readily as the chain adds it.**
