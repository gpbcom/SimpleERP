🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 📦 [SC15 Wholesale and distribution](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC15-05 EDI orders validated

# 📏 BR-SC15-05 EDI orders validated

**Status:** ✅ specified

## Statement

An EDI order is checked against the agreement's prices and the catalogue before it is accepted; differences are sent
back.

## Why

See [D359](../../../06-decisions/sectors/d359-wholesale-sector-coverage.md).

## Examples

| Case | Result |
|---|---|
| Price differs | Order held, answer with the agreed price |

## Applies to

Every SC15 use case concerned.

## Exceptions

None.

## Configurable

Tolerance.

## Open questions

None.

---

⬅️ [BR-SC15-04 Yearly agreement on time](br-sc15-04-yearly-agreement-on-time.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC15-06 Offline orders synced](br-sc15-06-offline-orders-synced.md)
