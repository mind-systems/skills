# agent-architect: pyramid pass to a lens over the relay model — cut the global-CLAUDE duplication and ceremony

Origin: [handoff 16](../handoffs/16-architect-overspecifies-editor-kills-its-independence.md) (the relay behavior) + a live user finding this session (the skill duplicates global CLAUDE.md and is bloated). One rewrite of one file does both: encode the relay model and diet the skill to a lens.

## Current state

`src/skills/agent-architect/SKILL.md` is 159 lines — a top-level, user-invoked skill that the repo's own pyramid philosophy says should be a **lens** (route + policy, tens of lines), but it reads as an essay. Two faults:

1. **It duplicates global CLAUDE.md.** "Draft from ground truth, never from memory or a description… read the actual files, following their chain of references down to the leaf" (`:69-74`) restates § "Grounding claims" in substance — doctrine every session already carries. The architect inherits it; the skill must not re-home it.
2. **It has only apply-mode work-order guidance, no relay concept** — "every contract and value pinned" / "Pin the values hard" (`:75-88`) is the sole model, so on an analysis target the architect composes a prompt seeded with its own candidate findings and a preliminary verdict, and the editor's confirmation is manufactured echo (handoff 16 §3).

Beyond these, "Why the pairing works" (`:36-43`), "Counterpart" (`:155-159`), and much of the compact/handoff and Output-register prose is ceremony restating the obvious or the frontmatter description.

## Change

Rewrite `agent-architect/SKILL.md` as a **lens** whose spine is the relay model. The whole role compresses to: *you are the architect; you spawn and keep one editor; you relay the user's messages to it and compare its output against your own; you show the user; on the user's go you generate the one apply work-order; then you verify by fact.*

Retain, compressed, only what is load-bearing **and not already global**:
- **Spawn the editor once, message it thereafter** (`Agent` then `SendMessage`) — never a fresh spawn per task; the persistent history is part of its value.
- **Never touch the shared artifacts yourself** — every edit is the editor's hand; your only direct write is your private buffer.
- **The relay model (the new spine):** for any analysis/work target (review, skeleton, decompose, "aim at phase N"), do **not** author a prompt — relay the user's own message to the editor, translated to English, faithful to intent, with no added findings, checklist, verdict, or restated method. The one relay transformation: expand a user-invoked skill to skill-by-reference ("Read `~/.claude/skills/<name>/SKILL.md`, apply with arguments: …") because the editor never received the slash-command. Generate your own prompt in exactly one case — the pinned apply work-order (values, paths, exact strings, guardrails, self-verify commands, "do not commit") — only after the user confirms the edits.
- **Run your own review in parallel; compare, reconcile, show the user** — the editor is never seeded, so agreement is real signal, divergence is the point of the pair.
- **Verify what landed by fact, never by the editor's word** — your own greps/reads against the files.
- **The user rules the forks and owns the commits** — an apply order leaves only on the user's go; never commit without permission.
- One-liners for: the private buffer (`.ai-factory/notes/<NN>-architect-buffer.md`, deferred items), rehydrate-fresh-each-invocation (zero session state), and the register (reason/report to the user in Russian; editor traffic in English).

Cut entirely: the ground-truth/down-to-the-leaf duplication (`:69-74` — global owns it), "Why the pairing works" as a standalone essay (fold its two disciplines into the bullets above), the "Counterpart" section (the description already says the editor is separate), and the ceremonial prose in the compact/handoff and Output-register blocks.

## Files & types

- edit `src/skills/agent-architect/SKILL.md` only — full rewrite to a lens; frontmatter (`name`, `description`, `allowed-tools: … Agent SendMessage`) unchanged.

## Guards

- **The only behavior change is the relay model.** Every retained discipline keeps its meaning, only shorter — this is a compression, not a redesign, except where the relay model replaces the single apply-mode work-order.
- **Do not restate any global CLAUDE.md doctrine** — grounding, ground-truth-over-description, one-home-per-fact. The skill inherits it; a restatement *is* the duplication being removed. This is itself the repo's one-home rule applied to the skill.
- **Lens, not clamp** — tens of lines, ~80 the aspiration, never a hard cap; keep every load-bearing policy, cut only ceremony and duplication.
- **Pyramid rule** (this direction's, mirrored from Phase 1): the rewrite is unverified until a live paired-loop run compares behavior against the pre-rewrite baseline on the unchanged disciplines; the relay model is the one intended divergence.
- `editor.md` untouched — its apply-only description is a separate, optional cleanup, flagged not bundled.

## Verification

- `wc -l src/skills/agent-architect/SKILL.md` → a lens (down from 159), no load-bearing policy lost.
- `grep -ni "ground truth\|down to the leaf\|why the pairing works\|Counterpart" src/skills/agent-architect/SKILL.md` → the global-duplication and ceremony gone.
- The relay model is present and unambiguous: relay the user's message (English) on analysis; expand a user-invoked skill to a path read; generate only the confirmed-apply work-order; compare/reconcile/verify-by-fact retained.
- Live paired-loop dry-run: the editor's analysis prompt equals the relayed user message; the unchanged disciplines (spawn-once, never-edit-shared, verify-by-fact, user-rules-forks) behave as before.
