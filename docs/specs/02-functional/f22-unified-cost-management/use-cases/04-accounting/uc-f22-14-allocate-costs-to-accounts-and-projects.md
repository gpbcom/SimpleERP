🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💸 [F22 Unified platform cost management](../../README.md) › 📝 [Use cases](../README.md) ›
📝 [Use cases: FL-F22-04 Accounting](README.md) › 📝 UC-F22-14 Allocate costs to accounts and projects

# 📝 UC-F22-14 Allocate costs to accounts and projects

**Status:** ✅ specified

## Summary

Accounting allocates costs to accounts and projects by rules.

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Goal

Costs in books.

## Trigger

Month.

## Frequency

Monthly.

## Preconditions

- Rules.

## Postconditions

- Success: posted.
- Failure: unallocated.

## Main flow

1. Set rules (S-F22-14).
2. Apply (BR-F22-12).
3. Post.
4. Projects see margins.

## Alternative flows

- 1a. Self-hosted compute allocated too.

## Error flows

- 2e. No rule: unallocated.
- Any step: a service does not answer; the call is retried first (BR-F3-32), then the message follows the error pattern
  (D122) and what was typed stays on the screen.

## Business rules

- [BR-F22-12 Costs allocated to accounts](../../business-rules/br-f22-12-allocation-to-accounts.md)
- [BR-F22-01 Bills and allocations follow the country pack](../../business-rules/br-f22-01-costs-follow-the-country-pack.md)
- [BR-F22-15 Self-hosted compute has a cost](../../business-rules/br-f22-15-self-hosted-compute-has-a-cost.md)

## Entities

- [E-F22-09 Allocation rule](../../data/e-f22-09-allocation-rule.md)
- [E-F22-02 Metered call record](../../data/e-f22-02-metered-call-record.md)
- [E-F22-15 Compute machine](../../data/e-f22-15-compute-machine.md)

## Permissions

Accounting.

## Notifications

- None.

## Audit events

Rules.

## AI involvement

None.

## API, MCP and A2A exposure

Through T5 and T6 with the caller's rights (BR-F3-34).

## Screens

- [S-F22-14 Allocation rules](../../screens/04-accounting/s-f22-14-allocation-rules.md)

## Flowchart

See [FL-F22-04 Accounting](../../flows/fl-f22-04-accounting.md#flowchart).

## Sequence diagram

```mermaid
sequenceDiagram
  actor A as Accounting
  participant S as Allocation rules
  A->>S: Tag Durand to project Durand
```

## Acceptance criteria

1. **Given** tag Durand **when** applied **then** project Durand.
2. **Given** no rule **when** applied **then** unallocated.
3. **Given** compute **when** allocated **then** per feature.

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

- [UC-F22-03 See costs per department, project and client](uc-f22-03-see-costs-per-department-project-and-client.md)

## Open questions

None.

---

⬅️ [UC-F22-13 Match suppliers' invoices in accounting](uc-f22-13-match-suppliers-invoices-in-accounting.md) ·
⬆️ [Up](README.md) ·
➡️ [UC-F22-15 See the hosted quota and units billed](../05-billing/uc-f22-15-see-the-hosted-quota-and-units-billed.md)
