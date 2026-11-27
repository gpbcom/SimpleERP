🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🛍️ [SC02 Retail](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC02-07 Transfers in transit

# 📏 BR-SC02-07 Transfers in transit

**Status:** ✅ specified

## Statement

A transfer leaves the sending store's stock at once and stays in transit until received; differences at receipt are
recorded with a reason.

## Why

See [D320](../../../06-decisions/sectors/d320-retail-sector-coverage.md).

## Examples

| Case | Result |
|---|---|
| 10 sent, 9 received | 1 difference, reason asked |

## Applies to

Every SC02 use case concerned.

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-SC02-06 Replenish from min, max and sales](br-sc02-06-replenish-from-min-max-and-sales.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC02-08 One stock for all channels](br-sc02-08-one-stock-for-all-channels.md)
