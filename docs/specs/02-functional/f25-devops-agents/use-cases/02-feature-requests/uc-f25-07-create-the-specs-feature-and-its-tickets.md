🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F25-02 Feature requests](README.md) › 📝 UC-F25-07 Create the SPECS feature and its tickets

# 📝 UC-F25-07 Create the SPECS feature and its tickets

**Status:** ✅ specified

## Summary

Agents create the SPECS feature and its tickets with the approval label.

## Personas

- [U47 simple-ERP maintainer](../../../../01-users/personas/u47-simple-erp-maintainer.md)

## Goal

Planned work.

## Trigger

PR approved.

## Frequency

Weekly.

## Preconditions

- PR.

## Postconditions

- Success: tickets.
- Failure: none.

## Main flow

1. Feature (S-F25-07).
2. Tickets.
3. Approval label (BR-F25-07).
4. Backlog.

## Alternative flows

- 3a. Maintainer removes label.

## Error flows

- 2e. None.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F25-07 Approval before Ready](../../business-rules/br-f25-07-approval-before-ready.md)
- [BR-F25-06 Specs and code studied first](../../business-rules/br-f25-06-specs-and-code-studied-first.md)

## Entities

- [E-F25-03 USER ticket](../../data/e-f25-03-user-ticket.md)
- [E-F25-06 Agent ticket](../../data/e-f25-06-agent-ticket.md)
- [E-F25-15 SPECS feature](../../data/e-f25-15-specs-feature.md)

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

- [S-F25-07 SPECS feature](../../screens/02-feature-requests/s-f25-07-specs-feature.md)

## Flowchart

See [FL-F25-02 Feature requests](../../flows/fl-f25-02-feature-requests.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  participant AG as Agents
  participant S as SPECS feature
  AG->>S: Feature and 3 tickets
```

## Acceptance criteria

1. **Given** created **when** done **then** labelled.
2. **Given** in Backlog **when** label on **then** not Ready.
3. **Given** removed **when** maintainer **then** Ready.

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

⬅️ [UC-F25-06 Draft the spec changes as a pull request](uc-f25-06-draft-the-spec-changes-as-a-pull-request.md) ·
⬆️ [Up](README.md) · ➡️ [UC-F25-08](../03-bugs/uc-f25-08-reproduce-a-bug-on-the-managed-simple-erp.md)
