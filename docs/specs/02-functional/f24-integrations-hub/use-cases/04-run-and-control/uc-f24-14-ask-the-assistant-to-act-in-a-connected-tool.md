🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔌 [F24 Integrations hub](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F24-04 Run and control](README.md) › 📝 UC-F24-14 Ask the AI assistant to act in a connected tool

# 📝 UC-F24-14 Ask the AI assistant to act in a connected tool

**Status:** ✅ specified

## Summary

The owner or sales asks the AI assistant to act in a connected tool; writes are confirmed.

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U03 Sales](../../../../01-users/personas/u03-sales.md)

## Goal

Act by asking.

## Trigger

Request.

## Frequency

Daily.

## Preconditions

- Connections.

## Postconditions

- Success: done.
- Failure: refused.

## Main flow

1. Ask (S-F24-14).
2. Proposed action shown with the tool's icon.
3. Confirm (BR-F24-04).
4. Done.

## Alternative flows

- 3a. Cancel.

## Error flows

- 2e. Beyond rights.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F24-04 Every integration in the AI assistant](../../business-rules/br-f24-04-every-integration-in-the-assistant.md)
- [BR-F24-16 Every integration shows its icon](../../business-rules/br-f24-16-every-integration-shows-its-icon.md)

## Entities

- [E-F24-09 Connector action](../../data/e-f24-09-connector-action.md)

## Permissions

Within rights.

## Notifications

- None.

## Audit events

Actions.

## AI involvement

Tools.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F24-14 Assistant actions](../../screens/04-run-and-control/s-f24-14-assistant-actions.md)

## Flowchart

See [FL-F24-04 Run and control](../../flows/fl-f24-04-run-and-control.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor O as Owner
  participant S as Assistant actions
  O->>S: Post in Element
  S-->>O: Confirm
```

## Acceptance criteria

1. **Given** a post **when** confirmed **then** sent.
2. **Given** beyond rights **when** asked **then** refused.
3. **Given** the action **when** shown **then** with the tool's icon.

## Non-functional notes

D408's targets ([Performance](../../../../05-non-functional/performance.md)): 95 % of screens within 1 second; lists
paged on the server, the first page within 1 second; reports within 5 seconds or in the background.

## Regulatory references

Data rules of the France country pack that connectors follow:
[CR-FR-049 Processors and transfers outside the EU](../../../../10-country-packs/france/data-protection/cr-fr-049-processors-and-transfers.md),
[CR-FR-195 Candidates' personal data](../../../../10-country-packs/france/data-protection/cr-fr-195-candidate-data.md),
[CR-FR-063 Consent for email and SMS marketing](../../../../10-country-packs/france/consumer/cr-fr-063-electronic-marketing-consent.md),
[CR-FR-170 Switching between cloud services (Data Act)](../../../../10-country-packs/france/digital/cr-fr-170-data-act-switching.md),
[CR-FR-051 Access and erasure requests](../../../../10-country-packs/france/data-protection/cr-fr-051-access-and-erasure.md),
[CR-FR-052 Personal data kept no longer than needed](../../../../10-country-packs/france/data-protection/cr-fr-052-storage-limitation.md).

## Related use cases

- [UC-F24-06 Use the suite's chat for notifications and the AI assistant](../02-office-suites/uc-f24-06-use-the-suite-s-chat-for-notifications-and-the-assistant.md)

## Open questions

None.

---

⬅️ [UC-F24-13 Import history once](../03-crm-and-ats/uc-f24-13-import-history-once.md) · ⬆️ [Up](README.md) ·
➡️ [UC-F24-15 Follow each connector's health and sync log](uc-f24-15-follow-each-connector-s-health-and-sync-log.md)
