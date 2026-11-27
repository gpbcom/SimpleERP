🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧭 [F21 Onboarding and module activation](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F21-04 Learn and improve](README.md) › 📝 UC-F21-13 Try with demo data, then clear it

# 📝 UC-F21-13 Try with demo data, then clear it

**Status:** ✅ specified

## Summary

The owner tries with demo data and clears it.

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Goal

Learn safely.

## Trigger

Choice.

## Frequency

Once.

## Preconditions

- None.

## Postconditions

- Success: cleared.
- Failure: none.

## Main flow

1. Load (S-F21-13).
2. Try.
3. Clear (BR-F21-08).
4. Real data only.

## Alternative flows

- 1a. Sector demo.

## Error flows

- 3e. Clear fails: retried.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F21-08 Demo data kept apart](../../business-rules/br-f21-08-demo-data-separate.md)

## Entities

- [E-F21-09 Demo data set](../../data/e-f21-09-demo-data-set.md)

## Permissions

Owner.

## Notifications

- None.

## Audit events

Loads.

## AI involvement

None.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F21-13 Demo data](../../screens/04-learn-and-improve/s-f21-13-demo-data.md)

## Flowchart

See [FL-F21-04 Learn and improve](../../flows/fl-f21-04-learn-and-improve.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor O as Owner
  participant S as Demo data
  O->>S: Load
  O->>S: Clear
```

## Acceptance criteria

1. **Given** demo **when** loaded **then** marked.
2. **Given** cleared **when** done **then** gone.
3. **Given** demo **when** exporting **then** never sent.

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

- [UC-F21-14 Follow the checklist and resume later](uc-f21-14-follow-the-checklist-and-resume-later.md)

## Open questions

None.

---

⬅️ [UC-F21-12 Ask the AI assistant at any step](../01-first-run/uc-f21-12-ask-the-assistant-at-any-step.md) ·
⬆️ [Up](README.md) ·
➡️ [UC-F21-14 Follow the checklist and resume later](uc-f21-14-follow-the-checklist-and-resume-later.md)
