# Handoff — the roadmap family's canonical example email is a real-looking address, not a placeholder

> Cleanup/discussion handoff. Surfaced from an orchestrator session: a developer's actual git identity (`trickster77777@gmail.com`) differed from the example email baked into the skills, and they asked "where did `kg.wmservice@gmail.com` come from — it's not mine."

## The issue

The roadmap family documents slug derivation with a concrete example: `kg.wmservice@gmail.com → kg-wmservice`. `kg.wmservice@gmail.com` is a **real-looking Gmail address, not a neutral placeholder** (like `john.doe@example.com`). It reads as someone's personal address, and it has propagated as THE canonical example across the family — and downstream into consumer repos (the orchestrator's docs/tests/config-example, now being cleaned there).

## Where it lives in skills (`grep -rInE "kg-wmservice|kg\.wmservice"`, excluding `upstream/`)

- `src/skills/roadmap-engine/SKILL.md:57` — **the origin**: the slug-derivation rule's example.
- `src/skills/orchestrator-artifacts/SKILL.md:28-29` — artifact-layout example.
- `docs/multiuser-roadmaps.md:15,24,47` — governing spec (incl. an `> Owner:` line example).
- `.ai-factory/specs/43-engine-named-roadmap-contract.md:14`, `.ai-factory/specs/48-orchestrator-artifacts-subdir-layout-mirror.md:15` — specs.
- `.ai-factory/ROADMAP.md:79`, `.ai-factory/handoffs/13-…`, `.ai-factory/handoffs/14-…` — roadmap/handoffs (historical).

## Recommendation

Replace `kg.wmservice@gmail.com` → `john.doe@example.com` and `kg-wmservice` → `john-doe`. Prioritize the **live** surfaces that keep the example propagating: `src/skills/roadmap-engine/SKILL.md`, `src/skills/orchestrator-artifacts/SKILL.md`, and `docs/multiuser-roadmaps.md`. Specs/roadmap/handoffs are historical — sweep them too if you want zero occurrences, but the live SKILL.md + docs are what re-seed the example.

Slug derivation is identical (`john.doe` → `john-doe`), so no example loses correctness. Use the `example.com` domain (RFC 2606 reserved) so it is unmistakably a placeholder.

## Scope note

This handoff is only about the **skills** repo (the origin). The orchestrator repo's active docs and `orchestrator.json.example` are already cleaned to `john-doe`; its `tests/test_main.py` and two historical handoffs are being handled on the orchestrator side.
