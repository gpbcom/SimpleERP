🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎭 [SC16 Events and culture](../../README.md) ›
📝 [Use cases](../README.md) › 📝 [Use cases: FL-SC16-03 People and partners](README.md) ›
📝 UC-SC16-08 Manage accreditations

# 📝 UC-SC16-08 Manage accreditations

**Status:** ✅ specified

## Summary

Press, staff, artists and partners request accreditations; the producer approves; badges give access by zone and day.

## Personas

- [U43 Event producer](../../../../01-users/personas/u43-event-producer.md)
- [U44 Box-office agent](../../../../01-users/personas/u44-box-office-agent.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Goal

Access controlled by zone.

## Trigger

A request.

## Frequency

Per event.

## Preconditions

- The SC16 sector pack is installed for the company,
  [UC-F14-02](../../../../02-functional/f14-plugin-store/use-cases/01-find-and-install/uc-f14-02-install-a-plugin-or-sector-pack.md),
  and its users have their roles,
  [UC-F1-06](../../../../02-functional/f01-administration/use-cases/04-edit-a-role/uc-f01-06-edit-a-role-and-its-record-rules.md).

## Postconditions

- **Success:** the badge is printed.
- **Failed:** the request is refused.

## Main flow

1. The person requests on [S-SC16-08 Accreditations](../../screens/03-people-and-partners/s-sc16-08-accreditations.md).
2. The producer approves with zones and days.
3. The badge is printed.
4. The badge is scanned at zones ([BR-SC16-11](../../business-rules/br-sc16-11-accreditations-by-zone.md)).

## Alternative flows

- 3a. A last-minute badge: it is printed on site.

## Error flows

- 4e. A wrong zone: access is refused.
- 2e. A request after the deadline: the producer decides.
- Any step: a call to a service or an outside system fails: it is retried first
  ([BR-F3-32](../../../../02-functional/f03-assistant/business-rules/br-f03-32-retry-before-an-error.md)), then the
  error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed; what was
  typed is kept.

## Business rules

- [BR-SC16-11 Accreditations by zone](../../business-rules/br-sc16-11-accreditations-by-zone.md)

## Entities

- [E-SC16-09 Accreditation](../../data/e-sc16-09-accreditation.md)

## Permissions

The event producer, box-office agent and customer roles; the record rules of their role and site apply,
[UC-F1-06](../../../../02-functional/f01-administration/use-cases/04-edit-a-role/uc-f01-06-edit-a-role-and-its-record-rules.md).

## Notifications

None beyond the in-app updates of the records concerned.

## Audit events

Every creation, change and state change of accreditation records, with who, when and the values before and after (T3).

## AI involvement

The AI assistant answers questions on the accreditation records of this use case, with links, and prepares them as
drafts the user confirms. It works within the user's rights,
[BR-F3-34](../../../../02-functional/f03-assistant/business-rules/br-f03-34-every-capability-is-reachable-from-the-assistant.md),
and never deletes or does anything irreversible without the user's confirmation,
[BR-F3-07](../../../../02-functional/f03-assistant/business-rules/br-f03-07-no-deletes-no-irreversible-acts.md).

## API, MCP and A2A exposure

Through the API and webhooks (T5) and the MCP and A2A gateway (T6), with the caller's rights,
[BR-F3-34](../../../../02-functional/f03-assistant/business-rules/br-f03-34-every-capability-is-reachable-from-the-assistant.md),
reading, creating and changing the records of this use case; nothing irreversible without a person's confirmation.

## Screens

- [S-SC16-08 Accreditations](../../screens/03-people-and-partners/s-sc16-08-accreditations.md)

## Flowchart

See [FL-SC16-03 People and partners](../../flows/fl-sc16-03-people-and-partners.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor A1 as Customer
  actor A2 as Event producer
  actor A3 as Box-office agent
  participant P1 as Accreditations
  A1->>P1: Request
  A2->>P1: Approve
  A3->>P1: Print the badge
  P1-->>A3: Printed
  A3->>P1: Scan
  alt a wrong zone
    P1-->>A3: Access is refused
  end
  alt a request after the deadline
    P1-->>A2: The producer decides
  end
```

## Acceptance criteria

1. **Given** the example venue's press badge for the foyer on 12 December **when** it is scanned at the foyer **then**
   access is granted.
2. **Given** a press badge for the foyer **when** it is scanned backstage **then** access is refused.

## Non-functional notes

[D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)'s targets
([performance](../../../../05-non-functional/performance.md)): 95 % of screens within 1 second; lists paged on the
server, the first page within 1 second; reports within 5 seconds or in the background. WCAG 2.2 AA and RGAA
([D46](../../../../06-decisions/ux/d46-accessibility-standard.md)).

## Regulatory references

None specific to this use case; the sector's legal rules are listed in [SC16 regulatory](../../regulatory.md).

## Related use cases

- [UC-SC16-09 Plan staff and volunteer shifts](uc-sc16-09-plan-staff-and-volunteer-shifts.md)

## Open questions

None.

---

⬅️ [UC-SC16-07 Run the box office on the day](../02-ticketing/uc-sc16-07-run-the-box-office-on-the-day.md) ·
⬆️ [Up](README.md) · ➡️ [UC-SC16-09 Plan staff and volunteer shifts](uc-sc16-09-plan-staff-and-volunteer-shifts.md)
