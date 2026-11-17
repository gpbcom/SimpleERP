🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💸 [F22 Unified platform cost management](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F22-04 Accounting](README.md) › 📝 UC-F22-03 See costs per department, project and client

# 📝 UC-F22-03 See costs per department, project and client

**Status:** ✅ specified

## Summary

Managers and accounting see costs per department, project and client by the allocation rules.

## Personas

- [U02 Manager](../../../../01-users/personas/u02-manager.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Goal

Costs in margins.

## Trigger

Review.

## Frequency

Monthly.

## Preconditions

- Rules.

## Postconditions

- Success: read.
- Failure: none.

## Main flow

1. Open (S-F22-03).
2. Choose the axis.
3. Read.
4. Export.

## Alternative flows

- 2a. Per client for re-billing.

## Error flows

- 2e. Unallocated: shown apart.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F22-12 Costs allocated to accounts](../../business-rules/br-f22-12-allocation-to-accounts.md)

## Entities

- [E-F22-02 Metered call record](../../data/e-f22-02-metered-call-record.md)
- [E-F22-09 Allocation rule](../../data/e-f22-09-allocation-rule.md)

## Permissions

Managers own; accounting all.

## Notifications

- None.

## Audit events

Exports.

## AI involvement

None.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F22-03 Cost allocation](../../screens/04-accounting/s-f22-03-cost-allocation.md)

## Flowchart

See [FL-F22-04 Accounting](../../flows/fl-f22-04-accounting.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor M as Manager
  participant S as Allocation
  M->>S: Project Durand
  S-->>M: 24 EUR
```

## Acceptance criteria

1. **Given** project Durand **when** read **then** 24.00 EUR.
2. **Given** unallocated **when** read **then** apart.
3. **Given** a manager **when** opening **then** own team.

## Non-functional notes

D408's targets ([Performance](../../../../05-non-functional/performance.md)): 95 % of screens within 1 second; lists
paged on the server, the first page within 1 second; reports within 5 seconds or in the background.

## Regulatory references

Billing and accounting rules of the France country pack:
[CR-FR-015 Mandatory invoice mentions](../../../../10-country-packs/france/invoicing/cr-fr-015-invoice-mandatory-mentions.md),
[CR-FR-016 Electronic invoicing](../../../../10-country-packs/france/invoicing/cr-fr-016-electronic-invoicing.md),
[CR-FR-100 VAT on services to clients abroad](../../../../10-country-packs/france/tax-and-vat/cr-fr-100-vat-on-services-abroad.md),
[CR-FR-002 Accounting records kept 10 years](../../../../10-country-packs/france/accounting/cr-fr-002-accounting-records-kept-ten-years.md),
[CR-FR-202 Price reductions on invoices](../../../../10-country-packs/france/invoicing/cr-fr-202-price-reductions-on-invoices.md),
[CR-FR-049 Processors and transfers outside the EU](../../../../10-country-packs/france/data-protection/cr-fr-049-processors-and-transfers.md).

## Related use cases

- [UC-F22-14 Allocate costs to accounts and projects](uc-f22-14-allocate-costs-to-accounts-and-projects.md)

## Open questions

None.

---

⬅️ [UC-F22-02](../01-see-and-set-up/uc-f22-02-see-costs-per-module-feature-and-provider.md) · ⬆️ [Up](README.md) ·
➡️ [UC-F22-04](../01-see-and-set-up/uc-f22-04-register-a-paid-provider-and-its-prices.md)
