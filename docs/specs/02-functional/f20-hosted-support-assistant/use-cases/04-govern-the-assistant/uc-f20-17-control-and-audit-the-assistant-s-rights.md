🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F20-04 Govern the AI assistant](README.md) › 📝 UC-F20-17 Control and audit the AI assistant's rights

# 📝 UC-F20-17 Control and audit the AI assistant's rights

**Status:** ✅ specified

## Summary

The hosting engineer controls and audits the AI assistant's rights.

## Personas

- [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md)

## Goal

Least rights.

## Trigger

Review.

## Frequency

Quarterly.

## Preconditions

- Policy.

## Postconditions

- Success: changed.
- Failure: none.

## Main flow

1. Open (S-F20-17).
2. Review rights.
3. Change.
4. Audit.

## Alternative flows

- 3a. New fix kind.

## Error flows

- 3e. Secret access: refused.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F20-03 Only the customer's own namespace](../../business-rules/br-f20-03-own-namespace-only.md)
- [BR-F20-04 Every fix needs a maintainer's yes](../../business-rules/br-f20-04-fixes-need-a-maintainer-yes.md)

## Entities

- [E-F20-11 Assistant policy](../../data/e-f20-11-assistant-policy.md)

## Permissions

Engineer.

## Notifications

- None.

## Audit events

Changes.

## AI involvement

None.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F20-17 Assistant rights](../../screens/04-govern-the-assistant/s-f20-17-assistant-rights.md)

## Flowchart

See [FL-F20-04 Govern the AI assistant](../../flows/fl-f20-04-govern-the-assistant.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor E as Engineer
  participant S as Rights
  E->>S: Add restart
```

## Acceptance criteria

1. **Given** restart **when** added **then** allowed.
2. **Given** secrets **when** asked **then** refused.
3. **Given** audit **when** opened **then** all reads.

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

- [UC-F20-18 Mask personal data and secrets](uc-f20-18-mask-personal-data-and-secrets.md)

## Open questions

None.

---

⬅️ [UC-F20-16 Rate the help and review quality](uc-f20-16-rate-the-help-and-review-quality.md) · ⬆️ [Up](README.md) ·
➡️ [UC-F20-18 Mask personal data and secrets](uc-f20-18-mask-personal-data-and-secrets.md)
