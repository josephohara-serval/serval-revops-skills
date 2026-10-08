# Check Gmail and Notion setup

Run this mode for `Use nda-review to check my setup`. Optionally accept `Check my setup with this Terrain portal page: <URL>`. Run the relevant checks automatically before submission or monitoring as well. An explicit setup check returns a readiness report and ends; it does not continue into submission or scheduling.

Use real, minimal read-only calls in the current host. A listed plugin or tool is not proof of authentication. A successful identity read is not proof of access to a particular review page. Reuse successful checks in the same session unless the account, host, connection, or permissions change. Do not ask for an NDA or a Notion URL before running account checks that do not need one.

## 1. Discover the connections

Inspect the available Gmail and Notion plugin, connector, or MCP tools and their schemas. In a standalone setup check, also inspect the host's scheduler controls to report full workflow readiness. For automatic checks inside another task, inspect only capabilities needed by that task; a submission-only task does not need a scheduler. Report a missing connection as missing; report an installed but unavailable connection separately.

For a missing plugin or expired login, give the host's supported connect/reconnect action or link when available. The user completes interactive login and consent. Do not request passwords, tokens, or session cookies. Do not install plugins, switch accounts, change permissions, send mail, create drafts/comments, or create test schedules during a check. If the user separately requests a setup change, act within that request and the host's permissions.

## 2. Check Gmail

1. Read the connected Gmail account's current profile/identity. Report its email address and whether it matches the invoking user's intended sending account. Do not hardcode a user or infer identity from an email display name alone. When intent is ambiguous, report the connected address and the unresolved sender choice rather than passing the sender check.
2. Make a bounded read-only mailbox search, preferably returning at most one message ID or metadata record. Use agreement names/title and the submission time when available; otherwise a small recent-mail query is sufficient. Verify that search can discover messages outside a supplied review thread, including already-read and archived mail. A thread read alone does not establish this capability. Inspect full-message/HTML-link retrieval and pagination support as well, because Notion notifications may carry the review link only in HTML. Do not print unrelated message contents. A successful empty result verifies that the query works; it is not an authentication failure or proof of actual handoff discovery. Full thread, HTML-link, and attachment access remain untested unless exercised on a relevant item. During active monitoring, use both discovery paths in [review monitoring](review-monitoring.md); the one-result setup probe does not replace them.
3. Inspect whether attachment-capable sending and sent-message readback tools are exposed and whether their permissions can be read without mutation. Report `available, send not exercised` when only capability is known. Do not send a test email or save a draft to prove write access.

4. Inspect whether the connection supports marking a thread as read (or removing only `UNREAD` from its messages) and reading back that state. Report capability availability separately from execution. Do not change read state or any labels during a setup check; mark the actual mutation `NOT TESTED` unless already verified during an authorized monitoring run. Missing mark-read permission affects that step, not otherwise available review reading.

On an authentication error, mark Gmail blocked and give the reconnect step. A different connected account is a sender mismatch, not a passing check. Preserve the requested sender; never silently use the account that happens to work.

## 3. Check Notion and the Terrain portal

1. Read the current Notion user/session identity and workspace identity when exposed. Prefer a current-user lookup over listing workspace members. Report only the identity actually returned; some connectors authenticate as an integration rather than a person. A bot identity does not establish the invoking user's personal login.
2. Inspect the live connection's page-fetch and comment/discussion permissions or tool-access map when available. Respect parameter restrictions. A metadata response alone establishes capabilities, not that private page/comment access works.
3. If a Terrain review URL was supplied by the user or already belongs to the active review, fetch that exact page and verify its NDA context. Read its relevant discussions, including inline/block and resolved history when permitted. Follow pagination and inspect truncation or unavailable-content indicators. A successful complete empty comments response is valid; a denied or omitted discussion response is not evidence of no comments. Inspect the relevant response's attachment and link fields. When a response file is available, make a bounded read-only retrieval or verify access to its exact source link; distinguish actual file access from a login page or metadata-only result. Do not browse unrelated files or create public links to prove access. Without a response file, mark file retrieval `NOT TESTED`; page and comment access alone do not pass it.
4. If no Terrain URL is available yet, finish the account/capability checks and mark portal access `NOT TESTED — no Terrain review link yet`. Do not browse unrelated Notion pages as a substitute or block the initial Gmail submission solely because the portal link has not arrived.

Terrain's client portal may be in a different workspace from the user's connected Notion workspace. A successful Notion login does not establish access to that external page. Distinguish a login failure from a page-sharing or comment-permission failure. An authenticated browser can be checked when available and authorized; identify it as a browser fallback and do not label the plugin itself working because the browser succeeded. A public page fetch does not prove authenticated discussion access.

## 4. Check monitoring availability without starting it

Inspect whether the host can schedule future runs, retain private context, access the same connections in those runs, update the active source, enforce a timezone-aware 08:00–17:00 America/Los_Angeles window, retain the next 08:00 wake across an overnight pause, and stop the schedule on terminal outcomes. Distinguish overnight pause/resume support from terminal cancellation; verify available timezone and daylight-saving controls without creating a test schedule. A foreground loop is insufficient for durable monitoring. Exposed scheduler controls establish availability, not successful scheduled execution. Do not create a test task, heartbeat, or daemon in setup-check mode.

## 5. Return a short report and the next action

Use `PASS` for an operation that succeeded, `BLOCKED` for a required capability that failed or is missing, and `NOT TESTED` for something not exercised. Separate rows when one component has mixed evidence. Include the check time and current host.

| Check | Status | Evidence or next action |
| --- | --- | --- |
| Gmail login and sender | PASS / BLOCKED / NOT TESTED | Actual account and any sender ambiguity. |
| Gmail mailbox search across threads | PASS / BLOCKED / NOT TESTED | Successful bounded search, even if empty; read/archived mail is not excluded. |
| Gmail thread and full-message/HTML-link access | PASS / BLOCKED / NOT TESTED | Actual relevant reads when available; capability inspection alone is not a verified handoff. |
| Gmail mark-thread-read | PASS / BLOCKED / NOT TESTED | Read-state capability and any prior authorized execution evidence; no mutation in setup-check mode. |
| Gmail attachment send/readback | PASS / BLOCKED / NOT TESTED | Tool/permission availability; actual sending is not exercised by this mode. |
| Notion login | PASS / BLOCKED / NOT TESTED | Actual user or integration; workspace only if returned. |
| Terrain page and discussions | PASS / BLOCKED / NOT TESTED | Exact tested review URL, access limitation, or no link yet. |
| Terrain response files | PASS / BLOCKED / NOT TESTED | Exact response file retrieved or accessible link verified; identify untested formats, denied files, or no response file yet. |
| Background monitoring | PASS / BLOCKED / NOT TESTED | Available controls and execution limits; no schedule was created. |

Describe readiness by step: account checks passed, submission capability available but unexercised, portal handoff verified or still pending, response-file access tested or untested, and background scheduling available but unexercised. Untested Terrain file access does not block initial submission before a portal link exists; a later file failure must be reported with the response rather than keeping monitoring active. Do not compress partial evidence into "everything works" or claim logged-in status across untested platforms. Give one concrete fix for each blocker. Retry the affected checks after the user completes a login/access change; do not loop on an unchanged failure.
