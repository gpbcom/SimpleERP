🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 📒 [F8 Accounting](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F8-13 Client money is segregated and never negative per client

# 📏 BR-F8-13 Client money is segregated and never negative per client

**Status:** ✅ specified

## Statement

Money held for clients sits on a segregated account; each client's ledger is never negative, and the account's balance
equals the sum of client balances every day.

## Why

Using one client's money for another is a breach of the agent's and lawyer's duties (CR-FR-139, CR-FR-151).

## Examples

| Case | Result |
|---|---|
| Pay 900 EUR, balance 742 EUR | Refused |
| Bank 184,100, ledgers 184,300 | Gap listed |

## Applies to

- [UC-F8-21 Keep third-party client money](../use-cases/07-client-money-grants-and-non-profits/uc-f08-21-keep-third-party-client-money.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F8-12 Spend follows card and approval limits](br-f08-12-spend-follows-limits.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F8-14 A grant is earned as its conditions are met](br-f08-14-a-grant-is-earned-as-its-conditions-are-met.md)
