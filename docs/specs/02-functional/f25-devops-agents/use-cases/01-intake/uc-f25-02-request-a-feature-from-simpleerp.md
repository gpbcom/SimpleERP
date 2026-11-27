🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F25-01 Intake](README.md) › 📝 UC-F25-02 Request a feature from SimpleERP

# 📝 UC-F25-02 Request a feature from SimpleERP

**Status:** ✅ specified

## Summary

The owner or administrator requests a feature with examples.

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Goal

Needs heard.

## Trigger

A need.

## Frequency

Occasional.

## Preconditions

- Signed in.

## Postconditions

- Success: sent.
- Failure: none.

## Main flow

1. Open (S-F25-02).
2. Describe the need.
3. Give examples.
4. Send.

## Alternative flows

- 4a. Custom need: factory offer (UC-F25-16).

## Error flows

- 4e. Send fails: retried.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F25-02 One USER feature, one ticket](../../business-rules/br-f25-02-one-user-feature-one-ticket.md)
- [BR-F25-10 Custom needs go to the feature factory](../../business-rules/br-f25-10-custom-needs-go-to-the-factory.md)

## Entities

- [E-F25-01 Bug or feature request](../../data/e-f25-01-bug-or-feature-request.md)

## Permissions

Owner, administrator.

## Notifications

- Status.

## Audit events

Requests.

## AI involvement

Helps.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F25-02 Request a feature](../../screens/01-intake/s-f25-02-request-a-feature.md)

## Flowchart

See [FL-F25-01 Intake](../../flows/fl-f25-01-intake.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor O as Owner
  participant S as Request a feature
  O->>S: Kanban for purchases
  S-->>O: Received
```

## Acceptance criteria

1. **Given** a need **when** sent **then** received.
2. **Given** custom **when** detected **then** factory offer.
3. **Given** declined later **when** declined **then** public vote.

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

- [UC-F25-05 Study the code and the specs for a feature](../02-feature-requests/uc-f25-05-study-the-code-and-the-specs-for-a-feature.md)
- [UC-F25-24 Vote on declined requests](../05-tell-the-customer/uc-f25-24-vote-on-declined-requests.md)

## Open questions

None.

---

⬅️ [UC-F25-01 Report a bug from SimpleERP](uc-f25-01-report-a-bug-from-simpleerp.md) · ⬆️ [Up](README.md) ·
➡️ [UC-F25-03 Open the USER feature with its ticket](uc-f25-03-open-the-user-feature-with-its-ticket.md)
