🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧭 [F21 Onboarding and module activation](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F21-01 First run](README.md) › 📝 UC-F21-03 Pick a sector template

# 📝 UC-F21-03 Pick a sector template

**Status:** ✅ specified

## Summary

The owner picks a sector template, previews and applies it.

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Goal

Quick set-up.

## Trigger

Guide.

## Frequency

Once.

## Preconditions

- Profile.

## Postconditions

- Success: applied.
- Failure: none.

## Main flow

1. See templates (S-F21-03).
2. Preview.
3. See prices (BR-F21-10).
4. Apply.

## Alternative flows

- 1a. None for the sector.

## Error flows

- 4e. Fails: nothing changed.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F21-02 One click per module](../../business-rules/br-f21-02-one-click-per-module.md)
- [BR-F21-10 Hosted prices shown before switching on](../../business-rules/br-f21-10-hosted-prices-shown-first.md)

## Entities

- [E-F21-03 Set-up template](../../data/e-f21-03-set-up-template.md)

## Permissions

Owner.

## Notifications

- None.

## Audit events

Template.

## AI involvement

None.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F21-03 Templates](../../screens/01-first-run/s-f21-03-templates.md)

## Flowchart

See [FL-F21-01 First run](../../flows/fl-f21-01-first-run.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor O as Owner
  participant S as Templates
  O->>S: Home care
  O->>S: Apply
```

## Acceptance criteria

1. **Given** home care **when** applied **then** modules on.
2. **Given** paid modules **when** shown **then** prices.
3. **Given** failure **when** applied **then** nothing changed.

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

- [UC-F21-04 Switch modules on in one click](../02-modules/uc-f21-04-switch-modules-on-in-one-click.md)

## Open questions

None.

---

⬅️ [UC-F21-02 Describe the company](uc-f21-02-describe-the-company.md) · ⬆️ [Up](README.md) ·
➡️ [UC-F21-04 Switch modules on in one click](../02-modules/uc-f21-04-switch-modules-on-in-one-click.md)
