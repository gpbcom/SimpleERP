🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F20-02 Diagnose and fix](README.md) › 📝 UC-F20-07 Apply and verify the fix

# 📝 UC-F20-07 Apply and verify the fix

**Status:** ✅ specified

## Summary

The approved fix is applied, verified and the customer told.

## Personas

- [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md)

## Goal

Problem gone.

## Trigger

Approved.

## Frequency

Some requests.

## Preconditions

- Approved.

## Postconditions

- Success: verified.
- Failure: rolled back.

## Main flow

1. The fix is applied (S-F20-07).
2. The AI assistant verifies (BR-F20-05).
3. The customer is told.
4. The request closes.

## Alternative flows

- 2a. Partial: more steps.

## Error flows

- 2e. Not fixed: rolled back.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F20-04 Every fix needs a maintainer's yes](../../business-rules/br-f20-04-fixes-need-a-maintainer-yes.md)
- [BR-F20-05 Fixes are verified and reversible](../../business-rules/br-f20-05-fixes-are-verified-and-reversible.md)

## Entities

- [E-F20-06 Fix proposal](../../data/e-f20-06-fix-proposal.md)
- [E-F20-04 Diagnosis](../../data/e-f20-04-diagnosis.md)

## Permissions

Hosting engineer.

## Notifications

- Customer.

## Audit events

Fixes.

## AI involvement

Verification.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F20-07 Fix result](../../screens/02-diagnose-and-fix/s-f20-07-fix-result.md)

## Flowchart

See [FL-F20-02 Diagnose and fix](../../flows/fl-f20-02-diagnose-and-fix.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  participant A as AI assistant
  actor AD as Administrator
  A->>A: Apply, verify
  A-->>AD: Fixed
```

## Acceptance criteria

1. **Given** applied **when** verified **then** fixed.
2. **Given** not fixed **when** verified **then** rolled back.
3. **Given** fixed **when** told **then** closed.

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

- [UC-F20-16 Rate the help and review quality](../04-govern-the-assistant/uc-f20-16-rate-the-help-and-review-quality.md)

## Open questions

None.

---

⬅️ [UC-F20-06 Propose a fix for a maintainer's yes](uc-f20-06-propose-a-fix-for-a-maintainer-s-yes.md) ·
⬆️ [Up](README.md) · ➡️ [UC-F20-08 Escalate to an engineer](../03-incidents/uc-f20-08-escalate-to-an-engineer.md)
