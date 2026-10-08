# Serval RevOps Skills

Shared skills for the team's daily work and project tasks. Each skill lives in its own folder under `skills/`.

## Available skills

| Skill | Use |
| --- | --- |
| [revops-standard-ui](skills/revops-standard-ui/SKILL.md) | Build a new HTML interface or redesign an existing file. Apply Serval design guidelines. Match the layout to the data. Use uselayouts and transitions.dev for design references. |
| [nda-review](skills/nda-review/SKILL.md) | Check Gmail and Notion setup, prepare and submit a verified NDA PDF, and monitor until email approval or a Terrain Notion reply, returning the reply and its files. |

## Install revops-standard-ui in Codex

Clone this repository. From the repository folder, install `revops-standard-ui` and its updater:

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

## Use nda-review

Invoke `$nda-review` with an NDA to prepare it, submit it to legal, and track the review without separate send or monitoring confirmation. The skill defaults to `serval@in.marko.ai` as the legal recipient. The sender is the invoking user's verified email account. It accepts an attached PDF or information that lets the agent acquire or generate one. Explicit scope limits such as preparation-only, draft-only, send-only, no-send, no-monitoring, and setup-check override the default.

Default monitoring checks every twenty minutes for one three-hour window measured from the full-workflow invocation, or from a separate monitoring request. While Gmail is active, each run reads the original review thread and searches for separate messages associated with the NDA, including already-read or archived Notion notifications, unless a terminal outcome ends the run first. An email acknowledgment keeps the review pending. Explicit approval by the legal-review agent stops monitoring and produces a signing-clearance alert. Terrain's client-portal link may arrive in a reply, a separate email, or a Notion notification. After the correct agreement, page, and discussion access are verified, tracking moves to that Notion review, even if the email does not list specific changes. A verified, unreported Terrain Legal reply ends monitoring immediately, including a reply already present at handoff. Return the full reply and all files attached to or explicitly supplied with that update, with any retrieval failures identified. Requested changes, questions, conditional approval, and status replies all end Notion scanning; signing clearance still requires explicit legal approval for the applicable version. Monitoring stays stopped until the user requests a new window. The original deadline still applies across the Gmail-to-Notion handoff.

The shared skill supports installation in Codex, ChatGPT Work, Cursor, Claude Code, and Claude Cowork. See [platform setup](skills/nda-review/references/platform-setup.md) for installation routes, packaging, and required integrations. The updater above manages only `revops-standard-ui`; it does not install or update `nda-review`. Keep the complete skill folder together.

Example requests after installing or attaching the skill:

Attach an NDA and invoke `$nda-review` for the full submit-and-track workflow.

```text
Use nda-review to check my setup.
```

This makes live read-only Gmail and Notion login checks and reports what works, what is blocked, and what is still untested. It does not send email or start monitoring. Add a Terrain portal URL to check access to that specific page and its discussions. The relevant checks also run before submission and monitoring; preparation-only requests do not require connected accounts.

```text
Use nda-review to prepare this online NDA as a PDF for legal review: <URL>.
```

```text
Use nda-review to send the attached NDA to legal and monitor the review for three hours.
```

```text
Use nda-review to resume monitoring this Notion legal review for two hours: <Notion URL>.
The original submission is in this email thread: <email link>.
```

Installation does not establish Gmail, Notion, or scheduler access. The agent checks those capabilities for the requested steps and reports any blocker. Private agreements and monitoring state stay outside this repository.

## Add a skill

Create `skills/<skill-name>/SKILL.md`. Include YAML frontmatter with `name` and `description`. Put optional references and scripts in the same skill folder. Keep team data and credentials out of the repository.
