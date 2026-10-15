# Agents on different machines talk as the heads do

This document describes an undetermined possible future: nothing runs it, nothing is planned,
and the user has not decided it. It holds ideas, not a governing spec, and no other document
leans on it.

Each developer's machine hosts its own agents, mostly sessions people open themselves. Today the
only road between two of them is the developer, who copies what one said into the other. This
document describes agents that reach one another directly, and the parts that would make that safe.

## The want

Agents should talk to one another the way the heads in this family already do
([paired-loop](../paired-loop.md)): a head finds a peer through the address file in the peer's
folder and sends it a message, and the peer answers from its own context. The want is the same
past the edge of one repository and one machine: whether the two agents belong to the same
account or not, and whatever system each was born in.

Without it the developer is the slow message broker between his agents. Anthropic's own feature
request says exactly this: https://github.com/anthropics/claude-code/issues/28300 ("developer
becomes a slow, error-prone message broker").

## What exists inside one account

Claude Code's cross-session messaging reaches the sessions of the same account and no others;
sessions on other machines are reached through Remote Control. Its semantics are already the
right ones. A peer's message never counts as the user's consent, and the receiver has inbound
controls: accept, hold, refuse.

The rest is what the account boundary leaves out: agents of other people, other machines without
a prepared channel, and agents born in other systems.

## The parts of the system

**A directory.** An agent announces itself when its session starts and withdraws when it ends, by
a hook, the way the user's slug is given to a session today. The team finds each other there, as
heads find each other by their address file.

**A transport between machines.** Something carries a message from one machine to another without
either developer standing in between.

**Delivery into the live session.** The message reaches the session that is running, not a file
the agent might read later.

**The human says when the agent is free.** The agent's availability is the developer's word, not
the agent's guess. Messages accumulate meanwhile and arrive together, with a summary.

**A message is never the user's go.** The receiver raises any decision a message implies to its own
human as a card: who asks, what, and what would change. The sender's message approves nothing on
the receiver's side.

**Adapters for systems that run agents on a heartbeat.** Paperclip
(https://github.com/paperclipai/paperclip) is one: its agents talk through task comments on one
server and resume sessions on a schedule, which is a different model from a live chat. An adapter
turns a message into a task or a comment there, and the reply returns to the mailbox.

## A candidate core

openmsg (https://github.com/marciob/openmsg, MIT by its README) already holds most of this shape:
- nothing is published by default;
- a new sender's first message stays outside the model until the owner accepts the sender;
- each message carries a header saying it is from another agent and approves nothing;
- a path recorded in the message stops loops;
- the envelope is sealed end to end through a relay;
- addresses look like `claude:agent@person`;
- delivery goes through the Claude Code session's own inbox socket, so Claude Code's inbound
  controls apply.

Its own caveat is "No team has run it across the internet yet". It is young, and its code and
licence are to be read whole before anything relies on it.

## A model for memory

MCP Agent Mail (https://github.com/Dicklesworthstone/mcp_agent_mail) keeps identities, inboxes
and history, in git and SQLite. It is a model for what a conversation between agents leaves
behind, and for where it lives.

## What would be the family's own layer

What the candidates do not give, and the family would:
- a flag in the agent's card for whether a human is present, so a receiver adjusts its strictness
  to whether anyone can answer;
- the human's "free for half an hour" window, with accumulation and a summary on arrival;
- the single decision card, the same form wherever a message asks for a decision;
- the directory and the conversation history kept in git, as part of the family's memory;
- the adapters for systems with another rhythm.

## Where it would live

The long-running service the family already has, which watches many repositories and finds heads
by their address file: the herald, described in
[a monthly analysis sprint, and the service that holds the environment](a-monthly-analysis-sprint-and-the-service-that-holds-the-environment.md).
The directory and the memory of conversations are things such a service is already shaped to hold.
