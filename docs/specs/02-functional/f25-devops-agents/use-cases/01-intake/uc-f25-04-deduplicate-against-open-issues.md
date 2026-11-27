🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F25-01 Intake](README.md) › 📝 UC-F25-04 Deduplicate against open issues

# 📝 UC-F25-04 Deduplicate against open issues

**Status:** ✅ specified

## Summary

Agents deduplicate against open issues.

## Personas

- [U47 SimpleERP maintainer](../../../../01-users/personas/u47-simpleerp-maintainer.md)

## Goal

No duplicates.

## Trigger

New request.

## Frequency

Daily.

## Preconditions

- Request.

## Postconditions

- Success: linked or filed.
- Failure: none.

## Main flow

1. Search (S-F25-04).
2. Compare.
3. Link as a voice (BR-F25-03).
4. Or file.

## Alternative flows

- 3a. Votes counted.

## Error flows

- 2e. Unsure: maintainer.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F25-03 Duplicates are merged](../../business-rules/br-f25-03-duplicates-merged.md)

## Entities

- [E-F25-02 USER feature](../../data/e-f25-02-user-feature.md)

## Permissions

Agents.

## Notifications

- Reporter.

## Audit events

Links.

## AI involvement

Agents.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F25-04 Duplicates](../../screens/01-intake/s-f25-04-duplicates.md)

## Flowchart

See [FL-F25-01 Intake](../../flows/fl-f25-01-intake.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  participant AG as Agents
  participant S as Duplicates
  AG->>S: Similar to ,313
```

## Acceptance criteria

1. **Given** similar **when** found **then** linked.
2. **Given** none **when** found **then** filed.
3. **Given** unsure **when** found **then** maintainer.

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

- [UC-F25-03 Open the USER feature with its ticket](uc-f25-03-open-the-user-feature-with-its-ticket.md)

## Open questions

None.

---

⬅️ [UC-F25-03 Open the USER feature with its ticket](uc-f25-03-open-the-user-feature-with-its-ticket.md) ·
⬆️ [Up](README.md) · ➡️ [UC-F25-05](../02-feature-requests/uc-f25-05-study-the-code-and-the-specs-for-a-feature.md)
