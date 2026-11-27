🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › ⚖️ [SC11 Professional firms](../../README.md) ›
📝 [Use cases](../README.md) › 📝 [Use cases: FL-SC11-04 Deadlines and filings](README.md) ›
📝 UC-SC11-08 Follow deadlines, hearings and limitation periods

# 📝 UC-SC11-08 Follow deadlines, hearings and limitation periods

**Status:** ✅ specified

## Summary

The professional's assistant enters deadlines; reminders go to their owner; a missed reminder escalates.

## Personas

- [U37 Professional's assistant](../../../../01-users/personas/u37-assistant.md)
- [U36 Professional](../../../../01-users/personas/u36-professional.md)

## Goal

No deadline missed.

## Trigger

A deadline arises.

## Frequency

Daily.

## Preconditions

- The SC11 sector pack is installed for the company,
  [UC-F14-02](../../../../02-functional/f14-plugin-store/use-cases/01-find-and-install/uc-f14-02-install-a-plugin-or-sector-pack.md),
  and its users have their roles,
  [UC-F1-06](../../../../02-functional/f01-administration/use-cases/04-edit-a-role/uc-f01-06-edit-a-role-and-its-record-rules.md).

## Postconditions

- **Success:** the deadline is done.
- **Failed:** the partner is alerted.

## Main flow

1. The professional's assistant enters it on
   [S-SC11-08 Deadlines](../../screens/04-deadlines-and-filings/s-sc11-08-deadlines.md) with its owner.
2. Reminders go out ([BR-SC11-07](../../business-rules/br-sc11-07-deadlines-never-silent.md)).
3. The professional does the act.
4. The deadline is done.

## Alternative flows

- 1a. A court calendar import: hearings come through the connector (T12).

## Error flows

- 2e. A missed reminder: the partner is alerted.
- 1e. No owner: it is refused.
- Any step: a call to a service or an outside system fails: it is retried first
  ([BR-F3-32](../../../../02-functional/f03-assistant/business-rules/br-f03-32-retry-before-an-error.md)), then the
  error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed; what was
  typed is kept.

## Business rules

- [BR-SC11-07 Deadlines never silent](../../business-rules/br-sc11-07-deadlines-never-silent.md)

## Entities

- [E-SC11-09 Deadline](../../data/e-sc11-09-deadline.md)

## Permissions

The professional's assistant and professional roles; the record rules of their role and site apply,
[UC-F1-06](../../../../02-functional/f01-administration/use-cases/04-edit-a-role/uc-f01-06-edit-a-role-and-its-record-rules.md).

## Notifications

None beyond the in-app updates of the records concerned.

## Audit events

Every creation, change and state change of deadline records, with who, when and the values before and after (T3).

## AI involvement

The AI assistant answers questions on the deadline records of this use case, with links, and prepares them as drafts the
user confirms. It works within the user's rights,
[BR-F3-34](../../../../02-functional/f03-assistant/business-rules/br-f03-34-every-capability-is-reachable-from-the-assistant.md),
and never deletes or does anything irreversible without the user's confirmation,
[BR-F3-07](../../../../02-functional/f03-assistant/business-rules/br-f03-07-no-deletes-no-irreversible-acts.md).

## API, MCP and A2A exposure

Through the API and webhooks (T5) and the MCP and A2A gateway (T6), with the caller's rights,
[BR-F3-34](../../../../02-functional/f03-assistant/business-rules/br-f03-34-every-capability-is-reachable-from-the-assistant.md),
reading, creating and changing the records of this use case; nothing irreversible without a person's confirmation.

## Screens

- [S-SC11-08 Deadlines](../../screens/04-deadlines-and-filings/s-sc11-08-deadlines.md)

## Flowchart

See [FL-SC11-04 Deadlines and filings](../../flows/fl-sc11-04-deadlines-and-filings.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor A1 as Professional's assistant
  actor A2 as Professional
  participant P1 as Deadlines
  A1->>P1: Enter
  A1->>P1: Remind
  A2->>P1: Do
  A2->>P1: Done
  P1-->>A2: Done
  alt a missed reminder
    P1-->>A1: The partner is alerted
  end
  alt no owner
    P1-->>A1: It is refused
  end
```

## Acceptance criteria

1. **Given** the example firm's appeal on M-221 due 20 November **when** it is entered **then** reminders are planned
   for its owner.
2. **Given** the appeal of 20 November not acknowledged **when** the reminder passes **then** the partner is alerted.

## Non-functional notes

[D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)'s targets
([performance](../../../../05-non-functional/performance.md)): 95 % of screens within 1 second; lists paged on the
server, the first page within 1 second; reports within 5 seconds or in the background. WCAG 2.2 AA and RGAA
([D46](../../../../06-decisions/ux/d46-accessibility-standard.md)).

## Regulatory references

None specific to this use case; the sector's legal rules are listed in [SC11 regulatory](../../regulatory.md).

## Related use cases

- [UC-SC11-11 Run an accountant's client portfolio and tax calendar](uc-sc11-11-run-an-accountant-s-client-portfolio-and-tax-calendar.md)

## Open questions

None.

---

⬅️ [UC-SC11-07](../03-time-and-billing/uc-sc11-07-hold-client-funds-on-trust-accounts.md) · ⬆️ [Up](README.md) ·
➡️ [UC-SC11-09](../02-matters-and-documents/uc-sc11-09-manage-documents-with-versions-and-e-signature.md)
