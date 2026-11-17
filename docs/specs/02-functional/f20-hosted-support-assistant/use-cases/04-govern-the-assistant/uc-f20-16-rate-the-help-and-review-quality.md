🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F20-04 Govern the AI assistant](README.md) › 📝 UC-F20-16 Rate the help and review quality

# 📝 UC-F20-16 Rate the help and review quality

**Status:** ✅ specified

## Summary

The administrator rates help and the engineers review quality by samples.

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md)

## Goal

Better help.

## Trigger

Request closed.

## Frequency

Each request.

## Preconditions

- Closed.

## Postconditions

- Success: rated.
- Failure: none.

## Main flow

1. Rate (S-F20-16).
2. Samples reviewed.
3. Improvements.
4. Tracked.

## Alternative flows

- 1a. Comment.

## Error flows

- 1e. No rating.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F20-02 Plain words first](../../business-rules/br-f20-02-plain-words-first.md)

## Entities

- [E-F20-10 Rating](../../data/e-f20-10-rating.md)

## Permissions

Administrator rates; engineers review.

## Notifications

- None.

## Audit events

Ratings.

## AI involvement

None.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F20-16 Quality](../../screens/04-govern-the-assistant/s-f20-16-quality.md)

## Flowchart

See [FL-F20-04 Govern the AI assistant](../../flows/fl-f20-04-govern-the-assistant.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor A as Administrator
  participant S as Quality
  A->>S: 5, quick
```

## Acceptance criteria

1. **Given** 5 **when** rated **then** stored.
2. **Given** samples **when** reviewed **then** noted.
3. **Given** low **when** rated **then** reviewed.

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

- [UC-F20-07 Apply and verify the fix](../02-diagnose-and-fix/uc-f20-07-apply-and-verify-the-fix.md)

## Open questions

None.

---

⬅️ [UC-F20-15 Handle a security incident or breach](../03-incidents/uc-f20-15-handle-a-security-incident-or-breach.md) ·
⬆️ [Up](README.md) ·
➡️ [UC-F20-17 Control and audit the AI assistant's rights](uc-f20-17-control-and-audit-the-assistant-s-rights.md)
