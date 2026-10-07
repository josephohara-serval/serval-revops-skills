# Platform setup and capability checks

The same `nda-review` folder supplies the workflow in Codex, ChatGPT Work, Cursor, Claude Code, and Claude Cowork. Keep its references with `SKILL.md`. `agents/openai.yaml` is optional OpenAI display metadata; the workflow does not depend on it. Platform installation, connected accounts, and scheduling must be verified separately.

After installation, say **Use nda-review to check my setup**. The [setup check](setup-check.md) makes live read-only account checks and reports Gmail, Notion, Terrain portal access, and scheduling readiness. No agreement is required. Supply a Terrain review URL when available to test that page and its discussions.

## Install the shared skill

| Host | Installation route |
| --- | --- |
| Codex | Copy the complete folder to a supported user or project skill directory, such as `~/.agents/skills/nda-review/`. Check skill discovery in a fresh session. |
| ChatGPT Work | Use the desktop skill mechanism, or bundle the folder in a ChatGPT plugin for distribution to Work on other surfaces. A folder in this repository alone is not an installed Work plugin. Follow the host's current skill/plugin UI and workspace policy. |
| Cursor | Copy the folder to `.cursor/skills/nda-review/` in the target project or `~/.cursor/skills/nda-review/` for that user. Verify discovery; local user skills are not automatically available to every remote worker. |
| Claude Code | Copy the folder to `.claude/skills/nda-review/` in the target project or `~/.claude/skills/nda-review/` for that user, or use an enabled skill/plugin installation. |
| Claude Cowork | ZIP the complete `nda-review` folder, upload it through Customize > Skills, and enable it for the user's Claude account. Verify it is available in the Cowork session; a Claude Code local directory alone is insufficient. |

Do not overwrite an existing customized installation. Inspect and update it deliberately. This repository's current managed updater targets `revops-standard-ui` only; do not use it to install or update `nda-review`.

From the repository root, create a distribution ZIP outside the repository:

```sh
nda_package_dir="$(mktemp -d)"
(cd skills && zip -r "$nda_package_dir/nda-review.zip" nda-review -x '*/.DS_Store' '*/__pycache__/*')
```

Upload/install only when requested. Do not include run records, source agreements, passwords, or mail attachments in the package.

## Map capabilities before promising the full workflow

| Capability | Required evidence |
| --- | --- |
| PDF preparation | Can read supplied files, acquire authorized sources, compare text, and inspect rendered pages. Use available libraries or native export. |
| Invoking user's email | Can inspect the current account identity, send a real PDF attachment, and read the sent message back. |
| Gmail tracking | Can read complete messages and reply/thread identifiers in the same user's mailbox. |
| Notion tracking | Can access Terrain's linked client-portal page and full relevant comments, including inline and resolved discussion history. A login to a different Notion workspace or search-only access is insufficient. |
| Durable monitoring | Can schedule a future run with the needed connections, retain private state, and update/stop the schedule. It must enforce the same deadline after a source change. |
| User notification | Can report changes in the originating task or another user-authorized destination. |

Prefer a host's supported connectors or MCP tools, then an authorized browser when suitable. Tools vary across installations. Inspect the current schema instead of copying another platform's tool calls. Read-only mail search is not email sending; page retrieval is not comment retrieval; a chat promise is not a schedule.

For Notion tools that expose these options, fetch the page with discussion markers, then read comments with child-block and resolved-discussion inclusion, or fetch the relevant discussion IDs explicitly. Check truncation and access restrictions. Other integrations may use different options.

Use the host's native scheduler when it meets the capability requirements. In Codex, this can be a thread heartbeat. Other hosts may expose scheduled tasks, routines, or session-only loops; inspect the actual availability and lifetime. Do not replace unavailable background scheduling with an undisclosed foreground loop or a new external service. Report which steps work and which remain blocked.

## Verification before claiming platform support

Check skill discovery and references, then exercise preparation, attachment send/readback, Gmail decisions, Notion handoff/comments, deadline handling, and scheduler cancellation in the target host. Use synthetic material and isolated tests for decision checks. Live emails and scheduled actions require user authorization. A successful run in one host does not prove integrations in the other four.

Official installation references, checked October 7, 2026:

- [ChatGPT and Codex skills](https://learn.chatgpt.com/docs/build-skills)
- [Cursor skills](https://cursor.com/docs/skills)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Claude skills and upload](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

Recheck official instructions when the host's interface or installation behavior differs.
