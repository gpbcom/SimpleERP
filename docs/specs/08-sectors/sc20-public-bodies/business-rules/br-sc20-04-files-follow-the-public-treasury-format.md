🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏛️ [SC20 Public bodies](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC20-04 Files follow the public treasury format

# 📏 BR-SC20-04 Files follow the public treasury format

**Status:** ✅ specified, ⚖️ lawyer review before launch (D574)

## Statement

A batch is sent to the public accountant only in the national exchange format, after the format check, and contains only
signed orders. Each answer is applied to its order, and a rejection is shown with its reason.

## Why

A batch in the wrong format is not processed and payments are delayed
([D564](../../../06-decisions/sectors/d564-benchmark-gaps-sc20-public-bodies.md)). (⚖️ lawyer review before launch, D574) The
France-pack rule is still to write: to read the DGFiP's PES V2 exchange protocol and the list of supporting documents of
local public expenditure (CGCT D1617-19 and its annex).

## Examples

| Case | Result |
|---|---|
| Valid format | sent and followed |
| Format error | not sent, errors listed |
| Unsigned order in the batch | refused |
| Answer: paid | the order is Paid |
| Answer: rejected | the order is Rejected with the reason |

## Applies to

- [UC-SC20-04](../use-cases/01-public-accounting/uc-sc20-04-exchange-with-the-public-treasury.md)
- [E-SC20-04 Treasury exchange](../data/e-sc20-04-treasury-exchange.md)
- [E-SC20-04 Treasury exchange](../data/e-sc20-04-treasury-exchange.md)
- [E-SC20-03 Payment order](../data/e-sc20-03-payment-order.md)

## Exceptions

None.

## Configurable

The identification of the body and the certificate, set by the authorising officer.

## Open questions

None.

---

⬅️ [BR-SC20-03](br-sc20-03-orders-are-signed-by-the-authorising-officer.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC20-05 The procedure follows the thresholds](br-sc20-05-the-procedure-follows-the-thresholds.md)
