🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏭 [SC05 Manufacturing](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC05-18 Production starts only after the proof is approved

# 📏 BR-SC05-18 Production starts only after the proof is approved

**Status:** ✅ specified

## Statement

Production of a personalised product starts only when its proof is Approved by the customer. A change after approval
creates a new proof that must be approved again, and the earlier one is Superseded.

## Why

A batch made from an unapproved or outdated proof is the usual source of rejected personalised goods and of disputes
that the company loses. The owner asked for personalisation
([D549](../../../06-decisions/sectors/d549-benchmark-gaps-sc05-manufacturing.md)).

## Examples

| Case | Result |
|---|---|
| Proof Approved by the customer | the manufacturing order can be released |
| Proof Sent, no answer | no release |
| Customer changes the colour after approval | a new version is sent and the old one is Superseded |
| Proof Expired after 30 days | sent again before production |
| Dispute after delivery | the Approved proof is the reference |

## Applies to

- [UC-SC05-18](../use-cases/06-excise-refurbishment-and-cutting/uc-sc05-18-personalise-products-for-customers.md)
- [E-SC05-17 Proof](../data/e-sc05-17-proof.md)
- [E-F12-04](../../../02-functional/f12-manufacturing/data/e-f12-04-manufacturing-order.md)

## Exceptions

None.

## Configurable

The reminder delay and the expiry delay of a proof, by sales.

## Open questions

None.

---

⬅️ [BR-SC05-17 Every refurbished unit is graded and tested](br-sc05-17-every-refurbished-unit-is-graded-and-tested.md) ·
⬆️ [Up](README.md) · ➡️ [BR-SC05-19](br-sc05-19-remnants-above-the-minimum-size-go-back-to-stock.md)
