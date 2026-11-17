🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🩺 [SC09 Health practices](../../README.md) ›
📝 [Use cases](../README.md) › 📝 [Use cases: FL-SC09-02 Patient file and care](README.md) ›
📝 UC-SC09-03 Register patients and their insurance

# 📝 UC-SC09-03 Register patients and their insurance

**Status:** ✅ specified

## Summary

The medical secretary reads the patient's card, completes identity and complementary insurance, and records consents and
objections.

## Personas

- [U33 Medical secretary](../../../../01-users/personas/u33-medical-secretary.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Goal

A patient file ready for care and billing.

## Trigger

A first visit.

## Frequency

Daily.

## Preconditions

- The SC09 sector pack is installed for the company,
  [UC-F14-02](../../../../02-functional/f14-plugin-store/use-cases/01-find-and-install/uc-f14-02-install-a-plugin-or-sector-pack.md),
  and its users have their roles,
  [UC-F1-06](../../../../02-functional/f01-administration/use-cases/04-edit-a-role/uc-f01-06-edit-a-role-and-its-record-rules.md).

## Postconditions

- **Success:** the patient is registered with insurance and consents.
- **Failed:** the patient is registered by hand and flagged.

## Main flow

1. The secretary reads the insurance card on
   [S-SC09-03 Patient file](../../screens/02-patient-file-and-care/s-sc09-03-patient-file.md).
2. The secretary completes identity and complementary insurance.
3. The patient gives consents and objections.
4. The patient is registered.

## Alternative flows

- 1a. A digital card: the phone's card is read.

## Error flows

- 1e. The card unreadable: the identity is typed and flagged.
- 2e. A duplicate patient: the secretary merges.
- Any step: a call to a service or an outside system fails: it is retried first
  ([BR-F3-32](../../../../02-functional/f03-assistant/business-rules/br-f03-32-retry-before-an-error.md)), then the
  error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed; what was
  typed is kept.

## Business rules

- [BR-SC09-03 Secrecy by default](../../business-rules/br-sc09-03-secrecy-by-default.md)
- [BR-SC09-06 Third-party payment when due](../../business-rules/br-sc09-06-third-party-payment-when-due.md)

## Entities

- [E-SC09-02 Patient](../../data/e-sc09-02-patient.md)

## Permissions

The medical secretary and customer roles; the record rules of their role and site apply,
[UC-F1-06](../../../../02-functional/f01-administration/use-cases/04-edit-a-role/uc-f01-06-edit-a-role-and-its-record-rules.md).

## Notifications

None beyond the in-app updates of the records concerned.

## Audit events

Every creation, change and state change of patient records, with who, when and the values before and after (T3).

## AI involvement

The AI assistant answers questions on the patient records of this use case, with links, and prepares them as drafts the
user confirms. It works within the user's rights,
[BR-F3-34](../../../../02-functional/f03-assistant/business-rules/br-f03-34-every-capability-is-reachable-from-the-assistant.md),
and never deletes or does anything irreversible without the user's confirmation,
[BR-F3-07](../../../../02-functional/f03-assistant/business-rules/br-f03-07-no-deletes-no-irreversible-acts.md).

## API, MCP and A2A exposure

Through the API and webhooks (T5) and the MCP and A2A gateway (T6), with the caller's rights,
[BR-F3-34](../../../../02-functional/f03-assistant/business-rules/br-f03-34-every-capability-is-reachable-from-the-assistant.md),
reading, creating and changing the records of this use case; nothing irreversible without a person's confirmation.

## Screens

- [S-SC09-03 Patient file](../../screens/02-patient-file-and-care/s-sc09-03-patient-file.md)

## Flowchart

See [FL-SC09-02 Patient file and care](../../flows/fl-sc09-02-patient-file-and-care.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor A1 as Medical secretary
  actor A2 as Customer
  participant P1 as Patient file
  A1->>P1: Read the card
  A1->>P1: Complete
  A2->>P1: Record consents
  A1->>P1: Save
  P1-->>A1: Registered
  alt the card unreadable
    P1-->>A1: The identity is typed and flagged
  end
  alt a duplicate patient
    P1-->>A1: The secretary merges
  end
```

## Acceptance criteria

1. **Given** the example health centre's J. Martin, born 1980, general scheme **when** he is registered **then** his
   consent to SMS and objection to the national record are recorded.
2. **Given** J. Martin's card damaged **when** it is read **then** the identity is typed and flagged.

## Non-functional notes

[D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)'s targets
([performance](../../../../05-non-functional/performance.md)): 95 % of screens within 1 second; lists paged on the
server, the first page within 1 second; reports within 5 seconds or in the background. WCAG 2.2 AA and RGAA
([D46](../../../../06-decisions/ux/d46-accessibility-standard.md)).

## Regulatory references

None specific to this use case; the sector's legal rules are listed in [SC09 regulatory](../../regulatory.md).

## Related use cases

- [UC-SC09-04 Keep the clinical record](uc-sc09-04-keep-the-clinical-record.md)

## Open questions

None.

---

⬅️ [UC-SC09-02](../01-appointments/uc-sc09-02-remind-patients-and-handle-no-shows.md) · ⬆️ [Up](README.md) ·
➡️ [UC-SC09-04 Keep the clinical record](uc-sc09-04-keep-the-clinical-record.md)
