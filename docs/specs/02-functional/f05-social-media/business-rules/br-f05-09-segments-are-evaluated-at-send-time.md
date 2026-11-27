🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📣 [F5 Social media and marketing](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F5-09 Segments are evaluated at send time

# 📏 BR-F5-09 Segments are evaluated at send time

**Status:** ✅ specified

## Statement

A dynamic segment is evaluated again at each send, and every send removes contacts without consent for its channel or on
the suppression list.

## Why

A segment saved last month must not reach someone who withdrew yesterday.

## Examples

| Case | Result |
|---|---|
| Contact withdrew consent yesterday | Not sent |
| New customer today | Included |

## Applies to

- [UC-F5-14 Build a segment of contacts](../use-cases/06-audiences-consent-and-journeys/uc-f05-14-build-a-segment-of-contacts.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F5-08 Marketing messages need consent](br-f05-08-marketing-needs-consent.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F5-10 Consent is proven and withdrawn at once](br-f05-10-consent-is-proven-and-withdrawn-at-once.md)
