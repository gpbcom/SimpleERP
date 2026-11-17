🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧭 [F21 Onboarding and module activation](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F21-03 Team and data](README.md) › 📝 UC-F21-09 Import existing data

# 📝 UC-F21-09 Import existing data

**Status:** ✅ specified

## Summary

The administrator imports existing data from any file with a mapping; named tools have a ready one (UC-F21-21).

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Goal

Data in.

## Trigger

Guide.

## Frequency

Once.

## Preconditions

- Modules on.

## Postconditions

- Success: imported.
- Failure: errors listed.

## Main flow

1. Upload (S-F21-09).
2. Map columns.
3. Preview errors.
4. Import.

## Alternative flows

- 1a. Named tool: UC-F21-21.

## Error flows

- 3e. Errors: listed.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F21-05 Plain words with examples](../../business-rules/br-f21-05-plain-words-with-examples.md)
- [BR-F21-09 The AI assistant at every step](../../business-rules/br-f21-09-assistant-at-every-step.md)
- [BR-F21-12 Migrations read the old tool's known formats](../../business-rules/br-f21-12-migrations-read-the-old-tools-known-formats.md)

## Entities

- [E-F21-07 Import job](../../data/e-f21-07-import-job.md)
- [E-F21-14 Migration source](../../data/e-f21-14-migration-source.md)

## Permissions

Administrator.

## Notifications

- When done.

## Audit events

Imports.

## AI involvement

Maps.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F21-09 Import](../../screens/03-team-and-data/s-f21-09-import.md)

## Flowchart

See [FL-F21-03 Team and data](../../flows/fl-f21-03-team-and-data.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor A as Administrator
  participant S as Import
  A->>S: customers.csv
  S-->>A: 412, 0 errors
```

## Acceptance criteria

1. **Given** 412 rows **when** imported **then** 412.
2. **Given** errors **when** previewed **then** listed.
3. **Given** EBP **when** chosen **then** ready mapping.

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

- [UC-F21-21 Migrate from a named tool](../05-migration-from-another-tool/uc-f21-21-migrate-from-a-named-tool.md)

## Open questions

None.

---

⬅️ [UC-F21-08 Invite users and give roles](uc-f21-08-invite-users-and-give-roles.md) · ⬆️ [Up](README.md) ·
➡️ [UC-F21-10 Connect email, calendar and bank](uc-f21-10-connect-email-calendar-and-bank.md)
