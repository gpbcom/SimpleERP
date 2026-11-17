🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F20-03 Incidents](README.md) › 📝 UC-F20-11 Warn before customers notice

# 📝 UC-F20-11 Warn before customers notice

**Status:** ✅ specified

## Summary

The hosting engineer detects a problem before customers notice, proposes a fix and tells them.

## Personas

- [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md)

## Goal

Prevent.

## Trigger

Alert.

## Frequency

Weekly.

## Preconditions

- Monitoring.

## Postconditions

- Success: fixed.
- Failure: incident.

## Main flow

1. An alert fires (S-F20-11).
2. A fix is proposed.
3. A maintainer approves (BR-F20-04).
4. The customer is told.

## Alternative flows

- 4a. No visible effect: told after.

## Error flows

- 2e. No fix: incident.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F20-04 Every fix needs a maintainer's yes](../../business-rules/br-f20-04-fixes-need-a-maintainer-yes.md)

## Entities

- [E-F20-07 Service incident](../../data/e-f20-07-service-incident.md)
- [E-F20-06 Fix proposal](../../data/e-f20-06-fix-proposal.md)

## Permissions

Engineer.

## Notifications

- Customer.

## Audit events

Alerts.

## AI involvement

Detection.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F20-11 Proactive alerts](../../screens/03-incidents/s-f20-11-proactive-alerts.md)

## Flowchart

See [FL-F20-03 Incidents](../../flows/fl-f20-03-incidents.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  participant M as Monitoring
  actor E as Engineer
  M-->>E: Disk 85 percent
  E->>M: Expand
```

## Acceptance criteria

1. **Given** disk 85 % **when** alerted **then** fix proposed.
2. **Given** approved **when** applied **then** customer told.
3. **Given** no fix **when** failing **then** incident.

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

- [UC-F20-10 Handle a wide incident with a status page](uc-f20-10-handle-a-wide-incident-with-a-status-page.md)

## Open questions

None.

---

⬅️ [UC-F20-10 Handle a wide incident with a status page](uc-f20-10-handle-a-wide-incident-with-a-status-page.md) ·
⬆️ [Up](README.md) · ➡️ [UC-F20-12](../01-talk-it-through/uc-f20-12-answer-how-to-questions-from-the-documentation.md)
