🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 💻 [SC14 IT and software](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC14-19 Sponsor tiers are invoiced like subscriptions

# 📏 BR-SC14-19 Sponsor tiers are invoiced like subscriptions

**Status:** ✅ specified

## Statement

A sponsorship is invoiced as a subscription: each period at its tier's price, with the same invoice numbering, payment
collection and dunning steps. Its benefits are active only while it is Active and are withdrawn when it lapses.

## Why

Sponsors that are invoiced by hand are forgotten and sponsors that stay listed after they stop paying are a grievance.
The owner asked for open-source sponsorship
([D558](../../../06-decisions/sectors/d558-benchmark-gaps-sc14-it-and-software.md)). The invoices follow the
France pack's numbering and mentions (CR-FR-014, CR-FR-015); a payment for visibility is a service with VAT, not a
gift.

## Examples

| Case | Result |
|---|---|
| Silver at 100.00 EUR a month | an invoice of 100.00 EUR each month |
| Payment unpaid after the last reminder | the sponsorship lapses and the logo is withdrawn |
| Tier changed in the period | applies at the next period |
| Sponsor who did not consent to be listed | not in the public list |
| Gift without a counterpart | handled as a donation, not as a sponsorship |

## Applies to

- [UC-SC14-25](../use-cases/07-hardware-licences-and-tax-credits/uc-sc14-25-accept-open-source-sponsorship.md)
- [E-SC14-20 Sponsorship](../data/e-sc14-20-sponsorship.md)
- [E-F6-07](../../../02-functional/f06-customers-and-sales/data/e-f06-07-subscription-contract.md)

## Exceptions

None.

## Configurable

The tiers, their benefits and periods, by the owner.

## Open questions

None.

---

⬅️ [BR-SC14-18 Claimed hours have timesheet evidence](br-sc14-18-claimed-hours-have-timesheet-evidence.md) ·
⬆️ [Up](README.md)
