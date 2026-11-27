🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F25-03 Bugs](README.md) › 📝 UC-F25-11 Create the PRODUCT ticket

# 📝 UC-F25-11 Create the PRODUCT ticket

**Status:** ✅ specified

## Summary

Agents create the PRODUCT ticket.

## Personas

- [U47 SimpleERP maintainer](../../../../01-users/personas/u47-simpleerp-maintainer.md)

## Goal

Tracked.

## Trigger

Fix.

## Frequency

Daily.

## Preconditions

- Fix.

## Postconditions

- Success: ticket.
- Failure: none.

## Main flow

1. Ticket (S-F25-11).
2. Link.
3. Label (BR-F25-07).
4. Backlog.

## Alternative flows

- 2a. Several tickets.

## Error flows

- 1e. None.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F25-07 Approval before Ready](../../business-rules/br-f25-07-approval-before-ready.md)

## Entities

- [E-F25-06 Agent ticket](../../data/e-f25-06-agent-ticket.md)

## Permissions

Agents.

## Notifications

- Maintainer.

## Audit events

Tickets.

## AI involvement

Agents.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F25-11 PRODUCT ticket](../../screens/03-bugs/s-f25-11-product-ticket.md)

## Flowchart

See [FL-F25-03 Bugs](../../flows/fl-f25-03-bugs.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  participant AG as Agents
  participant S as PRODUCT ticket
  AG->>S: ,314
```

## Acceptance criteria

1. **Given** a fix **when** ticketed **then** linked.
2. **Given** label **when** on **then** Backlog.
3. **Given** triage **when** done **then** targets.

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

- [UC-F25-12 Approve or refuse agents' tickets](../04-approve-and-govern/uc-f25-12-approve-or-refuse-agents-tickets.md)

## Open questions

None.

---

⬅️ [UC-F25-10](uc-f25-10-propose-the-fix-as-a-pull-request-tests-first.md) · ⬆️ [Up](README.md) ·
➡️ [UC-F25-12](../04-approve-and-govern/uc-f25-12-approve-or-refuse-agents-tickets.md)
