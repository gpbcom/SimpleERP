🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F20-03 Only the customer's own namespace

# 📏 BR-F20-03 Only the customer's own namespace

**Status:** ✅ specified

## Statement

The AI assistant reads only the customer's namespace through a read-only, audited service account; it never reads
another customer's resources or any secret value.

## Why

See [D393](../../../06-decisions/f20-hosted-support-assistant/d393-hosted-support-assistant-coverage.md).

## Examples

| Case | Result |
|---|---|
| Logs of a shared ingress | Filtered to this customer's lines |

## Applies to

Every F20 use case concerned.

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F20-02 Plain words first](br-f20-02-plain-words-first.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F20-04 Every fix needs a maintainer's yes](br-f20-04-fixes-need-a-maintainer-yes.md)
