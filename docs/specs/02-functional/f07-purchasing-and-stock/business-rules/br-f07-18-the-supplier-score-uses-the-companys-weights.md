🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📦 [F7 Purchasing and stock](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F7-18 The supplier score uses the company's weights

# 📏 BR-F7-18 The supplier score uses the company's weights

**Status:** ✅ specified

## Statement

A supplier's score combines on-time and in-full delivery, quality rejects, price variance and lead-time drift with the
weights the company sets, and shows only with enough receipts.

## Why

Each company weighs quality and delay differently.

## Examples

| Case | Result |
|---|---|
| Weights 40/30/20/10 | Score from them |
| 3 receipts | No score |

## Applies to

- [UC-F7-19 Follow supplier performance](../use-cases/07-supplier-agreements-and-performance/uc-f07-19-follow-supplier-performance.md)

## Exceptions

None.

## Configurable

Weights; minimum receipts (Proposed: 5).

## Open questions

None.

---

⬅️ [BR-F7-17 Carbon figures say how they were computed](br-f07-17-carbon-figures-say-how-they-were-computed.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F7-19 Consigned stock is never valued as own stock](br-f07-19-consigned-stock-is-never-valued-as-own-stock.md)
