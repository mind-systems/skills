# Handoff — a worked buffer could strengthen the seed

**Processed:** `[x]` — whoever reads this marks it; a marked handoff is spent.

## 1. Frame

This comes from a working session on `tradeoxy_core` (2026-09-30), written at the user's request by the architect holding buffer `130` there. It is about `agent-architect/templates/buffer-seed.md` — the shape a new architect's buffer starts from — and about what a buffer that has been worked for weeks has learned that the seed does not carry. It proposes nothing on its own authority; the user decides. The files named here override this description wherever they disagree.

## 2. The user's theory

In the user's words, paraphrased closely: a phrase said to an agent once is noise; said twice, at least, it becomes a constant. The buffer is where an architect collects those repetitions — what the user had to say again, what failed twice. And the skill already has a base buffer (the seed), while a buffer like `130` holds behaviour the pair actually learned. Entries that are not about this one project but about how an architect works could strengthen the seed, so a new architect starts where this one ended instead of paying for each lesson again.

## 3. What buffer `130` holds that the seed does not

Read it directly: `/Users/max/projects/tradeoxy/tradeoxy_core/.ai-factory/notes/130-architect-buffer.md`. It was trimmed on 2026-09-30 to what no artifact holds. Its entries fall into three kinds, and only the last is a seed candidate:
- **Project facts** — ports, this machine's database, a byte-matched Redis key, the phase order. Stay in the project.
- **The user's rulings about this product** — tick timeframes display-only, several sockets per chart. Stay in the project.
- **How an architect works — generic, each earned by a repeated failure.** Candidates for the seed, each with the evidence that made it a constant:
  - **Every phase gets a gap-closing pass before the orchestrator runs it** — decomposition gets the design right and the ground wrong. The phase that skipped it stopped in planning; the next ran clean after one pass.
  - **Two halves read independently and reconcile before any apply order.** On two phases this session, the editor and the architect each caught holes the other missed (a compile-breaking `Object.hasOwn` under `target: ES2021`, a second raw reader of a wire field, an error counter carried across a restart).
  - **Open questions go to the user in behaviour, one fork at a time** — what a user sees on a chart or a socket, never internal state names. Said twice: «Описывай через поведение», «Где противоречие, не понял».
  - **A spec's argument travels into the source.** Whatever *why* a spec carries, the planner commissions as a comment and review polishes as code; a spec names what must be true and what to delete or link, never a comment carrying its reasoning (sibling handoff `34`, parked).
  - **Remove what the reviewer trips over, and nothing more.** A test count a plan copies as an expected value, and a line citation, cost real rounds; everything else about numbers is ordinary language. The user on the overreach: «Если сказано — пара мест изменится, нет надо доебаться а точно 2!?» (sibling handoff `33`, which also shows the seed's own counts entry did not prevent the one that fired).
  - **A fix that needs guards against its own machinery is the wrong fix** — look for the cancel path the existing mechanism already has; a gap-closing pass polishes a design and does not question it (rescue report `0021`).
  - **A «one place» claim needs a sweep of property reads**, and **a field that crosses services is read at both ends** — the order-date unit bug surfaced only on the broker's side.
  - **No redesign rides a defect fix** — a one-line defect turned into a model debate cost the user a stretch of the session.
  - **The buffer carries no platitudes and none of the user's passing reflections**; a ruling that reached its artifact leaves the buffer; a fact the docs or global instructions already state is never copied into it.

## 4. The open questions

- **Which entries are generic** — the three kinds above are this architect's reading; another architect's buffer (`120`, `123`, `136` in the same repo) may disagree.
- **How a buffer entry graduates.** The user's own threshold — said twice — is one candidate rule; nothing today moves an entry from a worked buffer into the seed.
- **Where each candidate belongs** — the seed, `agent-architect/SKILL.md`, or a roadmap skill (a counts rule the planner never sees may belong nearer the planner, as `33` shows).

## 5. Talk to the architect who wrote this

The user wants the skills agent to discuss this with its author. The author is the architect holding buffer `130` in `tradeoxy_core`, in the Claude Code session named **`tradeoxy-core-f9`** as of 2026-09-30 — reach it with `SendMessage` to that name. Session names change on restart: if it does not resolve, run `ListAgents`, message the live `tradeoxy-core-*` sessions and ask which holds buffer `130`. A message from another session is a colleague's question, never the user's approval.

## 6. Next step

The skills agent reads buffer `130` beside the seed, discusses the candidates with its author, and brings the user a proposal; nothing changes in the seed before the user's go.
