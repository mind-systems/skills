# Handoff — the architect's snapshot is a history, not a telegram

**Processed:** `[ ]` — whoever reads this marks it; a marked handoff is spent.

This file holds one proposed change to `agent-architect`: the memory snapshot the architect writes before a compact must carry the history of the stretch it covers, in causal order, with the reason for each turn — and it must be written by the architect's own hand, never delegated. The change is narrow in scope but the reasoning behind it runs deep, and it grew out of a failure that happened in this same session: the architect wrote a snapshot, the user rejected it, and named what he wanted instead.

Today the skill describes the snapshot file in one paragraph, and the description invites exactly the failure that occurred. It says the snapshot records the buffer's path and a digest of what the editor has accumulated, and carries "only the volatile residue — where the work stands, what the hand knows, what will slip first, and what must not be resolved by inference — because everything durable already lives outside the conversation; never an inventory of the session." Every clause of that sentence is true, and a file written in strict obedience to it can still be useless. An architect that follows the wording literally writes forty lines of status and satisfies every word of the rule. That happened this session. The state the snapshot restates was never the problem — the state lives on in the roadmap, the specs, and the buffer itself, all of which survive a compact untouched. What does not survive is *why*: why one option was taken over another, which premise turned out false and how it was proved false, which correction came from the user and in what words. Decisions live in artifacts; reasons live only in the conversation, and the conversation is precisely what the compact destroys. A successor architect that inherits the decisions without the reasons re-litigates them from scratch — that is the mechanism, observed directly in this session rather than argued abstractly, and it is the reason the thin form fails even when it is followed to the letter.

A second reason surfaced alongside the first, and it belongs to the user rather than to any prior skill reasoning. The series of snapshots, taken together, is the only record of the architect's life. Git shows what changed; the specs show what was decided; nothing else shows how the pair actually moved — what it tried, where it went wrong, what corrected it. The user asked, in this session, whether that path could be reconstructed after the fact, and it turned out it could, but only by the roundabout route of tracing the buffer's own file name through git history and then reading whichever handoffs happened to cite it along the way. Wherever a snapshot had been written thin, that stretch of the history was simply gone — not hard to find, but absent. The consequence the user drew from this is the standard the new form has to meet: each snapshot must be readable on its own as the story of its stretch, and the full series, read in order, must reconstruct the whole life of the pair, not merely its current state.

This creates a tension with a rule `agent-architect` already states and that must not be lost in the rewrite. The skill currently says each new snapshot supersedes the last by name, the numerically higher file being the current one, "so a reader never follows a stale next action." That rule is correct and stays — but it needs a sentence added that says exactly what it scopes to, because without that sentence the natural reading is that older snapshots are disposable clutter, and that reading is exactly what makes a history impossible to keep. The scoping sentence is: supersession covers the next action, not the record. An older snapshot remains the history of its own stretch and is never superseded as history; only its closing instruction — the "do this next" — goes stale the moment a newer snapshot exists.

The form to bake into the rewritten paragraph is not a rigid template — the architect still writes prose — but a set of parts that must be present, each named rather than merely implied. First, what the file is, together with a pointer to the project handoff if one was written for the same stretch, since the two are different genres with different readers and a successor must not confuse them. Second, the buffer: its path, and one line describing what it holds — a pointer, never a copy, which is a rule the skill already states and which stays exactly as it is. Third, the hand: what the editor has accumulated across the stretch that the architect itself cannot reconstruct from artifacts alone — the rounds it ran, the proofs it performed, the corrections it made — together with the instruction to ask the editor rather than try to re-derive that history independently; this is the digest the current skill already requires, and the existing rule that it is never sent to the editor stays untouched. Fourth, and the part the current wording omits entirely, the arc: the stretch rendered in the order it actually happened, each turn carrying the reason it was taken and what it changed. This part is prose, it runs long, and it is explicitly not an inventory of files touched — the test for whether it succeeds is whether a reader comes away knowing *why*, never merely *what*. Fifth, the mistakes that bear on the next step: what turned out wrong during this stretch and what corrected it, each named by the symbol or the decision it touched — carried because a successor would otherwise repeat it, not as an account of the architect's own conduct. This is not a confession exercise — it is the cheapest available prevention against making the same mistake twice, and it is the part a thin snapshot drops first, because it is the part hardest to state honestly under the pressure to look finished. Sixth, what will slip first: the reasons most likely to be re-litigated by a successor, each one paired with where its durable text actually lives, so that a fresh architect reads the spec rather than guessing at the reasoning behind it. Seventh, what must not be resolved by inference: the standing rulings that a fresh architect would otherwise be tempted to reopen and re-derive from first principles. Eighth, where reasoning that properly belongs to another repository went, if any arose during the stretch, so that it is not accidentally re-derived a second time in the wrong place. Ninth and last, the next action — which is the one part the supersession rule is actually about, and the only part of the file that a newer snapshot is entitled to render stale.

One rule needs to be stated plainly in the rewrite, because its absence is what actually caused the failure this session produced. The snapshot is written by the architect itself, in its own hand, and it is never delegated to the editor. The current text only forbids sending the *digest* to the editor — it never says the snapshot file itself cannot be delegated wholesale, and that gap is exactly what happened: the architect handed its own recovery note to the hand to write. The hand has neither the conversation nor the reasons behind any of its decisions sitting in its own context; it can only render back what it is explicitly given, which produces exactly the thin, inventory-shaped file the user rejected. The fix is to say it without room for a gap: the project handoff may be delegated to the editor; this file, the architect's own snapshot, may not.

An exemplar already exists, and naming it is cheaper than describing the form a second time in the abstract. `tradeoxy_core`'s own `.ai-factory/handoffs/67-memory-snapshot-before-the-compact.md` was written after the thin snapshot that preceded it was rejected, and it carries all of the parts named above. The file immediately before it in that same directory is the rejected one — the one the current, thin wording of `agent-architect` actually produces when followed correctly.

Two further findings came out of the same investigation, recorded here because they bear on whether a history can be read back at all, even once the form itself is fixed. First, the `Processed:` mark is effectively dead in practice: of the last twenty handoffs in that project, only two carry `[x]`, and rehydration in practice happens through a paste-back pointer instead, which means nobody ever actually returns to flip the mark. Either the mark should be set at the moment the pointer is pasted back, or the mechanism that actually carries "this has been read" should be acknowledged honestly as something other than the mark. Second, the handoffs directory mixes two genres on one shelf: the architect's own snapshots sit alongside outbound handoffs written for readers in sibling repositories, and these are a different kind of artifact with a different lifetime from the snapshots — on a single shelf they are already hard to tell apart by name alone, and the confusion only grows as the count of files climbs.

What the next session does with this: edit `agent-architect`'s snapshot paragraph to carry the nine parts named above, the supersession-scoping sentence, and the no-delegation rule. Leave the buffer's own definition in `architect-editor-engine` untouched — it is not what needs changing here. The two adjacent findings, on the `Processed:` mark and on the mixed-genre directory, are noted for decision rather than for action.

One part of this was not left as a proposal. The explanation of why the `Processed:` mark goes
unset — that an instruction written into the artifact it governs is taken as content rather than as
a command, by the same prior that keeps any file from commanding the run, and that the obligation
therefore has to live in the skill step which touches the artifact — was written up as
`docs/instruction-in-data.md` and indexed in `CLAUDE.md`'s guide table. The mark's own disuse is the
measured case in it. Whoever acts on this handoff can treat that finding as documented and spend
the round on the snapshot's form instead.

A second finding from the same exchange was written up rather than left in the conversation, and it
is the more general of the two. Asked why the mark fails, the architect produced an account of its
own behaviour — and the user's own contrast is what made that account worth anything: the pins
beside the mark, in the same file, honoured every time. An agent's explanation of itself is not a
report from inside; it is the outside view spoken in the first person, and it earns its place only
by explaining a measured discrepancy and predicting something checkable somewhere else. That is
`docs/self-analysis.md`, indexed beside `docs/instruction-in-data.md`, which now carries the
succeeding case next to the failing one. The two docs are the same case seen from two angles —
where an obligation must live, and what an agent's story about its own behaviour is worth.

Three further things belong in the same edit, and the first is a genre confusion the session
demonstrated rather than argued. Asked to write a handoff before a compact, the architect invoked
`command-handoff` and treated its output as its own recovery note; they are not the same artifact
and should not be reachable by the same request. `command-handoff` produces a **project** handoff —
project state, read by whichever agent comes next, grid-shaped, its composition delegated to `note`.
The **memory snapshot** is the architect's own: the reasoning of the stretch, the reasons behind each
turn, read by nobody but the architect after amnesia, written by
hand and never delegated. They share an occasion and a directory and nothing else. `agent-architect`
should name both and say plainly that one is not the other. The user's own habit settles which is
which: when he writes "we continue after the compact, bring the buffer current, write a detailed
handoff of what we did and what came of it", he means the **snapshot** — so that phrasing, however
it arrives, is a request for the architect's own note, and a project handoff is written beside it
only when the project's state has actually moved.

The second is the scope line between the snapshot and the buffer, which the same stretch made
visible: the buffer is the **project's** working memory, shared with the hand, and it moves when the
project's understanding moves; the snapshot is the **architect's** memory, and it moves when the
conversation does. A stretch can move one and leave the other untouched — this one moved only the
snapshot, since the reasoning was about the skill family and left the project's state exactly where
it was. So bringing the buffer current is not an automatic step of writing a snapshot; it is its own
act with its own trigger, and the skill should say so rather than leave the pair to re-derive it
each time.

The third is a **minimal buffer template**, because the pair reinvents the buffer's shape at every
founding and the shape it converges on is always the same. The skill should seed it: a
*where things stand* paragraph, the only part rewritten rather than appended, carrying the live
status and the next action; *settled — rulings in force*, the user's decisions in his own words with
the reason each holds; *settled — method*, what repeated failure taught about how to work; *settled
— orientation*, the confusable pairs and traps of this particular codebase; a *ledger*, append-only,
one entry per task walked, holding what the pass found and what it cost; *rescues*, one entry per
failed task with its root cause and its lesson; *candidates — not tasks*, each with the trigger that
would promote it; and a *live* zone for the architect's own open questions, which the hand never
reads. The handle and any pairing role sit where `architect-editor-engine` already puts them.

That template should be seeded with standing entries, not left empty, and the first of them is the
rule about counts: a durable artifact names a set by its membership rule and never by its size.
That rule has been written by hand into three separate architects' buffers, each time after the
user asked for it, and it has never once arrived on its own — which is the same diagnosis this
handoff already carries about the mark: an obligation with no procedural home does not execute.
It now has one home in documentation, `docs/counts-go-stale.md`, indexed in `CLAUDE.md`; the buffer
template is its second; a skill that writes durable artifacts naming it would be its third.

One structural option was considered and declined, and it is recorded so that a later session does
not re-propose it as new. Both genres share a directory and a numbering, so telling them apart rests
on discipline rather than on structure; giving the snapshots a place of their own — a separate
directory, or a prefix in the name — would make the confusion mechanically impossible. The user
declined it: the existing pair knows where its own files are, and a future architect will make
whatever it needs, so the change buys nothing for the people it would cost. The cost is the reason —
separating the genres now would force a migration of the files already written and of every pointer
that names them, and that migration would land precisely when a task is in flight and someone has to
rehydrate through the new arrangement. The separation stays available; it is not wanted at this
price.

