# Using the language — where it binds, where it is only vocabulary

Two companion docs precede this one: [reserved-words](reserved-words.md) is the lexicon — the words and their meanings; [skill-description-field](skill-description-field.md) is how the language loads as always-present context. This one is **where the language applies** — the discipline that keeps a real contract from curdling into style-policing.

The reserved-words language is a **contract on the product we author**, not a purity rule over every text the system touches. It answers three questions: what conforms, what does not, and the one rule that keeps the two apart.

## What conforms

The language binds what we ship and what is always loaded as the system's own contract:

- **skill bodies** — every `SKILL.md`, the executable instructions themselves.
- **skill-descriptions** — the `description:` fields, read as one always-loaded [skill-description-field](skill-description-field.md).
- **the docs that specify the system** — [reserved-words](reserved-words.md), [skill-description-field](skill-description-field.md), this file, the philosophy docs, and the discipline in the global CLAUDE.md.

Here conformance is real: sweep the vocabulary, hold one word to one meaning, verify. Drift here is drift in the product — read on every run.

## What does not conform

Ordinary language — written once, read in context, never part of the shipped contract:

- **runtime artifacts the pipeline produces** — plans, plan-reviews, reviews. The orchestrator writes these while working; they are working communication, not a surface of the language.
- **the free prose inside an individual roadmap or task-spec** — a contract-line or a spec is authored per task and read by whoever picks it up; draw on the vocabulary where it sharpens, never scrub the sentence around it.
- **what the system reads** — user input is mapped by context, never conformed. A user types "milestone"; the agent understands.

The vocabulary is *available* in all of these to make them precise. It is never a constraint imposed on them.

## The one rule

**A reserved word fixes a concept's meaning; it does not restrict where the word may appear.**

`phase` means the same thing wherever the concept of a phase comes up — so writing "phase" in a plan is correct, not a violation. Refusing to write "phase" in a plan because "phase belongs to the roadmap" is the mistake: it confuses *this word names a roadmap structure* with *this word may only be typed in a roadmap*. A stable name exists precisely so the concept can be named wherever it appears. Banning the word from working text defeats its purpose and buys nothing.

## Protocol tokens are a different axis

A string a program **scans or emits** — the review heading `## Deferred observations`, the entry line `- Affects: …`, the PASS-signal literals `PLAN_REVIEW_PASS` / `REVIEW_PASS`, the on-disk `Spec:` tag — is **mechanism, not vocabulary**. It stays byte-identical wherever it is produced and consumed, because code depends on the exact characters. The reserved word (`deferred-observations`, `PASS-signal`) lives in the prose *about* the token; the literal token itself is left alone. Across repos this is a joint contract: a token the orchestrator emits and a skill scans changes only in lockstep, or not at all.
