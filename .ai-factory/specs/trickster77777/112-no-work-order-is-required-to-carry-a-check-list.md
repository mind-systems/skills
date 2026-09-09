# No work-order is required to carry a check list

## Current state (grounded, read fresh)

`src/skills/agent-architect/SKILL.md` lists what an apply work-order must carry: "pin every value, path, and exact string it needs; state the guardrails — what NOT to touch, a collision-safe method where order matters; the commands the editor runs to self-verify before reporting; and an explicit **"do not commit."**" The third of those four is a standing requirement: every work-order carries a block of commands and the numbers they must return.

`src/skills/architect-pairing-engine/SKILL.md` repeats that component twice for the paired half — once where the deciding architect's work-order is described as carrying "the same pinned values, guardrails, self-verify commands, and the explicit 'do not commit'", and once in the single-code-block rule, "every pinned value, guardrail, self-verify command and the 'do not commit' inside it".

`src/agents/editor.md` tells the editor to "run the work-order's own verify commands and read the diff back in apply mode".

Beside all of that, `agent-architect` § "Verify the report by fact" already requires the architect to run its own greps and reads against the real files after every apply round, and to check the reporter's judgment calls on the file rather than on the note.

One session's evidence, across the apply rounds of phases 31 to 34 of this roadmap: the self-verify block caught no defect in any landing — every landing was confirmed separately by the architect's own reads — while seven of its pinned expectations were themselves wrong. Three shapes recurred: a count taken over the whole tree while other files were already modified; a count contradicting a guardrail in the same order, so that it could only pass by breaking one; and a count that cannot return its pinned number by construction, because the check must restate the phrase it checks. The editor flagged each rather than trimming text to match, and each cost a round.

## The change

`agent-architect` drops the self-verify component from the apply work-order's required list. The architect authors no block of counts, and the list names no replacement for it: after this task the editor reads the diff back and reports what it found, and the architect checks the landing against the files itself.

`architect-pairing-engine` loses the same component from both of its enumerations, in lockstep with the above.

`editor.md` states that the editor reads the diff back in apply mode always, and runs a verify command only where the order pins one.

## Blast radius

`architect-editor-engine` says an `APPLY-EDIT` receiver "makes exactly the edits specified, self-verifies, and does not commit". That sentence is unchanged and stays true: reading the diff back is the self-verification it names.

`agent-architect` § "Verify the report by fact" is untouched, and becomes the only check on a landing — which is the check that worked all session.

A sweep for self-verify across every skill, command and agent definition finds it in exactly these four files; nothing else in the family mentions it, and no work-order already written is retracted.
