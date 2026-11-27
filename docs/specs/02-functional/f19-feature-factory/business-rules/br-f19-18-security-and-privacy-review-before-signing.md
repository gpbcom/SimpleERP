🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F19-18 Security and privacy review before signing

# 📏 BR-F19-18 Security and privacy review before signing

**Status:** ✅ specified

## Statement

Before a generated feature is signed, the maintainer reviews its security (permissions, outside calls, secrets) and,
when it handles personal data, its privacy: data used, purpose, retention, access; a feature that needs an impact
assessment is signed only after the customer's assessment is approved (UC-F15-11).

## Why

Generated code must be safe (D476); personal data needs privacy by design
([CR-FR-050](../../../10-country-packs/france/data-protection/cr-fr-050-privacy-by-design.md)) and, when high risk, an
impact assessment.

## Examples

| Case | Result |
|---|---|
| Gate booking reading visitors' names and plates | passes after the review records data, purpose and a 30-day retention |
| Feature scoring employees | fails until the customer's impact assessment is approved (CR-FR-058) |
| Undeclared outside call | fails: rejected |

## Applies to

- [UC-F19-24 Review a feature's security and privacy](../use-cases/02-build-and-check/uc-f19-24-review-a-features-security-and-privacy.md)
- [UC-F19-06 Review and sign the feature](../use-cases/02-build-and-check/uc-f19-06-review-and-sign-the-feature.md)
- [UC-F19-13 Review a promotion for genericity and privacy](../use-cases/04-promote/uc-f19-13-review-a-promotion-for-genericity-and-privacy.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F19-17 Generated code is AGPL and stays usable](br-f19-17-generated-code-is-agpl-and-stays-usable.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F19-19 Factory billing posted to accounting](br-f19-19-factory-billing-posted-to-accounting.md)
