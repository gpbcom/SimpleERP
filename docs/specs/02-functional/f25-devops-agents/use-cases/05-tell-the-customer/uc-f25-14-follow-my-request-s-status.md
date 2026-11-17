🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F25-05 Tell the customer](README.md) › 📝 UC-F25-14 Follow my request's status

# 📝 UC-F25-14 Follow my request's status

**Status:** ✅ specified

## Summary

The owner and administrator follow their request's status in plain words.

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Goal

Know.

## Trigger

Any time.

## Frequency

Weekly.

## Preconditions

- Request.

## Postconditions

- Success: read.
- Failure: none.

## Main flow

1. Open (S-F25-14).
2. Read status (BR-F25-09).
3. See the target from triage.
4. Comment.

## Alternative flows

- 2a. Declined: vote (UC-F25-24).

## Error flows

- 1e. None.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F25-09 The customer is told in plain words](../../business-rules/br-f25-09-customer-told-in-plain-words.md)
- [BR-F25-14 Triage with severity, priority and target times](../../business-rules/br-f25-14-triage-with-severity-priority-and-target-times.md)

## Entities

- [E-F25-01 Bug or feature request](../../data/e-f25-01-bug-or-feature-request.md)
- [E-F25-09 Request status](../../data/e-f25-09-request-status.md)
- [E-F25-11 Triage](../../data/e-f25-11-triage.md)

## Permissions

Own company.

## Notifications

- Status.

## Audit events

Comments.

## AI involvement

None.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F25-14 My requests](../../screens/05-tell-the-customer/s-f25-14-my-requests.md)

## Flowchart

See [FL-F25-05 Tell the customer](../../flows/fl-f25-05-tell-the-customer.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor O as Owner
  participant S as My requests
  O->>S: Open
  S-->>O: Planned for 3.5
```

## Acceptance criteria

1. **Given** planned **when** read **then** release shown.
2. **Given** declined **when** read **then** reason and vote.
3. **Given** a comment **when** sent **then** added.

## Non-functional notes

D408's targets ([Performance](../../../../05-non-functional/performance.md)): 95 % of screens within 1 second; lists
paged on the server, the first page within 1 second; reports within 5 seconds or in the background.

## Regulatory references

Rules of the France country pack the agents follow:
[CR-FR-049 Processors and transfers outside the EU](../../../../10-country-packs/france/data-protection/cr-fr-049-processors-and-transfers.md),
[CR-FR-199 Notifying a personal data breach](../../../../10-country-packs/france/data-protection/cr-fr-199-personal-data-breach-notification.md),
[CR-FR-056 People know they deal with an AI](../../../../10-country-packs/france/ai-and-recording/cr-fr-056-people-know-they-deal-with-an-ai.md),
[CR-FR-057 A person confirms what the AI does](../../../../10-country-packs/france/ai-and-recording/cr-fr-057-human-oversight.md),
[CR-FR-168 Cyber Resilience Act reporting](../../../../10-country-packs/france/digital/cr-fr-168-cyber-resilience-reporting.md),
[CR-FR-052 Personal data kept no longer than needed](../../../../10-country-packs/france/data-protection/cr-fr-052-storage-limitation.md).

## Related use cases

- [UC-F25-24 Vote on declined requests](uc-f25-24-vote-on-declined-requests.md)

## Open questions

None.

---

⬅️ [UC-F25-13 Ask the agents for changes](../04-approve-and-govern/uc-f25-13-ask-the-agents-for-changes.md) ·
⬆️ [Up](README.md) · ➡️ [UC-F25-15 Be told when it ships](uc-f25-15-be-told-when-it-ships.md)
