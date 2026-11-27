🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📦 [F7 Purchasing and stock](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F7-10 Third-party stock is reconciled daily

# 📏 BR-F7-10 Third-party stock is reconciled daily

**Status:** ✅ specified

## Statement

Stock held by a third-party warehouse is compared with its daily snapshot; differences open recount requests.

## Why

See [D305](../../../06-decisions/f07-purchasing-and-stock/d305-f7-benchmark-gaps.md).

## Examples

| Case | Result |
|---|---|
| 3PL shows 98, ERP 100 | Variance report, recount |

## Applies to

UC-F7-16

## Exceptions

None.

## Configurable

Tolerance.

## Open questions

None.

---

⬅️ [BR-F7-09 Orders between group companies mirror each other](br-f07-09-group-orders-mirror.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F7-11 Contract prices apply within their validity](br-f07-11-contract-prices-apply-within-their-validity.md)
