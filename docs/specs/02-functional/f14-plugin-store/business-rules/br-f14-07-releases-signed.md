🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🧰 [F14 Plugin store](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F14-07 Releases signed

# 📏 BR-F14-07 Releases signed

**Status:** ✅ specified

## Statement

Only releases signed after the security review install; a tampered package is refused.

## Why

See [D368](../../../06-decisions/f14-plugin-store/d368-plugin-store-coverage.md).

## Examples

| Case | Result |
|---|---|
| Signature mismatch | Install refused |

## Applies to

Every F14 use case concerned.

- [UC-F14-23 Take over an abandoned plugin](../use-cases/07-plugin-end-of-life/uc-f14-23-take-over-an-abandoned-plugin.md)
- [UC-F14-24 Publish to the beta channel](../use-cases/06-release-channels-and-rollback/uc-f14-24-publish-to-the-beta-channel.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F14-06 Automated checks before review](br-f14-06-automated-checks-before-review.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F14-08 Vulnerabilities handled by publishers](br-f14-08-vulnerabilities-handled-by-publishers.md)
