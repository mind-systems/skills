# Consolidation Targets and Sample Proposal Dialog

**Common files that should move to the resolved docs directory:**

| Root file | Target in docs dir | Merge or move? |
|-----------|-----------------|----------------|
| `CONTRIBUTING.md` | `<resolved docs dir>/contributing.md` | Move |
| `ARCHITECTURE.md` | `<resolved docs dir>/architecture.md` | Move |
| `DEPLOYMENT.md` | `<resolved docs dir>/deployment.md` | Move |
| `SETUP.md` | `<resolved docs dir>/getting-started.md` | Merge (append to existing) |
| `DEVELOPMENT.md` | `<resolved docs dir>/getting-started.md` or `<resolved docs dir>/contributing.md` | Merge |
| `API.md` | `<resolved docs dir>/api.md` | Move |
| `TESTING.md` | `<resolved docs dir>/testing.md` | Move |
| `SECURITY.md` | `<resolved docs dir>/security.md` | Move |

**Files that stay in root** (standard convention):
- `README.md` — always stays
- `CHANGELOG.md` — standard root-level file, keep as-is
- `LICENSE` / `LICENSE.md` — standard root-level file, keep as-is
- `CODE_OF_CONDUCT.md` — standard root-level file, keep as-is

**Sample proposal dialog:**

```
Found [N] markdown files in the project root:

  CONTRIBUTING.md (45 lines) — contribution guidelines
  ARCHITECTURE.md (120 lines) — system architecture overview
  DEPLOYMENT.md (80 lines) — deployment instructions
  SETUP.md (30 lines) — setup guide (overlaps with getting-started)

Suggested actions:
  → Move CONTRIBUTING.md → <resolved docs dir>/contributing.md
  → Move ARCHITECTURE.md → <resolved docs dir>/architecture.md
  → Move DEPLOYMENT.md → <resolved docs dir>/deployment.md
  → Merge SETUP.md into <resolved docs dir>/getting-started.md
```
