🏠 [Specs](../../README.md) › ⚙️ [Technical capabilities](../README.md) ›
🧗 [Technical challenges from the functional side](README.md) › 🌐 TC-19 Languages, currencies and countries

# 🌐 TC-19 Languages, currencies and countries

**Status:** ✅ listed for the technical interviews

## Challenge

Translate the product, the documents, the generated sites and the AI assistant's answers, handle several currencies and
companies, and let the community add country packs worldwide.

## Raised by

- [F6 Customers and sales](../../02-functional/f06-customers-and-sales/README.md)
- [F8 Accounting](../../02-functional/f08-accounting/README.md)
- [F18 Hosted websites and domains (hosted edition)](../../02-functional/f18-hosted-websites-and-domains/README.md)
- [T10 Translations and notifications](../t10-translations-and-notifications/README.md)
- [T11 Legal corpora](../t11-legal-corpora/README.md)

## Why it is hard

- Legal documents must stay exact in each language.
- Amounts must convert with the right rates and rounding.
- Community packs need review without slowing the release.

## Already decided

- [D293](../../06-decisions/country-packs/d293-capabilities-take-legal-rules-from-the-pack.md) Capabilities take legal
  rules from the country pack

## Options to weigh

- Translation catalogues with a review workflow.
- Money as exact decimals with currency everywhere.

## Settled in

- 19e Configuration ([chapter](../../../technical/architecture/configuration.md))
- 19l Release and versioning ([chapter](../../../technical/delivery/release-and-versioning.md))
- Then the technical capabilities:
  [T10 Translations and notifications](../t10-translations-and-notifications/README.md).

## Questions for the interview

- Which languages ship in the first version?
- Is consolidation across companies in scope?

---

⬅️ [TC-18 Install, upgrade and migrate without a consultant](tc-18-install-upgrade-and-migrate.md) ·
⬆️ [Up](README.md) · ➡️ [TC-20 Testing a very wide product](tc-20-testing-a-very-wide-product.md)
