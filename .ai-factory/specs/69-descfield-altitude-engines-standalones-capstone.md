# skill-description-field altitude — engines + standalones, then the whole field (capstone)

Phase 14, task 14.3. Same method and governing spec as [task 14.1](67-descfield-altitude-new-work-flow.md): level `description:` altitude/register to the **field reference** 14.1 records. Two groups here, then a whole-field pass.

**Preconditions.** Runs after phases 9–13 and after 14.1 and 14.2 (it is the capstone — it reads the *entire* manifest, so the other groups must be levelled first). **Re-verify before running.**

## Groups

**Engines** — `note`, `roadmap-engine`, `test-philosophy`, `orchestrator-artifacts`. These share a register of their own ("shared X engine, load-once, holds Y") — level them **even among themselves first**, then check that engine register sits at a comparable altitude to the philosophy skills; the announce-that-you-are-shared voice may legitimately differ in *tone* but not in *grain*.

**Standalones** — `aif`, `aif-architecture`, `detangle`, `temporal-tree`, `observe-logs`. Provisional: this group (with `note`) holds the **terse pole** — `aif` / `note` are one-crisp-line; levelling here is likely **up** toward the reference. `aif-skill-generator` is **excluded** (upstream-pristine symlink into `upstream/ai-factory/`, never edited).

## Capstone — the whole field as one document

After both groups are levelled, read the **entire manifest** — every `description:` across all flows, in the order the harness loads them — as one continuous text. Per-group evenness does not guarantee the whole reads level: two flows can each be internally even yet sit at different altitudes. Confirm one altitude and one register field-wide; fix any residual step between flows against 14.1's reference.

## Guards

- Triggers/routing untouched; no vocabulary; **no topology**; no behavior/information loss.
- Level to 14.1's reference; the capstone's job is field-wide convergence, not a new grain.
- **`aif-skill-generator` never edited** (upstream).
- **"No change" is legal** per group and for the capstone — the field may already read even.
- Re-verify before running.

## Verification

- Engines even among themselves and at the reference grain; standalones at the reference (no terse `aif`/`note` outlier left).
- The full manifest, read end to end, reads as one document at one altitude — no altitude step at a flow boundary.
- Every trigger/keyword byte-identical; every skill still routes; `upstream/` untouched.
