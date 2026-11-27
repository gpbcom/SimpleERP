🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F25-05 Tell the customer](README.md) › 📝 UC-F25-16 Offer the feature factory for a custom need

# 📝 UC-F25-16 Offer the feature factory for a custom need

**Status:** ✅ specified

## Summary

A custom need is offered as a feature-factory feature.

## Personas

- [U47 SimpleERP maintainer](../../../../01-users/personas/u47-simpleerp-maintainer.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Goal

Custom needs met.

## Trigger

Custom.

## Frequency

Occasional.

## Preconditions

- Request.

## Postconditions

- Success: offered.
- Failure: declined.

## Main flow

1. Detect (S-F25-16).
2. Offer F19 (BR-F25-10).
3. Customer chooses.
4. Declined request stays public (UC-F25-24).

## Alternative flows

- 3a. Accepts F19.

## Error flows

- 3e. Refuses.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F25-10 Custom needs go to the feature factory](../../business-rules/br-f25-10-custom-needs-go-to-the-factory.md)

## Entities

- [E-F25-01 Bug or feature request](../../data/e-f25-01-bug-or-feature-request.md)

## Permissions

Maintainer; owner.

## Notifications

- Owner.

## Audit events

Offers.

## AI involvement

Detects.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F25-16 Custom offer](../../screens/05-tell-the-customer/s-f25-16-custom-offer.md)

## Flowchart

See [FL-F25-05 Tell the customer](../../flows/fl-f25-05-tell-the-customer.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  participant AG as Agents
  actor O as Owner
  AG-->>O: Feature factory, 300 EUR a month
```

## Acceptance criteria

1. **Given** custom **when** detected **then** offered.
2. **Given** accepted **when** chosen **then** F19.
3. **Given** declined **when** declined **then** public vote.

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

⬅️ [UC-F25-15 Be told when it ships](uc-f25-15-be-told-when-it-ships.md) · ⬆️ [Up](README.md) ·
➡️ [UC-F25-17](../04-approve-and-govern/uc-f25-17-control-the-agents-rights-and-audit.md)
