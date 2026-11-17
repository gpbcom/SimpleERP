🏠 [Specs](../../README.md) › ⚙️ [Technical capabilities](../README.md) › 🕸️ [Connectors and scrapers](README.md) ›
🚨 Errors

# 🚨 Errors

**Status:** ✅ specified

## Error cases

A refused login, an expired token, a changed page, a rate limit, a budget spent, an action outside the allow-list.

## Handling

Retries with exponential backoff (BR-F3-32), then the request goes back to a human with the reason, following the error
message pattern (D122).

---

⬅️ [Operations](operations.md) · ⬆️ [Up](README.md) · ➡️ [Tests](tests.md)
