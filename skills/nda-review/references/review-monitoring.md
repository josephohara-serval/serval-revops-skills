# Track review through signing clearance

The intake recipient remains `serval@in.marko.ai`. The legal-review agent may clear the NDA directly. If it does not approve, a Terrain team member replies with a Notion link to Terrain's client portal. That handoff is sufficient to move tracking to the linked review; do not require a separate agent non-approval message, an email enumerating changes, or another instruction from the user. Verify the target and access first.

## One review, one monitor

Default cadence: five minutes. Default window: three hours from the user's monitoring request, including preparation time if the request covers the full workflow. An explicit duration, deadline, or cadence overrides the default. Resolve relative time using the user's timezone, store an absolute UTC deadline, and show the local cutoff. Never silently extend the window or restart it at the Gmail-to-Notion handoff.

Use the host's supported scheduler. Reuse an existing monitor for the same sender, submission, and agreement version. Store enough private context for a new scheduled session to resume without the original chat. Verify that it has the required account connections and skill instructions. An interactive session loop is not durable background monitoring.

Keep a compact run record in private task storage or supported scheduler context:

| Field | Purpose |
| --- | --- |
| Sender and legal recipient | Prevent account drift. |
| Counterparty, PDF artifact/version/hash | Bind decisions to the reviewed agreement. |
| Sent message/thread IDs, RFC Message-ID, email link | Find the actual review conversation. |
| Current source: Gmail or Notion | Select exactly one active tracking source. |
| Notion page and relevant discussion IDs/links | Resume the legal review after handoff. |
| Review status and outstanding conditions | Separate pending review from approval. |
| Start, absolute deadline, cadence, monitor ID | Preserve schedule and termination. |
| Last processed message/comment IDs and notified events | Avoid missed history and duplicate alerts. |
| Approval author, timestamp, evidence link, approved version | Support a clearance alert. |
| Monitor status and stop reason | Distinguish active, expired, blocked, cancelled, and completed. |

Do not store credentials, full agreement text, or unnecessary correspondence in scheduler prompts. Keep runtime state out of the shared repository. Persist state and notification progress as the host supports; do not claim exactly-once notifications when the scheduler cannot guarantee them.

## Every scheduled run

1. Load the run record and current time before any Gmail or Notion read. If monitoring was stopped or cancelled, perform no review reads. If the deadline has been reached, mark the monitor expired, disable it, and report the unfinished review once.
2. Check that the active source is accessible with the intended account. Before each additional remote review read, recheck the deadline. Access failure or account mismatch stops the monitor and produces one actionable blocker alert.
3. Read new content plus enough earlier context to understand authorship, conditions, and version scope. Follow pagination and inspect completeness indicators. Do not classify a search snippet, truncated page, or partial comment set as a complete decision.
4. Apply the decision rules below. Persist the latest state and processed identifiers. Stay quiet while nothing actionable changes.
5. On a terminal outcome, save the stopped state and disable/cancel the scheduler. Verify the scheduler result. If cancellation fails, report that failure and preserve a stopped-state guard so future runs do no review reads. Do not claim successful cancellation without evidence.

Use a scheduler end time when available as well as the per-run deadline guard. Arrange a supported final cleanup/expiry notification if the scheduler would otherwise expire without a final run. Do not promise exact execution times when the host only offers periodic or session-bound checks.

## Gmail decisions

Match messages using the verified thread ID or reply headers, not subject alone. Exclude the original outbound message. A reply may come from Terrain or the legal-review agent using an address different from the intake inbox; establish that it belongs to this review and identify the actual author. Do not require the sender to equal the intake address, invent a Terrain email domain, or treat quoted old approvals as new decisions.

| Current evidence | Result |
| --- | --- |
| Receipt acknowledgment, queue notice, or "we are reviewing" | Pending. Continue Gmail monitoring. |
| The legal-review agent or a Terrain legal reviewer explicitly approves the applicable version with no outstanding conditions | Cleared. Stop monitoring and issue the clearance alert. |
| Terrain supplies the NDA's Notion client-portal link, whether or not specific changes are described | Follow the handoff procedure below. Do not leave Gmail as the active source once the transfer succeeds. |
| Agent non-approval or changes requested, without a usable portal link | Keep the review pending and continue Gmail monitoring for Terrain's reply within the remaining window. Surface any concrete user action or changes. Do not invent a page or send a request for the link without authorization. |
| Conditional approval, conflicting decisions, or unclear version | Pending. Surface the conditions or ambiguity. Do not announce clearance. |
| Delivery failure | Stop and report failed submission. Do not automatically resend. |

## Handoff to Terrain's Notion client portal

1. Open the Notion client-portal link supplied in Terrain's response. Confirm its counterparty/agreement context matches the submitted review. If the link leads to a general portal, locate the specific linked NDA review before tracking it; do not monitor unrelated client pages. If the link is ambiguous or points to another agreement, keep Gmail as the source and alert the user to the mismatch.
2. Read the page and the relevant discussion, including inline/block comments and resolved discussions that may contain decision history. Page access does not establish comment access. Use the host's comments API or authenticated UI; include pagination and thread replies. A default page-level-only or unresolved-only comments query can omit the legal decision.
3. Establish a baseline of page content, authors, review status, any requested changes, and discussion identifiers. Missing change details do not prevent a handoff to the correct accessible review. Evaluate any approval already present during this baseline; do not wait for another update to recognize it. If the applicable version is already cleared, use the terminal approval procedure immediately. Skip the source transfer and any stale handoff alert.
4. Only after page and discussion access is verified, update the existing monitor's source to Notion. Preserve the Gmail identifiers as provenance, the same deadline, and the review/version identity. Read back the updated schedule/context before claiming the transfer succeeded. Do not leave separate Gmail and Notion monitors running.
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
