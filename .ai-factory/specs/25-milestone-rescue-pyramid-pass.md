# milestone-rescue: pyramid pass — compress the ceremony, keep every contract table verbatim

## Current state

`src/skills/milestone-rescue/SKILL.md` is the heaviest philosophy top in the package (477 lines). Its load-bearing content is contractual: the artifact-discovery block, depth routing (spec / spec+plan / spec+plan+code / plan-ratified-implementation-absent), the per-variant deleted-file sets, the sidecar `step` closed-set table mirroring `orchestrator/main.py`, the governing-spec read, the Diagnosis Report's narrative register, downstream propagation. Around those contracts sits procedural ceremony — transitional prose, restated protocol the loaded `orchestrator-artifacts` engine already carries, step narration an executor performs unprompted.

## Change

One pyramid pass over the file — a compression, not a redesign:

- **Verbatim-protected (contract text, untouchable):** the sidecar `step` closed-set table; the per-variant deleted-file sets; the artifact-discovery block; the Diagnosis Report register (chronological prose, domain language, zero pipeline vocabulary, standalone root-cause sentence); the governing-spec mandatory read; the "What NOT to do" list.
- **Cut:** anything the `orchestrator-artifacts` engine already states (directory layout, PASS signals, sidecar fields — link, never restate), procedural narration of obvious steps, duplicated rationale prose.
- Two-reader register: rules as intent, contracts pinned exact.

## Guards

- **Behavior-identical** — every diagnosis, rollback, and report a pre-rewrite run would produce, the post-rewrite run produces; the protected blocks land byte-identical.
- `loads:` and frontmatter unchanged; ≤ 500 stays trivially, but the target is meaningful shrinkage of ceremony, not the limit.
- Live baseline before the next phase task: replay the skill on a preserved failed-milestone artifact set (or the most recent real rescue) and compare the Diagnosis Report and rollback actions to the pre-rewrite behavior.

## Verification

- `diff` shows protected blocks byte-identical; removed hunks are ceremony/protocol-restatement only.
- `grep -c` of protocol vocabulary duplicated from `orchestrator-artifacts` → materially reduced.
- Live baseline run: same diagnosis depth, same rollback file set, same report register.
