🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F20-01 Talk it through](README.md) › 📝 UC-F20-09 Follow the request

# 📝 UC-F20-09 Follow the request

**Status:** ✅ specified

## Summary

The administrator and the owner follow their requests and timeline and reply.

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Goal

Know where things are.

## Trigger

Any time.

## Frequency

Daily.

## Preconditions

- Requests.

## Postconditions

- Success: read.
- Failure: none.

## Main flow

1. They open My requests (S-F20-09).
2. They read the timeline.
3. They reply.
4. The status updates.

## Alternative flows

- 2a. Time left against the targets.

## Error flows

- 1e. None.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F20-02 Plain words first](../../business-rules/br-f20-02-plain-words-first.md)
- [BR-F20-11 Response times per support plan](../../business-rules/br-f20-11-response-times-per-plan.md)

## Entities

- [E-F20-01 Support request](../../data/e-f20-01-support-request.md)
- [E-F20-02 Message](../../data/e-f20-02-message.md)

## Permissions

Own company.

## Notifications

- Status changes.

## Audit events

Replies.

## AI involvement

None.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F20-09 My requests](../../screens/01-talk-it-through/s-f20-09-my-requests.md)

## Flowchart

See [FL-F20-01 Talk it through](../../flows/fl-f20-01-talk-it-through.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor A as Administrator
  participant S as My requests
  A->>S: Open
  S-->>A: 2 open
```

## Acceptance criteria

1. **Given** 2 open **when** opened **then** shown.
2. **Given** a reply **when** sent **then** status updates.
3. **Given** an employee **when** opening **then** own only.

## Non-functional notes

D408's targets ([Performance](../../../../05-non-functional/performance.md)): 95 % of screens within 1 second; lists
paged on the server, the first page within 1 second; reports within 5 seconds or in the background.

## Regulatory references

Support rules of the France country pack:
[CR-FR-199 Notifying a personal data breach](../../../../10-country-packs/france/data-protection/cr-fr-199-personal-data-breach-notification.md),
[CR-FR-169 NIS2 incident notification](../../../../10-country-packs/france/digital/cr-fr-169-nis2-incident-notification.md),
[CR-FR-049 Processors and transfers outside the EU](../../../../10-country-packs/france/data-protection/cr-fr-049-processors-and-transfers.md),
[CR-FR-056 People know they deal with an AI](../../../../10-country-packs/france/ai-and-recording/cr-fr-056-people-know-they-deal-with-an-ai.md),
[CR-FR-057 A person confirms what the AI does](../../../../10-country-packs/france/ai-and-recording/cr-fr-057-human-oversight.md),
[CR-FR-052 Personal data kept no longer than needed](../../../../10-country-packs/france/data-protection/cr-fr-052-storage-limitation.md),
[CR-FR-168 Cyber Resilience Act reporting](../../../../10-country-packs/france/digital/cr-fr-168-cyber-resilience-reporting.md).

## Related use cases

- [UC-F20-01 Report a problem in plain words](uc-f20-01-report-a-problem-in-plain-words.md)

## Open questions

None.

---

⬅️ [UC-F20-08 Escalate to an engineer](../03-incidents/uc-f20-08-escalate-to-an-engineer.md) · ⬆️ [Up](README.md) ·
➡️ [UC-F20-10](../03-incidents/uc-f20-10-handle-a-wide-incident-with-a-status-page.md)
