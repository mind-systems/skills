# Stack Analysis

## Project-File Scan (Mode 1 Step 1)

Read these files (if they exist):
- `package.json` → Node.js dependencies
- `composer.json` → PHP (Laravel, Symfony)
- `requirements.txt` / `pyproject.toml` → Python
- `go.mod` → Go
- `Cargo.toml` → Rust
- `docker-compose.yml` → Services
- `prisma/schema.prisma` → Database schema
- Directory structure (`src/`, `app/`, `api/`, etc.)

## MCP Detection Table (Mode 1 Step 5)

| Detection | MCP |
|-----------|-----|
| Prisma/PostgreSQL | `postgres` |
| GitHub repo (.git) | `github` |
