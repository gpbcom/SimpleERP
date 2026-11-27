🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F19-22 Pledges are charged only when the goal is met

# 📏 BR-F19-22 Pledges are charged only when the goal is met

**Status:** ✅ specified, ⚖️ lawyer review before launch (D574)

## Statement

A pledge is a promise, not a payment: it is charged only when the pledges reach the goal by the deadline, all at once;
if the goal is not met by then, or the funding is closed, every pledge lapses and nothing is charged.

## Why

Customers must not pay for a feature that is never built, and a goal not met must cost nobody anything. The owner asked
for co-funded features ([D538](../../../06-decisions/f19-feature-factory/d538-benchmark-gaps-f19-feature-factory.md)).
(⚖️ lawyer review before launch, D574) The France-pack rule on VAT on pledges is still to write, with a tax adviser:
to read how [CR-FR-010 When VAT is due](../../../10-country-packs/france/tax-and-vat/cr-fr-010-vat-due-date.md) applies to a pledge
charged once the goal is met.

## Examples

| Case | Result |
|---|---|
| Goal 1,200 EUR, pledges 1,250 EUR on day 41 | charged on day 41, the extra shared back |
| Goal 1,200 EUR, pledges 900 EUR at the deadline | all lapse, nothing charged |
| A pledge withdrawn on day 20 | cancelled, no charge |
| A pledge after the deadline | refused |
| A pledger whose payment fails after the goal | retried once, then lapses |

## Applies to

- [UC-F19-29](../use-cases/07-catalogue-and-co-funding/uc-f19-29-co-fund-a-feature.md)
- [E-F19-18 Funding pledge](../data/e-f19-18-funding-pledge.md)
- [E-F19-02 Feature specification](../data/e-f19-02-feature-specification.md)
- [E-F19-01 Feature request](../data/e-f19-01-feature-request.md)

## Exceptions

None.

## Configurable

The deadline (60 days by default) and the lowest pledge, by the SimpleERP team.

## Open questions

None.

---

⬅️ [BR-F19-21 Fixed-price changes keep their price](br-f19-21-fixed-price-changes-keep-their-price.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F19-23 Maintenance covers upgrades within the plan](br-f19-23-maintenance-covers-upgrades-within-the-plan.md)
