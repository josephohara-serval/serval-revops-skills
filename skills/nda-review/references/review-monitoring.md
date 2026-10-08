# Track review through signing clearance

The intake recipient remains `serval@in.marko.ai`. The legal-review agent may clear the NDA directly. Terrain's Notion client-portal link may arrive in the original thread, a separate email, or a Notion mention, comment, or sharing notification. A verified handoff is sufficient to move tracking to the linked review; do not require a reply to the submission, a separate agent non-approval message, an email enumerating changes, or another instruction from the user. Verify the target and access first.

## One review, one monitor

Default cadence: five minutes. Default window: three hours from the skill invocation that authorizes the full workflow, including preparation time, or from a separate monitoring request. A plain invocation with an NDA authorizes monitoring without another confirmation; explicit send-only or no-monitoring requests override that default. An explicit duration, deadline, or cadence overrides the default. Resolve relative time using the user's timezone, store an absolute UTC deadline, and show the local cutoff. Never silently extend the window or restart it at the Gmail-to-Notion handoff.

Use the host's supported scheduler. Reuse an existing monitor for the same sender, submission, and agreement version. Store enough private context for a new scheduled session to resume without the original chat. Follow [scheduled prompt guidance](platform-setup.md#preserve-discovery-in-scheduled-prompts) when writing or updating its instructions so both Gmail discovery paths are preserved. Verify that it has the required account connections and skill instructions. An interactive session loop is not durable background monitoring.

Keep a compact run record in private task storage or supported scheduler context:

| Field | Purpose |
| --- | --- |
| Sender and legal recipient | Prevent account drift. |
| Counterparty, PDF artifact/version/hash | Bind decisions to the reviewed agreement. |
| Sent message/thread IDs, RFC Message-ID, email link | Find the actual review conversation. |
| Submission time, party names, known counterparty aliases, document title | Discover separate handoff messages without assuming they share a thread. |
| Discovery queries, last completed search time, candidate message/thread IDs and disposition | Track mailbox coverage and distinguish rejected, unresolved, and verified candidates. |
| Current source: Gmail or Notion | Select exactly one active tracking source. |
| Notion page and relevant discussion IDs/links | Resume the legal review after handoff. |
| Review status and outstanding conditions | Separate pending review from approval. |
| Start, absolute deadline, cadence, monitor ID | Preserve schedule and termination. |
| Last processed message IDs across all discovered threads, comment IDs, and notified events | Avoid missed history and duplicate alerts. |
| Approval author, timestamp, evidence link, approved version | Support a clearance alert. |
| Monitor status and stop reason | Distinguish active, expired, blocked, cancelled, and completed. |

Do not store credentials, full agreement text, or unnecessary correspondence in scheduler prompts. Keep runtime state out of the shared repository. Persist state and notification progress as the host supports; do not claim exactly-once notifications when the scheduler cannot guarantee them.

## Every scheduled run

1. Load the run record and current time before any Gmail or Notion read. If monitoring was stopped or cancelled, perform no review reads. If the deadline has been reached, mark the monitor expired, disable it, and report the unfinished review once.
2. Check that the active source is accessible with the intended account. Before each additional remote review read, recheck the deadline. Access failure or account mismatch stops the monitor and produces one actionable blocker alert.
3. Read new content plus enough earlier context to understand authorship, conditions, and version scope. While Gmail is active, complete both the thread read and the separate-message search below on every run. Once Notion is active, read only that review page and its relevant discussions. Follow pagination and inspect completeness indicators. Do not classify a search snippet, truncated page, or partial comment set as a complete decision, or report no handoff when mailbox discovery was incomplete.
4. Apply the decision rules below. Persist the latest state and processed identifiers. Stay quiet while nothing actionable changes.
5. On a terminal outcome, save the stopped state and disable/cancel the scheduler. Verify the scheduler result. If cancellation fails, report that failure and preserve a stopped-state guard so future runs do no review reads. Do not claim successful cancellation without evidence.

Use a scheduler end time when available as well as the per-run deadline guard. Arrange a supported final cleanup/expiry notification if the scheduler would otherwise expire without a final run. Do not promise exact execution times when the host only offers periodic or session-bound checks.

## Gmail discovery and verification

Check both paths on every run while Gmail is the active source:

1. Read the original submission thread and any previously verified review threads for replies. Use thread IDs or reply headers to bind those replies to the submission. Exclude the original outbound message as a decision.
2. Search the same mailbox for separate messages received since submission that mention the agreement's party names, known counterparty aliases, or document title. Use alternative names as alternatives, not a requirement that every name appear together. Include Notion mention, comment, and sharing notifications. Do not restrict discovery to the original thread, unread mail, the inbox, or a single sender. Include already-read and archived messages. Revisit the submission-to-present window so late-indexed messages are not lost behind the last check time; use processed message IDs to avoid duplicate work. Follow all result pages, subject to the deadline guard.
3. Read each new candidate message in full, including the HTML part and links when the plain-text part is only a mention or preview. Resolve the review-page link to its destination when a notification uses a redirect; do not follow notification-settings or unsubscribe links. A matching subject, sender, or snippet identifies a candidate, not a verified handoff or approval.
4. For a candidate Notion link, follow the handoff procedure below. Bind a standalone legal decision to the review using its actual author, agreement context, parties, and applicable version; thread membership is useful evidence but is not required for discovery. Do not treat a Notion mention or quoted old approval as a new legal decision. If multiple reviews share the same parties and the version cannot be established, keep the review pending and surface the ambiguity.
5. Record candidate message and thread IDs, evidence links, and their disposition across all discovered threads. Keep unresolved candidates in the run record until resolved; deduplication must not silently discard an unfinished handoff. Record search completion separately from thread-read completion. Report an access failure or incomplete result set instead of claiming that no portal link arrived.

Do not require a sender to equal the intake address or invent a Terrain email domain. A Notion notification may identify the reviewer in its body while the sender is Notion itself. Verify the linked review and authorship rather than rejecting it for having a different sender.

## Gmail decisions

| Current evidence | Result |
| --- | --- |
| Receipt acknowledgment, queue notice, or "we are reviewing" | Pending. Continue Gmail monitoring. |
| The legal-review agent or a Terrain legal reviewer explicitly approves the applicable version with no outstanding conditions | Cleared. Stop monitoring and issue the clearance alert. |
| A reply, separate email, or Notion notification supplies a candidate client-portal link, whether or not specific changes are described | Verify the linked review using the handoff procedure below. Do not leave Gmail as the active source once the transfer succeeds. |
| Agent non-approval or changes requested, without a verified portal handoff | Keep the review pending and continue both Gmail discovery paths within the remaining window. Surface any concrete user action or changes. Do not invent a page or send a request for the link without authorization. |
| Conditional approval, conflicting decisions, or unclear version | Pending. Surface the conditions or ambiguity. Do not announce clearance. |
| Delivery failure | Stop and report failed submission. Do not automatically resend. |

## Handoff to Terrain's Notion client portal

1. Open the candidate Notion client-portal link from the reply, separate email, or Notion notification. Confirm its relationship to the submitted NDA using the parties, agreement context, and available version information. The same parties alone may not distinguish multiple agreements. If the link leads to a general portal, locate the specific linked NDA review before tracking it; do not monitor unrelated client pages. If a purported handoff is ambiguous or points to another agreement, keep Gmail as the source and alert the user to the mismatch. Clearly unrelated search results can be recorded and excluded without an alert.
2. Read the page and the relevant discussion, including inline/block comments and resolved discussions that may contain decision history. Page access does not establish comment access. Use the host's comments API or authenticated UI; include pagination and thread replies. A default page-level-only or unresolved-only comments query can omit the legal decision.
3. Establish a baseline of page content, authors, review status, any requested changes, and discussion identifiers. Missing change details do not prevent a handoff to the correct accessible review. Evaluate any approval already present during this baseline; do not wait for another update to recognize it. If the applicable version is already cleared, use the terminal approval procedure immediately. Skip the source transfer and any stale handoff alert.
4. Only after page and discussion access is verified, update the existing monitor's source to Notion. Preserve both the original submission identifiers and the separate handoff message/thread identifiers as provenance, the same deadline, and the review/version identity. Read back the updated schedule/context before claiming the transfer succeeded. Do not leave separate Gmail and Notion monitors running.
5. Notify the user once that Terrain has moved the review to its Notion client portal. Include the page link, observed review status, any documented changes or needed action, and the unchanged cutoff. Do not invent changes when the email or page only announces further review. If access or the scheduler update fails, record a blocked handoff and stop the monitor with the relevant access/setup requirement; do not claim Notion is being monitored. Use [setup check](setup-check.md) for a targeted diagnosis when requested; an expired or stopped monitor must not run new diagnostic reads automatically.

## Notion decisions

Monitor the linked page and relevant discussions together. Comment additions may not be reliably represented by a page timestamp alone. Inspect discussion history even when the page body appears unchanged. Refresh related discussions when the page indicates a new review thread. Follow a moved review only when its relationship to this agreement is established.

- New requested changes or an action for the user: notify with the responsible reviewer, concise change/action, and evidence link. Continue monitoring within the window; do not post or negotiate.
- Revised terms, resolved comments, suggested edits accepted, an unsigned final file, silence, or a counterparty's acceptance: these alone do not establish legal clearance.
- Explicit Terrain legal approval: establish the reviewer's role from the review context and bind the decision to the applicable version. Preserve stated limitations. If the approved version differs from the submitted PDF, identify and link the approved version; do not label the old PDF cleared.
- Conditional approval stays pending until there is evidence that the conditions are satisfied and legal has cleared the applicable version. A changed document or conflicting subsequent comment prevents an unqualified clearance alert.
- A resolved thread that contains an explicit legal approval can establish clearance; resolution itself cannot. If approval authorship, scope, or completeness cannot be verified, report the uncertainty and keep the review pending.

## Alerts and completion

Clearance alert: `Legal has cleared <counterparty>'s NDA (<approved version>) for signing.` Include the legal reviewer, evidence link, and approved artifact when available. State that monitoring stopped only after verifying cancellation. Never sign, submit an acceptance form, or initiate e-signature as part of this alert.

Expiry alert: state that the monitoring window ended, the last known review status, any outstanding action, and the Gmail or Notion link. Expiry does not mean approval. An explicit user request may resume monitoring with a new deadline, preserving the existing submission and source without resending.

Stop on explicit cancellation or access failure. Notify only on meaningful changes, required action, clearance, expiry, or a blocker. Do not repeat an acknowledgment or unchanged requested-change summary on every run.
