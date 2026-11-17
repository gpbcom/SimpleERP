🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏪 [F10 Point of sale (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F10-06 Offline, the till keeps selling

# 📏 BR-F10-06 Offline, the till keeps selling

**Status:** ✅ specified

## Statement

Without network, the till keeps selling, numbering and chaining its sales locally, and syncs on reconnect; a card
terminal that loses its link cancels the payment.

## Why

See [D295](../../../06-decisions/f10-point-of-sale/d295-pos-coverage.md).

## Examples

| Case | Result |
|---|---|
| 40 minutes offline | Sales synced, chain intact |
| Terminal link lost during payment | Payment cancelled, asked again |

## Applies to

Every F10 use case concerned.

- [UC-F5-18 Sell at the box office and scan tickets](../../f05-social-media/use-cases/07-events-and-ticketing/uc-f05-18-sell-at-the-box-office-and-scan-tickets.md)

## Exceptions

None.

## Configurable

A warning after 24 hours offline.

## Open questions

None.

---

⬅️ [BR-F10-05 Manager approval for sensitive till actions](br-f10-05-manager-pin-for-sensitive-actions.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F10-07 Paper receipts on request](br-f10-07-receipts-on-request.md)
