🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔌 [F24 Integrations hub](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F24-03 CRM and ATS](README.md) › 📝 UC-F24-11 Sync an ATS both ways

# 📝 UC-F24-11 Sync an ATS both ways

**Status:** ✅ specified

## Summary

HR syncs an ATS both ways, or imports from HR SaaS (UC-F24-23).

## Personas

- [U06 HR](../../../../01-users/personas/u06-hr.md)

## Goal

One candidate base.

## Trigger

ATS used.

## Frequency

Once.

## Preconditions

- ATS.

## Postconditions

- Success: synced.
- Failure: errors.

## Main flow

1. Connect (S-F24-11).
2. Map.
3. Sync.
4. Candidates' data rules (BR-F24-01).

## Alternative flows

- 1a. HR SaaS (UC-F24-23).

## Error flows

- 3e. Conflict.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F24-05 The default 50 ATS and CRM](../../business-rules/br-f24-05-the-default-fifty.md)
- [BR-F24-07 Two-way sync with an owner per field](../../business-rules/br-f24-07-two-way-sync-with-ownership.md)
- [BR-F24-01 Synced data follows the country pack](../../business-rules/br-f24-01-connectors-follow-the-country-pack.md)

## Entities

- [E-F24-06 Sync job](../../data/e-f24-06-sync-job.md)
- [E-F24-07 Field mapping](../../data/e-f24-07-field-mapping.md)

## Permissions

HR.

## Notifications

- Errors.

## Audit events

Syncs.

## AI involvement

None.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F24-11 ATS sync](../../screens/03-crm-and-ats/s-f24-11-ats-sync.md)

## Flowchart

See [FL-F24-03 CRM and ATS](../../flows/fl-f24-03-crm-and-ats.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor H as HR
  participant S as ATS sync
  H->>S: Teamtailor
```

## Acceptance criteria

1. **Given** connected **when** synced **then** candidates.
2. **Given** conflict **when** found **then** shown.
3. **Given** retention **when** passed **then** erased.

## Non-functional notes

D408's targets ([Performance](../../../../05-non-functional/performance.md)): 95 % of screens within 1 second; lists
paged on the server, the first page within 1 second; reports within 5 seconds or in the background.

## Regulatory references

Data rules of the France country pack that connectors follow:
[CR-FR-049 Processors and transfers outside the EU](../../../../10-country-packs/france/data-protection/cr-fr-049-processors-and-transfers.md),
[CR-FR-195 Candidates' personal data](../../../../10-country-packs/france/data-protection/cr-fr-195-candidate-data.md),
[CR-FR-063 Consent for email and SMS marketing](../../../../10-country-packs/france/consumer/cr-fr-063-electronic-marketing-consent.md),
[CR-FR-170 Switching between cloud services (Data Act)](../../../../10-country-packs/france/digital/cr-fr-170-data-act-switching.md),
[CR-FR-051 Access and erasure requests](../../../../10-country-packs/france/data-protection/cr-fr-051-access-and-erasure.md),
[CR-FR-052 Personal data kept no longer than needed](../../../../10-country-packs/france/data-protection/cr-fr-052-storage-limitation.md).

## Related use cases

- [UC-F24-23 Bring HR and payroll data from Silae, PayFit or Lucca](../06-business-tools/uc-f24-23-bring-hr-and-payroll-data-from-silae-payfit-or-lucca.md)

## Open questions

None.

---

⬅️ [UC-F24-10 Sync a CRM both ways](uc-f24-10-sync-a-crm-both-ways.md) · ⬆️ [Up](README.md) ·
➡️ [UC-F24-12 Map fields and resolve conflicts](uc-f24-12-map-fields-and-resolve-conflicts.md)
