# Serval RevOps Skills

Shared skills for the team's daily work and project tasks. Each skill lives in its own folder under `skills/`.

## Available skills

| Skill | Use |
| --- | --- |
| [revops-standard-ui](skills/revops-standard-ui/SKILL.md) | Build a new HTML interface or redesign an existing file. Apply Serval design guidelines. Match the layout to the data. Use uselayouts and transitions.dev for design references. |

## Use in Codex

Clone this repository. From the repository folder, install the skill and its updater:

```sh
serval_codex_dir="${CODEX_HOME:-$HOME/.codex}"
mkdir -p "$serval_codex_dir/skill-sources/serval-revops"
cp skills/revops-standard-ui/scripts/update_installation.py "$serval_codex_dir/skill-sources/serval-revops/update.py"
python3 "$serval_codex_dir/skill-sources/serval-revops/update.py" \
  --repo "$PWD" \
  --destination "$serval_codex_dir/skills/revops-standard-ui" \
  --state "$serval_codex_dir/skill-sources/serval-revops/state.json" \
  --seed
```

Use `--seed` for the first installation only. It installs the local skill before publication. Later updates use the same command without `--seed`. The updater fetches `origin/main` and installs only `skills/revops-standard-ui/` from that commit. It preserves your repository's working files. It also preserves local edits to the installed skill. It checks the remote at most once every seven days. If the remote does not contain the skill, it keeps the installed version.

Codex versions that scan `~/.agents/skills` can use a link to the installed folder:

```sh
mkdir -p "$HOME/.agents/skills"
ln -s "$serval_codex_dir/skills/revops-standard-ui" "$HOME/.agents/skills/revops-standard-ui"
```

Create the link only if that destination is unused. Start a new Codex chat or restart Codex if the skill does not appear.

For automatic updates, schedule a weekly Codex automation that runs the updater without `--seed`. Keep the updater outside the installed skill folder. The update operation reads downloaded files; it does not execute downloaded scripts. The local updater remains fixed until you explicitly replace it. Notify on changes or failures. Stay quiet when the installed files remain unchanged.

Example requests:

```text
Use $revops-standard-ui to redesign ./pipeline.html.
Preserve all records, totals, filters, and links.
```

```text
Use $revops-standard-ui to build ./onboarding.html from ./accounts.csv.
Help the team find blocked accounts and inspect their next steps.
```

The skill reads both design sources when selecting patterns. It creates local HTML output by default. It supports standalone files without a build step. Source access is needed to inspect current patterns. The agent reports any unavailable source or browser checks.

The skill includes [Serval design guidelines](skills/revops-standard-ui/references/serval-design.md), official logo assets, a local Inter font, and its license. The guidelines take priority over the inspiration sources. Keep the full skill folder together when installing or updating it.

## Add a skill

Create `skills/<skill-name>/SKILL.md`. Include YAML frontmatter with `name` and `description`. Put optional references and scripts in the same skill folder. Keep team data and credentials out of the repository.
