# Memory snapshot — the vocabulary written down

You are the same architect, in the same work. This supersedes snapshot 38's next action; 38 stays the record of 2026-10-01 to 2026-10-05 and carries the reasoning of the day the team found Ports and Adapters. This one covers the rest of 2026-10-05, after 38 was written: where the followed sources live, architects per user, Paperclip examined as a neighbour, and the two docs that wrote the day's conclusion down.

## Read first

`buffer.md` whole — `## Team`, then § "Where the work stands" (the position only; rewritten, not appended), then § "Rulings, in the user's own terms". Then snapshot 38 if you need why the day went as it did; this file assumes it.

## Where you stand

Committed: the last commit is `7db7bbe` "Names and reasons, not laws". Nothing in flight; the tree was clean after it except the buffer edit and this file.

Above the stop: 73, 74, 75 decomposed and queued for the orchestrator; 76 outlined and deepened with no tasks. Below the stop: nothing.

## What happened, and why each turn was taken

**Sources found a home: `upstream/`, one file per source.** The user disliked both `.ai-factory/source-checks.md` and the list in `CLAUDE.md`, with no proposal of his own. I proposed a tracked `sources/` folder; he refused the name ("сорсес не подходит, тк уже есть срц") and also `docs/` ("там наше поведение"). Then I proposed the folder that already exists: `upstream/`, holding `ai-factory.md`, `spec-kit.md`, `paperclip.md` (URL, counterparts, why we follow it, check entries with `Last seen:`), each source's git-ignored clone beside it, `.gitignore` taking `upstream/*/`. He kept the name: "апстрим хорошее место и название пусть остаётся." The script in 75.1 now reads its list from those files — no list kept in two places. Before that, his correction to the first design: cloning into a temp dir on every run is slow; keep local clones and fetch.

**Architects are per user (phase 76).** His thought: "архитекторы у каждого юзера свои и надо было сразу их класть в именованные папки." Like named roadmaps: `.ai-factory/architects/<slug>/<NN>/`, numbering within the user's folder, the slug derived as for a named roadmap. `docs/paired-loop.md`, `docs/the-pipeline-speaks-to-an-architect.md` and `CLAUDE.md` already say so; the phase note lists only the skills that lag (engine path and numbering, `agent-architect`'s probe and peer passages, the seed's `## Team`). Migration of existing heads is by his hand.

**Paperclip as a neighbour.** Read in depth: a server that runs agents as a company; work and review history in its Postgres; it wakes Claude Code by spawning `claude --resume <session-id>` (or ACP) with a wake payload, never an open session; atomic checkout by one conditional update; budgets as the brake; it writes `.claude/settings.local.json` to override the user's permissions. Our orchestrator is the same shape at one task's scale (headless `claude -p`, session ids in the sidecar). The editor is a subagent of the head's session — reachable only from it, which is why stopping it kills it. Waking a head that is not live would be `claude -p --resume <id>` from `address.md`, never while its chat is open, read-only work only.

His questions about it, and where I was wrong: I said Paperclip's agents would refuse to code because our global layer says "chat plans; the orchestrator implements" — he pointed out the orchestrator gets the same input and codes; the rule carries its scope ("In a chat session"), and agents apply it where its reason holds. I listed conflicts of running beside Paperclip in one repo; he said that is ordinary two-people-in-one-repo work, branches and PRs. What stayed interesting to him: a protocol for talking with foreign agents — ours exists (folder number and slug, `address.md`, a one-way note or pointer, a peer's word never a go, handoff files for volume), scattered across two docs, written for our own heads only. Thought, not task.

**The herald, still open.** No conclusions drawn — he asked, and the answer is no. His thought: a herald as a knowledge base in its own form for any model, possibly an interface like Paperclip, and what `backtest-path.md` became by hand in tradeoxy. My reading: a derived read model over the repository, never authoritative, does not break one home per fact.

**The vocabulary.** He pasted GPT's account of hexagonal vs SOLID and of state machine vs engine. Hexagonal says where to invert, DIP says that you invert; SOLID can hold while the domain stays glued to the ORM. Engine = how to execute, the state machine = what should happen, pluggable policy — GPT's text slipped once and called the engine policy; our ARCHITECTURE.md already names it right (engine = mechanism, philosophy = policy). He realised what he had called SRP was all of SOLID: "оказывается солид — это то, что я называл срп." I mapped each letter to where the family asks it — S the Atomicity Gate, O the polymorphism lens, D the architecture map (phase 73); L and I asked nowhere. His hypothesis: L and I come by themselves, since agents behave as seniors when nothing writes the answer for them; the orchestrator's verify port came out one method with interchangeable implementations, unprompted. He called my paragraph on principles living as questions at their moment "квинтэссенция всего пути скилов и оркестратора. Мы стремимся к тому, что б агенты писали код лучше меня, а не хуже."

**Two docs.** `docs/names-and-reasons-not-laws.md`: what a durable text gives an agent reader — the reader executes; an answer written ahead fails (numbers in specs, checks and fences, maps that forbade, a rule in a buffer that beat a skill); a name, a reason, a question at its moment and a living example work; the harness as a sensor, not a regulator; one test before a sentence enters a durable text. Its reconciliation with `instruction-in-data` is deliberate: an action a file only asks for goes undone, what a text states as the shape of the work is built in. `docs/philosophy/principles-at-their-moment.md`: the aim, then each principle with where and when the family asks it, what is not asked (L, I), and where a question stops short (a seam cut is not a cut whole). He moved it to philosophy ("принципам как будто бы место в философии"); the editor translated it to match the Russian neighbours, and he reversed that: "зря на русский перевёл. пусть англ будет." Two corrections of mine in it: the L/I example is the orchestrator's verify port, not the broker's time port (the user wrote that by hand), and the port is designed, not built — I checked the code.

**sakshi is isolated.** His ruling, now in the buffer: our docs name no side project; a head's contacts elsewhere are help given, not sources to cite.

**One home per fact, aligned.** The global stated it twice (§ "Project CLAUDE.md authoring", § "Documentation style") while the final `reserved-words.md` points to § "Grounding claims". I argued the registry was right — a fact in two places leaves nothing single to ground on — and the global was ours to change. Now stated once in § "Grounding claims"; he asked why "Anything stated in two places will drift." had gone — its meaning had survived as "the copies drift" — and I put the exact sentence back: the short formula is the name people remember.

## What the hand knows

`acc89e764a95dcebe`, alive and current on all of the above; it holds the English principles text it restored. It flags its own judgment calls well; twice this stretch it stated something from my brief as fact without checking (the time port, the port being built) — ask it to verify a claim it did not read.

## What will slip first

- Translating or moving by a general rule when the user has a preference: ask before translating a doc.
- Overstating a conflict from a thought experiment; he reads it against ordinary practice.
- Writing forming thoughts into the buffer.

## What must not be resolved by inference

- The herald, the foreign-agent protocol, waking heads, Paperclip: thoughts, not direction.
- The chain-only-adds deferral: its trigger fired (77 after 39); he has not ruled.
- The lens-integrity candidate: waits for a second instance or his word.

## Next

Nothing queued for this head. When the orchestrator lands 73: run the new `aif-architecture` live on a real project. Watch broker 13.2.2. Phase 76 decomposes when he says. Commit only on his word.
