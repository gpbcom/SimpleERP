🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-20 Outside call caps

# 📏 BR-F3-20 Outside call caps

**Status:** ✅ specified

## Statement

A connection may have a monthly call cap, and a cap per user; administrators are warned at 80 %; at 100 % the AI
assistant stops calling it until the next month or until an administrator raises the cap, and tells the user why,
following the error message pattern (D122).

## Why

Paid tools must not overspend. See [D172](../../../06-decisions/f03-assistant/d172-outside-call-caps.md).

## Examples

| Case | Result |
|---|---|
| Cap 1,000 calls, 800 used | Administrators warned |
| Cap reached | "The shipping tool has reached its monthly limit. Ask your administrator to raise it, or try again on 1 December." |
| No cap | Calls are counted and shown |

## Applies to

- [UC-F3-06](../use-cases/06-use-an-outside-tool/uc-f03-06-use-an-outside-tool-through-the-assistant.md)
- [UC-F3-18 See the cost before an expensive question](../use-cases/12-personal-cost-aware-and-learning/uc-f03-18-see-the-cost-before-an-expensive-question.md)

## Exceptions

None.

## Configurable

Yes: per connection and per user, by the administrator; no cap by default.

## Open questions

None.

---

⬅️ [BR-F3-19 Personal connections for allowed services](br-f03-19-personal-connections-for-allowed-services.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F3-21 Knowledge stays within its audience](br-f03-21-knowledge-stays-within-its-audience.md)
