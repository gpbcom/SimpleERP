🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F19-04 Generated code runs in the sandbox

# 📏 BR-F19-04 Generated code runs in the sandbox

**Status:** ✅ specified

## Statement

Generation and tests run in an isolated sandbox with test data; never with the customer's live data or secrets.

## Why

See [D389](../../../06-decisions/f19-feature-factory/d389-generated-features-are-plugins.md).

## Examples

| Case | Result |
|---|---|
| Test needs a customer | A synthetic one is used |

## Applies to

Every F19 use case concerned.

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F19-03 The specification is agreed before the build](br-f19-03-spec-agreed-before-build.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F19-05 Checks, review and signing before install](br-f19-05-checks-review-and-signing.md)
