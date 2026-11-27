🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧭 [F21 Onboarding and module activation](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F21-01 First run](README.md) › 📝 UC-F21-01 Start the first-run guide

# 📝 UC-F21-01 Start the first-run guide

**Status:** ✅ specified

## Summary

The owner starts the first-run guide, chooses the pace (quick or complete) and begins; the guide can be left and
resumed.

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Goal

A guided start.

## Trigger

First sign-in.

## Frequency

Once.

## Preconditions

- Company created.

## Postconditions

- Success: guide started.
- Failure: none.

## Main flow

1. The owner signs in; the Welcome (S-F21-01) opens.
2. They choose the pace.
3. They start; the guide saves each answer (BR-F21-06).
4. They can leave and resume.

## Alternative flows

- 2a. Language chosen first (UC-F21-24).

## Error flows

- 3e. Leaves: resumes later.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F21-05 Plain words with examples](../../business-rules/br-f21-05-plain-words-with-examples.md)
- [BR-F21-06 Resume anywhere](../../business-rules/br-f21-06-resume-anywhere.md)

## Entities

- [E-F21-01 Onboarding progress](../../data/e-f21-01-onboarding-progress.md)

## Permissions

Owner, administrator.

## Notifications

- None.

## Audit events

Steps.

## AI involvement

Assistant at each step.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F21-01 Welcome](../../screens/01-first-run/s-f21-01-welcome.md)

## Flowchart

See [FL-F21-01 First run](../../flows/fl-f21-01-first-run.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor O as Owner
  participant S as Welcome
  O->>S: Quick pace
  S-->>O: Step 1
```

## Acceptance criteria

1. **Given** first sign-in **when** opened **then** welcome shows.
2. **Given** quick **when** chosen **then** required steps only.
3. **Given** left **when** back **then** resumes.

## Non-functional notes

D408's targets ([Performance](../../../../05-non-functional/performance.md)): 95 % of screens within 1 second; lists
paged on the server, the first page within 1 second; reports within 5 seconds or in the background.

## Regulatory references

Set-up rules of the France country pack:
[CR-FR-001 Company identifiers](../../../../10-country-packs/france/company/cr-fr-001-company-identifiers.md),
[CR-FR-016 Electronic invoicing](../../../../10-country-packs/france/invoicing/cr-fr-016-electronic-invoicing.md),
[CR-FR-005 Accounting entries file (FEC)](../../../../10-country-packs/france/accounting/cr-fr-005-fec-export.md),
[CR-FR-038 Personnel register](../../../../10-country-packs/france/labour/cr-fr-038-personnel-register.md),
[CR-FR-048 Record of processing activities](../../../../10-country-packs/france/data-protection/cr-fr-048-record-of-processing.md),
[CR-FR-069 Website legal notices](../../../../10-country-packs/france/consumer/cr-fr-069-website-legal-notices.md).

## Related use cases

- [UC-F21-02 Describe the company](uc-f21-02-describe-the-company.md)
- [UC-F21-24 Choose the company's and each user's language](uc-f21-24-choose-the-companys-and-each-users-language.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [UC-F21-02 Describe the company](uc-f21-02-describe-the-company.md)
