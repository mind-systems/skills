# Handoff — memory snapshot: the roadmap turned into execution

You are the same architect, in the same work, interrupted by context and nothing else. This supersedes snapshot 26 — the next action only; 26 stays the record of its own stretch. No processed mark, and none expected.

## Read first, and read it as a warning

`.ai-factory/notes/07-architect-buffer.md` — yours, whole, one memory with no regions. The zone split was removed today, by ruling; if anything still tells you the editor may not read part of it, that text is stale and is being repaired by an open task.

Then the six open contract lines in `.ai-factory/roadmaps/trickster77777.md`. **All six edit the skills you are loaded from.** Until they land, `agent-architect`, `architect-editor-engine`, `command-pin-gaps`, `roadmap-engine`, `roadmap-decompose-skeleton` and `command-handoff` say the old thing on exactly the points the pair is working. You will otherwise obey text that is already decided against. Read the lines, then the skill — not the reverse.

## What happened, in the order it happened

The day opened planning and ended executing. Phases 41–55 existed as headers; five became tasks, and while the pair was still talking the orchestrator ran them. `56.1`, `56.2`, `57.2`, `57.3`, `58.1` landed with no rescue. That is the fact to carry: the pipeline is not fragile. Six tasks, one failure.

The failure is the whole lesson. `58.2` asked for one clause appended to each of two sentences, pinned word for word — and failed three planning rounds. Its spec's invariant predicted that a search would return *exactly one line*, over a paragraph the same task re-wraps. A line-based search cannot honour that. The planner wrote a long deviation negotiating with the number, and each round found a fresh wrong number inside the negotiation. Every finding across all three rounds sat in the checking half of the plan; none ever faulted the change. Rescued at spec+plan depth — the invariant became a property of the text — and it landed first try.

That traced back to us. A pin-gaps pass had run over every spec, ten rounds, one task each, and it had grown the blast-radius sections rather than shrinking them: for a prose task whose replacement text is pinned verbatim there is nothing in the *content* to close, so the only holes a gap pass can find are in the *checking apparatus*, and it closes them by enlarging it. The architect's own standing rule against counts arrived two rounds after the spec that killed the run.

Then the user named the disease above the symptom: the orchestrator already owns planning, integration and review, and we were dragging that responsibility into the task. A task is a ticket. A ticket does not consist mostly of instructions about what not to break. Checked against the prompts rather than argued: the planner's own Step 3 discovers integration points and side effects itself, freshly; neither planner nor reviewer asks a plan to contain verification; the implementer reads the plan alone; the reviewer holds the spec and judges against it. So a spec must say what done looks like and must never say how to check — the reviewer does the checking, and a spec that also verifies hands the implementer a job that is not its own, which a planner then renders as plan tasks.

Two of the user's rulings turned out to have lived only in the buffer for weeks — that a task is not an instruction for reviewing itself, and that a task explains what an artifact must hold, never where to type it. Neither existed in any doc or skill. That absence is what let the apparatus grow unopposed. It is now `docs/what-a-task-carries.md`, written first, with phase 61 created against it: `61.1` puts the blast-radius clause in the indicative, `61.2` states in `roadmap-engine` what the three parts of a spec are *not*.

Alongside, two smaller rulings landed and one campaign closed. The buffer has no zones — the editor reads it whole and never writes to it. The editor is the architect's hand and needs no permission to spawn or respawn; a death is reported in passing. And the census hunt ended: every live spec lost its prediction of a command's output, and `docs/counts-go-stale.md` is its home.

## What the hand knows

`acc89e764a95dcebe`. Three hands ran today; two died. One was killed by `TaskStop` — which is terminal, not a round-cancel, and there is no way to abort a round and keep the hand. One was lost to a network fault mid-round and had already finished its work on disk.

This hand is good at the thing that matters here: it corrected the architect on facts more than once and refused to widen its own scope when it found something outside the order. It caught that five tasks had already been executed while the architect was still reasoning from a stale picture of the roadmap. Ask it to read; never to recall.

## What will slip first

That the skills you load are behind the roadmap. Named above because it is the single most expensive thing to forget.

That a *finding* is not automatically safe. Turning a check into a finding removes the instruction and does nothing about a tally — a finding can be a census. What makes either safe is membership stated as a category that survives a new member arriving.

That a quoted phrase is not a usable search anchor in this repository. The prose wraps at a fixed column, so a multi-word phrase straddles a line break and a single-line search for it silently matches nothing and reads as clean. Met twice in one day.

That `.ai-factory/` is perishable and a document must never cite it. One philosophy doc was found pointing at two task specs that a prune had already deleted.

## What must not be resolved by inference

Phase 43 is parked twice over and stays parked: its preamble is about the unit of the call, its title promises something about empty results the body never states, and the half that today's evidence speaks to is being fixed by phase 61 instead. Do not decompose it to look useful.

Phase 46 waits on field evidence from a `command-pin-gaps` run in `tradeoxy_core`, not on a ruling. Do not put its two questions to the user again.

Phase 44 the user dislikes; whether it shrinks to a single `test-philosophy` clause or dies is his, unsaid.

The resolver fork behind phase 42 is still unanswered.

## Next

Nothing is in flight. Six tasks are open and ordered: `58.4`, `59.1`, `59.2`, `60.1`, `61.1`, `61.2`. The orchestrator runs them; the pair's job when one fails is the rescue, and the rescue's first question is now a known one — is the failure in the change, or in what the spec asked someone to check.
