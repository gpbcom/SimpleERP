🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔌 [F24 Integrations hub](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F24-02 Office suites](README.md) › 📝 UC-F24-08 Link projects, wiki, notes and tables

# 📝 UC-F24-08 Link projects, wiki, notes and tables

**Status:** ✅ specified

## Summary

Managers and office workers link projects, wiki, notes and tables.

## Personas

- [U02 Manager](../../../../01-users/personas/u02-manager.md)
- [U16 Office worker](../../../../01-users/personas/u16-office-worker.md)

## Goal

One view.

## Trigger

Project.

## Frequency

Weekly.

## Preconditions

- Suite.

## Postconditions

- Success: linked.
- Failure: none.

## Main flow

1. Link (S-F24-08).
2. Sync tasks or tables.
3. Open from the ERP.
4. Update.

## Alternative flows

- 2a. Read only.

## Error flows

- 2e. Rights.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F24-03 Office suites: full read and write](../../business-rules/br-f24-03-suites-full-read-write.md)

## Entities

- [E-F24-03 Suite component](../../data/e-f24-03-suite-component.md)

## Permissions

Within rights.

## Notifications

- None.

## Audit events

Links.

## AI involvement

None.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F24-08 Suite projects](../../screens/02-office-suites/s-f24-08-suite-projects.md)

## Flowchart

See [FL-F24-02 Office suites](../../flows/fl-f24-02-office-suites.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor M as Manager
  participant S as Suite projects
  M->>S: Link OpenProject
```

## Acceptance criteria

1. **Given** linked **when** tasks change **then** synced.
2. **Given** read only **when** chosen **then** no write.
3. **Given** rights **when** missing **then** refused.

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

- [UC-F24-04 Store and edit documents in the suite](uc-f24-04-store-and-edit-documents-in-the-suite.md)

## Open questions

None.

---

⬅️ [UC-F24-07 Start meetings from the suite's video](uc-f24-07-start-meetings-from-the-suite-s-video.md) ·
⬆️ [Up](README.md) ·
➡️ [UC-F24-09 Use the suites' full read and write API](uc-f24-09-use-the-suites-full-read-and-write-api.md)
