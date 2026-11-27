🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 📒 [F8 Accounting](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F8-30 Peppol serves only flows outside the French platforms

# 📏 BR-F8-30 Peppol serves only flows outside the French platforms

**Status:** ✅ specified

## Statement

Peppol carries only exchanges that are not already covered by the French e-invoicing platforms: an invoice between a
company in France and another company in France is never sent by Peppol, while an invoice to or from a company abroad
that is on Peppol may be.

## Why

French companies must exchange invoices through the approved platforms
([D454](../../../06-decisions/f08-accounting/d454-e-invoicing-platforms.md)); using Peppol for the same flow would
bypass the reporting those platforms carry. The owner asked for Peppol e-invoicing
([D527](../../../06-decisions/f08-accounting/d527-benchmark-gaps-f08-accounting.md)). The exact scope waits
for the France-pack rule.

## Examples

| Case | Result |
|---|---|
| An invoice to a customer in Belgium on Peppol | may go by Peppol |
| An invoice to a customer in France | goes through the approved platform, never Peppol |
| An invoice from a German supplier on Peppol | received by Peppol |
| A customer abroad not on Peppol | goes by email or portal |
| A French company's own invoice to its French subsidiary | through the French platform |

## Applies to

- [UC-F8-38](../use-cases/12-audit-leases-and-special-books/uc-f08-38-send-and-receive-invoices-through-peppol.md)
- [E-F8-42 Peppol participant](../data/e-f08-42-peppol-participant.md)
- [E-F6-05 Invoice](../../f06-customers-and-sales/data/e-f06-05-invoice.md)
- [E-F7-05 Supplier invoice](../../f07-purchasing-and-stock/data/e-f07-05-supplier-invoice.md)

## Exceptions

None.

## Configurable

Yes: the countries whose exchanges may use Peppol, by the administrator, within the rule.

## Open questions

None.

---

⬅️ [BR-F8-29 Leases follow the book's standard](br-f08-29-leases-follow-the-books-standard.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F8-31](br-f08-31-trips-outside-the-travel-policy-need-approval.md)
