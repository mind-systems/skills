# HTML Build Mechanics (--web flag)

#### 3.1: Create docs-html/ directory

```bash
mkdir -p docs-html
```

#### 3.2: Generate HTML files

For each markdown file (README.md + `<resolved docs dir>/*.md`), generate an HTML version:

Read the HTML template from `templates/html-template.html` and use it for each page.
Customize: `{page_title}`, `{project_name}`, `{nav_links}`, `{content}`.

#### 3.3: Convert markdown to HTML

For each doc file: parse markdown → convert to HTML elements → fix `.md` links to `.html` → generate nav bar → write to `docs-html/`.

File mapping: `README.md` → `index.html`, `<resolved docs dir>/*.md` → `*.html`.

#### 3.4: Output result

Show tree of generated files and `open docs-html/index.html` hint.
