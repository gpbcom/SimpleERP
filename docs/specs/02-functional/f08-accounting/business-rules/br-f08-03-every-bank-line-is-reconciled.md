🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 📒 [F8 Accounting](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F8-03 Every bank line is reconciled

# 📏 BR-F8-03 Every bank line is reconciled

**Status:** ✅ specified

## Statement

Every bank line is matched to entries, by reconciliation models and the AI, or explained by a person; unmatched lines
stay visible in a suspense account until done; nothing is deleted.

## Why

See [D279](../../../06-decisions/f08-accounting/d279-bank-connections.md).

## Examples

| Case | Result |
|---|---|
| A transfer with the invoice number | Matched automatically |
| A card fee each month | A model writes the fee entry |
| An unknown transfer | Suspense, a person explains it |

## Applies to

Every F8 use case concerned.

- [UC-F8-21 Keep third-party client money](../use-cases/07-client-money-grants-and-non-profits/uc-f08-21-keep-third-party-client-money.md)

## Exceptions

None.

## Configurable

Yes: reconciliation models.

## Open questions

None.

---

⬅️ [BR-F8-02 Lock dates](br-f08-02-lock-dates.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F8-04 Filings need an accountant](br-f08-04-filings-need-an-accountant.md)
