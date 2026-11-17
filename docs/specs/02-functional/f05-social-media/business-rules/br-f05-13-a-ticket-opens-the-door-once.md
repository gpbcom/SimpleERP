🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📣 [F5 Social media and marketing](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F5-13 A ticket opens the door once

# 📏 BR-F5-13 A ticket opens the door once

**Status:** ✅ specified

## Statement

A ticket is valid once for its session (once per session for a pass); a second scan is refused with the time of the
first.

## Why

Copied tickets must not let two people in.

## Examples

| Case | Result |
|---|---|
| Second scan | Refused, first scan 20:05 |
| Pass, second session | Valid |

## Applies to

- [UC-F5-18 Sell at the box office and scan tickets](../use-cases/07-events-and-ticketing/uc-f05-18-sell-at-the-box-office-and-scan-tickets.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F5-12 One seat, one ticket, across every channel](br-f05-12-one-seat-one-ticket-across-every-channel.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F5-14](br-f05-14-forms-collect-only-what-they-declare-with-consent.md)
