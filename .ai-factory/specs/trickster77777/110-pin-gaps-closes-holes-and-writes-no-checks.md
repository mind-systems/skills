# `command-pin-gaps` closes holes and writes no checks

## Current state (grounded, read fresh)

`src/commands/command-pin-gaps.md` carries three finding classes: a value hole — an unpinned value, closed by reading the code and pinning the exact one; a meaning hole — an undefined edge or a constraint no document states, closed by writing it from the observed behaviour of the code; a blast-radius hole — what the change breaks elsewhere, closed by a sweep whose enumeration goes into the task spec.

Those three are the three parts a task spec holds, one class per part. The command never says so.

Its mandate is "Any question that would need an answer during implementation is space for the agent to fantasize. Close all of it now." It carries no stopping rule and no statement of what it does not produce. Verification is not among its three classes, and nothing in the command forbids a pass from writing one.

## The change

The command names the three parts as the shape it repairs toward, mapping each to the hole class that closes it: a value hole to what is true now, a meaning hole to what must be true after, a blast-radius hole to what breaks on contact.

The command states what it does not write: it pins values and enumerates breakage, and it never authors a verification check. A check that can only fail where the instruction was ignored describes a loud failure, which `test-philosophy` already says is not written.

The value-hole repair stops writing a position address into the spec. Its instruction today is to pin the exact value with a `file:line` citation; after this task it pins the value and names its source the way `docs/reference-by-name.md` requires — the file, and the name of the thing inside it that holds the value, never a line number, because a spec outlives the numbering it was written against. The scan-mode report line is untouched: it is printed to chat and thrown away, which is the exemption that document itself grants a work-order.

## Blast radius

The three hole classes, both modes and the owner-routing to `roadmap-decompose`, `aif-docs` and `test-philosophy` all survive; this task adds no class and removes none. What changes inside them is one clause of the value-hole repair, and the scan-mode report line is not touched.

`command-pin-gaps` declares `loads: roadmap-engine`, so the shape it names has one home there and is not restated in the command.
