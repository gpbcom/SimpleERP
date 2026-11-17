🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧭 [F21 Onboarding and module activation](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F21-02 Modules](README.md) › 📝 UC-F21-05 Understand a module's dependencies

# 📝 UC-F21-05 Understand a module's dependencies

**Status:** ✅ specified

## Summary

The administrator reads a module's dependencies in plain words and accepts both.

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Goal

No surprises.

## Trigger

Module chosen.

## Frequency

Occasional.

## Preconditions

- None.

## Postconditions

- Success: understood.
- Failure: none.

## Main flow

1. Open (S-F21-05).
2. See needs.
3. Read why.
4. Accept both.

## Alternative flows

- 4a. Decline.

## Error flows

- 4e. None.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F21-03 Dependencies explained, never hidden](../../business-rules/br-f21-03-dependencies-explained.md)

## Entities

- [E-F21-04 Module activation](../../data/e-f21-04-module-activation.md)
- [E-F21-05 Module dependency](../../data/e-f21-05-module-dependency.md)

## Permissions

Administrator.

## Notifications

- None.

## Audit events

None.

## AI involvement

Explains.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F21-05 Dependencies](../../screens/02-modules/s-f21-05-dependencies.md)

## Flowchart

See [FL-F21-02 Modules](../../flows/fl-f21-02-modules.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor A as Administrator
  participant S as Dependencies
  A->>S: F10
  S-->>A: Needs F6
```

## Acceptance criteria

1. **Given** F10 **when** opened **then** F6 shown.
2. **Given** accepted **when** done **then** both on.
3. **Given** declined **when** done **then** none.

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

- [UC-F21-04 Switch modules on in one click](uc-f21-04-switch-modules-on-in-one-click.md)

## Open questions

None.

---

⬅️ [UC-F21-04 Switch modules on in one click](uc-f21-04-switch-modules-on-in-one-click.md) · ⬆️ [Up](README.md) ·
➡️ [UC-F21-06 Switch a module off and keep its data](uc-f21-06-switch-a-module-off-and-keep-its-data.md)
