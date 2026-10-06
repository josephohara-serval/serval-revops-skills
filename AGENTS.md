# Repository Guidelines

## Project Structure & Module Organization

This repository stores shared RevOps skills, rather than an application. `README.md` lists available skills and installation instructions.

Each skill lives in `skills/<skill-name>/`:

- `SKILL.md`: YAML frontmatter and task instructions.
- `agents/openai.yaml`: Codex display metadata and default prompt.
- `references/`: supporting guidance and source references.
- `assets/`: bundled logos, fonts, and license notices.

The current skill is `revops-standard-ui`. Add optional scripts inside the skill that uses them. Keep the full skill folder together when distributing it.

## Build, Test, and Development Commands

There is no build system, package manifest, or local development server. Install the current skill from the repository root:

```sh
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/revops-standard-ui "${CODEX_HOME:-$HOME/.codex}/skills/"
```

For updates, follow the replacement instructions in `README.md`. Start a new Codex chat if the installed skill is unavailable.

Run `git diff --check` to detect whitespace errors. Use `git status --short` to confirm which files will enter the change, including new files.

## Coding Style & Naming Conventions

Use lowercase, hyphen-separated skill names, such as `revops-standard-ui`. Match the frontmatter `name` to the folder name. Include a task-specific `description`.

Use Markdown headings, short instructions, and relative links within each skill. Use two spaces for YAML indentation. Keep detailed guidance in `references/`. No formatter or linter is configured.

For UI skill changes, read `references/serval-design.md` and `references/design-sources.md`. Keep design rules in their existing reference files.

## Testing Guidelines

No automated test framework or coverage threshold is configured. Check frontmatter, metadata, relative links, and bundled asset paths after edits. Exercise changed skill instructions with a representative request in Codex.

For HTML output, verify data, controls, keyboard access, narrow layouts, reduced motion, and console errors. Report checks that remain unverified.

## Commit & Pull Request Guidelines

Git history contains only `Initial commit`; no commit convention is established. Use short, imperative subjects that identify the changed skill or document.

In pull requests, describe the purpose, changed behavior, and validation performed. Link relevant issues. Include screenshots when a change affects generated UI appearance.

## Security & Agent Instructions

Keep team data and credentials out of the repository. Preserve asset licenses and required source attribution.

Use short, active sentences in explanations. Aim for ASD-STE100 controlled English. Use Mermaid when a diagram helps. Keep HTML explanations local. Create explainer videos only when explicitly requested.
