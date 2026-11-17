🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F20-02 Diagnose and fix](README.md) › 📝 UC-F20-14 Investigate slowness

# 📝 UC-F20-14 Investigate slowness

**Status:** ✅ specified

## Summary

The administrator reports slowness; the AI assistant measures and fixes or advises.

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Goal

Speed back.

## Trigger

Slowness.

## Frequency

Occasional.

## Preconditions

- Request.

## Postconditions

- Success: fixed or advised.
- Failure: escalated.

## Main flow

1. Report (S-F20-14).
2. Measure.
3. Find cause.
4. Fix or advise.

## Alternative flows

- 4a. Customer-side cause.

## Error flows

- 3e. Unknown: escalate.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F20-03 Only the customer's own namespace](../../business-rules/br-f20-03-own-namespace-only.md)
- [BR-F20-02 Plain words first](../../business-rules/br-f20-02-plain-words-first.md)

## Entities

- [E-F20-04 Diagnosis](../../data/e-f20-04-diagnosis.md)
- [E-F20-05 Cluster reading](../../data/e-f20-05-cluster-reading.md)

## Permissions

Administrator.

## Notifications

- Administrator.

## Audit events

Measures.

## AI involvement

Measures.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F20-14 Slowness](../../screens/02-diagnose-and-fix/s-f20-14-slowness.md)

## Flowchart

See [FL-F20-02 Diagnose and fix](../../flows/fl-f20-02-diagnose-and-fix.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor A as Administrator
  participant S as Slowness
  A->>S: Lists are slow
  S-->>A: Index missing, fixed
```

## Acceptance criteria

1. **Given** lists slow **when** measured **then** cause found.
2. **Given** fixed **when** verified **then** speed back.
3. **Given** unknown **when** found **then** escalated.

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

- [UC-F20-04 Diagnose on the cluster](uc-f20-04-diagnose-on-the-cluster.md)

## Open questions

None.

---

⬅️ [UC-F20-13 Restore data from a backup](uc-f20-13-restore-data-from-a-backup.md) · ⬆️ [Up](README.md) ·
➡️ [UC-F20-15 Handle a security incident or breach](../03-incidents/uc-f20-15-handle-a-security-incident-or-breach.md)
