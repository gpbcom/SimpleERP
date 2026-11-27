🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F25-12 Security reports stay private

# 📏 BR-F25-12 Security reports stay private

**Status:** ✅ specified

## Statement

A report that may be a vulnerability in SimpleERP never becomes a public USER issue: the intake service sends it to a
private GitHub security advisory, seen by maintainers only; it is fixed, then published with its advisory and a CVE
(Security, the Cyber Resilience Act's duties of the publisher).

## Why

A public issue would show attackers the hole before the fix. See the review of 2026-11-12 (R20) and
[Security](../../../05-non-functional/security.md).

## Examples

| Case | Result |
|---|---|
| "Anyone can read other companies' invoices with this link" | A private advisory, no USER issue |
| A display bug | A USER issue as usual |

## Applies to

Every F25 use case concerned.

- [UC-F25-22 Handle a reported vulnerability under the CRA](../use-cases/06-vulnerability-handling/uc-f25-22-handle-a-reported-vulnerability-under-the-cra.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F25-11 Agents are metered and audited](br-f25-11-agents-metered-and-audited.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F25-13 Health data out of the agents' reach](br-f25-13-health-data-out-of-reach.md)
