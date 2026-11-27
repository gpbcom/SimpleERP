🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F20-02 Diagnose and fix](README.md) › 📝 UC-F20-06 Propose a fix for a maintainer's yes

# 📝 UC-F20-06 Propose a fix for a maintainer's yes

**Status:** ✅ specified

## Summary

The AI assistant proposes a fix with effect, risk and rollback; a maintainer approves or refuses.

## Personas

- [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md)

## Goal

Safe fixes.

## Trigger

Cause known.

## Frequency

Some requests.

## Preconditions

- Fix kind allowed.

## Postconditions

- Success: approved.
- Failure: refused.

## Main flow

1. The AI assistant proposes (S-F20-06).
2. The customer is told.
3. A maintainer reviews (BR-F20-04).
4. Yes or no.

## Alternative flows

- 3a. Backup needed first.

## Error flows

- 4e. Refused: engineer takes over.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F20-04 Every fix needs a maintainer's yes](../../business-rules/br-f20-04-fixes-need-a-maintainer-yes.md)

## Entities

- [E-F20-06 Fix proposal](../../data/e-f20-06-fix-proposal.md)

## Permissions

Maintainer approves.

## Notifications

- Customer before and after.

## Audit events

Proposals.

## AI involvement

Proposal.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F20-06 Fix approval](../../screens/02-diagnose-and-fix/s-f20-06-fix-approval.md)

## Flowchart

See [FL-F20-02 Diagnose and fix](../../flows/fl-f20-02-diagnose-and-fix.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  participant A as AI assistant
  actor M as Maintainer
  A->>M: Raise memory, low risk, revert
  M->>A: Yes
```

## Acceptance criteria

1. **Given** a fix **when** proposed **then** risk and rollback shown.
2. **Given** approval **when** given **then** applied.
3. **Given** refusal **when** given **then** engineer.

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

- [UC-F20-07 Apply and verify the fix](uc-f20-07-apply-and-verify-the-fix.md)

## Open questions

None.

---

⬅️ [UC-F20-05 Explain the cause simply](uc-f20-05-explain-the-cause-simply.md) · ⬆️ [Up](README.md) ·
➡️ [UC-F20-07 Apply and verify the fix](uc-f20-07-apply-and-verify-the-fix.md)
