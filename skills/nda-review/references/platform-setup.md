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
| Terrain response delivery | Can inspect response attachment/link fields, retrieve associated files or verify accessible source links, preserve original formats, and return the full reply and files to the user. Page/comment reads alone do not prove file access. |
| Durable monitoring | Can schedule a future run with the needed connections, retain private state, and update/stop the schedule. It must enforce the same deadline after a source change. |
| User notification | Can report changes in the originating task or another user-authorized destination. |

Prefer a host's supported connectors or MCP tools, then an authorized browser when suitable. Tools vary across installations. Inspect the current schema instead of copying another platform's tool calls. Read-only mail search is not email sending; page retrieval is not comment retrieval; a chat promise is not a schedule.

For Notion tools that expose these options, fetch the page with discussion markers, then read comments with child-block and resolved-discussion inclusion, or fetch the relevant discussion IDs explicitly. Check truncation and access restrictions. Other integrations may use different options.

Use the host's native scheduler when it meets the capability requirements. In Codex, this can be a thread heartbeat. Other hosts may expose scheduled tasks, routines, or session-only loops; inspect the actual availability and lifetime. Do not replace unavailable background scheduling with an undisclosed foreground loop or a new external service. Report which steps work and which remain blocked.

## Preserve discovery in scheduled prompts

When creating or updating an authorized monitoring schedule, carry forward the stopped-state and deadline guards, run-record path, submission time, agreement discovery terms, and processed identifiers. Explicitly require both Gmail operations on every run while Gmail is active: read the original and verified review threads, and search for separate agreement-related messages, including read/archived Notion mention, comment, and sharing notifications. A verified terminal outcome ends scanning early. A prompt that only says to read a thread is incomplete. Follow [Gmail discovery and verification](review-monitoring.md#gmail-discovery-and-verification) for full-message/HTML-link inspection, candidate verification, pagination, and deduplication.

Require verification of the linked NDA page and all relevant discussions before transferring the same monitor to Notion; preserve the original deadline and inspect any unreported Terrain replies already present. A verified Terrain reply, including requested changes, a question, conditional approval, a status reply, or a file-only response, ends monitoring during handoff or later checks. Save the response and stopped state, cancel the scheduler and verify the result, then deliver the full reply and every associated file, identifying any missing material. Keep legal status separate; do not keep scanning until approval. Once Notion is active, read only that review source.

Carry the verified Notion source/page/discussion IDs, response IDs/revisions, file-manifest references, inventory completeness, and delivery status in private run state, including when a reply stops the workflow during handoff. The same invocation can finish targeted inspection of that response's file fields and file retrieval after stopping; later scheduled invocations must exit without review reads or duplicate alerts, even if delivery is partial. An incomplete attachment inventory keeps delivery partial even if every visible file was returned. A user-requested delivery recovery is limited to the recorded response and does not resume scanning. Read back the saved schedule/context to confirm these instructions survived. When changing an existing active monitor under an authorized request, replace any saved instruction to continue until Terrain approval with these response-delivery rules. Updating the skill files alone does not update saved scheduler prompts or authorize restarting a stopped monitor.

## Verification before claiming platform support

Check skill discovery and references, then exercise preparation, attachment send/readback, Gmail decisions, Notion handoff/comments, response-file retrieval and delivery, deadline handling, and scheduler cancellation in the target host. Use synthetic material and isolated tests for decision checks. Live emails and scheduled actions require user authorization. A successful run in one host does not prove integrations in the other four. Report scenario evaluation separately from real Terrain file retrieval, scheduler cancellation, and user-visible delivery.

Include these handoff scenarios when evaluating the monitoring instructions:

| Scenario | Required outcome |
| --- | --- |
| Original thread has non-approval; a separate, already-read Notion notification names the NDA and contains its link only in HTML | Discover the notification, verify the matching page and discussions, then transfer the same monitor with the unchanged deadline. |
| Notification is archived, appears on a later search-results page, or becomes searchable after an earlier check | Discover it without depending on unread/inbox state or advancing past the unprocessed message's timestamp. |
| Unrelated NDA notification, or another agreement with the same parties | Exclude the unrelated result; keep ambiguous versions pending instead of transferring or declaring approval. |
| Same notification is returned on later runs | Preserve any unresolved candidate; do not duplicate a completed handoff or alert. |
| Correct page is accessible but its discussions are denied | Stop with a blocked handoff; do not claim Notion tracking or clearance. |
| Matching page already contains explicit legal approval for the applicable version | Stop and deliver the Terrain reply and its files with the clearance alert; do not start another monitor or announce a stale pending handoff. |
| Matching page already contains an unreported Terrain reply requesting changes and a redlined DOCX | Capture the reply and its file, stop without transferring to a pending Notion monitor, and deliver both. Keep legal status as changes requested. |
| A Terrain reply appears in an inline or resolved discussion while the page timestamp is unchanged | Read the discussion, stop, and deliver the full response and its associated files. |
| Terrain asks a question, gives conditional approval, posts a status acknowledgment, or supplies only an attributed file | Stop and deliver the response/files. None of these requires unconditional approval to end scanning. |
| A Notion notification only says there is a reply, or an unrelated/user-authored comment appears | Retrieve and verify the actual Terrain response before using the response stop path; do not treat the notification or unrelated comment as that response. |
| Several unreported Terrain replies contain an approval followed by a correction or condition | Deliver the relevant sequence and its files, stop scanning, and preserve the current condition instead of announcing unqualified clearance. |
| One response file is inaccessible, or its link expires | Refresh an expired URL from the exact source once; return available material and identify missing files. Keep scanning stopped and delivery partial. |
| Reply text is complete, but attachment fields are omitted or the associated file list is truncated/denied | Stop and deliver the reply and visible files, report the incomplete inventory, and keep delivery partial even if all visible files were delivered. Do not claim no attachments. |
| Reply and file are verified just before the deadline; delivery finishes afterward | Stop discovery at the original deadline and finish delivery of that already verified response without polling again. |
| Cancellation fails after a Terrain response is saved | Deliver the response with the cancellation failure; the stopped-state guard prevents later review reads. |
| A scheduled invocation runs after complete or interrupted response delivery | Perform no review reads or duplicate alert. Keep the recorded delivery progress for user-requested recovery. |
| User requests recovery of a missing attachment or explicitly resumes monitoring | Recovery reads only the recorded response/file; resumption uses a new window, the saved Notion source/submission, and delivered IDs without resending the NDA. |
| A reply stopped the initial handoff, then the user asks to resume after responding to Terrain | Resume the saved verified Notion review directly; do not depend on rediscovering a processed Gmail portal notification. |
| Monitor is cancelled/expired, or has already moved to Notion | Perform no review reads when stopped; while active in Notion, do not resume Gmail discovery. |

Official installation references, checked October 7, 2026:

- [ChatGPT and Codex skills](https://learn.chatgpt.com/docs/build-skills)
- [Cursor skills](https://cursor.com/docs/skills)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Claude skills and upload](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

Recheck official instructions when the host's interface or installation behavior differs.
