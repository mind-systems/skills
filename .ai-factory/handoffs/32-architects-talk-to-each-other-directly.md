# Handoff — architects talk to each other directly, and the pairing engine should go

**Processed:** `[x]` — whoever reads this marks it; a marked handoff is spent.

## 1. Frame

This comes from a working session on `tradeoxy_core` (2026-09-29). It proposes an update to this repo that the user asked for in so many words. It is written by the architect holding buffer `130` there, for whichever architect works this repo next. The evidence is a real stretch of work, described below. The files named here override this description wherever they disagree.

**The user's verdict, verbatim:** «Скилл в текущем его состоянии — нерабочая штука. Плохой получился, а то что мы с тобой тут делали — именно этого я ждал изначально. И решающий-применяющий — это должно уйти из скила, мы со 123 и 120 не договаривались кто что делает, мы просто разговаривали и обсуждали таски. Простой рабочий процесс. Чем больше правил агенту навешиваешь — тем сложней ему исполнять то что он делает лучше всего. А этот наш прогон был в лучшем виде.»

## 2. What happened

- **The discovery.** Every chat on the machine is a Claude Code session. `ListAgents` lists live peer sessions by name, and `SendMessage` to that name reaches the session directly: the message arrives in its conversation, marked as coming from another session. Two dormant architects (buffers `120` and `123`) were being rehydrated in their own chats. Their editors were unreachable, because a subagent of another session cannot be addressed at all. The architects themselves answered at once.
- **Waking them.** Each was asked what it last remembered: HEAD, phase, open threads. From their own answers, checked against git, three handoffs were written in the project (`78`, `79`, `80`). The user invoked the architect skill in each chat with its handoff, and both rehydrated fully.
- **Working together on one phase.** Phase 39 was buffer 123's zone. The two architects did the following:
  - They read the phase independently. Each held its read until the other's arrived, then they reconciled. They agreed on the core finding, and each caught what the other missed. From there they converged on a new task order; 123 refined mine, and I conceded.
  - Buffer 123's pair re-grounded five specs. Then both pairs ran pin-gaps over the tail in parallel, with neither sending findings until both reports existed, and reconciled again. They found thirteen corrections between them, including a run that would have hung forever on a dead order stream — a real defect neither pair had alone.
  - Buffer 123 applied every change with its own editor, on the user's go given in its own chat. Buffer 130 verified the result against the files. Once, buffer 130 wrongly reported a correction as missing, and buffer 123 caught the faulty grep behind it.
  - The phase then ran through the orchestrator without a single rescue.
- **Nobody assigned roles.** There was no deciding half and no applying half. Each architect owned its own zone and edited only there. The other read, questioned and verified.

## 3. What actually carried weight

A few things did all the work. Each is a plain habit, not a protocol:
- **Approval stays in each chat.** A peer's message is a colleague's request, never the user's go. The harness already frames cross-session messages that way; the architect only has to keep to it and say so.
- **Hold your own reading until the other's report exists**, then reconcile: concede where the other is sharper, hold where the principle says so, and give the reason either way. This is the rule the skill already has for the architect and its editor, applied between two heads. It is why their agreement was signal and not echo.
- **Verify what the other reports against the files**, in both directions.
- **Ask; don't read another head's buffer.** The existing rule held. When one architect needed to know what the other still had open, it asked.
- **No impersonation.** The user asked whether the first messages should pose as the other architect's own head. They should not. Words attributed to a head that never said them become false memory in that head's hand, and the pretence buys nothing, since an agent reports by fact whoever asks.

## 4. Addressing: identity by buffer, reach by session

The user finds the buffer number convenient as the architect's identity, and it is: the buffer is the head's memory, stable across compacts, restarts and sessions.

What was missing was **reach**:
- The session name (`tradeoxy-core-cd`) is the address. It belongs to the session, not to the head, and it changes when the session restarts.
- Nothing maps a buffer to a session. The architect had to message both fresh `tradeoxy_core` sessions, introduce itself honestly, and ask which buffer each held.
- An architect can learn its own address: `ListAgents` opens with «This session is `<name>`».

**The user's proposal, which this architect supports:** an architect records its current address in its buffer, beside its editor's handle, and rewrites it on every start or rehydration.

The one tension to settle: `architect-editor-engine` says no architect reads another's buffer. Two ways out, for the skills pair to choose between:
- **(a)** The buffer's header carries a single address line — the one thing a peer may read — and the no-read rule narrows to the memory itself.
- **(b)** The address lives outside the buffer, in a small roster of «buffer → session», where each head writes only its own line.

(a) is fewer artifacts and matches the user's instinct. (b) keeps the no-read rule whole.

## 5. The proposed change

Keep it small; the user's ruling is that every added rule costs the agent its best work.

1. **Retire `architect-pairing-engine`.** Its whole premise is gone: the user as courier, relays pasted as one code block, deciding versus applying. Remove the skill and every reference to it. Find them with `grep -rl "architect-pairing-engine" src docs`; at writing, `agent-architect`'s paragraph on recording an assigned pairing role is one.
2. **Add a short passage on working with another architect**, in `agent-architect`, or in the engine if it concerns both halves. Aim for a few sentences, not a contract. It should cover:
   - how to find a peer (`ListAgents`, `SendMessage`);
   - that the buffer is the identity and the session name the address;
   - that approval stays in each chat;
   - hold, then reconcile;
   - ask rather than read;
   - no impersonation;
   - each architect edits only its own zone, through its own editor.
3. **The address line**, per section 4, once (a) or (b) is chosen.
4. **`docs/paired-loop.md`**: bring it in line wherever it describes two architects.

## 5a. Going further: one folder per architect, found without being told

The user took section 4 further. Today an architect's buffer lives in `.ai-factory/notes/` and its snapshots in `.ai-factory/handoffs/`, mixed in with every other note and handoff. The user's proposal:

- **`.ai-factory/architects/`**, holding one folder per architect.
- Each folder keeps that architect's **buffer and its own snapshots together**. Reading the folder then reads the architect's life: what it did, in order.
- Handoffs that belong to the project rather than to one head stay where they are: inbound handoffs from another repo, and a common catch-up like `tradeoxy_core`'s `78`. A folder holds the head's own memory and the snapshots that continue it.

**The second half of the proposal: the architect knows its folder without being told.** Today the only carrier is the handoff that names the buffer, and the user has to hand the architect its handoff after each compact. The user calls this unreliable, and it is. What would carry it:

- **The session id survives compaction.** Evidence from the run: `tradeoxy_core`'s session `d80d7c1f-…` compacted many times over two weeks, and its transcript, its subagents and the editor spawned on 2026-09-14 all still live under that one id. A compact changes the context, not the session.
- **The architect cannot reliably read its own session id, but a hook can.** A `SessionStart` hook receives `session_id` in its input and fires with source `compact` (as well as `startup`/`resume`), and its output is added to the context. So a hook could look the id up in `.ai-factory/architects/*/` and inject one line into the fresh context: «you are the architect of `.ai-factory/architects/<NN>/`; rehydrate from its latest snapshot».
- **The bare invocation is the whole trigger** (the user's refinement): `/agent-architect` with no argument at all. The skill checks whether a folder claims this session.
  - **If one does**, the architect rehydrates: it reads that folder's latest snapshot, then whatever the snapshot points to.
  - **If none does**, this is a fresh architect. It founds its own folder under `.ai-factory/architects/` — «создаёт себе поле жизни» — seeds the buffer there, and writes its session id and address into the folder.

  No argument, no «регидрируйся», no handoff pasted by the user. Any text the user adds is the work to do, not the way home.

**What to verify before building it:**
- that `--resume` keeps the same session id, or else what re-registration looks like;
- the exact hook output field that adds context;
- where the hook is configured — project or user settings. That is the user's to place; an agent does not edit its own settings.

The folder would also settle section 4's tension: the address and the session id sit in the folder as files of their own, so a peer reads a file, never the buffer.

## 6. What is not known yet

- Every session in this run was live and in the same permission mode (`bypass`), so messages arrived at once. A peer in another mode holds cross-session messages for its own user's approval, and a closed chat cannot be reached at all. Neither case was exercised.
- Whether an architect should proactively tell its peers its new address after a restart, or wait to be asked.
- Where the passage in 5.2 lives best: `agent-architect`, the engine, or both.

## Next

Plan this as a phase in this repo with the user:
- retire the pairing engine;
- add the short passage;
- move the buffer and snapshots into `.ai-factory/architects/<NN>/`, with the session id and the address as files there, so no reader of another architect's folder ever reads its buffer;
- rehydrate without being told, through a `SessionStart` hook the user places.

Docs first, as this repo's own discipline has it — `architect-editor-engine` holds the buffer's path and numbering today and changes with it.
