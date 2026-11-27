🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F19-16 Nothing charged without an accepted feature

# 📏 BR-F19-16 Nothing charged without an accepted feature

**Status:** 🔄 waiting for the owner

## Statement

Billing starts only when the customer accepts the feature after its try-out; a feature refused after the change rounds
closes the order without charge, and an accepted feature made unusable by a defect not fixed within (Proposed) 10
business days is credited for that month by a credit note.

## Why

Customers pay for features that work (D476); billing starts at acceptance (BR-F19-09).

## Examples

| Case | Result |
|---|---|
| Feature refused after 3 change rounds (Proposed) | passes: order closed, no invoice |
| Defect reported on 2027-02-03, fixed 2027-02-10 | passes: no credit |
| Defect reported on 2027-02-03, not fixed by 2027-02-17 | passes: February credited, 300.00 EUR excluding VAT |

## Applies to

- [UC-F19-22 Refund when acceptance fails](../use-cases/06-delivery-and-refunds/uc-f19-22-refund-when-acceptance-fails.md)
- [UC-F19-07 Try the feature on a copy of the data](../use-cases/03-try-install-and-maintain/uc-f19-07-try-the-feature-on-a-copy-of-the-data.md)
- [UC-F19-10 Report a defect](../use-cases/03-try-install-and-maintain/uc-f19-10-report-a-defect.md)
- [UC-F19-19 Follow features, costs and credits](../use-cases/05-bill-and-credit/uc-f19-19-follow-features-costs-and-credits.md)

## Exceptions

A defect caused by the customer's own changes outside the feature is not credited.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F19-15 A delivery date is committed and kept](br-f19-15-a-delivery-date-is-committed-and-kept.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F19-17 Generated code is AGPL and stays usable](br-f19-17-generated-code-is-agpl-and-stays-usable.md)
