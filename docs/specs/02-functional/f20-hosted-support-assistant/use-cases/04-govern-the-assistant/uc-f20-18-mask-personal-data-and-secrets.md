🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F20-04 Govern the AI assistant](README.md) › 📝 UC-F20-18 Mask personal data and secrets

# 📝 UC-F20-18 Mask personal data and secrets

**Status:** ✅ specified

## Summary

The hosting engineer sets, tests and applies masking rules.

## Personas

- [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md)

## Goal

No leaks.

## Trigger

Review.

## Frequency

Quarterly.

## Preconditions

- Rules.

## Postconditions

- Success: applied.
- Failure: none.

## Main flow

1. Open (S-F20-18).
2. Set rules.
3. Test.
4. Apply.

## Alternative flows

- 2a. Emails, keys.

## Error flows

- 3e. Test fails.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F20-07 Personal data and secrets masked](../../business-rules/br-f20-07-data-and-secrets-masked.md)
- [BR-F20-06 Screenshots with consent, masked](../../business-rules/br-f20-06-screenshots-with-consent-and-masking.md)

## Entities

- [E-F20-11 Assistant policy](../../data/e-f20-11-assistant-policy.md)
- [E-F20-03 Screenshot](../../data/e-f20-03-screenshot.md)

## Permissions

Engineer.

## Notifications

- None.

## Audit events

Rules.

## AI involvement

None.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F20-18 Masking](../../screens/04-govern-the-assistant/s-f20-18-masking.md)

## Flowchart

See [FL-F20-04 Govern the AI assistant](../../flows/fl-f20-04-govern-the-assistant.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor E as Engineer
  participant S as Masking
  E->>S: Mask IBANs
  S-->>E: Test passed
```

## Acceptance criteria

1. **Given** IBAN rule **when** tested **then** masked.
2. **Given** failing **when** tested **then** not applied.
3. **Given** applied **when** logs read **then** masked.

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

- [UC-F20-17 Control and audit the AI assistant's rights](uc-f20-17-control-and-audit-the-assistant-s-rights.md)

## Open questions

None.

---

⬅️ [UC-F20-17 Control and audit the AI assistant's rights](uc-f20-17-control-and-audit-the-assistant-s-rights.md) ·
⬆️ [Up](README.md) ·
➡️ [UC-F20-19 Choose a support plan and see its times](uc-f20-19-choose-a-support-plan-and-see-its-times.md)
