🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F12-11 Production costed per order

# 📏 BR-F12-11 Production costed per order

**Status:** ✅ specified

## Statement

Each order's actual cost is its components, work centre time at its rate and subcontracting; variances to the standard
go to accounting; stock is valued at its production cost, fixed overheads allocated on the normal capacity, losses and
wastage and administrative costs (other than a dedicated structure's) left out, per
[CR-FR-081 Production cost of manufactured stock](../../../10-country-packs/france/accounting/cr-fr-081-production-cost-of-inventories.md).

## Why

See [D312](../../../06-decisions/f12-manufacturing/d312-manufacturing-coverage.md).

## Examples

| Case | Result |
|---|---|
| Standard 42.00, actual 44.10 | Variance 2.10 posted |

## Applies to

Every F12 use case concerned.

- [UC-F12-27 Value work in progress at month end](../use-cases/05-subcontracting-and-costs/uc-f12-27-value-work-in-progress-at-month-end.md)

## Exceptions

None.

## Configurable

Standard or actual costing per product.

## Open questions

None.

---

⬅️ [BR-F12-10 Maintenance frees the plan](br-f12-10-maintenance-frees-the-plan.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F12-12 Subcontracted stock stays ours](br-f12-12-subcontracted-stock-stays-ours.md)
