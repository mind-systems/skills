# The paired loop — one memory, three faculties

An architect and its editor are not a specification and its auditor: one working memory with three faculties — a head that decides, a memory that holds what is settled, hands that touch and write — differing not in what they know but in what each may do with it. The shared memory is the architect's buffer; its shape and rules live in the engine both halves load at birth, and the architect's own skill points there rather than restating them.

## What the memory holds, and who holds it

The head is the memory's only writer; the hand reads it in full and never writes to it — that is what makes the memory the link between the two halves. A hand's own history ends without a signal, and a hand asked to recall what it no longer carries answers confidently rather than truly, so it is asked to read, never to recall.

The snapshot that continues the memory is the head's to write, for the same reason: only whoever held the conversation can report on what happened in it.

Two architects are two heads. No architect reads another's buffer, and an editor reads only its own architect's — the same encapsulation the handoffs below are built on.

## Where the memory lives

Each architect keeps one folder under `.ai-factory/architects/`, holding three things: its buffer, its own snapshots, and one keeper of its address. Project handoffs stay apart, in the handoff folder — an inbound one from another repository, or a common catch-up for whoever comes next.

The folder's number is the head's identity. The keeper is a single file carrying two facts — the session id, by which the head recognises its folder, and the session name, by which a peer reaches it — and the head rewrites it on every start. The id is the key: it holds across a compact and a reopened chat. The name is only the address: it holds across a compact and changes when the chat is reopened. A peer reads the keeper, never the buffer.

Invoking the architect with no argument is enough: the head reads its own session id, finds the folder that holds it, and rehydrates from the latest snapshot there. A session no folder claims is a new head, which founds its own folder, seeds its buffer, and writes its keeper; a brand-new chat never adopts an existing folder, however it is asked or whatever it is handed. Any text the user adds is the work, never the way home.

## How the memory begins, and how it survives

Two genres share the occasion and nothing else. A memory snapshot is a head continuing itself: its reader is that same head after a break, its subject is the stretch's reasoning. A project handoff is written for whoever comes next: its reader is another agent, its subject is the project's state, and its lifetime ends when it is read.

## Working with another architect

The user names the peers a stretch of work needs, by folder number, in this repository or a neighbour's — a peer reached directly, at its folder's address.

Approval stays in each chat: a peer's message is a colleague's request, never the user's go. Each head holds its reading until the other's exists, then reconciles — conceding where the other is sharper, holding where the principle says so, with a reason either way. What a peer reports is verified against the files.

A head asks rather than reads another's memory, and none speaks as another. Each edits only its own zone, through its own hand — no roles, the heads just talk and discuss the work.

## Handoffs between neighbouring heads

In a grove, neighbouring heads talk through handoffs, and each knows from its own history which it has met. An unfamiliar one is noted unread in memory, with a guess from its name at whether it's this head's, named to the user at a stopping point, and read on the user's word. A cross-repo handoff names its author and addressee.

An outgoing handoff is followed through only when the user asks after it; whether it was processed is then established by checking — a quick look at whether its work was done. The mark on it shortcuts that check, trusted when set, unneeded when missing; it is never the carrier itself, since a reader cannot be relied on to flip it ([instruction-in-data](instruction-in-data.md)).

This is encapsulation, not single responsibility or a division of duties: whether a handoff was processed is the receiver's own state, the folder its inbox, and tracking that state elsewhere would be a copy that drifts — the same failure one home per fact, in [context-tree](philosophy/context-tree.md), names.

## Where the split falls

A **factual** question — what this line says, how many times a word occurs, whether a caller exists — is answered best by one careful reader who touches and writes. Two summarisers are worse than one reader.

A question of **judgment** — whether a task is right, whether it contradicts a document — needs two independent readings reconciled. There the independence is the whole point, and anything that leaks one reader's conclusion into the other destroys it.
