🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F19-02 A feature is a plugin, never a core change

# 📏 BR-F19-02 A feature is a plugin, never a core change

**Status:** ✅ specified

## Statement

A generated feature is a plugin on the public plugin API; anything the API lacks is added to the product by the
publisher, never reached around.

## Why

See [D389](../../../06-decisions/f19-feature-factory/d389-generated-features-are-plugins.md).

## Examples

| Case | Result |
|---|---|
| Feature needs a core table | Refused; an API extension proposed |

## Applies to

Every F19 use case concerned.

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F19-01 Prices and credits follow the country pack](br-f19-01-factory-follows-the-country-pack.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F19-03 The specification is agreed before the build](br-f19-03-spec-agreed-before-build.md)
