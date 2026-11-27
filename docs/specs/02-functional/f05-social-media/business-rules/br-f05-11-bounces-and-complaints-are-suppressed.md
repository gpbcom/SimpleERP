🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📣 [F5 Social media and marketing](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F5-11 Bounces and complaints are suppressed

# 📏 BR-F5-11 Bounces and complaints are suppressed

**Status:** ✅ specified

## Statement

A hard bounce or a complaint suppresses the address for marketing at once; soft bounces after 3 in a row; a
complaint rate above the threshold pauses sending.

## Why

Sending to dead or angry addresses harms every later email.

## Examples

| Case | Result |
|---|---|
| Hard bounce | Suppressed |
| Complaint rate 0.5 % | Sending paused |

## Applies to

- [UC-F5-16 Keep emails delivered](../use-cases/06-audiences-consent-and-journeys/uc-f05-16-keep-emails-delivered.md)

## Exceptions

None.

## Configurable

The threshold (default: 0.3 %).

## Open questions

None.

---

⬅️ [BR-F5-10 Consent is proven and withdrawn at once](br-f05-10-consent-is-proven-and-withdrawn-at-once.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F5-12 One seat, one ticket, across every channel](br-f05-12-one-seat-one-ticket-across-every-channel.md)
