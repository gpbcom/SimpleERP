🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🚛 [SC07 Transport and logistics](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC07-18 A failed delivery gets a new slot or a relay point

# 📏 BR-SC07-18 A failed delivery gets a new slot or a relay point

**Status:** 🔄 waiting for the owner

## Statement

A parcel whose delivery failed always gets a next step: a new slot or a relay point chosen by the recipient, or after
the second failed attempt the default relay point. It never stays in the van without a decision, and each delivery ends
with a proof.

## Why

Parcels returned to the depot without a choice make the recipient call, pay twice and leave. The owner asked for the
last-mile courier ([D551](../../../06-decisions/sectors/d551-benchmark-gaps-sc07-transport.md)).

## Examples

| Case | Result |
|---|---|
| First attempt fails | the recipient chooses a new slot or a relay point |
| Second attempt fails, no choice | default relay point |
| Parcel left at the relay beyond the holding time | returned to the sender |
| Neighbour accepts with prior consent | delivered with the neighbour's name |
| Delivery with no proof | not Delivered |

## Applies to

- [UC-SC07-23](../use-cases/07-passengers-removals-courier-and-freight/uc-sc07-23-run-last-mile-rounds.md)
- [E-SC07-20 Parcel](../data/e-sc07-20-parcel.md)
- [E-SC07-16 Proof of delivery](../data/e-sc07-16-proof-of-delivery.md)

## Exceptions

None.

## Configurable

The holding time at the relay point and the default relay point, by the dispatcher.

## Open questions

None.

---

⬅️ [BR-SC07-17 The removal quote binds once signed](br-sc07-17-the-removal-quote-binds-once-signed.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-SC07-19 Customs entries carry the EORI number](br-sc07-19-customs-entries-carry-the-eori-number.md)
