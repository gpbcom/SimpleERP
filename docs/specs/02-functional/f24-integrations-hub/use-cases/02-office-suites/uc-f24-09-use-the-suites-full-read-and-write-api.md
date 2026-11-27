🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔌 [F24 Integrations hub](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F24-02 Office suites](README.md) › 📝 UC-F24-09 Use the suites' full read and write API

# 📝 UC-F24-09 Use the suites' full read and write API

**Status:** ✅ specified

## Summary

The administrator enables the suites' full read and write API.

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Goal

Full use.

## Trigger

Need.

## Frequency

Rare.

## Preconditions

- Suite.

## Postconditions

- Success: enabled.
- Failure: none.

## Main flow

1. Enable components (S-F24-09).
2. Grant scopes (BR-F24-03).
3. Use in workflows.
4. Use in the AI assistant.

## Alternative flows

- 2a. Limited scopes.

## Error flows

- 2e. Refused.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F24-03 Office suites: full read and write](../../business-rules/br-f24-03-suites-full-read-write.md)
- [BR-F24-04 Every integration in the AI assistant](../../business-rules/br-f24-04-every-integration-in-the-assistant.md)

## Entities

- [E-F24-03 Suite component](../../data/e-f24-03-suite-component.md)

## Permissions

Administrator.

## Notifications

- None.

## Audit events

Scopes.

## AI involvement

Tools.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F24-09 Suite API](../../screens/02-office-suites/s-f24-09-suite-api.md)

## Flowchart

See [FL-F24-02 Office suites](../../flows/fl-f24-02-office-suites.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor A as Administrator
  participant S as Suite API
  A->>S: Nextcloud read and write
```

## Acceptance criteria

1. **Given** enabled **when** used **then** read and write.
2. **Given** limited **when** used **then** read only.
3. **Given** refused **when** granted **then** error.

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

- [UC-F24-03 Sign in once through the suite's identity provider](uc-f24-03-sign-in-once-through-the-suite-s-identity-provider.md)

## Open questions

None.

---

⬅️ [UC-F24-08 Link projects, wiki, notes and tables](uc-f24-08-link-projects-wiki-notes-and-tables.md) ·
⬆️ [Up](README.md) · ➡️ [UC-F24-10 Sync a CRM both ways](../03-crm-and-ats/uc-f24-10-sync-a-crm-both-ways.md)
