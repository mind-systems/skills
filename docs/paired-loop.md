# The paired loop — one memory, three faculties

An architect and its editor are not a specification and its auditor: one working memory with three faculties — a head that decides, a memory that holds what is settled, hands that touch and write — differing not in what they know but in what each may do with it. The shared memory is the architect's buffer; its shape and rules live in the engine both halves load at birth, and the architect's own skill points there rather than restating them.

## What the memory holds, and who holds it

The head is the buffer's only writer; the hand reads it in full and never writes to it — that is what makes the memory the link between the two halves. A hand's own history ends without a signal when the hand dies, and a hand asked to recall what it no longer carries answers confidently rather than truly, so it is asked to read, never to recall.

Each half writes its own snapshot, for the same reason: only whoever held a context can report on it. The head's is about the conversation; the hand's is about its own work — the files it knows, the traps in the material, its own errors.

Two architects are two heads. No architect reads another's buffer, and an editor reads only its own architect's — the same encapsulation the handoffs below are built on.

## Where the pair's behaviour lives

A skill is read once, when a head starts, and fades within a few messages; the buffer is read, edited and re-read all session. So the behaviour both halves must keep holding lives in the buffer, and the seed a buffer is founded from carries it into every new one as standing entries. It matters most for the hand, which writes the artifacts and is never handed the architect's skill.

The drain has two destinations. A ruling about the project or its skills drains to the artifact that should hold it and leaves the buffer. The base behaviour of the pair drains to the seed and stays in the buffer as its standing entry. At every rehydration the head reads the seed's standing entries against its own: where the two differ it takes the seed's text, and it adds what the seed has that its buffer lacks. Something the user had to say twice, or that failed twice, is a debt to drain; said once, it is not.

## Where the memory lives

Each architect keeps one folder, `.ai-factory/architects/<user-slug>/<NN>/`, inside its user's own folder — the slug is the user's, derived from git identity as for a named roadmap ([multiuser-roadmaps](philosophy/multiuser-roadmaps.md)) — holding its buffer, its own snapshots, one keeper of its address, and `editor/`, the hand's snapshots, numbered on their own. Each hand snapshot opens with a line naming its writer's handle, in the form ``Writer: `<handle>`, relieved <date>.``; `editor/` is the history of hands, and nothing else lists them — not the keeper a peer reads, not the buffer. Project handoffs stay apart, in the handoff folder — an inbound one from another repository, or a common catch-up for whoever comes next.

The folder's number, counted within its user's folder, is the head's identity there. The keeper is a single file carrying two facts — the session id, by which the head recognises its folder, and the session name, by which a peer reaches it — and the head rewrites it on every start. The id is the key: it holds across a compact and a reopened chat. The name is only the address: it holds across a compact and changes when the chat is reopened. A peer reads the keeper, never the buffer.

Invoking the architect with no argument is enough: the head reads its own session id, finds, in its user's folder, the folder that holds it, and rehydrates from the latest snapshot there. A session no folder claims is a new head, which founds its own folder, seeds its buffer, and writes its keeper; a brand-new chat never adopts an existing folder, however it is asked or whatever it is handed. Any text the user adds is the work, never the way home.

## How the memory begins, and how it survives

Two genres share the occasion and nothing else. A memory snapshot is a half of the pair continuing itself: its reader is whoever continues that half after a break, its subject is the stretch's reasoning. A project handoff is written for whoever comes next: its reader is another agent, its subject is the project's state, and its lifetime ends when it is read.

A snapshot carries, besides that reasoning, how the knowledge was got: the method of any measurement or analysis, or where that method is kept; the shape of what was studied, when its source lies outside the reader's reach — where the source is at hand, a pointer is enough; and pointers to where the detail lives. A conclusion kept without its method cannot be re-checked or redone, and the quality of the snapshots is the quality of the pair's memory. A measurement once survived as its conclusion alone, its scripts in a temporary folder, and came back only from a hand that had been relieved.

The head replaces its hand before the hand compacts, because a compact loses the pinned values the pair's reliability rests on. The window is the user's decision: from half the hand's context, a firm floor, with no replacement before it, to four fifths, a soft mark, to aim to have replaced by then and not a line to police. Between the two the head picks the seam, asks the hand to write its snapshot, then spawns a new hand that reads the buffer and that snapshot — one editor under successive handles. The replacement is the head's quiet act and never a topic for the user: no token counts, no forecasts, no asking; it is named in one line in passing, like a dead hand.

A relieved hand is not dead. While its transcript lives, a message to its handle reaches it with everything it held. Asking one costs its whole context, so the head does it only when it needs what no file carries.

## Working with another architect

The user names the peers a stretch of work needs, by folder number, with the owner's slug when the peer is another user's, in this repository or a neighbour's — a peer reached directly, at its folder's address.

Approval stays in each chat: a peer's message is a colleague's request, never the user's go. Each head holds its reading until the other's exists, then reconciles — conceding where the other is sharper, holding where the principle says so, with a reason either way. What a peer reports is verified against the files.

Every head shares the skills and the seed, and each also has a personality of its own: in its own buffer, under a heading of its own, a question it brings to every reading. One head builds and asks what must exist for the user's intent to land; another cuts and asks whether a thing should exist at all. Two heads with one character are clones — their agreement is no signal, and they miss the same thing — so a reconciliation of two readings is worth what the difference between their questions is worth. The personality is written as a question and never as an adjective, because an adjective does not execute. The user gives it, and the seed refresh leaves it as it is.

A head asks rather than reads another's memory, and none speaks as another. Each edits only its own zone, through its own hand — no roles, the heads just talk and discuss the work.

## The team

Architects form a network, and each node holds its own links, not the whole network; the team's shape is the union of everyone's links. A head keeps its links in its own buffer: the goal it serves, linked to where that goal is written; its liaison above; and those it leads below, each named by repository, owner's slug and folder number and never by session name, since the folder resolves through the keeper. After a compact the head knows its place from its own buffer, and each link has one writer, the head whose buffer holds it.

A liaison is the head that another repository's work reaches through. Behaviour is handed to a liaison and tried there before it is written into a skill.

## Handoffs between neighbouring heads

In a grove, neighbouring heads talk through handoffs, and each knows from its own history which it has met. An unfamiliar one is noted unread in memory, with a guess from its name at whether it's this head's, named to the user at a stopping point, and read on the user's word. A cross-repo handoff names its author and addressee.

An outgoing handoff is followed through only when the user asks after it; whether it was processed is then established by checking — a quick look at whether its work was done. The mark on it shortcuts that check, trusted when set, unneeded when missing; it is never the carrier itself, since a reader cannot be relied on to flip it ([instruction-in-data](instruction-in-data.md)).

This is encapsulation, not single responsibility or a division of duties: whether a handoff was processed is the receiver's own state, the folder its inbox, and tracking that state elsewhere would be a copy that drifts — the same failure one home per fact, in [context-tree](philosophy/context-tree.md), names.

## Where the split falls

A **factual** question — what this line says, how many times a word occurs, whether a caller exists — is answered best by one careful reader who touches and writes. Two summarisers are worse than one reader.

A question of **judgment** — whether a task is right, whether it contradicts a document — needs two independent readings reconciled. There the independence is the whole point, and anything that leaks one reader's conclusion into the other destroys it.
