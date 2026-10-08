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
| Gmail tracking | Can read review threads and search the same mailbox for separate messages since submission, including read/archived Notion notifications; can follow result pages and retrieve complete message bodies and HTML review links. |
| Notion tracking | Can access Terrain's linked client-portal page and full relevant comments, including inline and resolved discussion history. A login to a different Notion workspace or search-only access is insufficient. |
| Durable monitoring | Can schedule a future run with the needed connections, retain private state, and update/stop the schedule. It must enforce the same deadline after a source change. |
| User notification | Can report changes in the originating task or another user-authorized destination. |

Prefer a host's supported connectors or MCP tools, then an authorized browser when suitable. Tools vary across installations. Inspect the current schema instead of copying another platform's tool calls. Read-only mail search is not email sending; page retrieval is not comment retrieval; a chat promise is not a schedule.

For Notion tools that expose these options, fetch the page with discussion markers, then read comments with child-block and resolved-discussion inclusion, or fetch the relevant discussion IDs explicitly. Check truncation and access restrictions. Other integrations may use different options.

Use the host's native scheduler when it meets the capability requirements. In Codex, this can be a thread heartbeat. Other hosts may expose scheduled tasks, routines, or session-only loops; inspect the actual availability and lifetime. Do not replace unavailable background scheduling with an undisclosed foreground loop or a new external service. Report which steps work and which remain blocked.

## Preserve discovery in scheduled prompts

When creating or updating an authorized monitoring schedule, carry forward the stopped-state and deadline guards, run-record path, submission time, agreement discovery terms, and processed identifiers. Explicitly require both Gmail operations on every run while Gmail is active: read the original and verified review threads, and search for separate agreement-related messages, including read/archived Notion mention, comment, and sharing notifications. A prompt that only says to read a thread is incomplete. Follow [Gmail discovery and verification](review-monitoring.md#gmail-discovery-and-verification) for full-message/HTML-link inspection, candidate verification, pagination, and deduplication.

Require verification of the linked NDA page and all relevant discussions before transferring the same monitor to Notion; preserve the original deadline and inspect any approval already present. Once Notion is active, read only that review source. Read back the saved schedule/context to confirm these instructions survived. Updating this skill does not authorize restarting a cancelled or expired monitor.

## Verification before claiming platform support

Check skill discovery and references, then exercise preparation, attachment send/readback, Gmail decisions, Notion handoff/comments, deadline handling, and scheduler cancellation in the target host. Use synthetic material and isolated tests for decision checks. Live emails and scheduled actions require user authorization. A successful run in one host does not prove integrations in the other four.

Include these handoff scenarios when evaluating the monitoring instructions:

| Scenario | Required outcome |
| --- | --- |
| Original thread has non-approval; a separate, already-read Notion notification names the NDA and contains its link only in HTML | Discover the notification, verify the matching page and discussions, then transfer the same monitor with the unchanged deadline. |
| Notification is archived, appears on a later search-results page, or becomes searchable after an earlier check | Discover it without depending on unread/inbox state or advancing past the unprocessed message's timestamp. |
| Unrelated NDA notification, or another agreement with the same parties | Exclude the unrelated result; keep ambiguous versions pending instead of transferring or declaring approval. |
| Same notification is returned on later runs | Preserve any unresolved candidate; do not duplicate a completed handoff or alert. |
| Correct page is accessible but its discussions are denied | Stop with a blocked handoff; do not claim Notion tracking or clearance. |
| Matching page already contains explicit legal approval for the applicable version | Use the terminal approval procedure; do not start another monitor or announce a stale pending handoff. |
| Monitor is cancelled/expired, or has already moved to Notion | Perform no review reads when stopped; while active in Notion, do not resume Gmail discovery. |

Official installation references, checked October 7, 2026:

- [ChatGPT and Codex skills](https://learn.chatgpt.com/docs/build-skills)
- [Cursor skills](https://cursor.com/docs/skills)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Claude skills and upload](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

Recheck official instructions when the host's interface or installation behavior differs.
