🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛒 [F6 Customers and sales](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F6-21 Call-offs never exceed the balance without approval

# 📏 BR-F6-21 Call-offs never exceed the balance without approval

**Status:** 🔄 waiting for the owner

## Statement

A call-off never takes a quantity or an amount above the contract's balance without sales' approval; the balance falls
with each confirmed call-off and rises when a call-off order is cancelled; after the validity no call-off is accepted.

## Why

A call-off above the balance sells at a price the company committed only for a quantity; the owner asked for frame
contracts ([D525](../../../06-decisions/f06-customers-and-sales/d525-benchmark-gaps-f06-customers-and-sales.md)).
[BR-F6-04 Large discounts need approval](br-f06-04-large-discounts-need-approval.md) already asks approval for large
discounts.

## Examples

| Case | Result |
|---|---|
| Balance 800, call-off 200 | accepted, balance 600 |
| Balance 100, call-off 150 | waits for approval |
| Approved at the list price | the 50 units above the balance use the list price |
| A call-off cancelled | its quantity returns to the balance |
| A call-off dated after the validity | refused |

## Applies to

- [UC-F6-29](../use-cases/10-partners-contracts-and-warranties/uc-f06-29-agree-a-frame-contract-and-call-off-orders.md)
- [E-F6-25 Frame contract](../data/e-f06-25-frame-contract.md)
- [E-F6-04 Order](../data/e-f06-04-order.md)

## Exceptions

None.

## Configurable

Yes: the price used above the balance (agreed or list), by sales, per contract.

## Open questions

None.

---

⬅️ [BR-F6-20 Identifiers are checked per scheme](br-f06-20-identifiers-are-checked-per-scheme.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F6-22](br-f06-22-terms-above-the-limit-need-a-recent-solvency-check.md)
