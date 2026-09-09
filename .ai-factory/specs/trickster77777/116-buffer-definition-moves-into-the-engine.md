# The buffer's definition moves into the engine both halves load

## Current state (grounded, read fresh)

`src/skills/agent-architect/SKILL.md` § "Your buffer is yours alone" (`:220-237`) defines the buffer — its content, its path, its numbering — and closes it to the editor by name: "The editor is never told about it and no work-order references it — nothing is broken if it happens to see the file; it is the one file you edit directly, because it isn't a shared artifact." (`:235-237`).

`src/skills/architect-editor-engine/SKILL.md`'s own `description:` states "Holds only the two formats; when-to-use policy stays with the caller." (`:5-8`), and its body carries exactly two sections — "## The two channel-message formats" and "## The mode rule" (`:19-28`) — no buffer, no mention of shared memory. `docs/paired-loop.md:5` already names this file as the buffer's home: "Its shape and rules live in the engine both halves load at birth."

No settled/live split exists anywhere in `agent-architect`, `editor.md`, `architect-editor-engine`, or `architect-pairing-engine`. The buffer's only stated content, per `agent-architect/SKILL.md:230-232`, is deferral entries: "Each deferral entry names *what*, *why deferred*, and the *trigger* that resolves it... deferral entries remain the buffer's primary content."

`.ai-factory/ARCHITECTURE.md` § "Composition: mechanism vs policy" (`:32-39`) gates a move into a shared skill on carrying "shared content — a mechanism, rule, or format used by two or more callers." Both halves already load `architect-editor-engine` at birth — `agent-architect/SKILL.md:42-45` before the first channel-message, `editor.md:16-21` as the first action on spawn — and under `docs/paired-loop.md`'s model the settled zone is exactly that: content both hold. Nothing in the mechanism/policy rule blocks the move; its own test argues for it.

## The change

`architect-editor-engine` gains the buffer's definition: where it lives (unchanged — `.ai-factory/notes/<NN>-architect-buffer.md`), the two zones and what each holds, which zone the editor holds as its own working context and why the live zone stays with the architect alone (an independent reading would otherwise return an echo of the head's own conclusion), that the editor re-reads the settled zone on change rather than once at birth, and the drain rule — a ruling recorded there is a debt against the skill, erased when it reaches the artifact that should hold it.

`agent-architect` stops defining the buffer itself and points at the engine instead; the sentence closing it to the editor goes with the definition it belonged to, since the editor now holds the settled zone by design.

`architect-editor-engine`'s own `description:` stops claiming it holds only the two channel-message formats.

## Blast radius

Both halves already load the engine at birth, so the definition reaches the editor through an edge that already exists — no new `loads:` entry anywhere, and `editor.md` needs no change to receive it.

The buffer files already on disk are not rewritten; only the skill text defining the buffer's shape moves.
