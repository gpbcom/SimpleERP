🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F20-04 Govern the AI assistant](README.md) › 📝 UC-F20-20 Export a support conversation

# 📝 UC-F20-20 Export a support conversation

**Status:** ✅ specified

## Summary

The administrator exports a support conversation with its actions and screenshots.

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Goal

Keep records.

## Trigger

Need.

## Frequency

Rare.

## Preconditions

- Conversation.

## Postconditions

- Success: exported.
- Failure: none.

## Main flow

1. Open (S-F20-20).
2. Choose.
3. Export (BR-F20-12).
4. Download.

## Alternative flows

- 3a. PDF.

## Error flows

- 3e. Too large: zip.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F20-12 Conversations kept and exportable](../../business-rules/br-f20-12-conversations-kept-and-exportable.md)

## Entities

- [E-F20-01 Support request](../../data/e-f20-01-support-request.md)
- [E-F20-02 Message](../../data/e-f20-02-message.md)
- [E-F20-03 Screenshot](../../data/e-f20-03-screenshot.md)
- [E-F20-18 Support conversation export](../../data/e-f20-18-support-conversation-export.md)

## Permissions

Administrator.

## Notifications

- None.

## Audit events

Exports.

## AI involvement

None.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F20-20 Export](../../screens/04-govern-the-assistant/s-f20-20-export.md)

## Flowchart

See [FL-F20-04 Govern the AI assistant](../../flows/fl-f20-04-govern-the-assistant.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor A as Administrator
  participant S as Export
  A->>S: R-41
  S-->>A: PDF
```

## Acceptance criteria

1. **Given** R-41 **when** exported **then** PDF.
2. **Given** screenshots **when** exported **then** masked.
3. **Given** large **when** exported **then** zip.

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

- [UC-F20-09 Follow the request](../01-talk-it-through/uc-f20-09-follow-the-request.md)

## Open questions

None.

---

⬅️ [UC-F20-19 Choose a support plan and see its times](uc-f20-19-choose-a-support-plan-and-see-its-times.md) ·
⬆️ [Up](README.md) ·
➡️ [UC-F20-21 Announce planned maintenance](../05-maintenance-and-releases/uc-f20-21-announce-planned-maintenance.md)
