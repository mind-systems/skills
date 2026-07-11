# State B: Split Existing README into the resolved docs directory

#### 2.1: Analyze README structure

Read README.md and identify:
- Which sections should stay (landing page content)
- Which sections should move to the resolved docs directory (detailed content)

**Stays in README:**
- Title, tagline, badges
- "Why?" / key features bullet list
- Quick install (1-3 commands)
- Brief example
- Pointer line to the docs directory
- External links, license

**Moves to the resolved docs directory:**
- Detailed setup instructions → `getting-started.md`
- Architecture / project structure → `architecture.md`
- Full API reference → `api.md`
- Configuration details → `configuration.md`
- Contributing guidelines → `contributing.md`
- Any section longer than ~30 lines that covers a single topic

#### 2.2: Propose changes to user

```
Your README.md is [N] lines. I suggest splitting it:

README.md (~100 lines) — keep as landing page:
  ✓ Title + tagline
  ✓ Key features
  ✓ Quick install
  ✓ Example
  ✓ Pointer line to docs dir

Move to docs dir:
  → "Installation" section → <resolved docs dir>/getting-started.md
  → "Configuration" section → <resolved docs dir>/configuration.md
  → "API Reference" section → <resolved docs dir>/api.md
  → "Architecture" section → <resolved docs dir>/architecture.md

Proceed?
```

#### 2.3: Execute the split

1. Create the resolved docs directory
2. Create each doc file with content from README
3. Rewrite README as landing page with a pointer line to the docs dir; update the CLAUDE.md Documentation Index — see the body's "Update the CLAUDE.md Documentation Index" section
4. **Verify no content was lost** — every section from old README must exist somewhere
