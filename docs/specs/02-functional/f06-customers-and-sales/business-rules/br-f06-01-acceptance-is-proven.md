🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛒 [F6 Customers and sales](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F6-01 Acceptance is proven

# 📏 BR-F6-01 Acceptance is proven

**Status:** ✅ specified

## Statement

A quote accepted by click keeps the accepting person's name, the date and time, the IP address and the exact version
accepted, with the words "good for agreement"; a document type set to e-signature is signed through the chosen provider,
its proof file kept with the quote; an accepted version can no longer change.

## Why

The company must be able to prove the agreement. See
[D254](../../../06-decisions/f06-customers-and-sales/d254-quote-acceptance.md).

Legal values from the France country pack:
[CR-FR-020 Proof of acceptance and e-signature](../../../10-country-packs/france/invoicing/cr-fr-020-electronic-acceptance-and-signature.md).

## Examples

| Case | Result |
|---|---|
| J. Durand clicks Accept on Q-2026-121 v2 | Accepted, proof kept, v2 frozen |
| A maintenance contract, type set to e-signature | Sent through Yousign; the signed file and its proof are kept |

## Applies to

Every F6 use case concerned.

## Exceptions

None.

## Configurable

Yes: the document types needing an e-signature, and the signature level.

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [BR-F6-02 No card number in simple-ERP](br-f06-02-no-card-number-in-simple-erp.md)
