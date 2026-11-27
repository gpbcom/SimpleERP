🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F20-04 Every fix needs a maintainer's yes

# 📏 BR-F20-04 Every fix needs a maintainer's yes

**Status:** ✅ specified

## Statement

A fix is proposed with its effect, risk and rollback, and applied only after a SimpleERP maintainer approves it; the
customer is told before and after.

## Why

See [D393](../../../06-decisions/f20-hosted-support-assistant/d393-hosted-support-assistant-coverage.md).

## Examples

| Case | Result |
|---|---|
| Restart proposed at night | Paged maintainer approves, applied |

## Applies to

Every F20 use case concerned.

## Exceptions

None.

## Configurable

Allowed fix kinds.

## Open questions

None.

---

⬅️ [BR-F20-03 Only the customer's own namespace](br-f20-03-own-namespace-only.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F20-05 Fixes are verified and reversible](br-f20-05-fixes-are-verified-and-reversible.md)
