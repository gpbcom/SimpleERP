🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎓 [SC12 Education and training](../../README.md) ›
📝 [Use cases](../README.md) › 📝 [Use cases: FL-SC12-02 Enrol and fund](README.md) ›
📝 UC-SC12-05 Send invitations and needs assessments

# 📝 UC-SC12-05 Send invitations and needs assessments

**Status:** ✅ specified

## Summary

The training coordinator sends invitations and pre-course questionnaires and shares the answers with the trainer.

## Personas

- [U38 Training coordinator](../../../../01-users/personas/u38-training-coordinator.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Goal

Learners invited and their needs known.

## Trigger

A session approaches.

## Frequency

Per session.

## Preconditions

- The SC12 sector pack is installed for the company,
  [UC-F14-02](../../../../02-functional/f14-plugin-store/use-cases/01-find-and-install/uc-f14-02-install-a-plugin-or-sector-pack.md),
  and its users have their roles,
  [UC-F1-06](../../../../02-functional/f01-administration/use-cases/04-edit-a-role/uc-f01-06-edit-a-role-and-its-record-rules.md).

## Postconditions

- **Success:** answers are shared with the trainer.
- **Failed:** a reminder is sent.

## Main flow

1. Invitations and questionnaires go out on
   [S-SC12-05 Invitations](../../screens/02-enrol-and-fund/s-sc12-05-invitations.md).
2. Learners answer.
3. Answers go to the trainer.
4. Answers are kept as quality evidence ([BR-SC12-07](../../business-rules/br-sc12-07-quality-evidence-kept.md)).

## Alternative flows

- 2a. Adapted access needs: the coordinator adapts the session.

## Error flows

- 2e. No answer: a reminder is sent.
- 1e. No email: the employer is asked.
- Any step: a call to a service or an outside system fails: it is retried first
  ([BR-F3-32](../../../../02-functional/f03-assistant/business-rules/br-f03-32-retry-before-an-error.md)), then the
  error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed; what was
  typed is kept.

## Business rules

- [BR-SC12-07 Quality evidence kept](../../business-rules/br-sc12-07-quality-evidence-kept.md)

## Entities

- [E-SC12-03 Enrolment](../../data/e-sc12-03-enrolment.md)
- [E-F1-04 Invitation](../../../../02-functional/f01-administration/data/e-f01-04-invitation.md)

## Permissions

The training coordinator and customer roles; the record rules of their role and site apply,
[UC-F1-06](../../../../02-functional/f01-administration/use-cases/04-edit-a-role/uc-f01-06-edit-a-role-and-its-record-rules.md).

## Notifications

None beyond the in-app updates of the records concerned.

## Audit events

Every creation, change and state change of enrolment records, with who, when and the values before and after (T3).

## AI involvement

The AI assistant answers questions on the enrolment records of this use case, with links, and prepares them as drafts
the user confirms. It works within the user's rights,
[BR-F3-34](../../../../02-functional/f03-assistant/business-rules/br-f03-34-every-capability-is-reachable-from-the-assistant.md),
and never deletes or does anything irreversible without the user's confirmation,
[BR-F3-07](../../../../02-functional/f03-assistant/business-rules/br-f03-07-no-deletes-no-irreversible-acts.md).

## API, MCP and A2A exposure

Through the API and webhooks (T5) and the MCP and A2A gateway (T6), with the caller's rights,
[BR-F3-34](../../../../02-functional/f03-assistant/business-rules/br-f03-34-every-capability-is-reachable-from-the-assistant.md),
reading, creating and changing the records of this use case; nothing irreversible without a person's confirmation.

## Screens

- [S-SC12-05 Invitations](../../screens/02-enrol-and-fund/s-sc12-05-invitations.md)

## Flowchart

See [FL-SC12-02 Enrol and fund](../../flows/fl-sc12-02-enrol-and-fund.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor A1 as Training coordinator
  actor A2 as Customer
  participant P1 as Invitations
  A1->>P1: Send
  A2->>P1: Answer
  P1-->>A2: Answered
  A1->>P1: Share
  A1->>P1: Keep as evidence
  alt no answer
    P1-->>A2: A reminder is sent
  end
  alt no email
    P1-->>A1: The employer is asked
  end
```

## Acceptance criteria

1. **Given** the example training centre's 10 learners of S-41 **when** 9 answer **then** the trainer sees 9 answers.
2. **Given** J. Martin not answering **when** the reminder date comes **then** a reminder is sent.

## Non-functional notes

[D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)'s targets
([performance](../../../../05-non-functional/performance.md)): 95 % of screens within 1 second; lists paged on the
server, the first page within 1 second; reports within 5 seconds or in the background. WCAG 2.2 AA and RGAA
([D46](../../../../06-decisions/ux/d46-accessibility-standard.md)).

## Regulatory references

None specific to this use case; the sector's legal rules are listed in [SC12 regulatory](../../regulatory.md).

## Related use cases

- [UC-SC12-06 Sign attendance per half-day](../03-deliver-and-assess/uc-sc12-06-sign-attendance-per-half-day.md)

## Open questions

None.

---

⬅️ [UC-SC12-04 Get funding](uc-sc12-04-get-funding.md) · ⬆️ [Up](README.md) ·
➡️ [UC-SC12-06 Sign attendance per half-day](../03-deliver-and-assess/uc-sc12-06-sign-attendance-per-half-day.md)
