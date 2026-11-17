🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔌 [F24 Integrations hub](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F24-02 Office suites](README.md) › 📝 UC-F24-04 Store and edit documents in the suite

# 📝 UC-F24-04 Store and edit documents in the suite

**Status:** ✅ specified

## Summary

Office workers store and edit documents in the suite from records.

## Personas

- [U16 Office worker](../../../../01-users/personas/u16-office-worker.md)
- [U01 Employee](../../../../01-users/personas/u01-employee.md)

## Goal

Documents in one place.

## Trigger

A document.

## Frequency

Daily.

## Preconditions

- Suite.

## Postconditions

- Success: stored.
- Failure: none.

## Main flow

1. Choose the folder (S-F24-04).
2. Save or open.
3. Edit together.
4. Version linked.

## Alternative flows

- 2a. From the phone.

## Error flows

- 2e. Rights: refused.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F24-03 Office suites: full read and write](../../business-rules/br-f24-03-suites-full-read-write.md)
- [BR-F24-04 Every integration in the AI assistant](../../business-rules/br-f24-04-every-integration-in-the-assistant.md)

## Entities

- [E-F24-03 Suite component](../../data/e-f24-03-suite-component.md)
- [E-F24-04 Linked document](../../data/e-f24-04-linked-document.md)

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

- [S-F24-04 Suite files](../../screens/02-office-suites/s-f24-04-suite-files.md)

## Flowchart

See [FL-F24-02 Office suites](../../flows/fl-f24-02-office-suites.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor W as Office worker
  participant S as Suite files
  W->>S: Save INV-0142
```

## Acceptance criteria

1. **Given** an invoice **when** saved **then** in the folder.
2. **Given** editing **when** together **then** version 3.
3. **Given** no rights **when** opened **then** refused.

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

- [UC-F24-08 Link projects, wiki, notes and tables](uc-f24-08-link-projects-wiki-notes-and-tables.md)

## Open questions

None.

---

⬅️ [UC-F24-03](uc-f24-03-sign-in-once-through-the-suite-s-identity-provider.md) · ⬆️ [Up](README.md) ·
➡️ [UC-F24-05 Sync mail, calendars and contacts](uc-f24-05-sync-mail-calendars-and-contacts.md)
