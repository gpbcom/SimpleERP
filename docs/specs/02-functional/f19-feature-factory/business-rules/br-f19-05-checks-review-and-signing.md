🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F19-05 Checks, review and signing before install

# 📏 BR-F19-05 Checks, review and signing before install

**Status:** ✅ specified

## Statement

A generated plugin passes the store's automated checks (tests, conventions, licences, vulnerabilities, declared
permissions), a check that no closed factory code is in it, and a maintainer's review and signature, before install.

## Why

See [D389](../../../06-decisions/f19-feature-factory/d389-generated-features-are-plugins.md).

## Examples

| Case | Result |
|---|---|
| Undeclared outside call | Rejected |

## Applies to

Every F19 use case concerned.

- [UC-F19-24 Review a feature's security and privacy](../use-cases/02-build-and-check/uc-f19-24-review-a-features-security-and-privacy.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F19-04 Generated code runs in the sandbox](br-f19-04-generated-code-runs-sandboxed.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F19-06 Tried on a copy first](br-f19-06-tried-on-a-copy-first.md)
